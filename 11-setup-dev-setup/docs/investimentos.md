<!-- Arquivo GERADO por tools/investimentos/investimentos.py a partir de data/investimentos.json. Não edite à mão. -->

# Investimentos: todas as metodologias, ao mesmo tempo, nas quatro classes do ARCA

[← Índice da documentação](README.md)

> Não é recomendação de investimento. O setup aplica as regras que você escreveu; a decisão de comprar, manter ou vender é sua. Os tickers dos exemplos são inventados.

## Regras

- Portão: só entra dinheiro no ARCA com o cartão zerado e a reserva de emergência completa (3 → 6 → 12 meses). A reserva de emergência fica fora do ARCA, nos caixas do financeiro.
- Aporte mensal planejado de R$ 800; meta de renda passiva de R$ 800 por mês.
- ARCA em dois níveis: primeiro o percentual de cada classe (Ações, Real estate, Caixa, Internacional); depois, dentro de cada classe, um percentual por metodologia, com limites por ativo e por setor.
- Todas as metodologias rodam ao mesmo tempo: cada ativo recebe o resultado de cada metodologia que se aplica a ele e um consenso (quantas aprovaram). O consenso desempata a compra dentro de cada metodologia.
- Aporte pequeno não vira migalha: fatias abaixo do mínimo por compra (R$ 100 por padrão) vão para a fatia maior. Com R$ 800 por mês, cada mês reforça só as classes e metodologias mais abaixo do alvo, e o equilíbrio vem ao longo dos meses.
- Metodologia que não faz sentido para um tipo de ativo aparece como 'não se aplica' e não conta no consenso (por exemplo, Fórmula Mágica em bancos, IPCA+ em título pós-fixado).
- Uma carteira por metodologia (real ou simulada) e uma do índice, por classe, para comparar resultados. Metodologia que perder do índice por 3 anos é revista.
- Rebalancear de preferência com aporte novo: vender só quando a regra de venda da metodologia mandar.
- Indicadores vêm de fonte que você confere (RI da empresa, CVM, relatório do fundo, Tesouro); o script só calcula.
- Recomendar ativos para outras pessoas exige registro na CVM (analista ou consultor). Até lá, tudo aqui é para a sua carteira.

## Impostos e garantias que entram no cálculo

- Renda fixa tributada (CDB, Tesouro, debênture comum): tabela regressiva de 22,5% (até 180 dias), 20% (até 360), 17,5% (até 720) e 15% (acima de 720). O script usa essa tabela para comparar título isento com tributado.
- LCI, LCA, CRI, CRA, debêntures incentivadas e rendimentos de FII seguem isentos para pessoa física: a MP 1303/2025, que tributaria parte deles, perdeu a validade em 08/10/2025.
- Investimento direto no exterior: 15% ao ano sobre o rendimento realizado (dividendos, juros, venda), pago na declaração (Lei 14.754/2023); o imposto pago lá fora abate até esse limite.
- Dividendos acima de R$ 50 mil por mês da mesma empresa têm retenção de 10% desde 2026 (Lei 15.270/2025); não afeta o seu tamanho de carteira hoje.
- FGC: até R$ 250 mil por CPF por instituição (conglomerado), com teto global de R$ 1 milhão a cada 4 anos. Tesouro Direto é garantido pelo governo, não pelo FGC.
- Regras de imposto mudam: confira a cada ano na revisão da política.

## Como o consenso classifica cada ativo

Cada ativo passa por todas as metodologias da sua classe. Consenso = metodologias que aprovaram ÷ metodologias que se aplicam. **Forte** a partir de 70%, **médio** a partir de 50%, **fraco** abaixo disso.

## Ações (A do ARCA)

Colunas do CSV: `ticker, setor, preco, dy, dy_medio, dividendo_medio, crescimento_dividendos, divida_pl, lpa, vpa, liquidez_corrente, roe, margem_liquida, divida_liquida_ebitda, roic, ev_ebit, fscore, peg, anos_dividendos, anos_lucro`

