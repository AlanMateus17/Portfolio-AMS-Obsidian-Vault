#!/usr/bin/env python3
"""Avalia uma pasta de templates de sites e diz qual é útil, qual adaptar e qual descartar.

    python tools/avaliador/avaliar.py ~/templates            # cada subpasta ou .zip é um template
    python tools/avaliador/avaliar.py ~/templates --fotos    # fotos de tela (Playwright, se instalado)

Segurança: só LÊ os arquivos. Não roda npm install, build nem PHP dos templates (código de terceiros).
Saída: avaliacao-templates.md e avaliacao-templates.json na pasta dos templates.
Os .zip são extraídos numa pasta nova "_extraidos" ao lado, nunca por cima de nada.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "kitsites"))
from checagem import checar, modulos_presentes, nota  # noqa: E402

SW = RAIZ / "data" / "softwares.json"
PALAVRAS = {  # tipo de negócio do catálogo -> palavras que aparecem nos templates
    "site-padaria": "padaria|confeitaria|bakery|bolo|cake|doce",
    "site-restaurante": "restaurante|restaurant|lanchonete|pizza|burger|hamb|sushi|food",
    "site-cafeteria": r"caf[ée]|coffee",
    "site-imobiliaria": r"im[óo]ve|imobili|real estate|property|apartamento",
    "site-construtora": r"constru|obra|engenharia|building|architect",
    "site-oficina": r"oficina|mec[âa]nic|auto ?pe[çc]a|car repair|garage",
    "site-assistencia": r"assist[êe]ncia|conserto|repair|celular|smartphone",
    "site-clinica": r"cl[íi]nica|m[ée]dic|sa[úu]de|health|psic|fisio|nutri",
    "site-odonto": r"odonto|dentist|dental",
    "site-beleza": r"sal[ãa]o|barbear|beauty|est[ée]tica|spa|cabelo",
    "site-academia": r"academia|gym|fitness|personal|crossfit|yoga",
    "site-pet": r"\bpet\b|veterin|dog|cachorro|gato",
    "site-escola": r"escola|school|curso|educa|course",
    "site-advocacia": r"advoca|advogad|lawyer|law firm|jur[íi]d",
    "site-contabilidade": r"contab|account",
    "site-loja": r"loja|shop|store|moda|fashion|roupa",
    "site-mercado": r"mercado|hortifruti|market|grocery|a[çc]ougue",
    "site-pousada": r"pousada|hotel|hostel|resort",
    "site-floricultura": r"flor|flower|floricultura",
    "site-eventos": r"evento|buffet|wedding|casamento|fot[óo]graf|photograph",
    "site-arquitetura": r"arquitet|interior|marcenaria|design de interiores",
    "site-autoescola": r"autoescola|auto escola|driving",
    "site-solar": r"solar|energia|el[ée]tric",
    "site-mudancas": r"mudan[çc]a|frete|transport|logistic",
    "site-igreja": r"igreja|church|ong|doa[çc]",
    "site-industria": r"ind[úu]stria|industrial|fornecedor|factory",
}


def tecnologia(pasta: Path) -> str:
    if (pasta / "package.json").exists():
        try:
            pj = json.loads((pasta / "package.json").read_text(encoding="utf-8", errors="replace"))
        except ValueError:
            return "node (package.json inválido)"
        deps = {**pj.get("dependencies", {}), **pj.get("devDependencies", {})}
        for k, n in (("next", "Next.js"), ("astro", "Astro"), ("nuxt", "Nuxt"), ("vite", "Vite"), ("react", "React"), ("vue", "Vue"), ("gatsby", "Gatsby")):
            if k in deps:
                return n
        return "Node"
    for css in pasta.rglob("style.css"):
        if "Theme Name" in css.read_text(encoding="utf-8", errors="replace")[:2000]:
            return "WordPress (tema)"
    if any(pasta.rglob("*.php")):
        return "PHP"
    if any(pasta.rglob("index.html")):
        return "HTML estático"
    return "desconhecida"


def licenca(pasta: Path) -> str:
    for f in pasta.rglob("*"):
        if f.is_file() and re.match(r"(licen[cs]e|licen[çc]a|copying|termos)", f.name, re.I):
            txt = f.read_text(encoding="utf-8", errors="replace")[:4000].lower()
            if "mit license" in txt or "permission is hereby granted" in txt:
                return "MIT"
            if "gnu general public" in txt:
                return "GPL"
            if "creative commons" in txt:
                return "Creative Commons"
            return f"arquivo {f.name} (ler os termos)"
    return "não encontrada"


def principal_html(pasta: Path) -> Path | None:
    cands = sorted(pasta.rglob("index.html"), key=lambda p: (len(p.parts), str(p)))
    cands = [c for c in cands if "node_modules" not in c.parts]
    return cands[0] if cands else None


def encaixe(texto: str) -> list[str]:
    baixo = texto.lower()
    return [k for k, rx in PALAVRAS.items() if re.search(rx, baixo)]


def avaliar_pasta(pasta: Path) -> dict:
    tec = tecnologia(pasta)
    idx = principal_html(pasta)
    html = idx.read_text(encoding="utf-8", errors="replace") if idx else ""
    nomes = " ".join(p.name for p in pasta.rglob("*") if p.is_file())[:20000]
    if idx:
        raiz = idx.parent

        def existe(alvo):
            c = Path(alvo.replace("file://", ""))
            return c.exists() or (c / "index.html").exists()
        itens = checar(html, base=raiz.resolve().as_uri() + "/", existe=existe)
        n = nota(itens)
    else:
        itens, n = [], 0
    mods = modulos_presentes(html)
    nichos = encaixe(pasta.name + " " + html[:200000] + " " + nomes)
    manut = {"HTML estático": 3, "Next.js": 3, "Astro": 3, "Vite": 2, "React": 2, "WordPress (tema)": 2, "Vue": 1, "Nuxt": 1, "Gatsby": 1, "PHP": 1, "Node": 1}.get(tec, 0)
    lic = licenca(pasta)
    pontos = n * 0.5 + min(len(mods), 8) * 3 + min(len(nichos), 3) * 5 + manut * 5
    if not idx and tec in ("Next.js", "Astro", "Vite", "React", "Vue", "Nuxt", "Gatsby", "Node"):
        pontos += 25  # precisa de build para ver o HTML; não penalizar a nota técnica
    veredito = "útil" if pontos >= 70 and nichos else "adaptar" if pontos >= 45 else "descartar"
    if lic == "não encontrada":
        veredito += " (confirmar licença)"
    return {"template": pasta.name, "tecnologia": tec, "licenca": lic, "nota_html": n, "modulos": mods,
            "nichos": nichos, "pontos": round(pontos), "veredito": veredito,
            "corrigir": [i["item"] for i in itens if not i["ok"]], "precisa_build": not idx and manut > 0}


def preparar(origem: Path) -> list[Path]:
    pastas = [p for p in sorted(origem.iterdir()) if p.is_dir() and not p.name.startswith(("_", "."))]
    zips = sorted(origem.glob("*.zip"))
    if zips:
        destino = origem / "_extraidos"
        destino.mkdir(exist_ok=True)
        for z in zips:
            alvo = destino / z.stem
            if not alvo.exists():
                with zipfile.ZipFile(z) as zf:
                    for m in zf.namelist():  # proteção contra caminhos que saem da pasta
                        if m.startswith("/") or ".." in Path(m).parts:
                            raise SystemExit(f"{z.name}: caminho suspeito dentro do zip ({m}); não extraído")
                    zf.extractall(alvo)
            pastas.append(alvo)
    return pastas


def relatorio(res: list[dict]) -> str:
    o = ["# Avaliação dos templates\n",
         f"{len(res)} templates. **Útil:** pronto para virar base de um tipo de negócio. **Adaptar:** aproveitável com trabalho. "
         "**Descartar:** não compensa. Sem licença encontrada, confirme os termos da compra antes de usar com cliente.\n",
         "| # | Template | Veredito | Pontos | Tecnologia | Nota HTML | Tipos de negócio | Módulos | Licença |",
         "|---:|---|---|---:|---|---:|---|---|---|"]
    for i, r in enumerate(sorted(res, key=lambda r: -r["pontos"]), 1):
        nh = "precisa build" if r["precisa_build"] else r["nota_html"]
        o.append(f"| {i} | {r['template']} | **{r['veredito']}** | {r['pontos']} | {r['tecnologia']} | {nh} | "
                 f"{', '.join(n.replace('site-', '') for n in r['nichos'][:4]) or '—'} | {', '.join(r['modulos']) or '—'} | {r['licenca']} |")
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pasta")
    ap.add_argument("--fotos", action="store_true")
    a = ap.parse_args()
    origem = Path(a.pasta).expanduser()
    if not origem.is_dir():
        print(f"Pasta não encontrada: {origem}", file=sys.stderr)
        return 1
    res = [avaliar_pasta(p) for p in preparar(origem)]
    if a.fotos:
        try:
            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                b = pw.chromium.launch()
                for r, p in zip(res, preparar(origem)):
                    idx = principal_html(p)
                    if idx:
                        pg = b.new_page(viewport={"width": 390, "height": 900})
                        pg.goto(idx.resolve().as_uri(), timeout=30000)
                        pg.screenshot(path=str(origem / f"foto-{r['template']}-celular.png"))
                b.close()
        except ImportError:
            print("Playwright não instalado: sem fotos.")
    (origem / "avaliacao-templates.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    (origem / "avaliacao-templates.md").write_text(relatorio(res), encoding="utf-8")
    uteis = sum(r["veredito"].startswith("útil") for r in res)
    print(f"{len(res)} templates avaliados: {uteis} úteis. Relatório em {origem / 'avaliacao-templates.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
