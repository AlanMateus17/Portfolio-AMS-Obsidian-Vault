import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import biblioteca  # noqa: E402


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["AMTECH_VAULT"] = self.tmp.name
        self.d = biblioteca.carregar()

    def tearDown(self):
        os.environ.pop("AMTECH_VAULT", None)
        self.tmp.cleanup()

    def test_dados_validos(self):
        self.assertEqual(biblioteca.validar(self.d), [])

    def test_ordem_das_etapas(self):
        etapas = ["H1.6", "7.14", "0.10", "0.2", "inglês", "1.3"]
        self.assertEqual(sorted(etapas, key=biblioteca.chave_etapa), ["0.2", "0.10", "1.3", "7.14", "H1.6", "inglês"])

    def test_livros_do_assunto_0_4(self):
        ids = [li["id"] for li, _ in biblioteca.para_assunto(self.d, "0.4")]
        self.assertIn("petzold-codigo", ids)

    def test_comprar_na_ordem(self):
        compras = biblioteca.a_comprar(self.d)
        etapas = [e for _, e in compras]
        self.assertEqual(etapas, sorted(etapas, key=biblioteca.chave_etapa))

    def test_registrar_leitura(self):
        li = biblioteca.achar(self.d, "petzold-codigo")
        arq = biblioteca.registrar(li, "cap. 1|2", 50, "0.4", "bit é a menor unidade", date(2026, 11, 18))
        texto = arq.read_text(encoding="utf-8")
        self.assertIn("| 2026-11-18 |", texto)
        self.assertIn("cap. 1/2", texto, "barra vertical não pode quebrar a tabela")
        linhas = biblioteca.ler_registro(li["titulo"])
        self.assertEqual(len(linhas), 1)
        self.assertEqual(linhas[0][3], "50")

    def test_nota_longa_recusada(self):
        li = biblioteca.achar(self.d, "petzold-codigo")
        with self.assertRaises(SystemExit):
            biblioteca.registrar(li, "cap. 1", 30, "0.4", "x" * (biblioteca.NOTA_MAX + 1))

    def test_doc_tem_compra(self):
        self.assertIn("Código", biblioteca.gerar_doc(self.d))


if __name__ == "__main__":
    unittest.main()
