#!/usr/bin/env python3
"""Guarda de escopo: nenhum teste de segurança roda fora do que o cliente autorizou por escrito.

Testar sistema de terceiros sem autorização é crime (Lei 12.737/2012, art. 154-A do Código Penal).
Esta ferramenta é a trava: lê o escopo assinado (TOML) e só libera um alvo se

  1. a autorização estiver registrada (quem assinou, quando e o arquivo assinado existir);
  2. o momento estiver dentro da janela combinada;
  3. o alvo estiver na lista de alvos e fora da lista de exclusões (exclusão sempre vence).

    python tools/seguranca/escopo.py validar ~/clientes/loja/escopo.toml
    python tools/seguranca/escopo.py checar  ~/clientes/loja/escopo.toml app.loja.example
    python tools/seguranca/escopo.py rodar   ~/clientes/loja/escopo.toml app.loja.example -- nmap -sV app.loja.example

"rodar" só executa o comando se o alvo passar e grava cada execução em registro.jsonl, ao lado do
escopo: é o registro de atividades que entra no apêndice do relatório e que prova o que foi feito.
Modelo do escopo: infra/templates/seguranca/escopo.example.toml.
"""
from __future__ import annotations

import argparse
import datetime as dt
import ipaddress
import json
import shlex
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import urlsplit

CAMPOS = ("cliente", "contrato", "autorizacao", "janela", "alvos")


def carregar(caminho: Path) -> dict:
    with open(caminho, "rb") as f:
        d = tomllib.load(f)
    d["_pasta"] = str(Path(caminho).resolve().parent)
    return d


def _data(v) -> dt.datetime:
    if isinstance(v, dt.datetime):
        return v
    if isinstance(v, dt.date):
        return dt.datetime.combine(v, dt.time(), tzinfo=dt.timezone.utc)
    return dt.datetime.fromisoformat(str(v))


def validar(d: dict) -> list[str]:
    erros = [f"falta o campo '{c}'" for c in CAMPOS if c not in d]
    if erros:
        return erros
    aut = d["autorizacao"]
    for c in ("assinada_por", "assinada_em", "arquivo"):
        if not str(aut.get(c, "")).strip():
            erros.append(f"autorização sem '{c}': sem documento assinado não há teste")
    arq = str(aut.get("arquivo", "")).strip()
    if arq and not (Path(d.get("_pasta", ".")) / arq).expanduser().exists():
        erros.append(f"o arquivo da autorização assinada não existe: {arq}")
    jan = d["janela"]
    try:
        ini, fim = _data(jan["inicio"]), _data(jan["fim"])
        if ini.tzinfo is None or fim.tzinfo is None:
            erros.append("a janela precisa de fuso horário (ex.: 2027-03-10T09:00:00-03:00)")
        elif fim <= ini:
            erros.append("a janela termina antes de começar")
        elif aut.get("assinada_em") and _data(aut["assinada_em"]).date() > ini.date():
            erros.append("a autorização foi assinada depois do início da janela")
    except (KeyError, ValueError, TypeError) as e:
        erros.append(f"janela inválida: {e}")
    alvos = d["alvos"]
    if not any(alvos.get(k) for k in ("dominios", "ips", "urls")):
        erros.append("nenhum alvo listado")
    for grupo in (alvos, d.get("fora", {})):
        for rede in grupo.get("ips", []):
            try:
                ipaddress.ip_network(rede, strict=False)
            except ValueError:
                erros.append(f"IP ou faixa inválida: {rede}")
    return erros


def host_de(alvo: str) -> str:
    alvo = alvo.strip()
    if "://" in alvo:
        return (urlsplit(alvo).hostname or "").lower()
    if alvo.count(":") == 1:  # host:porta
        alvo = alvo.split(":", 1)[0]
    return alvo.split("/", 1)[0].lower().rstrip(".")


def _ip(h: str):
    try:
        return ipaddress.ip_address(h)
    except ValueError:
        return None


def _bate_dominio(host: str, padroes: list[str]) -> bool:
    for p in padroes:
        p = p.lower().rstrip(".")
        if p.startswith("*."):
            base = p[2:]
            if host.endswith("." + base):  # *.x.com vale para sub.x.com, não para x.com
                return True
        elif host == p:
            return True
    return False


