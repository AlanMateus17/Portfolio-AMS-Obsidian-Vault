import copy
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import falar
import politica

MODELO = Path(__file__).resolve().parent / "politica.example.toml"


class TestePolitica(unittest.TestCase):
    def setUp(self):
        self.d = politica.carregar(MODELO)

    def test_modelo_valido(self):
        self.assertEqual(politica.validar(self.d), [])

    def test_luz_livre(self):
        self.assertEqual(politica.decidir(self.d, "light.turn_on", "light.sala")[0], "livre")

    def test_trancar_livre_destrancar_celular(self):
        self.assertEqual(politica.decidir(self.d, "lock.lock", "lock.porta_da_frente")[0], "livre")
        self.assertEqual(politica.decidir(self.d, "lock.unlock", "lock.porta_da_frente")[0], "celular")

    def test_arquivo_nao_afrouxa_os_minimos(self):
        d = copy.deepcopy(self.d)
        d["regra"].insert(0, {"acao": "lock.unlock", "nivel": "livre"})
        d["regra"].insert(0, {"acao": "cover.open_cover", "tipo": "janela", "nivel": "livre"})
        d["regra"].insert(0, {"acao": "camera.turn_off", "nivel": "livre"})
        nivel, motivo = politica.decidir(d, "lock.unlock", "lock.porta_da_frente")
        self.assertEqual(nivel, "celular")
        self.assertIn("mínimo fixo", motivo)
        self.assertEqual(politica.decidir(d, "cover.open_cover", "cover.janela_quarto")[0], "celular")
        self.assertEqual(politica.decidir(d, "camera.turn_off", "camera.quintal")[0], "proibido")

    def test_cortina_pode_abrir_janela_nao(self):
        self.assertEqual(politica.decidir(self.d, "cover.open_cover", "cover.cortina_sala")[0], "livre")
        self.assertEqual(politica.decidir(self.d, "cover.open_cover", "cover.janela_quarto")[0], "celular")

    def test_geladeira(self):
        self.assertEqual(politica.decidir(self.d, "switch.turn_off", "switch.geladeira")[0], "celular")
        self.assertEqual(politica.decidir(self.d, "switch.turn_off", "switch.tomada_escritorio")[0], "voz")
        d = copy.deepcopy(self.d)
        for e in d["entidade"]:
            if e["id"] == "switch.geladeira":
                del e["religar_em_min"]
        self.assertTrue(any("religar_em_min" in x for x in politica.validar(d)))

    def test_desconhecido_e_padrao(self):
        self.assertEqual(politica.decidir(self.d, "light.turn_on", "light.cozinha")[0], "proibido")
        self.assertEqual(politica.decidir(self.d, "vacuum.return_to_base", "vacuum.robo_aspirador")[0], "voz")
        self.assertEqual(politica.decidir(self.d, "alarm_control_panel.alarm_disarm", "camera.quintal")[0], "proibido")

    def test_limite_de_entidades(self):
        d = copy.deepcopy(self.d)
        d["geral"]["max_entidades_expostas"] = 3
        self.assertTrue(any("limite 3" in x for x in politica.validar(d)))

    def test_entidade_oculta(self):
        d = copy.deepcopy(self.d)
        d["entidade"][0]["exposta"] = False
        self.assertEqual(politica.decidir(d, "light.turn_on", "light.sala")[0], "proibido")
        self.assertNotIn("light.sala", " ".join(politica.expor(d)))

    def test_ha_yaml(self):
        y = politica.ha_yaml(self.d)
        for trecho in ("id: jarvis_religar_switch_geladeira", "entity_id: switch.geladeira", "minutes: 30",
                       "action: switch.turn_on", "action: notify.mobile_app_celular_do_alan"):
            self.assertIn(trecho, y)
        self.assertNotIn("light.sala", y)


class TesteFalar(unittest.TestCase):
    def transcript(self, linhas):
        tmp = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8")
        for x in linhas:
            tmp.write((x if isinstance(x, str) else json.dumps(x)) + "\n")
        tmp.close()
        self.addCleanup(os.unlink, tmp.name)
        return Path(tmp.name)

    def test_ultima_resposta(self):
        t = self.transcript([
            {"type": "user", "message": {"content": "oi"}},
            {"type": "assistant", "message": {"content": [{"type": "text", "text": "Primeira."}]}},
            "linha quebrada {",
            {"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Bash"}]}},
            {"type": "assistant", "message": {"content": [{"type": "text", "text": "Pronto, criei a pasta."}]}},
        ])
        self.assertEqual(falar.ultima_resposta(t), "Pronto, criei a pasta.")

    def test_limpar(self):
        md = ("## Feito\n\n- Criei **a pasta** `aulas/`\n- Veja [o guia](https://x.example/guia)\n\n"
              "```bash\nrm -rf /\n```\n\n| a | b |\n|---|---|\n\nAcesse https://site.example agora.")
        t = falar.limpar(md)
        for proibido in ("**", "`", "rm -rf", "|", "https://", "##"):
            self.assertNotIn(proibido, t)
        self.assertIn("Criei a pasta aulas/", t)
        self.assertIn("deixei o código na tela", t)
        self.assertIn("o guia", t)

    def test_limita_tamanho(self):
        t = falar.limpar("Frase curta. " * 100, limite=100)
        self.assertLessEqual(len(t), 130)
        self.assertTrue(t.endswith("O resto está na tela."))

    def test_hook_nunca_quebra(self):
        with mock.patch("sys.stdin", io.StringIO("isto não é json")):
            self.assertEqual(falar.main([]), 0)
        with mock.patch("sys.stdin", io.StringIO(json.dumps({"transcript_path": "/nao/existe.jsonl"}))):
            self.assertEqual(falar.main([]), 0)

    def test_mudo_e_sem_piper(self):
        with mock.patch.dict(os.environ, {"JARVIS_MUDO": "1"}):
            self.assertEqual(falar.falar("teste"), 0)
        with mock.patch("shutil.which", return_value=None):
            self.assertEqual(falar.falar("teste"), 0)


if __name__ == "__main__":
    unittest.main()
