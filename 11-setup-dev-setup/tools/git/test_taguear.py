import unittest
import taguear

CHANGELOG = """# Changelog

## [2.8.0] - 2026-11-02
- c

## [2.7.1] - 2026-11-02
- b

## [1.24.0] - 2026-10-01
- a
"""


class TesteTaguear(unittest.TestCase):
    def test_versoes_ordem(self):
        self.assertEqual(taguear.versoes(CHANGELOG), ["1.24.0", "2.7.1", "2.8.0"])

    def test_changelog_real_tem_muitas(self):
        from pathlib import Path
        real = (Path(taguear.__file__).resolve().parents[2] / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertIn("2.8.0", taguear.versoes(real))
        self.assertGreater(len(taguear.versoes(real)), 10)

    def test_planejar_pula_existentes(self):
        taguear.commit_da_versao, orig = (lambda v: "abc123"), taguear.commit_da_versao
        try:
            vs = [v for v, _ in taguear.planejar(CHANGELOG, {"v2.8.0"})]
        finally:
            taguear.commit_da_versao = orig
        self.assertEqual(vs, ["1.24.0", "2.7.1"])

    def test_planejar_so_ultima(self):
        taguear.commit_da_versao, orig = (lambda v: "abc123"), taguear.commit_da_versao
        try:
            vs = [v for v, _ in taguear.planejar(CHANGELOG, set(), so_ultima=True)]
            vazio = taguear.planejar(CHANGELOG, {"v2.8.0"}, so_ultima=True)
        finally:
            taguear.commit_da_versao = orig
        self.assertEqual(vs, ["2.8.0"])      # só a mais nova
        self.assertEqual(vazio, [])          # já tagueada: nada a fazer


if __name__ == "__main__":
    unittest.main()
