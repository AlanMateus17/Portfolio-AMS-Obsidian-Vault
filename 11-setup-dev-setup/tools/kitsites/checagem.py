"""Checagens de qualidade de um site, só com a biblioteca padrão do Python.

Usado pelo kit de sites (conferir antes de entregar) e pelo avaliador de templates.
Não executa JavaScript: confere o HTML entregue. Fotos de tela são opcionais (Playwright, se instalado).
"""
from __future__ import annotations

import re
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path


class _Coletor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self._em_title = False
        self.meta: dict[str, str] = {}
        self.imgs: list[dict] = []
        self.links: list[str] = []
        self.scripts = 0
        self.forms = 0
        self.h1 = 0
        self.lang = ""
        self.texto: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "html":
            self.lang = a.get("lang", "")
        elif tag == "title":
            self._em_title = True
        elif tag == "meta":
            k = (a.get("name") or a.get("property") or "").lower()
            if k:
                self.meta[k] = a.get("content", "")
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "a" and a.get("href"):
            self.links.append(a["href"])
        elif tag == "script":
            self.scripts += 1
        elif tag == "form":
            self.forms += 1
        elif tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._em_title = False

    def handle_data(self, data):
        if self._em_title:
            self.title += data
        elif data.strip():
            self.texto.append(data.strip())


def analisar_html(html: str) -> _Coletor:
    c = _Coletor()
    c.feed(html)
    return c


def checar(html: str, base: str = "", existe=None) -> list[dict]:
    """Lista de itens {item, ok, detalhe, peso}. `existe(href)` diz se um link interno existe (opcional)."""
    c = analisar_html(html)
    itens = []

    def it(item, ok, detalhe="", peso=1):
        itens.append({"item": item, "ok": bool(ok), "detalhe": detalhe, "peso": peso})

    it("Título da página", 10 <= len(c.title.strip()) <= 70, c.title.strip()[:70] or "sem <title>", 2)
    d = c.meta.get("description", "")
    it("Descrição para o Google", 50 <= len(d) <= 170, f"{len(d)} caracteres", 2)
    it("Funciona no celular (viewport)", "width=device-width" in c.meta.get("viewport", ""), c.meta.get("viewport", "sem viewport"), 3)
    it("Idioma declarado", bool(c.lang), c.lang or "sem lang no <html>")
    it("Um título principal (h1)", c.h1 == 1, f"{c.h1} h1")
    sem_alt = [i.get("src", "")[:40] for i in c.imgs if not i.get("alt", "").strip()]
    it("Imagens com descrição (alt)", not sem_alt, f"{len(sem_alt)} de {len(c.imgs)} sem alt", 2)
    it("Imagem de compartilhamento (og:image)", bool(c.meta.get("og:image")), "", 1)
    whats = any("wa.me" in l or "api.whatsapp.com" in l for l in c.links)
    it("Botão de WhatsApp", whats, "", 2)
    tel = any(l.startswith("tel:") for l in c.links)
    it("Telefone clicável", tel, "", 1)
    mapa = "google.com/maps" in html or "maps.app.goo.gl" in html or "goo.gl/maps" in html
    it("Mapa ou endereço com link", mapa, "", 1)
    inseguros = [l for l in c.links if l.startswith("http://")]
    it("Links seguros (https)", not inseguros, f"{len(inseguros)} links http://", 1)
    if existe is not None:
        quebrados = []
        for l in c.links:
            if l.startswith(("http", "mailto:", "tel:", "#", "javascript:")) or "wa.me" in l:
                continue
            alvo = urllib.parse.urljoin(base, l.split("#")[0].split("?")[0])
            if alvo and not existe(alvo):
                quebrados.append(l)
        it("Links internos funcionando", not quebrados, ", ".join(quebrados[:5]), 3)
    it("Peso do HTML abaixo de 300 KB", len(html.encode()) < 300_000, f"{len(html.encode()) // 1024} KB", 1)
    return itens


def nota(itens: list[dict]) -> int:
    total = sum(i["peso"] for i in itens) or 1
    return round(100 * sum(i["peso"] for i in itens if i["ok"]) / total)


SINAIS_MODULOS = {
    "cardapio": r"card[áa]pio|menu\b|prato|pizza|lanche",
    "pedidos": r"carrinho|pedido|add to cart|adicionar ao carrinho|delivery",
    "agenda": r"agend|reserv|booking|hor[áa]rio dispon",
    "catalogo": r"im[óo]ve(l|is)|cat[áa]logo|produtos|filtrar|venda|aluguel",
    "galeria": r"galeria|portf[óo]lio|gallery|projetos|obras",
    "orcamento": r"or[çc]amento|cota[çc][ãa]o|quote",
    "blog": r"\bblog\b|not[íi]cias|artigos",
    "avaliacoes": r"depoimento|avalia[çc]|testimonial|review",
    "portal": r"\blogin\b|entrar|minha conta|área do cliente",
    "pagamento": r"\bpix\b|checkout|pagamento|assinatura|planos",
    "leads": r"<form|newsletter|inscreva|contato",
    "vitrine": r"sobre|servi[çc]os|contato|endere[çc]o",
}


def modulos_presentes(html: str) -> list[str]:
    baixo = html.lower()
    return [m for m, rx in SINAIS_MODULOS.items() if re.search(rx, baixo)]


def ler_arquivo_local(caminho: Path) -> str:
    return caminho.read_text(encoding="utf-8", errors="replace")
