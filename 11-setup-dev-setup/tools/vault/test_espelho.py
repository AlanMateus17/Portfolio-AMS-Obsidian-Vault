import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import espelho  # noqa: E402


class TestEspelho(unittest.TestCase):
    def test_copia_atualiza_e_remove(self):
        with tempfile.TemporaryDirectory() as t:
            o, d = Path(t) / "o", Path(t) / "d"
            (o / "docs").mkdir(parents=True)
            (o / "docs" / "a.md").write_text("A")
            (o / "b.md").write_text("B")
            (d / "velho").mkdir(parents=True)
            (d / "velho" / "x.ps1").write_text("parado em 27/10")
            (d / "b.md").write_text("antigo")
            n = espelho.espelhar(o, d, ["docs/a.md", "b.md"], simular=True)
            self.assertEqual(n, {"novo": 1, "mudou": 1, "saiu": 1})
            self.assertTrue((d / "velho" / "x.ps1").exists(), "simular não muda nada")
            espelho.espelhar(o, d, ["docs/a.md", "b.md"])
            self.assertEqual((d / "b.md").read_text(), "B")
            self.assertFalse((d / "velho").exists())
            self.assertIn("Espelho automático", (d / espelho.INDICE).read_text())
            self.assertEqual(espelho.espelhar(o, d, ["docs/a.md", "b.md"]), {"novo": 0, "mudou": 0, "saiu": 0})

    def test_so_espelha_no_vault(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertFalse(espelho.eh_vault(Path(t)))
            (Path(t) / "00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md").write_text("x")
            self.assertTrue(espelho.eh_vault(Path(t)))

    def test_lista_real_sem_github(self):
        lista = espelho.arquivos()
        self.assertIn("justfile", lista)
        self.assertFalse(any(f.startswith(".github/") for f in lista))


if __name__ == "__main__":
    unittest.main()
