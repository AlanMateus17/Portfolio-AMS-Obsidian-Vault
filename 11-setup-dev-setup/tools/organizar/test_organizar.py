import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from downloads import destino, plano  # noqa: E402
from senhas_csv import dominio, grupo, processar  # noqa: E402


class TestDownloads(unittest.TestCase):
    def test_tipos(self):
        self.assertEqual(destino(Path("a.PDF")), "Documentos")
        self.assertEqual(destino(Path("x.unknown")), "Outros")
        self.assertIsNone(destino(Path("Chrome Passwords.csv")))

    def test_simula_sem_mover_e_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p / "a.pdf").write_text("1")
            (p / "Documentos").mkdir()
            (p / "Documentos" / "a.pdf").write_text("antigo")
            mover, _ = plano(p)
            self.assertEqual(mover[0][1].name, "a (1).pdf")
            self.assertTrue((p / "a.pdf").exists())


class TestSenhas(unittest.TestCase):
    def test_dominio_e_grupo(self):
        self.assertEqual(dominio("https://www.github.com/login"), "github.com")
        self.assertEqual(grupo("nubank.com.br"), "Bancos e dinheiro")

    def test_relatorio_sem_senhas(self):
        linhas = [{"titulo": "a.com", "usuario": "u", "senha": "123", "url": "", "nota": ""},
                  {"titulo": "b.com", "usuario": "u", "senha": "123", "url": "", "nota": ""},
                  {"titulo": "a.com", "usuario": "u", "senha": "123", "url": "", "nota": ""}]
        unicas, rel = processar(linhas)
        self.assertEqual(len(unicas), 2)
        self.assertEqual(rel["repetidas"], ["a.com", "b.com"])
        self.assertNotIn("123", str(rel))


if __name__ == "__main__":
    unittest.main()
