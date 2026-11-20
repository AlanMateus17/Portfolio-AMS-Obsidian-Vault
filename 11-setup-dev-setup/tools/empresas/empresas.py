#!/usr/bin/env python3
"""Empresas do Grupo AMtech Digital: valida data/empresas.json contra o portfólio e os softwares e gera
docs/empresas.md (visão interna) e docs/vitrines/<empresa>.md (o que mostrar ao cliente).

Cada empresa tem produtos principais no raciocínio do AM Gestão: um produto junta componentes (ofertas do
portfolio.json ou uma suíte do softwares.json) e é vendido em pacotes.

    python3 tools/empresas/empresas.py          # regenera
    python3 tools/empresas/empresas.py --check  # falha se algo estiver desatualizado ou inconsistente (CI)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
EMPRESAS = RAIZ / "data" / "empresas.json"
PORTFOLIO = RAIZ / "data" / "portfolio.json"
SOFTWARES = RAIZ / "data" / "softwares.json"
SAIDA = RAIZ / "docs" / "empresas.md"
VITRINES = RAIZ / "docs" / "vitrines"
AVISO = "<!-- Arquivo GERADO por tools/empresas/empresas.py a partir de data/empresas.json. Não edite à mão. -->\n"
ESTADOS = {"ativa": "Ativa", "pausada": "Pausada", "software-primeiro": "Software primeiro, empresa depois"}
VEREDITO = {"agora": "agora", "proxima": "próxima", "manter": "manter", "fila": "fila", "em2027": "2027",
            "decidir": "decidir", "descartar": "descartada"}
SITE = "https://alanmateus17.github.io"


def carregar() -> tuple[dict, dict, dict]:
    ler = lambda p: json.loads(p.read_text(encoding="utf-8"))  # noqa: E731
    return ler(EMPRESAS), ler(PORTFOLIO), ler(SOFTWARES)


def dono_das_ofertas(e: dict, p: dict) -> dict[str, str]:
    por_frente = {f: x["id"] for x in e["empresas"] for f in x["frentes"]}
    return {o["id"]: por_frente.get(o["frente"], "") for o in p["ofertas"]}


def validar(e: dict, p: dict, s: dict) -> list[str]:
    erros, vistas, usadas = [], {}, {}
    ofs = {o["id"]: o for o in p["ofertas"]}
    suites = {x["id"] for x in s.get("suites", [])}
    for x in e["empresas"]:
        if x["estado"] not in ESTADOS:
            erros.append(f"{x['id']}: estado inválido {x['estado']}")
        if x["estado"] == "software-primeiro" and not all(x.get(k) for k in ("fase1", "fase2", "gatilho")):
            erros.append(f"{x['id']}: software primeiro precisa de fase1, fase2 e gatilho")
        for k in ("para_quem", "problema", "faz"):
            if not str(x.get(k, "")).strip():
                erros.append(f"{x['id']}: sem {k} (a vitrine do cliente precisa)")
        for f in x["frentes"]:
            if f not in p["frentes"]:
                erros.append(f"{x['id']}: frente inexistente {f}")
            if f in vistas:
                erros.append(f"frente {f} em duas empresas ({vistas[f]} e {x['id']})")
            vistas[f] = x["id"]
        if not x.get("produtos"):
            erros.append(f"{x['id']}: sem produtos")
        for pr in x.get("produtos", []):
            if not pr.get("resolve", "").strip():
                erros.append(f"{x['id']}/{pr['id']}: sem o que resolve")
            if pr.get("suite") and pr["suite"] not in suites:
                erros.append(f"{x['id']}/{pr['id']}: suíte inexistente {pr['suite']}")
            elif pr.get("suite") and pr.get("pacotes"):
                n = len(next(y for y in s["suites"] if y["id"] == pr["suite"])["pacotes"])
                if len(pr["pacotes"]) != n:
                    erros.append(f"{x['id']}/{pr['id']}: {len(pr['pacotes'])} pacotes para o cliente, mas a suíte tem {n}")
            for c in pr["componentes"]:
                if c not in ofs:
                    erros.append(f"{x['id']}/{pr['id']}: componente inexistente {c}")
                    continue
                if ofs[c]["frente"] not in x["frentes"]:
                    erros.append(f"{x['id']}/{pr['id']}: {c} é da frente {ofs[c]['frente']}, de outra empresa")
                if c in usadas:
                    erros.append(f"{c} está em dois produtos ({usadas[c]} e {pr['id']})")
                usadas[c] = pr["id"]
            if not pr.get("suite") and not pr["componentes"]:
                erros.append(f"{x['id']}/{pr['id']}: produto sem componentes")
    for f in p["frentes"]:
        if f not in vistas and f not in e.get("fora", {}):
            erros.append(f"frente {f} sem empresa (ponha numa empresa ou em 'fora' com o motivo)")
    return erros


def _pacotes(pr: dict, s: dict) -> list[dict]:
    """Os pacotes escritos para o cliente; sem eles, os da suíte do softwares.json."""
    if pr.get("pacotes"):
        return pr["pacotes"]
    if pr.get("suite"):
        nome = {x["id"]: x["nome"].split(" (")[0] for x in s["softwares"]}
        su = next(x for x in s["suites"] if x["id"] == pr["suite"])
        return [{"nome": pc["nome"], "inclui": ", ".join(nome[i] for i in pc["sistemas"])} for pc in su["pacotes"]]
    return pr.get("pacotes", [])


def gerar(e: dict, p: dict, s: dict) -> str:
    dono = dono_das_ofertas(e, p)
    ofs = {o["id"]: o for o in p["ofertas"]}
    nome_sw = {x["id"]: x["nome"].split(" (")[0] for x in s["softwares"]}
    o = [AVISO, f"# Empresas do {e['grupo']}\n", "[← Índice da documentação](../README.md)\n",
         f"**Regra:** {e['regra']}\n",
         "O que mostrar ao cliente está em [vitrines](vitrines/README.md), uma página por empresa.\n",
         "## A sequência\n", "| Etapa | Empresa | Estado | Produtos principais |\n|---:|---|---|---|"]
    for x in sorted(e["empresas"], key=lambda x: x["etapa"]):
        o.append(f"| {x['etapa']} | [{x['nome']}](#{x['id']}) | {ESTADOS[x['estado']]} | {', '.join(pr['nome'] for pr in x['produtos'])} |")
    o.append("")
    for x in e["empresas"]:
        o.append(f'<a id="{x["id"]}"></a>\n')
        o.append(f"## {x['nome']}\n")
        o.append(f"**{ESTADOS[x['estado']]}** · etapa {x['etapa']}. {x['faz']}.\n")
        if x["estado"] == "software-primeiro":
            o.append(f"1. **Primeiro, software:** {x['fase1']}.")
            o.append(f"2. **Depois, empresa:** {x['fase2']}.")
            o.append(f"3. **Quando vira empresa:** {x['gatilho']} (a decisão é sua).\n")
        for pr in x["produtos"]:
            o.append(f"### {pr['nome']}\n")
            o.append(f"*{pr['estado']}.* {pr['resolve']}\n")
            comp = [ofs[c]["nome"] for c in pr["componentes"]]
            if pr.get("suite"):
                su = next(y for y in s["suites"] if y["id"] == pr["suite"])
                comp = [nome_sw[i] for i in su["sistemas"]] + comp
            if comp:
                o.append(f"- **Componentes:** {'; '.join(comp)}")
            pcs = _pacotes(pr, s)
            if pcs:
                o.append("- **Pacotes:** " + " · ".join(pc["nome"] for pc in pcs))
            o.append("")
        soltas = [of for of in p["ofertas"] if dono[of["id"]] == x["id"]
                  and not any(of["id"] in pr["componentes"] for pr in x["produtos"]) and of["veredito"] != "descartar"]
        if soltas:
            o.append("**Outras ofertas da empresa, fora dos produtos principais** (candidatas a corte ou a virar componente):\n")
            o += [f"- {of['nome']} ({VEREDITO[of['veredito']]})" for of in sorted(soltas, key=lambda q: q["nome"])]
            o.append("")
    for f, motivo in e.get("fora", {}).items():
        o.append(f"**Fora das empresas — {p['frentes'][f]}:** {motivo}.\n")
    return "\n".join(o)


def gerar_vitrine(x: dict, s: dict) -> str:
    """Página para o cliente: sem veredito, onda ou número interno; só problema, solução, produtos e pacotes."""
    o = [AVISO, f"# {x['nome']}\n", f"**{x['faz']}.**\n", "## Para quem é\n", f"{x['para_quem']}.\n",
         "## O problema\n", f"{x['problema']}\n", "## Como resolvemos\n"]
    for pr in x["produtos"]:
        nome = pr["nome"].replace(" (nome provisório)", "").replace(" (renda ativa)", "")
        o.append(f"### {nome}\n")
        o.append(f"{pr['resolve']}\n")
        pcs = _pacotes(pr, s)
        if pcs:
            o.append("| Pacote | O que inclui |\n|---|---|")
            o += [f"| {pc['nome']} | {pc['inclui']} |" for pc in pcs]
            o.append("")
        if any(w in pr["estado"] for w in ("depois", "fase 2", "onda", "fila", "pausada", "construção")):
            o.append(f"*Situação: {pr['estado']}.*\n")
    o.append("## Fale com a gente\n")
    o.append(f"{x['nome']} é uma empresa do Grupo AMtech Digital, de Alan Mateus (Barbacena, MG). Contato e portfólio: {SITE}\n")
    return "\n".join(o)


def saidas(e: dict, p: dict, s: dict) -> dict[Path, str]:
    out = {SAIDA: gerar(e, p, s)}
    idx = [AVISO, "# Vitrines para clientes\n", "[← Empresas do grupo](../empresas.md)\n",
           "Uma página por empresa, para mostrar e explicar ao cliente o que a empresa e cada produto resolvem. "
           "Cada uma vira o README do repositório público da empresa (`just vitrine EMPRESA DESTINO`).\n"]
    for x in e["empresas"]:
        out[VITRINES / f"{x['id']}.md"] = gerar_vitrine(x, s)
        idx.append(f"- [{x['nome']}]({x['id']}.md): {x['faz']}")
    out[VITRINES / "README.md"] = "\n".join(idx) + "\n"
    return out


def main() -> int:
    e, p, s = carregar()
    erros = validar(e, p, s)
    for x in erros:
        print("ERRO:", x, file=sys.stderr)
    if erros:
        return 1
    out = saidas(e, p, s)
    if "--check" in sys.argv:
        ruins = [c for c, t in out.items() if not c.exists() or c.read_text(encoding="utf-8") != t]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python3 tools/empresas/empresas.py", file=sys.stderr)
        if ruins:
            return 1
        print(f"Empresas em dia: {len(e['empresas'])}.")
        return 0
    VITRINES.mkdir(parents=True, exist_ok=True)
    for c, t in out.items():
        c.write_text(t, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
