import copy
import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path

import cvss
import escopo
import relatorio

RAIZ = Path(__file__).resolve().parents[2]
MODELOS = RAIZ / "infra" / "templates" / "seguranca"
DENTRO = dt.datetime(2027, 3, 11, 15, 0, tzinfo=dt.timezone.utc)


class TesteCVSS(unittest.TestCase):
    # Notas conferidas na calculadora oficial do FIRST.
    CASOS = {
        "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H": 9.8,
        "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H": 10.0,
        "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N": 5.5,
        "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N": 6.1,
        "CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N": 6.5,
        "CVSS:3.1/AV:P/AC:H/PR:H/UI:R/S:U/C:L/I:N/A:N": 1.6,
        "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N": 0.0,
    }

    def test_notas_oficiais(self):
        for vetor, nota in self.CASOS.items():
            with self.subTest(vetor=vetor):
                self.assertEqual(cvss.nota_base(vetor), nota)

    def test_severidade(self):
        self.assertEqual(cvss.severidade(9.8), "Crítica")
        self.assertEqual(cvss.severidade(7.0), "Alta")
        self.assertEqual(cvss.severidade(6.9), "Média")
        self.assertEqual(cvss.severidade(0.1), "Baixa")
        self.assertEqual(cvss.severidade(0.0), "Nenhuma")

    def test_roundup_da_especificacao(self):
        self.assertEqual(cvss.roundup(4.02), 4.1)
        self.assertEqual(cvss.roundup(4.0), 4.0)

    def test_vetor_invalido(self):
        for ruim in ("AV:N/AC:L", "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H", "CVSS:3.1/AV:X/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H",
                     "CVSS:3.1/AV:N/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"):
            with self.subTest(ruim=ruim), self.assertRaises(cvss.VetorInvalido):
                cvss.nota_base(ruim)


class BaseEscopo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        pasta = Path(self.tmp.name)
        (pasta / "escopo.toml").write_text((MODELOS / "escopo.example.toml").read_text(encoding="utf-8"), encoding="utf-8")
        (pasta / "autorizacao-assinada.pdf").write_bytes(b"%PDF-1.4 teste")
        self.pasta = pasta
        self.d = escopo.carregar(pasta / "escopo.toml")

    def tearDown(self):
        self.tmp.cleanup()


