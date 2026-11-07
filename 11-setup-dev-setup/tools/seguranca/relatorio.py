#!/usr/bin/env python3
"""Gera o relatório de pentest (Markdown) a partir do escopo assinado e dos achados.

    python tools/seguranca/relatorio.py ~/clientes/loja/escopo.toml ~/clientes/loja/achados.toml
    python tools/seguranca/relatorio.py ESCOPO ACHADOS --saida relatorio.md

O relatório segue a ordem que o cliente lê: sumário executivo (para quem decide), escopo e regras,
metodologia, achados do mais grave ao mais leve (para quem corrige) e o registro de atividades
(o registro.jsonl que o escopo.py grava). A nota de cada achado sai do vetor CVSS 3.1, nunca à mão.

Recusa gerar se um achado apontar para um ativo fora do escopo: achado fora do escopo é prova de
teste não autorizado, não entra em relatório.
Modelo dos achados: infra/templates/seguranca/achados.example.toml.
"""
from __future__ import annotations

import argparse
import json
import sys
import tomllib
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import escopo as esc  # noqa: E402
from cvss import VetorInvalido, nota_base, severidade  # noqa: E402

CAMPOS = ("id", "titulo", "vetor", "ativo", "descricao", "evidencia", "impacto", "recomendacao")
STATUS = {"aberto": "Aberto", "corrigido": "Corrigido (reteste ok)", "aceito": "Risco aceito pelo cliente"}
ORDEM_SEV = ("Crítica", "Alta", "Média", "Baixa", "Nenhuma")


def carregar_achados(caminho: Path) -> dict:
    with open(caminho, "rb") as f:
        return tomllib.load(f)


def validar(escopo: dict, achados: dict) -> list[str]:
    erros = [f"escopo: {e}" for e in esc.validar(escopo)]
    lista = achados.get("achado", [])
    if not lista:
        erros.append("nenhum achado: um teste limpo também tem relatório; registre um item informativo com C:N/I:N/A:N (nota 0)")
    vistos = set()
    for a in lista:
        ident = a.get("id", "?")
        for c in CAMPOS:
            if not str(a.get(c, "")).strip():
                erros.append(f"{ident}: falta '{c}'")
        if ident in vistos:
            erros.append(f"id repetido: {ident}")
        vistos.add(ident)
        try:
            nota_base(a.get("vetor", ""))
        except VetorInvalido as e:
            erros.append(f"{ident}: vetor CVSS inválido ({e})")
        if a.get("status", "aberto") not in STATUS:
            erros.append(f"{ident}: status inválido {a.get('status')} (use {', '.join(STATUS)})")
        if a.get("ativo") and not _no_escopo(escopo, a["ativo"]):
            erros.append(f"{ident}: o ativo {a['ativo']} está fora do escopo assinado")
    return erros


def _no_escopo(escopo: dict, ativo: str) -> bool:
    """Confere só os alvos e as exclusões (a janela vale para testar, não para escrever o relatório)."""
    meio = esc._data(escopo["janela"]["inicio"])
    ok, _ = esc.checar(escopo, ativo, agora=meio)
    return ok


def ordenar(lista: list[dict]) -> list[dict]:
    return sorted(lista, key=lambda a: (-nota_base(a["vetor"]), a["id"]))


