import unittest

from tabela_verdade import Parser, tabela, tokens, markdown, latex


def tipo(expr):
    return tabela(expr)[4]


class TestTabelaVerdade(unittest.TestCase):
    def test_classificacao(self):
        self.assertEqual(tipo("p | ~p"), "tautologia")
        self.assertEqual(tipo("p & ~p"), "contradição")
        self.assertEqual(tipo("p -> q"), "contingência")

    def test_equivalencias_classicas(self):
        self.assertEqual(tipo("(p -> q) <-> (~q -> ~p)"), "tautologia")  # contrapositiva
        self.assertEqual(tipo("~(p & q) <-> (~p | ~q)"), "tautologia")  # De Morgan
        self.assertEqual(tipo("(p -> q) <-> (~p | q)"), "tautologia")
        self.assertEqual(tipo("(p ^ q) <-> ~(p <-> q)"), "tautologia")

    def test_condicional_associa_a_direita(self):
        a = Parser(tokens("p -> q -> r")).tudo()
        self.assertEqual(a.texto(), "p → (q → r)")

    def test_precedencia(self):
        a = Parser(tokens("~p & q | r")).tudo()
        self.assertEqual(a.texto(), "(¬p ∧ q) ∨ r")

    def test_simbolos_unicode(self):
        self.assertEqual(tipo("(p → q) ↔ (¬q → ¬p)"), "tautologia")

    def test_linhas_e_ordem(self):
        _, vs, _, linhas, _ = tabela("p & q")
        self.assertEqual(vs, ["p", "q"])
        self.assertEqual([l[-1] for l in linhas], [True, False, False, False])

    def test_saidas(self):
        self.assertIn("**tautologia**", markdown("p | ~p"))
        self.assertIn(r"\begin{tabular}", latex("p -> q"))

    def test_erros(self):
        for ruim in ["p &", "(p | q", "p $ q", "p q"]:
            with self.assertRaises(ValueError):
                tabela(ruim)


if __name__ == "__main__":
    unittest.main()
