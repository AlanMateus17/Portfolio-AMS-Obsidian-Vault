#!/usr/bin/env python3
"""Motor de decisão 0.1 (ADR 0014): a escada de 5 degraus, o catálogo e o registro. Não chama IA nenhuma.

    python3 tools/motor/motor.py decidir "calcular o rateio da conta de luz deste mês"
    python3 tools/motor/motor.py decidir "escreva 15 questões teóricas de SO" --json
    python3 tools/motor/motor.py custo claude sonnet --entrada 12000 --saida 1800 --usd 0.06 --decisao 7
    python3 tools/motor/motor.py resultado 7 ok          # ou: resultado 7 refazer
    python3 tools/motor/motor.py relatorio               # decisões por degrau, gasto e candidatas à regra de três

Ordem da escada (para no primeiro "sim"): 5 · você (aprovar, pagar, publicar, decidir) é checado antes porque
nenhuma automação pode passar por cima de um portão humano; depois 1 · pronto, 2 · código, 3 · automação,
4 · linguagem (IA). Dado sensível (CPF, e-mail, senha, aluno...) nunca vai para IA online.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
REGRAS = RAIZ / "data" / "motor" / "regras.json"
RECURSOS = RAIZ / "data" / "recursos.json"
ECO = RAIZ / "data" / "ecossistema.json"
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
sys.path.insert(0, str(RAIZ / "tools" / "triagem"))
import nucleo as nuc  # noqa: E402
from triagem import palavras  # noqa: E402

PROMOVER_COM = 3  # regra de três


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.lower())
    return " ".join("".join(c for c in s if not unicodedata.combining(c)).split())


def carregar(caminho: Path = REGRAS) -> dict:
    return json.loads(caminho.read_text(encoding="utf-8"))


def tem(texto_norm: str, lista: list[str]) -> list[str]:
    """Termos da lista presentes no texto (palavra inteira ou expressão)."""
    achou, vistos = [], set()
    for t in lista:
        t_n = norm(t)
        if t_n not in vistos and re.search(rf"(?<![a-z0-9]){re.escape(t_n)}(?![a-z0-9])", texto_norm):
            achou.append(t)
            vistos.add(t_n)
    return achou


def sensivel(pedido: str, regras: dict) -> list[str]:
    """Motivos pelos quais o pedido carrega dado sensível (vazio = pode ir para IA online)."""
    s = regras["sensivel"]
    motivos = [f"palavra '{p}'" for p in tem(norm(pedido), s["palavras"])]
    motivos += [f"padrão de {nome}" for nome, rx in s["padroes"].items() if re.search(rx, pedido)]
    return motivos


def catalogo(recursos: dict, eco: dict, pedido: str) -> list[str]:
    """Degrau 1: rotas de data/recursos.json e blocos do ecossistema que casam com 2+ palavras do pedido."""
    ps = set(palavras(pedido))
    achados = []
    for r in recursos.get("rotas", []):
        if len(ps & set(palavras(r["tarefa"]))) >= 2:
            achados.append(f"Rota '{r['tarefa']}': {r['primaria']} (reserva: {r['reserva']}; portão: {r['portao']})")
    for b in eco.get("blocos", []):
        if len(ps & set(palavras(b["rotulo"]))) >= 2:
            achados.append(f"Bloco '{b['rotulo']}' ({b['id']}): {b['descricao']}")
    return achados[:5]


def tipo_do_pedido(t: str, regras: dict) -> str:
    notas = {tipo: len(tem(t, ps)) for tipo, ps in regras["tipos"].items()}
    melhor = max(notas, key=lambda k: (notas[k], k))
    return melhor if notas[melhor] else "padrao"


def modelo(t: str, regras: dict, sensivel_: bool) -> str:
    m = regras["modelos"]
    if sensivel_ or tem(t, m["local"]["quando"]):
        return m["local"]["destino"]
    for chave in ("forte", "codigo"):
        if tem(t, m[chave]["quando"]):
            return m[chave]["destino"]
    return m["padrao"]["destino"]


def decidir(pedido: str, regras: dict, recursos: dict | None = None, eco: dict | None = None) -> dict:
    t = norm(pedido)
    p = regras["palavras"]
    sens = sensivel(pedido, regras)
    pronto = catalogo(recursos or {}, eco or {}, pedido)
    if (achou := tem(t, p["voce"])):
        degrau, motivo = 5, f"portão humano: {', '.join(achou)}"
    elif pronto:
        degrau, motivo = 1, "já existe no setup"
    elif (achou := tem(t, p["codigo"])):
        degrau, motivo = 2, f"regra escrevível: {', '.join(achou)}"
        if (ag := tem(t, p["automacao"])):
            motivo += f"; disparo por {', '.join(ag)} (script + automação)"
    elif (achou := tem(t, p["automacao"])):
        degrau, motivo = 3, f"evento ou horário: {', '.join(achou)}"
    elif (achou := tem(t, p["linguagem"])):
        degrau, motivo = 4, f"linguagem: {', '.join(achou)}"
    else:
        degrau, motivo = 4, "nenhuma regra casou; a IA interpreta e você confirma o formulário"
    tipo = tipo_do_pedido(t, regras)
    ent = regras["entregaveis"][tipo]
    destino = regras["degraus"][str(degrau)]["quem"]
    if degrau == 4:
        destino = modelo(t, regras, bool(sens))
    return {
        "pedido": pedido, "degrau": degrau, "nome": regras["degraus"][str(degrau)]["nome"], "destino": destino,
        "motivo": motivo, "sensivel": sens, "pronto_no_setup": pronto, "tipo": tipo, "assinatura": assinatura(pedido),
        "formulario": {
            "TAREFA": pedido, "ENTREGÁVEL": ent["entregavel"], "PRONTO QUANDO": ent["pronto"],
            "FORA DO ESCOPO": "o que não couber nas 3 frentes \"agora\"",
            "RESTRIÇÕES": regras["restricoes"] + ([regras["sensivel"]["regra"]] if sens else []),
            "CONFIRMAR COM VOCÊ": ["PARA QUE", "ESCOPO (com número)", "PRONTO QUANDO"],
        },
    }


def assinatura(pedido: str) -> str:
    """Forma curta e estável do pedido (5 palavras mais longas, em ordem): base da regra de três."""
    ps = sorted(set(palavras(pedido)), key=lambda w: (-len(w), w))[:5]
    return " ".join(sorted(ps))


def texto(d: dict) -> str:
    out = [f"Pedido: {d['pedido']}", "", f"[DEGRAU {d['degrau']}] {d['nome']} → {d['destino']}", f"Por quê: {d['motivo']}"]
    if d["sensivel"]:
        out.append(f"DADO SENSÍVEL ({'; '.join(d['sensivel'])}): só IA local ou código.")
    if d["pronto_no_setup"]:
        out += ["", "Já no setup:"] + [f"  - {x}" for x in d["pronto_no_setup"]]
    out += ["", "Formulário (confirme os três últimos campos):"]
    for k, v in d["formulario"].items():
        out.append(f"  {k}: " + ("; ".join(v) if isinstance(v, list) else v))
    if d.get("id"):
        out += ["", f"Registrado como decisão #{d['id']}. Depois: motor.py resultado {d['id']} ok|refazer"]
    return "\n".join(out)


def _nucleo():
    if os.environ.get("NUCLEO_DESLIGADO"):
        return None
    try:
        return nuc.abrir(criar=False)
    except Exception:  # noqa: BLE001 - o registro é opcional
        return None


def _eventos(con, tipo: str) -> list[dict]:
    return [dict(json.loads(r["dados"]), _id=r["id"]) for r in con.execute(
        "SELECT id, dados FROM eventos WHERE tipo=? ORDER BY id", (tipo,))]


def relatorio(con) -> str:
    decisoes = _eventos(con, "motor.decisao")
    custos = _eventos(con, "motor.custo")
    resultados = {r["decisao"]: r["ok"] for r in _eventos(con, "motor.resultado")}
    por_degrau = Counter(d["degrau"] for d in decisoes)
    out = [f"Decisões: {len(decisoes)}"] + [f"  degrau {g}: {por_degrau.get(g, 0)}" for g in range(1, 6)]
    usd = sum(c.get("usd", 0) for c in custos)
    tok = sum(c.get("entrada", 0) + c.get("saida", 0) for c in custos)
    out += ["", f"Gasto registrado: US$ {usd:.2f} em {tok} tokens ({len(custos)} chamadas)"]
    por_ferr = defaultdict(float)
    for c in custos:
        por_ferr[f"{c['ferramenta']}/{c['modelo']}"] += c.get("usd", 0)
    out += [f"  {k}: US$ {v:.2f}" for k, v in sorted(por_ferr.items(), key=lambda x: -x[1])]
    aprovadas = Counter(d["assinatura"] for d in decisoes if resultados.get(d["_id"]) is True and d["degrau"] == 4)
    cand = [(a, n) for a, n in aprovadas.items() if n >= PROMOVER_COM]
    out += ["", f"Candidatas à regra de três (pedidos de IA aprovados {PROMOVER_COM}+ vezes):"]
    out += [f"  - {a} ({n}x): vire cache, template ou script, com teste e PR" for a, n in cand] or ["  nenhuma ainda"]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    d = s.add_parser("decidir"); d.add_argument("pedido"); d.add_argument("--json", action="store_true")
    c = s.add_parser("custo"); c.add_argument("ferramenta"); c.add_argument("modelo")
    c.add_argument("--entrada", type=int, default=0); c.add_argument("--saida", type=int, default=0)
    c.add_argument("--usd", type=float, default=0.0); c.add_argument("--decisao", type=int)
    r = s.add_parser("resultado"); r.add_argument("decisao", type=int); r.add_argument("estado", choices=("ok", "refazer"))
    s.add_parser("relatorio")
    args = ap.parse_args(argv)
    con = _nucleo()
    try:
        if args.cmd == "decidir":
            regras = carregar()
            rec = json.loads(RECURSOS.read_text(encoding="utf-8")) if RECURSOS.exists() else {}
            eco = json.loads(ECO.read_text(encoding="utf-8")) if ECO.exists() else {}
            dec = decidir(args.pedido, regras, rec, eco)
            if con:
                reg = {k: dec[k] for k in ("pedido", "degrau", "destino", "motivo", "tipo", "assinatura")}
                reg["sensivel"] = bool(dec["sensivel"])
                dec["id"] = nuc.evento(con, "motor.decisao", reg, fonte="motor")
            print(json.dumps(dec, ensure_ascii=False, indent=1) if args.json else texto(dec))
            return 0
        if con is None:
            print("Núcleo não iniciado: rode `python3 tools/nucleo/nucleo.py iniciar` primeiro.", file=sys.stderr)
            return 2
        if args.cmd == "custo":
            dados = {"ferramenta": args.ferramenta, "modelo": args.modelo, "entrada": args.entrada,
                     "saida": args.saida, "usd": args.usd, "decisao": args.decisao}
            print(f"Custo #{nuc.evento(con, 'motor.custo', dados, fonte='motor')} registrado.")
        elif args.cmd == "resultado":
            nuc.evento(con, "motor.resultado", {"decisao": args.decisao, "ok": args.estado == "ok"}, fonte="motor")
            print(f"Decisão #{args.decisao}: {args.estado}.")
        elif args.cmd == "relatorio":
            print(relatorio(con))
    finally:
        if con:
            con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
