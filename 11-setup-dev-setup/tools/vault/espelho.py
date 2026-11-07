#!/usr/bin/env python3
"""Espelha o dev-setup dentro do seu vault do Obsidian (pasta 11-setup-dev-setup), para estudo e setup ficarem num lugar só.

A fonte da verdade é o repositório dev-setup (CI, testes, geradores). O vault recebe uma cópia dos arquivos versionados:
o que mudou é copiado, e o que saiu do setup sai do vault. Só sai o que o próprio espelho copiou antes (lista em
.espelho-manifesto): arquivo que você criou na pasta 11 nunca é apagado, só avisado. Não edite os arquivos copiados no
Obsidian: a próxima cópia desfaz. O índice da pasta (00-INDICE-DO-SETUP.md) é do vault e é regenerado aqui.

    python3 tools/vault/espelho.py                 # copia para ~/dev/notas/11-setup-dev-setup (ou AMTECH_VAULT)
    python3 tools/vault/espelho.py --simular       # só mostra o que mudaria
"""
from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTA = "11-setup-dev-setup"
INDICE = "00-INDICE-DO-SETUP.md"
MANIFESTO = ".espelho-manifesto"  # o que o espelho copiou da última vez; só isso pode ser removido


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def eh_vault(v: Path) -> bool:
    """O seu vault tem o Sumário Único na raiz; uma pasta qualquer não recebe o espelho."""
    return (v / "00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md").exists() or (v / "00-INICIO.md").exists()


def arquivos(raiz: Path = RAIZ) -> list[str]:
    saida = subprocess.run(["git", "-C", str(raiz), "ls-files"], capture_output=True, text=True, check=True).stdout
    return [f for f in saida.splitlines() if f and not f.startswith(".github/") and (raiz / f).is_file()]


def indice_md() -> str:
    return f"""---
tags: [setup, dev-setup, indice, espelho]
tipo: indice
atualizado: {date.today().isoformat()}
---

# Setup completo (dev-setup) dentro do vault

> **Espelho automático.** Esta pasta é uma cópia exata do repositório `dev-setup`, refeita a cada `just docs` e na
> manutenção de domingo. **Não edite aqui**: a próxima cópia desfaz. Para mudar o setup, mude o repositório
> (`~/dev/dev-setup`) ou peça ao Claude.

## Por onde começar

- **O que fazer hoje no setup:** no Ubuntu do WSL, `cd ~/dev/dev-setup && just agora`
- **O que estudar hoje:** `just professor hoje`. O método está em [docs/professor/metodo.md](docs/professor/metodo.md) e o plano de 12 meses em [docs/plano-eixo.md](docs/plano-eixo.md)
- **O roteiro inteiro:** [docs/implantacao/README.md](docs/implantacao/README.md)
- **As decisões (ADRs):** [docs/adr](docs/adr)
- **O que mudou:** [CHANGELOG.md](CHANGELOG.md)
"""


def espelhar(origem: Path, destino: Path, lista: list[str], simular: bool = False) -> dict[str, int]:
    n = {"novo": 0, "mudou": 0, "saiu": 0, "seus": 0}
    alvo = set(lista) | {INDICE, MANIFESTO}
    man = destino / MANIFESTO
    copiados_antes = set(man.read_text(encoding="utf-8").splitlines()) if man.exists() else set()
    for rel in lista:
        o, d = origem / rel, destino / rel
        if d.exists() and filecmp.cmp(o, d, shallow=False):
            continue
        n["mudou" if d.exists() else "novo"] += 1
        if not simular:
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(o, d)
    if destino.exists():
        for d in sorted(destino.rglob("*"), reverse=True):
            rel = d.relative_to(destino).as_posix()
            if d.is_file() and rel not in alvo:
                if rel not in copiados_antes:
                    n["seus"] += 1  # não veio do espelho: fica, e o aviso diz onde
                    print(f"aviso: {rel} não é do dev-setup e ficou na pasta 11; mova para outra pasta do vault", file=sys.stderr)
                    continue
                n["saiu"] += 1
                if not simular:
                    d.unlink()
            elif d.is_dir() and not simular and not any(d.iterdir()):
                d.rmdir()
    if not simular:
        destino.mkdir(parents=True, exist_ok=True)
        (destino / INDICE).write_text(indice_md(), encoding="utf-8")
        man.write_text("\n".join(sorted(lista)) + "\n", encoding="utf-8")
    return n


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--se-existir", action="store_true", help="sem vault, sai em silêncio (usado pelo just docs e pelo CI)")
    args = ap.parse_args(argv)
    v = vault()
    if not eh_vault(v):
        if args.se_existir:
            return 0
        print(f"Não achei o seu vault em {v}. Rode: bash scripts/wsl/vault.sh (clona o Portfolio-AMS-Obsidian-Vault).", file=sys.stderr)
        return 2
    n = espelhar(RAIZ, v / PASTA, arquivos(), args.simular)
    verbo = "mudaria" if args.simular else "espelho atualizado"
    extra = f", {n['seus']} seus mantidos" if n["seus"] else ""
    print(f"{v / PASTA}: {verbo} ({n['novo']} novos, {n['mudou']} mudados, {n['saiu']} removidos{extra}).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
