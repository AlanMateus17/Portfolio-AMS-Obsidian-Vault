#!/usr/bin/env python3
"""Biblioteca: os livros do seu estudo e o registro de tudo o que você lê.

Cada livro aponta para os assuntos do mapa de estudo (github.com/AlanMateus17/mapa-de-estudo) em que ele é usado.
Cada leitura vira uma linha no seu vault (07-estudo-e-carreira/leituras.md): data, livro, trecho, minutos,
assunto e uma nota com as SUAS palavras. Página de livro nunca entra aqui, nem vai para a IA.

    python3 tools/biblioteca/biblioteca.py lista                 # todos os livros, por situação
    python3 tools/biblioteca/biblioteca.py para 0.4              # o que ler (e o que falta comprar) para um assunto
    python3 tools/biblioteca/biblioteca.py comprar               # o que comprar, na ordem em que vai precisar
    python3 tools/biblioteca/biblioteca.py ler petzold-codigo --trecho "cap. 1-3" --min 50 --assunto 0.4 \
        --nota "o que eu entendi, com as minhas palavras"
    python3 tools/biblioteca/biblioteca.py lidos [--livro ID]    # o seu registro de leituras
    python3 tools/biblioteca/biblioteca.py marcar petzold-codigo tenho
    python3 tools/biblioteca/biblioteca.py docs [--check]        # docs/biblioteca.md a partir de data/biblioteca.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "biblioteca.json"
DOC = RAIZ / "docs" / "biblioteca.md"
SITUACOES = ("tenho", "comprar", "gratis-online", "emprestado")
NOTA_MAX = 600  # nota longa demais costuma ser texto copiado do livro
CABECALHO = ("# Registro de leituras\n\n"
             "Gerado por `just livros ler`. Cada linha é uma sessão de leitura; a nota é escrita com as suas palavras "
             "(nunca texto copiado do livro).\n\n"
             "| Data | Livro | Trecho | Min | Assunto | Nota |\n|---|---|---|---|---|---|\n")


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def registro() -> Path:
    return vault() / "07-estudo-e-carreira" / "leituras.md"


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def salvar(d: dict) -> None:
    DADOS.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def chave_etapa(etapa: str) -> tuple:
    """Ordena 0.2 < 0.10 < 1.1 < 7.14 < H1.6 < inglês."""
    m = re.fullmatch(r"(H)?(\d+)\.(\d+)", etapa)
    if not m:
        return (2, 0, 0, etapa)
    return (1 if m.group(1) else 0, int(m.group(2)), int(m.group(3)), etapa)


def validar(d: dict) -> list[str]:
    erros, ids = [], set()
    for li in d["livros"]:
        if li["id"] in ids:
            erros.append(f"id repetido: {li['id']}")
        ids.add(li["id"])
        if li["situacao"] not in SITUACOES:
            erros.append(f"{li['id']}: situação inválida {li['situacao']}")
        if li["situacao"] == "gratis-online" and not li.get("onde"):
            erros.append(f"{li['id']}: livro grátis precisa do campo 'onde'")
        if not li.get("assuntos"):
            erros.append(f"{li['id']}: sem assunto do mapa")
    return erros


def achar(d: dict, livro_id: str) -> dict:
    for li in d["livros"]:
        if li["id"] == livro_id:
            return li
    raise SystemExit(f"livro {livro_id} não existe (veja: just livros lista)")


def para_assunto(d: dict, etapa: str) -> list[tuple[dict, str]]:
    return [(li, a["trecho"]) for li in d["livros"] for a in li["assuntos"] if a["etapa"] == etapa]


def a_comprar(d: dict) -> list[tuple[dict, str]]:
    itens = []
    for li in d["livros"]:
        if li["situacao"] == "comprar":
            primeira = min((a["etapa"] for a in li["assuntos"]), key=chave_etapa)
            itens.append((li, primeira))
    return sorted(itens, key=lambda x: chave_etapa(x[1]))


def linha_tabela(s: str) -> str:
    return s.replace("|", "/").replace("\n", " ").strip()


def registrar(livro: dict, trecho: str, minutos: int, assunto: str, nota: str, hoje: date | None = None) -> Path:
    if len(nota) > NOTA_MAX:
        raise SystemExit(f"nota com {len(nota)} caracteres (máximo {NOTA_MAX}): escreva com as suas palavras, "
                         "em poucas frases; texto do livro não entra no registro")
    if minutos <= 0:
        raise SystemExit("minutos precisa ser maior que zero")
    arq = registro()
    arq.parent.mkdir(parents=True, exist_ok=True)
    if not arq.exists():
        arq.write_text(CABECALHO, encoding="utf-8")
    dia = (hoje or date.today()).isoformat()
    with arq.open("a", encoding="utf-8") as f:
        f.write(f"| {dia} | {linha_tabela(livro['titulo'])} | {linha_tabela(trecho)} | {minutos} | "
                f"{linha_tabela(assunto)} | {linha_tabela(nota)} |\n")
    return arq


def ler_registro(livro_titulo: str | None = None) -> list[list[str]]:
    arq = registro()
    if not arq.exists():
        return []
    linhas = []
    for ln in arq.read_text(encoding="utf-8").splitlines():
        if not ln.startswith("| 2"):
            continue
        cols = [c.strip() for c in ln.strip("|").split("|")]
        if livro_titulo is None or cols[1] == linha_tabela(livro_titulo):
            linhas.append(cols)
    return linhas


def gerar_doc(d: dict) -> str:
    rot = {"tenho": "✅ tenho", "comprar": "🛒 comprar", "gratis-online": "🌐 grátis online", "emprestado": "📚 emprestado"}
    out = ["<!-- GERADO por tools/biblioteca/biblioteca.py docs a partir de data/biblioteca.json. -->",
           "# Biblioteca", "",
           f"Os livros do estudo e os assuntos do [mapa de estudo]({d['mapa']}) em que cada um entra. "
           "Comandos: `just livros para ETAPA`, `just livros comprar`, `just livros ler ...`, `just livros lidos`.", "",
           f"> {d['regra']}", "",
           "## O que comprar, na ordem em que vai precisar", ""]
    compras = a_comprar(d)
    if compras:
        out += ["| Primeiro assunto | Livro | Autor | Edição | ISBN |", "|---|---|---|---|---|"]
        out += [f"| {etapa} | {li['titulo']} | {li['autor']} | {li.get('editora', '')} | {li.get('isbn', '')} |"
                for li, etapa in compras]
    else:
        out.append("Nada para comprar agora.")
    out += ["", "## Todos os livros", "", "| Livro | Autor | Situação | Assuntos |", "|---|---|---|---|"]
    for li in sorted(d["livros"], key=lambda x: chave_etapa(min((a["etapa"] for a in x["assuntos"]), key=chave_etapa))):
        etapas = ", ".join(sorted({a["etapa"] for a in li["assuntos"]}, key=chave_etapa))
        titulo = f"[{li['titulo']}]({li['onde'].split(' ')[0]})" if li.get("onde", "").startswith("http") else li["titulo"]
        out.append(f"| {titulo} | {li['autor']} | {rot[li['situacao']]} | {etapas} |")
    out += ["", "## Registro de leituras", "",
            "Cada sessão fica no vault, em `07-estudo-e-carreira/leituras.md` (`just livros ler`). "
            "Depois de ler: protocolo de fim de bloco, 1 a 3 cartões no Anki e `just professor fechar ID MINUTOS` "
            "quando a leitura for parte de um módulo.", ""]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("lista")
    p = s.add_parser("para"); p.add_argument("etapa")
    s.add_parser("comprar")
    p = s.add_parser("ler")
    p.add_argument("livro"); p.add_argument("--trecho", required=True); p.add_argument("--min", type=int, required=True)
    p.add_argument("--assunto", required=True); p.add_argument("--nota", required=True)
    p = s.add_parser("lidos"); p.add_argument("--livro")
    p = s.add_parser("marcar"); p.add_argument("livro"); p.add_argument("situacao", choices=SITUACOES)
    s.add_parser("docs").add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    d = carregar()
    erros = validar(d)
    if erros:
        print("\n".join(erros), file=sys.stderr)
        return 1

    if args.cmd == "lista":
        for sit in SITUACOES:
            grupo = [li for li in d["livros"] if li["situacao"] == sit]
            if grupo:
                print(f"\n{sit}:")
                for li in grupo:
                    print(f"  {li['id']:<36} {li['titulo']} ({li['autor']})")
    elif args.cmd == "para":
        itens = para_assunto(d, args.etapa)
        if not itens:
            print(f"Nenhum livro cadastrado para o assunto {args.etapa}: use a documentação oficial citada no arquivo do assunto.")
        for li, trecho in itens:
            falta = "  ← COMPRAR antes" if li["situacao"] == "comprar" else ""
            print(f"{li['titulo']} ({li['autor']}) · {li['situacao']} · {trecho}{falta}")
    elif args.cmd == "comprar":
        for li, etapa in a_comprar(d):
            isbn = f" · ISBN {li['isbn']}" if li.get("isbn") else ""
            print(f"[{etapa}] {li['titulo']} ({li['autor']}){isbn}")
    elif args.cmd == "ler":
        li = achar(d, args.livro)
        arq = registrar(li, args.trecho, args.min, args.assunto, args.nota)
        print(f"Registrado em {arq}.\nAgora: feche o livro, reconstrua de cabeça, faça 1 a 3 cartões no Anki"
              " e, se a leitura fazia parte de um módulo, `just professor fechar ID MINUTOS`.")
    elif args.cmd == "lidos":
        titulo = achar(d, args.livro)["titulo"] if args.livro else None
        linhas = ler_registro(titulo)
        for c in linhas:
            print(" · ".join(c[:5]) + f"\n    {c[5]}")
        print(f"{len(linhas)} sessões, {sum(int(c[3]) for c in linhas)} minutos.")
    elif args.cmd == "marcar":
        achar(d, args.livro)["situacao"] = args.situacao
        salvar(d)
        DOC.write_text(gerar_doc(d) + "\n", encoding="utf-8")
        print(f"{args.livro}: {args.situacao}")
    elif args.cmd == "docs":
        novo = gerar_doc(d) + "\n"
        if args.check:
            if not DOC.exists() or DOC.read_text(encoding="utf-8") != novo:
                print("docs/biblioteca.md desatualizado: rode just docs", file=sys.stderr)
                return 1
            print("biblioteca em dia")
        else:
            DOC.write_text(novo, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
