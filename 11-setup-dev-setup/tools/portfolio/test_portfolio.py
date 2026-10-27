import copy
import unittest

from portfolio import carregar, pontuar, ranking, validar


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.dados = carregar()

    def test_formula(self):
        self.assertEqual(pontuar({"sinergia": 5, "escala": 5, "demanda": 5, "esforco": 1, "capital": 1}), 18)
        self.assertEqual(pontuar({"sinergia": 1, "escala": 1, "demanda": 1, "esforco": 5, "capital": 5}), -6)

    def test_dados_reais_validos(self):
        self.assertEqual(validar(self.dados), [])

    def test_ranking_ordenado(self):
        pts = [o["pontos"] for o in ranking(self.dados)]
        self.assertEqual(pts, sorted(pts, reverse=True))

    def test_detecta_derivacao_quebrada(self):
        d = copy.deepcopy(self.dados)
        d["ofertas"][0]["deriva_de"] = ["nao-existe"]
        self.assertTrue(any("inexistente" in e for e in validar(d)))

    def test_detecta_nota_fora_da_faixa(self):
        d = copy.deepcopy(self.dados)
        d["ofertas"][0]["nota"]["demanda"] = 7
        self.assertTrue(any("1 a 5" in e for e in validar(d)))

    def test_toda_oferta_tem_proximo_passo_e_metrica(self):
        for o in self.dados["ofertas"]:
            self.assertTrue(o["proximo_passo"].strip(), o["id"])
            self.assertTrue(o["metrica"].strip(), o["id"])


if __name__ == "__main__":
    unittest.main()
