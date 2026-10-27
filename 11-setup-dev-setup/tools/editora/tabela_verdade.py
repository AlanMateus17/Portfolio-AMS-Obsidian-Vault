#!/usr/bin/env python3
"""Gera a tabela-verdade de uma proposição em LaTeX ou Markdown.

Conectivos aceitos (do mais forte ao mais fraco):
    ~  ou ¬   negação
    &  ou ∧   conjunção
    |  ou ∨   disjunção
    ^  ou ⊕   disjunção exclusiva
    -> ou →   condicional
    <-> ou ↔  bicondicional

Uso:
    python tools/editora/tabela_verdade.py "(p -> q) <-> (~q -> ~p)"
    python tools/editora/tabela_verdade.py "p & ~p" --formato latex
"""
from __future__ import annotations

import argparse
import itertools
import re
import sys
from dataclasses import dataclass

SIMBOLOS = {"¬": "~", "∧": "&", "∨": "|", "⊕": "^", "→": "->", "↔": "<->"}
TOKEN = re.compile(r"\s*(<->|->|[~&|^()]|[a-z]\w*)")
LATEX_OP = {"~": r"\neg ", "&": r"\land", "|": r"\lor", "^": r"\oplus", "->": r"\to", "<->": r"\leftrightarrow"}


@dataclass(frozen=True)
class No:
    op: str | None
    filhos: tuple = ()
    nome: str | None = None

    def avaliar(self, v: dict[str, bool]) -> bool:
        if self.nome is not None:
            return v[self.nome]
        a = [f.avaliar(v) for f in self.filhos]
        return {
            "~": lambda: not a[0],
            "&": lambda: a[0] and a[1],
            "|": lambda: a[0] or a[1],
            "^": lambda: a[0] != a[1],
            "->": lambda: (not a[0]) or a[1],
            "<->": lambda: a[0] == a[1],
        }[self.op]()

    def latex(self, topo: bool = True) -> str:
        if self.nome is not None:
            return self.nome
        if self.op == "~":
            return LATEX_OP["~"] + self.filhos[0].latex(False)
        s = f"{self.filhos[0].latex(False)} {LATEX_OP[self.op]} {self.filhos[1].latex(False)}"
        return s if topo else f"({s})"

    def texto(self, topo: bool = True) -> str:
        if self.nome is not None:
            return self.nome
        if self.op == "~":
            return "¬" + self.filhos[0].texto(False)
        sim = {"&": "∧", "|": "∨", "^": "⊕", "->": "→", "<->": "↔"}[self.op]
        s = f"{self.filhos[0].texto(False)} {sim} {self.filhos[1].texto(False)}"
        return s if topo else f"({s})"


def tokens(expr: str) -> list[str]:
    for k, v in SIMBOLOS.items():
        expr = expr.replace(k, v)
    pos, out = 0, []
    expr = expr.strip()
    while pos < len(expr):
        m = TOKEN.match(expr, pos)
        if not m:
            raise ValueError(f"Símbolo não reconhecido na posição {pos + 1}: {expr[pos:]!r}")
        out.append(m.group(1))
        pos = m.end()
        while pos < len(expr) and expr[pos].isspace():
            pos += 1
    return out


class Parser:
    # precedência: <-> (mais fraca) < -> < ^ < | < & < ~ (mais forte); -> é associativo à direita
    NIVEIS = ["<->", "->", "^", "|", "&"]

    def __init__(self, ts: list[str]):
        self.ts, self.i = ts, 0

    def ver(self):
        return self.ts[self.i] if self.i < len(self.ts) else None

    def comer(self, t=None):
        x = self.ver()
        if x is None or (t is not None and x != t):
            raise ValueError(f"Esperado {t or 'mais símbolos'}, encontrado {x!r}")
        self.i += 1
        return x

    def binario(self, n: int) -> No:
        if n == len(self.NIVEIS):
            return self.unario()
        op = self.NIVEIS[n]
        esq = self.binario(n + 1)
        if op == "->":
            if self.ver() == "->":
                self.comer()
                return No("->", (esq, self.binario(n)))
            return esq
        while self.ver() == op:
            self.comer()
            esq = No(op, (esq, self.binario(n + 1)))
        return esq

    def unario(self) -> No:
        t = self.ver()
        if t == "~":
            self.comer()
            return No("~", (self.unario(),))
        if t == "(":
            self.comer()
            no = self.binario(0)
            self.comer(")")
            return no
        if t is not None and re.fullmatch(r"[a-z]\w*", t):
            self.comer()
            return No(None, nome=t)
        raise ValueError(f"Esperada uma proposição, encontrado {t!r}")

    def tudo(self) -> No:
        no = self.binario(0)
        if self.ver() is not None:
            raise ValueError(f"Sobrou {self.ver()!r} no fim da expressão")
        return no


def subformulas(no: No) -> list[No]:
    vistos, ordem = set(), []

    def visitar(n: No):
        for f in n.filhos:
            visitar(f)
        if n.nome is None and n not in vistos:
            vistos.add(n)
            ordem.append(n)

    visitar(no)
    return ordem


def variaveis(no: No) -> list[str]:
    if no.nome is not None:
        return [no.nome]
    out = []
    for f in no.filhos:
        for v in variaveis(f):
            if v not in out:
                out.append(v)
    return out


def tabela(expr: str):
    arv = Parser(tokens(expr)).tudo()
    vs = sorted(variaveis(arv))
    colunas = subformulas(arv)
    linhas = []
    for valores in itertools.product([True, False], repeat=len(vs)):
        v = dict(zip(vs, valores))
        linhas.append([v[x] for x in vs] + [c.avaliar(v) for c in colunas])
    resultado = [l[-1] for l in linhas]
    tipo = "tautologia" if all(resultado) else "contradição" if not any(resultado) else "contingência"
    return arv, vs, colunas, linhas, tipo


def markdown(expr: str) -> str:
    arv, vs, cols, linhas, tipo = tabela(expr)
    cab = vs + [c.texto() for c in cols]
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for l in linhas:
        out.append("| " + " | ".join("V" if x else "F" for x in l) + " |")
    out.append("")
    out.append(f"A proposição é uma **{tipo}**.")
    return "\n".join(out)


def latex(expr: str) -> str:
    arv, vs, cols, linhas, tipo = tabela(expr)
    cab = [f"${x}$" for x in vs] + [f"${c.latex()}$" for c in cols]
    spec = "c" * len(vs) + "|" + "c" * len(cols)
    out = [r"\begin{tabular}{" + spec + "}", r"\toprule", " & ".join(cab) + r" \\", r"\midrule"]
    for l in linhas:
        out.append(" & ".join(r"\textsf{V}" if x else r"\textsf{F}" for x in l) + r" \\")
    out += [r"\bottomrule", r"\end{tabular}", f"% {tipo}"]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="Gera a tabela-verdade de uma proposição.")
    ap.add_argument("expressao")
    ap.add_argument("--formato", choices=["markdown", "latex"], default="markdown")
    a = ap.parse_args()
    try:
        print(latex(a.expressao) if a.formato == "latex" else markdown(a.expressao))
    except ValueError as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
