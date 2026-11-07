#!/usr/bin/env python3
"""Gera o kit de sites (docs/operacao/kit-sites.md) a partir de data/kitsites.json e data/softwares.json.

Inclui pacotes, ficha do cliente, um prompt pronto por tipo de negócio para o Website Builder ou o Horizons,
checklist de entrega e o modelo do relatório mensal.

    python tools/kitsites/gerar.py           # regenera
    python tools/kitsites/gerar.py --check   # CI
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
KIT = RAIZ / "data" / "kitsites.json"
SW = RAIZ / "data" / "softwares.json"
MD = RAIZ / "docs" / "operacao" / "kit-sites.md"
AVISO = "<!-- Arquivo GERADO por tools/kitsites/gerar.py a partir de data/kitsites.json e data/softwares.json. Não edite à mão. -->\n"
FERR = {"builder": "Website Builder com IA", "horizons": "Horizons"}


def carregar():
    return json.loads(KIT.read_text(encoding="utf-8")), json.loads(SW.read_text(encoding="utf-8"))


def validar(kit: dict, sw: dict) -> list[str]:
    e = []
    if len(kit["pacotes"]) != 3:
        e.append("O kit tem exatamente 3 pacotes (Essencial, Negócio, Vendas).")
    sites = [s for s in sw["softwares"] if s["categoria"] == "site"]
    for s in sites:
        if s["ferramenta"] not in FERR:
            e.append(f"{s['id']}: site deve usar o Website Builder ou o Horizons")
    if not sites:
        e.append("Nenhum site por nicho no catálogo de softwares.")
    return e


def prompt(s: dict, mods: dict) -> str:
    funcs = ", ".join(mods[m].lower() for m in s["modulos"])
    return (f"Crie um site em português do Brasil para [NOME DO NEGÓCIO], {s['publico'].split(',')[0]} em [CIDADE]. "
            f"Objetivo: {s['faz'].lower()}. Seções e funções: {funcs}. "
            "Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. "
            "Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). "
            "Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). "
            "SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.")


def gerar(kit: dict, sw: dict) -> str:
    mods = {m["id"]: m["nome"] for m in sw["modulos"]}
    sites = [s for s in sw["softwares"] if s["categoria"] == "site"]
    o = [AVISO, "# Kit de sites com IA da Hostinger\n", "[← Operação do grupo](README.md)\n",
         f"Tudo o que um site de cliente precisa para sair em poucas horas e virar mensalidade: 3 pacotes, a ficha do cliente, "
         f"{len(sites)} prompts prontos (um por tipo de negócio), a conferência automática, o checklist de entrega e o relatório mensal. "
         "Contrato: [modelo](contrato-sites-modelo.md). Catálogo completo: [softwares](softwares.md).\n",
         "## Fluxo\n",
         "1. O cliente preenche a **ficha** (formulário).",
         "2. Você cola o **prompt do tipo de negócio** no Website Builder ou no Horizons, trocando os campos entre colchetes.",
         "3. `python tools/kitsites/conferir.py https://endereco-do-site --fotos` gera o laudo; corrija o que estiver em CORRIGIR.",
         "4. Siga o **checklist de entrega** e cadastre o cliente no CRM e no monitoramento.",
         "5. Todo mês o **relatório** sai sozinho; você só atende as mudanças do pacote.\n",
         "## Regras\n"]
    o += [f"- {r}" for r in kit["regras"]]
    o += ["", "## Pacotes\n", "| Pacote | Inclui | Mudanças por mês | Meta de horas suas por mês |", "|---|---|---:|---:|"]
    for p in kit["pacotes"]:
        o.append(f"| **{p['nome']}** | {'; '.join(p['inclui'])} | {p['mudancas_mes']} | {p['horas_mes_meta']} h |")
    o += ["", "Preço: taxa de criação + mensalidade. Defina os valores pela sua hora mínima e pelo tempo real medido nos 3 primeiros clientes.\n",
          "## Ficha do cliente\n", "| Campo | Tipo |", "|---|---|"]
    o += [f"| {c} | {t} |" for c, t in kit["ficha"]]
    o += ["", "## Prompts por tipo de negócio\n"]
    for s in sites:
        o += [f"### {s['nome']}\n", f"Ferramenta: **{FERR[s['ferramenta']]}** · Para: {s['publico']}\n", "```text", prompt(s, mods), "```\n"]
    o += ["## Checklist de entrega\n"] + [f"- [ ] {c}" for c in kit["checklist_entrega"]]
    o += ["", "## Relatório mensal (modelo)\n"] + [f"- {r}" for r in kit["relatorio"]]
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    kit, sw = carregar()
    e = validar(kit, sw)
    if e:
        print("\n".join("ERRO: " + x for x in e), file=sys.stderr)
        return 1
    t = gerar(kit, sw)
    if a.check:
        if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
            print("docs/operacao/kit-sites.md está desatualizado. Rode: python tools/kitsites/gerar.py", file=sys.stderr)
            return 1
        print("Kit de sites em dia.")
        return 0
    MD.write_text(t, encoding="utf-8")
    print(f"Gerado {MD.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
