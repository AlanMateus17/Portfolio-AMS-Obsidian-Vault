#!/usr/bin/env python3
"""Motor de decisão da empresa solo: montar, colar ou construir, e o pacote de contexto para o arquiteto.

Dois comandos (os mesmos de `just triagem` e `just arquiteto`):

    python3 tools/triagem/triagem.py triar "atendimento no WhatsApp com fila para clientes"
    python3 tools/triagem/triagem.py triar "rebalancear a carteira ARCA" --nucleo sim
    python3 tools/triagem/triagem.py triar "agenda online" --nucleo nao --integra nao --adr docs/adr
    python3 tools/triagem/triagem.py arquitetar "módulo de aporte do AM Rendara" > pacote.md

triar: procura no setup (data/ecossistema.json) o que já resolve o pedido, olha a lista do que ficou
de fora (data/mapa.json) e decide uma de três opções:
    A · SUBIR PRONTO   já existe ferramenta aberta no setup e não precisa mexer nos sistemas AM (< 30 min)
    B · COLAR          existe o pronto, mas precisa ligar aos sistemas AM ou a outra ferramenta (< 1 dia, n8n ou API)
    C · CONSTRUIR      é o núcleo que gera faturamento: programa no Aura, na stack fixa, com ADR (2 a 3 dias por fatia)
Com --adr PASTA, grava o rascunho do ADR da decisão na próxima numeração da pasta.

arquitetar: não chama IA nenhuma. Monta um pacote curto (stack fixa, regras, o que já existe, o que foi
recusado e o pedido) para colar no Claude ou mandar por `claude -p`. Pedir o pacote pronto gasta menos
token do que o Claude descobrir tudo isso sozinho lendo o repositório.

Regra das 4 horas: programando há mais de 4 horas sem nada visível (tela ou teste passando)? Pare e
rode a triagem de novo: quase sempre a resposta era A ou B.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import nucleo as nuc  # noqa: E402


def _nucleo():
    """Banco do núcleo, se já foi iniciado (nucleo.py iniciar). Sem banco, a triagem funciona igual."""
    if os.environ.get("NUCLEO_DESLIGADO"):
        return None
    try:
        return nuc.abrir(criar=False)
    except Exception:  # noqa: BLE001 - o núcleo é opcional aqui
        return None
ECO = RAIZ / "data" / "ecossistema.json"
MAPA = RAIZ / "data" / "mapa.json"
ADRS = RAIZ / "docs" / "adr"

STACK = ("Sistemas AM: C#/.NET 10 · ASP.NET Core (Controllers) · Clean Architecture + DDD · PostgreSQL · Redis · "
         "SignalR · Next.js com TypeScript, Tailwind e Zod · Docker · GitHub Actions · deploy em VM pelo Kamal (ADR 0005). "
         "Fora do Aura, a melhor ferramenta para o trabalho (ADR 0007): Astro (sites), SvelteKit + PocketBase (MVP), "
         "Go (CLIs), Rust (firmware), Python (dados e IA). Cada sistema: apps/web, apps/api, packages/core, packages/db.")
REGRAS = [
    "Uma ferramenta por função: se o setup já tem uma que faz isso, use-a; ferramenta nova só com ADR.",
    "Infraestrutura é container pronto e aberto; só a regra de negócio que gera faturamento é programada.",
    "Contrato da API é o OpenAPI (Scalar); o front valida o que chega com Zod (ADR 0006).",
    "Mudar de stack só com medição (hyperfine, k6) mostrando o gargalo.",
    "Segredos só no KeePassXC; nunca no repositório, nem cifrados.",
    "Nada publicado, enviado ou cobrado em nome do Alan sem aprovação.",
]
INSTRUCAO = ("Responda seco, sem saudação nem resumo: (1) o que do setup já resolve parte disso, (2) a arquitetura mínima "
             "na stack fixa, (3) os contratos (rotas OpenAPI e esquemas Zod do front), (4) as 3 armadilhas de manutenção "
             "mais prováveis, (5) a primeira fatia entregável em até 4 horas. Não proponha ferramenta fora da stack sem "
             "dizer qual ADR ela exigiria.")
VAZIAS = {"a", "o", "e", "de", "do", "da", "dos", "das", "para", "com", "sem", "em", "no", "na", "nos", "nas",
          "um", "uma", "que", "por", "pra", "meu", "minha", "os", "as", "ao", "se", "sistema", "quero", "preciso",
          "criar", "fazer", "ter", "clientes", "cliente"}
OPCOES = {
    "A": ("SUBIR PRONTO", "< 30 min", "Suba o container/ferramenta que já está no setup e configure. Nada de código."),
    "B": ("COLAR", "< 1 dia", "Use o pronto e ligue com n8n ou com a API dele. Código só de cola, com teste."),
    "C": ("CONSTRUIR", "2 a 3 dias por fatia", "É núcleo: programe no Aura, na stack fixa, com ADR e testes."),
}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return "".join(c for c in s if not unicodedata.combining(c))


def palavras(texto: str) -> list[str]:
    return [p for p in re.findall(r"[a-z0-9]+", _norm(texto)) if len(p) > 2 and p not in VAZIAS]


def carregar() -> tuple[dict, dict]:
    return json.loads(ECO.read_text(encoding="utf-8")), json.loads(MAPA.read_text(encoding="utf-8"))


def buscar_blocos(pedido: str, eco: dict, limite: int = 5) -> list[dict]:
    """Blocos do setup cujo rótulo ou descrição tocam as palavras do pedido, do mais parecido ao menos."""
    ps = set(palavras(pedido))
    if not ps:
        return []
    achados = []
    for b in eco["blocos"]:
        rot, desc = set(palavras(b["rotulo"])), set(palavras(b["descricao"]))
        nota = 3 * len(ps & rot) + len(ps & desc)
        if nota:
            achados.append((nota, b))
    achados.sort(key=lambda x: (-x[0], x[1]["id"]))
    return [b for _, b in achados[:limite]]


def buscar_fora(pedido: str, mapa: dict) -> list[dict]:
    ps = set(palavras(pedido))
    return [f for f in mapa.get("fora", []) if ps & set(palavras(f["item"]))]


def decidir(nucleo: bool, candidatos: list[dict], integra: bool) -> str:
    if nucleo:
        return "C"
    if candidatos and not integra:
        return "A"
    return "B"


def _sim(v: str | None) -> bool | None:
    if v is None:
        return None
    v = _norm(v).strip()
    if v in ("sim", "s", "yes", "y", "1"):
        return True
    if v in ("nao", "n", "no", "0"):
        return False
    raise ValueError(f"responda sim ou não, não {v!r}")


def _perguntar(texto: str) -> bool:
    if not sys.stdin.isatty():
        return False
    while True:
        try:
            return bool(_sim(input(f"{texto} [s/n] ")))
        except ValueError as e:
            print(e)


def rotulo(b: dict) -> str:
    return b["rotulo"].replace("|", " ")


def relatorio(pedido: str, opcao: str, candidatos: list[dict], fora: list[dict], base: str = "") -> str:
    nome, prazo, o_que = OPCOES[opcao]
    out = [f"Pedido: {pedido}", "", f"[OPÇÃO {opcao}] {nome} ({prazo})", o_que, ""]
    if candidatos:
        out.append("Já no setup:")
        out += [f"  - {rotulo(b)} ({b['id']}): {b['descricao']}" for b in candidatos]
    else:
        out.append("Nada no setup cobre isso. Antes de construir, garimpe: commit há menos de 6 meses, poucas "
                   "dependências, licença MIT/Apache, sem 'any' e Trivy limpo.")
    if fora:
        out += ["", "Atenção, já recusado antes:"] + [f"  - {f['item']}: {f['motivo']}" for f in fora]
    if base:
        out += ["", "Já na base do núcleo:", base]
    out += ["", "Regra das 4 horas: sem nada visível em 4 horas, pare e rode a triagem de novo."]
    return "\n".join(out)


def proximo_adr(pasta: Path) -> int:
    nums = [int(m.group(1)) for p in pasta.glob("*.md") if (m := re.match(r"(\d{4})-", p.name))]
    return max(nums, default=0) + 1


def slug(texto: str) -> str:
    return "-".join(palavras(texto)[:6]) or "decisao"


def rascunho_adr(n: int, pedido: str, opcao: str, candidatos: list[dict], hoje: date) -> str:
    nome, prazo, o_que = OPCOES[opcao]
    usa = ", ".join(rotulo(b) for b in candidatos) or "nada pronto no setup"
    return (f"# {n:04d} · {pedido}\n\n- **Status:** proposta\n- **Data:** {hoje.isoformat()}\n\n"
            f"## Contexto\n\n{pedido}. No setup: {usa}.\n\n"
            f"## Decisão\n\nOpção {opcao} ({nome}, {prazo}). {o_que}\n\n"
            "## Alternativas avaliadas\n\n- (preencha: o que mais foi considerado e por que ficou de fora)\n\n"
            "## Consequências\n\n- (preencha: o que fica mais fácil, o que fica mais difícil, o custo de manter)\n")


def url_grep(pedido: str) -> str:
    """Busca no grep.app (código público do GitHub) com as palavras do pedido: referência para você abrir, não para colar."""
    from urllib.parse import quote_plus
    return "https://grep.app/search?q=" + quote_plus(" ".join(palavras(pedido)[:4]))


def pacote(pedido: str, eco: dict, mapa: dict, base: str = "") -> str:
    cand = buscar_blocos(pedido, eco, limite=8)
    fora = buscar_fora(pedido, mapa)
    adrs = sorted(p.stem for p in ADRS.glob("*.md")) if ADRS.exists() else []
    out = ["# Pedido de arquitetura", "", pedido, "", "## Stack fixa", "", STACK, "", "## Regras", ""]
    out += [f"- {r}" for r in REGRAS]
    out += ["", "## O que já existe no setup e toca o pedido", ""]
    out += [f"- {rotulo(b)}: {b['descricao']}" for b in cand] or ["- nada encontrado pelas palavras do pedido"]
    if fora:
        out += ["", "## Já recusado (não proponha de novo)", ""] + [f"- {f['item']}: {f['motivo']}" for f in fora]
    if adrs:
        out += ["", "## ADRs em vigor", ""] + [f"- {a}" for a in adrs]
    if base:
        out += ["", "## O que o núcleo já sabe (decisões, lições, garimpos)", "", base]
    out += ["", "## Referências para conferir (abra você; não é colado aqui)", "", f"- Código aberto parecido: {url_grep(pedido)}"]
    out += ["", "## Como responder", "", INSTRUCAO]
    texto = "\n".join(out) + "\n"
    return texto + f"\n<!-- cerca de {len(texto) // 4} tokens -->\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("triar", help="montar, colar ou construir")
    t.add_argument("pedido")
    t.add_argument("--nucleo", help="sim/não: é a regra de negócio que gera faturamento?")
    t.add_argument("--integra", help="sim/não: precisa ligar aos sistemas AM ou a outra ferramenta?")
    t.add_argument("--adr", metavar="PASTA", help="grava o rascunho do ADR na próxima numeração da pasta")
    a = sub.add_parser("arquitetar", help="pacote de contexto para o Claude")
    a.add_argument("pedido")
    a.add_argument("--saida", help="arquivo de saída (padrão: tela)")
    args = ap.parse_args(argv)
    eco, mapa = carregar()

    if args.cmd == "arquitetar":
        con = _nucleo()
        base = nuc.contexto(con, args.pedido) if con else ""
        txt = pacote(args.pedido, eco, mapa, base)
        if con:
            nuc.evento(con, "arquiteto.pacote", {"pedido": args.pedido}, fonte="triagem")
            con.close()
        if args.saida:
            Path(args.saida).write_text(txt, encoding="utf-8")
            print(f"Pacote salvo em {args.saida} (cerca de {len(txt) // 4} tokens).")
        else:
            sys.stdout.write(txt)
        return 0

    try:
        nucleo, integra = _sim(args.nucleo), _sim(args.integra)
    except ValueError as e:
        print(e, file=sys.stderr)
        return 2
    if nucleo is None:
        nucleo = _perguntar("É a regra de negócio que gera faturamento (o que te diferencia)?")
    cand = buscar_blocos(args.pedido, eco)
    if integra is None and not nucleo:
        integra = _perguntar("Precisa ligar aos sistemas AM, a dados de cliente ou a outra ferramenta?")
    opcao = decidir(nucleo, cand, bool(integra))
    con = _nucleo()
    base = nuc.contexto(con, args.pedido) if con else ""
    rel = relatorio(args.pedido, opcao, cand, buscar_fora(args.pedido, mapa), base)
    print(rel)
    if con:
        nuc.lembrar(con, rel, tipo="triagem", titulo=f"Triagem: {args.pedido} → {opcao}", tags=f"opcao-{opcao.lower()}")
        nuc.evento(con, "triagem.feita", {"pedido": args.pedido, "opcao": opcao}, fonte="triagem")
        con.close()
    if args.adr:
        pasta = Path(args.adr)
        pasta.mkdir(parents=True, exist_ok=True)
        n = proximo_adr(pasta)
        arq = pasta / f"{n:04d}-{slug(args.pedido)}.md"
        arq.write_text(rascunho_adr(n, args.pedido, opcao, cand, date.today()), encoding="utf-8")
        print(f"\nRascunho do ADR: {arq}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
