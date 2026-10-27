import copy
import unittest

from gerar import carregar, carregar_eco, gerar_html, gerar_md, quando_por_bloco, validar


class TestImplantacao(unittest.TestCase):
    def setUp(self):
        self.d = carregar()
        self.eco = carregar_eco()

    def test_dados_reais_validos(self):
        self.assertEqual(validar(self.d), [])

    def test_detecta_id_repetido(self):
        d = copy.deepcopy(self.d)
        d["fases"][1]["passos"].append(copy.deepcopy(d["fases"][0]["passos"][0]))
        self.assertTrue(any("repetido" in e for e in validar(d)))

    def test_detecta_script_inexistente(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["comando"] = "bash scripts/wsl/nao-existe.sh"
        self.assertTrue(any("não existe" in e for e in validar(d)))

    def test_todo_passo_aparece_no_roteiro_com_criterio(self):
        md = gerar_md(self.d)
        for f in self.d["fases"]:
            for p in f["passos"]:
                self.assertIn(p["titulo"], md)
                self.assertIn(p["pronto"], md)

    def test_todo_bloco_do_setup_esta_num_passo_com_quando(self):
        qb = quando_por_bloco(self.d)
        faltam = [b["id"] for b in self.eco["blocos"] if b["id"] not in qb]
        self.assertEqual(faltam, [])
        self.assertTrue(all(f.get("quando") for f in self.d["fases"]))

    def test_detecta_bloco_fora_do_roteiro(self):
        d = copy.deepcopy(self.d)
        for f in d["fases"]:
            for p in f["passos"]:
                p["blocos"] = [b for b in p["blocos"] if b != "kee"]
        self.assertTrue(any("kee" in e and "fora do roteiro" in e for e in validar(d, self.eco)))

    def test_detecta_bloco_novo_no_setup_mesmo_futuro(self):
        eco = copy.deepcopy(self.eco)
        eco["blocos"].append({"id": "novo", "camada": "win", "rotulo": "Programa novo", "tipo": "local",
                              "conta": False, "futuro": True, "descricao": "x"})
        self.assertTrue(any("novo" in e for e in validar(self.d, eco)))

    def test_detecta_bloco_inexistente_e_fase_sem_quando(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["blocos"].append("naoexiste")
        d["fases"][1]["quando"] = ""
        erros = validar(d, self.eco)
        self.assertTrue(any("naoexiste" in e for e in erros))
        self.assertTrue(any("sem 'quando'" in e for e in erros))

    def test_toda_oferta_do_portfolio_tem_passo(self):
        d = copy.deepcopy(self.d)
        for f in d["fases"]:
            for p in f["passos"]:
                p["ofertas"] = [o for o in p.get("ofertas", []) if o != "minicurso"]
        self.assertTrue(any("minicurso" in e and "sem passo" in e for e in validar(d, self.eco)))
        d["fases"][0]["passos"][0]["ofertas"] = ["minicurso", "naoexiste"]
        self.assertTrue(any("naoexiste" in e for e in validar(d, self.eco)))

    def test_comeca_pelo_diagnostico_e_tem_primeira_venda(self):
        self.assertTrue(self.d["fases"][0]["titulo"].startswith("Diagnóstico"))
        self.assertTrue(any(p["id"] == "mc-primeira-venda" for f in self.d["fases"] for p in f["passos"]))

    def test_precisa_invalido_e_resumo_de_hoje(self):
        d = copy.deepcopy(self.d)
        d["fases"][0]["passos"][0]["precisa"] = ["sorte"]
        self.assertTrue(any("precisa inválido" in e for e in validar(d, self.eco)))
        self.assertIn("Dá para fazer hoje", gerar_md(self.d, self.eco))

    def test_roteiro_e_pagina_mostram_cobertura(self):
        md, html = gerar_md(self.d, self.eco), gerar_html(self.d, self.eco)
        self.assertIn("## Quando entra cada bloco", md)
        self.assertIn("Implanta: KeePassXC", md)
        self.assertIn('"implanta"', html)
        self.assertNotIn("__DATA__", html)


if __name__ == "__main__":
    unittest.main()
