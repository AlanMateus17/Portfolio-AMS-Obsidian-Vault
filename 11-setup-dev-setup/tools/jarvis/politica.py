#!/usr/bin/env python3
"""Política do Jarvis: o que cada comando de voz pode fazer sozinho e o que precisa do seu ok.

Quatro níveis, do mais livre ao mais travado:
    livre     executa na hora (acender luz, perguntar o consumo, trancar a porta)
    voz       pede "tem certeza?" e você confirma falando (desligar uma tomada comum)
    celular   só executa depois do toque no aviso do app do Home Assistant (destrancar, abrir janela)
    proibido  não executa por voz nunca (desarmar alarme, desligar câmera, apagar gravação)

Alguns mínimos são fixos no código e o arquivo não consegue afrouxar: destrancar porta nunca fica abaixo
de "celular", porque voz pode ser imitada, gravada ou gritada do lado de fora.

    python3 tools/jarvis/politica.py validar ~/.config/amtech/jarvis.toml
    python3 tools/jarvis/politica.py decidir ~/.config/amtech/jarvis.toml lock.unlock lock.porta_da_frente
    python3 tools/jarvis/politica.py expor   ~/.config/amtech/jarvis.toml   # o que marcar como exposto no Assist
    python3 tools/jarvis/politica.py ha-yaml ~/.config/amtech/jarvis.toml > automations_jarvis.yaml

Modelo: tools/jarvis/politica.example.toml.
"""
from __future__ import annotations

import argparse
import sys
import tomllib
from pathlib import Path

NIVEIS = ("livre", "voz", "celular", "proibido")
TIPOS = {"luz", "tomada", "geladeira", "porta", "janela", "portao", "cortina", "camera", "alarme", "sensor",
         "clima", "midia", "robo", "aspirador", "valvula"}

# Mínimos que nenhum arquivo afrouxa. Chave: (ação, tipo da entidade); "*" vale para qualquer tipo.
MINIMOS = {
    ("lock.unlock", "*"): "celular",
    ("lock.open", "*"): "celular",
    ("cover.open_cover", "janela"): "celular",
    ("cover.open_cover", "portao"): "celular",
    ("cover.open_cover", "porta"): "celular",
    ("alarm_control_panel.alarm_disarm", "*"): "proibido",
    ("camera.turn_off", "*"): "proibido",
    ("switch.turn_off", "camera"): "proibido",
    ("switch.turn_off", "geladeira"): "celular",
    ("switch.turn_off", "alarme"): "proibido",
    ("valve.open_valve", "*"): "voz",
    ("frigate.delete", "*"): "proibido",
}
# Sem regra que case, o padrão é pedir confirmação falada: o que não foi pensado não roda sozinho.
PADRAO = "voz"


def carregar(caminho: Path) -> dict:
    with open(caminho, "rb") as f:
        return tomllib.load(f)


def _minimo(acao: str, tipo: str) -> str:
    for chave in ((acao, tipo), (acao, "*")):
        if chave in MINIMOS:
            return MINIMOS[chave]
    return "livre"


def _max(a: str, b: str) -> str:
    return a if NIVEIS.index(a) >= NIVEIS.index(b) else b


def entidades(d: dict) -> dict[str, dict]:
    return {e["id"]: e for e in d.get("entidade", [])}


def validar(d: dict) -> list[str]:
    erros = []
    ents = entidades(d)
    if len(ents) != len(d.get("entidade", [])):
        erros.append("entidade repetida")
    for e in d.get("entidade", []):
        if "." not in e.get("id", ""):
            erros.append(f"id de entidade inválido: {e.get('id')!r} (use dominio.nome, ex.: light.sala)")
        if e.get("tipo") not in TIPOS:
            erros.append(f"{e.get('id')}: tipo inválido {e.get('tipo')!r} (use {', '.join(sorted(TIPOS))})")
        if not str(e.get("apelido", "")).strip():
            erros.append(f"{e.get('id')}: falta o apelido (o nome que você fala)")
        if e.get("tipo") == "geladeira" and not isinstance(e.get("religar_em_min"), int):
            erros.append(f"{e.get('id')}: geladeira precisa de religar_em_min (inteiro): ela nunca fica desligada esquecida")
        if isinstance(e.get("religar_em_min"), int) and not 1 <= e["religar_em_min"] <= 120:
            erros.append(f"{e.get('id')}: religar_em_min deve ficar entre 1 e 120")
    for r in d.get("regra", []):
        if r.get("nivel") not in NIVEIS:
            erros.append(f"regra {r.get('acao')}: nível inválido {r.get('nivel')!r} (use {', '.join(NIVEIS)})")
        if "." not in str(r.get("acao", "")):
            erros.append(f"regra com ação inválida: {r.get('acao')!r} (use dominio.servico, ex.: light.turn_on)")
        if r.get("entidade") and r["entidade"] not in ents:
            erros.append(f"regra {r.get('acao')}: entidade {r['entidade']} não está na lista")
    expostas = [e for e in d.get("entidade", []) if e.get("exposta", True)]
    limite = d.get("geral", {}).get("max_entidades_expostas", 25)
    if len(expostas) > limite:
        erros.append(f"{len(expostas)} entidades expostas ao Assist (limite {limite}): com muitas, o modelo esquece aparelhos e erra")
    return erros


