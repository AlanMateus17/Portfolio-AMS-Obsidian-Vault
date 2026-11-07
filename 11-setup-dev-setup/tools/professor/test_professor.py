import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import professor  # noqa: E402
import nucleo as nuc  # noqa: E402

MODS = [
    {"id": "a", "trilha": "setup", "trimestre": 1, "prereq": []},
    {"id": "b", "trilha": "setup", "trimestre": 1, "prereq": ["a"]},
    {"id": "f", "trilha": "financas", "trimestre": 1, "prereq": []},
]


class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.con = nuc.abrir(Path(self.tmp.name) / "n.db")

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def test_escada_de_revisao(self):
        d = date(2026, 11, 6)
        self.assertEqual(professor.registrar_prova(self.con, "a", 90, d), (1, "2026-11-07"))
        self.assertEqual(professor.registrar_prova(self.con, "a", 85, d)[0], 3)
        self.assertEqual(professor.registrar_prova(self.con, "a", 40, d)[0], 1)
        nv = professor.niveis(self.con)["a"]
        self.assertEqual((nv["nivel"], nv["ultima_nota"]), (2, 40), "reprovar tira do nível 3")

    def test_subir_nunca_desce(self):
        professor.subir(self.con, "a", 4)
        professor.subir(self.con, "a", 1)
        self.assertEqual(professor.niveis(self.con)["a"]["nivel"], 4)

    def test_plano_respeita_prerequisito_e_revisao(self):
        pl = professor.plano_do_dia(MODS, {})
        self.assertEqual({k: v["id"] for k, v in pl["proximos"].items()}, {"setup": "a", "financas": "f"})
        nv = {"a": {"nivel": 3, "proxima_revisao": "2026-11-01"}}
        pl = professor.plano_do_dia(MODS, nv, date(2026, 11, 6))
        self.assertEqual(pl["revisoes"], ["a"])
        self.assertEqual(pl["proximos"]["setup"]["id"], "b")

    def test_cartoes_e_nota(self):
        aula = "# X\n## Cartões\n- O que é snapshot? :: Uma foto do estado\n* 3-2-1 :: três cópias\n## Se quiser ir além\n- a :: b"
        self.assertEqual(professor.cartoes_de(aula), [("O que é snapshot?", "Uma foto do estado"), ("3-2-1", "três cópias")])
        self.assertEqual(professor.nota_da_correcao('blá\n{"nota": 85, "revisar": ["prune"]}'), 85)
        with self.assertRaises(ValueError):
            professor.nota_da_correcao("sem nota")

    def test_pontos_fracos_viram_pratica_deliberada(self):
        texto = 'Q1 parcial\n{"nota": 70, "revisar": ["prune", "retenção"]}'
        self.assertEqual(professor.fracos_da_correcao(texto), ["prune", "retenção"])
        nuc.evento(self.con, "professor.prova", {"modulo": "a", "nota": 70, "revisar": ["prune"]}, fonte="t")
        nuc.evento(self.con, "professor.prova", {"modulo": "b", "nota": 100, "revisar": []}, fonte="t")
        self.assertEqual(professor.pontos_fracos(self.con), {"a": ["prune"]})

    def test_semana_e_entrada(self):
        self.assertEqual(professor.trilhas_do_dia(date(2026, 11, 8)), (), "domingo é folga")
        self.assertIn("matematica", professor.trilhas_do_dia(date(2026, 11, 10)))
        self.assertIn("fisica", professor.trilhas_do_dia(date(2026, 11, 7)))
        m = professor.modulo("o-dotnet")
        self.assertTrue(any("Alura" in ln for ln in professor.entrada(m)))
        backup = professor.entrada(professor.modulo("s-backup"))
        self.assertTrue(any("Akitando] #146" in ln for ln in backup), backup)
        pedido = professor.pedido_aula(m)
        self.assertIn("Não resuma o curso nem o livro", pedido)
        self.assertIn("Como você ensinaria isso", pedido)

    def test_curriculo_real_coerente(self):
        cur = professor.curriculo()
        ids = [m["id"] for m in cur["modulos"]]
        self.assertEqual(len(ids), len(set(ids)))
        eco = json.loads((professor.RAIZ / "data" / "ecossistema.json").read_text(encoding="utf-8"))
        blocos = {b["id"] for b in eco["blocos"]}
        for m in cur["modulos"]:
            self.assertIn(m["trilha"], professor.TRILHAS)
            self.assertTrue(any(m["trilha"] in dia for dia in professor.SEMANA.values()), m["trilha"])
            self.assertTrue(set(m["prereq"]) <= set(ids), m["id"])
            self.assertTrue(set(m["blocos"]) <= blocos, m["id"])
            self.assertGreaterEqual(len(m["objetivos"]), 3)
        pedido = professor.pedido_aula(cur["modulos"][0])
        self.assertIn("Perguntas de recuperação", pedido)
        self.assertNotIn("{titulo}", pedido)


if __name__ == "__main__":
    unittest.main()
