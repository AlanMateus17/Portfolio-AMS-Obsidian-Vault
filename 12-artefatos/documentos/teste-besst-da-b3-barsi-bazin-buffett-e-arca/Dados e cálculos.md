# Dados e cálculos

Esta aba lista cada dado usado no teste, de onde veio, e cada conta feita. As contas foram geradas por código a partir destes mesmos dados.

## Fontes e datas

| Abreviação | Fonte | Data dos dados |
| --- | --- | --- |
| Sua lista | Arquivo que você enviou | 26/10/2026, no meio do pregão (horário exato não informado) |
| SI | [Status Invest](https://statusinvest.com.br/acoes/itsa4), página de cada ação | Consultado em 26/10/2026; a página não informa a hora do preço, e várias mostram preços diferentes no topo e no texto |
| DM | [Dados de Mercado](https://www.dadosdemercado.com.br/acoes/itsa4), páginas da ação e de dividendos | Preços de 23/10/2026 (último fechamento antes da eleição), salvo indicação; balanços até o 2T26 |
| Redentia | [Redentia](https://www.redentia.com.br/dividendos/BBDC4) | Consultado em 26/10/2026 |

**O que isso significa:** só os preços marcados "Sua lista" são de 26/10. Os demais são de 23/10 ou de data não informada, ou seja, de antes da queda de hoje. Os dividendos e balanços são históricos e não mudam com o dia.

## Fórmulas usadas

- Média de 5 anos = soma dos dividendos por ação de 2021 a 2025 ÷ 5
- Dividendo usado (Bazin) = menor entre a média de 5 anos e os últimos 12 meses
- Preço-teto = dividendo usado ÷ 0,06
- DY = dividendo usado ÷ preço × 100
- Desconto = (preço-teto − preço) ÷ preço-teto × 100
- Dívida (Bazin) = dívida líquida ÷ patrimônio líquido; passa se ≤ 1
- Dívida (Buffett) = dívida líquida ÷ EBITDA; passa se ≤ 3
- ROE (Buffett) = passa se ≥ 15% em pelo menos 8 dos anos de 2016 a 2025 e também nos últimos 12 meses

## Etapa 1: pararam no Barsi

| Empresa | Preço (R$) | Fonte do preço | Dados e motivo |
| --- | --- | --- | --- |
| Auren (AURE3) | 10,27 | Sua lista (26/10, intradiário) | Prejuízo nos 12 meses (P/L −14,69; ROE −9,47%, SI) e dividendos 12m R$ 0,00 (SI). Pagamentos por ano: 2022 R$ 0,10; 2023 R$ 3,00; 2024 R$ 0,40; 2025 R$ 0,057; 2026 R$ 0 (SI). |
| Eneva (ENEV3) | 24,98 | Sua lista (26/10, intradiário) | Dividendos 12m R$ 0,00 (SI); não distribui dividendos. |
| Light (LIGT3) | 3,67 | Status Invest (data não informada) | Dividendos 12m R$ 0,00; último provento R$ 0,25 em 29/12/2022 (SI). |
| Oi (OIBR3) | 0,10 | Status Invest | Recuperação judicial (SI); ROE −69,03%; dividendos 12m R$ 0,00. |
| Orizon (ORVR3) | 20,84 | Status Invest | Dividendos 12m R$ 0,00; ROE 1,04% (SI). |
| Banco Pan (BPAN4) | 12,71 | Status Invest | Dividendos por ano (SI): 2021 R$ 0,22; 2022 R$ 0,28; 2023 R$ 0,22; 2024 R$ 0,24; 2025 R$ 0; 2026 R$ 0. Não pagou em todos os anos. |
| BR Partners (BRBI11) | 18,67 | Status Invest | Dividendos por ano (SI): 2021 e 2022 sem registro; 2023 R$ 0,66; 2024 R$ 1,95; 2025 R$ 1,86. |
| Banco Pine (PINE4) | 16,44 | Dados de Mercado (data não informada) | Tabela anual do DM só tem 2023 (R$ 0,16), 2024 (R$ 0,61), 2025 (R$ 0,64); sem registro de 2021 e 2022. |

## Etapa 2: Bazin, preço-teto

Todas estas empresas passaram no Barsi. As contas usam os valores completos; a tabela mostra 2 casas decimais. Média "—" quer dizer que não levantei o histórico porque o teto pelos 12 meses já fica abaixo do preço, e a média só poderia baixar ainda mais o teto.

| Empresa | Preço (R$) · fonte | Div. 12m (R$) · fonte | Dividendos 2021 · 22 · 23 · 24 · 25 (R$) | Média = soma ÷ n | Usado = menor | Teto = usado ÷ 0,06 | DY = usado ÷ preço | Desconto = (teto − preço) ÷ teto | Resultado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Itaú (ITUB4) | 40,82 · Sua lista, 26/10 | 3,14 · SI | 0,91 · 1,02 · 1,26 · 2,41 · 4,73 (DM) | 10,33 ÷ 5 = 2,07 | 2,07 | 2,0659 ÷ 0,06 = 34,43 | 2,07 ÷ 40,82 = 5,06% | (34,43 − 40,82) ÷ 34,43 = −18,6% | ❌ preço acima do teto |
| Banco do Brasil (BBAS3) | 17,68 · Sua lista, 26/10 | 0,69 · SI | 1,13 · 2,09 · 2,29 · 2,61 · 1,18 (DM) | 9,30 ÷ 5 = 1,86 | 0,69 | 0,6904 ÷ 0,06 = 11,51 | 0,69 ÷ 17,68 = 3,90% | (11,51 − 17,68) ÷ 11,51 = −53,7% | ❌ preço acima do teto |
| BTG (BPAC11) | 52,50 · Sua lista, 26/10 | 1,42 · SI | — | — | 1,42 | 1,4201 ÷ 0,06 = 23,67 | 1,42 ÷ 52,50 = 2,70% | (23,67 − 52,50) ÷ 23,67 = −121,8% | ❌ preço acima do teto |
| Mercantil (BMEB4) | 79,97 · SI | 3,51 · SI | — | — | 3,51 | 3,5102 ÷ 0,06 = 58,50 | 3,51 ÷ 79,97 = 4,39% | (58,50 − 79,97) ÷ 58,50 = −36,7% | ❌ preço acima do teto |
| Banco do Nordeste (BNBR3) | 114,01 · SI | 6,93 · SI | 4,77 · 4,42 · 3,54 · 6,06 · 6,04 (DM) | 24,82 ÷ 5 = 4,96 | 4,96 | 4,9638 ÷ 0,06 = 82,73 | 4,96 ÷ 114,01 = 4,35% | (82,73 − 114,01) ÷ 82,73 = −37,8% | ❌ preço acima do teto |
| ABC Brasil (ABCB4) | 29,49 · DM 23/10 | 2,70 · SI | 1,25 · 1,40 · 1,58 · 1,65 · 2,62 (DM) | 8,49 ÷ 5 = 1,70 | 1,70 | 1,6982 ÷ 0,06 = 28,30 | 1,70 ÷ 29,49 = 5,76% | (28,30 − 29,49) ÷ 28,30 = −4,2% | ❌ preço acima do teto; mesmo abaixo do teto hoje, cairia no Buffett (ROE ≥ 15% em 2 de 10 anos) |
| Banrisul (BRSR6) | 18,16 · DM 23/10 | 1,60 · DM (total de 2025, usado como aproximação de 12m) | 0,95 · 0,88 · 0,92 · 0,99 · 1,60 (DM) | 5,35 ÷ 5 = 1,07 | 1,07 | 1,0702 ÷ 0,06 = 17,84 | 1,07 ÷ 18,16 = 5,89% | (17,84 − 18,16) ÷ 17,84 = −1,8% | ❌ preço acima do teto; mesmo abaixo do teto hoje, cairia no Buffett (ROE ≥ 15% em 1 de 10 anos) |
| BMG (BMGB4) | 7,21 · DM 23/10 | 0,55 · SI | 0,32 · 0,37 · 0,38 · 0,37 · 0,55 (DM) | 1,97 ÷ 5 = 0,39 | 0,39 | 0,3947 ÷ 0,06 = 6,58 | 0,39 ÷ 7,21 = 5,47% | (6,58 − 7,21) ÷ 6,58 = −9,6% | ❌ preço acima do teto; mesmo abaixo do teto hoje, cairia no Buffett (ROE ≥ 15% em 0 de 10 anos) |
| Banestes (BEES3) | 10,00 · SI | 0,78 · SI | 0,34 · 0,56 · 0,63 · 0,66 · 0,71 (DM) | 2,91 ÷ 5 = 0,58 | 0,58 | 0,5829 ÷ 0,06 = 9,72 | 0,58 ÷ 10,00 = 5,83% | (9,72 − 10,00) ÷ 9,72 = −2,9% | ❌ preço acima do teto; mesmo abaixo do teto hoje, cairia no Buffett (ROE ≥ 15% em 3 de 10 anos). Obs.: DM mostra R$ 10,15 em 23/10 |
| Copel (CPLE3) | 14,98 · Sua lista, 26/10 | 1,06 · SI | 1,19 · 0,81 · 0,30 · 0,39 · 1,22 (DM) | 3,91 ÷ 5 = 0,78 | 0,78 | 0,7816 ÷ 0,06 = 13,03 | 0,78 ÷ 14,98 = 5,22% | (13,03 − 14,98) ÷ 13,03 = −15,0% | ❌ preço acima do teto |
| Coelce (COCE5) | 37,50 · DM (data não informada) | 1,48 · DM (total 2026 até agora, aproximação de 12m) | 3,62 · 1,94 · 0,31 · 0,99 · 1,35 (DM) | 8,21 ÷ 5 = 1,64 | 1,48 | 1,4833 ÷ 0,06 = 24,72 | 1,48 ÷ 37,50 = 3,96% | (24,72 − 37,50) ÷ 24,72 = −51,7% | ❌ preço acima do teto |
| Engie (EGIE3) | 27,25 · Sua lista, 26/10 | 1,12 · SI | — | — | 1,12 | 1,1200 ÷ 0,06 = 18,67 | 1,12 ÷ 27,25 = 4,11% | (18,67 − 27,25) ÷ 18,67 = −46,0% | ❌ preço acima do teto |
| Neoenergia (NEOE3) | 33,81 · SI | 0,81 · SI | — | — | 0,81 | 0,8107 ÷ 0,06 = 13,51 | 0,81 ÷ 33,81 = 2,40% | (13,51 − 33,81) ÷ 13,51 = −150,2% | ❌ preço acima do teto |
| Celesc (CLSC4) | 189,49 · SI | 2,65 · SI | — | — | 2,65 | 2,6540 ÷ 0,06 = 44,23 | 2,65 ÷ 189,49 = 1,40% | (44,23 − 189,49) ÷ 44,23 = −328,4% | ❌ preço acima do teto |
| Rede Energia (REDE3) | 5,52 · SI | 0,18 · SI | — | — | 0,18 | 0,1758 ÷ 0,06 = 2,93 | 0,18 ÷ 5,52 = 3,18% | (2,93 − 5,52) ÷ 2,93 = −88,4% | ❌ preço acima do teto |
| Axia (AXIA3) | 49,08 · Sua lista, 26/10 | 1,89 · SI | 2,38 · 0,72 · 0,22 · 1,27 · 4,54 (SI) | 9,12 ÷ 5 = 1,82 | 1,82 | 1,8250 ÷ 0,06 = 30,42 | 1,82 ÷ 49,08 = 3,72% | (30,42 − 49,08) ÷ 30,42 = −61,4% | ❌ preço acima do teto. Obs.: histórico de dividendos do SI (por data com) |
| Equatorial (EQTL3) | 34,73 · Sua lista, 26/10 | 1,90 · SI | 0,72 · 0,64 · 0,35 · 0,45 · 2,24 (SI) | 4,40 ÷ 5 = 0,88 | 0,88 | 0,8799 ÷ 0,06 = 14,66 | 0,88 ÷ 34,73 = 2,53% | (14,66 − 34,73) ÷ 14,66 = −136,8% | ❌ preço acima do teto. Obs.: histórico do SI |
| Energisa (ENGI11) | 46,42 · Sua lista, 26/10 | 1,20 · SI | 3,95 · 1,16 · 2,50 · 1,00 · 3,60 (SI) | 12,21 ÷ 5 = 2,44 | 1,20 | 1,2012 ÷ 0,06 = 20,02 | 1,20 ÷ 46,42 = 2,59% | (20,02 − 46,42) ÷ 20,02 = −131,9% | ❌ preço acima do teto. Obs.: histórico do SI |
| Alupar (ALUP11) | 38,68 · SI | 1,08 · SI | — | — | 1,08 | 1,0800 ÷ 0,06 = 18,00 | 1,08 ÷ 38,68 = 2,79% | (18,00 − 38,68) ÷ 18,00 = −114,9% | ❌ preço acima do teto |
| Sabesp (SBSP3) | 25,73 · Sua lista, 26/10 | 0,70 · SI | 0,08 · 0,19 · 0,26 · 0,29 · 0,75 (SI) | 1,56 ÷ 5 = 0,31 | 0,31 | 0,3115 ÷ 0,06 = 5,19 | 0,31 ÷ 25,73 = 1,21% | (5,19 − 25,73) ÷ 5,19 = −395,6% | ❌ preço acima do teto. Obs.: histórico do SI, ajustado ao desdobramento |
| Sanepar (SAPR11) | 41,92 · SI | 0,55 · SI | — | — | 0,55 | 0,5524 ÷ 0,06 = 9,21 | 0,55 ÷ 41,92 = 1,32% | (9,21 − 41,92) ÷ 9,21 = −355,3% | ❌ preço acima do teto. Obs.: página do SI inconsistente; pelo maior valor (R$ 1,96 pagos em 2026) o DY seria 4,7%, ainda abaixo de 6% |
| Copasa (CSMG3) | 51,35 · Sua lista, 26/10 | 2,00 · SI | — | — | 2,00 | 1,9996 ÷ 0,06 = 33,33 | 2,00 ÷ 51,35 = 3,89% | (33,33 − 51,35) ÷ 33,33 = −54,1% | ❌ preço acima do teto |
| Caixa Seguridade (CXSE3) | 20,46 · Sua lista, 26/10 | 1,38 · DM (total 2026 com anunciados) | 0,24 · 0,65 · 1,01 · 1,08 · 1,26 (DM) | 4,25 ÷ 5 = 0,85 | 0,85 | 0,8492 ÷ 0,06 = 14,15 | 0,85 ÷ 20,46 = 4,15% | (14,15 − 20,46) ÷ 14,15 = −44,6% | ❌ preço acima do teto |
| Porto Seguro (PSSA3) | 46,87 · Sua lista, 26/10 | 3,00 · SI | 2,61 · 1,16 · 1,41 · 1,54 · 2,59 (DM) | 9,32 ÷ 5 = 1,86 | 1,86 | 1,8637 ÷ 0,06 = 31,06 | 1,86 ÷ 46,87 = 3,98% | (31,06 − 46,87) ÷ 31,06 = −50,9% | ❌ preço acima do teto |
| IRB (IRBR3) | 67,67 · SI | 1,56 · SI | — | — | 1,56 | 1,5552 ÷ 0,06 = 25,92 | 1,56 ÷ 67,67 = 2,30% | (25,92 − 67,67) ÷ 25,92 = −161,1% | ❌ preço acima do teto |
| Vivo (VIVT3) | 29,80 · Sua lista, 26/10 | 1,06 · SI | — | — | 1,06 | 1,0637 ÷ 0,06 = 17,73 | 1,06 ÷ 29,80 = 3,57% | (17,73 − 29,80) ÷ 17,73 = −68,1% | ❌ preço acima do teto |
| Unifique (FIQE3) | 6,20 · SI | 0,57 · SI | 0,08 · 0,08 · 0,15 · 0,21 · 0,88 (DM) | 1,41 ÷ 5 = 0,28 | 0,28 | 0,2826 ÷ 0,06 = 4,71 | 0,28 ÷ 6,20 = 4,56% | (4,71 − 6,20) ÷ 4,71 = −31,6% | ❌ preço acima do teto |
| Desktop (DESK3) | 19,24 · SI | 0,19 · SI | — | — | 0,19 | 0,1858 ÷ 0,06 = 3,10 | 0,19 ÷ 19,24 = 0,97% | (3,10 − 19,24) ÷ 3,10 = −521,3% | ❌ preço acima do teto |
| Brisanet (BRST3) | 2,98 · SI | 0,04 · SI | — | — | 0,04 | 0,0411 ÷ 0,06 = 0,68 | 0,04 ÷ 2,98 = 1,38% | (0,68 − 2,98) ÷ 0,68 = −335,0% | ❌ preço acima do teto |
| Itaúsa (ITSA4) | 13,04 · Sua lista, 26/10 | 1,32 · SI | 0,39 · 0,61 · 0,58 · 0,67 · 1,76 (DM) | 4,02 ÷ 5 = 0,80 | 0,80 | 0,8033 ÷ 0,06 = 13,39 | 0,80 ÷ 13,04 = 6,16% | (13,39 − 13,04) ÷ 13,39 = 2,6% | ✅ passa |
| Bradesco (BBDC4) | 15,22 · Sua lista, 26/10 | 1,61 · Redentia | 1,03 · 0,42 · 1,70 · 1,11 · 1,44 (DM) | 5,70 ÷ 5 = 1,14 | 1,14 | 1,1396 ÷ 0,06 = 18,99 | 1,14 ÷ 15,22 = 7,49% | (18,99 − 15,22) ÷ 18,99 = 19,9% | ✅ passa. Obs.: outras fontes: R$ 1,55 (Suno, ago/26) e R$ 2,49 (Renova) |
| Santander (SANB11) | 26,51 · Sua lista, 26/10 | 2,17 · SI | 2,84 · 2,24 · 1,67 · 1,61 · 1,88 (DM) | 10,23 ÷ 5 = 2,05 | 2,05 | 2,0463 ÷ 0,06 = 34,11 | 2,05 ÷ 26,51 = 7,72% | (34,11 − 26,51) ÷ 34,11 = 22,3% | ✅ passa |
| Banese (BGIP4) | 37,01 · SI | 4,50 · SI | 1,25 · 1,10 · 3,78 · 2,41 · 4,69 (DM) | 13,22 ÷ 5 = 2,64 | 2,64 | 2,6444 ÷ 0,06 = 44,07 | 2,64 ÷ 37,01 = 7,15% | (44,07 − 37,01) ÷ 44,07 = 16,0% | ✅ passa. Obs.: DM mostra R$ 37,54 em 23/10 |
| Banco da Amazônia (BAZA3) | 75,70 · SI | 8,01 · SI | 2,60 · 6,63 · 5,33 · 6,63 · 7,70 (DM) | 28,88 ÷ 5 = 5,78 | 5,78 | 5,7768 ÷ 0,06 = 96,28 | 5,78 ÷ 75,70 = 7,63% | (96,28 − 75,70) ÷ 96,28 = 21,4% | ✅ passa. Obs.: DM mostra R$ 77,20 em 23/10 |
| Taesa (TAEE11) | 40,31 · Sua lista, 26/10 | 3,01 · SI | 4,50 · 4,85 · 2,91 · 3,53 · 3,23 (DM) | 19,03 ÷ 5 = 3,81 | 3,01 | 3,0065 ÷ 0,06 = 50,11 | 3,01 ÷ 40,31 = 7,46% | (50,11 − 40,31) ÷ 50,11 = 19,6% | ✅ passa |
| ISA Energia (ISAE4) | 25,71 · Sua lista, 26/10 | 2,04 · SI | 3,59 · 1,06 · 2,20 · 0,00 · 3,29 (DM) | 10,14 ÷ 5 = 2,03 | 2,03 | 2,0283 ÷ 0,06 = 33,81 | 2,03 ÷ 25,71 = 7,89% | (33,81 − 25,71) ÷ 33,81 = 23,9% | ✅ passa. Obs.: 2024 = R$ 0 por data com: os pagamentos de 2024 tinham data com em dez/2023 |
| Cemig (CMIG4) | 10,17 · Sua lista, 26/10 | 0,79 · SI | 1,18 · 1,53 · 1,29 · 1,43 · 1,65 (DM) | 7,08 ÷ 5 = 1,42 | 0,79 | 0,7878 ÷ 0,06 = 13,13 | 0,79 ÷ 10,17 = 7,75% | (13,13 − 10,17) ÷ 13,13 = 22,5% | ✅ passa. Obs.: 2022 a 2025 com 2 casas, como a página mostra |
| CPFL (CPFE3) | 43,09 · Sua lista, 26/10 | 3,74 · SI | 3,70 · 3,24 · 2,89 · 2,75 · 2,79 (DM) | 15,37 ÷ 5 = 3,07 | 3,07 | 3,0739 ÷ 0,06 = 51,23 | 3,07 ÷ 43,09 = 7,13% | (51,23 − 43,09) ÷ 51,23 = 15,9% | ✅ passa. Obs.: 2024 e 2025 com 2 casas, como a página mostra |
| Coelba (CEEB3) | 45,50 · SI | 5,81 · SI | 6,55 · 6,45 · 4,56 · 3,17 · 6,02 (DM) | 26,75 ÷ 5 = 5,35 | 5,35 | 5,3495 ÷ 0,06 = 89,16 | 5,35 ÷ 45,50 = 11,76% | (89,16 − 45,50) ÷ 89,16 = 49,0% | ✅ passa |
| CEB (CEBR6) | 26,00 · SI | 3,50 · SI | 20,86 · 3,90 · 2,92 · 1,72 · 4,93 (DM) | 34,32 ÷ 5 = 6,86 | 3,50 | 3,5026 ÷ 0,06 = 58,38 | 3,50 ÷ 26,00 = 13,47% | (58,38 − 26,00) ÷ 58,38 = 55,5% | ✅ passa. Obs.: DM mostra R$ 28,40 em 07/10 |
| Elektro (EKTR4) | 49,50 · SI | 5,20 · SI | — · 7,88 · 4,02 · 5,93 · 5,06 (DM) | 22,89 ÷ 4 = 5,72 | 5,20 | 5,2036 ÷ 0,06 = 86,73 | 5,20 ÷ 49,50 = 10,51% | (86,73 − 49,50) ÷ 86,73 = 42,9% | ✅ passa. Obs.: 2021 sem dado: média de 4 anos |
| Rio Paranapanema (GEPA4) | 38,00 · SI / DM 23/10 | 4,30 · SI | 2,94 · 1,34 · 3,04 · 2,96 · 10,21 (DM) | 20,49 ÷ 5 = 4,10 | 4,10 | 4,0978 ÷ 0,06 = 68,30 | 4,10 ÷ 38,00 = 10,78% | (68,30 − 38,00) ÷ 68,30 = 44,4% | ✅ passa |
| BB Seguridade (BBSE3) | 41,24 · Sua lista, 26/10 | 4,59 · SI | 1,00 · 1,97 · 3,49 · 2,65 · 4,26 (DM) | 13,36 ÷ 5 = 2,67 | 2,67 | 2,6728 ÷ 0,06 = 44,55 | 2,67 ÷ 41,24 = 6,48% | (44,55 − 41,24) ÷ 44,55 = 7,4% | ✅ passa |
| Wiz (WIZC3) | 7,07 · SI / DM 23/10 | 0,63 · SI | 0,61 · 0,59 · 0,45 · 0,25 · 0,57 (DM) | 2,45 ÷ 5 = 0,49 | 0,49 | 0,4909 ÷ 0,06 = 8,18 | 0,49 ÷ 7,07 = 6,94% | (8,18 − 7,07) ÷ 8,18 = 13,6% | ✅ passa |
| TIM (TIMS3) | 17,71 · Sua lista, 26/10 | 1,47 · SI | 0,43 · 0,58 · 0,91 · 1,14 · 2,51 (DM) | 5,57 ÷ 5 = 1,11 | 1,11 | 1,1148 ÷ 0,06 = 18,58 | 1,11 ÷ 17,71 = 6,29% | (18,58 − 17,71) ÷ 18,58 = 4,7% | ✅ passa |

## Etapa 3: Bazin (dívida) e Buffett (dívida, ROE, lucro)

Só as 16 que passaram no preço-teto. Dívida não se aplica a bancos e seguradoras.

| Empresa | Dívida líquida ÷ patrimônio (Bazin, máx. 1) | Dívida líquida ÷ EBITDA (Buffett, máx. 3) | ROE 2016 a 2025 (%) e 12 meses (DM) | Anos com ROE ≥ 15% | Lucro 2016 → 2025 (DM) | Resultado |
| --- | --- | --- | --- | --- | --- | --- |
| Itaúsa (ITSA4) | 4.086 ÷ 98.580 (R$ mi, DM, 2T26) = 0,04 → passa | 4.086 ÷ 20.464 (DM, 12m) = 0,20 → passa | 16,2 · 15,2 · 16,7 · 18,1 · 12,1 · 19,1 · 18,5 · 16,1 · 15,7 · 17,7; 12m: 18,5 | 9 de 10 → passa | R$ 8,22 bi → R$ 16,55 bi | ✅ passa para o valor intrínseco |
| Bradesco (BBDC4) | não se aplica | não se aplica | 15,0 · 13,3 · 15,8 · 16,9 · 11,5 · 14,9 · 13,4 · 9,4 · 11,9 · 14,2; 12m: 14,1 | 3 de 10; 12m abaixo de 15% → não passa | R$ 15,08 bi → R$ 24,55 bi | ❌ Buffett: ROE inconsistente |
| Santander (SANB11) | não se aplica | não se aplica | 8,8 · 10,5 · 14,0 · 17,1 · 12,7 · 14,7 · 13,0 · 8,3 · 11,2 · 10,2; 12m: 11,2 | 1 de 10; 12m abaixo de 15% → não passa | R$ 7,46 bi → R$ 12,97 bi | ❌ Buffett: ROE inconsistente |
| Banese (BGIP4) | não se aplica | não se aplica | 19,6 · 25,4 · 15,4 · 19,3 · 11,1 · 14,9 · 12,7 · 7,1 · 18,1 · 16,6; 12m: 17,2 | 6 de 10 → não passa | R$ 65,5 mi → R$ 151,5 mi | ❌ Buffett: ROE inconsistente |
| Banco da Amazônia (BAZA3) | não se aplica | não se aplica | 6,7 · 3,4 · 5,6 · 12,5 · 11,0 · 25,1 · 23,2 · 22,9 · 17,3 · 15,4; 12m: 12,1 | 5 de 10; 12m abaixo de 15% → não passa | R$ 130,7 mi → R$ 1,11 bi | ❌ Buffett: ROE inconsistente |
| Taesa (TAEE11) | 10.413 ÷ 8.070 (R$ mi, DM, 2T26) = 1,29 → não passa | 10.413 ÷ 2.994 (DM) = 3,48 → não passa | não levantado (já reprovada na dívida) | — | — | ❌ Bazin: dívida acima do patrimônio |
| ISA Energia (ISAE4) | 15.968 ÷ 22.480 (R$ mi, DM, 2T26) = 0,71 → passa | 15.968 ÷ 5.206 (DM, 12m) = 3,07 → não passa | 48,1 · 12,4 · 16,8 · 12,9 · 23,9 · 20,5 · 14,0 · 16,3 · 17,7 · 11,7; 12m: 12,8 | 6 de 10; 12m abaixo de 15% → não passa | R$ 4,95 bi → R$ 2,51 bi | ❌ Buffett: dívida acima de 3 vezes o EBITDA; ROE inconsistente |
| Cemig (CMIG4) | 19.270 ÷ 29.190 (R$ mi, DM, 2T26) = 0,66 → passa | 19.270 ÷ 8.475 (DM, 12m) = 2,27 → passa | 2,6 · 7,0 · 10,9 · 19,7 · 16,4 · 19,3 · 18,8 · 23,4 · 26,0 · 17,1; 12m: 15,8 | 7 de 10 → não passa | R$ 334,8 mi → R$ 4,90 bi | ❌ Buffett: ROE inconsistente |
| CPFL (CPFE3) | 1,21 (SI) → não passa | 2,03 (SI) → passa | não levantado (já reprovada na dívida) | — | — | ❌ Bazin: dívida acima do patrimônio |
| Coelba (CEEB3) | 2,34 (SI) → não passa | sem dado (SI) | não levantado (já reprovada na dívida) | — | — | ❌ Bazin: dívida acima do patrimônio |
| CEB (CEBR6) | −0,30 (SI, caixa líquido) → passa | caixa líquido → passa | 15,8 · 21,2 · 14,6 · 15,7 · 51,7 · 122,3 · 21,0 · 18,5 · 17,1 · 20,2; 12m: 16,9 | 9 de 10 → passa | R$ 133,7 mi → R$ 235,3 mi | ✅ passa para o valor intrínseco |
| Elektro (EKTR4) | 2,92 (SI) → não passa | 2,76 (SI) → passa | não levantado (já reprovada na dívida) | — | — | ❌ Bazin: dívida acima do patrimônio |
| Rio Paranapanema (GEPA4) | 809 ÷ 1.380 (R$ mi, DM, 2T26) = 0,59 → passa | 809 ÷ 750 (DM, 12m) = 1,08 → passa | 20,4 · 14,4 · 15,7 · 15,9 · 36,7 · −0,5 · 13,0 · 18,8 · 27,1 · 20,2; 12m: 16,3 | 7 de 10 → não passa | R$ 361,0 mi → R$ 250,9 mi; prejuízo em 2021 → não passa | ❌ Buffett: ROE inconsistente; prejuízo em 2021 |
| BB Seguridade (BBSE3) | não se aplica | não se aplica | 48,4 · 45,5 · 51,8 · 126,9 · 60,3 · 54,0 · 79,6 · 81,0 · 89,8 · 86,8; 12m: 84,4 | 10 de 10 → passa | R$ 4,01 bi → R$ 9,02 bi | ✅ passa para o valor intrínseco |
| Wiz (WIZC3) | −0,02 (SI, caixa líquido) → passa | −18 ÷ 661 (DM, caixa líquido) = −0,03 → passa | 121,4 · 97,8 · 104,3 · 113,6 · 67,0 · 25,5 · 23,6 · 20,4 · 25,6 · 28,4; 12m: 25,8 | 10 de 10 → passa | R$ 148,2 mi → R$ 367,7 mi | ✅ passa para o valor intrínseco |
| TIM (TIMS3) | −0,39 (SI, caixa líquido) → passa | −1.881 ÷ 6.750 (DM, caixa líquido) = −0,28 → passa | — · 9,2 · 7,9 · 17,5 · 8,0 · 11,8 · 6,6 · 10,9 · 11,9 · 18,0; 12m: 7,1 | 2 de 9; 12m abaixo de 15% → não passa | R$ 101,5 mi (2017) → R$ 4,31 bi | ❌ Buffett: ROE inconsistente |

## Etapa 4: valor intrínseco (Buffett)

Premissas: lucro por ação dos últimos 12 meses; crescimento igual ao do lucro de 2016 a 2025, limitado a 10% ao ano, por 10 anos; depois, 4% ao ano para sempre; desconto de 13% ao ano; margem de segurança de 30%.

Fórmulas: lucro do ano k = lucro inicial × (1 + crescimento)^k · valor presente = lucro do ano ÷ 1,13^k · valor terminal = lucro do ano 10 × 1,04 ÷ (0,13 − 0,04), trazido a hoje ÷ 1,13^10.

#### Itaúsa (ITSA4)

- Preço: R$ 13,04 · Lucro por ação dos últimos 12 meses (DM): R$ 1,62
- Crescimento do lucro 2016→2025 = (16,55 ÷ 8,22)^(1/9) − 1 = **8,09% ao ano** → usado: 8,09% (limite de 10%)

| Ano | Lucro por ação (R$) | Fator de desconto (1,13^ano) | Valor presente (R$) |
| --- | --- | --- | --- |
| 1 | 1,7510 | 1,1300 | 1,5496 |
| 2 | 1,8926 | 1,2769 | 1,4822 |
| 3 | 2,0456 | 1,4429 | 1,4177 |
| 4 | 2,2110 | 1,6305 | 1,3561 |
| 5 | 2,3898 | 1,8424 | 1,2971 |
| 6 | 2,5830 | 2,0820 | 1,2407 |
| 7 | 2,7919 | 2,3526 | 1,1867 |
| 8 | 3,0177 | 2,6584 | 1,1351 |
| 9 | 3,2617 | 3,0040 | 1,0858 |
| 10 | 3,5254 | 3,3946 | 1,0385 |

- Soma dos 10 anos: R$ 12,79
- Valor terminal = 3,5254 × 1,04 ÷ (0,13 − 0,04) = R$ 40,74; trazido a hoje: 40,74 ÷ 3,3946 = R$ 12,00
- **Valor intrínseco = 12,79 + 12,00 = R$ 24,79**
- Preço máximo com margem de 30% = 24,79 × 0,70 = **R$ 17,35** → preço R$ 13,04 ≤ limite → **passa**
- Teste com desconto de 15%: valor R$ 19,94, limite R$ 13,96 → passa
- Teste sem crescimento (13%): valor R$ 14,31, limite R$ 10,01 → não passa

#### BB Seguridade (BBSE3)

- Preço: R$ 41,24 · Lucro por ação dos últimos 12 meses (DM): R$ 4,73
- Crescimento do lucro 2016→2025 = (9,02 ÷ 4,01)^(1/9) − 1 = **9,43% ao ano** → usado: 9,43% (limite de 10%)

| Ano | Lucro por ação (R$) | Fator de desconto (1,13^ano) | Valor presente (R$) |
| --- | --- | --- | --- |
| 1 | 5,1758 | 1,1300 | 4,5804 |
| 2 | 5,6637 | 1,2769 | 4,4355 |
| 3 | 6,1975 | 1,4429 | 4,2952 |
| 4 | 6,7816 | 1,6305 | 4,1593 |
| 5 | 7,4208 | 1,8424 | 4,0277 |
| 6 | 8,1202 | 2,0820 | 3,9003 |
| 7 | 8,8856 | 2,3526 | 3,7769 |
| 8 | 9,7231 | 2,6584 | 3,6574 |
| 9 | 10,6396 | 3,0040 | 3,5417 |
| 10 | 11,6424 | 3,3946 | 3,4297 |

- Soma dos 10 anos: R$ 39,80
- Valor terminal = 11,6424 × 1,04 ÷ (0,13 − 0,04) = R$ 134,53; trazido a hoje: 134,53 ÷ 3,3946 = R$ 39,63
- **Valor intrínseco = 39,80 + 39,63 = R$ 79,44**
- Preço máximo com margem de 30% = 79,44 × 0,70 = **R$ 55,61** → preço R$ 41,24 ≤ limite → **passa**
- Teste com desconto de 15%: valor R$ 63,57, limite R$ 44,50 → passa
- Teste sem crescimento (13%): valor R$ 41,77, limite R$ 29,24 → não passa

#### Wiz (WIZC3)

- Preço: R$ 7,07 · Lucro por ação dos últimos 12 meses (DM): R$ 1,24
- Crescimento do lucro 2016→2025 = (367,71 ÷ 148,21)^(1/9) − 1 = **10,62% ao ano** → usado: 10,00% (limite de 10%)

| Ano | Lucro por ação (R$) | Fator de desconto (1,13^ano) | Valor presente (R$) |
| --- | --- | --- | --- |
| 1 | 1,3640 | 1,1300 | 1,2071 |
| 2 | 1,5004 | 1,2769 | 1,1750 |
| 3 | 1,6504 | 1,4429 | 1,1438 |
| 4 | 1,8155 | 1,6305 | 1,1135 |
| 5 | 1,9970 | 1,8424 | 1,0839 |
| 6 | 2,1967 | 2,0820 | 1,0551 |
| 7 | 2,4164 | 2,3526 | 1,0271 |
| 8 | 2,6581 | 2,6584 | 0,9999 |
| 9 | 2,9239 | 3,0040 | 0,9733 |
| 10 | 3,2162 | 3,3946 | 0,9475 |

- Soma dos 10 anos: R$ 10,73
- Valor terminal = 3,2162 × 1,04 ÷ (0,13 − 0,04) = R$ 37,17; trazido a hoje: 37,17 ÷ 3,3946 = R$ 10,95
- **Valor intrínseco = 10,73 + 10,95 = R$ 21,67**
- Preço máximo com margem de 30% = 21,67 × 0,70 = **R$ 15,17** → preço R$ 7,07 ≤ limite → **passa**
- Teste com desconto de 15%: valor R$ 17,31, limite R$ 12,11 → passa
- Teste sem crescimento (13%): valor R$ 10,95, limite R$ 7,66 → passa

#### CEB (CEBR6)

- Preço: R$ 26,00 · Lucro por ação dos últimos 12 meses (DM): R$ 2,22
- Crescimento do lucro 2016→2025 = (235,31 ÷ 133,69)^(1/9) − 1 = **6,48% ao ano** → usado: 6,48% (limite de 10%)

| Ano | Lucro por ação (R$) | Fator de desconto (1,13^ano) | Valor presente (R$) |
| --- | --- | --- | --- |
| 1 | 2,3639 | 1,1300 | 2,0920 |
| 2 | 2,5172 | 1,2769 | 1,9713 |
| 3 | 2,6804 | 1,4429 | 1,8577 |
| 4 | 2,8542 | 1,6305 | 1,7505 |
| 5 | 3,0392 | 1,8424 | 1,6496 |
| 6 | 3,2363 | 2,0820 | 1,5544 |
| 7 | 3,4461 | 2,3526 | 1,4648 |
| 8 | 3,6695 | 2,6584 | 1,3803 |
| 9 | 3,9075 | 3,0040 | 1,3007 |
| 10 | 4,1608 | 3,3946 | 1,2257 |

- Soma dos 10 anos: R$ 16,25
- Valor terminal = 4,1608 × 1,04 ÷ (0,13 − 0,04) = R$ 48,08; trazido a hoje: 48,08 ÷ 3,3946 = R$ 14,16
- **Valor intrínseco = 16,25 + 14,16 = R$ 30,41**
- Preço máximo com margem de 30% = 30,41 × 0,70 = **R$ 21,29** → preço R$ 26,00 > limite → **não passa**
- Teste com desconto de 15%: valor R$ 24,62, limite R$ 17,24 → não passa
- Teste sem crescimento (13%): valor R$ 19,60, limite R$ 13,72 → não passa

## Etapa 5: qualitativo

- **Wiz (WIZC3):** no 2T26 a receita caiu 18% (R$ 235,3 mi) e o lucro ajustado consolidado caiu 13,5% (R$ 101 mi) ([BPMoney](https://bpmoney.com.br/mercado/wiz-co-wizc3-tem-lucro-de-r-101-milhoes-no-2t26-mas-resultado-recua-135/)). Em 19/10/2026 anunciou a venda dos 39,75% da Inter Seguros por R$ 409,5 mi; essa participação gerou cerca de R$ 16,2 mi dos R$ 53,6 mi de lucro do trimestre ([O Petróleo](https://opetroleo.com.br/wiz-wizc3-vende-negocio-por-r-409-milhoes-mas-pode-perder-30-do-lucro-trimestral/)). Conta: 16,2 ÷ 53,6 = 30%. **Não passa.**
- **BB Seguridade (BBSE3):** lucro de R$ 2,2 bi no 2T26, queda de 4%; seguro agrícola −22,9% ([Análise de Ações](https://www.analisedeacoes.com/noticias/bb-seguridade-bbse3-tem-lucro-de-2-2-bilhoes-no-2t26-queda-de-4-mas-resultado-ainda-fica-acima-das-projecoes/)). Controle do Banco do Brasil. **Passa com ressalva.**
- **Itaúsa (ITSA4):** lucro de R$ 4,3 bi no 2T26, alta de 7%; ROE recorrente de 18,7% ([Money Times](https://www.moneytimes.com.br/itausa-itsa4-lucra-r-43-bilhoes-alta-de-7-no-2t26/)). **Passa.**

## Divergências entre fontes

Encontrei estas diferenças entre fontes ao revisar. Nenhuma delas muda quem passa ou não, mas mostram por que vale conferir no RI antes de comprar.

| Empresa | Dado | Valor usado | Outro valor encontrado |
| --- | --- | --- | --- |
| Bradesco (BBDC4) | Dividendos 12 meses | R$ 1,61 (Redentia) | R$ 1,55 (Suno, ago/26) e R$ 2,49 (Renova). Não muda nada: o teto usa a média de 5 anos (R$ 1,14), que é menor |
| Cemig (CMIG4) | Dividendos 12 meses | R$ 0,79 (SI) | R$ 1,14 (outro site, out/26). Com R$ 1,14 o desconto seria maior |
| CPFL (CPFE3) | Dividendos 12 meses | R$ 3,74 (SI) | R$ 2,79 (Investidor10). Não muda nada: a média de 5 anos (R$ 3,07) é a usada, e a CPFL para na dívida |
| TIM (TIMS3) | ROE dos últimos 12 meses | 7,14% (DM) | 15,91% (SI). Não muda nada: a TIM falha por ter ROE ≥ 15% em só 2 de 9 anos |
| Banese (BGIP4) | Preço | R$ 37,01 (SI) | R$ 37,54 (DM, 23/10) |
| Banco da Amazônia (BAZA3) | Preço | R$ 75,70 (SI) | R$ 77,20 (DM, 23/10) |
| Banestes (BEES3) | Preço | R$ 10,00 (SI) | R$ 10,15 (DM, 23/10) |
| CEB (CEBR6) | Preço | R$ 26,00 (SI) | R$ 28,40 (DM, 07/10) |
| Wiz (WIZC3) | Lucro usado no crescimento | Lucro consolidado (DM) | O lucro dos controladores é menor (R$ 53,6 mi no 2T26 contra R$ 101 mi consolidado ajustado). Não muda nada: a Wiz para no qualitativo |
