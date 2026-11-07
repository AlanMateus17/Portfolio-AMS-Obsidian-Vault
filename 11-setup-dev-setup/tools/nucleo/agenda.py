#!/usr/bin/env python3
"""O setup diz o que é seu: próximos passos manuais, decisões pendentes e progresso do roteiro.

Lê data/implantacao.json (o roteiro) e guarda o que você já fez na tabela passos_feitos do núcleo.
Passo de "script" ou "claude" não aparece como tarefa sua: só os de quem = "voce" e os marcados como decisão.

    python3 tools/nucleo/agenda.py agora                      # os próximos passos que dependem de você
    python3 tools/nucleo/agenda.py agora --empresa software   # só os da AMtech Software
    python3 tools/nucleo/agenda.py decisoes --empresa software
    python3 tools/nucleo/agenda.py feito f0 f3 kp-chave       # marca passos (ou fases inteiras) como feitos
    python3 tools/nucleo/agenda.py desfazer kp-chave
    python3 tools/nucleo/agenda.py progresso
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nucleo as nuc  # noqa: E402

RAIZ = Path(__file__).resolve().parents[2]


def roteiro(raiz: Path = RAIZ) -> list[dict]:
    return json.loads((raiz / "data" / "implantacao.json").read_text(encoding="utf-8"))["fases"]


def feitos(con) -> set[str]:
    return {r["passo"] for r in con.execute("SELECT passo FROM passos_feitos")}


def _todos(fases):
    for f in fases:
        for p in f["passos"]:
            yield f, p


def expandir(fases, ids: list[str]) -> list[str]:
    """Aceita id de passo ou de fase (a fase vira todos os passos dela). Id desconhecido é erro."""
    fase = {f["id"]: [p["id"] for p in f["passos"]] for f in fases}
    passo = {p["id"] for _, p in _todos(fases)}
    saida = []
    for i in ids:
        if i in fase:
            saida += fase[i]
        elif i in passo:
            saida.append(i)
        else:
            raise ValueError(f"não existe passo nem fase com id {i}")
    return saida


def marcar(con, ids: list[str], fases=None) -> int:
    fases = fases or roteiro()
    passos = expandir(fases, ids)
    con.executemany("INSERT OR IGNORE INTO passos_feitos (passo) VALUES (?)", [(p,) for p in passos])
    con.commit()
    nuc.evento(con, "roteiro.feito", {"passos": passos}, fonte="agenda")
    return len(passos)


def desmarcar(con, ids: list[str], fases=None) -> int:
    passos = expandir(fases or roteiro(), ids)
    n = con.executemany("DELETE FROM passos_feitos WHERE passo = ?", [(p,) for p in passos]).rowcount
    con.commit()
    return n


def _da_empresa(p, empresa):
    return not empresa or empresa in p.get("empresas", [])


def pendentes(fases, feitos_: set[str], empresa: str | None = None, so_decisoes: bool = False) -> list[tuple[dict, dict]]:
    """Passos ainda não feitos que dependem de você, na ordem do roteiro. Fases com gatilho ficam de fora até você
    marcar algum passo delas (sinal de que o gatilho chegou)."""
    saida = []
    for f in fases:
        if f.get("gatilho") and not any(p["id"] in feitos_ for p in f["passos"]):
            continue
        for p in f["passos"]:
            if p["id"] in feitos_ or not _da_empresa(p, empresa):
                continue
            if so_decisoes and not p.get("decisao"):
                continue
            if not so_decisoes and p["quem"] != "voce" and not p.get("decisao"):
                continue
            saida.append((f, p))
    return saida


def progresso(fases, feitos_: set[str], empresa: str | None = None) -> list[tuple[str, int, int]]:
    linhas = []
    for f in fases:
        ps = [p for p in f["passos"] if _da_empresa(p, empresa)]
        if ps:
            linhas.append((f["titulo"], sum(1 for p in ps if p["id"] in feitos_), len(ps)))
    return linhas


def _linha(f, p) -> str:
    marca = "DECIDIR" if p.get("decisao") else "FAZER  "
    custo = " [custa dinheiro]" if set(p.get("precisa", [])) & {"compra", "pagamento"} else ""
    s = f"{marca} {p['id']:<22} {p['titulo']}{custo}\n        fase: {f['titulo']} · {p['tempo_min']} min · pronto quando: {p['pronto']}"
    if p.get("comando"):
        s += f"\n        Ubuntu do WSL: {p['comando']}"
    if p.get("fora"):
        s += f"\n        Fora do terminal: {p['fora']}"
    return s


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    for nome in ("agora", "decisoes"):
        a = s.add_parser(nome)
        a.add_argument("--empresa")
        a.add_argument("-n", type=int, default=5 if nome == "agora" else 0, help="quantos mostrar (0 = todos)")
    for nome in ("feito", "desfazer"):
        s.add_parser(nome).add_argument("ids", nargs="+")
    s.add_parser("progresso").add_argument("--empresa")
    args = ap.parse_args(argv)
    fases = roteiro()
    con = nuc.abrir()
    try:
        if args.cmd in ("agora", "decisoes"):
            lista = pendentes(fases, feitos(con), args.empresa, so_decisoes=args.cmd == "decisoes")
            total = len(lista)
            if args.n:
                lista = lista[: args.n]
            if not lista:
                print("Nada pendente com você aqui. O resto é script, Claude ou fase que ainda não chegou.")
            for f, p in lista:
                print(_linha(f, p) + "\n")
            if total > len(lista):
                print(f"(+{total - len(lista)} depois destes; quando terminar um, rode: just feito ID)")
        elif args.cmd == "feito":
            print(f"{marcar(con, args.ids, fases)} passo(s) marcados como feitos.")
        elif args.cmd == "desfazer":
            print(f"{desmarcar(con, args.ids, fases)} passo(s) voltaram para pendentes.")
        elif args.cmd == "progresso":
            for titulo, feito, total in progresso(fases, feitos(con), args.empresa):
                barra = "█" * round(10 * feito / total) + "·" * (10 - round(10 * feito / total))
                print(f"{barra} {feito:>3}/{total:<3} {titulo}")
    except ValueError as erro:
        print(erro, file=sys.stderr)
        return 2
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
