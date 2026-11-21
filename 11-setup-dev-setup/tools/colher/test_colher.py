import os
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import colher  # noqa: E402

PREENCHIDA = {
    "Explicação": "Proposição é uma frase que é verdadeira ou falsa.",
    "Exemplo resolvido": "Negar 'chove e faz frio': não chove ou não faz frio (De Morgan).",
}
TABELA = ("| Nível | Pergunta | Resposta |\n|---|---|---|\n"
          "| N1 | O que é uma proposição? | Frase com valor verdadeiro ou falso |\n"
          "| N2 | Negue: p e q | não p ou não q |\n"
          "| n3 | Ache o erro: não(p ou q) = não p ou não q | O certo é não p e não q |\n")


def preencher(texto: str, exercicios: str = TABELA, aula_ok: bool = True) -> str:
    for nome, conteudo in PREENCHIDA.items():
        texto = texto.replace(f"## {nome}\n", f"## {nome}\n{conteudo}\n", 1)
    partes = texto.split("## Exemplo resolvido", 1)
    cauda = partes[1].replace(colher.VAZIO, "", 1)
    texto = partes[0] + "## Exemplo resolvido" + cauda
    primeira = texto.split("## Explicação", 1)
    texto = primeira[0] + "## Explicação" + primeira[1].replace(colher.VAZIO, "", 1)
    texto = texto.replace("| Nível | Pergunta | Resposta |\n|---|---|---|\n", exercicios)
    if aula_ok:
        for c in colher.CAMPOS_AULA:
            texto = texto.replace(f"- **{c}:** {colher.VAZIO}", f"- **{c}:** texto de {c}")
    return texto


class TestColher(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        os.environ["AMTECH_VAULT"] = str(base / "vault")
        os.environ["AMTECH_DIR"] = str(base / "AMtech")
        os.environ["ENSINO_TI"] = str(base / "ensino-ti")
        (base / "ensino-ti" / "tecnico-em-informatica" / "1-ano" / "logica-de-programacao").mkdir(parents=True)
        self.base = base

    def tearDown(self):
        for k in ("AMTECH_VAULT", "AMTECH_DIR", "ENSINO_TI"):
            os.environ.pop(k, None)
        self.tmp.cleanup()

    def test_ficha_nova_nao_esta_pronta(self):
        arq, nova = colher.criar_ficha("0.2")
        self.assertTrue(nova)
        self.assertIn("logica-de-programacao", arq.read_text(encoding="utf-8"))
        faltas = colher.conferir(arq.read_text(encoding="utf-8"))
        self.assertIn("seção 'Explicação' vazia", faltas)
        self.assertTrue(any(f.startswith("Exercícios: 0") for f in faltas))
        self.assertIn("Aula: falta 'Objetivo'", faltas)

    def test_criar_de_novo_nao_apaga(self):
        arq, _ = colher.criar_ficha("0.2")
        arq.write_text("meu texto", encoding="utf-8")
        _, nova = colher.criar_ficha("0.2")
        self.assertFalse(nova)
        self.assertEqual(arq.read_text(encoding="utf-8"), "meu texto")

    def test_colher_entrega_cada_secao(self):
        arq, _ = colher.criar_ficha("0.2")
        arq.write_text(preencher(arq.read_text(encoding="utf-8")), encoding="utf-8")
        self.assertEqual(colher.conferir(arq.read_text(encoding="utf-8")), [])
        r = colher.colher("0.2", hoje=date(2026, 11, 20))
        am = self.base / "AMtech"
        cap = am / "entrada" / "capitulos" / "0.2-linguagem-matematica-e-logica.md"
        self.assertIn("De Morgan", cap.read_text(encoding="utf-8"))
        yaml = (am / "banco" / "exercicios" / "0.2.yaml").read_text(encoding="utf-8")
        self.assertIn("nivel: N3", yaml)
        tsv = (am / "banco" / "anki" / "0.2.tsv").read_text(encoding="utf-8")
        self.assertIn("Negue: p e q\tnão p ou não q\tetapa-0-2 N2", tsv)
        plano = (self.base / "ensino-ti" / "tecnico-em-informatica" / "1-ano" / "logica-de-programacao"
                 / "planos-de-aula" / "0.2-linguagem-matematica-e-logica.md").read_text(encoding="utf-8")
        self.assertIn("**Prática (20 min):** texto de Prática", plano)
        self.assertEqual(r["exercicios"], 3)
        self.assertEqual(len(r["sem_repo"]), 2)  # os outros dois componentes não existem no teste
        self.assertIn("estado: colhida em 2026-11-20", arq.read_text(encoding="utf-8"))

    def test_nao_reescreve_o_que_voce_editou(self):
        arq, _ = colher.criar_ficha("0.2")
        arq.write_text(preencher(arq.read_text(encoding="utf-8")), encoding="utf-8")
        colher.colher("0.2")
        plano = next((self.base / "ensino-ti").rglob("planos-de-aula/*.md"))
        plano.write_text("editei na mão", encoding="utf-8")
        r = colher.colher("0.2")
        self.assertIn(plano, r["pulados"])
        self.assertEqual(plano.read_text(encoding="utf-8"), "editei na mão")
        colher.colher("0.2", forcar=True)
        self.assertNotEqual(plano.read_text(encoding="utf-8"), "editei na mão")

    def test_seco_nao_escreve(self):
        arq, _ = colher.criar_ficha("0.2")
        arq.write_text(preencher(arq.read_text(encoding="utf-8")), encoding="utf-8")
        r = colher.colher("0.2", seco=True)
        self.assertTrue(r["feitos"])
        self.assertFalse((self.base / "AMtech").exists())

    def test_ficha_incompleta_recusa(self):
        arq, _ = colher.criar_ficha("0.2")
        arq.write_text(preencher(arq.read_text(encoding="utf-8"), aula_ok=False), encoding="utf-8")
        with self.assertRaises(SystemExit):
            colher.colher("0.2")

    def test_nivel_invalido_recusa(self):
        with self.assertRaises(SystemExit):
            colher.exercicios("| N5 | p | r |")

    def test_etapa_desconhecida(self):
        with self.assertRaises(SystemExit):
            colher.criar_ficha("9.9")

    def test_ofertas_existem_no_portfolio(self):
        nomes = [n for n, _ in colher.ofertas_tocadas()]
        self.assertTrue(any("AM Mentor" in n for n in nomes))
        self.assertTrue(any("Mini-curso" in n for n in nomes))


if __name__ == "__main__":
    unittest.main()
