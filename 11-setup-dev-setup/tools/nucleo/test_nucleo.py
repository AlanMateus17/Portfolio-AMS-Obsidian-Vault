import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import nucleo  # noqa: E402


class TestNucleo(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.db = Path(self.dir.name) / "n.db"
        self.con = nucleo.abrir(self.db)

    def tearDown(self):
        self.con.close()
        self.dir.cleanup()

    def test_lembrar_e_buscar_sem_acento(self):
        nucleo.lembrar(self.con, "Implantação na t4g precisa do builder arm64", tipo="licao", tags="deploy")
        rs = nucleo.buscar(self.con, "implantacao arm64")
        self.assertEqual(rs[0]["tipo"], "licao")
        self.assertTrue(nucleo.buscar(self.con, "IMPLANTAÇÃO"))  # acento e maiúscula não atrapalham

    def test_busca_por_tipo_e_vazia(self):
        nucleo.lembrar(self.con, "Chatwoot atende WhatsApp", tipo="nota")
        self.assertEqual(nucleo.buscar(self.con, "chatwoot", tipo="adr"), [])
        self.assertEqual(nucleo.buscar(self.con, "de a"), [])

    def test_chave_nao_duplica(self):
        a = nucleo.lembrar(self.con, "v1", tipo="adr", titulo="X", chave="adr:0001")
        b = nucleo.lembrar(self.con, "v2 atualizada", tipo="adr", titulo="X", chave="adr:0001")
        self.assertEqual(a, b)
        self.assertEqual(self.con.execute("SELECT count(*) FROM conhecimento").fetchone()[0], 1)
        self.assertTrue(nucleo.buscar(self.con, "atualizada"))

    def test_tipo_invalido(self):
        with self.assertRaises(ValueError):
            nucleo.lembrar(self.con, "x", tipo="fofoca")

    def test_evento_tarefa_auditoria(self):
        eid = nucleo.evento(self.con, "venda.aprovada", '{"valor": 97}')
        tid = nucleo.tarefa_nova(self.con, "Enviar acesso", evento_id=eid)
        nucleo.tarefa_estado(self.con, tid, "feita")
        nucleo.auditar(self.con, "cobrador", "lembrete enviado", "avisa")
        self.assertEqual(self.con.execute("SELECT estado FROM tarefas WHERE id=?", (tid,)).fetchone()[0], "feita")
        with self.assertRaises(ValueError):
            nucleo.auditar(self.con, "x", "y", "talvez")
        with self.assertRaises(ValueError):
            nucleo.tarefa_estado(self.con, 999, "feita")

    def test_evento_aceita_texto_solto(self):
        eid = nucleo.evento(self.con, "backup.concluido", "snapshot abc")
        self.assertIn("snapshot abc", self.con.execute("SELECT dados FROM eventos WHERE id=?", (eid,)).fetchone()[0])

    def test_importar_adrs_e_recusas_reais(self):
        n = nucleo.importar(self.con)
        self.assertGreaterEqual(n["adr"], 9)
        self.assertTrue(nucleo.buscar(self.con, "Kamal", tipo="adr"))
        self.assertEqual(nucleo.importar(self.con), n)  # de novo não duplica
        total = self.con.execute("SELECT count(*) FROM conhecimento").fetchone()[0]
        self.assertEqual(total, n["adr"] + n["recusa"])

    def test_contexto_curto(self):
        nucleo.lembrar(self.con, "Deploy do AM Rendara vai para a VM da Oracle pelo Kamal. " * 20, tipo="licao")
        txt = nucleo.contexto(self.con, "deploy rendara")
        self.assertTrue(txt.startswith("- [licao]"))
        self.assertLess(len(txt), 450)

    def test_cli(self):
        os.environ["NUCLEO_DB"] = str(self.db)
        try:
            self.assertEqual(nucleo.main(["lembrar", "teste da linha de comando", "--tipo", "nota"]), 0)
            self.assertEqual(nucleo.main(["tarefa", "nova", "algo"]), 0)
            self.assertEqual(nucleo.main(["auditar", "a", "b", "--nivel", "automatico"]), 0)
        finally:
            del os.environ["NUCLEO_DB"]


if __name__ == "__main__":
    unittest.main()
