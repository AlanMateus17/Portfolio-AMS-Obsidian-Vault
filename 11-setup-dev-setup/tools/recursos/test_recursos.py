import copy
import unittest

import recursos


class TesteRecursos(unittest.TestCase):
    def setUp(self):
        self.d, self.eco = recursos.carregar()

    def test_dados_validos(self):
        self.assertEqual(recursos.validar(self.d, self.eco), [])

    def test_bloco_inexistente(self):
        d = copy.deepcopy(self.d)
        d["ferramentas"][0]["bloco"] = "naoexiste"
        self.assertTrue(any("não existe" in x for x in recursos.validar(d, self.eco)))

    def test_rota_sem_reserva(self):
        d = copy.deepcopy(self.d)
        d["rotas"][0]["reserva"] = " "
        self.assertTrue(any("reserva" in x for x in recursos.validar(d, self.eco)))

    def test_decisao_invalida(self):
        d = copy.deepcopy(self.d)
        d["ferramentas"][0]["recursos"][0]["decisao"] = "talvez"
        self.assertTrue(any("decisão inválida" in x for x in recursos.validar(d, self.eco)))

    def test_gera_tabelas(self):
        t = recursos.gerar(self.d)
        self.assertIn("| Tarefa | Primária | Reserva | Portão |", t)
        self.assertIn("## Esteira de sites", t)


if __name__ == "__main__":
    unittest.main()