class TesteEscopo(BaseEscopo):
    def test_modelo_valido(self):
        self.assertEqual(escopo.validar(self.d), [])

    def test_sem_arquivo_assinado_bloqueia(self):
        (self.pasta / "autorizacao-assinada.pdf").unlink()
        ok, motivo = escopo.checar(self.d, "loja.example", DENTRO)
        self.assertFalse(ok)
        self.assertIn("assinada", motivo)

    def test_sem_quem_assinou_bloqueia(self):
        d = copy.deepcopy(self.d)
        d["autorizacao"]["assinada_por"] = " "
        self.assertTrue(any("assinada_por" in e for e in escopo.validar(d)))

    def test_alvos_liberados(self):
        for alvo in ("loja.example", "https://app.loja.example/pedidos/1", "api.loja.example:8443", "203.0.113.20"):
            with self.subTest(alvo=alvo):
                ok, motivo = escopo.checar(self.d, alvo, DENTRO)
                self.assertTrue(ok, motivo)

    def test_alvos_bloqueados(self):
        for alvo in ("pagamento.loja.example", "https://pagamento.loja.example/checkout", "outraloja.example",
                     "loja.example.evil.com", "203.0.113.200", "8.8.8.8", "naoloja.example"):
            with self.subTest(alvo=alvo):
                ok, _ = escopo.checar(self.d, alvo, DENTRO)
                self.assertFalse(ok)

    def test_curinga_nao_vale_para_o_dominio_raiz(self):
        d = copy.deepcopy(self.d)
        d["alvos"]["dominios"] = ["*.loja.example"]
        self.assertFalse(escopo.checar(d, "loja.example", DENTRO)[0])
        self.assertTrue(escopo.checar(d, "www.loja.example", DENTRO)[0])

    def test_fora_da_janela(self):
        antes = dt.datetime(2027, 3, 9, 12, 0, tzinfo=dt.timezone.utc)
        depois = dt.datetime(2027, 3, 15, 12, 0, tzinfo=dt.timezone.utc)
        for quando in (antes, depois):
            ok, motivo = escopo.checar(self.d, "loja.example", quando)
            self.assertFalse(ok)
            self.assertIn("janela", motivo)

    def test_janela_sem_fuso(self):
        d = copy.deepcopy(self.d)
        d["janela"]["inicio"] = dt.datetime(2027, 3, 10, 9, 0)
        self.assertTrue(any("fuso" in e for e in escopo.validar(d)))

    def test_assinada_depois_do_inicio(self):
        d = copy.deepcopy(self.d)
        d["autorizacao"]["assinada_em"] = dt.date(2027, 3, 12)
        self.assertTrue(any("depois do início" in e for e in escopo.validar(d)))

    def test_rodar_bloqueia_sem_executar(self):
        # Janela já encerrada: o comando não roda e nada é registrado.
        arq = self.pasta / "escopo.toml"
        arq.write_text(arq.read_text(encoding="utf-8").replace("2027-03-1", "2020-03-1").replace("2027-03-01", "2020-03-01"),
                       encoding="utf-8")
        codigo = escopo.main(["rodar", str(self.pasta / "escopo.toml"), "loja.example", "--", sys.executable, "-c", "print(1)"])
        self.assertEqual(codigo, 1)
        self.assertFalse((self.pasta / "registro.jsonl").exists())

    def test_registro(self):
        reg = escopo.registrar(self.pasta, "loja.example", ["nmap", "-sV", "loja.example"], 0, DENTRO)
        linha = json.loads(reg.read_text(encoding="utf-8").splitlines()[0])
        self.assertEqual(linha["comando"], "nmap -sV loja.example")


class TesteRelatorio(BaseEscopo):
    def setUp(self):
        super().setUp()
        self.a = relatorio.carregar_achados(MODELOS / "achados.example.toml")

    def test_modelo_valido(self):
        self.assertEqual(relatorio.validar(self.d, self.a), [])

    def test_ordena_do_mais_grave(self):
        ids = [x["id"] for x in relatorio.ordenar(self.a["achado"])]
        self.assertEqual(ids, ["AMS-01", "AMS-02"])

    def test_recusa_achado_fora_do_escopo(self):
        a = copy.deepcopy(self.a)
        a["achado"][0]["ativo"] = "https://pagamento.loja.example/checkout"
        self.assertTrue(any("fora do escopo" in e for e in relatorio.validar(self.d, a)))

    def test_recusa_vetor_ruim_e_id_repetido(self):
        a = copy.deepcopy(self.a)
        a["achado"][1]["id"] = "AMS-01"
        a["achado"][1]["vetor"] = "CVSS:3.1/AV:N"
        erros = relatorio.validar(self.d, a)
        self.assertTrue(any("repetido" in e for e in erros))
        self.assertTrue(any("CVSS" in e for e in erros))

    def test_gera_secoes(self):
        md = relatorio.gerar(self.d, self.a, [{"quando": "2027-03-11T15:00:00+00:00", "alvo": "loja.example",
                                               "comando": "nmap -sV loja.example", "codigo_saida": 0}])
        for trecho in ("## 1. Sumário executivo", "## 2. Escopo", "## 4. Achados", "### AMS-01", "6.5 (`CVSS:3.1",
                       "Em aberto no fim do teste: **1** de 2", "nmap -sV loja.example", "pagamento.loja.example"):
            self.assertIn(trecho, md)


if __name__ == "__main__":
    unittest.main()
