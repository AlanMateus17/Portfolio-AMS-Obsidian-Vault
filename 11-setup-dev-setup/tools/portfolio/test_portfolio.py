import copy
import unittest

from portfolio import carregar, facilidade, pontuar, ranking, validar


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

    def test_facilidade(self):
        self.assertEqual(facilidade({"sinergia": 5, "escala": 1, "demanda": 5, "esforco": 1, "capital": 1}), 20)
        self.assertEqual(facilidade({"sinergia": 1, "escala": 5, "demanda": 1, "esforco": 5, "capital": 5}), 4)

    def test_limite_de_rendas_agora(self):
        d = copy.deepcopy(self.dados)
        for o in d["ofertas"]:
            o["veredito"] = "agora"
        self.assertTrue(any("máximo" in e for e in validar(d)))

    def test_veredito_sem_motivo(self):
        d = copy.deepcopy(self.dados)
        d["ofertas"][0]["motivo"] = " "
        self.assertTrue(any("motivo" in e for e in validar(d)))

    def test_proxima_com_ordem_unica(self):
        d = copy.deepcopy(self.dados)
        prox = [o for o in d["ofertas"] if o["veredito"] == "proxima"]
        prox[1]["ordem"] = prox[0]["ordem"]
        self.assertTrue(any("ordem" in e for e in validar(d)))

    def test_automacao_inexistente(self):
        d = copy.deepcopy(self.dados)
        d["ofertas"][0]["usa"] = ["nao-existe"]
        self.assertTrue(any("inexistente" in e for e in validar(d)))

    def test_passiva_precisa_de_automacao(self):
        d = copy.deepcopy(self.dados)
        o = next(x for x in d["ofertas"] if x["perfil"] == "passiva")
        o["usa"] = []
        self.assertTrue(any("passiva sem" in e for e in validar(d)))

    def test_automacao_a_construir_tem_passo(self):
        d = copy.deepcopy(self.dados)
        a = next(x for x in d["automacoes"] if x["estado"] == "construir")
        a["passo"] = None
        self.assertTrue(any("falta o passo" in e for e in validar(d)))

    def test_toda_oferta_tem_proximo_passo_e_metrica(self):
        for o in self.dados["ofertas"]:
            self.assertTrue(o["proximo_passo"].strip(), o["id"])
            self.assertTrue(o["metrica"].strip(), o["id"])


if __name__ == "__main__":
    unittest.main()
