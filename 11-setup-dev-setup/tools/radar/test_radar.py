import sys
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from radar import avaliar  # noqa: E402

CFG = tomllib.loads((Path(__file__).parent / "radar.example.toml").read_text(encoding="utf-8"))


class TestRadar(unittest.TestCase):
    def test_aprova_bom_negocio(self):
        r = avaliar({"titulo": "Notebook Lenovo ThinkPad T480 i5", "preco": "800"}, CFG)
        self.assertTrue(r["aprovado"], r)
        self.assertGreaterEqual(r["lucro_hora"], 45)

    def test_recusa_abaixo_da_hora_minima(self):
        r = avaliar({"titulo": "ThinkPad T480", "preco": "1150"}, CFG)
        self.assertFalse(r["aprovado"])

    def test_recusa_sinal_de_golpe(self):
        r = avaliar({"titulo": "iPhone 11 bloqueado icloud", "preco": "700"}, CFG)
        self.assertFalse(r["aprovado"])
        self.assertTrue(r["sinais"])

    def test_preco_baixo_demais(self):
        r = avaliar({"titulo": "ThinkPad T480", "preco": "300"}, CFG)
        self.assertFalse(r["aprovado"])
        self.assertIn("baixo demais", r["motivo"])

    def test_sem_referencia(self):
        r = avaliar({"titulo": "Geladeira", "preco": "500"}, CFG)
        self.assertFalse(r["aprovado"])


if __name__ == "__main__":
    unittest.main()
