import datetime as dt
import json
import os
import sys
import tempfile
import time
import unittest
from pathlib import Path

import processar as P


def resposta_valida(*_):
    return "Aqui está:\n```json\n" + json.dumps({
        "titulo": "Variáveis em C#", "oferta": "minicurso",
        "pecas": [{"tipo": "corte", "redes": ["instagram", "tiktok"], "titulo": "O que é variável",
                   "texto": "Texto do corte. Link na bio.", "inicio": "01:10", "fim": "01:55"},
                  {"tipo": "newsletter", "redes": ["newsletter"], "titulo": "Edição 12", "texto": "Olá!"}]}) + "\n```"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        for t in P.TIPOS:
            (self.base / "entrada" / t).mkdir(parents=True)
        guia = self.base / "marca.md"
        guia.write_text("Tom: direto e acolhedor.", encoding="utf-8")
        self.cfg = P.ler_config(self.base / "nao-existe.env")
        self.cfg.update(AMTECH_DIR=str(self.base), GUIA_MARCA=str(guia))
        self.agora = dt.datetime(2026, 10, 21, 14, 30)

    def tearDown(self):
        self.tmp.cleanup()

    def antigo(self, caminho: Path, texto="conteúdo"):
        caminho.write_text(texto, encoding="utf-8")
        velho = self.agora.timestamp() - 3600
        os.utime(caminho, (velho, velho))
        return caminho


class TestPipeline(Base):
    def test_texto_vira_pecas_na_fila_e_sai_da_entrada(self):
        arq = self.antigo(self.base / "entrada" / "capitulos" / "Cap 01 – Proposição.md")
        r = P.rodar(self.cfg, resposta_valida, self.agora)
        self.assertEqual(r["erros"], [])
        pasta = Path(r["processados"][0])
        self.assertEqual(pasta.name, "20261021-1430-cap-01-proposicao")
        self.assertTrue((pasta / "LEIA-ME.md").exists())
        self.assertEqual(json.loads((pasta / "status.json").read_text())["status"], "aguardando_aprovacao")
        self.assertIn("Trecho: 01:10 a 01:55", (pasta / "01-corte.md").read_text())
        self.assertFalse(arq.exists())
        self.assertTrue((self.base / "processados" / "capitulos" / arq.name).exists())

    def test_arquivo_recente_espera(self):
        (self.base / "entrada" / "ideias" / "nova.txt").write_text("x")
        os.utime(self.base / "entrada" / "ideias" / "nova.txt", (self.agora.timestamp(), self.agora.timestamp()))
        r = P.rodar(self.cfg, resposta_valida, self.agora)
        self.assertEqual(r, {"processados": [], "erros": []})

    def test_midia_passa_pelo_transcritor(self):
        video = self.antigo(self.base / "entrada" / "aulas" / "aula 03.mp4", "binário falso")
        self.cfg["TRANSCRITOR_CMD"] = (f"{sys.executable} -c \"import pathlib,sys; "
                                       "pathlib.Path(sys.argv[2],'t.txt').write_text('transcrição da aula')\" {arquivo} {saida}")
        vistos = {}

        def gerar(sistema, usuario, cfg):
            vistos["usuario"] = usuario
            return resposta_valida()
        r = P.rodar(self.cfg, gerar, self.agora)
        self.assertEqual(r["erros"], [])
        self.assertIn("transcrição da aula", vistos["usuario"])
        self.assertIn("3 cortes verticais", vistos["usuario"])
        pasta = Path(r["processados"][0])
        self.assertEqual((pasta / "transcricao.txt").read_text(), "transcrição da aula")
        self.assertFalse(video.exists())

    def test_resposta_ruim_tenta_tres_vezes_e_vai_para_quarentena(self):
        arq = self.antigo(self.base / "entrada" / "ideias" / "ideia.txt")
        for _ in range(3):
            P.rodar(self.cfg, lambda *a: "não é json", self.agora)
        self.assertFalse(arq.exists())
        self.assertTrue((self.base / "entrada" / "_com-erro" / "ideia.txt").exists())
        self.assertTrue((self.base / "entrada" / "_com-erro" / "ideia.txt.erro.txt").exists())

    def test_guia_de_marca_e_regras_vao_no_pedido(self):
        sistema, usuario = P.montar_pedido("reparos", "dell.txt", "troca de tela", "Tom: direto.")
        self.assertIn("Tom: direto.", sistema)
        self.assertIn("nada de dados de alunos ou clientes", sistema)
        self.assertIn("Google Perfil", usuario)

    def test_simulacao_nao_precisa_de_chave(self):
        self.antigo(self.base / "entrada" / "decisoes" / "outubro.md")
        r = P.rodar(self.cfg, P.simular_claude, self.agora)
        self.assertEqual(len(r["processados"]), 1)

    def test_sem_chave_da_erro_claro(self):
        self.cfg.pop("ANTHROPIC_API_KEY", None)
        with self.assertRaises(RuntimeError) as c:
            P.chamar_claude("s", "u", self.cfg)
        self.assertIn("ANTHROPIC_API_KEY", str(c.exception))

    def test_nomes_repetidos_nao_sobrescrevem(self):
        for _ in range(2):
            self.antigo(self.base / "entrada" / "ideias" / "mesma.txt")
            P.rodar(self.cfg, resposta_valida, self.agora)
        nomes = sorted(p.name for p in (self.base / "fila").iterdir())
        self.assertEqual(nomes, ["20261021-1430-mesma", "20261021-1430-mesma-2"])


class TestConfig(unittest.TestCase):
    def test_le_arquivo_e_ambiente_vence(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "c.env"
            f.write_text('# comentário\nANTHROPIC_MODEL="modelo-x"\nAMTECH_DIR=/tmp/a\n', encoding="utf-8")
            os.environ["AMTECH_DIR"] = "/tmp/b"
            try:
                cfg = P.ler_config(f)
            finally:
                del os.environ["AMTECH_DIR"]
            self.assertEqual(cfg["ANTHROPIC_MODEL"], "modelo-x")
            self.assertEqual(cfg["AMTECH_DIR"], "/tmp/b")

    def test_extrair_json_recusa_sem_pecas(self):
        with self.assertRaises(ValueError):
            P.extrair_json('{"titulo": "x", "pecas": []}')


if __name__ == "__main__":
    unittest.main()
