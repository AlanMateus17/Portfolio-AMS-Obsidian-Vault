import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import akita  # noqa: E402

POST = """---
title: "Como fazer backup
  sem drama"
date: '2026-07-11T10:00:00-03:00'
slug: backup-sem-drama
tags:
- backup
  - linux
draft: false
---

{{< youtube id="x" >}}

Texto que importa.
```bash
rm -rf /
```
![imagem](a.webp)
Outra linha.
"""


class TestAkita(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        arq = base / "content" / "2026" / "07" / "11" / "backup-sem-drama" / "index.md"
        arq.parent.mkdir(parents=True)
        arq.write_text(POST, encoding="utf-8")
        os.environ["AKITA_REPO"] = str(base)

    def tearDown(self):
        self.tmp.cleanup()
        os.environ.pop("AKITA_REPO", None)

    def test_le_post_sem_codigo_nem_imagem(self):
        [p] = akita.ler_posts(akita.repo_local())
        self.assertEqual(p["titulo"], "Como fazer backup sem drama")
        self.assertEqual(p["url"], "https://akitaonrails.com/2026/07/11/backup-sem-drama/")
        self.assertEqual((p["categoria"], p["prioridade"], p["video"]), ("ia-e-dev-atual", 1, True))
        self.assertEqual(p["tags"], ["backup", "linux"], "tags com e sem recuo")
        self.assertNotIn("rm -rf", p["_texto"])
        self.assertNotIn("webp", p["_texto"])

    def test_opiniao_nao_vira_regra(self):
        self.assertEqual(akita.classificar({"tags": ["Off-Topic"], "title": "x"}, 2026, False)[0], "opiniao")
        [p] = akita.ler_posts(akita.repo_local())
        d = {"notas": {}, "regras": []}
        ids = akita.registrar(d, p, {"resumo": "r", "opiniao": True, "itens": [
            {"tipo": "regra", "area": "infra", "texto": "Faça backup todos os dias sempre"}]})
        self.assertEqual(ids, [])
        self.assertTrue(d["notas"]["backup-sem-drama"]["opiniao"])

    def test_registrar_sem_repetir_e_decidir(self):
        [p] = akita.ler_posts(akita.repo_local())
        d = {"notas": {}, "regras": []}
        it = {"tipo": "regra", "area": "infra", "texto": "Faça backup externo todos os dias", "aplica_ao_setup": "já faz"}
        self.assertEqual(akita.registrar(d, p, {"resumo": "r", "itens": [it, dict(it)]}), ["AK-0001"])
        self.assertEqual(akita.decidir(d, "AK-0001", "aprovada", "ok")["estado"], "aprovada")
        with self.assertRaises(ValueError):
            akita.decidir(d, "AK-0009", "aprovada")
        with self.assertRaises(ValueError):
            akita.validar_extracao({"resumo": "r", "itens": [{"tipo": "palpite", "area": "infra", "texto": "x" * 20}]})

    def test_json_no_meio_do_texto(self):
        self.assertEqual(akita.extrair_json('Claro! {"resumo": "a", "itens": []} pronto'), {"resumo": "a", "itens": []})

    def test_dados_reais_coerentes(self):
        d = akita.carregar_regras()
        ids = [r["id"] for r in d["regras"]]
        self.assertEqual(len(ids), len(set(ids)))
        for r in d["regras"]:
            self.assertIn(r["estado"], akita.ESTADOS)
            self.assertIn(r["tipo"], akita.TIPOS)
            self.assertTrue(r["fonte"]["url"].startswith("https://akitaonrails.com/"))
        indice = json.loads(akita.INDICE.read_text(encoding="utf-8"))
        self.assertTrue(all("_texto" not in p and "description" not in p for p in indice), "texto do Akita não entra no repositório")


if __name__ == "__main__":
    unittest.main()
