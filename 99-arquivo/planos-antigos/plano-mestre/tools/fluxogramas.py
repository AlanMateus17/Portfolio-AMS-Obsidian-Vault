"""Junta todos os diagramas Mermaid dos documentos do setup numa página só."""
import re, sys, html, pathlib
docs = pathlib.Path(sys.argv[1]); out = sys.argv[2]

ORDEM = ["fluxos.md", "arquitetura.md"]
arqs = sorted(docs.rglob("*.md"), key=lambda p: (0 if p.name in ORDEM else 1 if "camadas" in p.parts else 2,
                                                 ORDEM.index(p.name) if p.name in ORDEM else 0, str(p)))
grupos = []
total = 0
for p in arqs:
    t = p.read_text(encoding="utf-8")
    if "```mermaid" not in t: continue
    doc_titulo = next((l[2:].strip() for l in t.splitlines() if l.startswith("# ")), p.stem)
    itens = []
    for m in re.finditer(r"```mermaid\n(.*?)```", t, re.S):
        antes = t[:m.start()]
        h = re.findall(r"^#{2,3} (.+)$", antes, re.M)
        titulo = h[-1].strip() if h else doc_titulo
        # parágrafo de explicação entre o título e o diagrama
        pos = max(antes.rfind("\n## "), antes.rfind("\n### "))
        trecho = antes[pos:].split("\n", 2)[-1] if pos >= 0 else ""
        texto = " ".join(l.strip() for l in trecho.splitlines() if l.strip() and not l.startswith(("|", "[", "<!--", ">", "-", "*")))
        itens.append((titulo, texto[:400], m.group(1)))
        total += 1
    grupos.append((str(p.relative_to(docs)), doc_titulo, itens))

def gid(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

nav = []; corpo = []
for rel, dt, itens in grupos:
    a = gid(rel)
    nav.append(f'<a href="#{a}">{html.escape(dt)} <span>{len(itens)}</span></a>')
    corpo.append(f'<section id="{a}"><h2>{html.escape(dt)}</h2><p class="src">docs/{html.escape(rel)}</p>')
    for i, (ti, tx, mm) in enumerate(itens):
        corpo.append(f'<figure><figcaption><b>{html.escape(ti)}</b>' + (f'<span>{html.escape(tx)}</span>' if tx else "") +
                     f'</figcaption><div class="box"><pre class="mermaid">{html.escape(mm)}</pre></div></figure>')
    corpo.append("</section>")

page = f"""<title>Fluxogramas do Setup</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
/* Layout: índice de documentos no topo, depois cada diagrama em largura total, com rolagem lateral própria */
:root{{--bg:#f5f6f3;--surface:#fff;--fg:#1d2420;--muted:#5d6862;--line:#d7dcd6;--accent:#0f6b58;--ochre:#a8640b;
--f-d:"Bricolage Grotesque",ui-sans-serif,system-ui,sans-serif;--f-b:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;--f-m:"IBM Plex Mono",ui-monospace,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#121614;--surface:#1a201d;--fg:#e4e9e5;--muted:#9aa59f;--line:#323a35;--accent:#5cc4a6;--ochre:#e0a14a;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#121614;--surface:#1a201d;--fg:#e4e9e5;--muted:#9aa59f;--line:#323a35;--accent:#5cc4a6;--ochre:#e0a14a;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font:15px/1.5 var(--f-b)}}
.wrap{{max-width:1200px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 60px}}
h1,h2{{font-family:var(--f-d);margin:0;text-wrap:balance}} h1{{font-size:clamp(28px,5vw,40px)}} h2{{font-size:24px;margin-top:36px}}
.lede{{color:var(--muted);max-width:70ch}}
nav{{display:flex;flex-wrap:wrap;gap:6px;margin:16px 0 8px}}
nav a{{font-size:13px;text-decoration:none;color:var(--fg);border:1px solid var(--line);background:var(--surface);border-radius:999px;padding:4px 10px}}
nav a span{{color:var(--ochre);font-weight:600;margin-left:4px;font-variant-numeric:tabular-nums}}
nav a:focus-visible{{outline:2px solid var(--accent);outline-offset:2px}}
.src{{font:12px var(--f-m);color:var(--muted);margin:2px 0 10px}}
figure{{margin:0 0 18px;background:var(--surface);border:1px solid var(--line);border-radius:10px;min-width:0}}
figcaption{{padding:10px 14px;border-bottom:1px solid var(--line);display:flex;flex-direction:column;gap:2px}}
figcaption span{{color:var(--muted);font-size:13.5px;max-width:80ch}}
.box{{overflow-x:auto;padding:12px}}
.box pre{{margin:0;background:transparent}}
</style>
<div class="wrap">
<h1>Fluxogramas do Setup</h1>
<p class="lede">Todos os {total} diagramas dos documentos do dev-setup numa página: os 17 fluxos de ponta a ponta, a arquitetura, as 23 camadas e os diagramas de operação, marketing, negócios e editora. Diagrama largo rola para o lado dentro do próprio quadro. Os mesmos diagramas estão nos documentos da pasta 11-setup-dev-setup do vault.</p>
<nav aria-label="Documentos">{''.join(nav)}</nav>
{''.join(corpo)}
</div>
"""
open(out, "w", encoding="utf-8").write(page)
print(total, "diagramas em", len(grupos), "documentos")
