import copy
import unittest

from gerar_docs import carregar, validar


class TestEcossistema(unittest.TestCase):
    def setUp(self):
        self.eco, _ = carregar()

    def test_dados_reais_validos(self):
        self.assertEqual(validar(self.eco), [])

    def test_detecta_bloco_isolado(self):
        eco = copy.deepcopy(self.eco)
        eco["blocos"].append({"id": "solto", "camada": "win", "rotulo": "Solto", "tipo": "local",
                              "conta": False, "futuro": False, "descricao": "x"})
        self.assertTrue(any("solto" in e and "sem nenhuma conexão" in e for e in validar(eco)))

    def test_detecta_conexao_nos_dois_sentidos(self):
        eco = copy.deepcopy(self.eco)
        c = eco["conexoes"][0]
        eco["conexoes"].append({"de": c["para"], "para": c["de"], "rotulo": "volta"})
        self.assertTrue(any("dois sentidos" in e for e in validar(eco)))

    def test_detecta_fluxo_com_passo_sem_conexao(self):
        eco = copy.deepcopy(self.eco)
        eco["fluxos"][0]["passos"].append({"bloco": "ups", "descricao": "x"})
        self.assertTrue(any("não tem conexão" in e for e in validar(eco)))


if __name__ == "__main__":
    unittest.main()
