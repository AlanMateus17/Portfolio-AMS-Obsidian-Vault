#!/usr/bin/env python3
"""Monta o contexto do planejamento semanal a partir da ementa e das suas regras, pronto para o preencher.py.

    python tools/fabrica/plano_semanal.py ementa.toml regras.toml 12 > contexto-semana-12.toml

ementa.toml: [[semana]] numero, tema, objetivos (lista), habilidades (lista), recursos (lista), atividade.
regras.toml: as suas regras (modelo em tools/fabrica/modelos/regras.example.toml), como o máximo de objetivos.
"""
from __future__ import annotations

import sys
import tomllib
from pathlib import Path


def contexto(ementa: dict, regras: dict, n: int) -> dict:
    sem = next((s for s in ementa.get("semana", []) if int(s["numero"]) == n), None)
    if sem is None:
        raise SystemExit(f"Semana {n} não está na ementa.")
    max_obj = int(regras.get("max_objetivos", 3))
    obj = list(sem.get("objetivos", []))
    if len(obj) > max_obj:
        print(f"aviso: {len(obj)} objetivos; a sua regra é no máximo {max_obj}. Ficaram os {max_obj} primeiros.", file=sys.stderr)
        obj = obj[:max_obj]
    ctx = {
        "professor": regras.get("professor", ""), "escola": regras.get("escola", ""),
        "disciplina": ementa.get("disciplina", ""), "turma": ementa.get("turma", ""),
        "semana": n, "tema": sem["tema"], "objetivos": obj,
        "habilidades": sem.get("habilidades", []), "recursos": sem.get("recursos", []),
        "atividade": sem.get("atividade", ""), "avaliacao": sem.get("avaliacao", regras.get("avaliacao_padrao", "")),
        "essencial": sem.get("essencial", obj[0] if obj else ""),
    }
    return ctx


def para_toml(ctx: dict) -> str:
    linhas = []
    for k, v in ctx.items():
        if isinstance(v, list):
            linhas.append(f"{k} = [" + ", ".join('"' + str(x).replace('"', "'") + '"' for x in v) + "]")
        elif isinstance(v, int):
            linhas.append(f"{k} = {v}")
        else:
            linhas.append(f'{k} = "' + str(v).replace('"', "'") + '"')
    return "\n".join(linhas) + "\n"


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 1
    ementa = tomllib.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    regras = tomllib.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
    sys.stdout.write(para_toml(contexto(ementa, regras, int(sys.argv[3]))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
