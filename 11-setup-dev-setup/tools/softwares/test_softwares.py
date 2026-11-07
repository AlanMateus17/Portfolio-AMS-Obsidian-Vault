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


if __name__ == "__main__":
    unittest.main()
