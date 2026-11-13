import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from downloads import destino, plano  # noqa: E402
from types import SimpleNamespace

from senhas_csv import OUTROS, configurar_bloqueio, reorganizar, dominio, gravar_no_cofre, grupo, nota_com_alerta, processar  # noqa: E402


class TestDownloads(unittest.TestCase):
    def test_tipos(self):
        self.assertEqual(destino(Path("a.PDF")), "Documentos")
        self.assertEqual(destino(Path("x.unknown")), "Outros")
        self.assertIsNone(destino(Path("Chrome Passwords.csv")))

    def test_simula_sem_mover_e_nao_sobrescreve(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p / "a.pdf").write_text("1")
            (p / "Documentos").mkdir()
            (p / "Documentos" / "a.pdf").write_text("antigo")
            mover, _ = plano(p)
            self.assertEqual(mover[0][1].name, "a (1).pdf")
            self.assertTrue((p / "a.pdf").exists())


class TestSenhas(unittest.TestCase):
    def test_dominio_e_grupo(self):
        self.assertEqual(dominio("https://www.github.com/login"), "github.com")
        self.assertEqual(grupo("nubank.com.br"), "01 Bancos e dinheiro")
        self.assertEqual(grupo("estudante.educacao.mg.gov.br"), "03 Escola (só os seus acessos)")
        self.assertEqual(grupo("acesso.gov.br"), "02 Governo")
        self.assertEqual(grupo("registro.br"), "04 Grupo AMtech Digital")
        self.assertEqual(grupo("site-desconhecido.com"), OUTROS)
        self.assertEqual(grupo("x.com"), "08 Redes")
        self.assertEqual(grupo("netflix.com"), "10 Compras e assinaturas")
        self.assertEqual(grupo("io.drivesocial.watcher.app"), OUTROS)

    def test_nota_marca_o_que_trocar(self):
        rel = {"repetidas": ["a.com"], "curtas": ["a.com"]}
        nota = nota_com_alerta({"titulo": "a.com", "nota": "minha"}, rel)
        self.assertIn("TROCAR: senha repetida", nota)
        self.assertIn("TROCAR: senha curta", nota)
        self.assertTrue(nota.endswith("minha"))

    def test_relatorio_sem_senhas(self):
        linhas = [{"titulo": "a.com", "usuario": "u", "senha": "123", "url": "", "nota": ""},
                  {"titulo": "b.com", "usuario": "u", "senha": "123", "url": "", "nota": ""},
                  {"titulo": "a.com", "usuario": "u", "senha": "123", "url": "", "nota": ""}]
        unicas, rel = processar(linhas)
        self.assertEqual(len(unicas), 2)
        self.assertEqual(rel["repetidas"], ["a.com", "b.com"])
        self.assertNotIn("123", str(rel))

    def test_grava_no_cofre_sem_senha_na_linha_de_comando(self):
        chamadas = []

        def falso(cmd, input, text, capture_output):
            chamadas.append((cmd, input))
            return SimpleNamespace(returncode=0)

        linhas = [{"titulo": "github.com", "usuario": "a", "senha": "S3GREDO", "url": "https://github.com", "nota": ""},
                  {"titulo": "github.com", "usuario": "b", "senha": "OUTRO", "url": "https://github.com", "nota": ""}]
        ok, falhas = gravar_no_cofre(linhas, {"repetidas": [], "curtas": []}, "c.kdbx", "cli", "mestre", run=falso)
        self.assertEqual((ok, falhas), (2, []))
        self.assertTrue(all("S3GREDO" not in " ".join(c) and "mestre" not in " ".join(c) for c, _ in chamadas))
        self.assertEqual(chamadas[0][1], "mestre\nS3GREDO\n")
        self.assertEqual(chamadas[1][0][-1], "06 Código e nuvem/github.com · b")

    def test_titulo_sem_barra_e_reorganizar(self):
        chamadas = []

        def falso(cmd, input, text, capture_output, **kw):
            chamadas.append(cmd)
            saida = "com.itau · a\nsite-qualquer.net\n" if cmd[1] == "ls" else ""
            return SimpleNamespace(returncode=0, stdout=saida)

        linhas = [{"titulo": "x.net", "usuario": "a", "senha": "1", "url": "", "nota": ""},
                  {"titulo": "x.net", "usuario": "Mozilla/5.0 (Linux)", "senha": "2", "url": "", "nota": ""}]
        gravar_no_cofre(linhas, {"repetidas": [], "curtas": []}, "c", "cli", "m", run=falso)
        self.assertNotIn("/5.0", chamadas[1][-1].split("/", 1)[1])
        movidos = reorganizar("c", "cli", "m", run=falso)
        self.assertEqual(movidos, [("com.itau · a", "01 Bancos e dinheiro")])

    def test_bloqueio_no_ini(self):
        with tempfile.TemporaryDirectory() as d:
            ini = Path(d) / "keepassxc.ini"
            ini.write_text("[General]\nConfigVersion=2\n\n[Security]\nLockDatabaseIdle=false\nClearClipboard=true\n", encoding="utf-8")
            configurar_bloqueio(ini, 300)
            txt = ini.read_text(encoding="utf-8")
            self.assertIn("LockDatabaseIdle=true", txt)
            self.assertIn("LockDatabaseIdleSeconds=300", txt)
            self.assertNotIn("LockDatabaseIdle=false", txt)
            self.assertIn("ClearClipboard=true", txt)
            self.assertIn("ConfigVersion=2", txt)


if __name__ == "__main__":
    unittest.main()
