#!/usr/bin/env python3
"""Cria as tags de versão a partir do CHANGELOG, achando o commit de cada versão. Rode na sua máquina.

Lê cada "## [x.y.z]" do CHANGELOG.md, descobre o commit que introduziu aquela linha (foi o commit que
publicou a versão) e cria uma tag anotada vx.y.z nele.

    python3 tools/git/taguear.py                    # mostra o que faria (não cria nada)
    python3 tools/git/taguear.py --criar --push     # cria e envia TODAS as versões (precisa do histórico completo)
    python3 tools/git/taguear.py --ultima --criar --push   # só a versão mais nova (o que o hook de push usa)

O --ultima não precisa do histórico completo (o commit da versão nova é recente), por isso serve para rodar
sozinho a cada push, pelo hook em scripts/git-hooks/pre-push. O envio de tag não funciona de dentro de
algumas sessões (proxy de git); na sua máquina funciona.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
CHANGELOG = RAIZ / "CHANGELOG.md"
VERSAO = re.compile(r"^## \[(\d+\.\d+\.\d+)\]", re.M)


def versoes(texto: str) -> list[str]:
    """Versões do CHANGELOG, da mais antiga para a mais nova (a ordem de tagueamento)."""
    return list(reversed(VERSAO.findall(texto)))


def git(args: list[str], env: dict | None = None) -> str:
    e = {**os.environ, **env} if env else None
    return subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True, check=True, env=e).stdout.strip()


def tags_existentes() -> set[str]:
    return set(git(["tag"]).splitlines())


def commit_da_versao(versao: str) -> str | None:
    """O commit que ADICIONOU a linha '## [versao]' ao CHANGELOG (-S acha quem introduziu o texto)."""
    saida = git(["log", "--reverse", "--format=%H", "-S", f"## [{versao}]", "--", "CHANGELOG.md"])
    linhas = [l for l in saida.splitlines() if l.strip()]
    return linhas[0] if linhas else None


def planejar(texto: str, existentes: set[str], so_ultima: bool = False) -> list[tuple[str, str | None]]:
    vs = versoes(texto)
    if so_ultima:
        vs = vs[-1:]
    return [(v, commit_da_versao(v)) for v in vs if f"v{v}" not in existentes]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Cria tags de versão a partir do CHANGELOG")
    ap.add_argument("--criar", action="store_true", help="cria as tags (sem isto, só mostra)")
    ap.add_argument("--push", action="store_true", help="envia as tags criadas para o origin")
    ap.add_argument("--ultima", action="store_true", help="só a versão mais nova do CHANGELOG (usado pelo hook de push)")
    a = ap.parse_args(argv)
    try:
        git(["rev-parse", "--git-dir"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("ERRO: rode dentro do repositório, numa máquina com git.", file=sys.stderr)
        return 1
    # Taguear TODAS as versões precisa do histórico completo; só a última, não (o commit é recente).
    if not a.ultima and git(["rev-parse", "--is-shallow-repository"]) == "true":
        print("ERRO: o histórico está incompleto (clone raso). Rode antes: git fetch --unshallow", file=sys.stderr)
        print("      Sem isto, as versões antigas apontariam todas para o commit errado.", file=sys.stderr)
        return 1
    plano = planejar(CHANGELOG.read_text(encoding="utf-8"), tags_existentes(), so_ultima=a.ultima)
    if not plano:
        if not a.ultima:
            print("Todas as versões do CHANGELOG já estão tagueadas.")
        return 0
    criadas, faltou = [], 0
    for versao, commit in plano:
        if commit is None:
            print(f"AVISO  v{versao}: não achei o commit (falta histórico? git fetch --unshallow)", file=sys.stderr)
            faltou += 1
            continue
        if not a.criar:
            print(f"criaria v{versao} em {commit[:9]}")
            continue
        try:
            git(["tag", "-a", f"v{versao}", "-m", f"v{versao}", commit])
            print(f"OK     v{versao} em {commit[:9]}")
            criadas.append(f"v{versao}")
        except subprocess.CalledProcessError as e:
            print(f"ERRO   v{versao}: {getattr(e, 'stderr', e)}", file=sys.stderr)
            faltou += 1
    if a.criar and a.push and criadas:
        try:
            # AMTECH_SKIP_HOOK evita que o pre-push dispare de novo neste push de tag (recursão).
            git(["push", "origin", *(f"refs/tags/{t}" for t in criadas)], env={"AMTECH_SKIP_HOOK": "1"})
            print(f"{len(criadas)} tag(s) enviada(s): {', '.join(criadas)}")
        except subprocess.CalledProcessError as e:
            print(f"ERRO ao enviar as tags: {getattr(e, 'stderr', e)}", file=sys.stderr)
            return 1
    elif not a.criar:
        print(f"\n{len(plano)} tag(s) a criar. Rode com --criar (e --push para enviar).")
    return 1 if faltou else 0


if __name__ == "__main__":
    sys.exit(main())
