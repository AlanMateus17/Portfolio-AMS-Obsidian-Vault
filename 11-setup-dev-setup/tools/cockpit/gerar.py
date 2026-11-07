#!/usr/bin/env python3
"""Gera o painel do Núcleo AMtech (docs/cockpit.html): a constelação do setup inteiro num lugar só.

Lê os mesmos dados de sempre (data/ecossistema.json, data/implantacao.json, data/portfolio.json) e as tabelas
do ADR 0008 (principal e reserva) e do docs/nucleo/README.md (autonomia, fases, o que já roda sozinho).
Nada é escrito à mão no painel: mudou o dado, mudou o painel.

    python3 tools/cockpit/gerar.py           # regenera
    python3 tools/cockpit/gerar.py --check   # CI: falha se o painel estiver desatualizado
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MODELO = Path(__file__).resolve().parent / "cockpit.template.html"
SAIDA = RAIZ / "docs" / "cockpit.html"
FASES_NUCLEO = ("f-solo", "f-nucleo", "f-soberania", "f-sprint")


def ler_json(nome: str) -> dict:
    return json.loads((RAIZ / "data" / f"{nome}.json").read_text(encoding="utf-8"))


def tabela(md: str, titulo: str) -> list[list[str]]:
    """Linhas da primeira tabela Markdown depois do título (sem cabeçalho e separador)."""
    i = md.find(titulo)
    if i < 0:
        raise ValueError(f"seção não encontrada: {titulo}")
    linhas = []
    for ln in md[i:].splitlines()[1:]:
        s = ln.strip()
        if s.startswith("|"):
            linhas.append([c.strip() for c in s.strip("|").split("|")])
        elif linhas:
            break
    return [l for l in linhas[2:] if any(l)]


def limpar(txt: str) -> str:
    """Tira a marcação Markdown simples (negrito, código, links) para o texto ir puro ao painel."""
    txt = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", txt)
    return txt.replace("**", "").replace("`", "")


def montar() -> dict:
    eco, imp, port = ler_json("ecossistema"), ler_json("implantacao"), ler_json("portfolio")
    ordem = [c["id"] for c in eco["camadas"]]
    passos, onde = [], {}
    fases = []
    for fi, f in enumerate(imp["fases"]):
        minutos = sum(p["tempo_min"] for p in f["passos"])
        fases.append({"id": f["id"], "t": f["titulo"], "q": f["quando"], "n": len(f["passos"]), "h": round(minutos / 60, 1),
                      "g": bool(f.get("gatilho")), "nuc": f["id"] in FASES_NUCLEO,
                      "compra": sum(1 for p in f["passos"] if "compra" in p.get("precisa", [])),
                      "pago": sum(1 for p in f["passos"] if "pagamento" in p.get("precisa", []))})
        for pj, p in enumerate(f["passos"], 1):
            passos.append([f"{fi}.{pj}", p["titulo"], fi])
            for b in p.get("blocos", []):
                onde.setdefault(b, []).append(len(passos) - 1)
    blocos = [{"id": b["id"], "c": ordem.index(b["camada"]), "r": b["rotulo"].replace("|", " "), "t": b["tipo"],
               "f": b["futuro"], "k": b["conta"], "d": b["descricao"], "o": onde.get(b["id"], [])} for b in eco["blocos"]]
    adr = (RAIZ / "docs" / "adr" / "0008-trocas-de-ferramenta-principal.md").read_text(encoding="utf-8")
    nuc = (RAIZ / "docs" / "nucleo" / "README.md").read_text(encoding="utf-8")
    ofertas = port["ofertas"]
    return {
        "camadas": [{"id": c["id"], "t": c["titulo"]} for c in eco["camadas"]],
        "blocos": blocos,
        "conexoes": [[c["de"], c["para"], c["rotulo"]] for c in eco["conexoes"]],
        "fases": fases,
        "passos": passos,
        "trocas": [[limpar(x) for x in l] for l in tabela(adr, "## Trocas")],
        "mantidas": [[limpar(x) for x in l] for l in tabela(adr, "## Mantidas")],
        "autonomia": [[limpar(x) for x in l] for l in tabela(nuc, "## Níveis de autonomia")],
        "produto": [[limpar(x) for x in l] for l in tabela(nuc, "## Para que serve")],
        "nucleo": [[limpar(x) for x in l] for l in tabela(nuc, "## Fases")],
        "hoje": [[limpar(x) for x in l] for l in tabela(nuc, "## Hoje")],
        "ofertas": {"total": len(ofertas), "agora": sum(1 for o in ofertas if o.get("veredito") == "agora"),
                    "auto": round(sum(o.get("automacao", 0) for o in ofertas) / max(1, len(ofertas)))},
    }


def gerar() -> str:
    dados = json.dumps(montar(), ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return MODELO.read_text(encoding="utf-8").replace("/*DADOS*/null", dados)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    html = gerar()
    if args.check:
        if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != html:
            print("docs/cockpit.html está desatualizado. Rode: python3 tools/cockpit/gerar.py", file=sys.stderr)
            return 1
        print("Painel do Núcleo em dia.")
        return 0
    SAIDA.write_text(html, encoding="utf-8")
    print(f"Gerado {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
