import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import coerencia  # noqa: E402


class TestCoerencia(unittest.TestCase):
    def setUp(self):
        self.d = coerencia.carregar()

    def test_dev_setup_sem_erro(self):
        erros = [a for a in coerencia.verificar(coerencia.RAIZ, self.d) if a.nivel == "erro"]
        self.assertEqual(erros, [], "rode: python3 tools/coerencia/coerencia.py")

    def test_acha_e_corrige(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "nota.md"
            p.write_text("O AM Rendara vem primeiro.\nAbrir um sushi no centro.\nFui sushiman.\n", encoding="utf-8")
            a = coerencia.verificar(Path(t), self.d)
            self.assertEqual({x.regra for x in a}, {"rendara", "restaurante-proprio"})
            coerencia.verificar(Path(t), self.d, corrigir=True)
            txt = p.read_text(encoding="utf-8")
            self.assertIn("AM Gestão · Financeiro", txt)
            self.assertIn("sushi no centro", txt, "sem troca segura: fica para revisão")
            self.assertIn("sushiman", txt)

    def test_ignora_historico(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "docs" / "adr").mkdir(parents=True)
            (Path(t) / "docs" / "adr" / "0001.md").write_text("AM Rendara", encoding="utf-8")
            (Path(t) / "CHANGELOG.md").write_text("AM Rendara", encoding="utf-8")
            self.assertEqual(coerencia.verificar(Path(t), self.d), [])

    def test_linha_que_explica_o_que_saiu(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "a.md").write_text("Restaurantes saíram do plano: sushi e padaria.", encoding="utf-8")
            self.assertEqual(coerencia.verificar(Path(t), self.d), [])

    def test_glob(self):
        self.assertTrue(coerencia.casa("x/99-arquivo/a.md", ["**/99-arquivo/**"]))
        self.assertTrue(coerencia.casa("docs/adr/0001.md", ["docs/adr/**"]))
        self.assertFalse(coerencia.casa("docs/adrx.md", ["docs/adr/**"]))


if __name__ == "__main__":
    unittest.main()
