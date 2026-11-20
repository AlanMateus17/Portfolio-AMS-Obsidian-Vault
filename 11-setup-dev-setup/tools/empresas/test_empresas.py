import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import empresas  # noqa: E402


class TestEmpresas(unittest.TestCase):
    def setUp(self):
        self.e, self.p, self.s = empresas.carregar()

    def test_dados_reais_validos(self):
        self.assertEqual(empresas.validar(self.e, self.p, self.s), [])

    def test_seis_empresas_e_maker_com_campo(self):
        ids = [x["id"] for x in self.e["empresas"]]
        self.assertEqual(len(ids), 6)
        self.assertNotIn("campo", ids)
        self.assertEqual(empresas.dono_das_ofertas(self.e, self.p)["assist"], "maker")

    def test_frente_sem_empresa(self):
        e = copy.deepcopy(self.e)
        e["empresas"][0]["frentes"].remove("servicos")
        self.assertTrue(any("sem empresa" in x for x in empresas.validar(e, self.p, self.s)))

    def test_componente_em_dois_produtos(self):
        e = copy.deepcopy(self.e)
        e["empresas"][1]["produtos"][1]["componentes"].append("minicurso")
        self.assertTrue(any("dois produtos" in x for x in empresas.validar(e, self.p, self.s)))

    def test_componente_de_outra_empresa(self):
        e = copy.deepcopy(self.e)
        e["empresas"][0]["produtos"][0]["componentes"].append("minicurso")
        self.assertTrue(any("de outra empresa" in x for x in empresas.validar(e, self.p, self.s)))

    def test_software_primeiro_precisa_de_gatilho(self):
        e = copy.deepcopy(self.e)
        next(x for x in e["empresas"] if x["id"] == "logistica").pop("gatilho")
        self.assertTrue(any("gatilho" in x for x in empresas.validar(e, self.p, self.s)))

    def test_vitrine_nao_mostra_numero_interno(self):
        for x in self.e["empresas"]:
            v = empresas.gerar_vitrine(x, self.s)
            for interno in ("veredito", "onda 0", "fila com portão", "R$"):
                self.assertNotIn(interno, v, f"{x['id']}: {interno}")


if __name__ == "__main__":
    unittest.main()
