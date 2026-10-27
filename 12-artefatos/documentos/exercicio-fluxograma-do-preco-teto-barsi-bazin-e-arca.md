# Exercício: Fluxograma do Preço-Teto (Barsi, Bazin e ARCA)

Oct 26, 2026 · @Alan Mateus

Neste exercício, você vai desenhar um fluxograma que decide, para cada empresa, se a ação está barata, no limite ou cara, seguindo três métodos de investimento por dividendos.

## Contexto e objetivo

Investidores que buscam renda com dividendos usam regras simples para decidir se uma ação vale a compra. Essas regras são um ótimo algoritmo: têm entradas, cálculos, decisões e uma saída.

Ao final, você deve ser capaz de:

- Identificar as entradas, os processos, as decisões e as saídas de um algoritmo real.
- Representar decisões encadeadas e repetição em um fluxograma.
- Aplicar o fluxograma aos dados e conferir os resultados à mão.

Os dados são de 26/10/2026 e servem só para fins didáticos. Este exercício não é recomendação de investimento.

## Conceitos e métricas

O fluxograma usa seis métricas, sempre nesta ordem.

**1. Filtro de setor (método Barsi).** A empresa só segue se for de um setor BESST: **B**ancos, **E**nergia, **S**aneamento, **S**eguros ou **T**elecomunicações. Se não for, o fluxograma descarta a empresa sem fazer nenhuma conta.

**2. DPA usado (dividendo por ação).** É quanto a empresa pagou de dividendos por ação. Algumas empresas têm dois valores: os últimos 12 meses e a média de 5 anos. Nesse caso, use o **menor** dos dois, que é o mais conservador. Se só houver o valor de 12 meses, use ele.

```latex
DPA_{usado} = \min(DPA_{12m},\ DPA_{5a})
```

**3. Dividend Yield (DY).** É quanto a ação paga por ano em relação ao preço, em porcentagem.

```latex
DY = \frac{DPA_{usado}}{Preço} \times 100
```

**4. Preço-teto (método Bazin).** É o preço máximo para a ação render pelo menos 6% ao ano.

```latex
PreçoTeto = \frac{DPA_{usado}}{0{,}06}
```

**5. Desconto.** É quanto o preço atual está abaixo do preço-teto, em porcentagem. Desconto negativo quer dizer que a ação está acima do teto.

```latex
Desconto = \frac{PreçoTeto - Preço}{PreçoTeto} \times 100
```

**6. Classificação.**

| Condição | Classificação |
| --- | --- |
| Desconto ≥ 20% | Compra com folga |
| 0% ≤ Desconto < 20% | No limite |
| Desconto < 0% | Acima do teto (não compra) |

**7. Aporte pelo ARCA.** O ARCA divide a carteira em quatro partes: **A**ções, **R**eal estate (fundos imobiliários), **C**aixa e **I**nternacional. Cada parte tem uma porcentagem-meta. O dinheiro novo só vai para ações até essa parte chegar na meta.

```latex
Aporte = (Carteira \times Meta) - ValorAtualEmAções
```

A quantidade de ações compradas é sempre um número inteiro, porque não se compra meia ação: use a parte inteira de Valor ÷ Preço.

## Símbolos do fluxograma

Use apenas estes cinco símbolos, ligados por setas que indicam a ordem.

| Símbolo | Forma | Quando usar | Exemplo neste exercício |
| --- | --- | --- | --- |
| Terminal | Oval | Início e fim | "Início", "Fim" |
| Entrada/Saída | Paralelogramo | Ler dados ou mostrar resultado | Ler Preço, DPA 12m, DPA 5a, Setor |
| Processo | Retângulo | Fazer um cálculo | Calcular PreçoTeto |
| Decisão | Losango | Pergunta de sim ou não | Setor é BESST? |
| Conector | Círculo pequeno | Juntar caminhos ou continuar em outra parte da folha | Volta para a próxima empresa |

Toda decisão tem exatamente duas saídas, marcadas **Sim** e **Não**.

## Dados das empresas

Estas são as entradas do seu algoritmo: 13 empresas, com preços de 26/10/2026. Quando a coluna da média de 5 anos estiver vazia, use só o DPA de 12 meses.

