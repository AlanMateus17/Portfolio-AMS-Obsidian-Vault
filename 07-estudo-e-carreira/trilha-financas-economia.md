---
tags: [estudo, financas, economia, contabilidade, portfolio-ams]
tipo: trilha
status: ativo
atualizado: 2026-10-26
---

# 💹 Trilha de Finanças e Economia — Especialização no Mercado Financeiro e Econômico

> **Objetivo:** ser o engenheiro de software que entende de dinheiro de verdade — contabilidade, tributos, mercado e economia — para construir sistemas financeiros (AM Kaixara, AM Rendara, Caixa da Casa, AM Vendra, aura-analytics) sem depender de alguém para traduzir a regra de negócio, e, no horizonte, modelar a economia brasileira.
>
> **Como ela convive com o resto:** os módulos F0–F3 são **leves e começam já**, dentro dos Passos que precisam deles (o caixa do Kaixara precisa de contabilidade no Passo 7, por exemplo). Do F4 em diante, a trilha vira uma **Trilha Paralela** normal, com gatilho. A teoria econômica pesada vem da [faculdade de Economia](formacao-academica.md); esta trilha cobre o que a faculdade **não** ensina bem: contabilidade empresarial, tributação brasileira, mercado na prática e aplicação em código.

---

## 🗺️ Visão geral dos módulos

| Módulo | Tema | Começa | A faculdade cobre? | Aplicação direta |
|---|---|---|---|---|
| **F0** | Finanças pessoais e investimentos | 🔄 já em curso | Não | Caixa da Casa · carteira real/simulada |
| **F1** | Contabilidade | Junto do Passo 5 | Pouco | Fechamento de caixa do Kaixara · DRE · Rendara PJ |
| **F2** | Matemática financeira | Junto do Passo 5 (Lins Cap. 6) | Parcial | Simuladores do Rendara · financiamento do apartamento |
| **F3** | Tributação brasileira na prática | Junto do Passo 7 | Não | Carnê-leão · IRPF · emissor fiscal do Kaixara |
| **F4** | Finanças corporativas e valuation | Depois do Passo 8 | Parcial | Motor de análise de ações do Rendara |
| **F5** | Mercado financeiro e regulação | Depois do F4 | Parcial | Compliance do Rendara · Pix e Open Finance |
| **F6** | Economia aplicada e dados | Com a faculdade + Python ([Trilha de Dados & IA](trilha-dados-ia.md)) | **Sim (teoria)** | aura-analytics · painel de indicadores |
| **F7** | Administração e negócios | Contínuo, em doses pequenas | Não | Renda extra · Grupo AMtech |
| **F8** | Finanças quantitativas | 🌌 horizonte | Parcial | Risco, derivativos, backtesting |

---

## F0 — Finanças pessoais e investimentos *(já em curso)*

- [ ] Métodos que você já segue, aplicados com rigor: **ARCA** (divisão da carteira), **Barsi/BEST** (setores perenes, dividendos), **Bazin** (preço-teto por dividendo), **Graham** (margem de segurança), **Buffett** (vantagem competitiva, valor)
- [ ] Trilhas da Finclass, na ordem da plataforma
- [ ] Uma carteira por metodologia (real e simulada) para comparar resultados
- [ ] Reserva de emergência: 3 → 6 → 12 meses de custo fixo; caixas separados (reserva, segurança, empreendimentos, investir, estudo, lazer)
- **Leituras:** *O Investidor Inteligente* (Graham) · *Faça Fortuna com Ações* (Décio Bazin) · cartas anuais de Buffett aos acionistas
- **✅ Pronto quando:** explica, para cada ativo que comprou, qual método justificou a compra e qual seria o gatilho de venda.

## F1 — Contabilidade *(o motor de qualquer sistema financeiro)*

- [ ] Partidas dobradas: débito, crédito, plano de contas
- [ ] Regime de caixa × regime de competência
- [ ] Balanço Patrimonial · DRE · DFC (método direto e indireto)
- [ ] Conciliação bancária
- [ ] Contabilidade gerencial: custo fixo/variável, margem de contribuição, ponto de equilíbrio
- **Desenvolver:** abertura/fechamento de caixa do AM Kaixara (Passo 7) gerando **lançamentos em partidas dobradas**, e uma DRE simples a partir deles. O mesmo ledger depois serve ao Caixa da Casa e ao Rendara PJ.
- **Leituras:** *Contabilidade Introdutória* (Equipe de Professores da FEA-USP) · o artigo *Accounting for Computer Scientists* (Martin Kleppmann) — partidas dobradas explicadas como grafo, escrito para programador
- **✅ Pronto quando:** a soma de débitos e créditos do seu sistema fecha em zero em qualquer período, e a DRE sai de consulta SQL, não de planilha.

## F2 — Matemática financeira

- [ ] Juros simples e compostos, capitalização contínua (Lins, Parte II, Cap. 6)
- [ ] Taxas equivalentes, nominal × efetiva, inflação e juros reais
- [ ] Séries de pagamento, SAC × Price, amortização
- [ ] VPL, TIR, payback
- **Desenvolver:** simulador de financiamento (o do seu apartamento) e simulador de aporte mensal com juros compostos, como módulo do Rendara.
- **✅ Pronto quando:** o simulador bate centavo a centavo com a calculadora do banco.

## F3 — Tributação brasileira na prática

