import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

os.environ["NUCLEO_DESLIGADO"] = "1"  # os testes nunca escrevem no seu banco
sys.path.insert(0, str(Path(__file__).resolve().parent))
from triagem import (buscar_blocos, buscar_fora, carregar, decidir, main, pacote, palavras,  # noqa: E402
                     proximo_adr, rascunho_adr, url_grep)

ECO = {"blocos": [
    {"id": "chatwoot", "rotulo": "Chatwoot|(atendimento)", "descricao": "Atendimento no WhatsApp com filas e respostas prontas."},
    {"id": "agenda", "rotulo": "Agenda online|(Cal.com)", "descricao": "Cliente marca horário sozinho."},
]}
MAPA = {"fora": [{"item": "Coolify e Dokploy", "motivo": "Um deploy só: Kamal."}]}


class TestTriagem(unittest.TestCase):
    def test_palavras_ignora_acento_e_vazias(self):
        self.assertEqual(palavras("Atendimento com fila para clientes"), ["atendimento", "fila"])

    def test_busca_acha_o_bloco_certo(self):
        self.assertEqual(buscar_blocos("atendimento whatsapp", ECO)[0]["id"], "chatwoot")

    def test_busca_vazia(self):
        self.assertEqual(buscar_blocos("de para com", ECO), [])

    def test_nucleo_sempre_constroi(self):
        self.assertEqual(decidir(True, ECO["blocos"], False), "C")

    def test_pronto_sem_integracao_sobe(self):
        self.assertEqual(decidir(False, ECO["blocos"], False), "A")

    def test_pronto_com_integracao_cola(self):
        self.assertEqual(decidir(False, ECO["blocos"], True), "B")

    def test_nada_pronto_e_nao_nucleo_cola(self):
        self.assertEqual(decidir(False, [], False), "B")

    def test_avisa_o_que_ja_foi_recusado(self):
        self.assertEqual(len(buscar_fora("subir o coolify", MAPA)), 1)

    def test_proximo_adr_e_rascunho(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            self.assertEqual(proximo_adr(p), 1)
            (p / "0007-algo.md").write_text("x", encoding="utf-8")
            self.assertEqual(proximo_adr(p), 8)
        txt = rascunho_adr(8, "Agenda online", "A", ECO["blocos"][1:], date(2026, 11, 6))
        self.assertIn("# 0008 · Agenda online", txt)
        self.assertIn("Opção A", txt)

    def test_pacote_tem_stack_e_instrucao(self):
        txt = pacote("atendimento", ECO, MAPA)
        self.assertIn(".NET 10", txt)
        self.assertIn("Responda seco", txt)
        self.assertIn("Chatwoot", txt)

    def test_url_do_grep_app(self):
        self.assertEqual(url_grep("Atendimento com fila"), "https://grep.app/search?q=atendimento+fila")

    def test_dados_reais_carregam_e_acham_chatwoot(self):
        eco, _ = carregar()
        self.assertIn("chatwoot", [b["id"] for b in buscar_blocos("atendimento whatsapp", eco)])

    def test_cli_grava_adr(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(main(["triar", "agenda online", "--nucleo", "não", "--integra", "nao", "--adr", d]), 0)
            self.assertEqual(len(list(Path(d).glob("0001-*.md"))), 1)

    def test_triagem_grava_e_consulta_no_nucleo(self):
        import triagem as tr
        with tempfile.TemporaryDirectory() as d:
            os.environ["NUCLEO_DB"] = str(Path(d) / "n.db")
            del os.environ["NUCLEO_DESLIGADO"]
            try:
                tr.nuc.abrir().close()
                main(["triar", "agenda online", "--nucleo", "nao", "--integra", "nao"])
                con = tr.nuc.abrir()
                self.assertEqual(con.execute("SELECT count(*) FROM conhecimento WHERE tipo='triagem'").fetchone()[0], 1)
                self.assertIn("Triagem: agenda online", tr.nuc.contexto(con, "agenda online"))
                con.close()
            finally:
                os.environ["NUCLEO_DESLIGADO"] = "1"
                del os.environ["NUCLEO_DB"]

    def test_cli_recusa_resposta_invalida(self):
        self.assertEqual(main(["triar", "agenda", "--nucleo", "talvez"]), 2)


if __name__ == "__main__":
    unittest.main()
