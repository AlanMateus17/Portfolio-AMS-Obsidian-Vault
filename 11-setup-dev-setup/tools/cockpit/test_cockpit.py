import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gerar  # noqa: E402


class TestCockpit(unittest.TestCase):
    def test_tabela_markdown(self):
        md = "## Fases\n\n| A | B |\n|---|---|\n| 1 | **dois** |\n| 3 | `x` |\n\nfim"
        self.assertEqual(gerar.tabela(md, "## Fases"), [["1", "**dois**"], ["3", "`x`"]])
        self.assertEqual(gerar.limpar("**dois** e [link](a.md)"), "dois e link")

    def test_secao_ausente(self):
        with self.assertRaises(ValueError):
            gerar.tabela("nada", "## Fases")

    def test_dados_reais(self):
        d = gerar.montar()
        self.assertEqual(len(d["camadas"]), 23)
        self.assertGreater(len(d["blocos"]), 400)
        self.assertTrue(all(b["o"] for b in d["blocos"]), "todo bloco entra em algum passo")
        self.assertTrue(d["trocas"] and d["mantidas"] and d["autonomia"] and d["nucleo"] and d["hoje"])
        self.assertTrue(any(f["nuc"] for f in d["fases"]))

    def test_html_tem_os_dados(self):
        html = gerar.gerar()
        self.assertNotIn("/*DADOS*/null", html)
        self.assertIn("<title>Núcleo AMtech</title>", html)
        ini = html.index("const D=") + len("const D=")
        fim = html.index(";\n", ini)
        self.assertIn("blocos", json.loads(html[ini:fim]))


if __name__ == "__main__":
    unittest.main()
