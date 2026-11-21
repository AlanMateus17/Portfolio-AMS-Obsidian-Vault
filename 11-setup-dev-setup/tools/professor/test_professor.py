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


def mock_pasta(raiz):
    import os
    from unittest import mock
    return mock.patch.dict(os.environ, {"PROFESSOR_NOTAS": str(Path(raiz) / "prof")})


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

    def test_mapa_manda_na_ordem(self):
        assuntos = {"0.1": {"titulo": "A", "depende": [], "escrito": True, "arquivo": "a.md"},
                    "0.2": {"titulo": "B", "depende": ["0.1"], "escrito": True, "arquivo": "b.md"},
                    "0.3": {"titulo": "C", "depende": ["0.2"], "escrito": False, "arquivo": None},
                    "2.1": {"titulo": "TS", "depende": ["0.3"], "escrito": False, "arquivo": None}}
        mods = [{"id": "base", "trilha": "base", "trimestre": 1, "prereq": [], "etapa": "0.1"},
                {"id": "mat", "trilha": "matematica", "trimestre": 1, "prereq": [], "etapa": "0.2"},
                {"id": "conj", "trilha": "matematica", "trimestre": 1, "prereq": [], "etapa": "0.3"},
                {"id": "ts", "trilha": "oficio", "trimestre": 1, "prereq": [], "etapa": "2.1"},
                {"id": "fis", "trilha": "fisica", "trimestre": 1, "prereq": [], "etapa": None}]
        pl = professor.plano_do_dia(mods, {}, assuntos=assuntos)
        self.assertEqual([m["id"] for m in pl["fila"]], ["base", "fis"], "0.2 espera o 0.1; 0.3 e 2.1 não estão escritos")
        self.assertNotIn("oficio", pl["proximos"], "TypeScript não entra antes da base")
        self.assertEqual(pl["a_escrever"], ["0.3"])
        self.assertIn("não foi escrito", professor.bloqueio(mods[3], mods, {}, assuntos))
        self.assertIn("base", professor.bloqueio(mods[1], mods, {}, assuntos))
        pl = professor.plano_do_dia(mods, {"base": {"nivel": 3}}, assuntos=assuntos)
        self.assertEqual(pl["proximos"]["matematica"]["id"], "mat")
        self.assertEqual(professor.plano_do_dia(mods, {}, assuntos={})["proximos"]["oficio"]["id"], "ts",
                         "sem o retrato do mapa, vale só o pré-requisito do módulo")

    def test_curriculo_real_comeca_pela_base(self):
        pl = professor.plano_do_dia(professor.curriculo()["modulos"], {}, assuntos=professor.assuntos_mapa())
        etapas = {m.get("etapa") for m in pl["fila"]}
        self.assertIn("0.1", etapas)
        self.assertTrue(etapas <= {"0.1", None}, f"sem nada dominado, só o 0.1 (e a física) liberam: {etapas}")

    def test_motor_ausente_avisa_em_portugues(self):
        from unittest import mock
        with mock.patch.object(professor.subprocess, "run", side_effect=FileNotFoundError):
            with self.assertRaises(professor.MotorAusente) as ctx:
                professor.rodar("claude", "x")
        self.assertIn("--motor imprimir", str(ctx.exception))
        self.assertEqual(professor.rodar("imprimir", "pedido"), "pedido")
        falha = professor.subprocess.CalledProcessError(1, ["claude"], stderr="not logged in")
        with mock.patch.object(professor.subprocess, "run", side_effect=falha):
            with self.assertRaises(ValueError) as ctx:
                professor.rodar("claude", "x")
        self.assertIn("not logged in", str(ctx.exception))

    def test_migra_ids_antigos(self):
        professor.subir(self.con, "o-csharp", 2)
        with mock_pasta(self.tmp.name):
            professor.migrar_ids(self.con)
        nv = professor.niveis(self.con)
        self.assertNotIn("o-csharp", nv)
        self.assertEqual(nv["o-typescript"]["nivel"], 2)

    def test_nota_sem_ia_libera_o_proximo(self):
        import os
        from unittest import mock
        banco = Path(self.tmp.name) / "cli.db"
        with mock_pasta(self.tmp.name), mock.patch.dict(os.environ, {"NUCLEO_DB": str(banco)}):
            self.assertEqual(professor.main(["nota", "b-aprender", "90"]), 0)
            self.assertEqual(professor.main(["nota", "b-aprender", "120"]), 2, "nota fora de 0 a 100")
        con = nuc.abrir(banco)
        self.assertEqual(professor.niveis(con)["b-aprender"]["nivel"], 3)
        pl = professor.plano_do_dia(professor.curriculo()["modulos"], professor.niveis(con), assuntos=professor.assuntos_mapa())
        con.close()
        self.assertIn("mat-linguagem", [m["id"] for m in pl["fila"]], "passou no 0.1: o 0.2 libera")

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
        self.assertIn("matematica", professor.trilhas_do_dia(date(2026, 11, 13)))
        self.assertEqual(professor.trilhas_do_dia(date(2026, 11, 10)), ("base",), "terça é o slot curto do Akita")
        self.assertIn("fisica", professor.trilhas_do_dia(date(2026, 11, 7)))
        m = professor.modulo("o-ts-projeto")
        self.assertEqual(professor.modulo("o-dotnet")["id"], "o-ts-projeto", "id antigo ainda resolve")
        self.assertTrue(any("Alura" in ln for ln in professor.entrada(m)))
        backup = professor.entrada(professor.modulo("s-backup"))
        self.assertTrue(any("Akitando] #146" in ln for ln in backup), backup)
        pedido = professor.pedido_aula(m)
        self.assertIn("Não resuma o curso nem o livro", pedido)
        self.assertIn("Como você ensinaria isso", pedido)
        self.assertIn("em TypeScript → em Python", pedido, "ADR 0017: C# não é mais o segundo jeito")
        self.assertNotIn("em C#", pedido)

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

    def test_modulos_ligados_ao_mapa_existem(self):
        ids = {m["id"] for m in professor.curriculo()["modulos"]}
        aulas = json.loads((professor.RAIZ / "data" / "aulas.json").read_text(encoding="utf-8"))
        for etapa, info in aulas["etapas"].items():
            if info.get("professor"):
                self.assertIn(info["professor"], ids, etapa)
                self.assertEqual(professor.etapa_do_modulo(info["professor"]), etapa)
        self.assertIsNone(professor.etapa_do_modulo("modulo-que-nao-existe"))


if __name__ == "__main__":
    unittest.main()