def _bate_ip(ip, redes: list[str]) -> bool:
    return any(ip in ipaddress.ip_network(r, strict=False) for r in redes)


def checar(d: dict, alvo: str, agora: dt.datetime | None = None) -> tuple[bool, str]:
    erros = validar(d)
    if erros:
        return False, "escopo inválido: " + "; ".join(erros)
    agora = agora or dt.datetime.now(dt.timezone.utc)
    ini, fim = _data(d["janela"]["inicio"]), _data(d["janela"]["fim"])
    if not ini <= agora <= fim:
        return False, f"fora da janela autorizada ({ini.isoformat()} a {fim.isoformat()})"
    host = host_de(alvo)
    if not host:
        return False, f"não consegui ler o host de {alvo!r}"
    fora, alvos = d.get("fora", {}), d["alvos"]
    ip = _ip(host)
    if "://" in alvo and any(alvo.startswith(u) for u in fora.get("urls", [])):
        return False, f"{alvo} está na lista de exclusões"
    if ip is not None:
        if _bate_ip(ip, fora.get("ips", [])):
            return False, f"{host} está numa faixa excluída"
        if _bate_ip(ip, alvos.get("ips", [])):
            return True, f"{host} autorizado (faixa de IP do contrato {d['contrato']})"
        return False, f"{host} não está nas faixas autorizadas"
    if _bate_dominio(host, fora.get("dominios", [])):
        return False, f"{host} está na lista de exclusões"
    if _bate_dominio(host, alvos.get("dominios", [])):
        return True, f"{host} autorizado (domínio do contrato {d['contrato']})"
    if "://" in alvo and any(alvo.startswith(u) for u in alvos.get("urls", [])):
        return True, f"{alvo} autorizado (URL do contrato {d['contrato']})"
    return False, f"{host} não está no escopo assinado"


def registrar(pasta: Path, alvo: str, comando: list[str], codigo: int, agora: dt.datetime) -> Path:
    reg = pasta / "registro.jsonl"
    linha = {"quando": agora.isoformat(timespec="seconds"), "alvo": alvo, "comando": shlex.join(comando), "codigo_saida": codigo}
    with open(reg, "a", encoding="utf-8") as f:
        f.write(json.dumps(linha, ensure_ascii=False) + "\n")
    return reg


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Guarda de escopo do pentest")
    sub = ap.add_subparsers(dest="acao", required=True)
    v = sub.add_parser("validar", help="confere se o escopo está completo")
    v.add_argument("escopo", type=Path)
    c = sub.add_parser("checar", help="diz se um alvo pode ser testado agora")
    c.add_argument("escopo", type=Path)
    c.add_argument("alvo")
    r = sub.add_parser("rodar", help="roda o comando só se o alvo estiver no escopo, e registra")
    r.add_argument("escopo", type=Path)
    r.add_argument("alvo")
    r.add_argument("comando", nargs=argparse.REMAINDER, help="depois de --")
    a = ap.parse_args(argv)

    d = carregar(a.escopo)
    if a.acao == "validar":
        erros = validar(d)
        for e in erros:
            print(f"ERRO: {e}", file=sys.stderr)
        if not erros:
            print(f"Escopo válido: {d['cliente']} · contrato {d['contrato']}")
        return 1 if erros else 0

    ok, motivo = checar(d, a.alvo)
    print(("LIBERADO: " if ok else "BLOQUEADO: ") + motivo, file=sys.stdout if ok else sys.stderr)
    if a.acao == "checar" or not ok:
        return 0 if ok else 1

    cmd = a.comando[1:] if a.comando and a.comando[0] == "--" else a.comando
    if not cmd:
        print("ERRO: diga o comando depois de --", file=sys.stderr)
        return 2
    if not any(host_de(a.alvo) in x.lower() for x in cmd):
        print(f"AVISO: o comando não cita {a.alvo}; confira se ele não aponta para outro alvo.", file=sys.stderr)
    codigo = subprocess.run(cmd, check=False).returncode  # sem shell: o comando roda como foi escrito
    reg = registrar(Path(d["_pasta"]), a.alvo, cmd, codigo, dt.datetime.now(dt.timezone.utc))
    print(f"Registrado em {reg}")
    return codigo


if __name__ == "__main__":
    sys.exit(main())
