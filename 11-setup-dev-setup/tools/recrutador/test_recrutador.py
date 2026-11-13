import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import recrutador as rec  # noqa: E402

nuc = rec.nuc


class TestRecrutador(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.con = nuc.abrir(Path(self.tmp.name) / "n.db")
        self.d = rec.dados()

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def test_dados_validos(self):
        self.assertEqual(rec.validar(self.d), [])

    def test_trimestre_do_eixo(self):
        self.assertEqual(rec.trimestre(date(2026, 11, 9)), 1)
        self.assertEqual(rec.trimestre(date(2027, 2, 1)), 2)
        self.assertEqual(rec.trimestre(date(2027, 9, 1)), 4)
        self.assertEqual(rec.trimestre(date(2028, 5, 1)), 4)

    def test_pacote_tem_regras_e_avaliacao(self):
        f = rec.formato(self.d, "amazon-lp")
        txt = rec.pacote(self.d, f, empresa="Amazon", vaga="Backend .NET", minhas_historias="Montei o setup sozinho")
        self.assertIn("Uma pergunta por vez", txt)
        self.assertIn("Empresa simulada: Amazon", txt)
        self.assertIn("INGLÊS:", txt)
        self.assertIn("Backend .NET", txt)
        self.assertIn("just recrutador registrar amazon-lp", txt)
        self.assertNotIn("INGLÊS:", rec.pacote(self.d, rec.formato(self.d, "br-triagem")))

    def test_registro_pronto_e_sugestao(self):
        hoje = date(2026, 11, 9)
        primeiro = rec.sugerir(self.d, rec.historico(self.con), hoje)
        self.assertEqual(primeiro["trimestre"], 1)
        for n in (2, 3, 3, 4):
            rec.registrar(self.con, "br-triagem", n, "resumo longo", hoje=hoje)
        notas = [x["nota"] for x in rec.historico(self.con)["br-triagem"]]
        self.assertTrue(rec.pronto(notas))
        self.assertNotEqual(rec.sugerir(self.d, rec.historico(self.con), hoje)["id"], "br-triagem")
        self.assertIn("PRONTO", rec.tabela(self.d, rec.historico(self.con), hoje))
        self.assertIn("entra no trimestre 4", rec.tabela(self.d, rec.historico(self.con), hoje))
        with self.assertRaises(ValueError):
            rec.registrar(self.con, "br-triagem", 5)


if __name__ == "__main__":
    unittest.main()
