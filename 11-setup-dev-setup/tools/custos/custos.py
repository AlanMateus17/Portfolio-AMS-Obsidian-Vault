#!/usr/bin/env python3
"""Auditoria de custos do setup: o que manter, cortar, trocar ou adiar, e os modelos abertos para cada tarefa.

Fonte: data/custos.json (cada item aponta para um bloco do ecossistema). Saída: docs/custos.md.
    python tools/custos/custos.py           # regenera
    python tools/custos/custos.py --check   # CI
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "custos.json"
ECO = RAIZ / "data" / "ecossistema.json"
MD = RAIZ / "docs" / "custos.md"
AVISO = "<!-- Arquivo GERADO por tools/custos/custos.py a partir de data/custos.json. Não edite à mão. -->\n"
DECISOES = ["testar grátis", "usar barato", "cortar", "cortar uma", "trocar", "trocar para comercial", "adiar", "limitar", "usar grátis", "manter grátis",
            "usar o que já paga", "manter", "regra"]


def carregar():
    return json.loads(DADOS.read_text(encoding="utf-8")), json.loads(ECO.read_text(encoding="utf-8"))


def validar(d: dict, eco: dict) -> list[str]:
    blocos = {b["id"] for b in eco["blocos"]}
    e = []
    for i in d["itens"]:
        if i["bloco"] not in blocos:
            e.append(f"{i['item']}: bloco {i['bloco']} não existe no ecossistema")
        if i["decisao"] not in DECISOES:
            e.append(f"{i['item']}: decisão inválida {i['decisao']}")
        if not i["motivo"].strip():
            e.append(f"{i['item']}: sem motivo")
    for k in ("construir", "open_source", "pagar"):
        if not d["regras"].get(k):
            e.append(f"regras.{k} vazia")
    return e


def gerar(d: dict) -> str:
    o = [AVISO, "# Custos: o que construir, o que pegar aberto e o que pagar\n", "[← Índice da documentação](README.md)\n",
         "Regra geral: **pague só pelo que custa menos que as suas horas ou exige confiança e legalidade.** "
         "O resto você constrói (se diferencia você) ou pega aberto (se é infraestrutura comum). Revisão a cada 3 meses (passo do roteiro).\n",
         "## A regra\n"]
    for k, t in (("construir", "Construir você mesmo"), ("open_source", "Pegar código aberto e hospedar"), ("pagar", "Pagar")):
        o.append(f"**{t}**\n")
        o += [f"- {x}" for x in d["regras"][k]]
        o.append("")
    ordem = {k: i for i, k in enumerate(DECISOES)}
    o += ["## Item por item\n", "| Decisão | Item | Hoje | Alternativa | Por quê |", "|---|---|---|---|---|"]
    for i in sorted(d["itens"], key=lambda i: (ordem[i["decisao"]], i["item"])):
        o.append(f"| **{i['decisao']}** | {i['item']} | {i['hoje']} | {i['alternativa']} | {i['motivo']} |")
    o += ["", "| Decisão | Itens |", "|---|---:|"]
    for k in DECISOES:
        n = sum(i["decisao"] == k for i in d["itens"])
        if n:
            o.append(f"| {k} | {n} |")
    o += ["", "## Modelos abertos para cada tarefa\n", "Para o que vira produto, prefira licença Apache 2.0 ou MIT e confira a licença do tamanho exato que baixar.\n",
          "| Tarefa | Modelo | Licença | Onde roda |", "|---|---|---|---|"]
    o += [f"| {m['tarefa']} | {m['modelo']} | {m['licenca']} | {m['roda']} |" for m in d["modelos_abertos"]]
    o += ["", "## Qual IA para cada tarefa\n", "| Tarefa | IA | Por quê |", "|---|---|---|"]
    o += [f"| {r['tarefa']} | {r['ia']} | {r['por_que']} |" for r in d.get("rotas_ia", [])]
    o += ["", "## Outras ferramentas de IA: o que acrescentam e quando\n", "| Categoria | Exemplos | Como gera renda | Decisão | Quando |", "|---|---|---|---|---|"]
    o += [f"| {x['categoria']} | {x['exemplos']} | {x['renda']} | {x['decisao']} | {x['quando']} |" for x in d.get("ia_extras", [])]
    o += ["", "## Fazer o limite do Claude durar\n"] + [f"- {x}" for x in d.get("economia_limite", [])]
    o += ["", "Coerência entre IAs: as mesmas regras em CLAUDE.md, AGENTS.md e GEMINI.md (scripts/wsl/regras-ia.sh)."]
    o.append("\nAssinaturas pessoais (streaming, apps) ficam fora do repositório: confira no Caixa da Casa.")
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
            print("docs/custos.md está desatualizado. Rode: python tools/custos/custos.py", file=sys.stderr)
            return 1
        print(f"Custos em dia: {len(d['itens'])} itens.")
        return 0
    MD.write_text(t, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
