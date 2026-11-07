import sys
import tomllib
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from roi import calcular, relatorio  # noqa: E402

CFG = tomllib.loads((Path(__file__).parent / "roi.example.toml").read_text(encoding="utf-8"))


class TestRoi(unittest.TestCase):
    def test_atribuicao_e_liquido(self):
        r = calcular(CFG, "2026-11")
        f = {x["nome"]: x for x in r["ferramentas"]}
        # sites: lucro 900 dividido entre Claude (110) e Hostinger (40)
        self.assertAlmostEqual(f["Hostinger"]["atribuido"], round(900 * 40 / 150, 2))
        self.assertEqual(r["liquido"], 900 + 300 - 175)

    def test_ferramenta_sem_renda_da_prejuizo(self):
        r = calcular(CFG, "2026-11")
        g = next(x for x in r["ferramentas"] if x["nome"] == "Google AI Plus")
        self.assertLess(g["resultado"], 0)
        self.assertIn("PREJUÍZO", relatorio(r))

    def test_hora_minima(self):
        r = calcular(CFG, "2026-11")
        ia = next(x for x in r["rendas"] if x["id"] == "avaliacaoia")
        self.assertTrue(ia["abaixo"])  # 300/8 = 37,5 < 45


if __name__ == "__main__":
    unittest.main()
