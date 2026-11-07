#!/usr/bin/env python3
"""Catálogo único de ofertas do grupo: valida, pontua e gera a documentação.

Fonte: data/portfolio.json. Saídas: docs/operacao/portfolio.md e docs/operacao/portfolio.html.

Pontuação (0 a 18, quanto maior, antes entra na fila):
    2 × sinergia + escala + demanda − esforço − capital
Cada nota vai de 1 a 5. Sinergia pesa em dobro porque reaproveitar o que já existe
(aulas, código, livro, clientes, setup) é o que cabe na sua agenda.

Facilidade (4 a 20, quanto maior, mais rápido vira dinheiro):
    sinergia + demanda + (6 − esforço) + (6 − capital)

Arsenal: cada oferta tem perfil (passiva, ativa que vale a pena, ativa), automação (%),
veredito (agora, próxima, manter, fila, em2027, decidir, descartar) e o motivo. As regras
(hora mínima, teto de horas, máximo de rendas "agora") ficam em data/portfolio.json.

Uso:
    python tools/portfolio/portfolio.py          # valida e regenera
    python tools/portfolio/portfolio.py --check  # falha se algo estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DADOS = RAIZ / "data" / "portfolio.json"
IMPLANTACAO = RAIZ / "data" / "implantacao.json"
MD = RAIZ / "docs" / "operacao" / "portfolio.md"
HTML = RAIZ / "docs" / "operacao" / "portfolio.html"
TEMPLATE = RAIZ / "tools" / "portfolio" / "portfolio.template.html"
AVISO = "<!-- Arquivo GERADO por tools/portfolio/portfolio.py a partir de data/portfolio.json. Não edite à mão. -->\n"

ESTAGIOS = {"ideia": "Ideia", "validacao": "Validação", "construcao": "Construção", "lancado": "Lançado",
            "escala": "Escala", "pausado": "Pausado"}
ESCALAS = {"digital": "Digital (custo por cliente perto de zero)", "produtizado": "Produtizado (pacote repetível)",
           "local": "Local (depende de gente e lugar)"}
NOTAS = ("sinergia", "escala", "demanda", "esforco", "capital")
PERFIS = {"passiva": "Passiva (construída uma vez, vende sozinha)",
          "ativa_boa": "Ativa que vale a pena (paga bem por hora ou vira recorrência)",
          "ativa": "Ativa (sua hora presente, capital ou ganho baixo)"}
ESTADOS = {"existe": "Já existe", "parcial": "Parcial (falta ligar)", "construir": "Construir"}
VEREDITOS = {"agora": "Agora", "proxima": "Próxima da fila", "manter": "Manter (já funciona)", "fila": "Fila com portão",
             "em2027": "2027, se a tarde ficar livre", "decidir": "Decidir depois (capital alto)", "descartar": "Descartar"}


def carregar() -> dict:
    return json.loads(DADOS.read_text(encoding="utf-8"))


def pontuar(nota: dict) -> int:
    return 2 * nota["sinergia"] + nota["escala"] + nota["demanda"] - nota["esforco"] - nota["capital"]


def facilidade(nota: dict) -> int:
    return nota["sinergia"] + nota["demanda"] + (6 - nota["esforco"]) + (6 - nota["capital"])


def validar(dados: dict) -> list[str]:
    erros = []
    ids = [o["id"] for o in dados["ofertas"]]
    if len(ids) != len(set(ids)):
        erros.append("Há ofertas com id repetido.")
    conjunto = set(ids)
    for o in dados["ofertas"]:
        if o["frente"] not in dados["frentes"]:
            erros.append(f"{o['id']}: frente inexistente {o['frente']}")
        if o["estagio"] not in ESTAGIOS:
            erros.append(f"{o['id']}: estágio inválido {o['estagio']}")
        if o["escala"] not in ESCALAS:
            erros.append(f"{o['id']}: escala inválida {o['escala']}")
        for d in o["deriva_de"]:
            if d not in conjunto:
                erros.append(f"{o['id']}: deriva de oferta inexistente {d}")
            if d == o["id"]:
                erros.append(f"{o['id']}: deriva de si mesma")
        for k in NOTAS:
            v = o["nota"].get(k)
            if not isinstance(v, int) or not 1 <= v <= 5:
                erros.append(f"{o['id']}: nota {k} deve ser inteira de 1 a 5")
        if not o["proximo_passo"].strip():
            erros.append(f"{o['id']}: sem próximo passo")
        if o.get("perfil") not in PERFIS:
            erros.append(f"{o['id']}: perfil inválido {o.get('perfil')}")
        if o.get("veredito") not in VEREDITOS:
            erros.append(f"{o['id']}: veredito inválido {o.get('veredito')}")
        a = o.get("automacao")
        if not isinstance(a, int) or not 0 <= a <= 100:
            erros.append(f"{o['id']}: automação deve ser inteira de 0 a 100")
        if not str(o.get("motivo", "")).strip():
            erros.append(f"{o['id']}: sem motivo do veredito")
    auts = {a["id"]: a for a in dados.get("automacoes", [])}
    if len(auts) != len(dados.get("automacoes", [])):
        erros.append("Há automações com id repetido.")
    passos = passos_roteiro()
    for a in auts.values():
        if a["estado"] not in ESTADOS:
            erros.append(f"automação {a['id']}: estado inválido {a['estado']}")
        if passos and a.get("passo") and a["passo"] not in passos:
            erros.append(f"automação {a['id']}: passo {a['passo']} não existe no roteiro")
        if a["estado"] != "existe" and not a.get("passo"):
            erros.append(f"automação {a['id']}: falta o passo do roteiro que a constrói")
    usadas = set()
    for o in dados["ofertas"]:
        for u in o.get("usa", []):
            usadas.add(u)
            if u not in auts:
                erros.append(f"{o['id']}: usa automação inexistente {u}")
            elif auts[u].get("universal"):
                erros.append(f"{o['id']}: {u} é universal (vale para todas); não liste")
        if o.get("perfil") == "passiva" and not o.get("usa"):
            erros.append(f"{o['id']}: passiva sem nenhuma automação")
    for a in auts.values():
        if not a.get("universal") and a["id"] not in usadas:
            erros.append(f"automação {a['id']} não é usada por nenhuma oferta")
    rg = dados.get("regras", {})
    for k in ("hora_minima", "teto_horas_semana", "max_agora"):
        if not isinstance(rg.get(k), int) or rg[k] <= 0:
            erros.append(f"regras.{k} deve ser inteiro positivo")
    agora = [o["id"] for o in dados["ofertas"] if o.get("veredito") == "agora"]
    if isinstance(rg.get("max_agora"), int) and len(agora) > rg["max_agora"]:
        erros.append(f"{len(agora)} rendas em 'agora' ({', '.join(agora)}); o máximo é {rg['max_agora']}. Uma entra quando outra passar no portão.")
    ordens = [o.get("ordem") for o in dados["ofertas"] if o.get("veredito") == "proxima"]
    if None in ordens or len(ordens) != len(set(ordens)):
        erros.append("Toda oferta 'proxima' precisa de 'ordem' única.")
    return erros


def quando_ofertas() -> dict[str, str]:
    """'passo 15.3 · Semanas 11 a 13 · jan/2027' para cada oferta, a partir do roteiro de implantação."""
    if not IMPLANTACAO.exists():
        return {}
    im = json.loads(IMPLANTACAO.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for i, f in enumerate(im["fases"]):
        for j, p in enumerate(f["passos"], 1):
            for o in p.get("ofertas", []):
                out.setdefault(o, f"passo {i}.{j} · {f.get('quando', '')}")
    return out


def passos_roteiro() -> set[str]:
    if not IMPLANTACAO.exists():
        return set()
    im = json.loads(IMPLANTACAO.read_text(encoding="utf-8"))
    return {p["id"] for f in im["fases"] for p in f["passos"]}


def nivel(o: dict) -> str:
    """Quanto o setup toca sozinho: 'sozinho' (≥85%), 'perto' (50–84%) ou 'hora' (<50%)."""
    a = o["automacao"]
    return "sozinho" if a >= 85 else "perto" if a >= 50 else "hora"


NIVEIS = {"sozinho": "O setup faz tudo, menos criar uma vez e aprovar (85% ou mais)",
          "perto": "O setup faz a maior parte; você atende exceções (50% a 84%)",
          "hora": "Depende da sua hora ou de parceiro (menos de 50%)"}


def ordem_automacoes(dados: dict) -> list[dict]:
    """Automações em ordem de construção: primeiro as que destravam rendas 'agora' e 'próximas', depois as que destravam mais rendas."""
    peso = {"agora": 100, "proxima": 20, "manter": 5, "fila": 3, "em2027": 1, "decidir": 1, "descartar": 0}
    out = []
    for a in dados["automacoes"]:
        quem = [o for o in dados["ofertas"] if a["id"] in o.get("usa", [])] if not a["universal"] else list(dados["ofertas"])
        out.append(dict(a, n=len(quem), prioridade=sum(peso[o["veredito"]] for o in quem),
                        agora=[o["nome"] for o in quem if o["veredito"] in ("agora", "proxima")]))
    est = {"existe": 2, "parcial": 1, "construir": 0}
    return sorted(out, key=lambda a: (est[a["estado"]] == 2, -a["prioridade"], -a["n"], a["nome"]))


def ranking(dados: dict) -> list[dict]:
    q = quando_ofertas()
    ofs = [dict(o, pontos=pontuar(o["nota"]), facil=facilidade(o["nota"]), nivel=nivel(o), quando=q.get(o["id"], "")) for o in dados["ofertas"]]
    return sorted(ofs, key=lambda o: (-o["pontos"], o["nome"]))


def esc_md(s: str) -> str:
    return s.replace("|", "\\|")


def gerar_arsenal(dados: dict, rk: list[dict]) -> list[str]:
    rg = dados["regras"]
    F = dados["frentes"]
    o = ["## Arsenal: o que entra agora e o que não dá\n",
         f"**Regras:** hora mínima de **R$ {rg['hora_minima']}** por hora sua em trabalho ativo extra; teto de **{rg['teto_horas_semana']} horas** extras por semana; "
         f"no máximo **{rg['max_agora']} rendas em \"agora\"**; portão para a próxima entrar: {rg['portao']}; corte: {rg['corte']}.\n",
         "**Facilidade = sinergia + demanda + (6 − esforço) + (6 − capital)** (de 4 a 20): quanto maior, mais rápido vira dinheiro com o que você já tem.\n",
         "A semana do arsenal:\n"]
    o += [f"- {b}" for b in rg["blocos_da_semana"]]
    o.append("")
    o.append("| Veredito | Ofertas | Passivas |\n|---|---:|---:|")
    for k, v in VEREDITOS.items():
        g = [x for x in rk if x["veredito"] == k]
        o.append(f"| {v} | {len(g)} | {sum(x['perfil'] == 'passiva' for x in g)} |")
    o.append("")
    def tabela(titulo, grupo, com_ordem=False):
        if not grupo:
            return
        o.append(f"### {titulo}\n")
        o.append(("| Ordem " if com_ordem else "") + "| Oferta | Marca | Perfil | Automático | Facilidade | Por quê |")
        o.append(("|---:" if com_ordem else "") + "|---|---|---|---:|---:|---|")
        for x in grupo:
            ini = f"| {x.get('ordem', '')} " if com_ordem else ""
            o.append(f"{ini}| {esc_md(x['nome'])} | {F[x['frente']]} | {PERFIS[x['perfil']].split(' (')[0]} | {x['automacao']}% | {x['facil']} | {esc_md(x['motivo'])} |")
        o.append("")
    por_facil = sorted(rk, key=lambda x: (-x["facil"], -x["pontos"], x["nome"]))
    tabela("Agora", [x for x in por_facil if x["veredito"] == "agora"])
    tabela("Próximas, nesta ordem", sorted([x for x in rk if x["veredito"] == "proxima"], key=lambda x: x["ordem"]), True)
    tabela("Manter", [x for x in por_facil if x["veredito"] == "manter"])
    tabela("Fila com portão (da mais fácil para a mais difícil)", [x for x in por_facil if x["veredito"] == "fila"])
    tabela("2027, se a tarde ficar livre", [x for x in por_facil if x["veredito"] == "em2027"])
    tabela("Decidir depois: capital alto", [x for x in por_facil if x["veredito"] == "decidir"])
    tabela("Descartadas (revisão trimestral)", [x for x in por_facil if x["veredito"] == "descartar"])
    o += gerar_automacoes(dados, rk)
    return o


def gerar_automacoes(dados: dict, rk: list[dict]) -> list[str]:
    nomes = {a["id"]: a["nome"] for a in dados["automacoes"]}
    o = ["## Automações: o que o setup faz sozinho e o que falta construir\n",
         "Nenhuma renda é 100% automática: alguém cria uma vez, aprova e atende a exceção. "
         "O que dá para fazer é construir **uma vez** as automações que várias rendas usam. "
         "O painel e os comandos pelo Telegram valem para todas.\n",
         "| Quanto o setup faz | Ofertas | Ativas agora ou próximas |\n|---|---:|---:|"]
    for k, v in NIVEIS.items():
        g = [x for x in rk if x["nivel"] == k]
        o.append(f"| {v} | {len(g)} | {sum(x['veredito'] in ('agora', 'proxima') for x in g)} |")
    o.append("")
    o.append("### Ordem de construção\n")
    o.append("Primeiro as que destravam as rendas de agora e as próximas; depois as que destravam mais rendas. As que já existem ficam no fim.\n")
    o.append("| # | Automação | Estado | Destrava | Rendas de agora e próximas | Passo |\n|---:|---|---|---:|---|---|")
    for i, a in enumerate(ordem_automacoes(dados), 1):
        ag = esc_md(", ".join(a["agora"])) or "—"
        o.append(f"| {i} | **{esc_md(a['nome'])}**: {esc_md(a['faz'])} | {ESTADOS[a['estado']]} | {'todas' if a['universal'] else a['n']} | {ag} | {a.get('passo') or '—'} |")
    o.append("")
    o.append("### O que o setup faz sozinho, por oferta\n")
    o.append("| Oferta | Veredito | Automático | Usa |\n|---|---|---:|---|")
    for x in sorted(rk, key=lambda x: (-x["automacao"], x["nome"])):
        o.append(f"| {esc_md(x['nome'])} | {VEREDITOS[x['veredito']]} | {x['automacao']}% | {esc_md(', '.join(nomes[u] for u in x['usa']))} |")
    o.append("")
    return o


def gerar_md(dados: dict) -> str:
    rk = ranking(dados)
    F = dados["frentes"]
    o = [AVISO, "# Portfólio de ofertas\n", "[← Operação do grupo](README.md)\n",
         f"Todas as {len(rk)} ofertas do grupo num catálogo só: o que já existe, o que está planejado e "
         f"{sum(x['nova'] for x in rk)} fontes de renda novas que saem do que você já tem. "
         "A versão interativa, com filtros, é [`portfolio.html`](portfolio.html).\n",
         "## Como a fila é decidida\n",
         "**Pontos = 2 × sinergia + escala + demanda − esforço − capital** (cada nota de 1 a 5; máximo 18).\n",
         "- **Sinergia:** quanto reaproveita do que já existe (suas aulas, código, livro, clientes, setup).",
         "- **Escala:** 5 quando cada cliente novo quase não custa nada; 1 quando cada venda pede você presente.",
         "- **Demanda:** evidência de que alguém paga. Nas ideias novas, é hipótese até a validação.",
         "- **Esforço e capital:** horas e dinheiro até a primeira venda.\n",
         "A pontuação ordena; quem decide é a [ordem de execução](07-ordem-de-execucao.md), que respeita a sua agenda e os portões dos negócios físicos.\n",
         *gerar_arsenal(dados, rk),
         "## Ranking geral\n",
         "| # | Oferta | Frente | Estágio | Escala | Pontos | Próximo passo | Quando entra |",
         "|---:|---|---|---|---|---:|---|---|"]
    for i, x in enumerate(rk, 1):
        nome = f"[{esc_md(x['nome'])}]({x['doc']})" if x.get("doc") else esc_md(x["nome"])
        if x["nova"]:
            nome += " · **nova**"
        o.append(f"| {i} | {nome} | {F[x['frente']]} | {ESTAGIOS[x['estagio']]} | {x['escala'].capitalize()} | "
                 f"{x['pontos']} | {esc_md(x['proximo_passo'])} | {esc_md(x['quando'])} |")
    o.append("")
    o.append("## Fontes de renda novas\n")
    o.append("Ideias que nasceram do cruzamento entre os negócios, as aulas, o livro e o setup. Cada uma começa pela validação mais barata possível.\n")
    o.append("| Oferta | Sai de | Modelo de receita | Validação mais barata | Pontos |\n|---|---|---|---|---:|")
    nomes = {x["id"]: x["nome"] for x in rk}
    for x in rk:
        if x["nova"]:
            de = ", ".join(nomes[d] for d in x["deriva_de"]) or "—"
            o.append(f"| {esc_md(x['nome'])} | {esc_md(de)} | {x['receita']} | {esc_md(x['proximo_passo'])} | {x['pontos']} |")
    o.append("")
    o.append("## De onde cada oferta nasce\n")
    o.append("Cada seta é um reaproveitamento: a oferta de baixo usa conteúdo, código, clientes ou estrutura da de cima.\n")
    o.append("```mermaid\nflowchart LR")
    usados = {d for x in rk for d in x["deriva_de"]} | {x["id"] for x in rk if x["deriva_de"]}
    for x in rk:
        if x["id"] in usados:
            rot = x["nome"].split(" (")[0].replace('"', "'")
            if len(rot) > 34:
                rot = rot[:32] + "…"
            o.append(f'  {x["id"]}["{rot}"]')
    for x in rk:
        for d in x["deriva_de"]:
            o.append(f"  {d} --> {x['id']}")
    novas = [x["id"] for x in rk if x["nova"] and x["id"] in usados]
    o.append("  classDef nova fill:#f3e7d3,stroke:#8a5e22,color:#13262b")
    if novas:
        o.append("  class " + ",".join(novas) + " nova")
    o.append("```\n")
    o.append("## Por frente\n")
    for fid, ftit in F.items():
        grupo = [x for x in rk if x["frente"] == fid]
        o.append(f"### {ftit}\n")
        o.append("| Oferta | Receita | Automático | Fica com você | Métrica |\n|---|---|---|---|---|")
        for x in grupo:
            auto = ", ".join(x["automatico"]) or "—"
            hum = ", ".join(x["humano"]) or "—"
            o.append(f"| {esc_md(x['nome'])} | {x['receita']} | {esc_md(auto)} | {esc_md(hum)} | {esc_md(x['metrica'])} |")
        o.append("")
    o.append("## Resumo\n")
    o.append("| Estágio | Ofertas |\n|---|---:|")
    for k, v in ESTAGIOS.items():
        n = sum(1 for x in rk if x["estagio"] == k)
        if n:
            o.append(f"| {v} | {n} |")
    o.append("")
    o.append("| Escala | Ofertas |\n|---|---:|")
    for k, v in ESCALAS.items():
        o.append(f"| {v} | {sum(1 for x in rk if x['escala'] == k)} |")
    o.append("")
    return "\n".join(o)


def gerar_html(dados: dict) -> str:
    payload = {"frentes": dados["frentes"], "estagios": ESTAGIOS, "escalas": ESCALAS, "perfis": PERFIS,
               "vereditos": VEREDITOS, "regras": dados["regras"], "ofertas": ranking(dados),
               "automacoes": {a["id"]: a["nome"] for a in dados["automacoes"]}}
    corpo = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", json.dumps(payload, ensure_ascii=False).replace("</", "<\\/"))
    return ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            "<!-- Arquivo GERADO por tools/portfolio/portfolio.py. Edite o template ou data/portfolio.json. -->\n"
            "</head>\n<body>\n" + corpo + "\n</body>\n</html>\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    dados = carregar()
    erros = validar(dados)
    if erros:
        for e in erros:
            print("ERRO:", e, file=sys.stderr)
        return 1
    saidas = {MD: gerar_md(dados), HTML: gerar_html(dados)}
    if a.check:
        ruins = [c for c, t in saidas.items() if (c.read_text(encoding="utf-8") if c.exists() else "") != t]
        for c in ruins:
            print(f"{c.relative_to(RAIZ)} está desatualizado. Rode: python tools/portfolio/portfolio.py", file=sys.stderr)
        if ruins:
            return 1
        print(f"Portfólio em dia: {len(dados['ofertas'])} ofertas.")
        return 0
    for c, t in saidas.items():
        c.write_text(t, encoding="utf-8")
        print(f"Gerado {c.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
