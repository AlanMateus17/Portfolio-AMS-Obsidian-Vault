import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import agenda  # noqa: E402
import nucleo as nuc  # noqa: E402

FASES = [
    {"id": "f1", "titulo": "Um", "passos": [
        {"id": "a", "titulo": "A", "quem": "voce", "pronto": "x", "tempo_min": 5, "empresas": ["software"]},
        {"id": "b", "titulo": "B", "quem": "script", "pronto": "x", "tempo_min": 5},
        {"id": "c", "titulo": "C", "quem": "claude", "pronto": "x", "tempo_min": 5, "decisao": True, "empresas": ["software"]},
    ]},
    {"id": "f2", "titulo": "Dois", "gatilho": "quando vender", "passos": [
        {"id": "d", "titulo": "D", "quem": "voce", "pronto": "x", "tempo_min": 5, "decisao": True},
    ]},
]


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.con = nuc.abrir(Path(self.tmp.name) / "n.db")

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def test_pendentes_so_o_que_e_seu(self):
        ids = [p["id"] for _, p in agenda.pendentes(FASES, set())]
        self.assertEqual(ids, ["a", "c"], "script fica de fora; fase com gatilho espera")
        self.assertEqual([p["id"] for _, p in agenda.pendentes(FASES, set(), so_decisoes=True)], ["c"])

    def test_marcar_fase_inteira_e_desfazer(self):
        self.assertEqual(agenda.marcar(self.con, ["f1"], FASES), 3)
        self.assertEqual(agenda.feitos(self.con), {"a", "b", "c"})
        self.assertEqual(agenda.desmarcar(self.con, ["c"], FASES), 1)
        self.assertEqual(self.con.execute("SELECT count(*) FROM eventos WHERE tipo='roteiro.feito'").fetchone()[0], 1)

    def test_gatilho_abre_quando_marca_passo(self):
        agenda.marcar(self.con, ["f1"], FASES)
        self.assertEqual(agenda.pendentes(FASES, agenda.feitos(self.con)), [])
        self.assertEqual(agenda.progresso(FASES, {"a"}, "software"), [("Um", 1, 2)])

    def test_id_desconhecido(self):
        with self.assertRaises(ValueError):
            agenda.marcar(self.con, ["zzz"], FASES)

    def test_roteiro_real_tem_a_empresa(self):
        fases = agenda.roteiro()
        sw = [p for _, p in agenda.pendentes(fases, set(), "software", so_decisoes=True)]
        self.assertTrue(any(p["id"] == "sw-formalizar" for p in sw))
        self.assertTrue(all("software" in p["empresas"] for p in sw))


if __name__ == "__main__":
    unittest.main()
