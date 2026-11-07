import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from avaliar import avaliar_pasta, licenca, preparar, tecnologia  # noqa: E402

BOM = """<!doctype html><html lang="pt-BR"><head><title>Padaria Pão Quente em Barbacena</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Padaria artesanal em Barbacena: pães, bolos e encomendas para festas. Peça pelo WhatsApp.">
<meta property="og:image" content="og.jpg"></head><body><h1>Padaria Pão Quente</h1>
<a href="https://wa.me/5532999999999">WhatsApp</a><a href="tel:+5532999999999">Ligar</a>
<a href="https://www.google.com/maps/place/x">Mapa</a><a href="sobre.html">Sobre</a>
<img src="a.jpg" alt="Pães"><section>Cardápio de bolos · Depoimentos · Encomenda e orçamento</section><form></form></body></html>"""


class TestAvaliador(unittest.TestCase):
    def test_template_bom_e_util(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "padaria-pao"
            p.mkdir()
            (p / "index.html").write_text(BOM, encoding="utf-8")
            (p / "sobre.html").write_text("<html></html>", encoding="utf-8")
            (p / "LICENSE").write_text("MIT License\nPermission is hereby granted", encoding="utf-8")
            r = avaliar_pasta(p)
            self.assertEqual(r["tecnologia"], "HTML estático")
            self.assertEqual(r["licenca"], "MIT")
            self.assertIn("site-padaria", r["nichos"])
            self.assertTrue(r["veredito"].startswith("útil"), r)

    def test_sem_licenca_avisa(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / "x"
            p.mkdir()
            (p / "index.html").write_text("<html><body>oi</body></html>", encoding="utf-8")
            self.assertEqual(licenca(p), "não encontrada")
            self.assertIn("confirmar licença", avaliar_pasta(p)["veredito"])

    def test_detecta_next(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t)
            (p / "package.json").write_text(json.dumps({"dependencies": {"next": "15"}}), encoding="utf-8")
            self.assertEqual(tecnologia(p), "Next.js")

    def test_zip_com_caminho_suspeito_recusado(self):
        with tempfile.TemporaryDirectory() as t:
            z = Path(t) / "mau.zip"
            with zipfile.ZipFile(z, "w") as zf:
                zf.writestr("../fora.txt", "x")
            with self.assertRaises(SystemExit):
                preparar(Path(t))


if __name__ == "__main__":
    unittest.main()
