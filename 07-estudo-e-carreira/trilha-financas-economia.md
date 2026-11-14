---
tags: [estudo, financas, economia, contabilidade, portfolio-ams]
tipo: trilha
status: ativo
atualizado: 2026-10-26
---

# 💹 Trilha de Finanças e Economia — Especialização no Mercado Financeiro e Econômico

> **Em palavras simples:** é o estudo de **dinheiro**: como investir, como uma empresa registra o que ganha e gasta (contabilidade), como funcionam juros, impostos, a bolsa e a economia do país. Você aprende para construir sistemas financeiros e para tirar as certificações. Começa leve e vai aprofundando.

> **Objetivo:** ser o engenheiro de software que entende de dinheiro de verdade — contabilidade, tributos, mercado e economia — para construir os módulos financeiros do AM Gestão (Caixa, Pedidos, Financeiro, Loja) e a análise de dados, sem depender de alguém para traduzir a regra de negócio, e, no horizonte, modelar a economia brasileira.
>
> **Como ela convive com o resto:** os módulos F0–F3 são **leves e começam já**, dentro dos Passos que precisam deles (o caixa do módulo Caixa precisa de contabilidade no Passo 7, por exemplo). Do F4 em diante, a trilha vira uma **Trilha Paralela** normal, com gatilho. A teoria econômica pesada vem da [faculdade de Economia](formacao-academica.md); esta trilha cobre o que a faculdade **não** ensina bem: contabilidade empresarial, tributação brasileira, mercado na prática e aplicação em código.

---

## 🗺️ Visão geral dos módulos

| Módulo | Tema | Começa | A faculdade cobre? | Aplicação direta |
|---|---|---|---|---|
| **F0** | Finanças pessoais e investimentos | 🔄 já em curso | Não | módulo Financeiro do AM Gestão · carteira real/simulada |
| **F1** | Contabilidade | Junto do Passo 5 | Pouco | Fechamento de caixa do módulo Caixa · DRE · módulo Financeiro |
| **F2** | Matemática financeira | Junto do Passo 5 (Lins Cap. 6) | Parcial | Simuladores do módulo Financeiro · financiamento do apartamento |
| **F3** | Tributação brasileira na prática | Junto do Passo 7 | Não | Carnê-leão · IRPF · emissor fiscal do módulo Caixa |
| **F4** | Finanças corporativas e valuation | Depois do Passo 8 | Parcial | Motor de análise de ações do módulo Financeiro |
| **F5** | Mercado financeiro e regulação | Depois do F4 | Parcial | Compliance do módulo Financeiro · Pix e Open Finance |
| **F6** | Economia aplicada e dados | Com a faculdade + Python ([Trilha de Dados & IA](trilha-dados-ia.md)) | **Sim (teoria)** | o módulo de dados do AM Gestão · painel de indicadores |
| **F7** | Administração e negócios | Contínuo, em doses pequenas | Não | Renda extra · Grupo AMtech |
| **F8** | Finanças quantitativas | 🌌 horizonte | Parcial | Risco, derivativos, backtesting |

---

## F0 — Finanças pessoais e investimentos *(já em curso)*

- [ ] Métodos que você já segue, aplicados com rigor: **ARCA** (divisão da carteira), **Barsi/BEST** (setores perenes, dividendos), **Bazin** (preço-teto por dividendo), **Graham** (margem de segurança), **Buffett** (vantagem competitiva, valor)
- [ ] Trilhas da Finclass, na ordem da plataforma
- [ ] Uma carteira por metodologia (real e simulada) para comparar resultados
- [ ] **Método próprio:** combinar as avaliações de Barsi, Bazin e Buffett (com a margem de Graham) numa regra sua de onde e quanto investir, seguida à risca — vira o motor do módulo Financeiro no F4
- [ ] Reserva de emergência: 3 → 6 → 12 meses de custo fixo; caixas separados (reserva, segurança, empreendimentos, investir, estudo, lazer)
- **Leituras:** *O Investidor Inteligente* (Graham) · *Faça Fortuna com Ações* (Décio Bazin) · cartas anuais de Buffett aos acionistas
- **✅ Pronto quando:** explica, para cada ativo que comprou, qual método justificou a compra e qual seria o gatilho de venda.

## F1 — Contabilidade *(o motor de qualquer sistema financeiro)*

