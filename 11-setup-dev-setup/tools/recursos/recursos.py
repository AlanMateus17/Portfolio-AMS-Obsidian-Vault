#!/usr/bin/env python3
"""Auditoria de recursos: o que cada ferramenta do setup oferece hoje, o que usar e qual ferramenta faz cada tarefa.

Fonte: data/recursos.json (cada ferramenta aponta para um bloco do ecossistema). Saída: docs/recursos.md.
    python tools/recursos/recursos.py           # regenera
    python tools/recursos/recursos.py --check   # CI
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "recursos.json"
ECO = RAIZ / "data" / "ecossistema.json"
MD = RAIZ / "docs" / "recursos.md"
AVISO = "<!-- Arquivo GERADO por tools/recursos/recursos.py a partir de data/recursos.json. Não edite à mão. -->\n"
DECISOES = ["usar já", "usar grátis", "trocar", "testar isolado", "adiar", "não usar"]


def carregar():
    return json.loads(DADOS.read_text(encoding="utf-8")), json.loads(ECO.read_text(encoding="utf-8"))


def validar(d: dict, eco: dict) -> list[str]:
    blocos = {b["id"] for b in eco["blocos"]}
    e = []
    for f in d["ferramentas"]:
        if f["bloco"] not in blocos:
            e.append(f"{f['nome']}: bloco {f['bloco']} não existe no ecossistema")
        if not f["fonte"].startswith("https://"):
            e.append(f"{f['nome']}: fonte sem link https")
        if not f["recursos"]:
            e.append(f"{f['nome']}: sem recursos")
        for r in f["recursos"]:
            if r["decisao"] not in DECISOES:
                e.append(f"{f['nome']} / {r['recurso']}: decisão inválida {r['decisao']}")
            for k in ("o_que", "custo", "uso"):
                if not r[k].strip():
                    e.append(f"{f['nome']} / {r['recurso']}: campo {k} vazio")
    for r in d["rotas"]:
        for k in ("tarefa", "primaria", "reserva", "portao"):
            if not r[k].strip():
                e.append(f"rota {r.get('tarefa', '?')}: campo {k} vazio (toda tarefa precisa de primária, reserva e portão)")
    if not d["esteira_sites"] or not d["regras"]:
        e.append("esteira_sites ou regras vazias")
    return e


def gerar(d: dict) -> str:
    o = [AVISO, "# Recursos: o melhor de cada ferramenta para cada tarefa\n", "[← Índice da documentação](README.md)\n",
         f"Auditado em {d['auditado_em']}. Refaça a cada 3 meses, junto com a auditoria de custos: os planos mudam rápido.\n",
         "## Regras\n"]
    o += [f"- {x}" for x in d["regras"]]
    o += ["", "## Qual ferramenta faz cada tarefa\n", "Toda tarefa tem uma primária, uma reserva e um portão. Assim nenhuma depende dos créditos de uma ferramenta só.\n",
          "| Tarefa | Primária | Reserva | Portão |", "|---|---|---|---|"]
    o += [f"| {r['tarefa']} | {r['primaria']} | {r['reserva']} | {r['portao']} |" for r in d["rotas"]]
    o += ["", "## Esteira de sites (você só confere)\n"]
    o += [f"{i}. {x}" for i, x in enumerate(d["esteira_sites"], 1)]
    o += ["", "## Ferramenta por ferramenta\n"]
    for f in d["ferramentas"]:
        o += [f"### {f['nome']}\n", "| Recurso | O que faz | Custo | Uso no setup | Decisão |", "|---|---|---|---|---|"]
        o += [f"| {r['recurso']} | {r['o_que']} | {r['custo']} | {r['uso']} | **{r['decisao']}** |" for r in f["recursos"]]
        o += ["", f"**Lacuna:** {f['lacuna']}", "", f"Fonte: <{f['fonte']}>", ""]
    o += ["## Resumo das decisões\n", "| Decisão | Recursos |", "|---|---:|"]
    todos = [r for f in d["ferramentas"] for r in f["recursos"]]
    for k in DECISOES:
        n = sum(r["decisao"] == k for r in todos)
        if n:
            o.append(f"| {k} | {n} |")
    o.append("\nFerramentas locais e de código aberto (Git, Neovim, Docker etc.) ficam fora desta auditoria: não escondem recursos pagos nem mudam de plano.")
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d, eco = carregar()
    e = validar(d, eco)
    if e:
        print("\n".join("ERRO: " + x for x in e), file=sys.stderr)
        return 1
    t = gerar(d)
    if a.check:
        if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
            print("docs/recursos.md está desatualizado. Rode: python tools/recursos/recursos.py", file=sys.stderr)
            return 1
        print(f"Recursos em dia: {len(d['ferramentas'])} ferramentas, {len(d['rotas'])} rotas.")
        return 0
    MD.write_text(t, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
