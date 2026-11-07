import copy
import unittest
from pathlib import Path

import orcamento

MODELO = Path(__file__).resolve().parent / "orcamento.example.toml"


class TesteOrcamento(unittest.TestCase):
    def setUp(self):
        self.d = orcamento.carregar(MODELO)

    def test_modelo_valido(self):
        self.assertEqual(orcamento.validar(self.d), [])

    def test_item_de_venda_fica_fora(self):
        r = orcamento.resumir(self.d)
        nomes = [it["nome"] for it in r["itens"]]
        self.assertFalse(any("produção" in n for n in nomes))
        self.assertTrue(any("produção" in n for n in r["fora_venda"]))

    def test_separa_unico_de_recorrente(self):
        r = orcamento.resumir(self.d)
        # Claude Pro (110) + GPU (0) são recorrentes; software único = 0
        self.assertEqual(r["por_categoria"]["software"]["mes"][0], 110)
        self.assertEqual(r["por_categoria"]["software"]["unico"][1], 0)
        # hardware é tudo compra única
        self.assertEqual(r["por_categoria"]["hardware"]["mes"], [0.0, 0.0])
        self.assertGreater(r["por_categoria"]["hardware"]["unico"][0], 0)

    def test_faixa_min_max(self):
        r = orcamento.resumir(self.d)
        lo, hi = r["unico"]
        self.assertLess(lo, hi)  # há itens com custo_max

    def test_filtra_por_etapa(self):
        r = orcamento.resumir(self.d, etapa=2)
        self.assertTrue(all(it.get("etapa", 1) == 2 for it in r["itens"]))
        self.assertEqual(r["mes"], [0.0, 0.0])  # etapa 2 não tem recorrente

    def test_categoria_invalida(self):
        d = copy.deepcopy(self.d)
        d["item"][0]["categoria"] = "servico"
        self.assertTrue(any("categoria inválida" in e for e in orcamento.validar(d)))

    def test_custo_max_menor_que_custo(self):
        d = copy.deepcopy(self.d)
        d["item"][2]["custo_max"] = 1  # menor que o custo
        self.assertTrue(any("custo_max" in e for e in orcamento.validar(d)))

    def test_markdown(self):
        md = orcamento.markdown(orcamento.resumir(self.d))
        self.assertIn("## Total", md)
        self.assertIn("## Por etapa", md)
        self.assertIn("Claude Pro", md)
        self.assertIn("são para vender", md)


if __name__ == "__main__":
    unittest.main()
