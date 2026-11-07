#!/usr/bin/env python3
"""Catálogo de softwares: tudo o que você pode criar e vender (e os seus próprios sites e ferramentas).

Fonte: data/softwares.json. Saída: docs/operacao/softwares.md.
Cada software liga a uma oferta do portfólio (data/portfolio.json) e é montado com módulos
reaproveitáveis: construir o módulo uma vez barateia todos os softwares que o usam.

Uso:
    python tools/softwares/softwares.py          # valida e regenera
    python tools/softwares/softwares.py --check  # falha se algo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "softwares.json"
PORTFOLIO = RAIZ / "data" / "portfolio.json"
MD = RAIZ / "docs" / "operacao" / "softwares.md"
AVISO = "<!-- Arquivo GERADO por tools/softwares/softwares.py a partir de data/softwares.json. Não edite à mão. -->\n"
ID_RE = re.compile(r"^[a-z0-9-]+$")

CATEGORIAS = {
    "site": "Sites por tipo de negócio",
    "sistema": "Sistemas AM (stack Aura)",
    "microsaas": "Micro-SaaS (validar rápido, reconstruir se vender)",
    "educacao": "Educação",
    "produto": "Produtos para devs e empresas",
    "proprio": "Seus sites e ferramentas (não vendidos)",
}
FERRAMENTAS = {
    "builder": "Website Builder com IA (Hostinger)", "horizons": "Horizons (Hostinger)", "aura": "Stack Aura (.NET + Next.js)",
    "nextjs": "Next.js", "wordpress": "WordPress", "n8n": "n8n", "python": "Python/planilha", "scripts": "Scripts do setup",
    "artifact": "Artefato do Claude",
}
ESTADOS = {"ideia": "Ideia", "planejado": "Planejado", "em-construcao": "Em construção", "existe": "Existe"}


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def ofertas() -> dict[str, dict]:
    return {o["id"]: o for o in json.loads(PORTFOLIO.read_text(encoding="utf-8"))["ofertas"]}


def validar(d: dict, ofs: dict | None = None) -> list[str]:
    ofs = ofertas() if ofs is None else ofs
    erros = []
    mods = [m["id"] for m in d["modulos"]]
    if len(mods) != len(set(mods)):
        erros.append("Há módulos com id repetido.")
    ids = [s["id"] for s in d["softwares"]]
    if len(ids) != len(set(ids)):
        erros.append("Há softwares com id repetido.")
    usados = set()
    for s in d["softwares"]:
        if not ID_RE.match(s["id"]):
            erros.append(f"id inválido: {s['id']}")
        if s["categoria"] not in CATEGORIAS:
            erros.append(f"{s['id']}: categoria inválida {s['categoria']}")
        if s["ferramenta"] not in FERRAMENTAS:
            erros.append(f"{s['id']}: ferramenta inválida {s['ferramenta']}")
        if s["estado"] not in ESTADOS:
            erros.append(f"{s['id']}: estado inválido {s['estado']}")
        if s["vende"] and s.get("oferta") not in ofs:
            erros.append(f"{s['id']}: vende, mas a oferta {s.get('oferta')} não existe no portfólio")
        if not s["vende"] and s.get("oferta"):
            erros.append(f"{s['id']}: não vende, então não liga a oferta")
        if not s["modulos"]:
            erros.append(f"{s['id']}: sem módulos")
        for m in s["modulos"]:
            usados.add(m)
            if m not in mods:
                erros.append(f"{s['id']}: módulo inexistente {m}")
    for m in sorted(set(mods) - usados):
        erros.append(f"módulo {m} não é usado por nenhum software")
    return erros


def esc(s: str) -> str:
    return s.replace("|", "\\|")


def ordem_modulos(d: dict) -> list[tuple[dict, int, int]]:
    out = []
    for m in d["modulos"]:
        quem = [s for s in d["softwares"] if m["id"] in s["modulos"]]
        out.append((m, len(quem), sum(s["vende"] for s in quem)))
    return sorted(out, key=lambda t: (-t[2], -t[1], t[0]["nome"]))


def gerar_md(d: dict) -> str:
    ofs = ofertas()
    sw = d["softwares"]
    vende = [s for s in sw if s["vende"]]
    mn = {m["id"]: m["nome"] for m in d["modulos"]}
    o = [AVISO, "# Catálogo de softwares\n", "[← Operação do grupo](README.md)\n",
         f"**{len(vende)} softwares que você pode criar e vender**, mais {len(sw) - len(vende)} sites e ferramentas seus. "
         f"Todos são montados a partir de **{len(d['modulos'])} módulos reaproveitáveis**: cada módulo construído uma vez "
         "deixa mais barato todo software que o usa. Cada software vendável liga a uma oferta do "
         "[portfólio](portfolio.md), onde estão o veredito, a fila e as automações.\n",
         "## Resumo\n", "| Categoria | Softwares | Já existem ou em construção |\n|---|---:|---:|"]
    for k, v in CATEGORIAS.items():
        g = [s for s in sw if s["categoria"] == k]
        o.append(f"| {v} | {len(g)} | {sum(s['estado'] in ('existe', 'em-construcao') for s in g)} |")
    o.append("")
    o.append("| Ferramenta | Softwares |\n|---|---:|")
    for k, v in FERRAMENTAS.items():
        n = sum(s["ferramenta"] == k for s in sw)
        if n:
            o.append(f"| {v} | {n} |")
    o.append("")
    o.append("## Módulos: construa nesta ordem\n")
    o.append("Primeiro os que entram em mais softwares vendáveis. É aqui que as horas de trabalho caem: "
             "um site novo de padaria ou de imobiliária vira montagem de módulos prontos, não um projeto do zero.\n")
    o.append("| # | Módulo | O que faz | Softwares que usam | Vendáveis |\n|---:|---|---|---:|---:|")
    for i, (m, n, v) in enumerate(ordem_modulos(d), 1):
        o.append(f"| {i} | **{esc(m['nome'])}** | {esc(m['faz'])} | {n} | {v} |")
    o.append("")
    o.append("## Regra de ferramenta\n")
    o.append("- **Website Builder com IA:** site institucional que o cliente edita sozinho. Menos manutenção.")
    o.append("- **Horizons:** quando o cliente paga por uma função (pedido, agenda, catálogo, área do cliente) e para validar micro-SaaS. "
             "O código exportado é só o frontend (React/Vite); o banco fica na Hostinger.")
    o.append("- **Stack Aura:** o que já provou que vende e precisa escalar, multi-empresa e com licença por módulo.")
    o.append("- **Conta e domínio no nome do cliente**, com você como colaborador; contrato com o que a mensalidade cobre.\n")
    for k, v in CATEGORIAS.items():
        g = [s for s in sw if s["categoria"] == k]
        o.append(f"## {v}\n")
        o.append("| Software | Para quem | O que faz | Ferramenta | Receita | Estado | Oferta | Módulos |\n|---|---|---|---|---|---|---|---|")
        for s in g:
            of = ofs[s["oferta"]]["nome"] if s.get("oferta") else "—"
            o.append(f"| **{esc(s['nome'])}** | {esc(s['publico'])} | {esc(s['faz'])} | {FERRAMENTAS[s['ferramenta']]} | {esc(s['receita'])} | "
                     f"{ESTADOS[s['estado']]} | {esc(of)} | {esc(', '.join(mn[m] for m in s['modulos']))} |")
        o.append("")
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d = carregar()
    erros = validar(d)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    t = gerar_md(d)
    if a.check:
        if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
            print("docs/operacao/softwares.md está desatualizado. Rode: python tools/softwares/softwares.py", file=sys.stderr)
            return 1
        print(f"Catálogo de softwares em dia: {len(d['softwares'])} softwares, {len(d['modulos'])} módulos.")
        return 0
    MD.write_text(t, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
