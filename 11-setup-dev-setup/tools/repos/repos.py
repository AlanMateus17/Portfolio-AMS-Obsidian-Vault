#!/usr/bin/env python3
"""Gera docs/repositorios.md a partir de repos.json: todos os repositórios do Alan, por status, com o papel de cada um.

    python3 tools/repos/repos.py          # regenera
    python3 tools/repos/repos.py --check  # falha se estiver desatualizado (CI)

O mesmo texto serve de README do perfil do GitHub (repositório AlanMateus17/AlanMateus17).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "repos.json"
SAIDA = RAIZ / "docs" / "repositorios.md"
DONO = "AlanMateus17"
STATUS = {"planejado": "Planejados: criar quando a vez chegar", "ativo": "Ativos: em uso agora", "estudo": "Estudo: material e exercícios",
          "revisar": "A revisar: decidir se mantém ou funde", "arquivar": "Arquivar: estudo concluído"}
EMPRESAS_REPO = {"grupo": "Grupo (operação e estudo)", "software": "AMtech Software", "instituto": "Instituto AMS Silva",
                 "midia": "AMtech Mídia", "maker": "AMtech Maker", "logistica": "AM Logística", "editora": "Editora AMS Silva",
                 "pessoal": "Pessoal"}
AVISO = "<!-- Arquivo GERADO por tools/repos/repos.py a partir de repos.json. Não edite à mão. -->\n"


def validar(d: dict) -> list[str]:
    erros, nomes = [], [r["nome"] for r in d["repos"]]
    if len(nomes) != len(set(nomes)):
        erros.append("repositório repetido em repos.json")
    for r in d["repos"]:
        if r.get("status") not in STATUS:
            erros.append(f"{r['nome']}: status inválido {r.get('status')}")
        if not str(r.get("papel", "")).strip():
            erros.append(f"{r['nome']}: sem papel")
        if r.get("empresa") not in EMPRESAS_REPO:
            erros.append(f"{r['nome']}: empresa inválida {r.get('empresa')}")
    return erros


def link(nome: str) -> str:
    cheio = nome if "/" in nome else f"{DONO}/{nome}"
    return f"[{nome.split('/')[-1]}](https://github.com/{cheio})"


def gerar(d: dict) -> str:
    o = [AVISO, "# Repositórios do Alan Mateus\n",
         "Tudo o que existe no GitHub e o que vai ser criado, por empresa, com o papel, o status e a visibilidade de cada repositório. "
         "Fonte: [`repos.json`](../repos.json); o plano em si está no `PLANO-UNICO-AMtech.md` do vault.\n",
         f"**Núcleo da stack:** {', '.join(d['nucleo_stack'])}. **Reserva:** {', '.join(d['reserva'])}.\n",
         "| Status | Quantos |\n|---|---:|"]
    o += [f"| {t} | {sum(r['status'] == k for r in d['repos'])} |" for k, t in STATUS.items()]
    o.append("")
    o.append("## Por empresa\n")
    o.append("| Empresa | Repositório | Para que serve | Status | Visibilidade |\n|---|---|---|---|---|")
    for k, t in EMPRESAS_REPO.items():
        for r in [r for r in d["repos"] if r["empresa"] == k]:
            o.append(f"| {t} | {link(r['nome'])} | {r['papel'].replace('|', '/')} | {r['status']} | {r.get('visibilidade', '—')} |")
    o.append("")
    p = d.get("produto_unico")
    if p:
        o.append(f"## Produto único: {p['nome']}\n")
        o.append("Ainda sem repositório próprio (nasce no trimestre 2 do plano).\n")
        o.append(f"- **Módulos:** {', '.join(p['modulos'])}")
        o.append(f"- **MVP:** {', '.join(p['mvp'])}")
        o.append(f"- **Stack:** {', '.join(p['stack'])}\n")
    return "\n".join(o)


def main() -> int:
    d = json.loads(DADOS.read_text(encoding="utf-8"))
    erros = validar(d)
    for e in erros:
        print("ERRO:", e, file=sys.stderr)
    if erros:
        return 1
    txt = gerar(d)
    if "--check" in sys.argv:
        if not SAIDA.exists() or SAIDA.read_text(encoding="utf-8") != txt:
            print("docs/repositorios.md está desatualizado. Rode: python3 tools/repos/repos.py", file=sys.stderr)
            return 1
        print(f"Repositórios em dia: {len(d['repos'])}.")
        return 0
    SAIDA.write_text(txt, encoding="utf-8")
    print(f"Gerado {SAIDA.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
