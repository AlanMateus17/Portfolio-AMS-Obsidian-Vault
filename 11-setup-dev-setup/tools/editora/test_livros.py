import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import livros  # noqa: E402


class TestLivros(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(livros.DADOS.read_text(encoding="utf-8"))
        self.a = json.loads(livros.MAPA.read_text(encoding="utf-8"))["assuntos"]
        self.o = {x["id"] for x in json.loads(livros.PORTFOLIO.read_text(encoding="utf-8"))["ofertas"]}

    def test_dados_reais_validos(self):
        self.assertEqual(livros.validar(self.d, self.a, self.o), [])

    def test_assunto_inexistente(self):
        d = copy.deepcopy(self.d)
        d["livros"][0]["volumes"][0]["capitulos"].append({"assunto": "9.99"})
        self.assertTrue(any("não existe" in e for e in livros.validar(d, self.a, self.o)))

    def test_assunto_em_dois_volumes(self):
        d = copy.deepcopy(self.d)
        d["livros"][0]["volumes"][1]["capitulos"].append({"assunto": "0.2"})
        self.assertTrue(any("dois volumes" in e for e in livros.validar(d, self.a, self.o)))

    def test_capitulo_1_escrito(self):
        c = self.d["livros"][0]["volumes"][0]["capitulos"][0]
        self.assertEqual((c["assunto"], c["estado"]), ("0.2", "escrito"))


if __name__ == "__main__":
    unittest.main()
