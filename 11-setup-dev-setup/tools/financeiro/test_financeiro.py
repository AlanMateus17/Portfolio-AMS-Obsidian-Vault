import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from financeiro import categorizar, conectar, importar, resumo_mes  # noqa: E402


class TestFinanceiro(unittest.TestCase):
    def test_importa_sem_duplicar_e_resume(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            c = p / "extrato.csv"
            c.write_text("Data,Valor,Identificador,Descrição\n05/11/2026,3000.00,a,Salario escola\n06/11/2026,-500.00,b,Aluguel\n", encoding="utf-8")
            db = conectar(p)
            regras = {"categorias": {"Moradia": ["aluguel"], "Renda": ["salario"]}}
            self.assertEqual(importar(c, db, regras), 2)
            self.assertEqual(importar(c, db, regras), 0)
            r = resumo_mes(db, "2026-11", {"caixa": [{"nome": "Reserva", "meta": 1000, "atual": 0}]})
            self.assertIn("Sobra:    R$ 2,500.00", r)
            self.assertIn("Reserva", r)

    def test_fatura_nubank_gasto_negativo(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            c = p / "fatura.csv"
            c.write_text("date,title,amount\n2026-11-02,Posto Shell,120.50\n", encoding="utf-8")
            db = conectar(p)
            importar(c, db, {})
            v = db.execute("select valor from lanc").fetchone()[0]
            self.assertAlmostEqual(v, -120.50)

    def test_categoria(self):
        self.assertEqual(categorizar("RACAO PREMIUM", {"categorias": {"Cães": ["racao"]}}), "Cães")


if __name__ == "__main__":
    unittest.main()
