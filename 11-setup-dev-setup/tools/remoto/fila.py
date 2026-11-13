#!/usr/bin/env python3
"""Fila de pedidos do celular: cada pedido vira um ramo com as mudanças, feito pela melhor IA disponível.

    python3 tools/remoto/fila.py adicionar "criar a página de vendas do curso de lógica"
    python3 tools/remoto/fila.py adicionar "@catalogo-html corrigir o menu no celular"   # outro repo de ~/dev
    python3 tools/remoto/fila.py listar
    python3 tools/remoto/fila.py trabalhar --uma        # processa um pedido e sai
    python3 tools/remoto/fila.py trabalhar              # fica rodando (serviço amtech-fila)

Para cada pedido:
  1. O motor de decisão (tools/motor) desce a escada. Degrau 5 (aprovar, pagar, publicar) volta para você;
     degrau 1 (já existe) responde com o que já está pronto. Só 2, 3 e 4 viram trabalho.
  2. Abre uma worktree separada (~/dev/.fila/ID, ramo fila/ID). Nada mexe na sua pasta de trabalho.
  3. Tenta, nesta ordem: Claude Code (assinatura) → aider com a cota grátis (LiteLLM, ou Gemini direto)
     → aider com o Ollama local (qwen2.5-coder:7b, direto, sem Docker).
     Dado sensível vai direto para o local. Quando o Claude diz que o limite acabou, ele fica de fora por 5 h.
  4. Faz commit no ramo, abre PR em rascunho se o gh estiver logado e avisa no Telegram. Nunca faz merge.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DEV = Path(os.environ.get("AMTECH_DEV", Path.home() / "dev"))
DIR = Path(os.environ.get("FILA_DIR", Path.home() / ".local" / "share" / "amtech" / "fila"))
ESTADO = DIR / "estado.json"
LITELLM_ENV = RAIZ / "infra" / "ia" / ".env"
LITELLM_URL = os.environ.get("LITELLM_URL", "http://localhost:4000")
PAUSA_CLAUDE = timedelta(hours=5)
LIMITE_MIN = int(os.environ.get("FILA_TIMEOUT_MIN", "40"))
MODELO_LOCAL = os.environ.get("FILA_MODELO_LOCAL", "qwen2.5-coder:7b")
SINAIS_LIMITE = ("usage limit", "rate limit", "limit reached", "limite de uso", "out of credits",
                 "credit balance", "quota", "/upgrade", "resets at", "429")


# ---------- partes puras (testadas) ----------

def separar_repo(texto: str) -> tuple[str, str]:
    """'@catalogo-html corrigir X' -> ('catalogo-html', 'corrigir X'); sem @ -> ('dev-setup', texto)."""
    m = re.match(r"\s*@([A-Za-z0-9._-]+)\s+(.*)", texto, re.S)
    return (m.group(1), m.group(2).strip()) if m else ("dev-setup", texto.strip())


def motores(sensivel: bool, claude_pausado: bool, tem_claude: bool) -> list[str]:
    """Ordem de tentativa. Sensível nunca sai da máquina."""
    if sensivel:
        return ["local"]
    ordem = [] if (claude_pausado or not tem_claude) else ["claude"]
    return ordem + ["gratis", "local"]


def bateu_limite(saida: str, codigo: int) -> bool:
    s = saida.lower()
    return codigo != 0 and any(x in s for x in SINAIS_LIMITE)


def montar_prompt(pedido: str, decisao: dict) -> str:
    f = decisao.get("formulario", {})
    linhas = [
        f"Pedido do Alan (feito pelo celular): {pedido}",
        "",
        "Você está numa worktree separada, num ramo só deste pedido. Faça a mudança completa nos arquivos.",
        "Regras: siga o CLAUDE.md e as regras do repositório; não publique, não pague, não envie nada;",
        "não mexa em segredos; se faltar informação, assuma o padrão mais seguro e anote a suposição",
        "num arquivo FILA-NOTAS.md na raiz.",
    ]
    if f.get("ENTREGÁVEL"):
        linhas.append(f"Entregável: {f['ENTREGÁVEL']}")
    if f.get("PRONTO QUANDO"):
        linhas.append(f"Pronto quando: {f['PRONTO QUANDO']}")
    for r in f.get("RESTRIÇÕES", []):
        linhas.append(f"Restrição: {r}")
    return "\n".join(linhas)


def ler_env(caminho: Path) -> dict:
    cfg = {}
    if caminho.exists():
        for linha in caminho.read_text(encoding="utf-8").splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                cfg[k.strip()] = v.strip().strip('"')
    return cfg


# ---------- armazenamento ----------

def _salvar(item: dict) -> None:
    DIR.mkdir(parents=True, exist_ok=True)
    (DIR / f"{item['id']}.json").write_text(json.dumps(item, ensure_ascii=False, indent=1), encoding="utf-8")


def itens() -> list[dict]:
    if not DIR.exists():
        return []
    return sorted((json.loads(p.read_text(encoding="utf-8")) for p in DIR.glob("2*.json")), key=lambda i: i["id"])


def adicionar(texto: str) -> dict:
    repo, pedido = separar_repo(texto)
    if not pedido:
        raise ValueError("pedido vazio")
    item = {"id": datetime.now().strftime("%Y%m%d-%H%M%S"), "repo": repo, "pedido": pedido,
            "status": "pendente", "criado": datetime.now().isoformat(timespec="seconds"), "log": []}
    _salvar(item)
    return item


def estado() -> dict:
    return json.loads(ESTADO.read_text(encoding="utf-8")) if ESTADO.exists() else {}


def pausar_claude() -> None:
    e = estado()
    e["claude_pausa_ate"] = (datetime.now() + PAUSA_CLAUDE).isoformat(timespec="seconds")
    DIR.mkdir(parents=True, exist_ok=True)
    ESTADO.write_text(json.dumps(e), encoding="utf-8")


def claude_pausado() -> bool:
    ate = estado().get("claude_pausa_ate")
    return bool(ate) and datetime.fromisoformat(ate) > datetime.now()


# ---------- execução ----------

def avisar(texto: str) -> None:
    subprocess.run([sys.executable, str(RAIZ / "tools" / "remoto" / "bot.py"), "--avisar", texto[:3900]],
                   capture_output=True, timeout=60, check=False)


def sh(cmd: list[str], cwd: Path | None = None, timeout: int = 600, env: dict | None = None) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout, env=env)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, f"tempo esgotado ({timeout}s)"
    except FileNotFoundError as e:
        return 127, str(e)


def decidir(pedido: str) -> dict:
    cod, out = sh([sys.executable, str(RAIZ / "tools" / "motor" / "motor.py"), "decidir", pedido, "--json"], timeout=60)
    try:
        return json.loads(out[out.index("{"):]) if cod == 0 else {"degrau": 4, "sensivel": []}
    except ValueError:
        return {"degrau": 4, "sensivel": []}


def litellm_no_ar() -> bool:
    return sh(["curl", "-fsS", "-m", "3", f"{LITELLM_URL}/health/liveliness"], timeout=10)[0] == 0


def comando_aider(nome: str, prompt: str, cfg: dict, litellm: bool) -> list[str] | None:
    """Monta o aider para o motor. 'local' fala direto com o Ollama (não depende do Docker);
    'gratis' usa o LiteLLM quando está no ar e, sem ele, a chave grátis do Gemini direto. None = indisponível."""
    base = ["aider", "--yes-always", "--no-check-update", "--no-show-model-warnings", "--no-gitignore", "--message", prompt]
    if nome == "local":
        return ["aider", "--model", f"ollama_chat/{MODELO_LOCAL}"] + base[1:]
    if litellm and cfg.get("LITELLM_MASTER_KEY"):
        return ["aider", "--model", "openai/gratis", "--openai-api-base", LITELLM_URL,
                "--openai-api-key", cfg["LITELLM_MASTER_KEY"]] + base[1:]
    if cfg.get("GEMINI_API_KEY"):
        return ["aider", "--model", "gemini/gemini-2.5-flash"] + base[1:]
    return None


def rodar_motor(nome: str, prompt: str, pasta: Path) -> tuple[int, str]:
    seg = LIMITE_MIN * 60
    if nome == "claude":
        return sh(["claude", "-p", prompt, "--permission-mode", "acceptEdits"], cwd=pasta, timeout=seg)
    cfg = {**ler_env(LITELLM_ENV), **{k: v for k, v in os.environ.items() if k.endswith("_KEY")}}
    cmd = comando_aider(nome, prompt, cfg, litellm_no_ar() if nome == "gratis" else False)
    if cmd is None:
        return 127, f"motor {nome} sem configuração (LiteLLM fora do ar e sem GEMINI_API_KEY)"
    env = {**os.environ, "OLLAMA_API_BASE": os.environ.get("OLLAMA_API_BASE", "http://localhost:11434")}
    if cfg.get("GEMINI_API_KEY"):
        env["GEMINI_API_KEY"] = cfg["GEMINI_API_KEY"]
    return sh(cmd, cwd=pasta, timeout=seg, env=env)


def processar(item: dict) -> dict:
    item["status"] = "trabalhando"
    _salvar(item)
    d = decidir(item["pedido"])
    item["degrau"], item["sensivel"] = d.get("degrau"), d.get("sensivel", [])
    if d.get("degrau") == 5:
        item["status"] = "precisa-de-voce"
        item["log"].append(d.get("motivo", "portão humano"))
        _salvar(item)
        avisar(f"Pedido {item['id']} precisa de você (aprovar, pagar ou publicar): {item['pedido']}")
        return item
    if d.get("degrau") == 1:
        item["status"] = "ja-existe"
        prontos = "\n".join(f"- {p}" for p in d.get("pronto_no_setup", [])) or d.get("destino", "")
        item["log"].append(prontos)
        _salvar(item)
        avisar(f"Pedido {item['id']}: já existe no setup.\n{prontos}")
        return item

    repo = DEV / item["repo"]
    if not (repo / ".git").exists():
        item["status"] = "erro"
        item["log"].append(f"repositório {repo} não encontrado")
        _salvar(item)
        avisar(f"Pedido {item['id']}: não achei {repo}.")
        return item
    ramo = f"fila/{item['id']}"
    pasta = DEV / ".fila" / item["id"]
    pasta.parent.mkdir(parents=True, exist_ok=True)
    cod, out = sh(["git", "worktree", "add", "-b", ramo, str(pasta)], cwd=repo, timeout=120)
    if cod != 0:
        item["status"] = "erro"
        item["log"].append(out[-800:])
        _salvar(item)
        return item

    prompt = montar_prompt(item["pedido"], d)
    usado = None
    for nome in motores(bool(item["sensivel"]), claude_pausado(), shutil.which("claude") is not None):
        if nome != "claude" and not shutil.which("aider"):
            item["log"].append("aider ausente: rode just ligar")
            continue
        cod, out = rodar_motor(nome, prompt, pasta)
        item["log"].append(f"[{nome}] código {cod}: {out[-600:]}")
        if nome == "claude" and bateu_limite(out, cod):
            pausar_claude()
            avisar("Limite do Claude atingido. A fila segue com a cota grátis e o modelo local pelas próximas 5 h.")
            continue
        if cod == 0:
            usado = nome
            break

    sh(["git", "add", "-A"], cwd=pasta)
    sh(["git", "commit", "-m", f"fila: {item['pedido'][:60]}\n\nPedido {item['id']} feito por {usado or 'nenhum motor'}."],
       cwd=pasta)
    _, base = sh(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo)
    _, stat = sh(["git", "diff", "--stat", f"{base.strip()}...{ramo}"], cwd=repo)
    item["motor"] = usado
    item["ramo"] = ramo
    if not usado or not stat.strip():
        item["status"] = "sem-mudanca" if usado else "falhou"
        _salvar(item)
        avisar(f"Pedido {item['id']} {'não gerou mudança' if usado else 'falhou em todos os motores'}: {item['pedido']}\n"
               f"Detalhes: just fila")
        return item

    pr = ""
    if shutil.which("gh") and sh(["gh", "auth", "status"])[0] == 0:
        if sh(["git", "push", "-u", "origin", ramo], cwd=pasta, timeout=300)[0] == 0:
            cod, out = sh(["gh", "pr", "create", "--draft", "--head", ramo, "--title", f"fila: {item['pedido'][:60]}",
                           "--body", f"Pedido feito pelo celular ({item['id']}), motor: {usado}.\n\n{item['pedido']}"],
                          cwd=pasta, timeout=120)
            pr = out.strip().splitlines()[-1] if cod == 0 and out.strip() else ""
    item["pr"] = pr
    item["status"] = "pronto"
    _salvar(item)
    avisar(f"Pedido {item['id']} pronto ({usado}).\n{stat.strip()[-1200:]}\n{pr or 'Ramo ' + ramo + ' no notebook.'}")
    return item


def trabalhar(uma: bool) -> int:
    while True:
        pend = [i for i in itens() if i["status"] == "pendente"]
        if pend:
            processar(pend[0])
        if uma:
            return 0
        time.sleep(30 if pend else 60)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("adicionar")
    a.add_argument("texto", nargs="+")
    sub.add_parser("listar")
    t = sub.add_parser("trabalhar")
    t.add_argument("--uma", action="store_true")
    args = ap.parse_args()
    if args.cmd == "adicionar":
        i = adicionar(" ".join(args.texto))
        print(f"Na fila: {i['id']} ({i['repo']})")
    elif args.cmd == "listar":
        for i in itens()[-15:]:
            extra = i.get("pr") or i.get("ramo") or ""
            print(f"{i['id']}  {i['status']:<15} {i.get('motor') or '-':<7} {i['repo']:<14} {i['pedido'][:50]}  {extra}")
        print(f"Claude {'em pausa (limite)' if claude_pausado() else 'disponível'} para a fila.")
    else:
        return trabalhar(args.uma)
    return 0


if __name__ == "__main__":
    sys.exit(main())