| Empresa | Código | Setor | Preço (R$) | DPA 12 meses (R$) | DPA média 5 anos (R$) |
| --- | --- | --- | --- | --- | --- |
| Bradesco | BBDC4 | Bancos | 15,22 | 1,55 |  |
| ISA Energia | ISAE4 | Energia | 25,71 | 2,04 |  |
| Taesa | TAEE11 | Energia | 40,31 | 3,01 |  |
| Itaú | ITUB4 | Bancos | 40,82 | 3,55 | 2,08 |
| Itaúsa | ITSA4 | Bancos | 13,04 | 1,32 | 0,79 |
| BB Seguridade | BBSE3 | Seguros | 41,24 | 4,53 | 2,67 |
| TIM | TIMS3 | Telecomunicações | 17,71 | 1,26 | 1,11 |
| Copel | CPLE3 | Energia | 14,98 | 1,06 |  |
| Vivo | VIVT3 | Telecomunicações | 29,80 | 1,06 |  |
| Banco do Brasil | BBAS3 | Bancos | 17,68 | 0,55 |  |
| Magazine Luiza | MGLU3 | Varejo | 5,70 |  |  |
| Vale | VALE3 | Mineração | 65,45 |  |  |
| Embraer | EMBR3 | Indústria | 95,17 |  |  |

As três últimas empresas não têm DPA na tabela de propósito: o seu fluxograma deve descartá-las antes de precisar desse dado.

## Exemplo resolvido: Itaú (ITUB4)

O Itaú termina **acima do teto**, mesmo pagando bons dividendos nos últimos 12 meses. Veja o passo a passo:

1. **Setor é BESST?** Bancos → Sim, segue.
2. **Tem média de 5 anos?** Sim → DPA usado = menor entre 3,55 e 2,08 = **2,08**.
3. **DY** = 2,08 ÷ 40,82 × 100 = **5,10%**.
4. **Preço-teto** = 2,08 ÷ 0,06 = **R$ 34,67**.
5. **Desconto** = (34,67 − 40,82) ÷ 34,67 × 100 = **−17,7%**.
6. **Desconto ≥ 20%?** Não. **Desconto ≥ 0%?** Não → **Acima do teto (não compra)**.

Repare na regra do passo 2: se você usasse o DPA de 12 meses (3,55), o Itaú pareceria barato. A escolha do valor mais conservador muda a resposta.

## Tarefas

**Parte 1 — Fluxograma para uma empresa**

1. Liste as **entradas**, os **processos**, as **decisões** e as **saídas** do algoritmo, antes de desenhar.
2. Desenhe o fluxograma que recebe os dados de **uma** empresa e mostra a classificação dela.
3. O fluxograma deve ter, no mínimo, quatro decisões: setor BESST, existência da média de 5 anos, desconto ≥ 20% e desconto ≥ 0%.
4. Faça o "teste de mesa": percorra o seu fluxograma com os dados do Itaú e confira se chega ao mesmo resultado do exemplo resolvido.

**Parte 2 — Fluxograma para todas as empresas**

5. Modifique o fluxograma para repetir o processo para as 13 empresas da tabela. Use um laço (repetição) com a pergunta "Ainda há empresas?".
6. Ao final, o fluxograma deve mostrar quantas empresas ficaram em cada classificação, incluindo as descartadas pelo setor.
7. Preencha esta tabela com os resultados do seu teste de mesa:

| Empresa | DPA usado (R$) | DY (%) | Preço-teto (R$) | Desconto (%) | Classificação |
| --- | --- | --- | --- | --- | --- |
| Bradesco |  |  |  |  |  |
| ISA Energia |  |  |  |  |  |
| Taesa |  |  |  |  |  |
| Itaú | 2,08 | 5,10 | 34,67 | −17,7 | Acima do teto |
| Itaúsa |  |  |  |  |  |
| BB Seguridade |  |  |  |  |  |
| TIM |  |  |  |  |  |
| Copel |  |  |  |  |  |
| Vivo |  |  |  |  |  |
| Banco do Brasil |  |  |  |  |  |
| Magazine Luiza |  |  |  |  |  |
| Vale |  |  |  |  |  |
| Embraer |  |  |  |  |  |

Arredonde valores em reais para 2 casas decimais e porcentagens para 1 ou 2 casas.

