#!/usr/bin/env python3
"""Resumo de um modelo IFC (BIM) sem instalar nada: esquema, pavimentos, elementos por tipo e quantidades.

    python3 tools/construcao/ifc_resumo.py casa.ifc            # resumo em Markdown
    python3 tools/construcao/ifc_resumo.py casa.ifc --json     # para outro programa (orçamento, painel)

Lê o arquivo IFC (formato STEP, IFC2x3 ou IFC4) como texto. Serve para conferir rápido um modelo que você
recebeu ou exportou (Bonsai, FreeCAD, Revit, Archicad): quantos pavimentos, paredes, lajes, pilares, portas,
e as quantidades que o próprio modelo traz (IfcElementQuantity: área, volume, comprimento).

Não calcula geometria. Se o modelo não exportou as quantidades, a tabela de quantidades vem vazia: exporte
com "quantidades base" ligadas, ou use o IfcOpenShell (ifcopenshell.util) para medir pela geometria.
Levantamento para orçamento de obra é responsabilidade do profissional habilitado; isto é conferência.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ELEMENTOS = {
    "IFCWALL": "Paredes", "IFCWALLSTANDARDCASE": "Paredes", "IFCSLAB": "Lajes e pisos", "IFCCOLUMN": "Pilares",
    "IFCBEAM": "Vigas", "IFCFOOTING": "Fundações", "IFCPILE": "Estacas", "IFCDOOR": "Portas", "IFCWINDOW": "Janelas",
    "IFCSTAIR": "Escadas", "IFCSTAIRFLIGHT": "Lances de escada", "IFCRAILING": "Guarda-corpos", "IFCROOF": "Coberturas",
    "IFCCOVERING": "Revestimentos", "IFCSPACE": "Ambientes", "IFCFURNISHINGELEMENT": "Mobiliário",
    "IFCFLOWSEGMENT": "Tubulações e dutos", "IFCPIPESEGMENT": "Tubulações e dutos", "IFCDUCTSEGMENT": "Tubulações e dutos",
    "IFCFLOWTERMINAL": "Pontos (louças, luminárias, tomadas)", "IFCSANITARYTERMINAL": "Pontos (louças, luminárias, tomadas)",
    "IFCLIGHTFIXTURE": "Pontos (louças, luminárias, tomadas)", "IFCOUTLET": "Pontos (louças, luminárias, tomadas)",
}
QUANTIDADES = {"IFCQUANTITYAREA": "m²", "IFCQUANTITYVOLUME": "m³", "IFCQUANTITYLENGTH": "m", "IFCQUANTITYCOUNT": "un",
               "IFCQUANTITYWEIGHT": "kg"}
ENTIDADE = re.compile(r"#(\d+)\s*=\s*(IFC[A-Z0-9_]+)\s*\((.*?)\)\s*;\s*$", re.S | re.M)


def argumentos(texto: str) -> list[str]:
    """Separa os argumentos do primeiro nível de uma entidade STEP, respeitando textos e parênteses."""
    out, atual, nivel, em_texto, i = [], [], 0, False, 0
    while i < len(texto):
        c = texto[i]
        if em_texto:
            atual.append(c)
            if c == "'":
                if i + 1 < len(texto) and texto[i + 1] == "'":  # aspas dobradas dentro do texto
                    atual.append("'")
                    i += 1
                else:
                    em_texto = False
        elif c == "'":
            em_texto = True
            atual.append(c)
        elif c == "(":
            nivel += 1
            atual.append(c)
        elif c == ")":
            nivel -= 1
            atual.append(c)
        elif c == "," and nivel == 0:
            out.append("".join(atual).strip())
            atual = []
        else:
            atual.append(c)
        i += 1
    out.append("".join(atual).strip())
    return out


def texto_step(valor: str) -> str:
    """'Térreo' -> Térreo; decodifica \\X2\\...\\X0\\ (acentos em IFC) e trata $ como vazio."""
    if not valor or valor in ("$", "*"):
        return ""
    if valor.startswith("'") and valor.endswith("'"):
        valor = valor[1:-1].replace("''", "'")
    def x2(m):
        h = m.group(1)
        return "".join(chr(int(h[k:k + 4], 16)) for k in range(0, len(h), 4))
    return re.sub(r"\\X2\\([0-9A-Fa-f]+)\\X0\\", x2, valor)


def numero(valor: str) -> float | None:
    m = re.search(r"-?\d+(?:\.\d*)?(?:E[-+]?\d+)?", valor or "", re.I)
    return float(m.group(0)) if m else None


def resumir(conteudo: str) -> dict:
    esquema = re.search(r"FILE_SCHEMA\s*\(\s*\(\s*'([^']+)'", conteudo)
    tipos: Counter = Counter()
    pavimentos, projeto = [], ""
    quantidades: dict[tuple[str, str], float] = defaultdict(float)
    for m in ENTIDADE.finditer(conteudo):
        tipo, args = m.group(2), m.group(3)
        if tipo in ELEMENTOS:
            tipos[ELEMENTOS[tipo]] += 1
        elif tipo == "IFCBUILDINGSTOREY":
            a = argumentos(args)
            elev = numero(a[9]) if len(a) > 9 else None
            pavimentos.append({"nome": texto_step(a[2]) if len(a) > 2 else "", "elevacao": elev})
        elif tipo == "IFCPROJECT":
            a = argumentos(args)
            projeto = texto_step(a[2]) if len(a) > 2 else ""
        elif tipo in QUANTIDADES:
            a = argumentos(args)
            v = numero(a[3]) if len(a) > 3 else None
            if v is not None:
                quantidades[(texto_step(a[0]), QUANTIDADES[tipo])] += v
    pavimentos.sort(key=lambda p: (p["elevacao"] is None, p["elevacao"] or 0))
    return {
        "esquema": esquema.group(1) if esquema else "desconhecido",
        "projeto": projeto,
        "pavimentos": pavimentos,
        "elementos": dict(sorted(tipos.items(), key=lambda kv: (-kv[1], kv[0]))),
        "quantidades": [{"nome": n, "unidade": u, "total": round(v, 3)} for (n, u), v in sorted(quantidades.items())],
    }


def markdown(r: dict, nome: str) -> str:
    o = [f"# Resumo do modelo IFC: {nome}", "", f"- Esquema: **{r['esquema']}**", f"- Projeto: {r['projeto'] or '(sem nome)'}",
         f"- Pavimentos: {len(r['pavimentos'])}", ""]
    if r["pavimentos"]:
        o += ["| Pavimento | Elevação |", "|---|---:|"]
        for p in r["pavimentos"]:
            elev = "" if p["elevacao"] is None else f"{p['elevacao']:.2f}"
            o.append(f"| {p['nome'] or '(sem nome)'} | {elev} |")
        o.append("")
    o += ["## Elementos", ""]
    if r["elementos"]:
        o += ["| Tipo | Quantidade |", "|---|---:|"] + [f"| {k} | {v} |" for k, v in r["elementos"].items()]
    else:
        o.append("Nenhum elemento construtivo encontrado.")
    o += ["", "## Quantidades que o modelo traz", ""]
    if r["quantidades"]:
        o += ["| Quantidade | Total | Unidade |", "|---|---:|---|"]
        o += [f"| {q['nome']} | {q['total']:.2f} | {q['unidade']} |" for q in r["quantidades"]]
    else:
        o.append("O modelo não exportou quantidades (IfcElementQuantity). Exporte com as quantidades base ligadas.")
    o += ["", "> Conferência rápida. Levantamento para orçamento é responsabilidade do profissional habilitado.", ""]
    return "\n".join(o)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Resumo de um modelo IFC")
    ap.add_argument("arquivo", type=Path)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        conteudo = a.arquivo.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        print(f"ERRO: não consegui ler {a.arquivo}: {e}", file=sys.stderr)
        return 1
    if "ISO-10303-21" not in conteudo[:200]:
        print("ERRO: não parece um IFC em texto (STEP). Arquivos .ifczip precisam ser descompactados antes.", file=sys.stderr)
        return 1
    r = resumir(conteudo)
    print(json.dumps(r, ensure_ascii=False, indent=1) if a.json else markdown(r, a.arquivo.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
