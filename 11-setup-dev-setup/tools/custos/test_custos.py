import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from custos import carregar, gerar, validar  # noqa: E402


class TestCustos(unittest.TestCase):
    def test_validos(self):
        d, eco = carregar()
        self.assertEqual(validar(d, eco), [])

    def test_bloco_inexistente(self):
        d, eco = carregar()
        d = copy.deepcopy(d)
        d["itens"][0]["bloco"] = "nao-existe"
        self.assertTrue(validar(d, eco))

    def test_claude_principal_e_rotas(self):
        d, _ = carregar()
        nomes = {i["item"]: i["decisao"] for i in d["itens"]}
        self.assertEqual(nomes["Claude (assinatura)"], "manter")
        self.assertIn("Claude (Pro)", [r["ia"] for r in d["rotas_ia"]])

    def test_gera(self):
        d, _ = carregar()
        self.assertIn("Modelos abertos", gerar(d))


if __name__ == "__main__":
    unittest.main()
