#!/usr/bin/env python3
"""Banco central do Núcleo AMtech (ADR 0009): eventos, conhecimento, tarefas e auditoria.

No notebook é um SQLite (~/.local/share/nucleo/nucleo.db, ou NUCLEO_DB); na VM, o mesmo modelo em PostgreSQL
(esquema-postgres.sql). Tudo o que o setup decide, garimpa e aprende entra aqui, e a triagem, o arquiteto e os
agentes consultam antes de agir.

    python3 tools/nucleo/nucleo.py iniciar                       # cria o banco e importa ADRs e recusas
    python3 tools/nucleo/nucleo.py lembrar "Kamal precisa de arch arm64 na t4g" --tipo licao --tags deploy
    python3 tools/nucleo/nucleo.py buscar "deploy arm"           # o que já se sabe sobre isso
    python3 tools/nucleo/nucleo.py contexto "deploy do AM Rendara"  # bloco curto para o pacote do arquiteto
    python3 tools/nucleo/nucleo.py evento venda.aprovada '{"oferta": "minicurso", "valor": 97}'
    python3 tools/nucleo/nucleo.py tarefa nova "Revisar PR do garimpo"   |   tarefa listar   |   tarefa feita 3
    python3 tools/nucleo/nucleo.py auditar claude-code "abriu PR" --nivel automatico --motivo "garimpo"
    python3 tools/nucleo/nucleo.py importar                      # reimporta ADRs e recusas (não duplica)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ESQUEMA = Path(__file__).resolve().parent / "esquema.sql"
TIPOS = ("adr", "triagem", "garimpo", "padrao", "trecho", "licao", "recusa", "nota", "referencia")
NIVEIS = ("automatico", "avisa", "pede-ok", "proibido")
ESTADOS = ("aberta", "fazendo", "esperando-ok", "feita", "cancelada")


def caminho_banco() -> Path:
    return Path(os.environ.get("NUCLEO_DB") or Path.home() / ".local" / "share" / "nucleo" / "nucleo.db")


def abrir(caminho: Path | None = None, criar: bool = True) -> sqlite3.Connection | None:
    p = caminho or caminho_banco()
    if not p.exists() and not criar:
        return None
    p.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(p)
    con.row_factory = sqlite3.Row
    con.executescript(ESQUEMA.read_text(encoding="utf-8"))
    return con


def _consulta_fts(texto: str) -> str:
    """Termos do pedido viram uma busca OU com prefixo, tolerante a acento e pontuação."""
    t = unicodedata.normalize("NFKD", texto.lower())
    termos = [w for w in re.findall(r"[a-z0-9]+", "".join(c for c in t if not unicodedata.combining(c))) if len(w) > 2]
    return " OR ".join(f'"{w}"*' for w in termos[:12])


def lembrar(con, texto: str, tipo: str = "nota", titulo: str = "", origem: str = "", tags: str = "",
            chave: str | None = None) -> int:
    if tipo not in TIPOS:
        raise ValueError(f"tipo inválido: {tipo} (use {', '.join(TIPOS)})")
    titulo = titulo or texto.strip().splitlines()[0][:90]
    cur = con.execute(
        "INSERT INTO conhecimento (tipo, titulo, texto, origem, tags, chave) VALUES (?,?,?,?,?,?) "
        "ON CONFLICT(chave) DO UPDATE SET titulo=excluded.titulo, texto=excluded.texto, origem=excluded.origem, tags=excluded.tags",
        (tipo, titulo, texto, origem, tags, chave))
    con.commit()
    if cur.lastrowid:
        return cur.lastrowid
    return con.execute("SELECT id FROM conhecimento WHERE chave=?", (chave,)).fetchone()["id"]


def buscar(con, texto: str, tipo: str | None = None, limite: int = 8) -> list[sqlite3.Row]:
    q = _consulta_fts(texto)
    if not q:
        return []
    sql = ("SELECT c.id, c.tipo, c.titulo, c.texto, c.origem, c.quando, bm25(conhecimento_fts, 5.0, 1.0, 2.0) AS nota "
           "FROM conhecimento_fts JOIN conhecimento c ON c.id = conhecimento_fts.rowid WHERE conhecimento_fts MATCH ?")
    args: list = [q]
    if tipo:
        sql += " AND c.tipo = ?"
        args.append(tipo)
    sql += " ORDER BY nota LIMIT ?"
    args.append(limite)
    return con.execute(sql, args).fetchall()


def contexto(con, pedido: str, limite: int = 5, max_chars: int = 280, excluir: tuple[str, ...] = ()) -> str:
    """Bloco curto (barato em token) com o que o núcleo já sabe sobre o pedido. `excluir` tira tipos (ex.: referencia,
    o texto de terceiros guardado só para consulta local)."""
    linhas = []
    for r in [x for x in buscar(con, pedido, limite=limite + 10) if x["tipo"] not in excluir][:limite]:
        corpo = [ln for ln in r["texto"].splitlines() if ln.strip() and not ln.lstrip().startswith(("#", "- **"))]
        resumo = " ".join(" ".join(corpo).split())[:max_chars]
        linhas.append(f"- [{r['tipo']}] {r['titulo']}: {resumo}")
    return "\n".join(linhas)


def evento(con, tipo: str, dados: dict | str = "{}", fonte: str = "manual") -> int:
    if isinstance(dados, str):
        try:
            dados = json.loads(dados) if dados.strip().startswith("{") else {"texto": dados}
        except json.JSONDecodeError:
            dados = {"texto": dados}
    cur = con.execute("INSERT INTO eventos (tipo, fonte, dados) VALUES (?,?,?)", (tipo, fonte, json.dumps(dados, ensure_ascii=False)))
    con.commit()
    return cur.lastrowid


def tarefa_nova(con, titulo: str, responsavel: str = "alan", evento_id: int | None = None) -> int:
    cur = con.execute("INSERT INTO tarefas (titulo, responsavel, evento_id) VALUES (?,?,?)", (titulo, responsavel, evento_id))
    con.commit()
    return cur.lastrowid


def tarefa_estado(con, tid: int, estado: str) -> None:
    if estado not in ESTADOS:
        raise ValueError(f"estado inválido: {estado}")
    if con.execute("UPDATE tarefas SET estado=? WHERE id=?", (estado, tid)).rowcount == 0:
        raise ValueError(f"tarefa {tid} não existe")
    con.commit()


def auditar(con, agente: str, acao: str, nivel: str, motivo: str = "", resultado: str = "", aprovado_por: str | None = None) -> int:
    if nivel not in NIVEIS:
        raise ValueError(f"nível inválido: {nivel} (use {', '.join(NIVEIS)})")
    cur = con.execute("INSERT INTO auditoria (agente, acao, nivel, motivo, resultado, aprovado_por) VALUES (?,?,?,?,?,?)",
                      (agente, acao, nivel, motivo, resultado, aprovado_por))
    con.commit()
    return cur.lastrowid


def importar(con, raiz: Path = RAIZ) -> dict[str, int]:
    """Traz para a base o que o setup já decidiu: ADRs e a lista de recusas. Rodar de novo só atualiza."""
    n = {"adr": 0, "recusa": 0}
    for arq in sorted((raiz / "docs" / "adr").glob("[0-9][0-9][0-9][0-9]-*.md")):
        texto = arq.read_text(encoding="utf-8")
        titulo = texto.splitlines()[0].lstrip("# ").strip()
        lembrar(con, texto, tipo="adr", titulo=titulo, origem=str(arq.relative_to(raiz)), chave=f"adr:{arq.stem[:4]}")
        n["adr"] += 1
    mapa = raiz / "data" / "mapa.json"
    if mapa.exists():
        for f in json.loads(mapa.read_text(encoding="utf-8")).get("fora", []):
            lembrar(con, f["motivo"], tipo="recusa", titulo=f["item"], origem="data/mapa.json", chave=f"recusa:{f['item']}")
            n["recusa"] += 1
    return n


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("iniciar")
    s.add_parser("importar")
    a = s.add_parser("lembrar"); a.add_argument("texto"); a.add_argument("--tipo", default="nota", choices=TIPOS)
    a.add_argument("--titulo", default=""); a.add_argument("--origem", default=""); a.add_argument("--tags", default="")
    b = s.add_parser("buscar"); b.add_argument("texto"); b.add_argument("--tipo", choices=TIPOS); b.add_argument("--limite", type=int, default=8)
    c = s.add_parser("contexto"); c.add_argument("pedido")
    e = s.add_parser("evento"); e.add_argument("tipo"); e.add_argument("dados", nargs="?", default="{}"); e.add_argument("--fonte", default="manual")
    t = s.add_parser("tarefa"); t.add_argument("acao", choices=("nova", "listar", "fazendo", "esperando-ok", "feita", "cancelada"))
    t.add_argument("valor", nargs="?", default="")
    u = s.add_parser("auditar"); u.add_argument("agente"); u.add_argument("acao"); u.add_argument("--nivel", required=True, choices=NIVEIS)
    u.add_argument("--motivo", default=""); u.add_argument("--resultado", default="")
    args = ap.parse_args(argv)
    con = abrir()
    try:
        if args.cmd in ("iniciar", "importar"):
            n = importar(con)
            print(f"Núcleo em {caminho_banco()}: {n['adr']} ADRs e {n['recusa']} recusas na base.")
        elif args.cmd == "lembrar":
            print(f"Guardado (#{lembrar(con, args.texto, args.tipo, args.titulo, args.origem, args.tags)}).")
        elif args.cmd == "buscar":
            rs = buscar(con, args.texto, args.tipo, args.limite)
            if not rs:
                print("Nada na base sobre isso.")
            for r in rs:
                print(f"#{r['id']} [{r['tipo']}] {r['titulo']}  ({r['quando'][:10]}{', ' + r['origem'] if r['origem'] else ''})")
                print("   " + " ".join(r["texto"].split())[:200])
        elif args.cmd == "contexto":
            print(contexto(con, args.pedido) or "(nada na base)")
        elif args.cmd == "evento":
            print(f"Evento #{evento(con, args.tipo, args.dados, args.fonte)}.")
        elif args.cmd == "tarefa":
            if args.acao == "nova":
                print(f"Tarefa #{tarefa_nova(con, args.valor)}.")
            elif args.acao == "listar":
                for r in con.execute("SELECT id, estado, responsavel, titulo FROM tarefas WHERE estado NOT IN ('feita','cancelada') ORDER BY id"):
                    print(f"#{r['id']} {r['estado']:<13} {r['responsavel']:<8} {r['titulo']}")
            else:
                tarefa_estado(con, int(args.valor), args.acao)
                print(f"Tarefa #{args.valor}: {args.acao}.")
        elif args.cmd == "auditar":
            print(f"Auditoria #{auditar(con, args.agente, args.acao, args.nivel, args.motivo, args.resultado)}.")
    except ValueError as erro:
        print(erro, file=sys.stderr)
        return 2
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