- [ ] Partidas dobradas: débito, crédito, plano de contas
- [ ] Regime de caixa × regime de competência
- [ ] Balanço Patrimonial · DRE · DFC (método direto e indireto)
- [ ] Conciliação bancária
- [ ] Contabilidade gerencial: custo fixo/variável, margem de contribuição, ponto de equilíbrio
- **Desenvolver:** abertura/fechamento de caixa do módulo Caixa do AM Gestão (Passo 7) gerando **lançamentos em partidas dobradas**, e uma DRE simples a partir deles. O mesmo ledger serve a todo o módulo Financeiro do AM Gestão.
- **Leituras:** *Contabilidade Introdutória* (Equipe de Professores da FEA-USP) · o artigo *Accounting for Computer Scientists* (Martin Kleppmann) — partidas dobradas explicadas como grafo, escrito para programador
- **✅ Pronto quando:** a soma de débitos e créditos do seu sistema fecha em zero em qualquer período, e a DRE sai de consulta SQL, não de planilha.

## F2 — Matemática financeira

- [ ] Juros simples e compostos, capitalização contínua (Lins, Parte II, Cap. 6)
- [ ] Taxas equivalentes, nominal × efetiva, inflação e juros reais
- [ ] Séries de pagamento, SAC × Price, amortização
- [ ] VPL, TIR, payback
- **Desenvolver:** simulador de financiamento (o do seu apartamento) e simulador de aporte mensal com juros compostos, como módulo do módulo Financeiro.
- **✅ Pronto quando:** o simulador bate centavo a centavo com a calculadora do banco.

## F3 — Tributação brasileira na prática

- [ ] Pessoa física: IRPF, carnê-leão (aulas, freela recebidos no CPF), IR sobre investimentos (tabela regressiva, isenções de dividendos e FII nas regras atuais)
- [ ] Pessoa jurídica: MEI × Simples Nacional × Lucro Presumido, anexos do Simples, fator R
- [ ] Documentos fiscais: NF-e, NFC-e, NFS-e (e a NFS-e nacional), noção de SPED
- [ ] Reforma tributária (IBS/CBS): o que muda e quando — **confira sempre a regra vigente**, isso muda todo ano
- **Desenvolver:** `IEmissorFiscal` do módulo Caixa com conhecimento real do que cada documento exige; aba de impostos do módulo Financeiro do AM Gestão.
- **✅ Pronto quando:** você faz a própria declaração de IR usando os dados do seu sistema.

## F4 — Finanças corporativas e valuation *(Trilha Paralela, depois do Passo 8)*

- [ ] Estrutura de capital, custo de capital (WACC), CAPM
- [ ] Fluxo de caixa descontado, múltiplos (P/L, EV/EBITDA, P/VP, dividend yield)
- [ ] Leitura de demonstrações de empresas listadas (ITR, DFP, release de resultados)
- **Desenvolver:** motor de análise do módulo Financeiro aplicando Barsi, Bazin, Graham e Buffett sobre dados reais da CVM, com cada método testado.
- **Leituras:** *Finanças Corporativas e Valor* (Alexandre Assaf Neto) · *Valuation* / material gratuito de Aswath Damodaran
- **✅ Pronto quando:** o sistema calcula preço-teto Bazin e Graham de uma empresa real e você confere à mão.

## F5 — Mercado financeiro e regulação

- [ ] Sistema Financeiro Nacional: CMN, BACEN, CVM, B3, ANBIMA — quem regula o quê
- [ ] Produtos: renda fixa (Tesouro, CDB, LCI/LCA, debêntures), ações, FIIs, fundos, ETFs, BDRs, noção de derivativos
- [ ] Regras que afetam seus produtos: **consultoria (Resolução CVM 19)**, **analista (Resolução CVM 20)**, LGPD para dado financeiro
- [ ] Infraestrutura de pagamentos: **Pix** (regulamento e API), **Open Finance Brasil**, noção de ISO 20022
- **Desenvolver:** checklist de compliance do módulo Financeiro (o que o sistema pode mostrar sem virar recomendação); integração de teste com uma API de Pix em sandbox.
- **Leituras:** *Mercado Financeiro* (Alexandre Assaf Neto) · materiais oficiais do BACEN e da CVM (portal do investidor)
- **Opcional:** prova **CPA** da ANBIMA como validação do módulo ([formacao-academica](formacao-academica.md)).
- **✅ Pronto quando:** você sabe dizer, para cada tela do módulo Financeiro, se ela é informação, educação ou recomendação — e o que a lei exige em cada caso.

## F6 — Economia aplicada e dados *(com a faculdade + Python)*

