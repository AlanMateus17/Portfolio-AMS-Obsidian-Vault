#!/usr/bin/env python3
"""Decide, antes de gastar, qual IA usar numa tarefa e estima o tamanho em tokens.

Não mede tokens exatos (cada modelo conta diferente); dá uma estimativa de bolso (~4 caracteres = 1 token)
e aplica a regra do roteador: tarefa barata vai para o modelo local ou grátis, o Claude fica para o que é
difícil ou vai para cliente. Serve para você (ou um agente) escolherem a rota certa sem pensar.

    python3 tools/ia/tokens.py rota "revisar a arquitetura do AM Kaixara"
    python3 tools/ia/tokens.py tamanho arquivo.md           # estima os tokens de um texto
    echo "meu texto" | python3 tools/ia/tokens.py tamanho -

A regra está em data/custos.json (rotas_ia). Isto é um guia, não um limite: o teto de gasto real
fica no gateway LiteLLM e no ai-usagebar.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Palavra na tarefa -> rota sugerida. A primeira que casar vale.
REGRAS = [
    (("arquitetura", "revisar código", "revisão", "segurança", "cliente", "decisão", "projeto", "pentest", "contrato"),
     "forte", "Claude Pro: raciocínio longo e coerência com o repositório. Gasta mais; use quando vale."),
    (("código", "programar", "script", "corrigir", "teste", "refatorar", "bug"),
     "codigo", "Claude Code (ou Copilot para issue pequena): lê e muda o repositório com testes."),
    (("rascunho", "resumir", "resumo", "transcrever", "legenda", "traduzir", "em lote", "ideias"),
     "barato", "Modelo local (Ollama) ou DeepSeek/OpenRouter grátis: volume sem gastar o Claude."),
    (("pesquisar", "pesquisa", "fontes", "procurar", "buscar"),
     "pesquisa", "Perplexity ou Gemini grátis para buscar; Claude só para fechar a decisão."),
    (("aula", "ementa", "documento", "plano de aula", "slide"),
     "fontes", "NotebookLM/Gemini preso às fontes que você carrega; Claude só na revisão curta."),
]
PADRAO = ("local", "Comece no modelo local; só suba para o Claude se o resultado não servir.")


def rota(tarefa: str) -> tuple[str, str]:
    t = tarefa.lower()
    for palavras, nome, motivo in REGRAS:
        if any(p in t for p in palavras):
            return nome, motivo
    return PADRAO


def estimar_tokens(texto: str) -> int:
    # Estimativa de bolso: ~4 caracteres por token. Confirme no ai-usagebar.
    return max(1, round(len(texto) / 4))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Rota de IA e estimativa de tokens")
    sub = ap.add_subparsers(dest="acao", required=True)
    r = sub.add_parser("rota", help="qual IA usar nesta tarefa")
    r.add_argument("tarefa", nargs="+")
    t = sub.add_parser("tamanho", help="estima os tokens de um arquivo (ou - para a entrada padrão)")
    t.add_argument("arquivo")
    a = ap.parse_args(argv)
    if a.acao == "rota":
        nome, motivo = rota(" ".join(a.tarefa))
        print(f"{nome}: {motivo}")
    else:
        texto = sys.stdin.read() if a.arquivo == "-" else Path(a.arquivo).read_text(encoding="utf-8", errors="replace")
        n = estimar_tokens(texto)
        print(f"~{n} tokens (~{n // 1000 or '<1'} mil). Estimativa de bolso; confirme no ai-usagebar.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
