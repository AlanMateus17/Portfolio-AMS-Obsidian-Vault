#!/usr/bin/env python3
"""Investimentos: aplica TODAS as suas metodologias, ao mesmo tempo, nas quatro classes do ARCA.

Não é recomendação de investimento: o script só calcula com as regras e os dados que você fornece.
Seus dados ficam em ~/financas (fora do repositório).

    python tools/investimentos/investimentos.py docs [--check]                  # docs/investimentos.md (CI)
    python tools/investimentos/investimentos.py iniciar                         # copia os modelos para ~/financas
    python tools/investimentos/investimentos.py avaliar acoes indicadores_acoes.csv
    python tools/investimentos/investimentos.py avaliar fiis indicadores_fiis.csv
    python tools/investimentos/investimentos.py avaliar caixa indicadores_caixa.csv
    python tools/investimentos/investimentos.py avaliar internacional indicadores_internacional.csv
    python tools/investimentos/investimentos.py aporte carteira.csv 800         # ARCA → classe → metodologia
    python tools/investimentos/investimentos.py comparar carteiras.csv          # cada carteira contra o índice
"""
from __future__ import annotations

import argparse
import copy
import csv
import json
import math
import shutil
import sys
import tomllib
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "investimentos.json"
MD = RAIZ / "docs" / "investimentos.md"
MODELOS = Path(__file__).resolve().parent / "modelos"
PASTA = Path.home() / "financas"
AVISO = "<!-- Arquivo GERADO por tools/investimentos/investimentos.py a partir de data/investimentos.json. Não edite à mão. -->\n"
REGRAS = {">=", "<=", ">", "<", "em", "<=teto", "<=graham", "<=gordon", "premio_ntnb", "equiv_cdi", "juro_real", "checklist", "rank"}
NA = "não se aplica"


# ---------- dados ----------

def carregar() -> dict:
    d = json.loads(DADOS.read_text(encoding="utf-8"))
    por_id = {f"{c['id']}.{m['id']}": m for c in d["classes"] for m in c["metodologias"]}
    for c in d["classes"]:
        for m in c["metodologias"]:
            if m.get("herda"):
                m["criterios"] = copy.deepcopy(por_id[m["herda"]]["criterios"])
            for cr in m["criterios"]:
                if m.get("aplica_se") and "aplica_se" not in cr:
                    cr["aplica_se"] = m["aplica_se"]
    return d


def classe(d: dict, cid: str) -> dict:
    for c in d["classes"]:
        if c["id"] == cid:
            return c
    raise SystemExit(f"Classe desconhecida: {cid}. Use: {', '.join(c['id'] for c in d['classes'])}")


def carregar_config(caminho: Path | None = None) -> dict:
    c = caminho or PASTA / "investimentos.toml"
    if not c.exists():
        c = MODELOS / "investimentos.example.toml"
    return tomllib.loads(c.read_text(encoding="utf-8"))


def validar(d: dict) -> list[str]:
    e = []
    for c in d["classes"]:
        ids = [m["id"] for m in c["metodologias"]]
        if len(ids) != len(set(ids)):
            e.append(f"{c['id']}: metodologia repetida")
        if sum(c["alocacao_padrao"].values()) != 100:
            e.append(f"{c['id']}: alocacao_padrao precisa somar 100")
        if set(c["alocacao_padrao"]) != set(ids):
            e.append(f"{c['id']}: alocacao_padrao precisa ter exatamente as metodologias da classe")
        for m in c["metodologias"]:
            if not m["criterios"]:
                e.append(f"{c['id']}.{m['id']}: sem critérios")
            if not m["fonte"].strip():
                e.append(f"{c['id']}.{m['id']}: sem fonte")
            for cr in m["criterios"]:
                if cr["regra"] not in REGRAS:
                    e.append(f"{c['id']}.{m['id']}: regra inválida {cr['regra']}")
    return e


# ---------- cálculo ----------

def num(v) -> float | None:
    if v is None:
        return None
    s = str(v).strip().replace("%", "")
    if not s or s in {"-", "—"}:
        return None
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def ir_regressivo(dias: float | None) -> float:
    d = dias or 0
    return 22.5 if d <= 180 else 20.0 if d <= 360 else 17.5 if d <= 720 else 15.0


