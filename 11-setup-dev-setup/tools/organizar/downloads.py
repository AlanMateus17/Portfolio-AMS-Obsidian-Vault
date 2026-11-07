#!/usr/bin/env python3
"""Organiza a pasta Downloads por tipo de arquivo. Por padrão só MOSTRA o que faria.

    python tools/organizar/downloads.py                       # simula na sua pasta Downloads do Windows
    python tools/organizar/downloads.py --aplicar             # move de verdade
    python tools/organizar/downloads.py --pasta ~/Downloads --aplicar

Nunca apaga nada. Arquivos de senha exportados (CSV do Chrome/Google) não são movidos:
o script avisa para importar no KeePassXC e apagar.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

TIPOS = {
    "Documentos": {".pdf", ".doc", ".docx", ".odt", ".txt", ".md", ".rtf", ".epub"},
    "Planilhas": {".xls", ".xlsx", ".ods", ".csv"},
    "Apresentacoes": {".ppt", ".pptx", ".odp", ".key"},
    "Imagens": {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".heic", ".bmp"},
    "Videos": {".mp4", ".mov", ".mkv", ".avi", ".webm"},
    "Audios": {".mp3", ".wav", ".m4a", ".ogg", ".flac"},
    "Compactados": {".zip", ".rar", ".7z", ".tar", ".gz", ".tgz"},
    "Instaladores": {".exe", ".msi", ".msix", ".appx", ".deb", ".appimage", ".iso"},
    "Codigo": {".py", ".js", ".ts", ".json", ".html", ".css", ".cs", ".sql", ".sh", ".ps1"},
}
SENHA = ("password", "senha", "passwords", "chrome passwords", "google passwords")


def pasta_padrao() -> Path:
    usuario = os.environ.get("USER", "")
    win = Path(f"/mnt/c/Users/{usuario}/Downloads")
    return win if win.exists() else Path.home() / "Downloads"


def destino(arq: Path) -> str | None:
    if arq.suffix.lower() == ".csv" and any(s in arq.stem.lower() for s in SENHA):
        return None
    for pasta, exts in TIPOS.items():
        if arq.suffix.lower() in exts:
            return pasta
    return "Outros"


def plano(pasta: Path) -> tuple[list[tuple[Path, Path]], list[Path]]:
    mover, senhas = [], []
    for a in sorted(pasta.iterdir()):
        if not a.is_file() or a.name.startswith("."):
            continue
        d = destino(a)
        if d is None:
            senhas.append(a)
            continue
        alvo = pasta / d / a.name
        n = 1
        while alvo.exists():
            alvo = pasta / d / f"{a.stem} ({n}){a.suffix}"
            n += 1
        mover.append((a, alvo))
    return mover, senhas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pasta")
    ap.add_argument("--aplicar", action="store_true")
    a = ap.parse_args()
    pasta = Path(a.pasta).expanduser() if a.pasta else pasta_padrao()
    if not pasta.is_dir():
        print(f"Pasta não encontrada: {pasta}", file=sys.stderr)
        return 1
    mover, senhas = plano(pasta)
    for o, d in mover:
        print(f"{'MOVIDO' if a.aplicar else 'moveria'}: {o.name} -> {d.parent.name}/")
        if a.aplicar:
            d.parent.mkdir(exist_ok=True)
            shutil.move(str(o), str(d))
    for s in senhas:
        print(f"ATENÇÃO: {s.name} parece exportação de senhas. Importe no KeePassXC e apague o arquivo.")
    print(f"{len(mover)} arquivos {'movidos' if a.aplicar else 'seriam movidos (use --aplicar)'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
