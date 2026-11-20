import copy
import unittest

from softwares import carregar, ordem_modulos, validar


class TestSoftwares(unittest.TestCase):
    def setUp(self):
        self.d = carregar()

    def test_dados_reais_validos(self):
        self.assertEqual(validar(self.d), [])

    def test_modulo_inexistente(self):
        d = copy.deepcopy(self.d)
        d["softwares"][0]["modulos"].append("nao-existe")
        self.assertTrue(any("inexistente" in e for e in validar(d)))

    def test_oferta_inexistente(self):
        d = copy.deepcopy(self.d)
        s = next(x for x in d["softwares"] if x["vende"])
        s["oferta"] = "nao-existe"
        self.assertTrue(any("não existe no portfólio" in e for e in validar(d)))

    def test_modulo_sem_uso(self):
        d = copy.deepcopy(self.d)
        d["modulos"].append({"id": "orfao", "nome": "Órfão", "faz": "nada"})
        self.assertTrue(any("orfao" in e for e in validar(d)))

    def test_ordem_por_vendaveis(self):
        v = [t[2] for t in ordem_modulos(self.d)]
        self.assertEqual(v, sorted(v, reverse=True))

    def test_am_gestao_e_a_suite_1_com_o_mvp(self):
        su = next(x for x in self.d["suites"] if x["ordem"] == 1)
        self.assertEqual(su["id"], "am-gestao")
        self.assertEqual(su["mvp"], ["am-kaixara", "am-rotara", "am-rendara"])

    def test_suite_com_menos_de_3_sistemas(self):
        d = copy.deepcopy(self.d)
        d["suites"][1]["sistemas"] = d["suites"][1]["sistemas"][:2]
        self.assertTrue(any("3 ou mais" in e for e in validar(d)))

    def test_sistema_em_duas_suites(self):
        d = copy.deepcopy(self.d)
        d["suites"][1]["sistemas"].append("am-kaixara")
        self.assertTrue(any("duas suítes" in e for e in validar(d)))

    def test_pacote_com_sistema_de_fora(self):
        d = copy.deepcopy(self.d)
        d["suites"][0]["pacotes"][0]["sistemas"].append("am-taskoro")
        self.assertTrue(any("não é da suíte" in e for e in validar(d)))

    def test_sistema_sem_suite(self):
        d = copy.deepcopy(self.d)
        d["fora_das_suites"].pop("am-vynla")
        self.assertTrue(any("sem suíte" in e for e in validar(d)))


if __name__ == "__main__":
    unittest.main()