| Metodologia | Origem | % alvo na classe | Ideia |
|---|---|---:|---|
| [Luiz Barsi (carteira previdenciária)](#acoes-barsi) | já usava | 20% | Empresas de setores perenes que pagam dividendos com constância, mantidas por décadas com reinvestimento. |
| [Décio Bazin (preço-teto)](#acoes-bazin) | já usava | 15% | Comprar só abaixo do preço que garante 6% de dividendos sobre o valor pago, em empresas pouco endividadas. |
| [Benjamin Graham (investidor defensivo)](#acoes-graham) | já usava | 10% | Margem de segurança abaixo do valor intrínseco, em empresas sólidas e com lucro estável. |
| [Warren Buffett (qualidade a preço justo)](#acoes-buffett) | já usava | 15% | Vantagem competitiva durável, alta rentabilidade e pouca dívida, por muito tempo. |
| [Raul Sena (Investidor Sardinha)](#acoes-sena) | já usava | 10% | As perguntas do método do Raul Sena, como ele usa e estendidas com as perguntas das outras metodologias. |
| [Fórmula Mágica (Joel Greenblatt)](#acoes-formula_magica) | nova | 10% | Somar a posição no ranking de retorno sobre o capital (ROIC alto) com a posição no ranking de preço (EV/EBIT baixo). |
| [Piotroski F-Score](#acoes-piotroski) | nova | 5% | Nove testes de lucro, endividamento e eficiência, nota de 0 a 9. |
| [Peter Lynch (PEG)](#acoes-lynch) | nova | 5% | P/L comparado ao crescimento do lucro: PEG até 1 indica preço não caro para o crescimento. |
| [Modelo de Gordon (preço justo por dividendos)](#acoes-gordon) | nova | 10% | Preço justo = próximo dividendo ÷ (retorno exigido − crescimento do dividendo). |

Limites: até 10% da classe num ativo e 30% num setor; pelo menos 8 ativos.

<a id="acoes-barsi"></a>
### Luiz Barsi (carteira previdenciária)

Empresas de setores perenes que pagam dividendos com constância, mantidas por décadas com reinvestimento.

Critérios:
- Setor perene (BESST)
- Dividendos em pelo menos 5 dos últimos anos
- Lucro em pelo menos 5 dos últimos anos
- Dividend yield de pelo menos 6% no preço atual

Perguntas que só você responde:
- A empresa existirá e venderá o mesmo serviço daqui a 20 anos?
- O dividendo vem do lucro recorrente ou de evento único?

**Quando vender:** Só se o fundamento quebrar (lucro e dividendo deixarem de ser recorrentes).

Fonte: Literatura pública sobre o método; confira com o material que você estudou.

<a id="acoes-bazin"></a>
### Décio Bazin (preço-teto)

Comprar só abaixo do preço que garante 6% de dividendos sobre o valor pago, em empresas pouco endividadas.

Critérios:
- Dividend yield médio de 3 a 5 anos de pelo menos 6%
- Dívida bruta / patrimônio líquido até 1
- Preço até o preço-teto (dividendo médio ÷ 6%)

Perguntas que só você responde:
- O dividendo médio inclui pagamento extraordinário que distorce a média?

**Quando vender:** Quando o dividend yield sobre o preço atual cair muito abaixo de 6% e houver opção melhor (regra sua).

Fonte: Livro 'Faça Fortuna com Ações, Antes que Seja Tarde', de Décio Bazin.

<a id="acoes-graham"></a>
### Benjamin Graham (investidor defensivo)

Margem de segurança abaixo do valor intrínseco, em empresas sólidas e com lucro estável.

Critérios:
- Lucro por ação positivo
- Valor patrimonial por ação positivo
- Liquidez corrente de pelo menos 1,5
- Preço com 25% de margem abaixo do valor de Graham (√(22,5 × LPA × VPA))

Perguntas que só você responde:
- O lucro dos últimos 10 anos foi positivo e estável?

**Quando vender:** Quando o preço passar do valor intrínseco (regra sua).

Fonte: Livro 'O Investidor Inteligente', de Benjamin Graham.

<a id="acoes-buffett"></a>
### Warren Buffett (qualidade a preço justo)

Vantagem competitiva durável, alta rentabilidade e pouca dívida, por muito tempo.

Critérios:
- ROE de pelo menos 15%
- Margem líquida de pelo menos 10%
- Dívida líquida / EBITDA até 2

Perguntas que só você responde:
- Qual é a vantagem competitiva (marca, custo, rede, troca difícil)?
- Eu entendo como a empresa ganha dinheiro?
- A gestão aloca bem o capital e trata bem o minoritário?

**Quando vender:** Quando a vantagem competitiva acabar, não por queda de preço.

Fonte: Cartas anuais da Berkshire Hathaway aos acionistas (públicas).

<a id="acoes-sena"></a>
### Raul Sena (Investidor Sardinha)

As perguntas do método do Raul Sena, como ele usa e estendidas com as perguntas das outras metodologias.

Critérios:
- Todas as suas perguntas do método respondidas com 'sim' (coluna sena = sim)

**Quando vender:** Preencha com a regra do método.

Fonte: Material do curso que você tem; só as suas anotações vão para ~/financas/investimentos.toml.

<a id="acoes-formula_magica"></a>
### Fórmula Mágica (Joel Greenblatt)

Somar a posição no ranking de retorno sobre o capital (ROIC alto) com a posição no ranking de preço (EV/EBIT baixo).

Critérios:
- Entre os 30% melhores no ranking combinado de ROIC e EV/EBIT (bancos e seguros ficam fora)

**Quando vender:** Rebalanceamento anual pelo ranking.

Fonte: Livro 'O Mercado de Ações ao Seu Alcance', de Joel Greenblatt.

<a id="acoes-piotroski"></a>
### Piotroski F-Score

Nove testes de lucro, endividamento e eficiência, nota de 0 a 9.

Critérios:
- Nota de pelo menos 7

**Quando vender:** Quando a nota cair para 3 ou menos (regra sua).

Fonte: Artigo de Joseph Piotroski, 'Value Investing: The Use of Historical Financial Statement Information' (2000).

<a id="acoes-lynch"></a>
### Peter Lynch (PEG)

P/L comparado ao crescimento do lucro: PEG até 1 indica preço não caro para o crescimento.

Critérios:
- PEG (P/L ÷ crescimento anual do lucro em %) até 1

Perguntas que só você responde:
- O crescimento usado é sustentável ou foi um ano fora da curva?

**Quando vender:** Quando a história de crescimento mudar.

Fonte: Livro 'O Jeito Peter Lynch de Investir', de Peter Lynch.

<a id="acoes-gordon"></a>
### Modelo de Gordon (preço justo por dividendos)

Preço justo = próximo dividendo ÷ (retorno exigido − crescimento do dividendo).

Critérios:
- Preço até o preço justo de Gordon (retorno exigido no investimentos.toml)

Perguntas que só você responde:
- O crescimento usado é menor que o retorno exigido? (senão a fórmula não vale)

**Quando vender:** Quando o preço passar muito do preço justo (regra sua).

Fonte: Modelo de desconto de dividendos (Gordon, 1959), conteúdo das provas CNPI e C-PRO.

## Real estate / FIIs (R do ARCA)

Colunas do CSV: `ticker, setor (segmento), tipo (tijolo, papel ou hibrido), preco, pvp, dy, dy_medio, dividendo_medio, anos_rendimentos, vacancia, num_imoveis, maior_inquilino, liquidez_diaria (R$ mil), taxa_adm, pct_high_grade, ltv_medio, sena`

| Metodologia | Origem | % alvo na classe | Ideia |
|---|---|---:|---|
| [Graham para FII (desconto patrimonial)](#fiis-desconto_pvp) | nova | 15% | Comprar abaixo do valor patrimonial: P/VP até 1. |
| [Bazin para FII (preço-teto)](#fiis-bazin_fii) | nova | 20% | Preço-teto pelo rendimento desejado: rendimento médio de 12 meses ÷ 8%. |
| [Barsi para FII (renda perene)](#fiis-barsi_fii) | nova | 20% | Renda constante e imóveis com ocupação alta, mantidos por muito tempo. |
| [Prêmio sobre o Tesouro IPCA+](#fiis-premio_ntnb) | nova | 15% | O rendimento do FII precisa pagar um prêmio acima do juro real do Tesouro IPCA+ (NTN-B), que tem risco menor. |
| [Buffett para FII (qualidade)](#fiis-qualidade_fii) | nova | 15% | Gestão barata, inquilinos diversificados e cota negociada todo dia. |
| [FII de papel (qualidade do crédito)](#fiis-papel_credito) | nova | 5% | Em fundo de recebíveis, o risco é o crédito: maioria em CRI de baixo risco e garantia folgada. |
| [Raul Sena (checklist estendido a FIIs)](#fiis-sena) | nova | 10% | As suas perguntas do método aplicadas também aos fundos. |

Limites: até 15% da classe num ativo e 35% num setor; pelo menos 6 ativos.

<a id="fiis-desconto_pvp"></a>
### Graham para FII (desconto patrimonial)

Comprar abaixo do valor patrimonial: P/VP até 1.

Critérios:
- P/VP até 1,0

Perguntas que só você responde:
- O valor patrimonial está atualizado por laudo recente?

**Quando vender:** Quando o P/VP passar de 1,2 sem melhora de fundamento (regra sua).

Fonte: Adaptação da margem de segurança de Graham; P/VP é o indicador padrão de FII.

<a id="fiis-bazin_fii"></a>
### Bazin para FII (preço-teto)

Preço-teto pelo rendimento desejado: rendimento médio de 12 meses ÷ 8%.

Critérios:
- Rendimento médio de pelo menos 8% ao ano
- Preço até o teto (rendimento médio anual ÷ 8%)

**Quando vender:** Quando o rendimento sobre o preço cair muito abaixo de 8% (regra sua).

Fonte: Adaptação do preço-teto de Décio Bazin.

<a id="fiis-barsi_fii"></a>
### Barsi para FII (renda perene)

Renda constante e imóveis com ocupação alta, mantidos por muito tempo.

Critérios:
- Pelo menos 5 anos pagando rendimentos
- Vacância física até 10% (só para tijolo, hibrido)
- Pelo menos 3 imóveis (só para tijolo, hibrido)

Perguntas que só você responde:
- Os imóveis continuarão úteis daqui a 20 anos (localização, padrão)?

**Quando vender:** Só se a renda deixar de ser recorrente.

Fonte: Adaptação da lógica de renda perene de Luiz Barsi.

<a id="fiis-premio_ntnb"></a>
### Prêmio sobre o Tesouro IPCA+

O rendimento do FII precisa pagar um prêmio acima do juro real do Tesouro IPCA+ (NTN-B), que tem risco menor.

Critérios:
- Rendimento pelo menos 2 pontos acima do juro real da NTN-B (valor do mês no investimentos.toml)

**Quando vender:** Quando o prêmio sumir por muito tempo.

Fonte: Prática de mercado de comparar FII com a NTN-B (conteúdo CGE e CNPI).

<a id="fiis-qualidade_fii"></a>
### Buffett para FII (qualidade)

Gestão barata, inquilinos diversificados e cota negociada todo dia.

Critérios:
- Maior inquilino até 30% da receita (só para tijolo, hibrido)
- Liquidez diária de pelo menos R$ 500 mil
- Taxa de administração até 1% ao ano

Perguntas que só você responde:
- A gestora tem histórico e não emite cotas abaixo do valor patrimonial?

**Quando vender:** Quando a gestão piorar (emissões ruins, taxa maior).

Fonte: Adaptação dos critérios de qualidade de Buffett.

<a id="fiis-papel_credito"></a>
### FII de papel (qualidade do crédito)

Em fundo de recebíveis, o risco é o crédito: maioria em CRI de baixo risco e garantia folgada.

Critérios:
- Pelo menos 70% em CRI de baixo risco (high grade) (só para papel, hibrido)
- LTV médio até 60% (só para papel, hibrido)

Perguntas que só você responde:
- Há algum CRI em atraso ou renegociado?

**Quando vender:** Inadimplência relevante na carteira.

Fonte: Relatório gerencial do fundo; critérios usuais de análise de CRI.

<a id="fiis-sena"></a>
### Raul Sena (checklist estendido a FIIs)

As suas perguntas do método aplicadas também aos fundos.

Critérios:
- Checklist respondido com 'sim' (coluna sena = sim)

**Quando vender:** Regra do método.

Fonte: As suas anotações do material do curso.

## Caixa / renda fixa (C do ARCA)

Colunas do CSV: `ticker (nome do título), emissor, tipo (selic, cdb, lci, lca, ipca, prefixado, debenture, debenture_incentivada, cri, cra), indexador (cdi, selic, ipca, pre), taxa (% do CDI, juro real ou taxa pré), liquidez_dias, vencimento_dias, garantia (tesouro, fgc ou nenhuma), rating, isento (sim/não), sena`

| Metodologia | Origem | % alvo na classe | Ideia |
|---|---|---:|---|
| [Liquidez com garantia (caixa de oportunidade)](#caixa-liquidez) | nova | 30% | Dinheiro que sai no mesmo dia, garantido pelo Tesouro ou pelo FGC, rendendo pelo menos o CDI depois do imposto equivalente. |
| [Proteção contra a inflação (IPCA+)](#caixa-inflacao) | nova | 30% | Juro real acima da sua meta, para a renda passiva não perder para a inflação. |
| [Escada de vencimentos](#caixa-escada) | nova | 25% | Títulos vencendo em anos diferentes: sempre há dinheiro voltando e você reaplica na taxa do momento. |
| [Graham na renda fixa (segurança do emissor)](#caixa-credito_seguro) | nova | 15% | Fora do Tesouro e do FGC, só emissor com nota de crédito alta. |

Limites: até 40% da classe num ativo e 60% num setor; pelo menos 3 ativos.

<a id="caixa-liquidez"></a>
### Liquidez com garantia (caixa de oportunidade)

Dinheiro que sai no mesmo dia, garantido pelo Tesouro ou pelo FGC, rendendo pelo menos o CDI depois do imposto equivalente.

Critérios:
- Resgate em até 1 dia
- Garantia do Tesouro ou do FGC
- Pelo menos 100% do CDI em taxa equivalente tributada (só para cdi, selic)

**Quando vender:** Quando precisar do dinheiro para uma oportunidade da sua política.

Fonte: Regras do FGC e tabela regressiva de IR.

<a id="caixa-inflacao"></a>
### Proteção contra a inflação (IPCA+)

Juro real acima da sua meta, para a renda passiva não perder para a inflação.

Critérios:
- Juro real de pelo menos o mínimo do investimentos.toml (só para ipca)
- Garantia do Tesouro ou do FGC (ou crédito aprovado na metodologia de crédito)

Perguntas que só você responde:
- O vencimento cabe no prazo do objetivo? (vender antes pode dar perda pela marcação a mercado)

**Quando vender:** Levar até o vencimento; vender antes só por regra sua.

Fonte: Tesouro Direto (títulos IPCA+).

<a id="caixa-escada"></a>
### Escada de vencimentos

Títulos vencendo em anos diferentes: sempre há dinheiro voltando e você reaplica na taxa do momento.

Critérios:
- Vencimento em até 5 anos
- Vencimento de pelo menos 1 ano
- Pelo menos 105% do CDI em taxa equivalente (prazo maior paga mais) (só para cdi)

**Quando vender:** Não vende: cada degrau vence e volta para o degrau mais longo.

Fonte: Estratégia clássica de escada (bond ladder).

<a id="caixa-credito_seguro"></a>
### Graham na renda fixa (segurança do emissor)

Fora do Tesouro e do FGC, só emissor com nota de crédito alta.

Critérios:
- Rating AAA, AA+ ou AA (só para nenhuma)
- Garantia conhecida

Perguntas que só você responde:
- A empresa emissora passaria nos critérios de Buffett para ações?

**Quando vender:** Rebaixamento de rating.

Fonte: Princípio de segurança de Graham aplicado a títulos de dívida.

## Internacional (último A do ARCA)

Colunas do CSV: `ticker, setor, tipo (etf, acao, reit, bdr), domicilio (eua, irlanda, br), indice_amplo (sim/não), taxa_adm, preco, pvp, dy, dy_medio, dividendo_medio, crescimento_dividendos, anos_aumento_dividendo, divida_pl, lpa, vpa, liquidez_corrente, roe, margem_liquida, divida_liquida_ebitda, fscore, peg, sena`

| Metodologia | Origem | % alvo na classe | Ideia |
|---|---|---:|---|
| [John Bogle (índice amplo e barato)](#internacional-bogle) | nova | 40% | ETF de índice amplo com taxa baixa como base da classe. |
| [Aristocratas de dividendos (Barsi lá fora)](#internacional-aristocratas) | nova | 15% | Empresas que aumentam o dividendo todo ano há pelo menos 25 anos. |
| [Buffett no exterior](#internacional-buffett_ext) | nova | 15% | Os mesmos critérios de qualidade das ações daqui. |
| [Graham no exterior](#internacional-graham_ext) | nova | 5% | Os mesmos critérios de margem de segurança das ações daqui. |
| [Bazin no exterior](#internacional-bazin_ext) | nova | 5% | Preço-teto pelo dividendo; o yield mínimo lá fora costuma ser menor (ajuste o seu). |
| [REITs (FII lá fora)](#internacional-reits) | nova | 10% | Os critérios de desconto e qualidade dos FIIs aplicados aos REITs. |
| [Raul Sena (checklist estendido ao exterior)](#internacional-sena) | nova | 10% | As suas perguntas do método aplicadas também aos ativos de fora. |

Limites: até 50% da classe num ativo e 40% num setor; pelo menos 3 ativos.

<a id="internacional-bogle"></a>
### John Bogle (índice amplo e barato)

ETF de índice amplo com taxa baixa como base da classe.

Critérios:
- ETF (ou BDR de ETF)
- Índice amplo (mercado total, S&P 500, mundo)
- Taxa de administração até 0,25% ao ano

Perguntas que só você responde:
- Domicílio: ETF da Irlanda (UCITS, acumulação) evita a retenção de 30% sobre dividendos dos EUA e o risco do imposto americano sobre herança acima de US$ 60 mil. Confira com um contador antes de escolher.

**Quando vender:** Não vende: só rebalanceia.

Fonte: Livro 'O Investidor de Bom Senso', de John Bogle.

<a id="internacional-aristocratas"></a>
### Aristocratas de dividendos (Barsi lá fora)

Empresas que aumentam o dividendo todo ano há pelo menos 25 anos.

Critérios:
- 25 anos ou mais aumentando o dividendo (só para acao, bdr)

**Quando vender:** Quando cortar o dividendo.

Fonte: Critério do índice S&P 500 Dividend Aristocrats.

<a id="internacional-buffett_ext"></a>
### Buffett no exterior

Os mesmos critérios de qualidade das ações daqui.

Usa os critérios de `acoes.buffett`.

Critérios:
- ROE de pelo menos 15% (só para acao, bdr)
- Margem líquida de pelo menos 10% (só para acao, bdr)
- Dívida líquida / EBITDA até 2 (só para acao, bdr)

**Quando vender:** Quando a vantagem competitiva acabar.

Fonte: Cartas da Berkshire Hathaway.

<a id="internacional-graham_ext"></a>
### Graham no exterior

Os mesmos critérios de margem de segurança das ações daqui.

Usa os critérios de `acoes.graham`.

Critérios:
- Lucro por ação positivo (só para acao, bdr)
- Valor patrimonial por ação positivo (só para acao, bdr)
- Liquidez corrente de pelo menos 1,5 (só para acao, bdr)
- Preço com 25% de margem abaixo do valor de Graham (√(22,5 × LPA × VPA)) (só para acao, bdr)

**Quando vender:** Quando o preço passar do valor intrínseco.

Fonte: Livro 'O Investidor Inteligente'.

<a id="internacional-bazin_ext"></a>
### Bazin no exterior

Preço-teto pelo dividendo; o yield mínimo lá fora costuma ser menor (ajuste o seu).

Usa os critérios de `acoes.bazin`.

Critérios:
- Dividend yield médio de 3 a 5 anos de pelo menos 6% (só para acao, bdr)
- Dívida bruta / patrimônio líquido até 1 (só para acao, bdr)
- Preço até o preço-teto (dividendo médio ÷ 6%) (só para acao, bdr)

**Quando vender:** Regra do Bazin.

Fonte: Livro de Décio Bazin.

<a id="internacional-reits"></a>
### REITs (FII lá fora)

Os critérios de desconto e qualidade dos FIIs aplicados aos REITs.

Critérios:
- P/VP até 1,1 (só para reit)
- Custos de gestão até 1% ao ano (só para reit)

**Quando vender:** Regras dos FIIs.

Fonte: Adaptação dos critérios de FII.

<a id="internacional-sena"></a>
### Raul Sena (checklist estendido ao exterior)

As suas perguntas do método aplicadas também aos ativos de fora.

Critérios:
- Checklist respondido com 'sim' (coluna sena = sim)

**Quando vender:** Regra do método.

Fonte: As suas anotações do material do curso.

## Alocações para comparar com o ARCA (carteiras simuladas)

| Estratégia | Divisão | Uso |
|---|---|---|
| ARCA (Thiago Nigro) | 25% em cada classe | A sua alocação principal (ajuste os percentuais no investimentos.toml). |
| Graham defensivo | Entre 25% e 75% em ações, o resto em renda fixa | Carteira simulada para comparar com o ARCA. |
| Portfólio permanente (Harry Browne) | 25% ações, 25% títulos longos, 25% caixa, 25% ouro | Carteira simulada; o ouro não faz parte do ARCA. |
| Bogle | Fundos de índice amplos, com a parte em renda fixa crescendo com a idade | Carteira simulada de índice: o comparador de todas as outras. |

## Como usar

```bash
python tools/investimentos/investimentos.py iniciar
python tools/investimentos/investimentos.py avaliar acoes ~/financas/indicadores_acoes.csv
python tools/investimentos/investimentos.py avaliar fiis ~/financas/indicadores_fiis.csv
python tools/investimentos/investimentos.py avaliar caixa ~/financas/indicadores_caixa.csv
python tools/investimentos/investimentos.py avaliar internacional ~/financas/indicadores_internacional.csv
python tools/investimentos/investimentos.py aporte ~/financas/carteira.csv 800
python tools/investimentos/investimentos.py comparar ~/financas/carteiras.csv
```

Os modelos de CSV estão em tools/investimentos/modelos (tickers inventados). A política completa fica em ~/financas/politica-investimentos.md.
