import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verificar import checar_abnt, checar_escola, corrigir_abnt, ler  # noqa: E402

DOC = ('<w:document xmlns:w="w"><w:body><w:p><w:r><w:t>{texto}</w:t></w:r></w:p>'
       '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr></w:body></w:document>')
STY = '<w:styles xmlns:w="w"><w:docDefaults><w:rPrDefault><w:rPr><w:sz w:val="22"/></w:rPr></w:rPrDefault></w:docDefaults></w:styles>'


def docx(p: Path, texto: str = "Introdução") -> Path:
    with zipfile.ZipFile(p, "w") as z:
        z.writestr("word/document.xml", DOC.format(texto=texto))
        z.writestr("word/styles.xml", STY)
    return p


class TestVerificar(unittest.TestCase):
    def test_carta_e_margens_erradas_reprovam_e_correcao_conserta(self):
        with tempfile.TemporaryDirectory() as t:
            p = docx(Path(t) / "tcc.docx")
            antes = {i["item"]: i["ok"] for i in checar_abnt(ler(p))}
            self.assertFalse(antes["Papel A4"])
            self.assertFalse(antes["Margem top 3 cm"])
            s = Path(t) / "c.docx"
            corrigir_abnt(p, s)
            depois = {i["item"]: i["ok"] for i in checar_abnt(ler(s))}
            for k in ("Papel A4", "Margem top 3 cm", "Margem right 2 cm", "Fonte 12 no texto", "Espaçamento 1,5", "Fonte Arial ou Times New Roman"):
                self.assertTrue(depois[k], k)

    def test_escola_campos_vazios_e_cpf(self):
        with tempfile.TemporaryDirectory() as t:
            p = docx(Path(t) / "plan.docx", "Tema {{tema}} [FALTA: turma] aluno CPF 123.456.789-00")
            r = {i["item"]: i["ok"] for i in checar_escola(ler(p))}
            self.assertFalse(r["Todos os campos do modelo preenchidos"])
            self.assertFalse(r["Sem dados pessoais de aluno (CPF, matrícula, nota individual)"])


if __name__ == "__main__":
    unittest.main()
