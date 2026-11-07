#!/usr/bin/env python3
"""Faz o Claude Code responder em voz: hook "Stop" que lê a última resposta e fala com o Piper (local).

O Claude Code já ouve (comando /voice). Este hook fecha o ciclo: quando ele termina uma resposta, o texto é
limpo (código, links e tabelas viram uma frase curta) e falado pela voz local, sem mandar nada para a nuvem.

Instalação (Ubuntu): pipx install piper-tts e baixe uma voz pt_BR (ex.: pt_BR-faber-medium.onnx) em
~/.local/share/piper. Depois, em ~/.claude/settings.json:

    {"hooks": {"Stop": [{"hooks": [{"type": "command",
        "command": "python3 ~/dev/dev-setup/tools/jarvis/falar.py"}]}]}}

    python3 tools/jarvis/falar.py --teste             # fala uma frase de teste
    python3 tools/jarvis/falar.py --texto "Olá, Alan"  # fala o texto
    JARVIS_MUDO=1                                       # desliga a voz sem mexer no settings.json

Nunca quebra o Claude Code: sem Piper, sem voz ou sem áudio, sai em silêncio com código 0.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LIMITE = 450  # caracteres falados; o resto fica na tela
VOZES = Path(os.environ.get("JARVIS_VOZES", Path.home() / ".local" / "share" / "piper"))


def ultima_resposta(transcript: Path) -> str:
    """Texto da última mensagem do assistente no transcript (JSONL) do Claude Code."""
    texto = ""
    for linha in transcript.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            item = json.loads(linha)
        except json.JSONDecodeError:
            continue
        if item.get("type") != "assistant":
            continue
        partes = (item.get("message") or {}).get("content") or []
        if isinstance(partes, str):
            partes = [{"type": "text", "text": partes}]
        atual = " ".join(p.get("text", "") for p in partes if isinstance(p, dict) and p.get("type") == "text").strip()
        if atual:
            texto = atual
    return texto


def limpar(texto: str, limite: int = LIMITE) -> str:
    """Deixa o texto bom de ouvir: sem blocos de código, tabelas, links crus nem símbolos de Markdown."""
    t = re.sub(r"```.*?```", " (deixei o código na tela) ", texto, flags=re.S)
    t = re.sub(r"^\s*\|.*\|\s*$", "", t, flags=re.M)              # linhas de tabela
    t = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", t)                 # [texto](link) -> texto
    t = re.sub(r"https?://\S+", "o link está na tela", t)
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"^\s{0,3}(#{1,6}|[-*+]|\d+\.)\s+", "", t, flags=re.M)  # títulos e marcadores
    t = re.sub(r"[*_~>#]", "", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > limite:
        corte = t[:limite]
        fim = max(corte.rfind(". "), corte.rfind("! "), corte.rfind("? "))
        t = (corte[: fim + 1] if fim > limite // 3 else corte.rsplit(" ", 1)[0] + ".") + " O resto está na tela."
    return t


def achar_voz() -> Path | None:
    escolhida = os.environ.get("JARVIS_VOZ")
    if escolhida and Path(escolhida).exists():
        return Path(escolhida)
    vozes = sorted(VOZES.glob("pt_BR-*.onnx")) if VOZES.exists() else []
    return vozes[0] if vozes else None


def falar(texto: str) -> int:
    if not texto or os.environ.get("JARVIS_MUDO"):
        return 0
    piper, voz = shutil.which("piper"), achar_voz()
    tocador = shutil.which("paplay") or shutil.which("aplay")
    if not (piper and voz and tocador):
        return 0  # sem voz instalada: só não fala
    with tempfile.TemporaryDirectory() as pasta:
        wav = Path(pasta) / "resposta.wav"
        gerou = subprocess.run([piper, "-m", str(voz), "-f", str(wav)], input=texto, text=True,
                               capture_output=True, timeout=60, check=False)
        if gerou.returncode != 0 or not wav.exists():
            return 0
        subprocess.run([tocador, str(wav)], capture_output=True, timeout=120, check=False)
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Voz das respostas do Claude Code")
    ap.add_argument("--teste", action="store_true", help="fala uma frase de teste")
    ap.add_argument("--texto", help="fala este texto")
    a = ap.parse_args(argv)
    if a.teste:
        return falar("Oi, Alan. A voz do Jarvis está funcionando.")
    if a.texto:
        return falar(limpar(a.texto))
    try:
        evento = json.loads(sys.stdin.read() or "{}")
        caminho = Path(evento.get("transcript_path", "")).expanduser()
        if evento.get("stop_hook_active") or not caminho.is_file():
            return 0
        return falar(limpar(ultima_resposta(caminho)))
    except Exception:  # um hook nunca pode travar o Claude Code
        return 0


if __name__ == "__main__":
    sys.exit(main())
