"""Confere se os números escritos à mão nos documentos batem com o motor financeiro e o portfólio.

Se um dado em data/negocios.json ou data/portfolio.json mudar, este teste aponta qual texto ficou velho.
"""
import json
import unittest

from financas import RAIZ, carregar

DOCS = RAIZ / "docs"


def mil(v: float) -> str:
    return f"R$ {v / 1000:,.1f} mil".replace(",", "X").replace(".", ",").replace("X", ".")


def ler(rel: str) -> str:
    return (DOCS / rel).read_text(encoding="utf-8")


class TestCoerencia(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _, ns = carregar()
        cls.n = {x.id: x for x in ns}
        cls.s = {x.id: x.resumo() for x in ns}

    def assertNoTexto(self, rel, trecho):
        self.assertIn(trecho, ler(rel), f"{rel} deveria conter {trecho!r}")

    def test_capital_por_fase(self):
        s = self.s
        doc = "negocios/00-estrutura-e-ordem.md"
        self.assertNoTexto(doc, mil(s["software"]["capital_minimo"]))
        self.assertNoTexto(doc, mil(s["loja"]["capital_minimo"] + s["produtos"]["capital_minimo"]))
        for i in ("entregas", "delivery", "sushi", "padaria", "cafeteria"):
            self.assertNoTexto(doc, mil(s[i]["capital_minimo"]))

    def test_capital_total(self):
        total = sum(x["capital_minimo"] for x in self.s.values())
        self.assertNoTexto("negocios/README.md", f"R$ {round(total / 1000)} mil")

    def test_receita_anual_do_grupo(self):
        ano = sum(x["receita"] for x in self.s.values()) * 12
        comida = sum(self.s[i]["receita"] for i in ("sushi", "cafeteria", "padaria")) * 12
        doc = "negocios/00-estrutura-e-ordem.md"
        self.assertNoTexto(doc, f"R$ {ano / 1e6:.1f} milhões".replace(".", ","))
        self.assertNoTexto(doc, f"R$ {round(comida / 1e6)} milhões")

    def test_cafeteria_investimento(self):
        self.assertNoTexto("negocios/08-cafeteria.md", mil(self.s["cafeteria"]["investimento"]))

    def test_sushi_margem_por_canal(self):
        linhas = {l["fonte"].split(" (")[0]: l for l in self.s["sushi"]["linhas"]}
        proprio = linhas["Delivery próprio"]["mc"] / linhas["Delivery próprio"]["receita"]
        ifood = linhas["iFood"]["mc"] / linhas["iFood"]["receita"]
        self.assertNoTexto("negocios/07-sushi.md", f"{round(proprio * 100)} centavos")
        self.assertNoTexto("negocios/07-sushi.md", f"{round(ifood * 100)} centavos")
        sem_voce = self.s["sushi"]["lucro"] - 3000 * 1.4
        self.assertNoTexto("negocios/07-sushi.md", f"R$ {round(sem_voce / 1000)} mil")

    def test_loja_servicos(self):
        s = self.s["loja"]
        serv = s["linhas"][0]
        self.assertNoTexto("negocios/02-assistencia-e-pecas.md",
                           f"{round(serv['receita'] / s['receita'] * 100)}% da receita e {round(serv['mc'] / s['mc'] * 100)}% da margem")

    def test_ponto_de_retirada(self):
        pacotes = sum(l["receita"] for l in self.s["loja"]["linhas"] if "retirada" in l["fonte"] or "Agência" in l["fonte"])
        self.assertNoTexto("negocios/04-ponto-de-retirada.md", f"R$ {round(pacotes, -1):,.0f}".replace(",", "."))

    def test_padaria_aliquota_e_equipe(self):
        s = self.s["padaria"]
        self.assertNoTexto("negocios/09-padaria-e-almoco.md", f"{s['imposto'] / s['receita'] * 100:.1f}%".replace(".", ","))
        pessoas = sum(e.get("qtd", 1) for e in self.n["padaria"].equipe)
        self.assertNoTexto("negocios/09-padaria-e-almoco.md", f"{pessoas} pessoas")

    def test_contagens_do_portfolio(self):
        p = json.loads((RAIZ / "data" / "portfolio.json").read_text(encoding="utf-8"))
        total = len(p["ofertas"])
        novas = sum(o["nova"] for o in p["ofertas"])
        self.assertNoTexto("operacao/README.md", f"{total} ofertas")
        self.assertNoTexto("operacao/07-ordem-de-execucao.md", f"{total} ofertas")
        self.assertIn(f"{total} ofertas", (RAIZ / "README.md").read_text(encoding="utf-8"))
        self.assertNoTexto("operacao/portfolio.md", f"{novas} fontes de renda novas")


if __name__ == "__main__":
    unittest.main()