def equiv_cdi(l: dict) -> float | None:
    """Taxa em % do CDI comparável com título tributado: isento vale taxa ÷ (1 − IR do prazo)."""
    t = num(l.get("taxa"))
    if t is None:
        return None
    if (l.get("isento") or "").lower() in ("sim", "s", "true", "1"):
        return round(t / (1 - ir_regressivo(num(l.get("vencimento_dias"))) / 100), 1)
    return t


def teto(l: dict, taxa_pct: float) -> float | None:
    dm = num(l.get("dividendo_medio"))
    return round(dm / (taxa_pct / 100), 2) if dm is not None and taxa_pct > 0 else None


def valor_graham(l: dict) -> float | None:
    lpa, vpa = num(l.get("lpa")), num(l.get("vpa"))
    if lpa is None or vpa is None or lpa <= 0 or vpa <= 0:
        return None
    return round(math.sqrt(22.5 * lpa * vpa), 2)


def preco_gordon(l: dict, cfg: dict) -> float | None:
    dm, g = num(l.get("dividendo_medio")), num(l.get("crescimento_dividendos"))
    k = num(cfg.get("mercado", {}).get("retorno_exigido"))
    if dm is None or g is None or k is None or g >= k:
        return None
    return round(dm * (1 + g / 100) / ((k - g) / 100), 2)


def aplica(cr: dict, l: dict) -> bool:
    for campo, vals in cr.get("aplica_se", {}).items():
        if (l.get(campo) or "").strip().lower() not in vals:
            return False
    return True


def criterio_ok(cr: dict, l: dict, cfg: dict, ranks: dict) -> bool | None | str:
    """True passa, False reprova, None sem dado, NA quando não se aplica ao ativo."""
    if not aplica(cr, l):
        return NA
    r, mer = cr["regra"], cfg.get("mercado", {})
    preco = num(l.get("preco"))
    if r == "em":
        v = (l.get(cr["chave"]) or "").strip().lower()
        return None if not v else v in cr["valor"]
    if r == "checklist":
        v = (l.get(cr["chave"]) or "").strip().lower()
        return None if not v else v in ("sim", "s")
    if r == "rank":
        return NA if l["ticker"] not in ranks else ranks[l["ticker"]] <= cr["valor"]
    if r in ("<=teto", "<=graham", "<=gordon"):
        ref = teto(l, cr["valor"]) if r == "<=teto" else valor_graham(l) if r == "<=graham" else preco_gordon(l, cfg)
        if ref is None or preco is None:
            return None
        return preco <= (ref * (1 - cr["valor"] / 100) if r == "<=graham" else ref)
    if r == "premio_ntnb":
        dy, ntnb = num(l.get(cr["chave"])), num(mer.get("ntnb_juro_real"))
        return None if dy is None or not ntnb else dy - ntnb >= cr["valor"]
    if r == "equiv_cdi":
        e = equiv_cdi(l)
        return None if e is None else e >= cr["valor"]
    if r == "juro_real":
        t, minimo = num(l.get(cr["chave"])), num(mer.get("juro_real_min"))
        return None if t is None or minimo is None else t >= minimo
    v = num(l.get(cr["chave"]))
    if v is None:
        return None
    return {">=": v >= cr["valor"], "<=": v <= cr["valor"], ">": v > cr["valor"], "<": v < cr["valor"]}[r]


def ranking_formula(linhas: list[dict]) -> dict:
    """Fórmula Mágica: posição percentual no ranking somado de ROIC (alto) e EV/EBIT (baixo). Bancos e seguros fora."""
    ok = [l for l in linhas if num(l.get("roic")) is not None and (num(l.get("ev_ebit")) or 0) > 0
          and (l.get("setor") or "").lower() not in ("bancos", "seguros")]
    if not ok:
        return {}
    roic = sorted(ok, key=lambda l: -num(l["roic"]))
    ev = sorted(ok, key=lambda l: num(l["ev_ebit"]))
    soma = {l["ticker"]: roic.index(l) + ev.index(l) for l in ok}
    ordem = sorted(soma, key=soma.get)
    return {t: round((ordem.index(t) + 1) / len(ordem) * 100, 1) for t in ordem}


def resultado(m: dict, l: dict, cfg: dict, ranks: dict) -> str:
    oks = [criterio_ok(cr, l, cfg, ranks) for cr in m["criterios"]]
    validos = [o for o in oks if o != NA]
    if not validos:
        return NA
    if False in validos:
        return "não"
    if None in validos:
        return "sem dado"
    return "passa"


