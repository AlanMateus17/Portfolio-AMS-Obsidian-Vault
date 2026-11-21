#!/usr/bin/env python3
"""Verificador de coerência: compara todos os arquivos de texto dos seus repositórios com o plano atual
(data/coerencia.json) e diz, arquivo por arquivo, o que ficou velho e como atualizar.

    python3 tools/coerencia/coerencia.py                       # só o dev-setup (o que o just check e o CI rodam)
    python3 tools/coerencia/coerencia.py ~/dev/notas ~/dev/*   # qualquer repositório ou pasta
    python3 tools/coerencia/coerencia.py ~/dev/notas --corrigir   # troca sozinho o que tem troca segura
    python3 tools/coerencia/coerencia.py ~/dev/* --relatorio ~/dev/COERENCIA.md

Níveis: "erro" (contradiz uma decisão; o CI do dev-setup falha) e "revisar" (precisa do seu olho; só avisa).
Fica de fora o que é histórico (ADRs, CHANGELOG, ESTADO, 99-arquivo), o espelho da pasta 11 (regenerado pelo
setup) e o que cada regra permite (ex.: "sushiman" na sua biografia, "site de padaria" para clientes).
Mudou uma decisão? Edite data/coerencia.json primeiro; o verificador passa a cobrar o novo em todo lugar.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REGRAS = RAIZ / "data" / "coerencia.json"
TEXTO = {".md", ".txt", ".html", ".htm", ".json", ".yml", ".yaml", ".toml", ".py", ".sh", ".ps1", ".js", ".ts",
         ".tsx", ".css", ".csv", ".liquid", ".xml", ""}


@dataclass
class Achado:
    repo: str
    arquivo: str
    linha: int
    regra: str
    nivel: str
    trecho: str
    sugestao: str


def carregar(caminho: Path = REGRAS) -> dict:
    d = json.loads(caminho.read_text(encoding="utf-8"))
    d["_geral"] = re.compile(d["permitir_linhas"]) if d.get("permitir_linhas") else None
    for r in d["regras"]:
        r["_re"] = re.compile(r["padrao"])
        r["_ok"] = re.compile(r["permitir_linhas"]) if r.get("permitir_linhas") else None
    return d


def _glob_re(p: str) -> re.Pattern:
    """Glob com ** (qualquer número de pastas), * (dentro de uma pasta) e ? ; casa o caminho inteiro."""
    out, k = "", 0
    while k < len(p):
        if p.startswith("**/", k):
            out += "(?:.*/)?"; k += 3
        elif p.startswith("/**", k) and k + 3 == len(p):
            out += "(?:/.*)?"; k += 3
        elif p.startswith("**", k):
            out += ".*"; k += 2
        elif p[k] == "*":
            out += "[^/]*"; k += 1
        elif p[k] == "?":
            out += "[^/]"; k += 1
        else:
            out += re.escape(p[k]); k += 1
    return re.compile(out + "$")


def casa(rel: str, padroes: list[str]) -> bool:
    return any(_glob_re(p).match(rel) for p in padroes)


def arquivos(repo: Path) -> list[str]:
    try:
        out = subprocess.run(["git", "-C", str(repo), "ls-files"], capture_output=True, text=True, check=True).stdout.splitlines()
    except (subprocess.CalledProcessError, FileNotFoundError):
        out = [str(p.relative_to(repo)) for p in repo.rglob("*") if p.is_file()]
    return [f for f in out if Path(f).suffix.lower() in TEXTO and (repo / f).is_file()]


def verificar(repo: Path, d: dict, corrigir: bool = False) -> list[Achado]:
    achados = []
    for rel in arquivos(repo):
        if casa(rel, d["ignorar"]):
            continue
        p = repo / rel
        try:
            texto = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        novo = texto
        for r in d["regras"]:
            if casa(rel, r.get("permitir_arquivos", [])):
                continue
            linhas = novo.splitlines()
            for i, l in enumerate(linhas, 1):
                if not r["_re"].search(l) or (r["_ok"] and r["_ok"].search(l)) or (d["_geral"] and d["_geral"].search(l)):
                    continue
                if corrigir and r.get("troca"):
                    continue
                trecho = l.strip()
                trecho = trecho[:160] + ("…" if len(trecho) > 160 else "")
                achados.append(Achado(repo.name, rel, i, r["id"], r["nivel"], trecho,
                                      f"trocar por \"{r['troca']}\"" if r.get("troca") else r.get("sugestao", "")))
            if corrigir and r.get("troca"):
                novo = "\n".join(l if (r["_ok"] and r["_ok"].search(l)) or (d["_geral"] and d["_geral"].search(l))
                                 else r["_re"].sub(r["troca"], l) for l in novo.split("\n"))
        if corrigir and novo != texto:
            p.write_text(novo, encoding="utf-8")
            print(f"corrigido: {repo.name}/{rel}")
    return achados


def relatorio(achados: list[Achado], d: dict) -> str:
    o = [f"# Coerência com o plano de {d['versao']}\n", f"**Objetivo:** {d['objetivo']}\n",
         "**Decisões em vigor:**\n", *[f"- {x}" for x in d["decisoes"]], ""]
    if not achados:
        o.append("Tudo alinhado: nenhum arquivo contradiz o plano.\n")
        return "\n".join(o)
    erros = sum(a.nivel == "erro" for a in achados)
    o.append(f"**{len(achados)} trechos para atualizar** ({erros} erros, {len(achados) - erros} para revisar), "
             f"em {len({(a.repo, a.arquivo) for a in achados})} arquivos.\n")
    motivos = {r["id"]: r["motivo"] for r in d["regras"]}
    for repo in sorted({a.repo for a in achados}):
        o.append(f"## {repo}\n")
        for arq in sorted({a.arquivo for a in achados if a.repo == repo}):
            o.append(f"### {arq}\n")
            for a in (x for x in achados if x.repo == repo and x.arquivo == arq):
                o.append(f"- linha {a.linha} · **{a.nivel}** · {motivos[a.regra]} → {a.sugestao}\n  > {a.trecho.replace('|', '/')}")
            o.append("")
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("caminhos", nargs="*", type=Path, default=[RAIZ])
    ap.add_argument("--corrigir", action="store_true", help="aplica as trocas seguras (as que têm 'troca' na regra)")
    ap.add_argument("--relatorio", type=Path, help="grava o relatório em Markdown neste arquivo")
    ap.add_argument("--estrito", action="store_true", help="falha também com 'revisar'")
    a = ap.parse_args()
    d = carregar()
    achados = []
    for c in a.caminhos:
        if c.is_dir():
            achados += verificar(c.resolve(), d, a.corrigir)
    txt = relatorio(achados, d)
    if a.relatorio:
        a.relatorio.write_text(txt, encoding="utf-8")
        print(f"Relatório em {a.relatorio}")
    erros = [x for x in achados if x.nivel == "erro" or a.estrito]
    resumo = f"Coerência (plano de {d['versao']}): {len(achados)} trechos, {len([x for x in achados if x.nivel == 'erro'])} erros."
    if not a.relatorio:
        for x in achados:
            print(f"{x.nivel.upper():7} {x.repo}/{x.arquivo}:{x.linha} [{x.regra}] {x.sugestao}\n        {x.trecho}")
    print(resumo)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
