#!/usr/bin/env python3
"""Calculadora da nota base CVSS 3.1 (a escala usada em relatórios de pentest e em CVEs).

    python tools/seguranca/cvss.py "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
    -> 9.8 Crítica

Segue a especificação oficial do FIRST (https://www.first.org/cvss/v3.1/specification-document),
inclusive o arredondamento "Roundup" da seção 7.4. Só a nota base: as notas temporal e de ambiente
dependem do cliente e entram no relatório como texto.

O CVSS 4.0 já existe, mas a 3.1 continua sendo a mais pedida em contratos e plataformas de bug bounty;
se o cliente pedir a 4.0, use a calculadora oficial do FIRST e registre o vetor no achado.
"""
from __future__ import annotations

import argparse
import math
import sys

PESOS = {
    "AV": {"N": 0.85, "A": 0.62, "L": 0.55, "P": 0.2},
    "AC": {"L": 0.77, "H": 0.44},
    "UI": {"N": 0.85, "R": 0.62},
    "C": {"H": 0.56, "L": 0.22, "N": 0.0},
    "I": {"H": 0.56, "L": 0.22, "N": 0.0},
    "A": {"H": 0.56, "L": 0.22, "N": 0.0},
}
PR = {"U": {"N": 0.85, "L": 0.62, "H": 0.27}, "C": {"N": 0.85, "L": 0.68, "H": 0.5}}
OBRIGATORIAS = ("AV", "AC", "PR", "UI", "S", "C", "I", "A")
SEVERIDADES = ((9.0, "Crítica"), (7.0, "Alta"), (4.0, "Média"), (0.1, "Baixa"), (0.0, "Nenhuma"))


class VetorInvalido(ValueError):
    """O vetor não segue o formato CVSS:3.1/AV:_/AC:_/PR:_/UI:_/S:_/C:_/I:_/A:_."""


def roundup(x: float) -> float:
    """Arredonda para cima com uma casa, como a seção 7.4 da especificação 3.1 manda."""
    inteiro = round(x * 100000)
    if inteiro % 10000 == 0:
        return inteiro / 100000.0
    return (math.floor(inteiro / 10000) + 1) / 10.0


def ler_vetor(vetor: str) -> dict[str, str]:
    partes = vetor.strip().split("/")
    if not partes or partes[0] not in ("CVSS:3.1", "CVSS:3.0"):
        raise VetorInvalido(f"o vetor deve começar com CVSS:3.1 (recebido: {vetor!r})")
    m: dict[str, str] = {}
    for p in partes[1:]:
        if ":" not in p:
            raise VetorInvalido(f"métrica sem valor: {p!r}")
        k, v = p.split(":", 1)
        if k in m:
            raise VetorInvalido(f"métrica repetida: {k}")
        m[k] = v
    faltam = [k for k in OBRIGATORIAS if k not in m]
    if faltam:
        raise VetorInvalido(f"faltam métricas base: {', '.join(faltam)}")
    if m["S"] not in ("U", "C"):
        raise VetorInvalido(f"S deve ser U ou C (recebido: {m['S']})")
    for k, tabela in PESOS.items():
        if m[k] not in tabela:
            raise VetorInvalido(f"{k}:{m[k]} não existe (use {', '.join(tabela)})")
    if m["PR"] not in PR["U"]:
        raise VetorInvalido(f"PR:{m['PR']} não existe (use N, L ou H)")
    return m


def nota_base(vetor: str) -> float:
    m = ler_vetor(vetor)
    mudou = m["S"] == "C"
    iss = 1 - (1 - PESOS["C"][m["C"]]) * (1 - PESOS["I"][m["I"]]) * (1 - PESOS["A"][m["A"]])
    if mudou:
        impacto = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15
    else:
        impacto = 6.42 * iss
    explorabilidade = 8.22 * PESOS["AV"][m["AV"]] * PESOS["AC"][m["AC"]] * PR[m["S"]][m["PR"]] * PESOS["UI"][m["UI"]]
    if impacto <= 0:
        return 0.0
    if mudou:
        return roundup(min(1.08 * (impacto + explorabilidade), 10))
    return roundup(min(impacto + explorabilidade, 10))


def severidade(nota: float) -> str:
    for minimo, nome in SEVERIDADES:
        if nota >= minimo:
            return nome
    return "Nenhuma"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Nota base CVSS 3.1")
    ap.add_argument("vetor", help='ex.: "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"')
    a = ap.parse_args(argv)
    try:
        n = nota_base(a.vetor)
    except VetorInvalido as e:
        print(f"ERRO: {e}", file=sys.stderr)
        return 2
    print(f"{n:.1f} {severidade(n)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