def avaliar(linhas: list[dict], d: dict, cid: str, cfg: dict) -> list[dict]:
    c = classe(d, cid)
    ranks = ranking_formula(linhas) if any(cr["regra"] == "rank" for m in c["metodologias"] for cr in m["criterios"]) else {}
    lim = d["consenso"]
    res = []
    for l in linhas:
        r = {"ticker": l["ticker"]}
        for m in c["metodologias"]:
            r[m["id"]] = resultado(m, l, cfg, ranks)
        contam = [v for k, v in r.items() if k != "ticker" and v != NA]
        passa = sum(v == "passa" for v in contam)
        pct = round(passa / len(contam) * 100) if contam else 0
        r["consenso"] = f"{passa}/{len(contam)} ({pct}%)"
        r["classificacao"] = "forte" if pct >= lim["forte"] else "médio" if pct >= lim["medio"] else "fraco"
        r["_pct"] = pct
        if cid in ("acoes", "internacional"):
            r["teto_bazin"], r["valor_graham"], r["preco_gordon"] = teto(l, 6), valor_graham(l), preco_gordon(l, cfg)
        if cid == "fiis":
            r["teto_8pct"] = teto(l, 8)
        if cid == "caixa":
            r["equiv_cdi"] = equiv_cdi(l)
        res.append(r)
    return sorted(res, key=lambda r: -r["_pct"])


