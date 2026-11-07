#!/usr/bin/env python3
"""Certificações: o que cada uma habilita, requisito, custo, ordem e fonte.

Fonte: data/certificacoes.json. Saída: docs/certificacoes.md.
    python tools/carreira/certificacoes.py           # regenera
    python tools/carreira/certificacoes.py --check   # CI
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "certificacoes.json"
MD = RAIZ / "docs" / "certificacoes.md"
AVISO = "<!-- Arquivo GERADO por tools/carreira/certificacoes.py a partir de data/certificacoes.json. Não edite à mão. -->\n"
CAMPOS = ("nome", "habilita", "requisito", "custo", "status", "fonte")


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def validar(d: dict) -> list[str]:
    e = []
    for t in d["trilhas"]:
        ordens = [i["ordem"] for i in t["itens"]]
        if len(ordens) != len(set(ordens)):
            e.append(f"trilha {t['id']}: ordem repetida")
        for i in t["itens"]:
            for k in CAMPOS:
                if not str(i.get(k, "")).strip():
                    e.append(f"{i.get('nome', '?')}: campo {k} vazio")
            if not i["fonte"].startswith("https://"):
                e.append(f"{i['nome']}: fonte sem link https")
    return e


def gerar(d: dict) -> str:
    o = [AVISO, "# Certificações: o que cada uma habilita e em que ordem\n", "[← Índice da documentação](README.md)\n",
         f"Conferido em {d['conferido_em']}.\n", "## Regras\n"]
    o += [f"- {x}" for x in d["regras"]]
    for t in d["trilhas"]:
        o += ["", f"## {t['nome']}\n", f"**Para quê:** {t['objetivo']}\n",
              "| Ordem | Certificação | Habilita | Requisito | Custo | Situação |", "|---:|---|---|---|---|---|"]
        for i in sorted(t["itens"], key=lambda i: i["ordem"]):
            o.append(f"| {i['ordem']} | [{i['nome']}]({i['fonte']}) | {i['habilita']} | {i['requisito']} | {i['custo']} | {i['status']} |")
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d = carregar()
    e = validar(d)
    if e:
        print("\n".join("ERRO: " + x for x in e), file=sys.stderr)
        return 1
    t = gerar(d)
    if a.check:
        if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
            print("docs/certificacoes.md está desatualizado. Rode: python tools/carreira/certificacoes.py", file=sys.stderr)
            return 1
        print(f"Certificações em dia: {sum(len(t['itens']) for t in d['trilhas'])} itens.")
        return 0
    MD.write_text(t, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
