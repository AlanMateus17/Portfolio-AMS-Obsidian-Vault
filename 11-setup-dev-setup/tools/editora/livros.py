#!/usr/bin/env python3
"""Gera docs/editora/livros.md a partir de data/livros.json: cada livro da Editora AMS Silva, volume por volume,
com os capítulos ligados aos assuntos do mapa-de-estudo e o estado de cada um.

    python3 tools/editora/livros.py          # regenera
    python3 tools/editora/livros.py --check  # falha se estiver desatualizado ou se um capítulo apontar para assunto inexistente
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "livros.json"
MAPA = RAIZ / "data" / "professor" / "mapa-assuntos.json"
PORTFOLIO = RAIZ / "data" / "portfolio.json"
SAIDA = RAIZ / "docs" / "editora" / "livros.md"
AVISO = "<!-- Arquivo GERADO por tools/editora/livros.py a partir de data/livros.json. Não edite à mão. -->\n"
ESTADOS = {"notas": "esperando as suas notas", "rascunho": "rascunho seu", "escrito": "escrito", "revisado": "revisado"}


def validar(d: dict, assuntos: dict, ofertas: set[str]) -> list[str]:
    erros, vistos = [], {}
    for lv in d["livros"]:
        for vol in lv["volumes"]:
            for c in vol["capitulos"]:
                a = c["assunto"]
                if a not in assuntos:
                    erros.append(f"{lv['id']} vol. {vol['id']}: assunto {a} não existe no mapa")
                if a in vistos:
                    erros.append(f"{lv['id']}: assunto {a} em dois volumes ({vistos[a]} e {vol['id']})")
                vistos[a] = vol["id"]
                if c.get("estado", "notas") not in ESTADOS:
                    erros.append(f"{lv['id']} {a}: estado inválido {c.get('estado')}")
        for o in lv.get("derivados", []):
            if o not in ofertas:
                erros.append(f"{lv['id']}: derivado {o} não existe no portfólio")
    return erros


def gerar(d: dict, assuntos: dict, nomes: dict[str, str]) -> str:
    o = [AVISO, "# Livros da Editora AMS Silva\n", "[← Editora](README.md)\n",
         f"**Estado da editora:** {d['estado']}.\n", f"**Regra:** {d['regra']}\n"]
    for lv in d["livros"]:
        caps = [c for v in lv["volumes"] for c in v["capitulos"]]
        prontos = sum(c.get("estado", "notas") != "notas" for c in caps)
        o.append(f"## {lv['titulo']}\n")
        o.append(f"*{lv['subtitulo']}*\n")
        o.append(f"- **Para quem:** {lv['publico']}")
        o.append(f"- **Capítulos:** {len(caps)} em {len(lv['volumes'])} volumes; {prontos} com texto seu")
        o.append(f"- **O que sai dele:** {', '.join(nomes[x] for x in lv.get('derivados', []))}\n")
        for v in lv["volumes"]:
            o.append(f"### Volume {v['id']}: {v['tema']}\n")
            o.append("| # | Capítulo (assunto do mapa) | Etapa | Estado |\n|---:|---|---|---|")
            for i, c in enumerate(v["capitulos"], 1):
                t = assuntos[c["assunto"]]["titulo"] + (f" · {c['nota']}" if c.get("nota") else "")
                o.append(f"| {i} | {t.replace('|', '/')} | {c['assunto']} | {ESTADOS[c.get('estado', 'notas')]} |")
            o.append("")
    o.append("## Como um capítulo nasce\n")
    o.append("1. Estude o assunto pelo mapa-de-estudo e feche com a ficha: `just ficha ETAPA`, escrita por você, sem abrir o arquivo do mapa.")
    o.append("2. `just colher ETAPA` leva a explicação e o exemplo resolvido para a entrada de capítulos.")
    o.append("3. Você reescreve como capítulo do livro, no padrão de [rigor editorial](03-rigor-editorial.md).")
    o.append("4. Mude o estado do capítulo em `data/livros.json` (notas → rascunho → escrito → revisado).\n")
    return "\n".join(o)


def main() -> int:
    d = json.loads(DADOS.read_text(encoding="utf-8"))
    assuntos = json.loads(MAPA.read_text(encoding="utf-8"))["assuntos"]
    ofs = {x["id"]: x["nome"] for x in json.loads(PORTFOLIO.read_text(encoding="utf-8"))["ofertas"]}
    erros = validar(d, assuntos, set(ofs))
    for e in erros:
        print("ERRO:", e, file=sys.stderr)
    if erros:
        return 1
    txt = gerar(d, assuntos, ofs)
    if "--check" in sys.argv:
        if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != txt:
            print("docs/editora/livros.md está desatualizado. Rode: python3 tools/editora/livros.py", file=sys.stderr)
            return 1
        print("Livros em dia.")
        return 0
    SAIDA.write_text(txt, encoding="utf-8")
    print(f"Gerado {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
