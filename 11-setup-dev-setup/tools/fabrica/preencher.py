#!/usr/bin/env python3
"""Preenche um modelo .docx da escola com os campos de um arquivo TOML. Sem dependências externas.

No modelo do Word, escreva os campos entre chaves duplas: {{turma}}, {{tema}}, {{objetivos}}...
    python tools/fabrica/preencher.py modelo-planejamento.docx contexto.toml planejamento-semana-12.docx

Listas no TOML viram linhas separadas. Campos que faltarem no TOML ficam marcados como [FALTA: campo].
Regra da Fábrica: nenhum dado de aluno (nome, nota, foto) entra no contexto; o script recusa campos com "aluno".
"""
from __future__ import annotations

import re
import sys
import tomllib
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

CAMPO = re.compile(r"\{\{((?:<[^>]+>|[^{}<])*?)\}\}")
PARTES = ("word/document.xml", "word/header", "word/footer")


def valor_xml(v) -> str:
    if isinstance(v, list):
        return "</w:t><w:br/><w:t>".join(escape(str(x)) for x in v)
    return escape(str(v))


def substituir(xml: str, ctx: dict) -> tuple[str, list[str]]:
    faltas = []

    def troca(m):
        nome = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if nome in ctx:
            return valor_xml(ctx[nome])
        faltas.append(nome)
        return escape(f"[FALTA: {nome}]")
    return CAMPO.sub(troca, xml), faltas


def validar_ctx(ctx: dict) -> None:
    proibidos = [k for k in ctx if "aluno" in k.lower()]
    if proibidos:
        raise SystemExit(f"Dados de aluno não entram na Fábrica: {', '.join(proibidos)}")


def preencher(modelo: Path, ctx: dict, saida: Path) -> list[str]:
    validar_ctx(ctx)
    faltas = []
    with zipfile.ZipFile(modelo) as zin, zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            dados = zin.read(item.filename)
            if item.filename.startswith(PARTES) and item.filename.endswith(".xml"):
                novo, f = substituir(dados.decode("utf-8"), ctx)
                faltas += f
                dados = novo.encode("utf-8")
            zout.writestr(item, dados)
    return faltas


def main() -> int:
    if len(sys.argv) != 4:
        print(__doc__)
        return 1
    modelo, ctx_p, saida = map(Path, sys.argv[1:])
    ctx = tomllib.loads(ctx_p.read_text(encoding="utf-8"))
    faltas = preencher(modelo, ctx, saida)
    print(f"Gerado {saida}" + (f" · campos sem valor: {', '.join(sorted(set(faltas)))}" if faltas else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
