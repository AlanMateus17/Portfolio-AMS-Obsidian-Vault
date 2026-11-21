#!/usr/bin/env python3
"""Liga o Professor ao mapa-de-estudo: cada módulo de data/professor/curriculo.json aponta (campo `etapa`) para um
assunto do MAPA.md do repositório AlanMateus17/mapa-de-estudo.

    python3 tools/professor/mapa.py atualizar ~/dev/mapa-de-estudo/MAPA.md   # regrava data/professor/mapa-assuntos.json
    python3 tools/professor/mapa.py conferir                                  # o que o just check roda (sem rede)

O retrato do mapa (data/professor/mapa-assuntos.json) é gerado do MAPA.md; o CI confere contra ele, sem precisar do outro
repositório. Regras conferidas:
1. todo módulo tem `etapa` que existe no mapa (ou `etapa: null` com `etapa_motivo`, para o que o mapa deixa fora das tabelas);
2. a ordem do Professor não contraria os pré-requisitos do mapa: se o assunto de A depende (direta ou indiretamente) do
   assunto de B, A não pode vir num trimestre anterior ao de B, e um pré-requisito do Professor não pode estar "depois" no mapa.

O retrato também guarda, para cada assunto, se o arquivo já está escrito e conferido (📘 na coluna Arquivo) e o caminho
dele no mapa-de-estudo. O Professor só libera um assunto escrito e cujos pré-requisitos do mapa já foram dominados
(ADR 0018: um assunto só entra quando o arquivo dele estiver escrito e conferido). O `conferir` também mostra a
cobertura: quantos assuntos do mapa têm módulo no Professor e quais assuntos escritos ainda não têm.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CURRICULO = RAIZ / "data" / "professor" / "curriculo.json"
RETRATO = RAIZ / "data" / "professor" / "mapa-assuntos.json"
ID = re.compile(r"^(?:\d+\.\d+|H\d+\.\d+)$")


LINK = re.compile(r"\]\(([^)#\s]+\.md)")


def ler_mapa(md: str) -> dict[str, dict]:
    """Extrai {id: {titulo, depende, escrito, arquivo}} das tabelas do MAPA.md, achando as colunas "Depende de" e
    "Arquivo" pelo cabeçalho de cada tabela. Escrito = 📘 na coluna Arquivo (as tabelas do horizonte não têm a coluna)."""
    assuntos, col_dep, col_tit, col_arq = {}, None, 1, None
    for linha in md.splitlines():
        if not linha.startswith("|"):
            col_dep = None if not linha.strip() else col_dep
            continue
        cel = [c.strip() for c in linha.strip().strip("|").split("|")]
        if cel and cel[0] == "#":
            col_dep = next((i for i, c in enumerate(cel) if c.lower().startswith("depende")), None)
            col_tit = next((i for i, c in enumerate(cel) if c.lower().startswith("assunto")), 1)
            col_arq = next((i for i, c in enumerate(cel) if c.lower().startswith("arquivo")), None)
            continue
        if not cel or not ID.match(cel[0]) or col_dep is None:
            continue
        deps = [d for d in re.split(r"[,;\s]+", cel[col_dep]) if ID.match(d)] if col_dep < len(cel) else []
        arq = cel[col_arq] if col_arq is not None and col_arq < len(cel) else ""
        link = LINK.search(arq)
        escrito = "📘" in arq and bool(link)
        assuntos[cel[0]] = {"titulo": re.sub(r"^↻\s*", "", cel[col_tit]), "depende": deps, "escrito": escrito,
                            "arquivo": link.group(1) if escrito else None}
    return assuntos


def cobertura(curriculo: dict, assuntos: dict[str, dict]) -> dict:
    """Quantos assuntos do mapa têm módulo no Professor, e quais assuntos já escritos ainda não têm módulo."""
    ligados = {m.get("etapa") for m in curriculo["modulos"]} - {None}
    escritos = [a for a, info in assuntos.items() if info.get("escrito")]
    return {"total": len(assuntos), "com_modulo": len(ligados & set(assuntos)), "escritos": len(escritos),
            "escritos_sem_modulo": [a for a in escritos if a not in ligados]}


def fecho(assuntos: dict[str, dict]) -> dict[str, set[str]]:
    """Para cada assunto, todos os assuntos de que ele depende, direta ou indiretamente."""
    memo: dict[str, set[str]] = {}

    def visita(a, pilha=()):
        if a in memo:
            return memo[a]
        if a in pilha:
            return set()
        tudo = set()
        for d in assuntos.get(a, {}).get("depende", []):
            tudo |= {d} | visita(d, pilha + (a,))
        memo[a] = tudo
        return tudo
    for a in assuntos:
        visita(a)
    return memo


def conferir(curriculo: dict, assuntos: dict[str, dict]) -> list[str]:
    erros = []
    mods = {m["id"]: m for m in curriculo["modulos"]}
    for m in curriculo["modulos"]:
        if "etapa" not in m:
            erros.append(f"{m['id']}: sem o campo etapa")
        elif m["etapa"] is None:
            if not str(m.get("etapa_motivo", "")).strip():
                erros.append(f"{m['id']}: etapa nula precisa de etapa_motivo")
        elif m["etapa"] not in assuntos:
            erros.append(f"{m['id']}: etapa {m['etapa']} não existe no mapa")
    if erros:
        return erros
    dep = fecho(assuntos)
    for a in curriculo["modulos"]:
        ea = a["etapa"]
        if ea is None:
            continue
        for b in curriculo["modulos"]:
            eb = b["etapa"]
            if eb is None or a is b or ea == eb:
                continue
            if eb in dep.get(ea, set()) and a.get("trimestre", 0) < b.get("trimestre", 0):
                erros.append(f"{a['id']} (trimestre {a['trimestre']}, {ea}) vem antes de {b['id']} (trimestre {b['trimestre']}, {eb}), "
                             f"mas no mapa {ea} depende de {eb}")
        for p in a.get("prereq", []):
            ep = mods[p]["etapa"] if p in mods else None
            if ep and ep != ea and ea in dep.get(ep, set()):
                erros.append(f"{a['id']} tem {p} como pré-requisito, mas no mapa {ep} depende de {ea}")
    return erros


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == "atualizar":
        md = Path(sys.argv[2] if len(sys.argv) > 2 else Path.home() / "dev" / "mapa-de-estudo" / "MAPA.md").expanduser()
        assuntos = ler_mapa(md.read_text(encoding="utf-8"))
        RETRATO.write_text(json.dumps({"fonte": "AlanMateus17/mapa-de-estudo/MAPA.md", "assuntos": assuntos},
                                      ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{len(assuntos)} assuntos gravados em {RETRATO.relative_to(RAIZ)}")
        return 0
    if len(sys.argv) >= 2 and sys.argv[1] == "conferir":
        assuntos = json.loads(RETRATO.read_text(encoding="utf-8"))["assuntos"]
        cur = json.loads(CURRICULO.read_text(encoding="utf-8"))
        erros = conferir(cur, assuntos)
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        print("Professor alinhado ao mapa de estudo." if not erros else f"{len(erros)} problema(s).")
        c = cobertura(cur, assuntos)
        print(f"Cobertura: {c['com_modulo']} de {c['total']} assuntos do mapa têm módulo; {c['escritos']} escritos e conferidos.")
        if c["escritos_sem_modulo"]:
            print("Escritos sem módulo (estude pelo arquivo do mapa): " + ", ".join(c["escritos_sem_modulo"]))
        return 1 if erros else 0
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
