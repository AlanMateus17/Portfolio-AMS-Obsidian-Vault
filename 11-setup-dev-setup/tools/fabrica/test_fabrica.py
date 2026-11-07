import sys
import tempfile
import tomllib
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from plano_semanal import contexto, para_toml  # noqa: E402
from preencher import preencher, substituir  # noqa: E402

DOC = ('<w:document xmlns:w="w"><w:body><w:p><w:r><w:t>Tema: {{te</w:t></w:r><w:r><w:t>ma}}</w:t></w:r></w:p>'
       '<w:p><w:r><w:t>{{objetivos}} {{faltando}}</w:t></w:r></w:p></w:body></w:document>')


class TestFabrica(unittest.TestCase):
    def test_campo_quebrado_entre_runs(self):
        xml, faltas = substituir(DOC, {"tema": "Algoritmos & lógica", "objetivos": ["a", "b"]})
        self.assertIn("Algoritmos &amp; lógica", xml)
        self.assertIn("<w:br/>", xml)
        self.assertEqual(faltas, ["faltando"])

    def test_preenche_docx_e_recusa_aluno(self):
        with tempfile.TemporaryDirectory() as t:
            m, s = Path(t) / "m.docx", Path(t) / "s.docx"
            with zipfile.ZipFile(m, "w") as z:
                z.writestr("word/document.xml", DOC)
                z.writestr("[Content_Types].xml", "<Types/>")
            preencher(m, {"tema": "X", "objetivos": ["a"], "faltando": "ok"}, s)
            self.assertIn("X", zipfile.ZipFile(s).read("word/document.xml").decode())
            with self.assertRaises(SystemExit):
                preencher(m, {"nome_aluno": "y"}, s)

    def test_plano_limita_objetivos(self):
        base = Path(__file__).parent / "modelos"
        em = tomllib.loads((base / "ementa.example.toml").read_text(encoding="utf-8"))
        em["semana"][0]["objetivos"].append("quarto objetivo")
        rg = tomllib.loads((base / "regras.example.toml").read_text(encoding="utf-8"))
        ctx = contexto(em, rg, 1)
        self.assertEqual(len(ctx["objetivos"]), 3)
        self.assertEqual(tomllib.loads(para_toml(ctx))["tema"], "Algoritmos no dia a dia")


if __name__ == "__main__":
    unittest.main()
