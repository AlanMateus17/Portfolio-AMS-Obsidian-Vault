#!/usr/bin/env python3
"""Registro de uma linha: o caderno de erros do estudo e os atritos do setup.

Os dois viram um arquivo só cada, no seu vault, para você nunca precisar abrir arquivo para anotar:
  - 07-estudo-e-carreira/caderno-de-erros.md : o erro, por que errou e o certo. Volta nas revisões e vira cartão.
  - 06-execucao-e-desenvolvimento/atritos-do-setup.md : o que foi manual, lento, quebrou ou se repetiu.
    Pela sua regra, o que aparece 3 vezes vira script ou automação do setup.

    python3 tools/registro/registro.py erro 0.2 "neguei 'todos são' como 'todos não são'" --certo "algum não é"
    python3 tools/registro/registro.py erros [--assunto 0.2]
    python3 tools/registro/registro.py atrito "conferir o backup à mão" --area backup
    python3 tools/registro/registro.py atritos               # agrupados, os repetidos 3 vezes ou mais primeiro
    python3 tools/registro/registro.py diag 0.1 c3 x2 c1 --min 4   # diagnóstico: certo/errado + certeza 1 a 3

O diagnóstico vira uma linha em 07-estudo-e-carreira/diagnosticos.md e devolve a decisão do roteiro
(pular o apoio ou fazer o roteiro inteiro). Um acerto no chute (c1) conta como não saber.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import Counter
from datetime import date
from pathlib import Path

LIMITE = 400  # uma linha curta, com as suas palavras
ERROS_CAB = ("# Caderno de erros\n\n"
             "Gerado por `just erro`. Cada erro volta nas revisões: transforme o \"certo\" em cartão do Anki.\n\n"
             "| Data | Assunto | O erro | O certo |\n|---|---|---|---|\n")
ATRITOS_CAB = ("# Atritos do setup\n\n"
               "Gerado por `just atrito`. O que foi manual, lento, quebrou ou se repetiu. "
               "O que aparece 3 vezes vira script ou automação (regra do setup).\n\n"
               "| Data | Área | O que aconteceu |\n|---|---|---|\n")


DIAG_CAB = ("# Diagnósticos\n\n"
            "Gerado por `just diag`. Antes de cada assunto: responder sem consulta, dar a certeza (1 chute, 2 acho, "
            "3 certeza) e só então conferir. Erro com certeza 3 vai para o caderno de erros na hora.\n\n"
            "| Data | Assunto | Acertos | Erros com certeza | Chutes certos | Minutos | Decisão |\n|---|---|---|---|---|---|---|\n")
CERTEZA = {"1": "chute", "2": "acho", "3": "certeza"}


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def arq_erros() -> Path:
    return vault() / "07-estudo-e-carreira" / "caderno-de-erros.md"


def arq_atritos() -> Path:
    return vault() / "06-execucao-e-desenvolvimento" / "atritos-do-setup.md"


def celula(s: str) -> str:
    return s.replace("|", "/").replace("\n", " ").strip()


def checar(*textos: str) -> None:
    for t in textos:
        if not t.strip():
            raise SystemExit("texto vazio")
        if len(t) > LIMITE:
            raise SystemExit(f"texto com {len(t)} caracteres (máximo {LIMITE}): escreva em uma linha, com as suas palavras")


def anexar(arq: Path, cabecalho: str, colunas: list[str], hoje: date | None = None) -> Path:
    arq.parent.mkdir(parents=True, exist_ok=True)
    if not arq.exists():
        arq.write_text(cabecalho, encoding="utf-8")
    dia = (hoje or date.today()).isoformat()
    with arq.open("a", encoding="utf-8") as f:
        f.write("| " + " | ".join([dia] + [celula(c) for c in colunas]) + " |\n")
    return arq


def linhas(arq: Path) -> list[list[str]]:
    if not arq.exists():
        return []
    return [[c.strip() for c in ln.strip("|").split("|")]
            for ln in arq.read_text(encoding="utf-8").splitlines() if ln.startswith("| 2")]


def erro(assunto: str, texto: str, certo: str, hoje: date | None = None) -> Path:
    checar(assunto, texto, certo)
    return anexar(arq_erros(), ERROS_CAB, [assunto, texto, certo], hoje)


def atrito(texto: str, area: str, hoje: date | None = None) -> Path:
    checar(texto, area)
    return anexar(arq_atritos(), ATRITOS_CAB, [area, texto], hoje)


def arq_diag() -> Path:
    return vault() / "07-estudo-e-carreira" / "diagnosticos.md"


def ler_respostas(respostas: list[str]) -> list[tuple[bool, int]]:
    """'c3' = certo com certeza 3; 'x1' = errado no chute. Recusa qualquer outra forma."""
    saida = []
    for r in respostas:
        r = r.strip().lower()
        if len(r) != 2 or r[0] not in "cx" or r[1] not in CERTEZA:
            raise SystemExit(f"resposta '{r}' inválida: use c ou x (certo/errado) + certeza 1, 2 ou 3. Ex.: c3 x2 c1")
        saida.append((r[0] == "c", int(r[1])))
    if not saida:
        raise SystemExit("informe pelo menos uma resposta. Ex.: just diag 0.1 c3 x2 c1")
    return saida


def avaliar(resp: list[tuple[bool, int]]) -> dict:
    total = len(resp)
    acertos = sum(1 for certo, _ in resp if certo)
    sabe = sum(1 for certo, conf in resp if certo and conf >= 2)
    confiantes_errados = [i + 1 for i, (certo, conf) in enumerate(resp) if not certo and conf == 3]
    chutes = [i + 1 for i, (certo, conf) in enumerate(resp) if certo and conf == 1]
    rapido = sabe == total
    return {"total": total, "acertos": acertos, "errados_com_certeza": confiantes_errados, "chutes_certos": chutes,
            "decisao": "modo rápido: pular o apoio" if rapido else "roteiro inteiro", "rapido": rapido}


def diag(assunto: str, respostas: list[str], minutos: int = 0, hoje: date | None = None) -> dict:
    checar(assunto)
    av = avaliar(ler_respostas(respostas))
    lista = lambda xs: ", ".join(str(x) for x in xs) or "nenhum"
    anexar(arq_diag(), DIAG_CAB, [assunto, f"{av['acertos']}/{av['total']}", lista(av["errados_com_certeza"]),
                                  lista(av["chutes_certos"]), str(minutos or "-"), av["decisao"]], hoje)
    return av


def resumo_atritos() -> list[tuple[str, int]]:
    """Conta por (área + texto em minúsculas): o mesmo atrito anotado de novo soma."""
    cont = Counter(f"{c[1]}: {c[2].lower()}" for c in linhas(arq_atritos()))
    return sorted(cont.items(), key=lambda x: (-x[1], x[0]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    p = s.add_parser("erro"); p.add_argument("assunto"); p.add_argument("texto"); p.add_argument("--certo", required=True)
    p = s.add_parser("erros"); p.add_argument("--assunto")
    p = s.add_parser("atrito"); p.add_argument("texto"); p.add_argument("--area", default="geral")
    s.add_parser("atritos")
    p = s.add_parser("diag"); p.add_argument("assunto"); p.add_argument("respostas", nargs="*"); p.add_argument("--min", type=int, default=0)
    a = ap.parse_args(argv)
    if a.cmd == "erro":
        print(f"Anotado em {erro(a.assunto, a.texto, a.certo)}. Faça o cartão do Anki com o \"certo\".")
    elif a.cmd == "erros":
        ls = [c for c in linhas(arq_erros()) if not a.assunto or c[1] == a.assunto]
        for c in ls:
            print(f"{c[0]} [{c[1]}] {c[2]}  →  {c[3]}")
        print(f"{len(ls)} erros.")
    elif a.cmd == "atrito":
        print(f"Anotado em {atrito(a.texto, a.area)}.")
    elif a.cmd == "diag":
        av = diag(a.assunto, a.respostas, a.min)
        print(f"Diagnóstico {a.assunto}: {av['acertos']}/{av['total']} certos. Decisão: {av['decisao']}.")
        for q in av["errados_com_certeza"]:
            print(f"  Pergunta {q}: errou com certeza. Prioridade máxima: leia a resposta comentada agora e anote:\n"
                  f"    just erro {a.assunto} \"o que eu achava\" --certo \"o que é\"")
        for q in av["chutes_certos"]:
            print(f"  Pergunta {q}: acertou no chute. Conta como não saber: estude essa parte normalmente.")
        print(f"  Registrado em {arq_diag()}.")
    elif a.cmd == "atritos":
        for chave, n in resumo_atritos():
            marca = "  ← 3 vezes: vira script/automação" if n >= 3 else ""
            print(f"{n}x {chave}{marca}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
