#!/usr/bin/env python3
"""Departamento financeiro pessoal, local. Os dados ficam em ~/financas (FORA do repositório e do GitHub).

    python tools/financeiro/financeiro.py iniciar                 # cria ~/financas com os modelos
    python tools/financeiro/financeiro.py importar extrato.csv    # Nubank (conta ou cartão) ou CSV genérico
    python tools/financeiro/financeiro.py mes 2026-11             # resumo do mês por categoria e a cascata

Categorias: regras em ~/financas/regras.toml (palavra no histórico -> categoria).
Não é assessoria financeira: a ferramenta aplica as SUAS regras; as decisões são suas.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import shutil
import sqlite3
import sys
import tomllib
from datetime import datetime
from pathlib import Path

PASTA = Path.home() / "financas"
MODELOS = Path(__file__).resolve().parent / "modelos"


def conectar(pasta: Path = PASTA) -> sqlite3.Connection:
    pasta.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(pasta / "financas.db")
    db.execute("create table if not exists lanc (id text primary key, data text, descricao text, valor real, origem text, categoria text)")
    return db


def _data(s: str) -> str:
    for f in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(s.strip(), f).strftime("%Y-%m-%d")
        except ValueError:
            pass
    raise ValueError(f"data não reconhecida: {s}")


def _valor(s: str) -> float:
    s = s.strip().replace("R$", "").replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    return float(s)


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f))
    if not linhas:
        return []
    cab = {k.lower(): k for k in linhas[0]}
    out = []
    for r in linhas:
        if "title" in cab and "amount" in cab:  # fatura Nubank: valor positivo = gasto
            out.append({"data": _data(r[cab["date"]]), "descricao": r[cab["title"]], "valor": -_valor(r[cab["amount"]]), "origem": "cartao"})
        elif "descrição" in cab and "valor" in cab:  # extrato da conta Nubank
            out.append({"data": _data(r[cab["data"]]), "descricao": r[cab["descrição"]], "valor": _valor(r[cab["valor"]]), "origem": "conta"})
        elif {"data", "descricao", "valor"} <= set(cab):
            out.append({"data": _data(r[cab["data"]]), "descricao": r[cab["descricao"]], "valor": _valor(r[cab["valor"]]), "origem": "csv"})
        else:
            raise SystemExit("Formato de CSV não reconhecido. Colunas esperadas: data, descricao, valor.")
    return out


def categorizar(desc: str, regras: dict) -> str:
    d = desc.lower()
    for cat, palavras in regras.get("categorias", {}).items():
        if any(p.lower() in d for p in palavras):
            return cat
    return "Sem categoria"


def carregar_regras(pasta: Path = PASTA) -> dict:
    p = pasta / "regras.toml"
    return tomllib.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def importar(caminho: Path, db: sqlite3.Connection, regras: dict) -> int:
    novos = 0
    for r in ler_csv(caminho):
        chave = hashlib.sha256(f"{r['data']}|{r['descricao']}|{r['valor']}|{r['origem']}".encode()).hexdigest()[:20]
        cur = db.execute("insert or ignore into lanc values (?,?,?,?,?,?)",
                         (chave, r["data"], r["descricao"], r["valor"], r["origem"], categorizar(r["descricao"], regras)))
        novos += cur.rowcount
    db.commit()
    return novos


def resumo_mes(db: sqlite3.Connection, mes: str, caixas: dict | None = None) -> str:
    rows = db.execute("select categoria, sum(valor) from lanc where substr(data,1,7)=? group by categoria order by sum(valor)", (mes,)).fetchall()
    ent = sum(v for _, v in rows if v > 0)
    sai = -sum(v for _, v in rows if v < 0)
    o = [f"Mês {mes}", f"Entradas: R$ {ent:,.2f}", f"Saídas:   R$ {sai:,.2f}", f"Sobra:    R$ {ent - sai:,.2f}", "", "Por categoria:"]
    o += [f"  {c:<22} R$ {v:>10,.2f}" for c, v in rows]
    if caixas and ent - sai > 0:
        o += ["", "Cascata (pelas suas regras em caixas.toml):"]
        resto = ent - sai
        for cx in caixas.get("caixa", []):
            falta = max(0.0, float(cx["meta"]) - float(cx.get("atual", 0)))
            vai = min(resto, falta)
            o.append(f"  {cx['nome']:<28} recebe R$ {vai:,.2f} (falta R$ {falta - vai:,.2f})")
            resto -= vai
            if resto <= 0:
                break
        if resto > 0:
            o.append(f"  Sobra para a divisão final (ARCA, empresa, estudo, sonhos): R$ {resto:,.2f}")
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("iniciar")
    i = sp.add_parser("importar")
    i.add_argument("csv")
    m = sp.add_parser("mes")
    m.add_argument("mes")
    a = ap.parse_args()
    if a.cmd == "iniciar":
        PASTA.mkdir(exist_ok=True)
        for f in MODELOS.iterdir():
            alvo = PASTA / f.name.replace(".example", "")
            if not alvo.exists():
                shutil.copy(f, alvo)
                print("criado", alvo)
        return 0
    db = conectar()
    if a.cmd == "importar":
        print(f"{importar(Path(a.csv).expanduser(), db, carregar_regras())} lançamentos novos (repetidos são ignorados).")
        return 0
    cx = PASTA / "caixas.toml"
    print(resumo_mes(db, a.mes, tomllib.loads(cx.read_text(encoding="utf-8")) if cx.exists() else None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
