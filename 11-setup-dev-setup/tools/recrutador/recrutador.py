#!/usr/bin/env python3
"""Recrutador do setup: simulações de entrevista nacionais e internacionais, com nota, histórico e o próximo treino.

O setup não finge ser a empresa: ele monta o entrevistador a partir de formatos públicos (data/recrutador/formatos.json),
das suas histórias reais (no vault) e da vaga que você colar. A entrevista acontece no Claude: no app, com o modo de voz
para as de inglês, ou no terminal. O que fica no setup é a nota, a evolução e o que treinar.

    python3 tools/recrutador/recrutador.py formatos                     # os formatos e em que trimestre entram
    python3 tools/recrutador/recrutador.py semana                       # qual simulação fazer agora (trimestre + ponto fraco)
    python3 tools/recrutador/recrutador.py entrevista br-triagem        # imprime o entrevistador para colar no Claude (zero token)
    python3 tools/recrutador/recrutador.py entrevista amazon-lp --empresa "Amazon" --vaga ~/vaga.txt
    python3 tools/recrutador/recrutador.py entrevista bigtech-coding --claude   # abre a entrevista no Claude Code do terminal
    python3 tools/recrutador/recrutador.py registrar br-triagem 3 --melhorar "resumo longo; pretensão sem número"
    python3 tools/recrutador/recrutador.py progresso                    # nota por formato e o que já está pronto
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import nucleo as nuc  # noqa: E402

FORMATOS = RAIZ / "data" / "recrutador" / "formatos.json"
TIPO = "entrevista.simulada"
INICIO_EIXO = date(2026, 11, 1)  # trimestre 1 do plano-eixo: nov/2026 a jan/2027


def dados() -> dict:
    return json.loads(FORMATOS.read_text(encoding="utf-8"))


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def pasta_vault() -> Path:
    return vault() / "07-estudo-e-carreira" / "recrutador"


def trimestre(hoje: date) -> int:
    meses = (hoje.year - INICIO_EIXO.year) * 12 + hoje.month - INICIO_EIXO.month
    return max(1, min(4, meses // 3 + 1))


def formato(d: dict, fid: str) -> dict:
    for f in d["formatos"]:
        if f["id"] == fid:
            return f
    raise KeyError(f"Formato desconhecido: {fid}. Veja: just recrutador formatos")


def validar(d: dict) -> list[str]:
    erros, ids = [], set()
    for f in d["formatos"]:
        if f["id"] in ids:
            erros.append(f"id repetido: {f['id']}")
        ids.add(f["id"])
        if sum(e["minutos"] for e in f["etapas"]) != f["minutos"]:
            erros.append(f"{f['id']}: as etapas não somam {f['minutos']} min")
        if f["idioma"] not in ("português", "inglês") or f["mercado"] not in ("nacional", "internacional"):
            erros.append(f"{f['id']}: idioma ou mercado inválido")
        if not 1 <= f["trimestre"] <= 4:
            erros.append(f"{f['id']}: trimestre fora de 1 a 4")
    return erros


def historias() -> str:
    """As suas histórias reais (STAR), escritas por você no vault. Sem elas, o entrevistador não inventa nada."""
    arq = pasta_vault() / "historias.md"
    return arq.read_text(encoding="utf-8").strip() if arq.exists() else ""


def pacote(d: dict, f: dict, empresa: str = "", vaga: str = "", minhas_historias: str = "") -> str:
    """O prompt do entrevistador. Só imprime: colar no Claude não gasta token do setup."""
    en = f["idioma"] == "inglês"
    etapas = "\n".join(f"{i}. {e['nome']} ({e['minutos']} min): {e['avalia']}" for i, e in enumerate(f["etapas"], 1))
    escala = "\n".join(f"{k} = {v}" for k, v in d["escala"].items())
    partes = [
        f"Você vai conduzir uma simulação de entrevista: {f['nome']}.",
        f"Estilo: {f['estilo']}." + (f" Empresa simulada: {empresa}. Use só o que é público sobre o processo dela; se não souber, diga que está usando o formato genérico." if empresa else ""),
        f"Idioma da entrevista: {f['idioma']}. Duração total: {f['minutos']} minutos.",
        "\nEtapas, nesta ordem:\n" + etapas,
        "\nRegras:\n" + "\n".join(f"- {r}" for r in d["regras_do_entrevistador"]),
    ]
    if vaga:
        partes.append("\nVaga para a qual o candidato está se preparando (use os requisitos para escolher as perguntas):\n" + vaga.strip())
    if minhas_historias:
        partes.append("\nHistórias reais do candidato, escritas por ele (use para aprofundar, não para responder por ele):\n" + minhas_historias)
    partes.append(
        "\nAo final, avalie em português, neste formato:\n"
        f"NOTA GERAL: 1 a 4\n{escala}\n"
        + "\n".join(f"- {c}: nota de 1 a 4 e uma frase com a evidência" for c in f["competencias"])
        + "\nO QUE UM ENTREVISTADOR EXIGENTE ANOTARIA: 3 pontos concretos, citando o que o candidato disse"
        + "\nREFAZER: a pergunta em que ele foi pior, para responder de novo agora"
        + ("\nINGLÊS: 3 frases que ele disse e a versão natural de cada uma" if en else "")
        + f"\nREGISTRO: just recrutador registrar {f['id']} NOTA --melhorar \"ponto 1; ponto 2\""
    )
    partes.append("\nComece agora: apresente-se como entrevistador em uma frase e faça a primeira pergunta.")
    return "\n".join(partes)


def registrar(con, fid: str, nota: int, melhorar: str = "", empresa: str = "", hoje: date | None = None) -> int:
    if not 1 <= nota <= 4:
        raise ValueError("A nota vai de 1 a 4")
    hoje = hoje or date.today()
    eid = nuc.evento(con, TIPO, {"formato": fid, "nota": nota, "melhorar": melhorar, "empresa": empresa, "data": hoje.isoformat()}, fonte="recrutador")
    if melhorar:
        nuc.lembrar(con, f"Entrevista {fid} ({hoje.isoformat()}), nota {nota}: melhorar {melhorar}", tipo="licao",
                    titulo=f"Entrevista {fid}", origem="recrutador", tags="entrevista")
    return eid


def historico(con) -> dict[str, list[dict]]:
    h: dict[str, list[dict]] = {}
    for (dj,) in con.execute("SELECT dados FROM eventos WHERE tipo = ? ORDER BY quando, id", (TIPO,)):
        x = json.loads(dj)
        h.setdefault(x["formato"], []).append(x)
    return h


def pronto(notas: list[int]) -> bool:
    return len(notas) >= 3 and all(n >= 3 for n in notas[-3:])


def sugerir(d: dict, h: dict[str, list[dict]], hoje: date) -> dict:
    """O próximo treino: dos formatos já liberados pelo trimestre, o que não está pronto e tem a pior média recente;
    empate vai para o que ficou mais tempo sem treino, e nunca treinado ganha de tudo."""
    t = trimestre(hoje)
    liberados = [f for f in d["formatos"] if f["trimestre"] <= t]
    def chave(f):
        notas = [x["nota"] for x in h.get(f["id"], [])]
        if not notas:
            return (0, 0, "")
        ultima = h[f["id"]][-1]["data"]
        return (1 if not pronto(notas) else 2, sum(notas[-3:]) / len(notas[-3:]), ultima)
    return sorted(liberados, key=chave)[0]


def tabela(d: dict, h: dict[str, list[dict]], hoje: date) -> str:
    t = trimestre(hoje)
    linhas = [f"Trimestre {t} do eixo · {d['pronto']}", "", f"{'formato':<18}{'tri':>4}{'feitas':>8}  últimas notas  situação"]
    for f in d["formatos"]:
        notas = [x["nota"] for x in h.get(f["id"], [])]
        if f["trimestre"] > t:
            sit = f"entra no trimestre {f['trimestre']}"
        elif pronto(notas):
            sit = "PRONTO"
        elif notas:
            sit = "treinando"
        else:
            sit = "liberado, nunca feito"
        linhas.append(f"{f['id']:<18}{f['trimestre']:>4}{len(notas):>8}  {' '.join(map(str, notas[-5:])) or '-':<13}  {sit}")
    return "\n".join(linhas)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Simulações de entrevista do setup")
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("formatos")
    s.add_parser("semana")
    s.add_parser("progresso")
    s.add_parser("validar")
    e = s.add_parser("entrevista")
    e.add_argument("formato")
    e.add_argument("--empresa", default="")
    e.add_argument("--vaga", help="arquivo .txt com o texto da vaga")
    e.add_argument("--claude", action="store_true", help="abre a entrevista no Claude Code do terminal")
    r = s.add_parser("registrar")
    r.add_argument("formato")
    r.add_argument("nota", type=int)
    r.add_argument("--melhorar", default="")
    r.add_argument("--empresa", default="")
    a = ap.parse_args(argv)
    d = dados()
    hoje = date.today()
    try:
        if a.cmd == "validar":
            erros = validar(d)
            print("\n".join(erros) or f"{len(d['formatos'])} formatos válidos")
            return 1 if erros else 0
        if a.cmd == "formatos":
            for f in d["formatos"]:
                print(f"{f['id']:<18} tri {f['trimestre']} · {f['mercado']:<13} · {f['idioma']:<9} · {f['minutos']:>2} min · {f['nome']}")
            return 0
        if a.cmd == "entrevista":
            f = formato(d, a.formato)
            vaga = Path(a.vaga).expanduser().read_text(encoding="utf-8") if a.vaga else ""
            texto = pacote(d, f, a.empresa, vaga, historias())
            if a.claude:
                return subprocess.call(["claude", texto])
            print(texto)
            dica = "no app do Claude, com o modo de voz ligado" if f["idioma"] == "inglês" else "no app do Claude ou com --claude no terminal"
            print(f"\n--- Copie tudo acima e cole {dica}. Ao terminar, diga 'fim da entrevista'.", file=sys.stderr)
            if not historias():
                print(f"--- Dica: escreva as suas histórias reais em {pasta_vault() / 'historias.md'} (modelo em docs/recrutador/historias-modelo.md).", file=sys.stderr)
            return 0
        con = nuc.abrir()
        if a.cmd == "registrar":
            formato(d, a.formato)
            registrar(con, a.formato, a.nota, a.melhorar, a.empresa, hoje)
            notas = [x["nota"] for x in historico(con)[a.formato]]
            print(f"Registrado: {a.formato} nota {a.nota}. Últimas: {' '.join(map(str, notas[-5:]))}" + (" · PRONTO" if pronto(notas) else ""))
        elif a.cmd == "progresso":
            print(tabela(d, historico(con), hoje))
        elif a.cmd == "semana":
            f = sugerir(d, historico(con), hoje)
            print(f"Treino desta semana: {f['nome']} ({f['minutos']} min, {f['idioma']})\n  just recrutador entrevista {f['id']}")
    except (KeyError, ValueError, FileNotFoundError) as erro:
        print(erro, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
