#!/usr/bin/env python3
"""Prepara a exportação de senhas do Chrome/Google para importar no KeePassXC. Roda só no seu computador.

    PowerShell do Windows: py $HOME\\dev-setup\\tools\\organizar\\senhas_csv.py "$HOME\\Downloads\\Chrome Passwords.csv"
    Ubuntu do WSL:         python3 tools/organizar/senhas_csv.py ~/Downloads/"Chrome Passwords.csv"

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
import getpass
import os
import shutil
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

# Palavra com "=" na frente vale só para o endereço exato (=x.com não pega netflix.com).
# A ordem importa: o primeiro grupo cuja palavra aparece no site ganha (por isso Escola vem antes de Governo).
# Os números deixam os grupos na mesma ordem no KeePassXC: 00 é a corrente de recuperação, que protege todo o resto.
GRUPOS = {
    "00 Essenciais (e-mail e contas-mãe)": ["accounts.google", "myaccount.google", "gmail", "outlook", "hotmail", "live.com",
                                            "microsoft", "apple", "icloud", "proton", "=google.com"],
    "01 Bancos e dinheiro": ["itau", "nubank", "pagbank", "pagseguro", "xp", "mercadopago", "paypal", "tesouro", "inter", "caixa", "bb.com",
                             "santander", "bradesco", "c6bank", "picpay", "binance", "blockchain", "rico", "clear", "btg", "b3.com", "b3investidor", "br.com.bb", "bb.com.br", "com.itau", "bitnuvem", "bitypreco", "recupera.com", "bahamascred", "sofisa", "biscoint", "visa.com"],
    "03 Escola (só os seus acessos)": ["educacao.mg", "see.mg", "sisap", "simade", "diario", "moodle", "classroom"],
    "02 Governo": ["gov.br", "receita", "fazenda", "detran", "sefaz", "inss", "esocial.gov", "inpi", "mg.gov.br", "sispatri", "prodemge", "correios", "copasa"],
    "04 Grupo AMtech Digital": ["registro.br", "cloudflare", "hostinger", "business.facebook", "business.whatsapp", "whatsapp", "cal.com",
                                "zoho", "resend", "upwork", "canva", "nuvemshop", "wordfence", "cloudclusters", "phpmyadmin"],
    "05 Instituto e Editora": ["hotmart", "kiwify", "eduzz", "udemy", "mailerlite", "amazon.com.br/kdp", "kdp", "clubedeautores", "isbn",
                               "cbl.org", "institutoamssilva"],
    "06 Código e nuvem": ["github", "gitlab", "vercel", "supabase", "azure", "aws", "cloud.google", "docker", "npmjs", "nuget", "oracle",
                          "backblaze", "tailscale", "sonarcloud", "sentry", "app-preview.com", "datadoghq", "n8n", "datomic", "hotreload", "obsidian.md", "infobip", "formspree", "=localhost", "wordpress.org"],
    "07 IA": ["claude", "anthropic", "openai", "chatgpt", "gemini", "perplexity", "huggingface", "cursor", "deepseek", "grok", "x.ai",
              "elevenlabs", "notebooklm", "claudeusercontent"],
    "08 Redes": ["facebook", "instagram", "tiktok", "linkedin", "youtube", "twitter", "=x.com", "kwai", "discord", "telegram", "threads", "vidiq", "twitch"],
    "09 Estudo": ["alura", "rocketseat", "dio.me", "estacio", "roadmap", "tryhackme", "hackthebox", "coursera", "ankiweb", "kaggle", "duolingo", "unicv", "anbimaedu", "cademi", "fabricadeprovas", "portaleducacional", "saberemrede", "pagtrust", "finclass", "cursoemvideo", "iungo", "unigrande", "refactoring.guru"],
    "10 Compras e assinaturas": ["mercadolivre", "shopee", "amazon", "aliexpress", "magazineluiza", "netflix", "spotify", "ifood", "uber", "kabum", "acer", "lojabhs", "superbid", "leiloes", "luizalabs", "magalu", "disneyplus", "max.com", "globo", "steampowered", "dreamstime", "adobe", "autodesk", "ilovepdf", "99app", "casio", "raizen", "indrive", "myhonda", "ticket360"],
    "12 Carreira e vagas": ["empregos", "abler", "infojobs", "vagas.com", "bne.com", "selecty", "talentbrand", "rivelli", "superestagios",
                            "fiemg", "catho", "gupy", "solides", "nerdin"],
}

OUTROS = "11 Outros (revisar)"
SETUP = "20 Setup técnico"
TODOS_OS_GRUPOS = sorted([*GRUPOS, OUTROS, SETUP])


def dominio(url: str) -> str:
    h = urllib.parse.urlparse(url if "://" in url else "https://" + url).hostname or url
    return h[4:] if h.startswith("www.") else h


def grupo(dom: str) -> str:
    d = dom.lower()
    for g, chaves in GRUPOS.items():
        if any(d == c[1:] if c.startswith("=") else c in d for c in chaves):
            return g
    return OUTROS


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


def nota_com_alerta(r: dict, rel: dict) -> str:
    """Marca na nota o que precisa de troca, para achar no KeePassXC buscando TROCAR."""
    alertas = []
    if r["titulo"] in rel["repetidas"]:
        alertas.append("TROCAR: senha repetida em outro site")
    if r["titulo"] in rel["curtas"]:
        alertas.append("TROCAR: senha curta")
    return "\n".join(alertas + ([r["nota"]] if r["nota"] else []))


def escrever(unicas: list[dict], saida: Path, rel: dict | None = None) -> None:
    rel = rel or {"repetidas": [], "curtas": []}
    fd = os.open(saida, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Group", "Title", "Username", "Password", "URL", "Notes"])
        for r in sorted(unicas, key=lambda r: (grupo(r["titulo"]), r["titulo"])):
            w.writerow([grupo(r["titulo"]), r["titulo"], r["usuario"], r["senha"], r["url"], nota_com_alerta(r, rel)])


def achar_cli() -> str | None:
    """keepassxc-cli no PATH ou no lugar padrão do Windows."""
    win = Path(os.environ.get("ProgramFiles", r"C:\Program Files")) / "KeePassXC" / "keepassxc-cli.exe"
    return shutil.which("keepassxc-cli") or (str(win) if win.exists() else None)


def _cli(cli: str, args: list[str], entrada: str, run=subprocess.run, utf8: bool = False):
    """Roda o keepassxc-cli mandando as senhas pela entrada padrão: nunca na linha de comando nem na tela.
    utf8=True lê a saída como UTF-8 (o keepassxc-cli escreve assim; no Windows o padrão do Python é cp1252 e estraga o '·')."""
    if utf8:
        return run([cli, *args], input=entrada, text=True, capture_output=True, encoding="utf-8", errors="replace")
    return run([cli, *args], input=entrada, text=True, capture_output=True)


def criar_grupos(cofre: str, cli: str, mestre: str, run=subprocess.run) -> int:
    """Cria os grupos numerados que faltam. Devolve quantos criou."""
    criados = 0
    for g in TODOS_OS_GRUPOS:
        r = _cli(cli, ["mkdir", "-q", cofre, g], mestre + "\n", run)
        criados += r.returncode == 0
    return criados


def gravar_no_cofre(unicas: list[dict], rel: dict, cofre: str, cli: str, mestre: str, run=subprocess.run) -> tuple[int, list[str]]:
    """Grava cada conta direto no cofre, sem arquivo intermediário. Devolve (gravadas, títulos que falharam)."""
    usados, falhas, ok = set(), [], 0
    for i, r in enumerate(sorted(unicas, key=lambda r: (grupo(r["titulo"]), r["titulo"])), 1):
        g = grupo(r["titulo"])
        base = r["titulo"].replace("/", "-")
        titulo = base if (g, base) not in usados else f"{base} · {r['usuario'] or 'sem usuário'}"
        n = 2
        while (g, titulo) in usados:
            titulo, n = f"{base} ({n})", n + 1
        titulo = titulo.replace("/", "-")
        usados.add((g, titulo))
        args = ["add", "-q", "-p", "-u", r["usuario"], "--url", r["url"]]
        alerta = nota_com_alerta({**r, "nota": ""}, rel)
        if alerta:
            args += ["--notes", alerta]
        res = _cli(cli, [*args, cofre, f"{g}/{titulo}"], f"{mestre}\n{r['senha']}\n", run)
        if res.returncode == 0:
            ok += 1
        else:
            falhas.append(f"{g}/{titulo}")
        if i % 25 == 0:
            print(f"  ... {i} de {len(unicas)}")
    return ok, falhas


def reorganizar(cofre: str, cli: str, mestre: str, run=subprocess.run) -> list[tuple[str, str]]:
    """Move do grupo Outros para o grupo certo o que as regras novas já reconhecem. Devolve (entrada, grupo) movidos."""
    r = _cli(cli, ["ls", "-q", cofre, OUTROS], mestre + "\n", run, utf8=True)
    movidos = []
    for titulo in (ln.strip() for ln in (r.stdout or "").splitlines()):
        if not titulo or titulo.startswith("[") or titulo.endswith("/"):
            continue
        destino = grupo(titulo.split(" · ")[0].split(" (")[0])
        if destino != OUTROS and _cli(cli, ["mv", "-q", cofre, f"{OUTROS}/{titulo}", destino], mestre + "\n", run, utf8=True).returncode == 0:
            movidos.append((titulo, destino))
    return movidos


def configurar_bloqueio(ini: Path, segundos: int = 300) -> None:
    """Liga no keepassxc.ini o bloqueio do cofre depois de N segundos parado (o KeePassXC precisa estar fechado)."""
    chaves = {"LockDatabaseIdle": "true", "LockDatabaseIdleSeconds": str(segundos)}
    linhas = ini.read_text(encoding="utf-8").splitlines() if ini.exists() else []
    if "[Security]" not in linhas:
        linhas += ["", "[Security]"]
    ini_sec = linhas.index("[Security]")
    fim = next((i for i in range(ini_sec + 1, len(linhas)) if linhas[i].startswith("[")), len(linhas))
    sec = [ln for ln in linhas[ini_sec + 1:fim] if ln.split("=", 1)[0] not in chaves]
    sec = [ln for ln in sec if ln.strip()] + [f"{k}={v}" for k, v in chaves.items()]
    novas = linhas[:ini_sec + 1] + sec + ([""] if fim < len(linhas) else []) + linhas[fim:]
    ini.parent.mkdir(parents=True, exist_ok=True)
    ini.write_text("\n".join(novas).strip("\n") + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?")
    ap.add_argument("--saida")
    ap.add_argument("--cofre", help="grava direto no Cofre.kdbx pelo keepassxc-cli, sem criar o CSV de importação")
    ap.add_argument("--so-grupos", action="store_true", help="só cria os grupos numerados no cofre (com --cofre)")
    ap.add_argument("--reorganizar", action="store_true", help="move do grupo Outros para o grupo certo (com --cofre)")
    ap.add_argument("--bloqueio", type=int, metavar="MINUTOS", help="liga o bloqueio automático do KeePassXC (feche o KeePassXC antes)")
    a = ap.parse_args()
    if a.bloqueio:
        ini = Path(os.environ.get("APPDATA", Path.home() / ".config")) / ("KeePassXC" if os.name == "nt" else "keepassxc") / "keepassxc.ini"
        configurar_bloqueio(ini, a.bloqueio * 60)
        print(f"Bloqueio automático depois de {a.bloqueio} min parado: {ini}")
        if not a.cofre and not a.csv:
            return 0
    if a.cofre:
        cli = achar_cli()
        if not cli:
            print("Não achei o keepassxc-cli. Instale o KeePassXC.", file=sys.stderr)
            return 1
        mestre = getpass.getpass("Senha mestra do cofre (não aparece na tela): ")
        if _cli(cli, ["ls", "-q", a.cofre], mestre + "\n").returncode != 0:
            print("Não abriu o cofre: senha mestra errada ou caminho errado. Nada foi gravado.", file=sys.stderr)
            return 1
        print(f"{criar_grupos(a.cofre, cli, mestre)} grupo(s) criados (os que já existiam ficaram).")
        if a.reorganizar:
            movidos = reorganizar(a.cofre, cli, mestre)
            for t, g in movidos:
                print(f"  {t} -> {g}")
            print(f"{len(movidos)} entrada(s) saíram de '{OUTROS}'.")
        if a.so_grupos or a.reorganizar:
            return 0
    if not a.csv:
        print("Falta o arquivo CSV exportado do navegador.", file=sys.stderr)
        return 1
    ent = Path(a.csv).expanduser()
    if not ent.exists():
        print(f"Arquivo não encontrado: {ent}", file=sys.stderr)
        return 1
    unicas, rel = processar(ler(ent))
    if a.cofre:
        ok, falhas = gravar_no_cofre(unicas, rel, a.cofre, cli, mestre)
        print(f"{ok} de {len(unicas)} contas gravadas no cofre ({rel['duplicatas_removidas']} duplicatas juntadas).")
        for f in falhas:
            print("  não gravou:", f)
    else:
        saida = Path(a.saida).expanduser() if a.saida else ent.with_name("keepassxc-importar.csv")
        escrever(unicas, saida, rel)
        print(f"{len(unicas)} contas prontas em {saida} ({rel['duplicatas_removidas']} duplicatas juntadas).")
    print(f"Senha repetida em vários sites ({len(rel['repetidas'])}): troque primeiro, começando por bancos e e-mail.")
    for s in rel["repetidas"]:
        print("  -", s)
    print(f"Senha com menos de 12 caracteres ({len(rel['curtas'])}):")
    for s in rel["curtas"]:
        print("  -", s)
    print(f"\nSem grupo conhecido: {sum(1 for r in unicas if grupo(r['titulo']) == OUTROS)} conta(s) em '{OUTROS}'.")
    print("No KeePassXC, busque TROCAR para ver as que precisam de senha nova.")
    if a.cofre:
        print(f"\nPróximo: confira o cofre e APAGUE o arquivo exportado: {ent}")
    else:
        print("\nPróximo: KeePassXC > Banco de dados > Importar > CSV. Depois APAGUE os dois arquivos CSV (Shift+Delete).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