## Desafios extras

**Desafio A — Aporte pelo ARCA.** Um investidor tem uma carteira de R$ 4.000,00. A meta para ações é 25%, e ele já tem R$ 700,00 em ações.

- Acrescente ao fluxograma o cálculo do aporte máximo em ações.
- Divida esse aporte igualmente entre as empresas classificadas como "Compra com folga".
- Calcule quantas ações inteiras de cada empresa ele consegue comprar e quanto dinheiro sobra.

**Desafio B — Pseudocódigo.** Escreva o algoritmo da Parte 2 em Portugol, usando `leia`, `se`/`senao`, `enquanto` e `escreva`.

**Desafio C — Caso de borda.** A Taesa tem desconto de 19,6%. O que mudaria na classificação se o preço caísse R$ 0,20? Explique usando o seu fluxograma.

## Gabarito do professor

Resultado final: 2 empresas com folga, 5 no limite, 3 acima do teto e 3 descartadas pelo setor. Remova esta seção antes de entregar aos alunos.

| Empresa | DPA usado (R$) | DY (%) | Preço-teto (R$) | Desconto (%) | Classificação |
| --- | --- | --- | --- | --- | --- |
| Bradesco | 1,55 | 10,18 | 25,83 | 41,1 | Compra com folga |
| ISA Energia | 2,04 | 7,93 | 34,00 | 24,4 | Compra com folga |
| Taesa | 3,01 | 7,47 | 50,17 | 19,6 | No limite |
| Copel | 1,06 | 7,08 | 17,67 | 15,2 | No limite |
| BB Seguridade | 2,67 | 6,47 | 44,50 | 7,3 | No limite |
| TIM | 1,11 | 6,27 | 18,50 | 4,3 | No limite |
| Itaúsa | 0,79 | 6,06 | 13,17 | 1,0 | No limite |
| Itaú | 2,08 | 5,10 | 34,67 | −17,7 | Acima do teto |
| Vivo | 1,06 | 3,56 | 17,67 | −68,7 | Acima do teto |
| Banco do Brasil | 0,55 | 3,11 | 9,17 | −92,9 | Acima do teto |
| Magazine Luiza | — | — | — | — | Descartada (não é BESST) |
| Vale | — | — | — | — | Descartada (não é BESST) |
| Embraer | — | — | — | — | Descartada (não é BESST) |

Pontos de atenção na correção:

- Itaú, Itaúsa, BB Seguridade e TIM usam a média de 5 anos, porque ela é menor que o DPA de 12 meses.
- DY ≥ 6% equivale a desconto ≥ 0%. O aluno pode usar qualquer uma das duas perguntas, mas não as duas como se fossem diferentes.
- O laço precisa de um contador para cada classificação, iniciado em zero antes da repetição.

**Desafio A.** Aporte = 4.000 × 0,25 − 700 = **R$ 300,00**. Metade (R$ 150,00) para cada empresa com folga:

| Empresa | Valor (R$) | Ações inteiras | Gasto (R$) |
| --- | --- | --- | --- |
| Bradesco | 150,00 | 9 | 136,98 |
| ISA Energia | 150,00 | 5 | 128,55 |
| Total | 300,00 |  | 265,53 |

Sobra **R$ 34,47** em caixa.

**Desafio C.** Com o preço em R$ 40,11, o desconto passa para 20,05% e a Taesa vira "Compra com folga". A lição: perto do limite, uma variação pequena de preço muda a decisão.

O fluxograma de referência está logo abaixo.

&#91;embedded content: fluxograma de referência · 5 decisões, 1 laço\]

Cada empresa passa por no máximo quatro decisões e volta ao laço; o laço termina quando não há mais empresas, e então os contadores são mostrados.

Fontes dos dividendos: [Status Invest](https://statusinvest.com.br/acoes/taee11), [Visno](https://visnoinvest.com.br/stocks/ITUB4/dividends), [Suno](https://www.suno.com.br/noticias/bancos-ou-eletricas-qual-setor-paga-mais-dividendos-mt/), [Meus Dividendos](https://www.meusdividendos.com/acao/BBSE3) e [Investidor10](https://investidor10.com.br/acoes/cple3/). As fontes divergem em alguns valores; para a aula, vale o que está na tabela de dados.
