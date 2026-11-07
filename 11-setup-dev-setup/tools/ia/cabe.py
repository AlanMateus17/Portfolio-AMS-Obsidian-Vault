#!/usr/bin/env python3
"""Este modelo cabe no meu computador? Estimativa de memória para rodar e para treinar (QLoRA).

    python tools/ia/cabe.py 70                     # 70 bilhões de parâmetros, nas quantizações comuns
    python tools/ia/cabe.py 32 --ram 32 --vram 4    # contra a sua máquina (padrão: Acer Nitro 32 GB + GTX 1650 4 GB)
    python tools/ia/cabe.py 30 --ativos 3           # MoE: 30B no total, 3B ativos por token
    python tools/ia/cabe.py --hf Qwen/Qwen3-VL-2B-Instruct   # lê o tamanho direto do Hugging Face

Contas aproximadas (pesos + cache de contexto + folga); confira sempre no primeiro teste real.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

BITS = {"Q4 (GGUF Q4_K_M)": 4.8, "Q5": 5.7, "Q8": 8.5, "FP16": 16}


def pesos_gb(bilhoes: float, bits: float) -> float:
    return bilhoes * bits / 8 * 1.05


def kv_gb(bilhoes: float, ctx: int) -> float:
    # aproximação: cache de contexto cresce com o tamanho do modelo; ~0,5 MB por token para 70B com GQA
    return ctx * 0.5e6 * (bilhoes / 70) ** 0.6 / 1e9


def rodar(bilhoes: float, ctx: int, ram: float, vram: float, ativos: float | None) -> list[dict]:
    out = []
    so_livre = ram - 6  # Windows + WSL + programas
    for nome, b in BITS.items():
        total = pesos_gb(bilhoes, b) + kv_gb(bilhoes, ctx) + 0.8
        if total <= vram:
            onde, vel = "inteiro na GPU", "rápido"
        elif total <= vram + so_livre:
            onde = f"GPU {vram:.0f} GB + RAM {total - vram:.1f} GB (offload)"
            base = ativos if ativos else bilhoes
            vel = "usável" if base <= 14 else "lento" if base <= 40 else "muito lento"
        else:
            onde, vel = "não cabe: GPU alugada, API ou cluster na rede", "—"
        out.append({"quant": nome, "gb": round(total, 1), "onde": onde, "velocidade": vel})
    return out


def qlora_gb(bilhoes: float) -> float:
    """Memória de GPU para fine-tuning QLoRA (4 bits + adaptadores + ativações), aproximada."""
    return bilhoes * 0.6 + 4


def parametros_hf(dados: dict) -> float:
    """Bilhões de parâmetros a partir da resposta da API do Hugging Face (safetensors ou GGUF)."""
    for chave in ("safetensors", "gguf"):
        total = (dados.get(chave) or {}).get("total")
        if isinstance(total, (int, float)) and total > 0:
            return total / 1e9
    raise ValueError("o repositório não informa o número de parâmetros (sem safetensors nem GGUF); passe o tamanho à mão")


def buscar_hf(repo: str, abrir=urllib.request.urlopen) -> dict:
    url = "https://huggingface.co/api/models/" + urllib.parse.quote(repo, safe="/")
    with abrir(url, timeout=20) as r:  # nosec - API pública do Hugging Face
        return json.loads(r.read().decode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("bilhoes", type=float, nargs="?")
    ap.add_argument("--hf", metavar="DONO/MODELO", help="lê o tamanho do modelo na API do Hugging Face")
    ap.add_argument("--ram", type=float, default=32)
    ap.add_argument("--vram", type=float, default=4)
    ap.add_argument("--ctx", type=int, default=8192)
    ap.add_argument("--ativos", type=float, help="parâmetros ativos por token (modelos MoE)")
    a = ap.parse_args()
    if a.hf:
        try:
            a.bilhoes = round(parametros_hf(buscar_hf(a.hf)), 2)
        except Exception as e:  # sem rede, repositório privado ou sem metadados
            print(f"ERRO: não consegui ler {a.hf} no Hugging Face: {e}", file=sys.stderr)
            return 1
        print(f"{a.hf}: {a.bilhoes:g} bilhões de parâmetros (API do Hugging Face)")
    if a.bilhoes is None:
        ap.error("diga o tamanho em bilhões ou use --hf DONO/MODELO")
    print(f"Modelo de {a.bilhoes:g}B · contexto {a.ctx} · máquina: {a.ram:g} GB RAM + {a.vram:g} GB GPU\n")
    print(f"{'Quantização':<18} {'Memória':>8}  Onde roda / velocidade")
    for r in rodar(a.bilhoes, a.ctx, a.ram, a.vram, a.ativos):
        print(f"{r['quant']:<18} {r['gb']:>6} GB  {r['onde']} · {r['velocidade']}")
    q = qlora_gb(a.bilhoes)
    gpu = "a sua GPU" if q <= a.vram else "T4 16 GB (Kaggle/Colab grátis)" if q <= 15 else "A100 40 GB alugada" if q <= 38 else "A100/H100 80 GB alugada" if q <= 78 else "várias GPUs alugadas"
    print(f"\nFine-tuning QLoRA: ~{q:.0f} GB de GPU → {gpu}")
    if a.vram <= 4:
        print("Aviso: a GTX 1650 não tem bfloat16. Treino que pede bf16 (ex.: SmolVLA) vai para GPU Ampere ou mais nova (L4, A10, RTX 30xx) alugada; o T4 do Kaggle também não tem bf16, mas treina em fp32 com mais memória.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
