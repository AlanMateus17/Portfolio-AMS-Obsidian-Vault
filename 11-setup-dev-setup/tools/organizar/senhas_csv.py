#!/usr/bin/env python3
"""Prepara a exportação de senhas do Chrome/Google para importar no KeePassXC. Roda só no seu computador.

    python tools/organizar/senhas_csv.py ~/Downloads/"Chrome Passwords.csv"

O que faz:
- gera um CSV no formato de importação do KeePassXC (Grupo, Título, Usuário, Senha, URL, Notas), com o título
  limpo (ex.: "github.com") e as contas agrupadas por categoria;
- junta duplicatas exatas (mesmo site, usuário e senha);
- mostra na tela SÓ nomes de sites: quais têm senha repetida em vários sites e quais têm senha curta.
  Nenhuma senha é impressa, enviada ou guardada em outro lugar.

Depois de importar no KeePassXC (Banco de dados > Importar > CSV), apague os DOIS arquivos CSV.
"""
from __future__ import annotations

import argparse
import csv
import os
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

GRUPOS = {
    "Bancos e dinheiro": ["itau", "nubank", "pagbank", "xp", "mercadopago", "paypal", "tesouro", "inter", "caixa", "bb.com", "santander", "bradesco", "binance", "blockchain"],
    "Governo": ["gov.br", "receita", "fazenda", "detran", "sefaz"],
    "Código e nuvem": ["github", "gitlab", "vercel", "cloudflare", "hostinger", "supabase", "azure", "aws", "google cloud", "docker"],
    "Vendas": ["hotmart", "kiwify", "eduzz", "mercadolivre", "shopee", "amazon", "udemy"],
    "Redes": ["facebook", "instagram", "tiktok", "linkedin", "youtube", "twitter", "x.com", "kwai", "discord"],
    "E-mail": ["gmail", "outlook", "hotmail", "proton"],
    "IA": ["claude", "openai", "chatgpt", "perplexity", "huggingface", "cursor"],
    "Estudo": ["alura", "rocketseat", "dio", "estacio", "roadmap"],
}


def dominio(url: str) -> str:
    h = urllib.parse.urlparse(url if "://" in url else "https://" + url).hostname or url
    return h[4:] if h.startswith("www.") else h


def grupo(dom: str) -> str:
    d = dom.lower()
    for g, chaves in GRUPOS.items():
        if any(c in d for c in chaves):
            return g
    return "Outros"


def ler(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f))
    out = []
    for r in linhas:
        url = r.get("url") or r.get("URL") or ""
        out.append({"url": url, "usuario": r.get("username") or r.get("Username") or "",
                    "senha": r.get("password") or r.get("Password") or "", "nota": r.get("note") or r.get("Notes") or "",
                    "titulo": dominio(url) if url else (r.get("name") or "sem site")})
    return out


def processar(linhas: list[dict]) -> tuple[list[dict], dict]:
    vistos, unicas = set(), []
    for r in linhas:
        k = (r["titulo"], r["usuario"], r["senha"])
        if k not in vistos:
            vistos.add(k)
            unicas.append(r)
    por_senha = defaultdict(set)
    for r in unicas:
        if r["senha"]:
            por_senha[r["senha"]].add(r["titulo"])
    repetidas = sorted({s for sites in por_senha.values() if len(sites) > 1 for s in sites})
    curtas = sorted({r["titulo"] for r in unicas if 0 < len(r["senha"]) < 12})
    vazias = sorted({r["titulo"] for r in unicas if not r["senha"]})
    return unicas, {"duplicatas_removidas": len(linhas) - len(unicas), "repetidas": repetidas, "curtas": curtas, "vazias": vazias}


def escrever(unicas: list[dict], saida: Path) -> None:
    fd = os.open(saida, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Group", "Title", "Username", "Password", "URL", "Notes"])
        for r in sorted(unicas, key=lambda r: (grupo(r["titulo"]), r["titulo"])):
            w.writerow([grupo(r["titulo"]), r["titulo"], r["usuario"], r["senha"], r["url"], r["nota"]])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--saida")
    a = ap.parse_args()
    ent = Path(a.csv).expanduser()
    if not ent.exists():
        print(f"Arquivo não encontrado: {ent}", file=sys.stderr)
        return 1
    unicas, rel = processar(ler(ent))
    saida = Path(a.saida).expanduser() if a.saida else ent.with_name("keepassxc-importar.csv")
    escrever(unicas, saida)
    print(f"{len(unicas)} contas prontas em {saida} ({rel['duplicatas_removidas']} duplicatas juntadas).")
    print(f"Senha repetida em vários sites ({len(rel['repetidas'])}): troque primeiro, começando por bancos e e-mail.")
    for s in rel["repetidas"]:
        print("  -", s)
    print(f"Senha com menos de 12 caracteres ({len(rel['curtas'])}):")
    for s in rel["curtas"]:
        print("  -", s)
    print("\nPróximo: KeePassXC > Banco de dados > Importar > CSV. Depois APAGUE os dois arquivos CSV.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
