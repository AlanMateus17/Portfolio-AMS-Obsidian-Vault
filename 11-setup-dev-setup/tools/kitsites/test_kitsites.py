import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from checagem import checar, modulos_presentes, nota  # noqa: E402
from gerar import carregar, gerar, validar  # noqa: E402


class TestKit(unittest.TestCase):
    def test_dados_validos(self):
        kit, sw = carregar()
        self.assertEqual(validar(kit, sw), [])

    def test_um_prompt_por_site(self):
        kit, sw = carregar()
        n = sum(s["categoria"] == "site" for s in sw["softwares"])
        self.assertEqual(gerar(kit, sw).count("```text"), n)

    def test_site_vazio_tira_nota_baixa(self):
        self.assertLess(nota(checar("<html><body></body></html>")), 30)

    def test_detecta_whatsapp_e_modulos(self):
        it = checar('<html lang="pt"><a href="https://wa.me/55">w</a></html>')
        self.assertTrue(next(i for i in it if i["item"] == "Botão de WhatsApp")["ok"])
        self.assertIn("cardapio", modulos_presentes("Nosso cardápio"))


if __name__ == "__main__":
    unittest.main()
