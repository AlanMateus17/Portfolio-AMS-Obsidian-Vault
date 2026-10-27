#!/usr/bin/env python3
"""Pipeline de conteúdo: o que você grava ou escreve vira peças prontas para aprovar.

Você coloca um arquivo numa pasta de entrada; o pipeline transcreve (se for áudio ou vídeo),
pede ao Claude as peças de cada rede seguindo o seu guia de marca e deixa tudo numa pasta da
fila de aprovação, com aviso no Telegram. Nada é publicado sozinho.

    ~/AMtech/entrada/aulas/aula-03-variaveis.mp4
    ~/AMtech/entrada/capitulos/cap01-proposicao.md
    ~/AMtech/entrada/reparos/notebook-dell-tela.txt
    ~/AMtech/entrada/decisoes/planejador-outubro.md
    ~/AMtech/entrada/ideias/ideia-curso-excel.txt
        ↓
    ~/AMtech/fila/20261021-1430-aula-03-variaveis/   (peças em .md + pecas.json + status.json)

Uso:
    python3 tools/conteudo/processar.py --uma-vez            # processa o que houver e sai (o timer chama assim)
    python3 tools/conteudo/processar.py --uma-vez --simular  # sem API: gera peças de teste para conferir o caminho

Configuração em ~/.config/amtech/conteudo.env (veja tools/conteudo/conteudo.env.example).
Só usa a biblioteca padrão do Python.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Callable

RAIZ_REPO = Path(__file__).resolve().parents[2]
CONFIG_PADRAO = Path.home() / ".config" / "amtech" / "conteudo.env"
MIDIA = {".mp4", ".mkv", ".mov", ".webm", ".mp3", ".wav", ".m4a", ".ogg"}
TEXTO = {".md", ".txt"}
ESPERA_SEGUNDOS = 60          # arquivo mexido há menos que isso ainda pode estar sendo copiado
MAX_TENTATIVAS = 3

# O que pedir para cada tipo de entrada (docs/operacao/03-flywheel-de-conteudo.md)
TIPOS: dict[str, dict] = {
    "aulas": {
        "descricao": "uma aula gravada (só tela e voz do professor, sem alunos)",
        "pecas": ["3 cortes verticais com início e fim (mm:ss) e título", "carrossel de 6 a 8 cards com o resumo",
                  "edição da newsletter", "1 questão de concurso com gabarito comentado", "legenda para Instagram e TikTok"],
    },
    "capitulos": {
        "descricao": "um trecho ou capítulo do livro Lógica e Máquina",
        "pecas": ["artigo de blog", "5 cards de conceito", "edição da newsletter", "roteiro de vídeo curto explicando o capítulo"],
    },
    "reparos": {
        "descricao": "anotações de um reparo feito na assistência técnica (sem dados do cliente)",
        "pecas": ["post de antes e depois para o Google Perfil da Empresa", "dica curta de manutenção para Reels",
                  "pergunta frequente para o site"],
    },
    "decisoes": {
        "descricao": "uma decisão real de negócio da semana (números, setup, planejamento)",
        "pecas": ["roteiro do vídeo semanal de build in public", "post para o LinkedIn", "edição da newsletter"],
    },
    "ideias": {
        "descricao": "uma ideia solta de conteúdo ou de oferta",
        "pecas": ["3 ângulos de conteúdo com título", "rascunho de post para Instagram",
                  "sugestão de entrada para o portfólio de ofertas (nome, receita, validação mais barata)"],
    },
}

FORMATO = """Responda SOMENTE com JSON válido, sem texto antes ou depois, neste formato:
{"titulo": "título curto do material", "oferta": "id da oferta do portfólio a que isso leva, se houver",
 "pecas": [{"tipo": "corte|carrossel|newsletter|questao|legenda|artigo|cards|roteiro|post|google|faq|angulos|portfolio",
            "redes": ["instagram", "tiktok", "youtube", "linkedin", "google", "newsletter", "blog"],
            "titulo": "...", "texto": "conteúdo pronto, em português do Brasil",
            "inicio": "mm:ss ou vazio", "fim": "mm:ss ou vazio"}]}"""


# ---------------------------------------------------------------- configuração

def ler_config(caminho: Path) -> dict[str, str]:
    cfg: dict[str, str] = {}
    if caminho.exists():
        for linha in caminho.read_text(encoding="utf-8").splitlines():
            linha = linha.strip()
            if not linha or linha.startswith("#") or "=" not in linha:
                continue
            k, v = linha.split("=", 1)
            cfg[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("ANTHROPIC_API_KEY", "ANTHROPIC_MODEL", "AMTECH_DIR", "TRANSCRITOR_CMD",
              "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID", "GUIA_MARCA"):
        if os.environ.get(k):
            cfg[k] = os.environ[k]
    cfg.setdefault("AMTECH_DIR", str(Path.home() / "AMtech"))
    cfg.setdefault("ANTHROPIC_MODEL", "claude-sonnet-5-5")
    cfg.setdefault("GUIA_MARCA", str(RAIZ_REPO / "config" / "marca.md"))
    cfg.setdefault("TRANSCRITOR_CMD",
                   "whisper-ctranslate2 --language pt --model small --output_format txt --output_dir {saida} {arquivo}")
    return cfg


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-zA-Z0-9]+", "-", t).strip("-").lower()
    return t[:60] or "material"


# ---------------------------------------------------------------- etapas

def transcrever(arquivo: Path, cfg: dict[str, str], pasta_tmp: Path) -> str:
    pasta_tmp.mkdir(parents=True, exist_ok=True)
    cmd = cfg["TRANSCRITOR_CMD"].format(arquivo=shlex.quote(str(arquivo)), saida=shlex.quote(str(pasta_tmp)))
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=3 * 3600)
    if r.returncode != 0:
        raise RuntimeError(f"transcrição falhou ({r.returncode}): {r.stderr[-400:]}")
    txts = sorted(pasta_tmp.glob("*.txt"))
    if not txts:
        raise RuntimeError("o transcritor não gerou nenhum .txt")
    return txts[0].read_text(encoding="utf-8")


def montar_pedido(tipo: str, nome: str, conteudo: str, guia: str) -> tuple[str, str]:
    t = TIPOS[tipo]
    sistema = (
        "Você é o editor de conteúdo do Grupo AMtech Digital. Siga o guia de marca abaixo à risca.\n"
        "Regras que nunca mudam: português do Brasil; nada de dados de alunos ou clientes; nenhuma promessa de "
        "resultado (renda, aprovação, emprego); cada peça termina com um próximo passo (newsletter, página da oferta "
        "ou WhatsApp); se faltar informação, escreva [CONFERIR] no lugar em vez de inventar.\n\n"
        f"GUIA DE MARCA:\n{guia}"
    )
    usuario = (
        f"Material de entrada: {t['descricao']}. Arquivo: {nome}.\n"
        f"Gere estas peças: {'; '.join(t['pecas'])}.\n\n{FORMATO}\n\nMATERIAL:\n{conteudo[:120_000]}"
    )
    return sistema, usuario


def chamar_claude(sistema: str, usuario: str, cfg: dict[str, str]) -> str:
    chave = cfg.get("ANTHROPIC_API_KEY")
    if not chave:
        raise RuntimeError("ANTHROPIC_API_KEY não configurada em ~/.config/amtech/conteudo.env")
    corpo = json.dumps({"model": cfg["ANTHROPIC_MODEL"], "max_tokens": 8000, "system": sistema,
                        "messages": [{"role": "user", "content": usuario}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=corpo, method="POST", headers={
        "x-api-key": chave, "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        dados = json.load(resp)
    return "".join(b.get("text", "") for b in dados.get("content", []) if b.get("type") == "text")


def simular_claude(sistema: str, usuario: str, cfg: dict[str, str]) -> str:
    nome = re.search(r"Arquivo: (.+?)\.\n", usuario)
    return json.dumps({"titulo": f"[SIMULADO] {nome.group(1) if nome else 'material'}", "oferta": "",
                       "pecas": [{"tipo": "post", "redes": ["instagram"], "titulo": "Peça de teste",
                                  "texto": "Gerada sem API para conferir o caminho das pastas.", "inicio": "", "fim": ""}]})


def extrair_json(texto: str) -> dict:
    m = re.search(r"```(?:json)?\s*(\{.*\})\s*```", texto, re.S)
    bruto = m.group(1) if m else texto[texto.find("{"): texto.rfind("}") + 1]
    dados = json.loads(bruto)
    if not isinstance(dados.get("pecas"), list) or not dados["pecas"]:
        raise ValueError("resposta sem peças")
    for p in dados["pecas"]:
        if not p.get("texto"):
            raise ValueError("peça sem texto")
    return dados


def escrever_fila(base: Path, tipo: str, origem: Path, transcricao: str | None, dados: dict, agora: dt.datetime) -> Path:
    pasta = base / "fila" / f"{agora:%Y%m%d-%H%M}-{slug(origem.stem)}"
    n = 2
    while pasta.exists():
        pasta = pasta.with_name(f"{pasta.name}-{n}")
        n += 1
    pasta.mkdir(parents=True)
    if transcricao is not None:
        (pasta / "transcricao.txt").write_text(transcricao, encoding="utf-8")
    (pasta / "pecas.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
    linhas = [f"# {dados.get('titulo', origem.stem)}", "", f"Origem: `{tipo}/{origem.name}` · gerado em {agora:%d/%m/%Y %H:%M}", "",
              "Revise cada peça, edite o que precisar e marque como aprovada no `status.json` (ou pelo Telegram, quando o n8n estiver ligado).", ""]
    for i, p in enumerate(dados["pecas"], 1):
        nome = f"{i:02d}-{slug(p.get('tipo', 'peca'))}.md"
        tempo = f"\n\nTrecho: {p['inicio']} a {p['fim']}" if p.get("inicio") else ""
        (pasta / nome).write_text(f"# {p.get('titulo', '')}\n\nRedes: {', '.join(p.get('redes', []))}{tempo}\n\n{p['texto']}\n",
                                  encoding="utf-8")
        linhas.append(f"- [{p.get('titulo', nome)}]({nome}) · {', '.join(p.get('redes', []))}")
    (pasta / "LEIA-ME.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
    (pasta / "status.json").write_text(json.dumps({"status": "aguardando_aprovacao", "origem": f"{tipo}/{origem.name}",
                                                   "oferta": dados.get("oferta", ""), "criado_em": agora.isoformat()},
                                                  ensure_ascii=False, indent=2), encoding="utf-8")
    return pasta


def avisar_telegram(cfg: dict[str, str], texto: str) -> None:
    token, chat = cfg.get("TELEGRAM_BOT_TOKEN"), cfg.get("TELEGRAM_CHAT_ID")
    if not token or not chat:
        return
    dados = urllib.parse.urlencode({"chat_id": chat, "text": texto}).encode()
    try:
        urllib.request.urlopen(f"https://api.telegram.org/bot{token}/sendMessage", data=dados, timeout=20)
    except OSError as e:  # aviso é bônus: não derruba o pipeline
        print(f"Aviso no Telegram falhou: {e}", file=sys.stderr)


# ---------------------------------------------------------------- orquestração

def pendentes(base: Path, agora_ts: float) -> list[tuple[str, Path]]:
    achados = []
    for tipo in TIPOS:
        pasta = base / "entrada" / tipo
        if not pasta.is_dir():
            continue
        for f in sorted(pasta.iterdir()):
            if f.is_file() and f.suffix.lower() in MIDIA | TEXTO and not f.name.startswith("."):
                if agora_ts - f.stat().st_mtime >= ESPERA_SEGUNDOS:
                    achados.append((tipo, f))
    return achados


def processar_um(tipo: str, arq: Path, cfg: dict[str, str], gerar: Callable[[str, str, dict], str],
                 agora: dt.datetime) -> Path:
    base = Path(cfg["AMTECH_DIR"])
    transcricao = None
    if arq.suffix.lower() in MIDIA:
        transcricao = transcrever(arq, cfg, base / ".tmp" / slug(arq.stem))
        conteudo = transcricao
    else:
        conteudo = arq.read_text(encoding="utf-8")
    guia_path = Path(cfg["GUIA_MARCA"])
    guia = guia_path.read_text(encoding="utf-8") if guia_path.exists() else "(guia de marca ainda não preenchido)"
    sistema, usuario = montar_pedido(tipo, arq.name, conteudo, guia)
    dados = extrair_json(gerar(sistema, usuario, cfg))
    pasta = escrever_fila(base, tipo, arq, transcricao, dados, agora)
    destino = base / "processados" / tipo
    destino.mkdir(parents=True, exist_ok=True)
    shutil.move(str(arq), str(destino / arq.name))
    shutil.rmtree(base / ".tmp" / slug(arq.stem), ignore_errors=True)
    return pasta


def registrar_erro(base: Path, arq: Path, erro: Exception) -> None:
    reg = base / "entrada" / ".erros.json"
    hist = json.loads(reg.read_text(encoding="utf-8")) if reg.exists() else {}
    chave = str(arq)
    hist[chave] = hist.get(chave, 0) + 1
    if hist[chave] >= MAX_TENTATIVAS:
        quarentena = base / "entrada" / "_com-erro"
        quarentena.mkdir(parents=True, exist_ok=True)
        shutil.move(str(arq), str(quarentena / arq.name))
        (quarentena / f"{arq.name}.erro.txt").write_text(str(erro), encoding="utf-8")
        del hist[chave]
    reg.write_text(json.dumps(hist, ensure_ascii=False, indent=2), encoding="utf-8")


def rodar(cfg: dict[str, str], gerar: Callable[[str, str, dict], str], agora: dt.datetime | None = None) -> dict:
    base = Path(cfg["AMTECH_DIR"])
    agora = agora or dt.datetime.now()
    resultado = {"processados": [], "erros": []}
    for tipo, arq in pendentes(base, agora.timestamp()):
        try:
            pasta = processar_um(tipo, arq, cfg, gerar, agora)
            resultado["processados"].append(str(pasta))
            avisar_telegram(cfg, f"Peças prontas para aprovar: {pasta.name}")
        except Exception as e:  # noqa: BLE001 - um arquivo ruim não pode parar a fila
            registrar_erro(base, arq, e)
            resultado["erros"].append(f"{arq.name}: {e}")
    return resultado


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--uma-vez", action="store_true", help="processa o que houver e sai")
    ap.add_argument("--simular", action="store_true", help="não chama a API; gera peças de teste")
    ap.add_argument("--config", type=Path, default=CONFIG_PADRAO)
    a = ap.parse_args()
    cfg = ler_config(a.config)
    base = Path(cfg["AMTECH_DIR"])
    (base / "entrada").mkdir(parents=True, exist_ok=True)
    with open(base / "entrada" / ".trava", "w") as trava:
        try:
            fcntl.flock(trava, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print("Outra execução está em andamento; saindo.")
            return 0
        r = rodar(cfg, simular_claude if a.simular else chamar_claude)
    for p in r["processados"]:
        print("OK  ", p)
    for e in r["erros"]:
        print("ERRO", e, file=sys.stderr)
    if not r["processados"] and not r["erros"]:
        print("Nada novo nas pastas de entrada.")
    return 1 if r["erros"] else 0


if __name__ == "__main__":
    sys.exit(main())