- [ ] Micro e macro em paralelo às disciplinas da faculdade
- [ ] Indicadores brasileiros: Selic, IPCA, IGP-M, PIB, câmbio, desemprego, resultado fiscal — de onde vêm e como se relacionam
- [ ] Dados abertos: API **SGS do Banco Central**, **SIDRA do IBGE**, dados abertos da **CVM**, Focus (expectativas de mercado)
- [ ] Econometria em Python: regressão, séries temporais (ARIMA, statsmodels, Prophet — já previstos no módulo de dados do AM Gestão)
- **Desenvolver:** painel de indicadores da economia brasileira no módulo de dados do AM Gestão — o primeiro tijolo do "sonho da economia brasileira", e um ótimo projeto de portfólio.
- **Leituras:** *Introdução à Economia* (Mankiw) · *Econometria Básica* (Gujarati) ou *Introductory Econometrics* (Wooldridge) · *Python for Data Analysis* (Wes McKinney)
- **✅ Pronto quando:** o painel atualiza sozinho a partir das APIs oficiais e você explica a relação Selic × IPCA dos últimos anos com os dados dele.

## F7 — Administração e negócios *(contínuo, doses pequenas)*

- [ ] Precificação de serviço e de SaaS (custo, margem, valor percebido)
- [ ] Vendas e prospecção (o gargalo real dos sites com manutenção)
- [ ] Marketing de conteúdo e funil (mini-curso → curso → plataforma)
- [ ] Processos de empresa que os ERPs automatizam: compras, estoque, faturamento, CRM
- [ ] Gestão de pessoas e contratação (quando houver o primeiro funcionário)
- **Aplicação:** a sua própria renda extra é o laboratório — cada fonte tratada como empresa (custo, margem, hora real) no módulo Financeiro do AM Gestão.

## F8 — Finanças quantitativas *(🌌 horizonte)*

Processos estocásticos, derivativos (*Options, Futures and Other Derivatives*, John Hull), gestão de risco (VaR), otimização de carteira (Markowitz), backtesting. **Gatilho:** faculdade de Economia na metade + Trilha de Dados & IA até o IA3.

---

## 🔗 Ligações
- Formação e certificações: [formacao-academica](formacao-academica.md)
- Software financeiro (ledger, idempotência, dinheiro em decimal): [trilha-engenharia-software](trilha-engenharia-software.md) §Engenharia de sistemas financeiros
- Python, estatística e IA: [trilha-dados-ia](trilha-dados-ia.md)
- Sistema que mais usa esta trilha: [rendara-documento-projeto-final](../02-sistemas-de-negocio/rendara-documento-projeto-final.md)

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Meu progresso financeiro (Dashboard)](../12-artefatos/tipados/meu-progresso-financeiro) · projeto (design/painel) · [sobre](../12-artefatos/tipados/meu-progresso-financeiro/LEIA-ME.md)
- [Teste BESST da B3: Barsi, Bazin, Buffett e ARCA](../12-artefatos/documentos/teste-besst-da-b3-barsi-bazin-buffett-e-arca/Teste%20BESST%20da%20B3%20Barsi,%20Bazin,%20Buffett%20e%20ARCA.md)
- [Teste BESST — Dados e cálculos](../12-artefatos/documentos/teste-besst-da-b3-barsi-bazin-buffett-e-arca/Dados%20e%20cálculos.md)
- [Exercício: Fluxograma do Preço-Teto (Barsi, Bazin e ARCA)](../12-artefatos/documentos/exercicio-fluxograma-do-preco-teto-barsi-bazin-e-arca.md)
- [Caixa da Casa 2 (versão de 17/10) · cópia 5hzp](../12-artefatos/paginas/caixa-da-casa-2-5hzp/index.html) · página interativa · [sobre](../12-artefatos/paginas/caixa-da-casa-2-5hzp/LEIA-ME.md)
- [Caixa da Casa 2 (versão de 17/10) · cópia t7mj](../12-artefatos/paginas/caixa-da-casa-2-t7mj/index.html) · página interativa · [sobre](../12-artefatos/paginas/caixa-da-casa-2-t7mj/LEIA-ME.md)
- [Caixa da Casa 2 — plano do sistema completo](../12-artefatos/documentos/caixa-da-casa-2-plano-do-sistema-completo.md)
- [Sistema de Controle Financeiro Familiar](../12-artefatos/documentos/sistema-de-controle-financeiro-familiar.md)
- [Plataforma financeira, contábil e tributária: análise completa](../12-artefatos/documentos/plataforma-financeira-contabil-e-tributaria-analise-completa.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
