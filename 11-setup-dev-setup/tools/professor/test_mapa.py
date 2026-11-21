"""Professor × mapa-de-estudo: todo módulo aponta para um assunto que existe e a ordem não contraria os pré-requisitos."""
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import mapa  # noqa: E402

MD = """
## Etapa 1

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 1.1 | Base | x | x | 1 | — | 📘 [a](assuntos/a.md) |
| 1.2 | ↻ Meio | x | x | 1 | 1.1, física T1 | 📝 |

## H7

| # | Assunto | Conceitos | Depende de |
|---|---|---|---|
| H7.1 | Topo | x | 1.2 |
"""


def mod(i, etapa, trimestre=1, prereq=()):
    return {"id": i, "etapa": etapa, "trimestre": trimestre, "prereq": list(prereq)}


class TestMapa(unittest.TestCase):
    def setUp(self):
        self.a = mapa.ler_mapa(MD)

    def test_le_tabelas_de_formatos_diferentes(self):
        self.assertEqual(set(self.a), {"1.1", "1.2", "H7.1"})
        self.assertEqual(self.a["1.2"], {"titulo": "Meio", "depende": ["1.1"], "escrito": False, "arquivo": None})
        self.assertEqual((self.a["1.1"]["escrito"], self.a["1.1"]["arquivo"]), (True, "assuntos/a.md"))
        self.assertFalse(self.a["H7.1"]["escrito"], "horizonte não tem coluna Arquivo")
        self.assertEqual(self.a["H7.1"]["depende"], ["1.2"])

    def test_assunto_inexistente_falha(self):
        erros = mapa.conferir({"modulos": [mod("x", "9.9")]}, self.a)
        self.assertTrue(any("não existe" in e for e in erros))

    def test_etapa_nula_exige_motivo(self):
        self.assertTrue(mapa.conferir({"modulos": [mod("x", None)]}, self.a))
        m = mod("x", None) | {"etapa_motivo": "fora das tabelas"}
        self.assertEqual(mapa.conferir({"modulos": [m]}, self.a), [])

    def test_ordem_contraria_ao_mapa_falha(self):
        erros = mapa.conferir({"modulos": [mod("topo", "H7.1", 1), mod("base", "1.1", 2)]}, self.a)
        self.assertTrue(any("depende de 1.1" in e for e in erros))
        erros = mapa.conferir({"modulos": [mod("base", "1.1", prereq=["topo"]), mod("topo", "H7.1")]}, self.a)
        self.assertTrue(any("pré-requisito" in e for e in erros))

    def test_ordem_certa_passa(self):
        c = {"modulos": [mod("base", "1.1", 1), mod("topo", "H7.1", 2, ["base"])]}
        self.assertEqual(mapa.conferir(c, self.a), [])

    def test_curriculo_real_alinhado_ao_retrato(self):
        c = json.loads(mapa.CURRICULO.read_text(encoding="utf-8"))
        a = json.loads(mapa.RETRATO.read_text(encoding="utf-8"))["assuntos"]
        self.assertEqual(mapa.conferir(c, a), [])
        self.assertEqual(len([m for m in c["modulos"] if m["etapa"] is None]), 2)  # só os de física

    def test_cobertura(self):
        c = mapa.cobertura({"modulos": [mod("base", "1.1")]}, self.a)
        self.assertEqual((c["total"], c["com_modulo"], c["escritos"], c["escritos_sem_modulo"]), (3, 1, 1, []))
        c = mapa.cobertura({"modulos": [mod("topo", "H7.1")]}, self.a)
        self.assertEqual(c["escritos_sem_modulo"], ["1.1"])

    def test_aulas_json_concorda_com_etapa(self):
        c = {m["id"]: m["etapa"] for m in json.loads(mapa.CURRICULO.read_text(encoding="utf-8"))["modulos"]}
        aulas = json.loads((mapa.RAIZ / "data" / "aulas.json").read_text(encoding="utf-8"))["etapas"]
        for etapa, info in aulas.items():
            if info.get("professor"):
                self.assertEqual(c[info["professor"]], etapa, info["professor"])


if __name__ == "__main__":
    unittest.main()
