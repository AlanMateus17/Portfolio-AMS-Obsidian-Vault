#!/usr/bin/env python3
"""Ficha do assunto e colheita: o que você escreve uma vez depois de estudar vai sozinho para cada destino.

    python3 tools/colher/colher.py ficha 0.2      # cria a ficha no vault (se não existir) e mostra o caminho
    python3 tools/colher/colher.py colher 0.2     # confere a ficha e entrega cada seção no seu destino
    python3 tools/colher/colher.py colher 0.2 --seco     # mostra o que faria, sem escrever nada
    python3 tools/colher/colher.py colher 0.2 --forcar   # reescreve destinos que já existem

Destinos (ADR 0021):
  - Explicação + Exemplo resolvido -> ~/AMtech/entrada/capitulos/  (pipeline: livro, minicurso, post, roteiro)
  - Exercícios (tabela Nível | Pergunta | Resposta) -> ~/AMtech/banco/exercicios/ETAPA.yaml (AM Mentor, simulados)
                                                     e ~/AMtech/banco/anki/ETAPA.tsv (importar no Anki)
  - Aula (50 min) -> ensino-ti/<componente>/planos-de-aula/ETAPA-slug.md, em cada componente ligado à etapa
  - Ideias -> ~/AMtech/entrada/ideias/
Pastas: AMTECH_VAULT (padrão ~/dev/notas), AMTECH_DIR (padrão ~/AMtech), ENSINO_TI (padrão ~/dev/ensino-ti).
Nada de dado de aluno na ficha: ela vai para o repositório público ensino-ti.
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
VAZIO = "(escreva aqui)"
CAMPOS_AULA = ("Objetivo", "Abertura", "Explicação", "Prática", "Verificação")
MIN_EXERCICIOS = 3

FICHA = """---
etapa: "{etapa}"
titulo: "{titulo}"
componentes: [{componentes}]
estado: rascunho
---

# Ficha · {etapa} {titulo}

> Escreva **depois de estudar**, com as suas palavras e **sem abrir o arquivo do mapa** (é a recuperação do assunto).
> Cada seção vai para um lugar diferente. Quando terminar: `just colher {etapa}`.
> Nada de nome, nota ou dado de aluno: a seção Aula vai para o repositório público ensino-ti.

## Explicação
<!-- Vai para: livro Lógica e Máquina, minicurso, aula particular e posts (pipeline de conteúdo).
     O que é, por que existe e como funciona, como você explicaria para um aluno do 1º ano. -->
{vazio}

## Exemplo resolvido
<!-- Vai para: livro e minicurso. Um exemplo passo a passo, com o porquê de cada passo. -->
{vazio}

## Exercícios
<!-- Vão para: AM Mentor, baralho do Anki e banco de questões. Uma linha por exercício, no mínimo 3.
     Nível N1 (reconhecer), N2 (aplicar), N3 (achar o erro ou decidir), N4 (ensinar ou criar).
     Não use a barra vertical dentro do texto. -->
| Nível | Pergunta | Resposta |
|---|---|---|

## Aula
<!-- Vai para: ensino-ti, nos componentes {destinos}. Uma aula de 50 minutos. -->
- **Objetivo:** {vazio}
- **Abertura:** {vazio}
- **Explicação:** {vazio}
- **Prática:** {vazio}
- **Verificação:** {vazio}

## Registro de entrevista
- **Contexto:** {vazio}
- **Decisão:** {vazio}
- **Resultado:** {vazio}
- **Pergunta que responde:** {vazio}

