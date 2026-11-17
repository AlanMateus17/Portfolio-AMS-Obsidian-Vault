import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import registro  # noqa: E402


class TestRegistro(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["AMTECH_VAULT"] = self.tmp.name

    def tearDown(self):
        os.environ.pop("AMTECH_VAULT", None)
        self.tmp.cleanup()

    def test_erro_vai_para_o_caderno(self):
        arq = registro.erro("0.2", "neguei 'todos são' como 'todos não são'", "algum não é", date(2026, 11, 20))
        self.assertTrue(arq.name == "caderno-de-erros.md")
        ls = registro.linhas(arq)
        self.assertEqual(ls[0], ["2026-11-20", "0.2", "neguei 'todos são' como 'todos não são'", "algum não é"])

    def test_barra_vertical_nao_quebra_tabela(self):
        arq = registro.erro("0.2", "a || b", "a ou b", date(2026, 11, 20))
        self.assertEqual(len(registro.linhas(arq)[0]), 4)

    def test_texto_longo_recusado(self):
        with self.assertRaises(SystemExit):
            registro.erro("0.2", "x" * (registro.LIMITE + 1), "certo")

    def test_atritos_repetidos_somam(self):
        for _ in range(3):
            registro.atrito("Conferir o backup à mão", "backup")
        registro.atrito("abrir o WSL", "wsl")
        resumo = registro.resumo_atritos()
        self.assertEqual(resumo[0], ("backup: conferir o backup à mão", 3))


if __name__ == "__main__":
    unittest.main()
