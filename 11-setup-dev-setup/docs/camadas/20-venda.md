<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 20 · Plataformas de venda e recebimento

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Cada venda é lançada no carnê-leão e o dinheiro cai na sua conta separada.

**15 blocos** · 12 precisam de conta · 2 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_pixa["Pix Automático + gateway (ex.: Asaas)"]
    n_agenda["Agenda online (Cal.com)"]
    n_crm["CRM simples (planilha)"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
    n_eduzz["Eduzz"]
    n_udemy["Udemy"]
    n_dio["DIO (parceria)"]
    n_ytm["YouTube (membros)"]
    n_mp["Mercado Pago"]
    n_afil["Afiliados (Amazon, Hotmart…)"]
    n_chatwoot["Chatwoot (atendimento)"]
    n_twenty["Twenty (CRM aberto)"]
    n_polar["Polar (venda internacional)"]
    n_heyform["HeyForm (qualifica o orçamento)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_oatend["Agente atendente (WhatsApp)"]
    n_ocob["Agente cobrador"]
    n_ocrm["CRM único + LGPD"]
  end
  subgraph L_pub["Público e canais"]
    n_comu["Comunidade (Discord ou grupo)"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_afprog["Programa de afiliados"]
    n_hooks["Webhooks de venda"]
    n_mailer["MailerLite"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_banco["Conta bancária separada (CPF)"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
    n_site["Site pessoal + blog (Jekyll)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_aulas["Aulas particulares"]
    n_curso["Mini-curso Lógica de Programação"]
    n_form["Formações (TI, Matemática, Finanças)"]
    n_livro["Livro Lógica e Máquina"]
    n_sites["Sites para pequenas empresas"]
    n_tmpl["Templates e código-fonte"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bcurso["Curso por seção"]
    n_prof["Edição do professor"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_lic["aura-licensing"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_pbiz["Plugins: small- business + marketing"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_nav["Navegador + Claude in Chrome"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_kee["KeePassXC"]
  end
  n_pixa -->|"cobrança recorrente"| n_lic
  n_pixa -->|"recebimento"| n_banco
  n_ocob -->|"Pix"| n_pixa
  n_agenda -->|"horários"| n_aulas
  n_agenda -->|"pagamento"| n_mp
  n_heyform -->|"libera a agenda"| n_agenda
  n_crm -->|"propostas"| n_sites
  n_crm -->|"vira"| n_ocrm
  n_hotm -->|"lança no carnê-leão"| n_nfse
  n_hotm -->|"saque"| n_banco
  n_hotm -->|"venda e reembolso"| n_hooks
  n_hotm -->|"convite na compra"| n_comu
  n_kee -->|"senhas"| n_hotm
  n_nav -->|"painel web"| n_hotm
  n_pbiz -->|"funil e lançamento"| n_hotm
  n_curso -->|"produto cadastrado"| n_hotm
  n_form -->|"produto"| n_hotm
  n_tmpl -->|"download"| n_hotm
  n_livro -->|"PDF"| n_hotm
  n_inst -->|"botão comprar"| n_hotm
  n_mailer -->|"lançamento"| n_hotm
  n_afprog -->|"afiliados cadastrados"| n_hotm
  n_bcurso -->|"venda"| n_hotm
  n_prof -->|"licença para escolas"| n_hotm
  n_kiwi -->|"lança no carnê-leão"| n_nfse
  n_kiwi -->|"saque"| n_banco
  n_kiwi -->|"venda e reembolso"| n_hooks
  n_curso -->|"produto"| n_kiwi
  n_inst -->|"botão comprar"| n_kiwi
  n_eduzz -->|"lança no carnê-leão"| n_nfse
  n_eduzz -->|"saque"| n_banco
  n_eduzz -->|"venda e reembolso"| n_hooks
  n_curso -->|"produto"| n_eduzz
  n_udemy -->|"carnê-leão (exterior)"| n_nfse
  n_udemy -->|"PayPal ou Payoneer"| n_banco
  n_curso -->|"versão para o marketplace"| n_udemy
  n_form -->|"proposta de parceria"| n_dio
  n_obsd -->|"artigos e projetos"| n_dio
  n_yt -->|"membros"| n_ytm
  n_mp -->|"lança no carnê-leão"| n_nfse
  n_mp -->|"saque"| n_banco
  n_aulas -->|"cobrança"| n_mp
  n_sites -->|"cobrança"| n_mp
  n_ocob -->|"cobrança"| n_mp
  n_afil -->|"comissões no carnê-leão"| n_nfse
  n_site -->|"links no blog"| n_afil
  n_yt -->|"links na descrição"| n_afil
  n_chatwoot -->|"usa o agente"| n_oatend
  n_twenty -->|"substitui a planilha"| n_ocrm
  n_tmpl -->|"vende lá fora"| n_polar
  n_heyform -->|"lead no CRM"| n_ocrm
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_pixa,n_agenda,n_crm,n_hotm,n_kiwi,n_eduzz,n_udemy,n_dio,n_ytm,n_mp,n_afil,n_chatwoot,n_twenty,n_polar,n_heyform desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Pix Automático + gateway (ex.: Asaas)](#pixa) | Remoto · precisa de conta · futuro | Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente. | passo 24.7 · Nov/2026 a out/2027, revisão no fim de cada trimestre; passo 45.9 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 52.4 · Quando a renda pedir (começa quando: a renda passou do valor de virada definido com o contador) |
| [Agenda online (Cal.com)](#agenda) | Remoto · precisa de conta | Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis. | passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 37.8 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 45.4 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 46.18 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 46.19 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [CRM simples (planilha)](#crm) | Local | Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes. | passo 37.9 · Semanas 8 a 10 · dez/2026 a jan/2027 |
| [Hotmart](#hotm) | Remoto · precisa de conta | Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público. | passo 37.5 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.2 · Semanas 12 a 15 · jan a fev/2027; passo 40.5 · Semanas 12 a 15 · jan a fev/2027; passo 40.10 · Semanas 12 a 15 · jan a fev/2027; passo 46.3 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 46.4 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Kiwify](#kiwi) | Remoto · precisa de conta | Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF. | passo 37.5 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 |
| [Eduzz](#eduzz) | Remoto · precisa de conta | Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio. | passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 |
| [Udemy](#udemy) | Remoto · precisa de conta | Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA. | passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 |
| [DIO (parceria)](#dio) | Remoto · precisa de conta | Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado. | passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027 |
| [YouTube (membros)](#ytm) | Remoto · precisa de conta · futuro | Assinatura mensal do canal, quando houver público. | passo 47.9 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Mercado Pago](#mp) | Remoto · precisa de conta | Pix e cartão para aulas particulares e serviços de sites. | passo 37.7 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.19 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Afiliados (Amazon, Hotmart…)](#afil) | Remoto · precisa de conta | Links de produtos de terceiros no blog e nos vídeos. | passo 37.11 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.1 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Chatwoot (atendimento)](#chatwoot) | Local | Caixa única de WhatsApp, Instagram, e-mail e site, com o agente atendente e passagem para você. Código aberto. | passo 33.5 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 45.2 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 45.5 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão) |
| [Twenty (CRM aberto)](#twenty) | Local | CRM de verdade (funil, tarefas, e-mails) no lugar da planilha, quando houver 20+ clientes ou leads ativos. | passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.6 · Com a primeira página de venda no ar (jan/2027) e por etapas |
| [Polar (venda internacional)](#polar) | Remoto · precisa de conta | Merchant of Record aberto: vende templates, código-fonte e assinaturas para fora do Brasil e cuida do imposto de cada país. Confirme no cadastro se aceita recebimento no Brasil. | passo 47.11 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [HeyForm (qualifica o orçamento)](#heyform) | Remoto · precisa de conta | Principal da qualificação (ADR 0008): formulário de conversa com lógica (escopo, prazo, verba) antes de liberar a agenda do Cal.com. | passo 23.7 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.9 · Com a primeira página de venda no ar (jan/2027) e por etapas |

<a id="pixa"></a>

### Pix Automático + gateway (ex.: Asaas)

*Remoto · precisa de conta · futuro*

Cobrança recorrente dos sistemas AM por Pix, sem cartão. Lançado pelo Banco Central em 2025. Entra quando o primeiro SaaS tiver cliente.

**Quando entra:** passo 24.7 · Nov/2026 a out/2027, revisão no fim de cada trimestre; passo 45.9 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 52.4 · Quando a renda pedir (começa quando: a renda passou do valor de virada definido com o contador) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [aura-licensing](11-app.md#lic) | Aplicação: sistemas AM (Aura) | cobrança recorrente |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | recebimento |
| ← recebe de | [Agente cobrador](23-oper.md#ocob) | Operação do grupo (esteira, marca, qualidade) | Pix |

<a id="agenda"></a>

### Agenda online (Cal.com)

*Remoto · precisa de conta*

Aluno particular escolhe horário sozinho e já paga. Open source, com plano grátis.

**Quando entra:** passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 37.8 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 45.4 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 46.18 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 46.19 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aulas particulares](17-prod.md#aulas) | Produtos (o que você vende) | horários |
| → envia para | [Mercado Pago](20-venda.md#mp) | Plataformas de venda e recebimento | pagamento |
| ← recebe de | [HeyForm (qualifica o orçamento)](20-venda.md#heyform) | Plataformas de venda e recebimento | libera a agenda |

<a id="crm"></a>

### CRM simples (planilha)

*Local*

Lista de alunos, clientes e propostas. Uma planilha resolve até dezenas de clientes.

**Quando entra:** passo 37.9 · Semanas 8 a 10 · dez/2026 a jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Sites para pequenas empresas](17-prod.md#sites) | Produtos (o que você vende) | propostas |
| → envia para | [CRM único + LGPD](23-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | vira |

<a id="hotm"></a>

### Hotmart

*Remoto · precisa de conta*

Checkout, área de membros e afiliados para cursos e PDFs. Aceita vender no CPF. Melhor quando você mesmo leva o público.

**Quando entra:** passo 37.5 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.2 · Semanas 12 a 15 · jan a fev/2027; passo 40.5 · Semanas 12 a 15 · jan a fev/2027; passo 40.10 · Semanas 12 a 15 · jan a fev/2027; passo 46.3 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 46.4 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](21-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| → envia para | [Comunidade (Discord ou grupo)](22-pub.md#comu) | Público e canais | convite na compra |
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senhas |
| ← recebe de | [Navegador + Claude in Chrome](03-win.md#nav) | Windows 11, apps e máquinas virtuais | painel web |
| ← recebe de | [Plugins: small- business + marketing](08-clc.md#pbiz) | Claude: recursos, conectores e plugins | funil e lançamento |
| ← recebe de | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | produto cadastrado |
| ← recebe de | [Formações (TI, Matemática, Finanças)](17-prod.md#form) | Produtos (o que você vende) | produto |
| ← recebe de | [Templates e código-fonte](17-prod.md#tmpl) | Produtos (o que você vende) | download |
| ← recebe de | [Livro Lógica e Máquina](17-prod.md#livro) | Produtos (o que você vende) | PDF |
| ← recebe de | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |
| ← recebe de | [MailerLite](21-mkt.md#mailer) | Marketing, automação e medição | lançamento |
| ← recebe de | [Programa de afiliados](21-mkt.md#afprog) | Marketing, automação e medição | afiliados cadastrados |
| ← recebe de | [Curso por seção](15-editora.md#bcurso) | Editora AMS Silva (produção de livros) | venda |
| ← recebe de | [Edição do professor](15-editora.md#prof) | Editora AMS Silva (produção de livros) | licença para escolas |

<a id="kiwi"></a>

### Kiwify

*Remoto · precisa de conta*

Mesma função da Hotmart, com painel mais simples. Aceita vender no CPF.

**Quando entra:** passo 37.5 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](21-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | produto |
| ← recebe de | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | botão comprar |

<a id="eduzz"></a>

### Eduzz

*Remoto · precisa de conta*

Outra plataforma brasileira de infoprodutos, com programa de afiliados próprio.

**Quando entra:** passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| → envia para | [Webhooks de venda](21-mkt.md#hooks) | Marketing, automação e medição | venda e reembolso |
| ← recebe de | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | produto |

<a id="udemy"></a>

### Udemy

*Remoto · precisa de conta*

Marketplace mundial: ela traz alunos que você não alcançaria. Ganha bem menos por venda orgânica do que pelo seu cupom. Recebe por PayPal ou Payoneer e pede um formulário fiscal dos EUA.

**Quando entra:** passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.11 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | carnê-leão (exterior) |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | PayPal ou Payoneer |
| ← recebe de | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | versão para o marketplace |

<a id="dio"></a>

### DIO (parceria)

*Remoto · precisa de conta*

Não é marketplace aberto como a Udemy. Os experts trabalham em parceria com a DIO; o caminho é publicar artigos e projetos lá e se candidatar ou ser convidado.

**Quando entra:** passo 37.6 · Semanas 8 a 10 · dez/2026 a jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Formações (TI, Matemática, Finanças)](17-prod.md#form) | Produtos (o que você vende) | proposta de parceria |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | artigos e projetos |

<a id="ytm"></a>

### YouTube (membros)

*Remoto · precisa de conta · futuro*

Assinatura mensal do canal, quando houver público.

**Quando entra:** passo 47.9 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [YouTube](22-pub.md#yt) | Público e canais | membros |

<a id="mp"></a>

### Mercado Pago

*Remoto · precisa de conta*

Pix e cartão para aulas particulares e serviços de sites.

**Quando entra:** passo 37.7 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.19 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | lança no carnê-leão |
| → envia para | [Conta bancária separada (CPF)](19-emp.md#banco) | Pessoa física: impostos e finanças | saque |
| ← recebe de | [Agenda online (Cal.com)](20-venda.md#agenda) | Plataformas de venda e recebimento | pagamento |
| ← recebe de | [Aulas particulares](17-prod.md#aulas) | Produtos (o que você vende) | cobrança |
| ← recebe de | [Sites para pequenas empresas](17-prod.md#sites) | Produtos (o que você vende) | cobrança |
| ← recebe de | [Agente cobrador](23-oper.md#ocob) | Operação do grupo (esteira, marca, qualidade) | cobrança |

<a id="afil"></a>

### Afiliados (Amazon, Hotmart…)

*Remoto · precisa de conta*

Links de produtos de terceiros no blog e nos vídeos.

**Quando entra:** passo 37.11 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.1 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | comissões no carnê-leão |
| ← recebe de | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | links no blog |
| ← recebe de | [YouTube](22-pub.md#yt) | Público e canais | links na descrição |

<a id="chatwoot"></a>

### Chatwoot (atendimento)

*Local*

Caixa única de WhatsApp, Instagram, e-mail e site, com o agente atendente e passagem para você. Código aberto.

**Quando entra:** passo 33.5 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 45.2 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão); passo 45.5 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Agente atendente (WhatsApp)](23-oper.md#oatend) | Operação do grupo (esteira, marca, qualidade) | usa o agente |

<a id="twenty"></a>

### Twenty (CRM aberto)

*Local*

CRM de verdade (funil, tarefas, e-mails) no lugar da planilha, quando houver 20+ clientes ou leads ativos.

**Quando entra:** passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.6 · Com a primeira página de venda no ar (jan/2027) e por etapas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [CRM único + LGPD](23-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | substitui a planilha |

<a id="polar"></a>

### Polar (venda internacional)

*Remoto · precisa de conta*

Merchant of Record aberto: vende templates, código-fonte e assinaturas para fora do Brasil e cuida do imposto de cada país. Confirme no cadastro se aceita recebimento no Brasil.

**Quando entra:** passo 47.11 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Templates e código-fonte](17-prod.md#tmpl) | Produtos (o que você vende) | vende lá fora |

<a id="heyform"></a>

### HeyForm (qualifica o orçamento)

*Remoto · precisa de conta*

Principal da qualificação (ADR 0008): formulário de conversa com lógica (escopo, prazo, verba) antes de liberar a agenda do Cal.com.

**Quando entra:** passo 23.7 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.9 · Com a primeira página de venda no ar (jan/2027) e por etapas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Agenda online (Cal.com)](20-venda.md#agenda) | Plataformas de venda e recebimento | libera a agenda |
| → envia para | [CRM único + LGPD](23-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | lead no CRM |

---

[↑ Camada 21 · Marketing, automação e medição](21-mkt.md) · [↓ Camada 19 · Pessoa física: impostos e finanças](19-emp.md)
