#!/usr/bin/env python3
"""Catálogo único de ofertas do grupo: valida, pontua e gera a documentação.

Fonte: data/portfolio.json. Saídas: docs/operacao/portfolio.md e docs/operacao/portfolio.html.

Pontuação (0 a 18, quanto maior, antes entra na fila):
    2 × sinergia + escala + demanda − esforço − capital
Cada nota vai de 1 a 5. Sinergia pesa em dobro porque reaproveitar o que já existe
(aulas, código, livro, clientes, setup) é o que cabe na sua agenda.

Uso:
    python tools/portfolio/portfolio.py          # valida e regenera
    python tools/portfolio/portfolio.py --check  # falha se algo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "portfolio.json"
IMPLANTACAO = RAIZ / "data" / "implantacao.json"
MD = RAIZ / "docs" / "operacao" / "portfolio.md"
HTML = RAIZ / "docs" / "operacao" / "portfolio.html"
TEMPLATE = RAIZ / "tools" / "portfolio" / "portfolio.template.html"
AVISO = "<!-- Arquivo GERADO por tools/portfolio/portfolio.py a partir de data/portfolio.json. Não edite à mão. -->\n"

ESTAGIOS = {"ideia": "Ideia", "validacao": "Validação", "construcao": "Construção", "lancado": "Lançado",
            "escala": "Escala", "pausado": "Pausado"}
ESCALAS = {"digital": "Digital (custo por cliente perto de zero)", "produtizado": "Produtizado (pacote repetível)",
           "local": "Local (depende de gente e lugar)"}
NOTAS = ("sinergia", "escala", "demanda", "esforco", "capital")


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def pontuar(nota: dict) -> int:
    return 2 * nota["sinergia"] + nota["escala"] + nota["demanda"] - nota["esforco"] - nota["capital"]


def validar(dados: dict) -> list[str]:
    erros = []
    ids = [o["id"] for o in dados["ofertas"]]
    if len(ids) != len(set(ids)):
        erros.append("Há ofertas com id repetido.")
    conjunto = set(ids)
    for o in dados["ofertas"]:
        if o["frente"] not in dados["frentes"]:
            erros.append(f"{o['id']}: frente inexistente {o['frente']}")
        if o["estagio"] not in ESTAGIOS:
            erros.append(f"{o['id']}: estágio inválido {o['estagio']}")
        if o["escala"] not in ESCALAS:
            erros.append(f"{o['id']}: escala inválida {o['escala']}")
        for d in o["deriva_de"]:
            if d not in conjunto:
                erros.append(f"{o['id']}: deriva de oferta inexistente {d}")
            if d == o["id"]:
                erros.append(f"{o['id']}: deriva de si mesma")
        for k in NOTAS:
            v = o["nota"].get(k)
            if not isinstance(v, int) or not 1 <= v <= 5:
                erros.append(f"{o['id']}: nota {k} deve ser inteira de 1 a 5")
        if not o["proximo_passo"].strip():
            erros.append(f"{o['id']}: sem próximo passo")
    return erros


def quando_ofertas() -> dict[str, str]:
    """'passo 15.3 · Semanas 11 a 13 · jan/2027' para cada oferta, a partir do roteiro de implantação."""
    if not IMPLANTACAO.exists():
        return {}
    im = json.loads(IMPLANTACAO.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for i, f in enumerate(im["fases"]):
        for j, p in enumerate(f["passos"], 1):
            for o in p.get("ofertas", []):
                out.setdefault(o, f"passo {i}.{j} · {f.get('quando', '')}")
    return out


def ranking(dados: dict) -> list[dict]:
    q = quando_ofertas()
    ofs = [dict(o, pontos=pontuar(o["nota"]), quando=q.get(o["id"], "")) for o in dados["ofertas"]]
    return sorted(ofs, key=lambda o: (-o["pontos"], o["nome"]))


def esc_md(s: str) -> str:
    return s.replace("|", "\\|")


def gerar_md(dados: dict) -> str:
    rk = ranking(dados)
    F = dados["frentes"]
    o = [AVISO, "# Portfólio de ofertas\n", "[← Operação do grupo](README.md)\n",
         f"Todas as {len(rk)} ofertas do grupo num catálogo só: o que já existe, o que está planejado e "
         f"{sum(x['nova'] for x in rk)} fontes de renda novas que saem do que você já tem. "
         "A versão interativa, com filtros, é [`portfolio.html`](portfolio.html).\n",
         "## Como a fila é decidida\n",
         "**Pontos = 2 × sinergia + escala + demanda − esforço − capital** (cada nota de 1 a 5; máximo 18).\n",
         "- **Sinergia:** quanto reaproveita do que já existe (suas aulas, código, livro, clientes, setup).",
         "- **Escala:** 5 quando cada cliente novo quase não custa nada; 1 quando cada venda pede você presente.",
         "- **Demanda:** evidência de que alguém paga. Nas ideias novas, é hipótese até a validação.",
         "- **Esforço e capital:** horas e dinheiro até a primeira venda.\n",
         "A pontuação ordena; quem decide é a [ordem de execução](07-ordem-de-execucao.md), que respeita a sua agenda e os portões dos negócios físicos.\n",
         "## Ranking geral\n",
         "| # | Oferta | Frente | Estágio | Escala | Pontos | Próximo passo | Quando entra |",
         "|---:|---|---|---|---|---:|---|---|"]
    for i, x in enumerate(rk, 1):
        nome = f"[{esc_md(x['nome'])}]({x['doc']})" if x.get("doc") else esc_md(x["nome"])
        if x["nova"]:
            nome += " · **nova**"
        o.append(f"| {i} | {nome} | {F[x['frente']]} | {ESTAGIOS[x['estagio']]} | {x['escala'].capitalize()} | "
                 f"{x['pontos']} | {esc_md(x['proximo_passo'])} | {esc_md(x['quando'])} |")
    o.append("")
    o.append("## Fontes de renda novas\n")
    o.append("Ideias que nasceram do cruzamento entre os negócios, as aulas, o livro e o setup. Cada uma começa pela validação mais barata possível.\n")
    o.append("| Oferta | Sai de | Modelo de receita | Validação mais barata | Pontos |\n|---|---|---|---|---:|")
    nomes = {x["id"]: x["nome"] for x in rk}
    for x in rk:
        if x["nova"]:
            de = ", ".join(nomes[d] for d in x["deriva_de"]) or "—"
            o.append(f"| {esc_md(x['nome'])} | {esc_md(de)} | {x['receita']} | {esc_md(x['proximo_passo'])} | {x['pontos']} |")
    o.append("")
    o.append("## De onde cada oferta nasce\n")
    o.append("Cada seta é um reaproveitamento: a oferta de baixo usa conteúdo, código, clientes ou estrutura da de cima.\n")
    o.append("```mermaid\nflowchart LR")
    usados = {d for x in rk for d in x["deriva_de"]} | {x["id"] for x in rk if x["deriva_de"]}
    for x in rk:
        if x["id"] in usados:
            rot = x["nome"].split(" (")[0].replace('"', "'")
            if len(rot) > 34:
                rot = rot[:32] + "…"
            o.append(f'  {x["id"]}["{rot}"]')
    for x in rk:
        for d in x["deriva_de"]:
            o.append(f"  {d} --> {x['id']}")
    novas = [x["id"] for x in rk if x["nova"] and x["id"] in usados]
    o.append("  classDef nova fill:#f3e7d3,stroke:#8a5e22,color:#13262b")
    if novas:
        o.append("  class " + ",".join(novas) + " nova")
    o.append("```\n")
    o.append("## Por frente\n")
    for fid, ftit in F.items():
        grupo = [x for x in rk if x["frente"] == fid]
        o.append(f"### {ftit}\n")
        o.append("| Oferta | Receita | Automático | Fica com você | Métrica |\n|---|---|---|---|---|")
        for x in grupo:
            auto = ", ".join(x["automatico"]) or "—"
            hum = ", ".join(x["humano"]) or "—"
            o.append(f"| {esc_md(x['nome'])} | {x['receita']} | {esc_md(auto)} | {esc_md(hum)} | {esc_md(x['metrica'])} |")
        o.append("")
    o.append("## Resumo\n")
    o.append("| Estágio | Ofertas |\n|---|---:|")
    for k, v in ESTAGIOS.items():
        n = sum(1 for x in rk if x["estagio"] == k)
        if n:
            o.append(f"| {v} | {n} |")
    o.append("")
    o.append("| Escala | Ofertas |\n|---|---:|")
    for k, v in ESCALAS.items():
        o.append(f"| {v} | {sum(1 for x in rk if x['escala'] == k)} |")
    o.append("")
    return "\n".join(o)


def gerar_html(dados: dict) -> str:
    payload = {"frentes": dados["frentes"], "estagios": ESTAGIOS, "escalas": ESCALAS, "ofertas": ranking(dados)}
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/"))
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/portfolio/portfolio.py. Edite o template ou data/portfolio.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    dados = carregar()
    erros = validar(dados)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    saidas = {MD: gerar_md(dados), HTML: gerar_html(dados)}
    if a.check:
        ruins = [c for c, t in saidas.items() if (c.read_text(encoding="utf-8") if c.exists() else "") != t]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python tools/portfolio/portfolio.py", file=sys.stderr)
        if ruins:
            return 1
        print(f"Portfólio em dia: {len(dados['ofertas'])} ofertas.")
        return 0
    for c, t in saidas.items():
        c.write_text(t, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
