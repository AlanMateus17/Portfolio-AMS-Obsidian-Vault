import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bot import carregar_env, permitido, responder  # noqa: E402


class TestBot(unittest.TestCase):
    def test_so_o_seu_chat(self):
        self.assertTrue(permitido({"chat": {"id": 42}}, "42"))
        self.assertFalse(permitido({"chat": {"id": 7}}, "42"))

    def test_comando_desconhecido_nao_executa(self):
        self.assertIn("Não conheço", responder("rm -rf /"))

    def test_ajuda(self):
        self.assertIn("/status", responder("/ajuda"))

    def test_env_legivel_por_outros_recusado(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "telegram.env"
            p.write_text("TELEGRAM_TOKEN=x\n")
            os.chmod(p, 0o644)
            with self.assertRaises(SystemExit):
                carregar_env(p)
            os.chmod(p, 0o600)
            self.assertEqual(carregar_env(p)["TELEGRAM_TOKEN"], "x")


if __name__ == "__main__":
    unittest.main()
