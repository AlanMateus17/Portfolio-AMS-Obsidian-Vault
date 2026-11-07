#!/usr/bin/env python3
"""Lucro e prejuízo de cada ferramenta paga e de cada renda, mês a mês.

Dados seus, fora do repositório: ~/financas/roi.toml (modelo em tools/roi/roi.example.toml).
    python tools/roi/roi.py                 # último mês do arquivo
    python tools/roi/roi.py --mes 2026-11
    python tools/roi/roi.py --telegram      # manda o resumo para o seu celular

Como a conta é feita:
- Renda: lucro = receita - custos diretos; lucro por hora = lucro / horas suas (ActivityWatch).
- Ferramenta paga: recebe parte do lucro das rendas que ela atende, proporcional ao custo entre as ferramentas
  daquela renda. Resultado = parte atribuída - custo do mês. É uma ESTIMATIVA honesta, não contabilidade.
- Prejuízo: ferramenta cujo resultado é negativo; alerta forte se for negativo há 2 meses ou mais.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
import tomllib
from pathlib import Path

ARQ = Path.home() / "financas" / "roi.toml"
RAIZ = Path(__file__).resolve().parents[2]


def calcular(cfg: dict, mes: str) -> dict:
    hm = cfg.get("geral", {}).get("hora_minima", 45)
    meses = {m["mes"]: m for m in cfg.get("mes", [])}
    if mes not in meses:
        raise SystemExit(f"Mês {mes} não está no arquivo.")
    rendas = {}
    for o in meses[mes].get("oferta", []):
        lucro = float(o.get("receita", 0)) - float(o.get("custos_diretos", 0))
        h = float(o.get("horas", 0))
        rendas[o["id"]] = {"id": o["id"], "receita": float(o.get("receita", 0)), "lucro": lucro, "horas": h,
                           "lucro_hora": (lucro / h) if h else None,
                           "abaixo": bool(h) and lucro / h < hm}
    ferr = cfg.get("ferramenta", [])
    atend = {f["nome"]: (list(rendas) if f.get("ofertas") == ["*"] else [x for x in f.get("ofertas", []) if x in rendas]) for f in ferr}
    atribuido = {f["nome"]: 0.0 for f in ferr}
    for rid, r in rendas.items():
        quem = [f for f in ferr if rid in atend[f["nome"]]]
        total = sum(float(f["custo"]) for f in quem)
        for f in quem:
            if total:
                atribuido[f["nome"]] += max(r["lucro"], 0) * float(f["custo"]) / total
    ferramentas = []
    for f in ferr:
        res = atribuido[f["nome"]] - float(f["custo"])
        ferramentas.append({"nome": f["nome"], "custo": float(f["custo"]), "atribuido": round(atribuido[f["nome"]], 2),
                            "resultado": round(res, 2), "rendas": atend[f["nome"]], "seguido": seguido_negativo(cfg, f, mes)})
    custo_ferr = sum(f["custo"] for f in ferramentas)
    liquido = sum(r["lucro"] for r in rendas.values()) - custo_ferr
    return {"mes": mes, "hora_minima": hm, "rendas": list(rendas.values()), "ferramentas": ferramentas, "liquido": round(liquido, 2)}


def seguido_negativo(cfg: dict, f: dict, mes: str) -> int:
    """Quantos meses seguidos (até este) a ferramenta ficou no prejuízo."""
    ordem = sorted(m["mes"] for m in cfg.get("mes", []) if m["mes"] <= mes)
    n = 0
    for m in reversed(ordem):
        sub = dict(cfg, ferramenta=[f])
        try:
            r = calcular_simples(sub, m)
        except SystemExit:
            break
        if r < 0:
            n += 1
        else:
            break
    return n


def calcular_simples(cfg: dict, mes: str) -> float:
    m = next(x for x in cfg["mes"] if x["mes"] == mes)
    f = cfg["ferramenta"][0]
    ids = [o["id"] for o in m.get("oferta", [])]
    servidas = ids if f.get("ofertas") == ["*"] else [i for i in f.get("ofertas", []) if i in ids]
    return (1.0 if any(float(o.get("receita", 0)) > float(o.get("custos_diretos", 0)) for o in m.get("oferta", []) if o["id"] in servidas) else -1.0)


def relatorio(r: dict) -> str:
    o = [f"Lucro e prejuízo · {r['mes']}", f"Resultado líquido do mês: R$ {r['liquido']:,.2f}", "", "Rendas:"]
    for x in sorted(r["rendas"], key=lambda x: -x["lucro"]):
        lh = f"R$ {x['lucro_hora']:.0f}/h" if x["lucro_hora"] is not None else "sem horas medidas"
        o.append(f"  {x['id']:<22} lucro R$ {x['lucro']:>9,.2f} · {lh}{'  ⚠ abaixo da hora mínima' if x['abaixo'] else ''}")
    o += ["", "Ferramentas pagas:"]
    for f in sorted(r["ferramentas"], key=lambda f: f["resultado"]):
        alerta = ""
        if f["resultado"] < 0:
            alerta = f"  ⚠ PREJUÍZO" + (f" há {f['seguido']} meses: cortar, trocar ou adiar" if f["seguido"] >= 2 else "")
        o.append(f"  {f['nome']:<26} custo R$ {f['custo']:>7,.2f} · gerou R$ {f['atribuido']:>8,.2f} · resultado R$ {f['resultado']:>8,.2f}{alerta}")
    o.append("\nEstimativa: a parte de cada ferramenta é proporcional ao custo entre as que atendem a mesma renda.")
    return "\n".join(o)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--arquivo", default=str(ARQ))
    ap.add_argument("--mes")
    ap.add_argument("--telegram", action="store_true")
    a = ap.parse_args()
    p = Path(a.arquivo).expanduser()
    if not p.exists():
        print(f"Crie {p} a partir de tools/roi/roi.example.toml", file=sys.stderr)
        return 1
    cfg = tomllib.loads(p.read_text(encoding="utf-8"))
    mes = a.mes or max(m["mes"] for m in cfg["mes"])
    txt = relatorio(calcular(cfg, mes))
    print(txt)
    if a.telegram:
        subprocess.run([sys.executable, str(RAIZ / "tools" / "remoto" / "bot.py"), "--avisar", txt], check=False)
    return 0


if __name__ == "__main__":
    sys.exit(main())
