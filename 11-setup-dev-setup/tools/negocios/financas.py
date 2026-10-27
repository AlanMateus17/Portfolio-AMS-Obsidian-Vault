#!/usr/bin/env python3
"""Motor financeiro dos negócios do grupo.

Calcula, para cada negócio de data/negocios.json:
- Simples Nacional por fonte de receita (cada fonte no seu anexo, faixa pela receita total);
- margem de contribuição por fonte e do negócio;
- ponto de equilíbrio mensal;
- rampa de abertura mês a mês, pior caixa acumulado e mês de retorno;
- capital mínimo para abrir com segurança.

As mesmas fórmulas rodam no Planejador do Grupo (artefato) para os números baterem.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]

# Simples Nacional 2026: (limite superior da faixa, alíquota nominal, parcela a deduzir)
ANEXOS: dict[str, list[tuple[float, float, float]]] = {
    "I": [(180_000, 0.04, 0), (360_000, 0.073, 5_940), (720_000, 0.095, 13_860),
          (1_800_000, 0.107, 22_500), (3_600_000, 0.143, 87_300), (4_800_000, 0.19, 378_000)],
    "II": [(180_000, 0.045, 0), (360_000, 0.078, 5_940), (720_000, 0.10, 13_860),
           (1_800_000, 0.112, 22_500), (3_600_000, 0.147, 85_500), (4_800_000, 0.30, 720_000)],
    "III": [(180_000, 0.06, 0), (360_000, 0.112, 9_360), (720_000, 0.135, 17_640),
            (1_800_000, 0.16, 35_640), (3_600_000, 0.21, 125_640), (4_800_000, 0.33, 648_000)],
    "V": [(180_000, 0.155, 0), (360_000, 0.18, 4_500), (720_000, 0.195, 9_900),
          (1_800_000, 0.205, 17_100), (3_600_000, 0.23, 62_100), (4_800_000, 0.305, 540_000)],
}
LIMITE_SIMPLES = 4_800_000
FATOR_R = 0.28


def aliquota_efetiva(anexo: str, rbt12: float) -> float:
    """Alíquota efetiva do Simples para a receita bruta dos últimos 12 meses."""
    if rbt12 <= 0:
        return ANEXOS[anexo][0][1]
    for limite, nominal, deduzir in ANEXOS[anexo]:
        if rbt12 <= limite:
            return (rbt12 * nominal - deduzir) / rbt12
    limite, nominal, deduzir = ANEXOS[anexo][-1]
    return (rbt12 * nominal - deduzir) / rbt12  # acima do limite: sai do Simples (sinalizado em alertas)


@dataclass
class Fonte:
    nome: str
    qtd: float
    ticket: float
    variavel: float  # fração da receita da fonte que é custo variável (CMV, comissão, entregador, cartão...)
    anexo: str       # "I", "II", "III", "V" ou "III/V" (Fator R)

    @property
    def receita(self) -> float:
        return self.qtd * self.ticket


@dataclass
class Negocio:
    id: str
    nome: str
    cluster: str
    investimento: list[dict]
    fixos: list[dict]
    equipe: list[dict]
    fontes: list[Fonte]
    rampa_meses: int
    rampa_inicio: float
    encargos: float
    reserva_meses: float
    prolabore: float = 0.0
    alertas: list[str] = field(default_factory=list)

    # ---------------- custos
    @property
    def total_investimento(self) -> float:
        return sum(i["valor"] for i in self.investimento)

    @property
    def folha(self) -> float:
        """Custo mensal da equipe CLT (salário × fator de encargos) mais o pró-labore."""
        return sum(p["salario"] * p.get("qtd", 1) * self.encargos for p in self.equipe) + self.prolabore

    @property
    def total_fixos(self) -> float:
        return sum(f["valor"] for f in self.fixos) + self.folha

    # ---------------- receita e imposto em um nível de atividade (fator 0..1 do alvo)
    def anexo_de(self, fonte: Fonte, receita_total: float) -> str:
        if fonte.anexo != "III/V":
            return fonte.anexo
        folha_salarial = sum(p["salario"] * p.get("qtd", 1) for p in self.equipe) + self.prolabore
        return "III" if receita_total > 0 and folha_salarial / receita_total >= FATOR_R else "V"

    def resultado(self, fator: float = 1.0, rbt12: float | None = None) -> dict:
        receitas = [f.receita * fator for f in self.fontes]
        total = sum(receitas)
        base = total * 12 if rbt12 is None else rbt12
        linhas = []
        imposto = variavel = 0.0
        for f, r in zip(self.fontes, receitas):
            anexo = self.anexo_de(f, total)
            t = aliquota_efetiva(anexo, base) * r
            v = f.variavel * r
            imposto += t
            variavel += v
            linhas.append({"fonte": f.nome, "receita": r, "variavel": v, "imposto": t,
                           "anexo": anexo, "mc": r - v - t})
        mc = total - variavel - imposto
        return {"receita": total, "variavel": variavel, "imposto": imposto, "mc": mc,
                "fixos": self.total_fixos, "lucro": mc - self.total_fixos, "linhas": linhas}

    def ponto_de_equilibrio(self) -> float | None:
        """Receita mensal (no mesmo mix de fontes) em que o lucro é zero. None se nunca empata."""
        alvo = self.resultado(1.0)["receita"]
        if alvo <= 0:
            return None
        lo, hi = 0.0, 20.0
        if self.resultado(hi)["lucro"] < 0:
            return None
        for _ in range(80):
            meio = (lo + hi) / 2
            if self.resultado(meio)["lucro"] < 0:
                lo = meio
            else:
                hi = meio
        return hi * alvo

    # ---------------- rampa de abertura
    def fator_mes(self, m: int) -> float:
        if self.rampa_meses <= 1 or m >= self.rampa_meses:
            return 1.0
        return self.rampa_inicio + (1 - self.rampa_inicio) * (m - 1) / (self.rampa_meses - 1)

    def rampa(self, meses: int = 36) -> list[dict]:
        caixa = -self.total_investimento
        historico: list[float] = []
        out = []
        for m in range(1, meses + 1):
            fator = self.fator_mes(m)
            receita_mes = sum(f.receita for f in self.fontes) * fator
            historico.append(receita_mes)
            # LC 123: empresa em início de atividade usa a média dos meses já vividos × 12
            janela = historico[-12:]
            rbt12 = sum(janela) / len(janela) * 12
            r = self.resultado(fator, rbt12)
            caixa += r["lucro"]
            out.append({"mes": m, "fator": fator, "receita": r["receita"], "lucro": r["lucro"], "caixa": caixa})
        return out

    def resumo(self) -> dict:
        r = self.resultado(1.0)
        ramp = self.rampa()
        pior = min([-self.total_investimento] + [x["caixa"] for x in ramp])
        retorno = next((x["mes"] for x in ramp if x["caixa"] >= 0), None)
        reserva = self.reserva_meses * self.total_fixos
        perdas_rampa = max(0.0, -(pior + self.total_investimento))
        pe = self.ponto_de_equilibrio()
        alertas = list(self.alertas)
        if r["receita"] * 12 > LIMITE_SIMPLES:
            alertas.append("Receita anual acima do limite do Simples (R$ 4,8 milhões).")
        return {
            "id": self.id, "nome": self.nome, "cluster": self.cluster,
            "investimento": self.total_investimento, "fixos": self.total_fixos, "folha": self.folha,
            "receita": r["receita"], "variavel": r["variavel"], "imposto": r["imposto"],
            "mc": r["mc"], "mc_pct": r["mc"] / r["receita"] if r["receita"] else 0,
            "lucro": r["lucro"], "lucro_70": self.resultado(0.7)["lucro"], "margem": r["lucro"] / r["receita"] if r["receita"] else 0,
            "ponto_equilibrio": pe, "pe_pct": (pe / r["receita"]) if pe and r["receita"] else None,
            "pior_caixa": pior, "perdas_rampa": perdas_rampa, "mes_retorno": retorno,
            "reserva": reserva, "capital_minimo": self.total_investimento + perdas_rampa + reserva,
            "linhas": r["linhas"], "rampa": ramp, "alertas": alertas,
        }


def carregar(caminho: Path | None = None) -> tuple[dict, list[Negocio]]:
    dados = json.loads((caminho or RAIZ / "data" / "negocios.json").read_text(encoding="utf-8"))
    p = dados["premissas"]
    negocios = []
    for n in dados["negocios"]:
        negocios.append(Negocio(
            id=n["id"], nome=n["nome"], cluster=n["cluster"],
            investimento=n["investimento"], fixos=n["fixos"], equipe=n.get("equipe", []),
            fontes=[Fonte(**f) for f in n["fontes"]],
            rampa_meses=n.get("rampa_meses", p["rampa_meses"]),
            rampa_inicio=n.get("rampa_inicio", p["rampa_inicio"]),
            encargos=p["encargos"], reserva_meses=p["reserva_meses"],
            prolabore=n.get("prolabore", 0.0), alertas=n.get("alertas", []),
        ))
    return dados, negocios


if __name__ == "__main__":
    _, ns = carregar()
    for n in ns:
        s = n.resumo()
        print(f"{s['nome'][:38]:38} inv {s['investimento']:>9,.0f}  rec {s['receita']:>9,.0f}  "
              f"lucro {s['lucro']:>8,.0f} ({s['margem']:.0%})  PE {s['ponto_equilibrio'] or 0:>9,.0f}  "
              f"retorno {s['mes_retorno']}  capital {s['capital_minimo']:>9,.0f}")
