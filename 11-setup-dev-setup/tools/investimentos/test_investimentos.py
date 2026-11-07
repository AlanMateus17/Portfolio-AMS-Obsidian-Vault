import copy
import unittest
from pathlib import Path

import investimentos as inv

M = Path(inv.__file__).parent / "modelos"


def cfg_aberto():
    c = inv.carregar_config(M / "investimentos.example.toml")
    c["portao"] = {"cartao_zerado": True, "reserva_completa": True}
    c["mercado"]["ntnb_juro_real"] = 6.5
    return c


class TesteInvestimentos(unittest.TestCase):
    def setUp(self):
        self.d = inv.carregar()
        self.cfg = cfg_aberto()

    def test_dados_validos(self):
        self.assertEqual(inv.validar(self.d), [])

    def test_quatro_classes(self):
        self.assertEqual([c["id"] for c in self.d["classes"]], ["acoes", "fiis", "caixa", "internacional"])

    def test_alocacao_precisa_bater_com_metodologias(self):
        d = copy.deepcopy(self.d)
        d["classes"][1]["alocacao_padrao"]["inexistente"] = 0
        self.assertTrue(any("exatamente" in x for x in inv.validar(d)))

    def test_herda_criterios(self):
        b = next(m for m in inv.classe(self.d, "internacional")["metodologias"] if m["id"] == "buffett_ext")
        self.assertEqual(len(b["criterios"]), 3)
        self.assertEqual(b["criterios"][0]["aplica_se"], {"tipo": ["acao", "bdr"]})

    def test_formulas(self):
        l = {"dividendo_medio": "1,6", "lpa": "2.5", "vpa": "15", "crescimento_dividendos": "4"}
        self.assertEqual(inv.teto(l, 6), 26.67)
        self.assertEqual(inv.valor_graham(l), 29.05)
        self.assertEqual(inv.preco_gordon(l, {"mercado": {"retorno_exigido": 12}}), 20.8)
        self.assertIsNone(inv.preco_gordon(l, {"mercado": {"retorno_exigido": 3}}))

    def test_equivalente_isento(self):
        self.assertEqual(inv.equiv_cdi({"taxa": "92", "isento": "sim", "vencimento_dias": "730"}), 108.2)
        self.assertEqual(inv.equiv_cdi({"taxa": "100", "isento": "não"}), 100)
        self.assertEqual(inv.ir_regressivo(100), 22.5)

    def test_acoes_todas_as_metodologias(self):
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores_acoes.example.csv"), self.d, "acoes", self.cfg)}
        self.assertEqual(r["EXEM3"]["bazin"], "passa")
        self.assertEqual(r["EXEM3"]["sena"], "passa")
        self.assertEqual(r["FICT3"]["formula_magica"], inv.NA)  # bancos ficam fora
        self.assertEqual(r["EXEM3"]["classificacao"], "forte")
        self.assertEqual(r["TEST4"]["classificacao"], "fraco")

    def test_fiis(self):
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores_fiis.example.csv"), self.d, "fiis", self.cfg)}
        self.assertEqual(r["LOGX11"]["desconto_pvp"], "passa")
        self.assertEqual(r["LOGX11"]["papel_credito"], inv.NA)
        self.assertEqual(r["PAPR11"]["papel_credito"], "passa")
        self.assertEqual(r["PAPR11"]["premio_ntnb"], "passa")
        self.assertEqual(r["SHOP11"]["barsi_fii"], "não")

    def test_caixa(self):
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores_caixa.example.csv"), self.d, "caixa", self.cfg)}
        self.assertEqual(r["TESOURO-SELIC"]["liquidez"], "passa")
        self.assertEqual(r["IPCA-2035"]["inflacao"], "passa")
        self.assertEqual(r["LCI-BANCOX-2Y"]["escada"], "passa")
        self.assertEqual(r["DEB-EMPY"]["credito_seguro"], "não")

    def test_internacional(self):
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores_internacional.example.csv"), self.d, "internacional", self.cfg)}
        self.assertEqual(r["WRLD"]["bogle"], "passa")
        self.assertEqual(r["WRLD"]["buffett_ext"], inv.NA)
        self.assertEqual(r["ARIS"]["aristocratas"], "passa")
        self.assertEqual(r["REIT"]["reits"], "passa")

    def test_sem_ntnb_fica_sem_dado(self):
        c = cfg_aberto()
        c["mercado"]["ntnb_juro_real"] = 0
        r = {x["ticker"]: x for x in inv.avaliar(inv.ler_csv(M / "indicadores_fiis.example.csv"), self.d, "fiis", c)}
        self.assertEqual(r["LOGX11"]["premio_ntnb"], "sem dado")

    def test_portao_fechado(self):
        c = inv.carregar_config(M / "investimentos.example.toml")
        avisos, div = inv.aporte(inv.ler_csv(M / "carteira.example.csv"), 800, c, self.d)
        self.assertEqual(div, {})
        self.assertIn("Portão fechado", avisos[0])

    def test_aporte_dois_niveis(self):
        avisos, div = inv.aporte(inv.ler_csv(M / "carteira.example.csv"), 800, self.cfg, self.d)
        self.assertNotIn("caixa", div)  # caixa já está acima de 25%
        total = sum(v for mets in div.values() for v in mets.values())
        self.assertAlmostEqual(total, 800, delta=1)
        self.assertIn("fiis", div)
        self.assertTrue(any("escada tem menos de 3" in a for a in avisos) or "caixa" not in div)

    def test_sem_migalhas(self):
        avisos, div = inv.aporte(inv.ler_csv(M / "carteira.example.csv"), 800, self.cfg, self.d)
        fatias = [v for mets in div.values() for v in mets.values()]
        self.assertTrue(all(f >= 100 for f in fatias))
        self.assertEqual(inv.juntar_pequenos({"a": 60, "b": 400, "c": 200}, 100), {"b": 440.0, "c": 220.0})

    def test_comparar_por_classe(self):
        o = inv.comparar(inv.ler_csv(M / "carteiras.example.csv"))
        self.assertIn("acoes / barsi: +12.0% (+4.0 p.p. contra o índice)", o)
        self.assertIn("fiis / bazin_fii: +7.0% (+4.0 p.p. contra o índice)", o)

    def test_docs(self):
        t = inv.gerar(self.d)
        for x in ("Não é recomendação", "Real estate", "Caixa / renda fixa", "Internacional", "consenso"):
            self.assertIn(x, t)


if __name__ == "__main__":
    unittest.main()
