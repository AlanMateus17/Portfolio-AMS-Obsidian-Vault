# Modelos de segurança

Peças prontas para copiar. O guia completo está em [docs/seguranca](../../../docs/seguranca/README.md).

| Arquivo | Para quê | Onde vai |
|---|---|---|
| `modelagem-ameacas.md` | STRIDE + checklist ASVS de cada sistema seu | `docs/seguranca/ameacas.md` do sistema (ex.: AM Kaixara) |
| `dast-zap.yml` | Varredura passiva do ZAP na homologação, toda segunda | `.github/workflows/` do sistema |
| `autorizacao-modelo.md` | Termo que o cliente assina antes de qualquer teste | Pasta do cliente, fora do GitHub (revisado por advogado antes do 1º contrato) |
| `escopo.example.toml` | O termo em formato que a guarda lê | `~/clientes/NOME/escopo.toml` |
| `achados.example.toml` | Achados do teste, com vetor CVSS 3.1 | `~/clientes/NOME/achados.toml` |
| `aula-re/` | Crackme da aula (C e C#) para os alunos quebrarem o próprio binário | Repositório de aulas |

Fluxo de um serviço:

```bash
mkdir -p ~/clientes/loja && cp infra/templates/seguranca/escopo.example.toml ~/clientes/loja/escopo.toml
python3 tools/seguranca/escopo.py validar ~/clientes/loja/escopo.toml
python3 tools/seguranca/escopo.py rodar ~/clientes/loja/escopo.toml loja.example -- nmap -sV loja.example
python3 tools/seguranca/relatorio.py ~/clientes/loja/escopo.toml ~/clientes/loja/achados.toml
```

A pasta `~/clientes` nunca vai para o GitHub nem para IA na nuvem: tem dado do cliente e evidência de falha.
