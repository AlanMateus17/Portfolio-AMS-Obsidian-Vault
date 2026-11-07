# Termo de autorização para teste de intrusão

> Modelo de trabalho, não é parecer jurídico. Antes do primeiro contrato pago, peça a um advogado para revisar
> este termo e o contrato de serviço (responsabilidade, sigilo, LGPD e limite de indenização).
> Sem este termo assinado por quem tem poder de autorizar, não há teste: a guarda `tools/seguranca/escopo.py` bloqueia.

**Contratante:** [razão social], CNPJ [número], representada por [nome], [cargo], que declara ter poder para autorizar
testes nos sistemas listados abaixo e que eles pertencem à contratante ou estão sob sua responsabilidade contratual.

**Contratada:** [Alan Mateus / razão social da AMtech], [CPF ou CNPJ].

**Contrato de referência:** [número, ex.: AMS-SEG-2027-001]

## 1. O que está autorizado

A contratante autoriza a contratada a realizar testes de segurança, inclusive tentativas controladas de exploração,
exclusivamente nos alvos abaixo, durante a janela indicada.

| Alvo (domínio, faixa de IP ou URL) | Ambiente | Observação |
|---|---|---|
| [loja.example] | produção / homologação | |
| [*.loja.example] | | subdomínios |

**Fora do escopo (proibido testar):** [ex.: gateway de pagamento de terceiro, e-mail corporativo hospedado por terceiro].
Sistemas de terceiros só entram com autorização escrita do próprio terceiro.

**Janela:** de [dd/mm/aaaa hh:mm] a [dd/mm/aaaa hh:mm], horário de Brasília.

## 2. O que não será feito

- Negação de serviço ou qualquer teste com o objetivo de derrubar o sistema.
- Engenharia social com funcionários, salvo se listada aqui: [não].
- Cópia de dados pessoais além do mínimo necessário para provar o achado; o que for visto é mascarado no relatório.
- Manter acesso depois da janela ou instalar qualquer coisa que permaneça no sistema.

## 3. Contatos e parada de emergência

- Contato técnico da contratante (24 h durante a janela): [nome, telefone].
- Se algo instável acontecer, a contratada para o teste imediatamente e avisa esse contato.
- A contratante avisa à hospedagem ou ao provedor, se o contrato deles exigir aviso prévio.

## 4. Sigilo e dados

- Achados, evidências e o relatório são confidenciais e entregues só à contratante.
- Evidências são guardadas criptografadas e apagadas [90] dias depois do reteste.
- Dado pessoal acessado durante o teste é tratado conforme a LGPD, só para provar o achado.

## 5. Entregáveis

Relatório com sumário executivo, escopo, metodologia, achados com nota CVSS 3.1, evidências, recomendações e
registro de atividades; reteste das correções em até [30] dias.

**Local e data:** [cidade], [dd/mm/aaaa]

______________________________  
[Nome], [cargo], pela contratante

______________________________  
[Nome], pela contratada
