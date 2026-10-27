#!/usr/bin/env python3
"""Gera o roteiro de implantação a partir de data/implantacao.json.

Saídas: docs/implantacao/roteiro.md e docs/implantacao/acompanhamento.html.

    python tools/implantacao/gerar.py          # valida e regenera
    python tools/implantacao/gerar.py --check  # falha se algo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "implantacao.json"
ECO = RAIZ / "data" / "ecossistema.json"
PORTFOLIO = RAIZ / "data" / "portfolio.json"
MD = RAIZ / "docs" / "implantacao" / "roteiro.md"
HTML = RAIZ / "docs" / "implantacao" / "acompanhamento.html"
TEMPLATE = RAIZ / "tools" / "implantacao" / "acompanhamento.template.html"
AVISO = "<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->\n"
QUEM = {"voce": "Você", "script": "Script", "claude": "Claude com você"}
PRECISA = {"compra": "comprar algo", "pagamento": "pagar um serviço", "conteudo": "conteúdo seu pronto (livro, capítulo)"}
ID_RE = re.compile(r"^[a-z0-9-]+$")


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def carregar_portfolio() -> dict:
    return json.loads(PORTFOLIO.read_text(encoding="utf-8"))


def carregar_eco() -> dict:
    return json.loads(ECO.read_text(encoding="utf-8"))


def rotulo(b: dict) -> str:
    return b["rotulo"].replace("|", " ").replace("  ", " ")


def quando_por_bloco(d: dict) -> dict[str, list[dict]]:
    """Para cada bloco, os passos em que ele entra, com a fase e quando."""
    out: dict[str, list[dict]] = {}
    for i, f in enumerate(d["fases"]):
        for j, p in enumerate(f["passos"], 1):
            for b in p.get("blocos", []):
                out.setdefault(b, []).append({"fase": i, "num": f"{i}.{j}", "id": p["id"], "fase_titulo": f["titulo"], "passo": p["titulo"],
                                              "quando": f.get("quando", ""), "gatilho": f.get("gatilho", "")})
    return out


def faz_hoje(f: dict, p: dict) -> bool:
    return not p.get("precisa") and not f.get("gatilho")


def validar(d: dict, eco: dict | None = None) -> list[str]:
    eco = eco if eco is not None else carregar_eco()
    erros, vistos = [], set()
    for f in d["fases"]:
        if not ID_RE.match(f["id"]):
            erros.append(f"fase com id inválido: {f['id']}")
        if not f["passos"]:
            erros.append(f"fase {f['id']} sem passos")
        for p in f["passos"]:
            if p["id"] in vistos:
                erros.append(f"passo repetido: {p['id']}")
            vistos.add(p["id"])
            if not ID_RE.match(p["id"]):
                erros.append(f"passo com id inválido: {p['id']}")
            if p["quem"] not in QUEM:
                erros.append(f"{p['id']}: quem inválido {p['quem']}")
            if not isinstance(p["tempo_min"], int) or p["tempo_min"] <= 0:
                erros.append(f"{p['id']}: tempo_min deve ser inteiro positivo")
            if not p["pronto"].strip():
                erros.append(f"{p['id']}: sem critério de pronto")
            for arq in re.findall(r"(scripts/[\w./-]+\.(?:ps1|sh)|tools/[\w./-]+\.py|infra/[\w./-]+)", p.get("comando", "").replace("\\", "/")):
                if not (RAIZ / arq).exists():
                    erros.append(f"{p['id']}: o comando cita {arq}, que não existe")
            for x in p.get("precisa", []):
                if x not in PRECISA:
                    erros.append(f"{p['id']}: precisa inválido {x} (use {', '.join(PRECISA)})")
            if not isinstance(p.get("blocos"), list):
                erros.append(f"{p['id']}: falta a lista 'blocos' (o que este passo implanta)")
    ids = {b["id"]: b for b in eco["blocos"]}
    qb = quando_por_bloco(d)
    for b in sorted(set(qb) - set(ids)):
        erros.append(f"bloco {b} citado no roteiro não existe em data/ecossistema.json")
    for b in eco["blocos"]:
        if b["id"] not in qb:
            erros.append(f"bloco {b['id']} ({rotulo(b)}) está no setup e fora do roteiro: ponha num passo, com fase e data")
    for f in d["fases"]:
        if not f.get("quando", "").strip():
            erros.append(f"fase {f['id']} ({f['titulo']}) sem 'quando'")
    ofertas = {o["id"] for o in carregar_portfolio()["ofertas"]}
    usadas = {o for f in d["fases"] for p in f["passos"] for o in p.get("ofertas", [])}
    for o in sorted(usadas - ofertas):
        erros.append(f"oferta {o} citada no roteiro não existe em data/portfolio.json")
    for o in sorted(ofertas - usadas):
        erros.append(f"oferta {o} do portfólio sem passo no roteiro: diga quando ela entra")
    if d.get("cobertura"):
        erros.append("'cobertura' não é mais usada: todo bloco entra num passo")
    return erros


def horas(minutos: int) -> str:
    h, m = divmod(minutos, 60)
    return f"{h} h {m:02d} min" if h else f"{m} min"


def gerar_md(d: dict, eco: dict | None = None) -> str:
    eco = eco if eco is not None else carregar_eco()
    B = {b["id"]: b for b in eco["blocos"]}
    OF = {o["id"]: o["nome"] for o in carregar_portfolio()["ofertas"]}
    qb = quando_por_bloco(d)
    todos = [(f, p) for f in d["fases"] for p in f["passos"]]
    total = sum(p["tempo_min"] for _, p in todos)
    hoje = [(f, p) for f, p in todos if faz_hoje(f, p)]
    t_hoje = sum(p["tempo_min"] for _, p in hoje)
    o = [AVISO, "# Roteiro de implantação\n", "[← Implantação](README.md)\n",
         f"{len(d['fases'])} fases, {len(todos)} passos, cerca de **{horas(total)}** de trabalho no total. "
         "Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o "
         "[`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).\n",
         "Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), "
         "**Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).\n",
         f"**Todo o planejamento está aqui:** os {len(B)} blocos do [mapa do setup](../mapa.html), de todas as {len(eco['camadas'])} camadas, "
         f"entram em algum passo, com a data ou o gatilho de quando, e cada uma das {len(OF)} ofertas do portfólio tem o passo em que entra à venda. "
         "Nada fica de fora; o CI falha se um bloco ou uma oferta nova não tiver passo "
         "([quando entra cada bloco](#quando-entra-cada-bloco)).\n",
         f"**Dá para fazer hoje:** {len(hoje)} dos {len(todos)} passos ({horas(t_hoje)}) só precisam do notebook e de contas grátis. "
         "Os outros dizem o que falta: comprar algo, pagar um serviço, ter um conteúdo seu pronto ou esperar o gatilho da fase.\n",
         "| Fase | Quando | Passos | Tempo |", "|---|---|---:|---:|"]
    for i, f in enumerate(d["fases"]):
        t = sum(p["tempo_min"] for p in f["passos"])
        q = f["quando"] + (f" · **gatilho:** {f['gatilho']}" if f.get("gatilho") else "")
        o.append(f"| [{i} · {f['titulo']}](#{f['id']}) | {q} | {len(f['passos'])} | {horas(t)} |")
    o.append("")
    for i, f in enumerate(d["fases"]):
        o.append(f'<a id="{f["id"]}"></a>\n')
        o.append(f"## {i} · {f['titulo']}\n")
        o.append(f"{f['objetivo']}\n")
        o.append(f"**Quando:** {f['quando']}\n")
        if f.get("gatilho"):
            o.append(f"**Começa quando:** {f['gatilho']}\n")
        for j, p in enumerate(f["passos"], 1):
            o.append(f"### {i}.{j} {p['titulo']}\n")
            o.append(f"**{QUEM[p['quem']]}** · {horas(p['tempo_min'])}\n")
            if p.get("comando"):
                lang = "powershell" if "powershell" in p["comando"] or p["comando"].startswith(("wsl ", "winget ")) else ("text" if p["comando"].startswith("http") else "bash")
                o.append(f"```{lang}\n{p['comando']}\n```\n")
            o.append(f"- [ ] **Pronto quando:** {p['pronto']}")
            if p.get("nota"):
                o.append(f"- {p['nota']}")
            if p.get("precisa"):
                o.append("- **Precisa:** " + ", ".join(PRECISA[x] for x in p["precisa"]))
            if p.get("ofertas"):
                o.append("- **Oferta:** " + " · ".join(OF[x] for x in p["ofertas"]))
            if p.get("blocos"):
                o.append("- Implanta: " + " · ".join(rotulo(B[b]) for b in p["blocos"]))
            o.append("")
    o += ['<a id="quando-entra-cada-bloco"></a>\n', "## Quando entra cada bloco\n",
          "Camada por camada, na mesma ordem do mapa. O número é o passo do roteiro.\n"]
    for c in eco["camadas"]:
        bs = [b for b in eco["blocos"] if b["camada"] == c["id"]]
        o += [f"### {c['titulo']}\n", "| Bloco | Passo | Quando |", "|---|---|---|"]
        for b in bs:
            ps = qb.get(b["id"], [])
            o.append(f"| {rotulo(b)} | {', '.join(x['num'] for x in ps)} | {'; '.join(dict.fromkeys(x['quando'] for x in ps))} |")
        o.append("")
    return "\n".join(o)


def dados_html(d: dict, eco: dict) -> dict:
    B = {b["id"]: b for b in eco["blocos"]}
    qb = quando_por_bloco(d)
    OF = {o["id"]: o["nome"] for o in carregar_portfolio()["ofertas"]}
    fases = [{**f, "passos": [{**{k: v for k, v in p.items() if k not in ("blocos", "ofertas")}, "hoje": faz_hoje(f, p),
                                "ofertas": [OF[x] for x in p.get("ofertas", [])],
                                "implanta": [rotulo(B[b]) for b in p.get("blocos", [])]} for p in f["passos"]]}
             for f in d["fases"]]
    camadas = [{"t": c["titulo"], "b": [[rotulo(b), [[x["num"], x["id"]] for x in qb.get(b["id"], [])],
                                          "; ".join(dict.fromkeys(x["quando"] for x in qb.get(b["id"], [])))]
                                         for b in eco["blocos"] if b["camada"] == c["id"]]} for c in eco["camadas"]]
    return {"precisa": PRECISA, "fases": fases, "camadas": camadas, "total_blocos": len(B)}


def gerar_html(d: dict, eco: dict | None = None) -> str:
    eco = eco if eco is not None else carregar_eco()
    dados = json.dumps(dados_html(d, eco), ensure_ascii=False).replace("</", "<\\/")
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", dados)
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/implantacao/gerar.py. Edite o template ou data/implantacao.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    d, eco = carregar(), carregar_eco()
    erros = validar(d, eco)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    saidas = {MD: gerar_md(d, eco), HTML: gerar_html(d, eco)}
    if a.check:
        ruins = [c for c, t in saidas.items() if (c.read_text(encoding="utf-8") if c.exists() else "") != t]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python tools/implantacao/gerar.py", file=sys.stderr)
        if ruins:
            return 1
        print("Roteiro de implantação em dia.")
        return 0
    for c, t in saidas.items():
        c.write_text(t, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
