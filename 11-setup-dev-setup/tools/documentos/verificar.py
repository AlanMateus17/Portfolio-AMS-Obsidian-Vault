#!/usr/bin/env python3
"""Confere (e corrige a formatação de) documentos .docx: TCC e trabalhos pela ABNT, ou documentos da escola.

    python3 tools/documentos/verificar.py tcc.docx                      # perfil ABNT: laudo na tela
    python3 tools/documentos/verificar.py tcc.docx --corrigir           # grava tcc-corrigido.docx (margens, A4, fonte, espaçamento)
    python3 tools/documentos/verificar.py planejamento.docx --perfil escola   # campos vazios, modelo, regras da Fábrica

Só formata e confere. Nunca escreve o trabalho de ninguém. Sem dependências externas.
ABNT (NBR 14724): A4; margens superior e esquerda 3 cm, inferior e direita 2 cm; fonte 12; espaçamento 1,5;
recuo de primeira linha 1,25 cm; numeração de página; sumário; referências.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

CM = 567  # twips por centímetro
A4 = (11906, 16838)
ABNT_MARGENS = {"top": 3, "left": 3, "bottom": 2, "right": 2}


def ler(docx: Path) -> dict[str, str]:
    with zipfile.ZipFile(docx) as z:
        return {n: z.read(n).decode("utf-8", errors="replace") for n in z.namelist() if n.endswith(".xml")}


def _attr(xml: str, tag: str, attr: str) -> str | None:
    m = re.search(rf"<w:{tag}\b[^>]*\bw:{attr}=\"([^\"]+)\"", xml)
    return m.group(1) if m else None


def texto(doc: str) -> str:
    return " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", doc))


def checar_abnt(partes: dict[str, str]) -> list[dict]:
    doc, est = partes.get("word/document.xml", ""), partes.get("word/styles.xml", "")
    itens = []

    def it(nome, ok, det=""):
        itens.append({"item": nome, "ok": bool(ok), "detalhe": det})

    w, h = _attr(doc, "pgSz", "w"), _attr(doc, "pgSz", "h")
    it("Papel A4", w and h and abs(int(w) - A4[0]) < 60 and abs(int(h) - A4[1]) < 60, f"{w}x{h} twips")
    for lado, cm in ABNT_MARGENS.items():
        v = _attr(doc, "pgMar", lado)
        it(f"Margem {lado} {cm} cm", v and abs(int(v) - cm * CM) <= 30, f"{int(v) / CM:.2f} cm" if v else "não definida")
    sz = _attr(est.split("</w:docDefaults>")[0], "sz", "val") if "docDefaults" in est else None
    it("Fonte 12 no texto", sz == "24", f"{int(sz) / 2:g} pt" if sz else "padrão do Word")
    fonte = _attr(est.split("</w:docDefaults>")[0], "rFonts", "ascii") if "docDefaults" in est else None
    it("Fonte Arial ou Times New Roman", fonte in ("Arial", "Times New Roman"), fonte or "não definida")
    linha = _attr(est.split("</w:docDefaults>")[0], "spacing", "line") if "docDefaults" in est else None
    it("Espaçamento 1,5", linha == "360", f"{int(linha) / 240:g}" if linha else "padrão do Word")
    it("Recuo de primeira linha 1,25 cm", re.search(r'w:firstLine="(70[0-9]|71[0-9])"', doc + est), "")
    cab = "".join(v for k, v in partes.items() if "header" in k or "footer" in k)
    it("Numeração de página", "PAGE" in cab, "")
    it("Sumário", "TOC" in doc or "SUMÁRIO" in texto(doc).upper(), "")
    it("Seção de referências", "REFERÊNCIAS" in texto(doc).upper(), "")
    return itens


def checar_escola(partes: dict[str, str], max_obj: int = 3) -> list[dict]:
    t = texto(partes.get("word/document.xml", ""))
    itens = []
    restos = re.findall(r"\{\{[^}]*\}\}", t)
    faltas = re.findall(r"\[FALTA: [^\]]+\]", t)
    itens.append({"item": "Todos os campos do modelo preenchidos", "ok": not restos and not faltas,
                  "detalhe": ", ".join((restos + faltas)[:5])})
    itens.append({"item": "Sem dados pessoais de aluno (CPF, matrícula, nota individual)",
                  "ok": not re.search(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|matr[íi]cula\s*:?\s*\d", t, re.I), "detalhe": ""})
    obj = re.search(r"objetivos?(.{0,600})", t, re.I)
    n = len(re.findall(r"(?:^|\s)(?:\d+[.)]|•|-)\s", obj.group(1))) if obj else 0
    itens.append({"item": f"No máximo {max_obj} objetivos", "ok": n <= max_obj, "detalhe": f"{n} encontrados" if n else ""})
    itens.append({"item": "Documento não está vazio", "ok": len(t.split()) > 30, "detalhe": f"{len(t.split())} palavras"})
    return itens


def corrigir_abnt(docx: Path, saida: Path) -> None:
    mar = f'<w:pgMar w:top="{3 * CM}" w:right="{2 * CM}" w:bottom="{2 * CM}" w:left="{3 * CM}" w:header="708" w:footer="708" w:gutter="0"/>'
    with zipfile.ZipFile(docx) as zin, zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            d = zin.read(item.filename)
            if item.filename == "word/document.xml":
                s = d.decode("utf-8")
                s = re.sub(r"<w:pgSz\b[^>]*/>", f'<w:pgSz w:w="{A4[0]}" w:h="{A4[1]}"/>', s)
                s = re.sub(r"<w:pgMar\b[^>]*/>", mar, s) if "<w:pgMar" in s else s.replace("</w:sectPr>", mar + "</w:sectPr>")
                d = s.encode("utf-8")
            elif item.filename == "word/styles.xml":
                s = d.decode("utf-8")
                padrao = ('<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
                          '<w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>'
                          '<w:spacing w:line="360" w:lineRule="auto"/><w:jc w:val="both"/></w:pPr></w:pPrDefault></w:docDefaults>')
                s = re.sub(r"<w:docDefaults>.*?</w:docDefaults>", padrao, s, flags=re.S) if "<w:docDefaults>" in s else re.sub(r"(<w:styles\b[^>]*>)", r"\1" + padrao, s, count=1)
                d = s.encode("utf-8")
            zout.writestr(item, d)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--perfil", choices=["abnt", "escola"], default="abnt")
    ap.add_argument("--corrigir", action="store_true")
    a = ap.parse_args()
    p = Path(a.docx).expanduser()
    if a.corrigir:
        if a.perfil != "abnt":
            print("Correção automática só no perfil ABNT.", file=sys.stderr)
            return 1
        saida = p.with_name(p.stem + "-corrigido.docx")
        corrigir_abnt(p, saida)
        print(f"Gravado {saida} (confira sumário, numeração e referências: essas o script só aponta).")
        p = saida
    partes = ler(p)
    itens = checar_abnt(partes) if a.perfil == "abnt" else checar_escola(partes)
    ok = sum(i["ok"] for i in itens)
    for i in itens:
        print(f"{'OK      ' if i['ok'] else 'CORRIGIR'} {i['item']}{' · ' + i['detalhe'] if i['detalhe'] else ''}")
    print(f"\n{ok} de {len(itens)} itens em ordem.")
    return 0 if ok == len(itens) else 1


if __name__ == "__main__":
    sys.exit(main())
