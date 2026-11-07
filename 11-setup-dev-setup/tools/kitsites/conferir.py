#!/usr/bin/env python3
"""Confere um site antes de entregar ao cliente e gera o laudo (Markdown).

    python tools/kitsites/conferir.py https://padaria-exemplo.com.br
    python tools/kitsites/conferir.py ./pasta-do-site            # site estático local (index.html)
    python tools/kitsites/conferir.py URL --saida laudo.md --fotos  # fotos de tela, se o Playwright estiver instalado

Sai com código 1 se a nota ficar abaixo do mínimo (padrão 80).
"""
from __future__ import annotations

import argparse
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checagem import checar, modulos_presentes, nota  # noqa: E402


def baixar(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "AMtech-conferir/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:  # nosec - URL do próprio cliente
        return r.read().decode("utf-8", errors="replace")


def existe_url(alvo: str) -> bool:
    try:
        req = urllib.request.Request(alvo, method="HEAD", headers={"User-Agent": "AMtech-conferir/1.0"})
        with urllib.request.urlopen(req, timeout=10):
            return True
    except Exception:
        return False


def fotos(alvo: str, saida: Path) -> list[str]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return []
    feitas = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        for nome, larg in (("celular", 390), ("computador", 1280)):
            pg = b.new_page(viewport={"width": larg, "height": 900})
            pg.goto(alvo, wait_until="load", timeout=30000)
            f = saida.with_name(f"{saida.stem}-{nome}.png")
            pg.screenshot(path=str(f), full_page=False)
            feitas.append(f.name)
        b.close()
    return feitas


def laudo(alvo: str, itens: list[dict], mods: list[str], imgs: list[str]) -> str:
    n = nota(itens)
    o = [f"# Laudo do site\n", f"**Endereço:** {alvo}  ", f"**Nota:** {n}/100\n",
         "| Item | Situação | Detalhe |", "|---|---|---|"]
    for i in itens:
        o.append(f"| {i['item']} | {'OK' if i['ok'] else 'CORRIGIR'} | {i['detalhe']} |")
    o.append("")
    o.append("**Módulos encontrados:** " + (", ".join(mods) or "nenhum"))
    if imgs:
        o.append("")
        o.append("**Fotos de tela:** " + ", ".join(imgs))
    o.append("\nO laudo confere o HTML entregue. Velocidade real e acessibilidade completa: rode também o Lighthouse do Chrome.")
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("alvo")
    ap.add_argument("--saida", default="laudo-site.md")
    ap.add_argument("--minimo", type=int, default=80)
    ap.add_argument("--fotos", action="store_true")
    a = ap.parse_args()
    p = Path(a.alvo)
    if p.exists():
        idx = p / "index.html" if p.is_dir() else p
        html = idx.read_text(encoding="utf-8", errors="replace")
        raiz = idx.parent.resolve()

        def existe(alvo):
            caminho = Path(alvo.replace("file://", ""))
            return caminho.exists() or (caminho / "index.html").exists() or caminho.with_suffix(".html").exists()
        itens = checar(html, base=raiz.as_uri() + "/", existe=existe)
        url = idx.resolve().as_uri()
    else:
        html = baixar(a.alvo)
        itens = checar(html, base=a.alvo, existe=existe_url)
        url = a.alvo
    saida = Path(a.saida)
    imgs = fotos(url, saida) if a.fotos else []
    saida.write_text(laudo(a.alvo, itens, modulos_presentes(html), imgs), encoding="utf-8")
    n = nota(itens)
    print(f"Nota {n}/100 · laudo em {saida}")
    return 0 if n >= a.minimo else 1


if __name__ == "__main__":
    sys.exit(main())
