import unittest

from financas import Fonte, Negocio, aliquota_efetiva, carregar


def negocio(**kw):
    base = dict(id="t", nome="Teste", cluster="A", investimento=[{"item": "x", "valor": 10_000}],
                fixos=[{"item": "aluguel", "valor": 2_000}], equipe=[],
                fontes=[Fonte("venda", 100, 50, 0.4, "I")], rampa_meses=1, rampa_inicio=1.0,
                encargos=1.4, reserva_meses=3)
    base.update(kw)
    return Negocio(**base)


class TestSimples(unittest.TestCase):
    def test_primeira_faixa_e_a_nominal(self):
        self.assertAlmostEqual(aliquota_efetiva("I", 100_000), 0.04)
        self.assertAlmostEqual(aliquota_efetiva("III", 180_000), 0.06)

    def test_faixas_seguintes_usam_parcela_a_deduzir(self):
        # Anexo I, 2ª faixa: (300.000 × 7,3% − 5.940) / 300.000 = 5,32%
        self.assertAlmostEqual(aliquota_efetiva("I", 300_000), 0.0532)
        # Anexo III, 4ª faixa: (1.000.000 × 16% − 35.640) / 1.000.000
        self.assertAlmostEqual(aliquota_efetiva("III", 1_000_000), 0.12436)

    def test_continuidade_na_virada_de_faixa(self):
        for anexo in ("I", "II", "III", "V"):
            a = aliquota_efetiva(anexo, 180_000)
            b = aliquota_efetiva(anexo, 180_000.01)
            self.assertAlmostEqual(a, b, places=4)


class TestNegocio(unittest.TestCase):
    def test_resultado_basico(self):
        n = negocio()
        r = n.resultado()
        self.assertEqual(r["receita"], 5_000)
        self.assertAlmostEqual(r["variavel"], 2_000)
        self.assertAlmostEqual(r["imposto"], 200)  # 4% (RBT12 = 60 mil)
        self.assertAlmostEqual(r["lucro"], 5_000 - 2_000 - 200 - 2_000)

    def test_encargos_da_equipe(self):
        n = negocio(equipe=[{"cargo": "a", "salario": 2_000, "qtd": 2}])
        self.assertAlmostEqual(n.folha, 5_600)
        self.assertAlmostEqual(n.total_fixos, 7_600)

    def test_ponto_de_equilibrio_zera_o_lucro(self):
        n = negocio()
        pe = n.ponto_de_equilibrio()
        self.assertAlmostEqual(n.resultado(pe / 5_000)["lucro"], 0, delta=0.01)
        self.assertAlmostEqual(pe, 2_000 / (1 - 0.4 - 0.04), delta=0.5)

    def test_sem_equilibrio_quando_a_margem_e_negativa(self):
        n = negocio(fontes=[Fonte("venda", 100, 50, 0.99, "I")])
        self.assertIsNone(n.ponto_de_equilibrio())

    def test_fator_r_decide_entre_anexo_iii_e_v(self):
        fontes = [Fonte("dev", 1, 10_000, 0, "III/V")]
        self.assertEqual(negocio(fontes=fontes, prolabore=2_800).resultado()["linhas"][0]["anexo"], "III")
        self.assertEqual(negocio(fontes=fontes, prolabore=2_700).resultado()["linhas"][0]["anexo"], "V")

    def test_rampa_linear(self):
        n = negocio(rampa_meses=5, rampa_inicio=0.2)
        self.assertAlmostEqual(n.fator_mes(1), 0.2)
        self.assertAlmostEqual(n.fator_mes(3), 0.6)
        self.assertAlmostEqual(n.fator_mes(5), 1.0)
        self.assertAlmostEqual(n.fator_mes(9), 1.0)

    def test_capital_minimo_soma_investimento_perdas_e_reserva(self):
        n = negocio(rampa_meses=4, rampa_inicio=0.1)
        s = n.resumo()
        self.assertGreater(s["perdas_rampa"], 0)
        self.assertAlmostEqual(s["capital_minimo"], 10_000 + s["perdas_rampa"] + 3 * 2_000)

    def test_dados_reais_carregam_e_fecham(self):
        dados, ns = carregar()
        ids = [n.id for n in ns]
        self.assertEqual(len(ids), len(set(ids)))
        for n in ns:
            s = n.resumo()
            self.assertGreater(s["receita"], 0, n.id)
            self.assertIsNotNone(s["ponto_equilibrio"], n.id)
            self.assertLess(s["ponto_equilibrio"], s["receita"], n.id)
            soma = sum(l["mc"] for l in s["linhas"])
            self.assertAlmostEqual(soma, s["mc"], places=6)
            for f in n.fontes:
                self.assertTrue(0 <= f.variavel < 1, f"{n.id}: {f.nome}")


if __name__ == "__main__":
    unittest.main()
