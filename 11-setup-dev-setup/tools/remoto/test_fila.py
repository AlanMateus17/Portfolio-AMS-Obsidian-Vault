import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import fila  # noqa: E402


class TestFila(unittest.TestCase):
    def test_repo_padrao_e_arroba(self):
        self.assertEqual(fila.separar_repo("criar X"), ("dev-setup", "criar X"))
        self.assertEqual(fila.separar_repo("@catalogo-html corrigir menu"), ("catalogo-html", "corrigir menu"))

    def test_sensivel_so_local(self):
        self.assertEqual(fila.motores(True, False, True), ["local"])

    def test_ordem_e_pausa(self):
        self.assertEqual(fila.motores(False, False, True), ["claude", "gratis", "local"])
        self.assertEqual(fila.motores(False, True, True), ["gratis", "local"])
        self.assertEqual(fila.motores(False, False, False), ["gratis", "local"])

    def test_limite(self):
        self.assertTrue(fila.bateu_limite("Claude usage limit reached. Resets at 3pm", 1))
        self.assertFalse(fila.bateu_limite("usage limit", 0))
        self.assertFalse(fila.bateu_limite("erro de sintaxe", 1))

    def test_prompt_leva_formulario(self):
        p = fila.montar_prompt("pagina", {"formulario": {"ENTREGÁVEL": "Site", "RESTRIÇÕES": ["Nada publicado"]}})
        self.assertIn("Entregável: Site", p)
        self.assertIn("Restrição: Nada publicado", p)
        self.assertIn("não publique", p)

    def test_aider_local_nao_precisa_de_chave(self):
        cmd = fila.comando_aider("local", "x", {}, False)
        self.assertIn("ollama_chat/" + fila.MODELO_LOCAL, cmd)

    def test_aider_gratis(self):
        self.assertIsNone(fila.comando_aider("gratis", "x", {}, False))
        self.assertIn("gemini/gemini-2.5-flash", fila.comando_aider("gratis", "x", {"GEMINI_API_KEY": "k"}, False))
        cmd = fila.comando_aider("gratis", "x", {"LITELLM_MASTER_KEY": "m"}, True)
        self.assertIn("openai/gratis", cmd)

    def test_adicionar_e_pausa(self):
        with tempfile.TemporaryDirectory() as t:
            fila.DIR = Path(t)
            fila.ESTADO = Path(t) / "estado.json"
            i = fila.adicionar("@x fazer y")
            self.assertEqual((i["repo"], i["status"]), ("x", "pendente"))
            self.assertEqual(len(fila.itens()), 1)
            self.assertFalse(fila.claude_pausado())
            fila.pausar_claude()
            self.assertTrue(fila.claude_pausado())
            with self.assertRaises(ValueError):
                fila.adicionar("   ")


if __name__ == "__main__":
    unittest.main()
