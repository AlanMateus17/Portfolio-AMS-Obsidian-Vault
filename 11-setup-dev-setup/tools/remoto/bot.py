#!/usr/bin/env python3
"""Bot do Telegram do setup: responde só ao SEU chat e só a comandos fixos. Nada de comando livre.

Configuração (fora do repositório, arquivo com permissão 600):
    ~/.config/amtech/telegram.env
        TELEGRAM_TOKEN=...      # do @BotFather; guarde também no KeePassXC
        TELEGRAM_CHAT_ID=...    # o seu id (o bot mostra no primeiro /start)

Uso:
    python tools/remoto/bot.py                 # fica ouvindo (rode como serviço, ver o roteiro)
    python tools/remoto/bot.py --avisar "texto"  # outros scripts mandam aviso para o seu celular

Comandos: /ajuda /status /resumo /radar /pedir /fila. Nunca recebe senha, nunca executa texto vindo da conversa
como comando: /pedir só guarda o pedido na fila (tools/remoto/fila.py), que trabalha numa worktree separada.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
ENV = Path.home() / ".config" / "amtech" / "telegram.env"
COMANDOS = {
    "/status": ["bash", str(RAIZ / "scripts" / "wsl" / "verificar.sh")],
    "/resumo": ["bash", str(RAIZ / "scripts" / "wsl" / "resumo-manha.sh"), "--texto"],
}
AJUDA = ("Comandos:\n/pedir TEXTO – manda um pedido para a fila (use @repo no começo para outro repositório)\n"
         "/fila – como estão os pedidos\n/status – o setup está ok?\n/resumo – resumo do dia\n"
         "/radar – últimas oportunidades aprovadas\n/ajuda – esta lista\n\nNunca mande senha por aqui.")


def carregar_env(caminho: Path = ENV) -> dict:
    cfg = {}
    if caminho.exists():
        if caminho.stat().st_mode & 0o077:
            raise SystemExit(f"{caminho} está legível por outros usuários. Rode: chmod 600 {caminho}")
        for linha in caminho.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                cfg[k.strip()] = v.strip()
    cfg.update({k: v for k, v in os.environ.items() if k.startswith("TELEGRAM_")})
    return cfg


def api(token: str, metodo: str, dados: dict | None = None) -> dict:
    url = f"https://api.telegram.org/bot{token}/{metodo}"
    corpo = urllib.parse.urlencode(dados or {}).encode()
    with urllib.request.urlopen(urllib.request.Request(url, data=corpo), timeout=70) as r:
        return json.loads(r.read().decode())


def responder(texto: str, raiz: Path = RAIZ) -> str:
    cmd = texto.strip().split()[0].split("@")[0].lower() if texto.strip() else ""
    if cmd in ("/start", "/ajuda", "/help"):
        return AJUDA
    if cmd == "/radar":
        r = Path.home() / "radar.md"
        return r.read_text(encoding="utf-8")[:3500] if r.exists() else "Ainda não há radar.md. Rode o radar primeiro."
    if cmd == "/pedir":
        resto = texto.strip().split(None, 1)
        if len(resto) < 2:
            return "Escreva o pedido depois do /pedir. Ex.: /pedir criar a página de vendas do curso de lógica"
        sys.path.insert(0, str(raiz / "tools" / "remoto"))
        import fila  # noqa: PLC0415
        item = fila.adicionar(resto[1])
        return f"Na fila: {item['id']} ({item['repo']}). Aviso aqui quando terminar."
    if cmd == "/fila":
        try:
            out = subprocess.run([sys.executable, str(raiz / "tools" / "remoto" / "fila.py"), "listar"],
                                 capture_output=True, text=True, timeout=60).stdout
        except Exception as e:  # noqa: BLE001
            return f"Falhou: {e}"
        return (out.strip() or "Fila vazia.")[-3500:]
    if cmd in COMANDOS:
        try:
            out = subprocess.run(COMANDOS[cmd], capture_output=True, text=True, timeout=120).stdout
        except Exception as e:  # noqa: BLE001
            return f"Falhou: {e}"
        return (out.strip() or "(sem saída)")[-3500:]
    return "Não conheço esse comando. /ajuda mostra a lista."


def permitido(msg: dict, chat_id: str) -> bool:
    return str(msg.get("chat", {}).get("id")) == str(chat_id)


def ouvir(cfg: dict) -> None:
    token, chat = cfg["TELEGRAM_TOKEN"], cfg.get("TELEGRAM_CHAT_ID", "")
    desloc = 0
    while True:
        try:
            r = api(token, "getUpdates", {"timeout": 60, "offset": desloc})
        except Exception:  # noqa: BLE001
            time.sleep(10)
            continue
        for up in r.get("result", []):
            desloc = up["update_id"] + 1
            msg = up.get("message") or {}
            if not chat:
                api(token, "sendMessage", {"chat_id": msg["chat"]["id"], "text": f"Seu chat id é {msg['chat']['id']}. Coloque em TELEGRAM_CHAT_ID."})
                continue
            if not permitido(msg, chat):
                continue  # ignora qualquer outra pessoa, sem responder
            api(token, "sendMessage", {"chat_id": chat, "text": responder(msg.get("text", ""))})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--avisar")
    a = ap.parse_args()
    cfg = carregar_env()
    if "TELEGRAM_TOKEN" not in cfg:
        print(f"Configure {ENV} (veja o topo deste arquivo).", file=sys.stderr)
        return 1
    if a.avisar:
        if not cfg.get("TELEGRAM_CHAT_ID"):
            print("Falta TELEGRAM_CHAT_ID.", file=sys.stderr)
            return 1
        api(cfg["TELEGRAM_TOKEN"], "sendMessage", {"chat_id": cfg["TELEGRAM_CHAT_ID"], "text": a.avisar[:4000]})
        return 0
    ouvir(cfg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