def ler_csv(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        amostra = f.read(2048)
        f.seek(0)
        sep = ";" if amostra.count(";") > amostra.count(",") else ","
        return [{k.strip().lower(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(f, delimiter=sep)]


def _divide(valor: float, alvo: dict, atual: dict, total: float) -> dict:
    falta = {k: max(0.0, alvo[k] / 100 * total - atual.get(k, 0)) for k in alvo}
    s = sum(falta.values())
    if not s:
        return {k: round(valor * alvo[k] / 100, 2) for k in alvo if alvo[k]}
    return {k: round(valor * f / s, 2) for k, f in falta.items() if f > 0}


def juntar_pequenos(div: dict, minimo: float) -> dict:
    """Tira a menor fatia abaixo do mínimo por compra e reparte entre as outras, na proporção delas, até todas passarem do mínimo."""
    div = {k: float(v) for k, v in div.items()}
    while len(div) > 1 and min(div.values()) < minimo:
        v = div.pop(min(div, key=div.get))
        s = sum(div.values())
        div = {k: x + v * x / s for k, x in div.items()}
    return {k: round(v, 2) for k, v in div.items()}


def aporte(carteira: list[dict], valor: float, cfg: dict, d: dict) -> tuple[list[str], dict]:
    """ARCA em dois níveis: o aporte vai às classes mais abaixo do alvo e, dentro delas, às metodologias mais abaixo do alvo."""
    p = cfg.get("portao", {})
    if not (p.get("cartao_zerado") and p.get("reserva_completa")):
        return ["Portão fechado: zere o cartão e complete a reserva antes de aportar no ARCA (atualize [portao] em investimentos.toml)."], {}
    arca = cfg.get("arca") or {c["id"]: 100 / len(d["classes"]) for c in d["classes"]}
    total = sum(num(l["valor_atual"]) or 0 for l in carteira) + valor
    por_classe = {}
    for l in carteira:
        por_classe[l["classe"]] = por_classe.get(l["classe"], 0) + (num(l["valor_atual"]) or 0)
    minimo = num(cfg.get("aporte", {}).get("minimo_por_compra")) or 100
    div_classes = juntar_pequenos(_divide(valor, arca, por_classe, total), minimo)
    avisos, divisao = [], {}
    for cid, v_classe in div_classes.items():
        c = classe(d, cid)
        ccfg = cfg.get("classes", {}).get(cid, {})
        alvo = ccfg.get("alocacao") or c["alocacao_padrao"]
        lim = {**c["concentracao"], **ccfg.get("concentracao", {})}
        itens = [l for l in carteira if l["classe"] == cid]
        tot_c = por_classe.get(cid, 0) + v_classe
        por_met, por_ticker, por_setor = {}, {}, {}
        for l in itens:
            v = num(l["valor_atual"]) or 0
            por_met[l["metodo"]] = por_met.get(l["metodo"], 0) + v
            por_ticker[l["ticker"]] = por_ticker.get(l["ticker"], 0) + v
            por_setor[l.get("setor", "")] = por_setor.get(l.get("setor", ""), 0) + v
        divisao[cid] = juntar_pequenos(_divide(v_classe, alvo, por_met, tot_c), minimo)
        teto_a, teto_s = lim["max_ativo_pct"] / 100 * tot_c, lim["max_setor_pct"] / 100 * tot_c
        setor = {l["ticker"]: l.get("setor", "") for l in itens}
        for met in divisao[cid]:
            cands = sorted({l["ticker"] for l in itens if l["metodo"] == met}, key=lambda t: por_ticker[t])
            livres = [t for t in cands if por_ticker[t] < teto_a and por_setor[setor[t]] < teto_s]
            avisos.append(f"{cid}/{met}: " + (f"candidatas dentro dos limites: {', '.join(livres[:3])}" if livres
                                              else "nenhum ativo da carteira dentro dos limites; escolha um novo pela avaliação (maior consenso primeiro)."))
        if len(por_ticker) < lim["min_ativos"]:
            avisos.append(f"{cid}: {len(por_ticker)} ativos; o seu mínimo é {lim['min_ativos']}.")
        for t, v in por_ticker.items():
            if v > teto_a:
                avisos.append(f"{cid}: {t} passou de {lim['max_ativo_pct']}% da classe; não aporte nele.")
        if cid == "caixa":
            por_emissor = {}
            for l in itens:
                if (l.get("garantia") or "").lower() == "fgc":
                    por_emissor[l.get("emissor", "")] = por_emissor.get(l.get("emissor", ""), 0) + (num(l["valor_atual"]) or 0)
            for em, v in por_emissor.items():
                if v > 250000:
                    avisos.append(f"caixa: {em} passou de R$ 250 mil com garantia do FGC; o excedente fica sem garantia.")
            anos = {int((num(l.get("vencimento_dias")) or 0) // 365) for l in itens if l["metodo"] == "escada"}
            if 0 < len(anos) < 3:
                avisos.append("caixa: a escada tem menos de 3 degraus (anos de vencimento diferentes).")
    return avisos, divisao


def comparar(linhas: list[dict]) -> list[str]:
    res, ref = [], {}
    for l in linhas:
        inv, atual = num(l["investido"]), num(l["valor_atual"])
        if not inv:
            continue
        r = (atual - inv) / inv * 100
        cl = l.get("classe", "")
        if l["carteira"].lower() == "indice":
            ref[cl] = r
        res.append((cl, l["carteira"], r))
    o = []
    for cl, nome, r in sorted(res, key=lambda x: (x[0], -x[2])):
        base = ref.get(cl)
        dif = "" if base is None or nome.lower() == "indice" else f" ({r - base:+.1f} p.p. contra o índice)"
        o.append(f"{cl + ' / ' if cl else ''}{nome}: {r:+.1f}%{dif}")
    return o


# ---------- documentação ----------

def gerar(d: dict) -> str:
    o = [AVISO, "# Investimentos: todas as metodologias, ao mesmo tempo, nas quatro classes do ARCA\n", "[← Índice da documentação](README.md)\n",
         f"> {d['aviso']}\n", "## Regras\n"]
    o += [f"- {x}" for x in d["regras"]]
    o += ["", "## Impostos e garantias que entram no cálculo\n"] + [f"- {x}" for x in d["impostos"]]
    cs = d["consenso"]
    o += ["", "## Como o consenso classifica cada ativo\n",
          f"Cada ativo passa por todas as metodologias da sua classe. Consenso = metodologias que aprovaram ÷ metodologias que se aplicam. "
          f"**Forte** a partir de {cs['forte']}%, **médio** a partir de {cs['medio']}%, **fraco** abaixo disso.\n"]
    for c in d["classes"]:
        o += [f"## {c['nome']}\n", f"Colunas do CSV: `{c['colunas']}`\n", "| Metodologia | Origem | % alvo na classe | Ideia |", "|---|---|---:|---|"]
        o += [f"| [{m['nome']}](#{c['id']}-{m['id']}) | {m['origem']} | {c['alocacao_padrao'][m['id']]}% | {m['ideia']} |" for m in c["metodologias"]]
        lim = c["concentracao"]
        o += ["", f"Limites: até {lim['max_ativo_pct']}% da classe num ativo e {lim['max_setor_pct']}% num setor; pelo menos {lim['min_ativos']} ativos.", ""]
        for m in c["metodologias"]:
            o += [f'<a id="{c["id"]}-{m["id"]}"></a>', f"### {m['nome']}\n", m["ideia"], ""]
            if m.get("herda"):
                o += [f"Usa os critérios de `{m['herda']}`.", ""]
            o += ["Critérios:"] + [f"- {cr['texto']}" + (" (só para " + ", ".join(v for vs in cr["aplica_se"].values() for v in vs) + ")" if cr.get("aplica_se") else "")
                                   for cr in m["criterios"]] + [""]
            if m["perguntas"]:
                o += ["Perguntas que só você responde:"] + [f"- {p}" for p in m["perguntas"]] + [""]
            o += [f"**Quando vender:** {m['venda']}", "", f"Fonte: {m['fonte']}", ""]
    o += ["## Alocações para comparar com o ARCA (carteiras simuladas)\n", "| Estratégia | Divisão | Uso |", "|---|---|---|"]
    o += [f"| {x['nome']} | {x['divisao']} | {x['uso']} |" for x in d["comparacoes_gerais"]]
    o += ["", "## Como usar\n", "```bash", "python tools/investimentos/investimentos.py iniciar"]
    o += [f"python tools/investimentos/investimentos.py avaliar {c['id']} ~/financas/indicadores_{c['id']}.csv" for c in d["classes"]]
    o += ["python tools/investimentos/investimentos.py aporte ~/financas/carteira.csv 800", "python tools/investimentos/investimentos.py comparar ~/financas/carteiras.csv", "```", "",
          "Os modelos de CSV estão em tools/investimentos/modelos (tickers inventados). A política completa fica em ~/financas/politica-investimentos.md."]
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    g = sp.add_parser("docs")
    g.add_argument("--check", action="store_true")
    sp.add_parser("iniciar")
    a = sp.add_parser("avaliar")
    a.add_argument("classe")
    a.add_argument("csv", type=Path)
    a.add_argument("--config", type=Path)
    b = sp.add_parser("aporte")
    b.add_argument("csv", type=Path)
    b.add_argument("valor", type=float)
    b.add_argument("--config", type=Path)
    c = sp.add_parser("comparar")
    c.add_argument("csv", type=Path)
    x = ap.parse_args()
    d = carregar()
    e = validar(d)
    if e:
        print("\n".join("ERRO: " + i for i in e), file=sys.stderr)
        return 1
    if x.cmd == "docs":
        t = gerar(d)
        if x.check:
            if (MD.read_text(encoding="utf-8") if MD.exists() else "") != t:
                print("docs/investimentos.md está desatualizado. Rode: python tools/investimentos/investimentos.py docs", file=sys.stderr)
                return 1
            n = sum(len(c["metodologias"]) for c in d["classes"])
            print(f"Investimentos em dia: {len(d['classes'])} classes, {n} metodologias.")
            return 0
        MD.write_text(t, encoding="utf-8")
        print(f"Gerado {MD.relative_to(RAIZ)}")
    elif x.cmd == "iniciar":
        PASTA.mkdir(exist_ok=True)
        for m in sorted(MODELOS.iterdir()):
            destino = PASTA / m.name.replace(".example", "")
            if not destino.exists():
                shutil.copy(m, destino)
                print(f"criado: {destino}")
    elif x.cmd == "avaliar":
        res = avaliar(ler_csv(x.csv), d, x.classe, carregar_config(x.config))
        cols = [k for k in (res[0] if res else {}) if k not in ("ticker", "_pct")]
        print("ticker | " + " | ".join(cols))
        for r in res:
            print(r["ticker"] + " | " + " | ".join("—" if r[k] is None else str(r[k]) for k in cols))
        print("\n" + d["aviso"])
    elif x.cmd == "aporte":
        avisos, div = aporte(ler_csv(x.csv), x.valor, carregar_config(x.config), d)
        for cid, mets in div.items():
            print(f"{cid}: R$ {sum(mets.values()):.2f}")
            for k, v in mets.items():
                print(f"  {k}: R$ {v:.2f}")
        print("\n".join(avisos))
    elif x.cmd == "comparar":
        print("\n".join(comparar(ler_csv(x.csv))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
