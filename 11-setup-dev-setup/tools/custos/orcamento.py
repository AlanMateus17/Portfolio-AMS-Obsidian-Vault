#!/usr/bin/env python3
"""Orçamento do setup: soma o que você vai gastar, só para desenvolver e testar protótipos.

Lê um arquivo de preços que VOCÊ confirma (não inventa nada) e soma por etapa e por tipo, separando
o gasto único (comprar uma vez) do recorrente (por mês). Item marcado como `venda = true` é para vender
um produto, não para desenvolver: ele fica de fora do total, como você pediu.

    python3 tools/custos/orcamento.py ~/financas/orcamento.toml           # relatório em Markdown
    python3 tools/custos/orcamento.py ~/financas/orcamento.toml --json    # para um painel
    python3 tools/custos/orcamento.py ~/financas/orcamento.toml --etapa 1 # só a etapa 1

Modelo: tools/custos/orcamento.example.toml. Os preços ficam em ~/financas, fora do GitHub.
Cada compra ainda passa pela cascata do Caixa da Casa (cartão quitado e reserva cheia antes).
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from collections import defaultdict
from pathlib import Path

CATEGORIAS = ("software", "hardware")


def carregar(caminho: Path) -> dict:
    with open(caminho, "rb") as f:
        return tomllib.load(f)


def validar(d: dict) -> list[str]:
    erros = []
    itens = d.get("item", [])
    if not itens:
        erros.append("nenhum item no orçamento")
    for it in itens:
        nome = it.get("nome", "?")
        if not str(it.get("nome", "")).strip():
            erros.append("item sem nome")
        if it.get("categoria") not in CATEGORIAS:
            erros.append(f"{nome}: categoria inválida {it.get('categoria')!r} (use {' ou '.join(CATEGORIAS)})")
        c = it.get("custo")
        if not isinstance(c, (int, float)) or c < 0:
            erros.append(f"{nome}: custo deve ser número ≥ 0 (em reais)")
        cmax = it.get("custo_max")
        if cmax is not None and (not isinstance(cmax, (int, float)) or cmax < c):
            erros.append(f"{nome}: custo_max deve ser número ≥ custo")
        if not isinstance(it.get("etapa", 1), int) or it.get("etapa", 1) < 1:
            erros.append(f"{nome}: etapa deve ser inteiro ≥ 1")
        for campo in ("recorrente", "venda"):
            if campo in it and not isinstance(it[campo], bool):
                erros.append(f"{nome}: {campo} deve ser true ou false")
    return erros


def faixa(it: dict) -> tuple[float, float]:
    lo = float(it["custo"])
    return lo, float(it.get("custo_max", lo))


def resumir(d: dict, etapa: int | None = None) -> dict:
    itens = [it for it in d.get("item", []) if not it.get("venda", False)]
    if etapa is not None:
        itens = [it for it in itens if it.get("etapa", 1) == etapa]
    fora = [it["nome"] for it in d.get("item", []) if it.get("venda", False)]
    por_etapa: dict = defaultdict(lambda: {"unico": [0.0, 0.0], "mes": [0.0, 0.0]})
    por_cat: dict = defaultdict(lambda: {"unico": [0.0, 0.0], "mes": [0.0, 0.0]})
    unico = [0.0, 0.0]
    mes = [0.0, 0.0]
    for it in itens:
        lo, hi = faixa(it)
        destino = "mes" if it.get("recorrente", False) else "unico"
        et = it.get("etapa", 1)
        for alvo, chave in ((por_etapa[et], destino), (por_cat[it["categoria"]], destino)):
            alvo[chave][0] += lo
            alvo[chave][1] += hi
        alvo_total = mes if destino == "mes" else unico
        alvo_total[0] += lo
        alvo_total[1] += hi
    return {
        "itens": itens, "fora_venda": fora,
        "unico": unico, "mes": mes,
        "por_etapa": {k: por_etapa[k] for k in sorted(por_etapa)},
        "por_categoria": {k: por_cat[k] for k in CATEGORIAS if k in por_cat},
        "ref": d.get("geral", {}).get("ref_mes", ""),
    }


def reais(par: list[float]) -> str:
    lo, hi = par
    f = lambda v: f"R$ {v:,.0f}".replace(",", ".")
    return f(lo) if abs(hi - lo) < 0.5 else f"{f(lo)}–{f(hi)}"


def markdown(r: dict) -> str:
    o = ["# Orçamento do setup (desenvolvimento e protótipos)", ""]
    if r["ref"]:
        o.append(f"Preços de referência: {r['ref']}. Confirme antes de comprar.")
    o += ["", "## Total", "", "| | Uma vez | Por mês |", "|---|---:|---:|",
          f"| **Geral** | {reais(r['unico'])} | {reais(r['mes'])} |"]
    for cat, v in r["por_categoria"].items():
        o.append(f"| {cat.capitalize()} | {reais(v['unico'])} | {reais(v['mes'])} |")
    o += ["", "## Por etapa", "", "| Etapa | Uma vez | Por mês |", "|---|---:|---:|"]
    for et, v in r["por_etapa"].items():
        o.append(f"| {et} | {reais(v['unico'])} | {reais(v['mes'])} |")
    o += ["", "## Itens", "", "| Item | Tipo | Etapa | Uma vez | Por mês |", "|---|---|---:|---:|---:|"]
    for it in sorted(r["itens"], key=lambda x: (x.get("etapa", 1), x["categoria"], x["nome"])):
        rec = it.get("recorrente", False)
        valor = reais(list(faixa(it)))
        o.append(f"| {it['nome']} | {it['categoria']} | {it.get('etapa', 1)} | {'—' if rec else valor} | {valor if rec else '—'} |")
    if r["fora_venda"]:
        o += ["", "## Fora do total (são para vender, não para desenvolver)", ""]
        o += [f"- {n}" for n in r["fora_venda"]]
    o += ["", "> Estimativa. Cada compra passa pela cascata do Caixa da Casa: cartão quitado e reserva cheia antes.", ""]
    return "\n".join(o)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Orçamento do setup (só desenvolvimento e protótipos)")
    ap.add_argument("arquivo", type=Path)
    ap.add_argument("--etapa", type=int, help="só uma etapa")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        d = carregar(a.arquivo)
    except (OSError, tomllib.TOMLDecodeError) as e:
        print(f"ERRO: não consegui ler {a.arquivo}: {e}", file=sys.stderr)
        return 1
    erros = validar(d)
    if erros:
        for e in erros:
            print(f"ERRO: {e}", file=sys.stderr)
        return 1
    r = resumir(d, a.etapa)
    if a.json:
        import json
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        print(markdown(r))
    return 0


if __name__ == "__main__":
    sys.exit(main())
