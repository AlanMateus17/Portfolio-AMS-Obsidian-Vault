import copy
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import repos  # noqa: E402


class TestRepos(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(repos.DADOS.read_text(encoding="utf-8"))

    def test_dados_reais_validos(self):
        self.assertEqual(repos.validar(self.d), [])

    def test_status_invalido(self):
        d = copy.deepcopy(self.d)
        d["repos"][0]["status"] = "talvez"
        self.assertTrue(repos.validar(d))

    def test_link_de_outra_organizacao(self):
        self.assertIn("https://github.com/Cursos-TI/x", repos.link("Cursos-TI/x"))
        self.assertIn("https://github.com/AlanMateus17/dev-setup", repos.link("dev-setup"))

    def test_empresa_invalida(self):
        d = copy.deepcopy(self.d)
        d["repos"][0]["empresa"] = "restaurante"
        self.assertTrue(repos.validar(d))

    def test_todo_repo_aparece(self):
        txt = repos.gerar(self.d)
        for r in self.d["repos"]:
            self.assertIn(r["nome"].split("/")[-1], txt)


if __name__ == "__main__":
    unittest.main()
