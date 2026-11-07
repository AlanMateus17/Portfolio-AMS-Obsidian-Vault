import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cabe import buscar_hf, parametros_hf, qlora_gb, rodar  # noqa: E402


class TestCabe(unittest.TestCase):
    def test_3b_cabe_na_gpu_em_q4(self):
        self.assertEqual(rodar(3, 4096, 32, 4, None)[0]["onde"], "inteiro na GPU")

    def test_14b_q4_offload(self):
        self.assertIn("offload", rodar(14, 8192, 32, 4, None)[0]["onde"])

    def test_70b_q4_nao_cabe_em_32gb(self):
        self.assertIn("não cabe", rodar(70, 8192, 32, 4, None)[0]["onde"])

    def test_moe_ativos_melhoram_velocidade(self):
        self.assertEqual(rodar(30, 8192, 32, 4, 3)[0]["velocidade"], "usável")

    def test_qlora_8b_cabe_no_kaggle(self):
        self.assertLessEqual(qlora_gb(8), 15)

    def test_parametros_hf_safetensors_e_gguf(self):
        self.assertAlmostEqual(parametros_hf({"safetensors": {"total": 2_127_532_032}}), 2.13, places=2)
        self.assertAlmostEqual(parametros_hf({"safetensors": None, "gguf": {"total": 4_022_468_096}}), 4.02, places=2)
        with self.assertRaises(ValueError):
            parametros_hf({"id": "x/y"})

    def test_buscar_hf_monta_a_url(self):
        vistos = []

        class Resp:
            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def read(self):
                return b'{"safetensors": {"total": 500000000}}'

        def abrir(url, timeout):
            vistos.append(url)
            return Resp()

        d = buscar_hf("lerobot/smolvla_base", abrir=abrir)
        self.assertEqual(vistos, ["https://huggingface.co/api/models/lerobot/smolvla_base"])
        self.assertAlmostEqual(parametros_hf(d), 0.5)


if __name__ == "__main__":
    unittest.main()


import tokens as _tok  # noqa: E402


class TestTokens(unittest.TestCase):
    def test_rota_forte_para_arquitetura(self):
        self.assertEqual(_tok.rota("revisar a arquitetura do AM Kaixara")[0], "forte")

    def test_rota_barato_para_rascunho(self):
        self.assertEqual(_tok.rota("resumir esta transcrição em lote")[0], "barato")

    def test_rota_padrao_local(self):
        self.assertEqual(_tok.rota("qualquer coisa fora das palavras")[0], "local")

    def test_estimativa_de_tokens(self):
        self.assertEqual(_tok.estimar_tokens("a" * 400), 100)
        self.assertEqual(_tok.estimar_tokens(""), 1)
