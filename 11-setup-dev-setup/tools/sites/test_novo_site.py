import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import novo_site  # noqa: E402

CAMPOS = {"id", "nome", "sigla", "dominio", "descricao", "chamada", "titulo", "subtitulo", "acao_principal", "secoes",
          "ofertas", "passos", "sobre", "contato", "tokens", "legal", "texto_sem_preco"}
CORES = {"fundo", "superficie", "tinta", "suave", "linha", "principal", "sobre_principal", "destaque"}


class TestSites(unittest.TestCase):
    def test_marcas_completas(self):
        for arq in sorted(novo_site.MARCAS.glob("*.json")):
            m = json.loads(arq.read_text(encoding="utf-8"))
            self.assertEqual(m["id"], arq.stem)
            self.assertTrue(CAMPOS <= set(m), f"{arq.stem}: falta {CAMPOS - set(m)}")
            self.assertTrue(CORES <= set(m["tokens"]) and CORES <= set(m["tokens"]["escuro"]), arq.stem)
            self.assertTrue(m["ofertas"] and m["passos"] and m["legal"]["termos"] and m["legal"]["dados"], arq.stem)
            self.assertNotRegex(json.dumps(m, ensure_ascii=False), r"\d{3}\.\d{3}\.\d{3}-\d{2}", "CPF nunca vai para o site")

    def test_pendencias_e_pronto(self):
        m = novo_site.carregar("amtech")
        self.assertTrue(any("dominio" in p for p in novo_site.pendencias(m)))
        m.update(dominio="exemplo.com.br", analytics={"umami": {"script": "x", "id": "y"}})
        m["contato"]["email"] = "contato@exemplo.com.br"
        m["legal"]["email_privacidade"] = "contato@exemplo.com.br"
        for o in m["ofertas"]:
            o["preco"] = "R$ 1"
        self.assertEqual(novo_site.pendencias(m), [])

    def test_gerar_e_atualizar_sem_apagar(self):
        with tempfile.TemporaryDirectory() as t:
            d = Path(t) / "site"
            novo_site.gerar("instituto", d)
            self.assertEqual(json.loads((d / "src" / "marca.json").read_text())["nome"], "Instituto AMS Silva")
            self.assertTrue((d / "src" / "pages" / "privacidade.astro").exists())
            (d / "LEIA.md").write_text("meu")
            (d / "src" / "pages" / "extra.astro").write_text("x")
            novo_site.gerar("instituto", d)
            self.assertEqual((d / "LEIA.md").read_text(), "meu", "não sobrescreve o LEIA do site")
            self.assertTrue((d / "src" / "pages" / "extra.astro").exists(), "página própria do site fica")

    def test_marca_inexistente(self):
        with self.assertRaises(ValueError):
            novo_site.carregar("nada")


if __name__ == "__main__":
    unittest.main()
