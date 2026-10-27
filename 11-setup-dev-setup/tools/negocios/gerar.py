#!/usr/bin/env python3
"""Gera docs/negocios/numeros.md a partir de data/negocios.json.

Uso:
    python tools/negocios/gerar.py          # regenera
    python tools/negocios/gerar.py --check  # falha se o arquivo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from financas import RAIZ, carregar  # noqa: E402

SAIDA = RAIZ / "docs" / "negocios" / "numeros.md"
PLANEJADOR = RAIZ / "docs" / "negocios" / "planejador.html"
TEMPLATE = RAIZ / "tools" / "negocios" / "planejador.template.html"
AVISO = "<!-- Arquivo GERADO por tools/negocios/gerar.py a partir de data/negocios.json. Não edite à mão. -->\n"
CLUSTER = {"A": "A · Tecnologia", "B": "B · Logística", "C": "C · Alimentação"}


def brl(v: float | None, casas: int = 0) -> str:
    if v is None:
        return "não empata"
    s = f"{abs(v):,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return ("−R$ " if v < 0 else "R$ ") + s


def pct(v: float | None) -> str:
    return "—" if v is None else f"{v * 100:.1f}%".replace(".", ",")


def gerar() -> str:
    dados, negocios = carregar()
    p = dados["premissas"]
    resumos = [n.resumo() for n in negocios]
    o = [AVISO, "# Números de cada negócio\n", "[← Negócios do grupo](README.md)\n",
         f"> {p['aviso']}\n",
         "## Premissas\n",
         f"- Cidade: {p['cidade']}. Data de referência: {p['data']}.",
         f"- Salário mínimo de 2026: {brl(p['salario_minimo'])}. {p['encargos_obs']}",
         f"- {p['variavel_obs']}",
         f"- {p['rampa_obs']} Cada negócio usa a própria rampa, indicada abaixo.",
         f"- Capital mínimo = investimento + prejuízo acumulado na rampa + reserva de {p['reserva_meses']} meses de custos fixos.",
         "- Simples Nacional calculado por fonte, no anexo de cada atividade, com a faixa definida pela receita total (tabelas de 2026). Nos primeiros meses, a receita dos 12 meses é a média dos meses já vividos × 12, como manda a LC 123.",
         "- Cenário conservador: o mesmo negócio vendendo 70% do alvo.\n",
         "## Resumo\n",
         "| Negócio | Investimento | Custos fixos/mês | Receita-alvo/mês | Lucro no alvo | Lucro a 70% | Ponto de equilíbrio | Retorno | Capital mínimo |",
         "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    total_cap = total_inv = 0.0
    for s in resumos:
        total_cap += s["capital_minimo"]
        total_inv += s["investimento"]
        ret = f"mês {s['mes_retorno']}" if s["mes_retorno"] else "após 36 meses"
        o.append(f"| [{s['nome']}](#{s['id']}) | {brl(s['investimento'])} | {brl(s['fixos'])} | {brl(s['receita'])} | "
                 f"{brl(s['lucro'])} ({pct(s['margem'])}) | {brl(s['lucro_70'])} | {brl(s['ponto_equilibrio'])} ({pct(s['pe_pct'])} do alvo) | {ret} | {brl(s['capital_minimo'])} |")
    o.append(f"| **Todos** | **{brl(total_inv)}** | | | | | | | **{brl(total_cap)}** |\n")
    o.append("O retorno é o mês em que o caixa acumulado, já descontado o investimento, volta a zero.\n")
    for n, s in zip(negocios, resumos):
        o.append(f'<a id="{s["id"]}"></a>\n')
        o.append(f"## {s['nome']}\n")
        o.append(f"{CLUSTER[s['cluster']]} · rampa de {n.rampa_meses} meses, começando em {pct(n.rampa_inicio)} do alvo.\n")
        for a in s["alertas"]:
            o.append(f"> {a}\n")
        o.append("### Investimento inicial\n")
        o.append("| Item | Valor |\n|---|---:|")
        for i in n.investimento:
            o.append(f"| {i['item']} | {brl(i['valor'])} |")
        o.append(f"| **Total** | **{brl(s['investimento'])}** |\n")
        o.append("### Custos fixos por mês\n")
        o.append("| Item | Valor |\n|---|---:|")
        for f in n.fixos:
            o.append(f"| {f['item']} | {brl(f['valor'])} |")
        for e in n.equipe:
            q = e.get("qtd", 1)
            o.append(f"| {e['cargo']} ({q} × salário {brl(e['salario'])} × {str(n.encargos).replace('.', ',')}) | {brl(e['salario'] * q * n.encargos)} |")
        if n.prolabore:
            o.append(f"| Pró-labore (seu) | {brl(n.prolabore)} |")
        o.append(f"| **Total** | **{brl(s['fixos'])}** |\n")
        o.append("### Fontes de receita no alvo\n")
        o.append("| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |")
        o.append("|---|---|---:|---:|---:|---:|")
        for f, l in zip(n.fontes, s["linhas"]):
            qtd = f"{f.qtd:,.0f}".replace(",", ".")
            o.append(f"| {f.nome} | {qtd} × {brl(f.ticket, 2)} | {brl(l['receita'])} | {brl(l['variavel'])} ({pct(f.variavel)}) | "
                     f"{brl(l['imposto'])} (Anexo {l['anexo']}) | {brl(l['mc'])} |")
        o.append(f"| **Total** | | **{brl(s['receita'])}** | **{brl(s['variavel'])}** | **{brl(s['imposto'])}** | **{brl(s['mc'])}** ({pct(s['mc_pct'])}) |\n")
        o.append(f"Margem de contribuição {brl(s['mc'])} − custos fixos {brl(s['fixos'])} = **lucro de {brl(s['lucro'])} por mês** no alvo "
                 f"e {brl(s['lucro_70'])} vendendo 70%. Empata com {brl(s['ponto_equilibrio'])} de receita por mês.\n")
        o.append("### Primeiros 12 meses\n")
        o.append("| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |\n|---:|---:|---:|---:|---:|")
        for x in s["rampa"][:12]:
            o.append(f"| {x['mes']} | {pct(x['fator'])} | {brl(x['receita'])} | {brl(x['lucro'])} | {brl(x['caixa'])} |")
        o.append("")
        o.append(f"Pior caixa: {brl(s['pior_caixa'])}. Capital mínimo: investimento {brl(s['investimento'])} + prejuízo da rampa "
                 f"{brl(s['perdas_rampa'])} + reserva {brl(s['reserva'])} = **{brl(s['capital_minimo'])}**.\n")
    return "\n".join(o)


def gerar_planejador() -> str:
    import json
    dados = json.loads((RAIZ / "data" / "negocios.json").read_text(encoding="utf-8"))
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(dados, ensure_ascii=False).replace("</", "<\\/"))
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/negocios/gerar.py. Edite o template ou data/negocios.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    saidas = {SAIDA: gerar(), PLANEJADOR: gerar_planejador()}
    if a.check:
        ruins = [c for c, novo in saidas.items() if (c.read_text(encoding="utf-8") if c.exists() else "") != novo]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python tools/negocios/gerar.py", file=sys.stderr)
        if ruins:
            return 1
        print("numeros.md e planejador.html em dia.")
        return 0
    for c, novo in saidas.items():
        c.write_text(novo, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
