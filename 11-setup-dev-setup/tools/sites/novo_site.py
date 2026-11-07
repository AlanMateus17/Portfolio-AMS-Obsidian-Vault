#!/usr/bin/env python3
"""Cria (ou atualiza) o site de uma marca do grupo a partir do modelo Astro do setup.

O modelo fica em infra/templates/site-marca e os textos de cada marca em data/marcas/<id>.json. O site gerado é um
repositório próprio em ~/dev/sites/<id> (ou --destino). Rodar de novo só atualiza src/marca.json e o modelo, sem tocar
no histórico do git do site.

    python3 tools/sites/novo_site.py amtech            # cria ou atualiza ~/dev/sites/amtech
    python3 tools/sites/novo_site.py instituto --checar  # só lista o que falta você preencher para publicar
    python3 tools/sites/novo_site.py --todas --checar
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
MODELO = RAIZ / "infra" / "templates" / "site-marca"
MARCAS = RAIZ / "data" / "marcas"
IGNORAR = shutil.ignore_patterns("node_modules", "dist", ".astro")


def carregar(mid: str) -> dict:
    arq = MARCAS / f"{mid}.json"
    if not arq.exists():
        raise ValueError(f"marca {mid} não existe (há: {', '.join(p.stem for p in sorted(MARCAS.glob('*.json')))})")
    return json.loads(arq.read_text(encoding="utf-8"))


def pendencias(m: dict) -> list[str]:
    """O que só o Alan pode preencher antes de publicar. Lista vazia = pronto para ir ao ar."""
    p = []
    if not m.get("dominio"):
        p.append("dominio: registre no Registro.br (passo dom) e escreva aqui, sem https://")
    c = m["contato"]
    if not (c.get("formulario") or c.get("whatsapp") or c.get("email")):
        p.append("contato: pelo menos um canal (formulário do HeyForm, WhatsApp Business ou e-mail do domínio)")
    if not m["legal"].get("email_privacidade"):
        p.append("legal.email_privacidade: o e-mail para pedidos da LGPD (pode ser o mesmo do contato)")
    sem_preco = [o["nome"] for o in m["ofertas"] if not o.get("preco")]
    if sem_preco:
        aviso = m.get("texto_sem_preco") or "Sob orçamento"
        p.append(f"ofertas sem preço ({', '.join(sem_preco)}): aparecem como '{aviso}'; decida no passo de preço ou deixe assim")
    vendem = [o["nome"] for o in m["ofertas"] if o.get("acao") and o.get("preco") not in ("Em breve", "Em produção") and not o.get("link")]
    if m["id"] != "amtech" and vendem:
        p.append(f"link de venda ou lista de espera de: {', '.join(vendem)} (checkout da Hotmart ou Kiwify, ou formulário)")
    if not (m.get("analytics") or {}).get("umami"):
        p.append("analytics.umami: script e id do Umami (opcional, mas sem ele você não mede visitas)")
    return p


def gerar(mid: str, destino: Path) -> Path:
    m = carregar(mid)
    novo = not destino.exists()
    destino.mkdir(parents=True, exist_ok=True)
    for item in MODELO.iterdir():
        alvo = destino / item.name
        if item.is_dir():
            shutil.copytree(item, alvo, dirs_exist_ok=True, ignore=IGNORAR)
        else:
            shutil.copy2(item, alvo)
    (destino / "src" / "marca.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    leia = destino / "LEIA.md"
    if novo or not leia.exists():
        leia.write_text(f"""# {m['nome']}: site

Gerado pelo dev-setup (`just site {mid}`). Textos, ofertas e cores ficam em `data/marcas/{mid}.json` no dev-setup: mude lá
e rode `just site {mid}` de novo, que este repositório é atualizado.

    npm install && npm run dev      # ver no navegador
    npm run build                   # gera dist/ para publicar

Publicar: ligue este repositório ao Cloudflare Pages ou à Hostinger (deploy por push). Antes, `just site {mid} --checar`
precisa voltar sem pendências.
""", encoding="utf-8")
    return destino


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("marca", nargs="?")
    ap.add_argument("--todas", action="store_true")
    ap.add_argument("--checar", action="store_true", help="só lista as pendências")
    ap.add_argument("--destino", help="pasta do site (padrão: ~/dev/sites/<marca>)")
    args = ap.parse_args(argv)
    ids = [p.stem for p in sorted(MARCAS.glob("*.json"))] if args.todas else [args.marca] if args.marca else []
    if not ids:
        ap.error("diga a marca (amtech, instituto, editora) ou --todas")
    try:
        total = 0
        for mid in ids:
            m = carregar(mid)
            pend = pendencias(m)
            total += len(pend)
            if not args.checar:
                destino = Path(args.destino) if args.destino and len(ids) == 1 else Path.home() / "dev" / "sites" / mid
                print(f"{m['nome']}: site em {gerar(mid, destino)}")
            print(f"{m['nome']}: " + ("pronto para publicar." if not pend else f"{len(pend)} pendência(s) suas:"))
            for p in pend:
                print(f"  - {p}")
        return 0 if (not args.checar or total == 0) else 1
    except ValueError as erro:
        print(erro, file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
