import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import motor  # noqa: E402

REGRAS = motor.carregar()
REC = {"rotas": [{"tarefa": "Site novo (seu ou de cliente)", "primaria": "Copilot", "reserva": "Claude Code", "portao": "Você aprova"}]}


class Escada(unittest.TestCase):
    def d(self, pedido, rec=None):
        return motor.decidir(pedido, REGRAS, rec or {}, {})

    def test_portao_humano_vem_antes_de_tudo(self):
        self.assertEqual(self.d("publicar o site novo do cliente", REC)["degrau"], 5)

    def test_pronto_no_catalogo(self):
        r = self.d("site novo para a padaria", REC)
        self.assertEqual(r["degrau"], 1)
        self.assertTrue(r["pronto_no_setup"])

    def test_codigo(self):
        self.assertEqual(self.d("calcular o rateio da conta de luz")["degrau"], 2)

    def test_codigo_com_agenda_fica_no_2_e_cita_a_automacao(self):
        r = self.d("calcular o rateio toda semana")
        self.assertEqual(r["degrau"], 2)
        self.assertIn("toda semana", r["motivo"])

    def test_automacao(self):
        self.assertEqual(self.d("toda semana me mandar o resumo das vendas")["degrau"], 3)

    def test_linguagem_vai_para_ia(self):
        r = self.d("escreva 15 questões teóricas de SO para a turma")
        self.assertEqual(r["degrau"], 4)
        self.assertEqual(r["tipo"], "aula")

    def test_sem_regra_cai_na_ia_com_aviso(self):
        r = self.d("xyz abc")
        self.assertEqual(r["degrau"], 4)
        self.assertIn("nenhuma regra", r["motivo"])

    def test_tarefa_grande_vai_para_o_modelo_forte(self):
        self.assertIn("Fable", self.d("planejar a arquitetura do AMtech OS")["destino"])


class Sensivel(unittest.TestCase):
    def test_cpf_forca_ia_local(self):
        r = motor.decidir("resumir o texto do CPF 123.456.789-00", REGRAS, {}, {})
        self.assertTrue(r["sensivel"])
        self.assertIn("Ollama", r["destino"])
        self.assertIn(REGRAS["sensivel"]["regra"], r["formulario"]["RESTRIÇÕES"])

    def test_texto_comum_nao_e_sensivel(self):
        self.assertEqual(motor.sensivel("escreva um post sobre Linux", REGRAS), [])


class Registro(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        os.environ["NUCLEO_DB"] = str(Path(self.tmp.name) / "n.db")
        os.environ.pop("NUCLEO_DESLIGADO", None)
        con = motor.nuc.abrir()
        con.close()

    def tearDown(self):
        os.environ.pop("NUCLEO_DB", None)
        self.tmp.cleanup()

    def test_regra_de_tres(self):
        con = motor.nuc.abrir()
        for _ in range(3):
            i = motor.nuc.evento(con, "motor.decisao", {"pedido": "p", "degrau": 4, "assinatura": "questoes redes"})
            motor.nuc.evento(con, "motor.resultado", {"decisao": i, "ok": True})
        motor.nuc.evento(con, "motor.custo", {"ferramenta": "claude", "modelo": "sonnet", "entrada": 100, "saida": 50, "usd": 0.01})
        rel = motor.relatorio(con)
        con.close()
        self.assertIn("questoes redes (3x)", rel)
        self.assertIn("US$ 0.01", rel)

    def test_duas_vezes_nao_basta(self):
        con = motor.nuc.abrir()
        for _ in range(2):
            i = motor.nuc.evento(con, "motor.decisao", {"pedido": "p", "degrau": 4, "assinatura": "x y"})
            motor.nuc.evento(con, "motor.resultado", {"decisao": i, "ok": True})
        self.assertIn("nenhuma ainda", motor.relatorio(con))
        con.close()


class Dados(unittest.TestCase):
    def test_regras_completas(self):
        self.assertEqual(sorted(REGRAS["degraus"]), ["1", "2", "3", "4", "5"])
        for tipo in REGRAS["tipos"]:
            self.assertIn(tipo, REGRAS["entregaveis"])
        self.assertIn("padrao", REGRAS["entregaveis"])

    def test_json_valido_na_saida(self):
        json.dumps(motor.decidir("organizar arquivos", REGRAS, {}, {}), ensure_ascii=False)


if __name__ == "__main__":
    unittest.main()