- [ ] Pessoa física: IRPF, carnê-leão (aulas, freela recebidos no CPF), IR sobre investimentos (tabela regressiva, isenções de dividendos e FII nas regras atuais)
- [ ] Pessoa jurídica: MEI × Simples Nacional × Lucro Presumido, anexos do Simples, fator R
- [ ] Documentos fiscais: NF-e, NFC-e, NFS-e (e a NFS-e nacional), noção de SPED
- [ ] Reforma tributária (IBS/CBS): o que muda e quando — **confira sempre a regra vigente**, isso muda todo ano
- **Desenvolver:** `IEmissorFiscal` do Kaixara com conhecimento real do que cada documento exige; aba de impostos do Caixa da Casa.
- **✅ Pronto quando:** você faz a própria declaração de IR usando os dados do seu sistema.

## F4 — Finanças corporativas e valuation *(Trilha Paralela, depois do Passo 8)*

- [ ] Estrutura de capital, custo de capital (WACC), CAPM
- [ ] Fluxo de caixa descontado, múltiplos (P/L, EV/EBITDA, P/VP, dividend yield)
- [ ] Leitura de demonstrações de empresas listadas (ITR, DFP, release de resultados)
- **Desenvolver:** motor de análise do Rendara aplicando Barsi, Bazin, Graham e Buffett sobre dados reais da CVM, com cada método testado.
- **Leituras:** *Finanças Corporativas e Valor* (Alexandre Assaf Neto) · *Valuation* / material gratuito de Aswath Damodaran
- **✅ Pronto quando:** o sistema calcula preço-teto Bazin e Graham de uma empresa real e você confere à mão.

## F5 — Mercado financeiro e regulação

- [ ] Sistema Financeiro Nacional: CMN, BACEN, CVM, B3, ANBIMA — quem regula o quê
- [ ] Produtos: renda fixa (Tesouro, CDB, LCI/LCA, debêntures), ações, FIIs, fundos, ETFs, BDRs, noção de derivativos
- [ ] Regras que afetam seus produtos: **consultoria (Resolução CVM 19)**, **analista (Resolução CVM 20)**, LGPD para dado financeiro
- [ ] Infraestrutura de pagamentos: **Pix** (regulamento e API), **Open Finance Brasil**, noção de ISO 20022
- **Desenvolver:** checklist de compliance do Rendara (o que o sistema pode mostrar sem virar recomendação); integração de teste com uma API de Pix em sandbox.
- **Leituras:** *Mercado Financeiro* (Alexandre Assaf Neto) · materiais oficiais do BACEN e da CVM (portal do investidor)
- **Opcional:** prova **CPA** da ANBIMA como validação do módulo ([formacao-academica](formacao-academica.md)).
- **✅ Pronto quando:** você sabe dizer, para cada tela do Rendara, se ela é informação, educação ou recomendação — e o que a lei exige em cada caso.

## F6 — Economia aplicada e dados *(com a faculdade + Python)*

- [ ] Micro e macro em paralelo às disciplinas da faculdade
- [ ] Indicadores brasileiros: Selic, IPCA, IGP-M, PIB, câmbio, desemprego, resultado fiscal — de onde vêm e como se relacionam
- [ ] Dados abertos: API **SGS do Banco Central**, **SIDRA do IBGE**, dados abertos da **CVM**, Focus (expectativas de mercado)
- [ ] Econometria em Python: regressão, séries temporais (ARIMA, statsmodels, Prophet — já previstos no aura-analytics)
- **Desenvolver:** painel de indicadores da economia brasileira no `aura-analytics` — o primeiro tijolo do "sonho da economia brasileira", e um ótimo projeto de portfólio.
- **Leituras:** *Introdução à Economia* (Mankiw) · *Econometria Básica* (Gujarati) ou *Introductory Econometrics* (Wooldridge) · *Python for Data Analysis* (Wes McKinney)
- **✅ Pronto quando:** o painel atualiza sozinho a partir das APIs oficiais e você explica a relação Selic × IPCA dos últimos anos com os dados dele.

## F7 — Administração e negócios *(contínuo, doses pequenas)*

- [ ] Precificação de serviço e de SaaS (custo, margem, valor percebido)
- [ ] Vendas e prospecção (o gargalo real dos sites com manutenção)
- [ ] Marketing de conteúdo e funil (mini-curso → curso → plataforma)
- [ ] Processos de empresa que os ERPs automatizam: compras, estoque, faturamento, CRM
- [ ] Gestão de pessoas e contratação (quando houver o primeiro funcionário)
- **Aplicação:** a sua própria renda extra é o laboratório — cada fonte tratada como empresa (custo, margem, hora real) no Caixa da Casa.

## F8 — Finanças quantitativas *(🌌 horizonte)*

Processos estocásticos, derivativos (*Options, Futures and Other Derivatives*, John Hull), gestão de risco (VaR), otimização de carteira (Markowitz), backtesting. **Gatilho:** faculdade de Economia na metade + Trilha de Dados & IA até o IA3.

---

## 🔗 Ligações
- Formação e certificações: [formacao-academica](formacao-academica.md)
- Software financeiro (ledger, idempotência, dinheiro em decimal): [trilha-engenharia-software](trilha-engenharia-software.md) §Engenharia de sistemas financeiros
- Python, estatística e IA: [trilha-dados-ia](trilha-dados-ia.md)
- Sistema que mais usa esta trilha: [rendara-documento-projeto-final](../02-sistemas-de-negocio/rendara-documento-projeto-final.md)
