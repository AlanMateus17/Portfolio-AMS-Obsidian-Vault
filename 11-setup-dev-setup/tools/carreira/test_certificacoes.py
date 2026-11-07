import copy
import unittest

import certificacoes as c


class TesteCertificacoes(unittest.TestCase):
    def setUp(self):
        self.d = c.carregar()

    def test_dados_validos(self):
        self.assertEqual(c.validar(self.d), [])

    def test_ordem_repetida(self):
        d = copy.deepcopy(self.d)
        d["trilhas"][0]["itens"][1]["ordem"] = d["trilhas"][0]["itens"][0]["ordem"]
        self.assertTrue(any("ordem repetida" in x for x in c.validar(d)))

    def test_sem_az204_na_fila(self):
        nomes = [i["nome"] for t in self.d["trilhas"] for i in t["itens"]]
        self.assertFalse(any(n.startswith("AZ-204") for n in nomes))

    def test_gera(self):
        self.assertIn("| Ordem | Certificação |", c.gerar(self.d))


if __name__ == "__main__":
    unittest.main()