def gerar(escopo: dict, achados: dict, registro: list[dict] | None = None) -> str:
    lista = ordenar(achados["achado"])
    contagem = {s: 0 for s in ORDEM_SEV}
    for a in lista:
        contagem[severidade(nota_base(a["vetor"]))] += 1
    abertos = [a for a in lista if a.get("status", "aberto") == "aberto"]
    jan = escopo["janela"]
    o = [f"# {achados.get('titulo', 'Relatório de teste de intrusão')}", "",
         f"**Cliente:** {escopo['cliente']}  ", f"**Contrato:** {escopo['contrato']}  ",
         f"**Período do teste:** {esc._data(jan['inicio']):%d/%m/%Y %H:%M} a {esc._data(jan['fim']):%d/%m/%Y %H:%M}  ",
         f"**Autorizado por:** {escopo['autorizacao']['assinada_por']} em {escopo['autorizacao']['assinada_em']}  ",
         f"**Responsável técnico:** {achados.get('responsavel', 'a preencher')}", "",
         "> Documento confidencial. Contém detalhes de vulnerabilidades: guarde e compartilhe só com quem vai corrigir.", "",
         "## 1. Sumário executivo", ""]
    if achados.get("resumo"):
        o += [achados["resumo"].strip(), ""]
    o += ["| Severidade | Achados |", "|---|---:|"]
    o += [f"| {s} | {contagem[s]} |" for s in ORDEM_SEV if s != "Nenhuma" or contagem[s]]
    o += ["", f"Em aberto no fim do teste: **{len(abertos)}** de {len(lista)}.", ""]
    if abertos:
        o += ["Prioridades de correção:", ""]
        o += [f"{i}. **{a['titulo']}** ({severidade(nota_base(a['vetor']))}, {a['ativo']})" for i, a in enumerate(abertos[:3], 1)]
        o.append("")
    al, fo = escopo["alvos"], escopo.get("fora", {})
    o += ["## 2. Escopo e regras de engajamento", "", "**Dentro do escopo:**", ""]
    o += [f"- {x}" for k in ("dominios", "ips", "urls") for x in al.get(k, [])]
    if any(fo.get(k) for k in ("dominios", "ips", "urls")):
        o += ["", "**Fora do escopo (não testado):**", ""]
        o += [f"- {x}" for k in ("dominios", "ips", "urls") for x in fo.get(k, [])]
    proib = escopo.get("regras", {}).get("proibido", [])
    if proib:
        o += ["", "**Não realizado por acordo:** " + "; ".join(proib) + "."]
    o += ["", "## 3. Metodologia", ""]
    for m in achados.get("metodologia", ["OWASP Web Security Testing Guide", "PTES (Penetration Testing Execution Standard)"]):
        o.append(f"- {m}")
    o += ["", "A severidade usa a nota base CVSS 3.1 (FIRST). Cada achado traz o vetor completo para conferência.", "",
          "## 4. Achados", ""]
    for a in lista:
        n = nota_base(a["vetor"])
        o += [f"### {a['id']} · {a['titulo']}", "",
              "| Severidade | CVSS 3.1 | Ativo | Status |", "|---|---|---|---|",
              f"| {severidade(n)} | {n:.1f} (`{a['vetor']}`) | {a['ativo']} | {STATUS[a.get('status', 'aberto')]} |", "",
              "**Descrição.** " + a["descricao"].strip(), "",
              "**Evidência.** " + a["evidencia"].strip(), "",
              "**Impacto.** " + a["impacto"].strip(), "",
              "**Recomendação.** " + a["recomendacao"].strip(), ""]
        if a.get("referencias"):
            o += ["**Referências:** " + ", ".join(a["referencias"]), ""]
    o += ["## 5. Registro de atividades", ""]
    if registro:
        o += ["| Quando (UTC) | Alvo | Comando | Saída |", "|---|---|---|---:|"]
        o += [f"| {r['quando']} | {r['alvo']} | `{r['comando']}` | {r['codigo_saida']} |" for r in registro]
    else:
        o.append("Sem registro anexado (rode os testes pelo `escopo.py rodar` para gerar o registro.jsonl).")
    o += ["", "## 6. Próximos passos", "",
          "1. Corrigir os achados na ordem de severidade.",
          "2. Pedir o reteste: cada correção é conferida e o status muda para \"Corrigido\" numa nova versão deste relatório.",
          "3. Repetir o teste a cada mudança grande no sistema ou, no mínimo, uma vez por ano.", ""]
    return "\n".join(o)


def ler_registro(pasta: Path) -> list[dict]:
    reg = pasta / "registro.jsonl"
    if not reg.exists():
        return []
    return [json.loads(x) for x in reg.read_text(encoding="utf-8").splitlines() if x.strip()]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Relatório de pentest a partir do escopo e dos achados")
    ap.add_argument("escopo", type=Path)
    ap.add_argument("achados", type=Path)
    ap.add_argument("--saida", type=Path, help="arquivo .md (padrão: relatorio.md ao lado dos achados)")
    a = ap.parse_args(argv)
    escopo, achados = esc.carregar(a.escopo), carregar_achados(a.achados)
    erros = validar(escopo, achados)
    if erros:
        for e in erros:
            print(f"ERRO: {e}", file=sys.stderr)
        return 1
    saida = a.saida or a.achados.parent / "relatorio.md"
    saida.write_text(gerar(escopo, achados, ler_registro(Path(escopo["_pasta"]))), encoding="utf-8")
    print(f"Relatório gerado: {saida} ({len(achados['achado'])} achados)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
