#!/usr/bin/env python3
"""Pacote de contexto curto para começar uma conversa NOVA com qualquer IA sem colar o mundo inteiro.

    python3 tools/sessao/contexto.py --passo ia-mcp          # um passo do roteiro, com tudo que ele precisa
    python3 tools/sessao/contexto.py --resumo                # estado geral do setup em poucas linhas
    python3 tools/sessao/contexto.py --inicio | clip.exe     # primeira mensagem de uma conversa nova (CONTINUAR.md + estado)
    python3 tools/sessao/contexto.py --passo fa-plano | clip.exe   # copia para a área de transferência do Windows

Conversa curta = limite que dura. Comece cada tarefa com este pacote; termine pedindo o resumo para o ESTADO.md.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REGRAS = RAIZ / "infra" / "templates" / "regras-ia" / "regras-ia.md"
ESTADO = RAIZ / "ESTADO.md"


def carregar():
    im = json.loads((RAIZ / "data" / "implantacao.json").read_text(encoding="utf-8"))
    eco = json.loads((RAIZ / "data" / "ecossistema.json").read_text(encoding="utf-8"))
    return im, {b["id"]: b for b in eco["blocos"]}


def regras_curtas(limite: int = 20) -> str:
    """Itens das regras, sem perder o sentido da seção: o que está em "## Nunca" sai com "NUNCA:" na frente."""
    linhas, secao = [], ""
    for l in REGRAS.read_text(encoding="utf-8").splitlines():
        if l.startswith("## "):
            secao = l[3:].strip().lower()
        elif l.startswith("- "):
            linhas.append("- NUNCA: " + l[2:] if secao == "nunca" else l)
    return "\n".join(linhas[:limite])


def pacote_passo(pid: str) -> str:
    im, B = carregar()
    for i, f in enumerate(im["fases"]):
        for j, p in enumerate(f["passos"], 1):
            if p["id"] == pid:
                o = [f"# Tarefa: passo {i}.{j} ({pid}) do roteiro do dev-setup", f"Fase: {f['titulo']} · {f.get('quando', '')}",
                     f"Objetivo da fase: {f.get('objetivo', '')}", f"Passo: {p['titulo']}", f"Pronto quando: {p['pronto']}"]
                if p.get("comando"):
                    o.append(f"Comando previsto: {p['comando']}")
                if p.get("fora"):
                    o.append(f"Fora do terminal: {p['fora']}")
                if p.get("nota"):
                    o.append(f"Nota: {p['nota']}")
                for b in p.get("blocos", []):
                    if b in B:
                        o.append(f"- Bloco {B[b]['rotulo'].replace('|', ' ')}: {B[b]['descricao']}")
                o += ["", "## Regras", regras_curtas(), "", "Responda só sobre este passo. No fim, me dê 5 linhas para o ESTADO.md."]
                return "\n".join(o)
    raise SystemExit(f"Passo {pid} não encontrado.")


def pacote_resumo() -> str:
    im, B = carregar()
    n = sum(len(f["passos"]) for f in im["fases"])
    log = subprocess.run(["git", "-C", str(RAIZ), "log", "--oneline", "-5"], capture_output=True, text=True).stdout.strip()
    o = [f"# Estado do dev-setup: {len(im['fases'])} fases, {n} passos, {len(B)} blocos", "", "Últimas mudanças:", log or "(sem git)"]
    if ESTADO.exists():
        o += ["", "ESTADO.md (decisões recentes):", "\n".join(ESTADO.read_text(encoding="utf-8").splitlines()[-15:])]
    o += ["", "## Regras", regras_curtas()]
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--passo")
    g.add_argument("--resumo", action="store_true")
    g.add_argument("--inicio", action="store_true", help="CONTINUAR.md + estado atual: primeira mensagem de uma conversa nova")
    a = ap.parse_args()
    if a.inicio:
        txt = (RAIZ / "CONTINUAR.md").read_text(encoding="utf-8") + "\n\n" + pacote_resumo()
    else:
        txt = pacote_passo(a.passo) if a.passo else pacote_resumo()
    sys.stdout.write(txt + "\n")
    print(f"\n(~{len(txt) // 4} tokens)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