## Ideias
<!-- Opcional. Vai para o pipeline de ideias: produto, conteúdo, oferta nova. Deixe vazio se não tiver. -->
"""


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def amtech() -> Path:
    return Path(os.environ.get("AMTECH_DIR") or Path.home() / "AMtech")


def ensino_ti() -> Path:
    return Path(os.environ.get("ENSINO_TI") or Path.home() / "dev" / "ensino-ti")


def mapa() -> dict:
    return json.loads((RAIZ / "data" / "aulas.json").read_text(encoding="utf-8"))


def etapa_info(etapa: str) -> dict:
    et = mapa()["etapas"].get(etapa)
    if not et:
        raise SystemExit(f"etapa {etapa} não está em data/aulas.json: acrescente o título e os componentes dela")
    return et


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def arq_ficha(etapa: str) -> Path:
    et = etapa_info(etapa)
    return vault() / "09-material-producao-simultanea" / "fichas" / f"{etapa}-{slug(et['titulo'])}.md"


def criar_ficha(etapa: str) -> tuple[Path, bool]:
    et, arq = etapa_info(etapa), arq_ficha(etapa)
    if arq.exists():
        return arq, False
    arq.parent.mkdir(parents=True, exist_ok=True)
    comp = et.get("componentes", [])
    texto = (FICHA.replace("{etapa}", etapa).replace("{titulo}", et["titulo"]).replace("{vazio}", VAZIO)
             .replace("{componentes}", ", ".join(f'"{c}"' for c in comp))
             .replace("{destinos}", ", ".join(c.rsplit("/", 1)[-1] for c in comp) or "(nenhum ligado ainda)"))
    arq.write_text(texto, encoding="utf-8")
    return arq, True


def secoes(texto: str) -> dict[str, str]:
    """Separa por '## Título'; tira os comentários <!-- -->."""
    corpo = re.sub(r"<!--.*?-->", "", texto, flags=re.S)
    partes = re.split(r"(?m)^## (.+)$", corpo)
    return {partes[i].strip(): partes[i + 1].strip() for i in range(1, len(partes) - 1, 2)}


def preenchida(conteudo: str) -> bool:
    return bool(conteudo.strip()) and VAZIO not in conteudo


def exercicios(conteudo: str) -> list[dict]:
    lista = []
    for ln in conteudo.splitlines():
        ln = ln.strip()
        if not ln.startswith("|") or set(ln) <= set("|-: "):
            continue
        cel = [c.strip() for c in ln.strip("|").split("|")]
        if len(cel) != 3 or cel[0].lower() == "nível":
            continue
        nivel, pergunta, resposta = cel
        if not re.fullmatch(r"N[1-4]", nivel.upper()):
            raise SystemExit(f"exercício com nível '{nivel}': use N1, N2, N3 ou N4")
        if pergunta and resposta:
            lista.append({"nivel": nivel.upper(), "pergunta": pergunta, "resposta": resposta})
    return lista


def campos(conteudo: str) -> dict[str, str]:
    return {m.group(1).strip(): m.group(2).strip()
            for m in re.finditer(r"(?m)^- \*\*(.+?):\*\*[ \t]*(.*)$", conteudo)}


def conferir(texto: str) -> list[str]:
    """Devolve o que falta. Lista vazia = pronta para colher."""
    sec, faltas = secoes(texto), []
    for nome in ("Explicação", "Exemplo resolvido"):
        if not preenchida(sec.get(nome, "")):
            faltas.append(f"seção '{nome}' vazia")
    ex = exercicios(sec.get("Exercícios", ""))
    if len(ex) < MIN_EXERCICIOS:
        faltas.append(f"Exercícios: {len(ex)} de no mínimo {MIN_EXERCICIOS}")
    aula = campos(sec.get("Aula", ""))
    for c in CAMPOS_AULA:
        if not preenchida(aula.get(c, "")):
            faltas.append(f"Aula: falta '{c}'")
    return faltas


def yaml_exercicios(etapa: str, titulo: str, ex: list[dict]) -> str:
    # strings em JSON são YAML válido: sem depender de biblioteca
    linhas = [f"# Gerado por just colher {etapa} a partir da ficha. Edite a ficha, não este arquivo.",
              f"etapa: {json.dumps(etapa)}", f"titulo: {json.dumps(titulo, ensure_ascii=False)}", "exercicios:"]
    for e in ex:
        linhas += [f"  - nivel: {e['nivel']}", f"    pergunta: {json.dumps(e['pergunta'], ensure_ascii=False)}",
                   f"    resposta: {json.dumps(e['resposta'], ensure_ascii=False)}"]
    return "\n".join(linhas) + "\n"


def tsv_anki(etapa: str, ex: list[dict]) -> str:
    limpa = lambda s: s.replace("\t", " ").replace("\n", " ")
    cab = "#separator:tab\n#html:false\n#tags column:3\n"
    return cab + "".join(f"{limpa(e['pergunta'])}\t{limpa(e['resposta'])}\tetapa-{etapa.replace('.', '-')} {e['nivel']}\n"
                         for e in ex)


def plano_de_aula(etapa: str, titulo: str, componente: str, aula: dict[str, str], hoje: date) -> str:
    tempos = {"Objetivo": "", "Abertura": " (5 min)", "Explicação": " (15 min)", "Prática": " (20 min)", "Verificação": " (10 min)"}
    corpo = "\n".join(f"- **{c}{tempos[c]}:** {aula[c]}" for c in CAMPOS_AULA)
    return (f"---\netapa: \"{etapa}\"\ncomponente: {componente.rsplit('/', 1)[-1]}\nduracao: 50 min\n"
            f"gerado-em: {hoje.isoformat()}\nfonte: ficha do assunto (just colher)\n---\n\n"
            f"# {titulo}\n\n{corpo}\n\n> Estudo de base: mapa-de-estudo, assunto {etapa}. "
            f"Adapte ao modelo oficial da escola antes de entregar o planejamento.\n")


def colher(etapa: str, seco: bool = False, forcar: bool = False, hoje: date | None = None) -> dict:
    hoje = hoje or date.today()
    et, arq = etapa_info(etapa), arq_ficha(etapa)
    if not arq.exists():
        raise SystemExit(f"ficha não existe: rode just ficha {etapa}")
    texto = arq.read_text(encoding="utf-8")
    faltas = conferir(texto)
    if faltas:
        raise SystemExit("A ficha ainda não está pronta:\n  - " + "\n  - ".join(faltas) + f"\n  Arquivo: {arq}")
    sec, s = secoes(texto), slug(et["titulo"])
    ex = exercicios(sec["Exercícios"])
    saidas: list[tuple[Path, str]] = []
    cap = f"# {etapa} {et['titulo']}\n\n## Explicação\n\n{sec['Explicação']}\n\n## Exemplo resolvido\n\n{sec['Exemplo resolvido']}\n"
    nome_cap = f"{etapa}-{s}.md"
    saidas.append((amtech() / "entrada" / "capitulos" / nome_cap, cap))
    saidas.append((amtech() / "banco" / "exercicios" / f"{etapa}.yaml", yaml_exercicios(etapa, et["titulo"], ex)))
    saidas.append((amtech() / "banco" / "anki" / f"{etapa}.tsv", tsv_anki(etapa, ex)))
    if preenchida(sec.get("Ideias", "")):
        saidas.append((amtech() / "entrada" / "ideias" / f"{etapa}-{s}-ideias.md", sec["Ideias"] + "\n"))
    aula = campos(sec["Aula"])
    base_ti, sem_repo = ensino_ti(), []
    for comp in et.get("componentes", []):
        pasta = base_ti / comp
        if not pasta.is_dir():
            sem_repo.append(comp)
            continue
        saidas.append((pasta / "planos-de-aula" / f"{etapa}-{s}.md", plano_de_aula(etapa, et["titulo"], comp, aula, hoje)))
    feitos, pulados = [], []
    ja_processado = (amtech() / "processados" / "capitulos" / nome_cap).exists()
    for destino, conteudo in saidas:
        existe = destino.exists() or (destino.name == nome_cap and ja_processado)
        if existe and not forcar and not (destino.exists() and destino.read_text(encoding="utf-8") == conteudo):
            pulados.append(destino)
            continue
        if not seco:
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(conteudo, encoding="utf-8")
        feitos.append(destino)
    if not seco:
        arq.write_text(re.sub(r"(?m)^estado: .*$", f"estado: colhida em {hoje.isoformat()}", texto, count=1), encoding="utf-8")
    return {"feitos": feitos, "pulados": pulados, "sem_repo": sem_repo, "exercicios": len(ex)}


def ofertas_tocadas() -> list[tuple[str, str]]:
    port = json.loads((RAIZ / "data" / "portfolio.json").read_text(encoding="utf-8"))
    por_id = {o["id"]: o for o in port["ofertas"]}
    ids = []
    for lista in mapa()["secoes"].values():
        ids += [i for i in lista if i in por_id and i not in ids]
    return [(por_id[i]["nome"], por_id[i].get("proximo_passo", "")) for i in ids]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("ficha").add_argument("etapa")
    c = s.add_parser("colher"); c.add_argument("etapa")
    c.add_argument("--seco", action="store_true"); c.add_argument("--forcar", action="store_true")
    a = ap.parse_args(argv)
    if a.cmd == "ficha":
        arq, nova = criar_ficha(a.etapa)
        print(("Ficha criada" if nova else "A ficha já existe") + f": {arq}")
        print(f"Preencha depois de estudar, sem abrir o arquivo do mapa. Depois: just colher {a.etapa}")
    else:
        r = colher(a.etapa, a.seco, a.forcar)
        verbo = "Escreveria" if a.seco else "Entregue"
        for d in r["feitos"]:
            print(f"{verbo}: {d}")
        for d in r["pulados"]:
            print(f"Já existe e foi mantido (use --forcar para reescrever): {d}")
        for comp in r["sem_repo"]:
            print(f"Aviso: pasta do componente não encontrada em {ensino_ti()}: {comp} (clone o ensino-ti ou ajuste ENSINO_TI)")
        print(f"{r['exercicios']} exercícios no banco. Importe no Anki o arquivo .tsv (Arquivo > Importar).")
        print("Ofertas que receberam material:")
        for nome, passo in ofertas_tocadas():
            print(f"  - {nome}: {passo}")
        print("  - Escola: os planos de aula estão no ensino-ti; faça commit lá quando revisar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
