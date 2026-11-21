"""Testes dos scripts de shell que mexem no vault: vault.sh reconhece o vault novo e padronizar-repo.sh não toca nele."""
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]


def rodar(args, home):
    env = dict(os.environ, HOME=str(home))
    return subprocess.run(["bash", *args], capture_output=True, text=True, env=env, cwd=RAIZ)


class TestVaultSh(unittest.TestCase):
    def test_reconhece_vault_pelo_plano_unico_e_nao_cria_pastas_modelo(self):
        for guia in ("PLANO-UNICO-AMtech.md", "CARTAO-voce-esta-aqui.md"):
            with tempfile.TemporaryDirectory() as t:
                v = Path(t) / "notas"
                v.mkdir()
                (v / guia).write_text("# guia\n")
                r = rodar(["scripts/wsl/vault.sh", "--pasta", str(v), "--simular"], t)
                self.assertEqual(r.returncode, 0, r.stderr)
                self.assertIn("Seu vault está em", r.stdout)
                self.assertNotIn("00-Entrada", r.stdout)

    def test_pasta_sem_guia_cai_no_modelo(self):
        with tempfile.TemporaryDirectory() as t:
            v = Path(t) / "outra"
            v.mkdir()
            r = rodar(["scripts/wsl/vault.sh", "--pasta", str(v), "--simular"], t)
            self.assertIn("não é o seu vault", r.stdout)


class TestPadronizarPulaVault(unittest.TestCase):
    def test_vault_nao_recebe_o_modelo(self):
        with tempfile.TemporaryDirectory() as t:
            v = Path(t) / "dev" / "notas"
            (v / ".git").mkdir(parents=True)
            (v / "PLANO-UNICO-AMtech.md").write_text("# plano\n")
            r = rodar(["scripts/wsl/padronizar-repo.sh", str(v)], t)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("vault do Obsidian", r.stdout)
            self.assertFalse((v / ".github").exists())
            self.assertFalse((v / ".editorconfig").exists())

    def test_repositorio_de_codigo_recebe(self):
        with tempfile.TemporaryDirectory() as t:
            repo = Path(t) / "dev" / "app"
            (repo / ".git").mkdir(parents=True)
            r = rodar(["scripts/wsl/padronizar-repo.sh", str(repo)], t)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertTrue((repo / ".editorconfig").exists())


if __name__ == "__main__":
    unittest.main()