def decidir(d: dict, acao: str, entidade: str) -> tuple[str, str]:
    """Devolve (nível, motivo). A primeira regra que casa vale, nunca abaixo do mínimo fixo."""
    e = entidades(d).get(entidade)
    if e is None:
        return "proibido", f"{entidade} não está na política: o Jarvis só mexe no que foi listado"
    if not e.get("exposta", True):
        return "proibido", f"{entidade} não está exposta ao Jarvis"
    tipo = e["tipo"]
    nivel, motivo = PADRAO, "sem regra para esta ação: pede confirmação falada"
    for r in d.get("regra", []):
        if r["acao"] != acao:
            continue
        if r.get("entidade") and r["entidade"] != entidade:
            continue
        if r.get("tipo") and r["tipo"] != tipo:
            continue
        nivel, motivo = r["nivel"], r.get("motivo", "regra do arquivo")
        break
    minimo = _minimo(acao, tipo)
    if NIVEIS.index(minimo) > NIVEIS.index(nivel):
        return minimo, f"mínimo fixo para {acao} em {tipo}: {minimo} (o arquivo pedia {nivel})"
    return nivel, motivo


def expor(d: dict) -> list[str]:
    return [f"{e['id']}  ({e['apelido']})" for e in d.get("entidade", []) if e.get("exposta", True)]


def ha_yaml(d: dict) -> str:
    """Automações do Home Assistant que religam sozinhas o que não pode ficar desligado."""
    notificar = d.get("geral", {}).get("notificar", "notify.notify")
    linhas = ["# Gerado por tools/jarvis/politica.py. Cole em automations.yaml (ou inclua o arquivo)."]
    for e in d.get("entidade", []):
        minutos = e.get("religar_em_min")
        if not isinstance(minutos, int):
            continue
        dominio = e["id"].split(".", 1)[0]
        slug = e["id"].replace(".", "_")
        linhas += [
            f"- id: jarvis_religar_{slug}",
            f'  alias: "Jarvis: religar {e["apelido"]} depois de {minutos} min"',
            "  mode: single",
            "  triggers:",
            "    - trigger: state",
            f"      entity_id: {e['id']}",
            '      to: "off"',
            "      for:",
            f"        minutes: {minutos}",
            "  actions:",
            f"    - action: {dominio}.turn_on",
            "      target:",
            f"        entity_id: {e['id']}",
            f"    - action: {notificar}",
            "      data:",
            f'        message: "{e["apelido"].capitalize()} religada automaticamente depois de {minutos} min desligada."',
        ]
    return "\n".join(linhas) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Política de risco dos comandos de voz")
    sub = ap.add_subparsers(dest="acao", required=True)
    for nome in ("validar", "expor", "ha-yaml"):
        sub.add_parser(nome).add_argument("arquivo", type=Path)
    dc = sub.add_parser("decidir")
    dc.add_argument("arquivo", type=Path)
    dc.add_argument("servico", help="ex.: lock.unlock")
    dc.add_argument("entidade", help="ex.: lock.porta_da_frente")
    a = ap.parse_args(argv)
    d = carregar(a.arquivo)
    erros = validar(d)
    if erros:
        for e in erros:
            print(f"ERRO: {e}", file=sys.stderr)
        return 1
    if a.acao == "validar":
        print(f"Política válida: {len(expor(d))} entidades expostas, {len(d.get('regra', []))} regras.")
    elif a.acao == "decidir":
        nivel, motivo = decidir(d, a.servico, a.entidade)
        print(f"{nivel}: {motivo}")
    elif a.acao == "expor":
        print("\n".join(expor(d)))
    else:
        sys.stdout.write(ha_yaml(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
