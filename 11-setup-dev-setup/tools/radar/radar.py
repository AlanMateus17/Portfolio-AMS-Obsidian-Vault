#!/usr/bin/env python3
"""Radar de revenda: avalia anúncios e só aprova o que passa da sua hora mínima.

Entrada: um CSV ou JSON de anúncios (titulo, preco, link, categoria) vindo do fluxo do n8n que lê os
alertas de busca salvos no Gmail, ou colado à mão. Referências de preço e conserto ficam num arquivo seu:
~/.config/amtech/radar.toml (modelo em tools/radar/radar.example.toml). Nada disso vai para o GitHub.

    python tools/radar/radar.py anuncios.csv
    python tools/radar/radar.py anuncios.json --config ~/.config/amtech/radar.toml --saida aprovados.md

O radar nunca compra e nunca fala com vendedor: ele só calcula e mostra o checklist antigolpe.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import tomllib
import unicodedata
from pathlib import Path

PADRAO = Path.home() / ".config" / "amtech" / "radar.toml"
CHECKLIST = {
    "celular": ["Consultar o IMEI em consultaaparelhoimpedido.com.br", "Ver a conta Google ou iCloud removida na sua frente",
                "Testar tela, câmera, carga, Wi-Fi e chip", "Recibo com nome e CPF de quem vendeu"],
    "notebook": ["Nota fiscal ou documento de origem", "Conferir número de série na etiqueta e no BIOS",
                 "Rodar o diagnóstico (bateria, disco, memória)", "Recibo com nome e CPF de quem vendeu"],
    "livro": ["Edição e estado das páginas", "Conferir o preço de revenda na Estante Virtual"],
    "pecas": ["Testar a peça antes de pagar", "Recibo com nome e CPF"],
    "veiculo": ["Débitos e restrições no Detran-MG", "Gravame e histórico de leilão ou sinistro", "Vistoria cautelar paga por você", "Nada de sinal antes de ver"],
}
ALERTAS = ["só pix adiantado", "pix adiantado", "sem nota", "urgente", "bloqueado", "icloud", "conta google", "retirada de peças", "sem caixa e sem nota"]


def norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s.lower()).encode("ascii", "ignore").decode()


def carregar_config(caminho: Path) -> dict:
    return tomllib.loads(caminho.read_text(encoding="utf-8"))


def ler_anuncios(caminho: Path) -> list[dict]:
    if caminho.suffix.lower() == ".json":
        return json.loads(caminho.read_text(encoding="utf-8"))
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def referencia(anuncio: dict, cfg: dict) -> dict | None:
    t = norm(anuncio["titulo"])
    melhor = None
    for r in cfg.get("referencia", []):
        if all(norm(p) in t for p in r["contem"]):
            if melhor is None or len(r["contem"]) > len(melhor["contem"]):
                melhor = r
    return melhor


def avaliar(anuncio: dict, cfg: dict) -> dict:
    g = cfg["geral"]
    preco = float(str(anuncio["preco"]).replace("R$", "").replace(".", "").replace(",", ".").strip())
    ref = referencia(anuncio, cfg)
    cat = (ref or {}).get("categoria") or anuncio.get("categoria") or "notebook"
    sinais = [a for a in ALERTAS if a in norm(anuncio["titulo"] + " " + anuncio.get("descricao", ""))]
    if ref is None:
        return {**anuncio, "preco": preco, "categoria": cat, "aprovado": False, "motivo": "sem preço de referência para este modelo",
                "lucro": None, "lucro_hora": None, "sinais": sinais, "checklist": CHECKLIST.get(cat, [])}
    venda = float(ref["revenda"])
    conserto = float(ref.get("conserto", 0))
    horas = float(ref.get("horas", g.get("horas_padrao", 2)))
    taxa = venda * float(g.get("taxa_plataforma", 0.12))
    lucro = venda - preco - conserto - taxa - float(g.get("deslocamento", 15))
    lph = lucro / horas if horas else 0
    margem = lucro / preco if preco else 0
    ok = lph >= g["hora_minima"] and margem >= g.get("margem_minima", 0.2) and not sinais
    motivo = "aprovado" if ok else ("sinais de golpe: " + ", ".join(sinais) if sinais else
                                    f"R$ {lph:.0f}/h (mínimo {g['hora_minima']})" if lph < g["hora_minima"] else f"margem {margem:.0%}")
    if preco < venda * 0.35:
        sinais.append("preço baixo demais: risco de roubo ou golpe")
        ok, motivo = False, "preço baixo demais: conferir a origem antes de qualquer conversa"
    return {**anuncio, "preco": preco, "categoria": cat, "revenda": venda, "lucro": round(lucro, 2), "lucro_hora": round(lph, 2),
            "aprovado": ok, "motivo": motivo, "sinais": sinais, "checklist": CHECKLIST.get(cat, [])}


def relatorio(res: list[dict]) -> str:
    ap = [r for r in res if r["aprovado"]]
    o = [f"# Radar de revenda\n", f"{len(res)} anúncios avaliados, **{len(ap)} aprovados**.\n"]
    for r in sorted(ap, key=lambda r: -r["lucro_hora"]):
        o += [f"## {r['titulo']}", f"Preço R$ {r['preco']:.0f} · revenda R$ {r['revenda']:.0f} · lucro R$ {r['lucro']:.0f} · **R$ {r['lucro_hora']:.0f}/h**  ",
              f"{r.get('link', '')}\n", "Antes de pagar:"] + [f"- [ ] {c}" for c in r["checklist"]] + [""]
    o.append("## Recusados\n")
    o += [f"- {r['titulo']}: {r['motivo']}" for r in res if not r["aprovado"]]
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("anuncios")
    ap.add_argument("--config", default=str(PADRAO))
    ap.add_argument("--saida", default="radar.md")
    a = ap.parse_args()
    cfg_p = Path(a.config).expanduser()
    if not cfg_p.exists():
        print(f"Crie {cfg_p} a partir de tools/radar/radar.example.toml", file=sys.stderr)
        return 1
    cfg = carregar_config(cfg_p)
    res = [avaliar(x, cfg) for x in ler_anuncios(Path(a.anuncios))]
    Path(a.saida).write_text(relatorio(res), encoding="utf-8")
    print(f"{sum(r['aprovado'] for r in res)} de {len(res)} aprovados · {a.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
