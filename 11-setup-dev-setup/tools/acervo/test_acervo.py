import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

import regras

AQUI = Path(__file__).resolve().parent


class TestRegras(unittest.TestCase):
    def test_nome_base_junta_copias(self):
        self.assertEqual(regras.nome_base("Aula-01 (2).docx"), regras.nome_base("Aula-01.docx"))
        self.assertEqual(regras.nome_base("Apostila-Terminal-3.docx"), "apostila-terminal")

    def test_pessoal_pelo_nome(self):
        self.assertEqual(regras.classificar_direitos("contracheque_202605.pdf", "")[0], "pessoal")
        self.assertEqual(regras.classificar_direitos("Nubank_2026-10-12.csv", "")[0], "pessoal")

    def test_pessoal_pelo_conteudo(self):
        texto = "Fulano 111.222.333-44\nBeltrano 555.666.777-88"
        self.assertEqual(regras.classificar_direitos("lista.docx", texto)[0], "pessoal")

    def test_terceiros(self):
        s, m = regras.classificar_direitos("Arduino pratico (Casa do Codigo).pdf", "Todos os direitos reservados")
        self.assertEqual(s, "terceiros")
        self.assertEqual(regras.classificar_direitos("Competente-o-Suficiente-ebook.pdf", "texto")[0], "terceiros")

    def test_seu_material_que_cita_plataformas_continua_seu(self):
        texto = "Meu plano de estudos: Alura, Udemy e DIO. Autor: Alan Mateus"
        self.assertEqual(regras.classificar_direitos("plano-estudos.md", texto)[0], "proprio")

    def test_escola_e_dado_de_aluno(self):
        s, m = regras.classificar_direitos("Prova.docx", "EMTI - Escola Estadual\nAluno: Maria\nQuestão 1")
        self.assertEqual(s, "escola")
        self.assertTrue(any("dados pessoais" in x for x in m))

    def test_tema_e_tipo(self):
        self.assertEqual(regras.tema("Aula01_LogicaProg_Aluno.pdf", "fluxograma e algoritmo"), "logica")
        self.assertEqual(regras.tipo("Gabarito_Prova_LabSoftware.docx"), "gabarito")
        self.assertEqual(regras.tipo("Exercicios_Resolvidos_Fluxograma.docx"), "exercicios")
        self.assertEqual(regras.tipo("Apostila-Terminal-Bash.docx"), "apostila")
        self.assertEqual(regras.tema("Apostila-Terminal-Bash-PowerShell-Docker.docx", "docker e git no terminal"), "terminal")
        self.assertEqual(regras.tema("Gabarito_Prova_LabSoftware.docx", "git e terminal"), "labsoft")
        self.assertEqual(regras.tema("Aula01_SO_Aluno.pdf", "processos e threads"), "so")
        self.assertEqual(regras.tema("Aula01_HTMLCSS_Aluno.pdf", ""), "htmlcss")

    def test_produtos_ignoram_terceiros_pessoais_e_copias(self):
        base = {"tema": "logica", "motivos": []}
        itens = [dict(base, tipo="aula", situacao="proprio", origem=f"a{i}") for i in range(3)]
        itens += [dict(base, tipo="aula", situacao="terceiros", origem="t"), dict(base, tipo="aula", situacao="proprio", origem="c", duplicado_de="a0")]
        prods = regras.sugerir_produtos(itens)
        curso = [p for p in prods if p["produto"].startswith("Mini-curso")]
        self.assertEqual(len(curso), 1)
        self.assertEqual(curso[0]["documentos"], 3)


class TestPonta(unittest.TestCase):
    def test_acervo_de_ponta_a_ponta_com_markdown(self):
        with tempfile.TemporaryDirectory() as t:
            t = Path(t)
            o = t / "origem"
            (o / "aulas").mkdir(parents=True)
            for i in range(1, 4):
                (o / "aulas" / f"Aula0{i}_LogicaProg.md").write_text(f"# Aula {i}\nalgoritmo e fluxograma {i}\nAutor: Alan", encoding="utf-8")
            (o / "aulas" / "Aula01_LogicaProg (1).md").write_text("# Aula 1\nalgoritmo e fluxograma 1\nAutor: Alan", encoding="utf-8")
            (o / "contracheque_202601.txt").write_text("salário", encoding="utf-8")
            (o / "instalador.exe").write_bytes(b"MZ")
            with zipfile.ZipFile(o / "pacote.zip", "w") as z:
                z.writestr("Apostila-Logica.md", "# Apostila\nalgoritmo, fluxograma, pseudocódigo")
                z.writestr("../fora.md", "zip-slip")
            r = subprocess.run([sys.executable, str(AQUI / "acervo.py"), "--origem", str(o), "--vault", str(t / "vault"), "--dados", str(t / "dados")],
                               capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr)
            cat = json.loads((t / "dados" / "catalogo.json").read_text(encoding="utf-8"))
            self.assertEqual(sum(1 for i in cat if i.get("duplicado_de")), 1)
            self.assertEqual([i["situacao"] for i in cat if "contracheque" in i["nome"]], ["pessoal"])
            self.assertFalse(any("contracheque" in str(p) for p in (t / "vault").rglob("*")))
            self.assertFalse((t / "fora.md").exists())
            mds = list((t / "vault" / "30-Acervo" / "logica").glob("*.md"))
            self.assertEqual(len(mds), 4)
            self.assertTrue(mds[0].read_text(encoding="utf-8").startswith("---\ntitulo:"))
            rel = (t / "vault" / "40-Produtos" / "Produtos do acervo.md").read_text(encoding="utf-8")
            self.assertIn("Mini-curso de Lógica de Programação", rel)
            fora = json.loads((t / "dados" / "fora.json").read_text(encoding="utf-8"))
            self.assertEqual([f["origem"] for f in fora], ["instalador.exe"])
            # segunda rodada não reconverte
            r2 = subprocess.run([sys.executable, str(AQUI / "acervo.py"), "--origem", str(o), "--vault", str(t / "vault"), "--dados", str(t / "dados")],
                                capture_output=True, text=True)
            self.assertEqual(r2.returncode, 0, r2.stderr)
            cat2 = json.loads((t / "dados" / "catalogo.json").read_text(encoding="utf-8"))
            self.assertTrue(any(i.get("reaproveitado") for i in cat2))


if __name__ == "__main__":
    unittest.main()
