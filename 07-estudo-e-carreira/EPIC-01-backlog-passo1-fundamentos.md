---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# EPIC-01: Fundamentos de Lógica de Programação e Matemática Básica
### Backlog no formato Sprint/User Story/Task — Passo 1 do plano mestre

---

## Visão geral do Epic

| Campo | Valor |
|---|---|
| **Epic** | EPIC-01 — Fundamentos |
| **Objetivo** | Dominar lógica de programação e matemática básica o suficiente para iniciar C# com fundamento real, sem lacuna |
| **Duração estimada** | 2-3 semanas (9h/semana ≈ 18-27h totais) |
| **Definição de pronto do Epic** | Todas as User Stories abaixo com status "Done", critério de aceite validado em cada uma |
| **Dependência** | Nenhuma — ponto de partida do projeto inteiro |
| **Bloqueia** | EPIC-02 (C# Fundamentals) não inicia sem este Epic em "Done" |

---

## Sprint 1 — Lógica Booleana e Estruturas de Controle (semana 1)

### US-01 — Variáveis, tipos e operadores
**Como** desenvolvedor em formação, **quero** dominar variável, tipo primitivo e operador, **para que** eu consiga representar e manipular dado corretamente em qualquer linguagem.

**Tasks:**
- [ ] TASK-01.1 — Estudar variável, constante, tipo primitivo (inteiro, decimal, texto, booleano)
- [ ] TASK-01.2 — Estudar operador aritmético (`+ - * / %`) e ordem de precedência
- [ ] TASK-01.3 — Estudar operador relacional (`== != > < >= <=`)
- [ ] TASK-01.4 — Estudar operador lógico (`&& || !`) e tabela-verdade de cada um
- [ ] TASK-01.5 — Exercício: escrever 10 expressões booleanas compostas e prever o resultado antes de rodar

**Critério de aceite:** dado uma expressão booleana composta com 3+ operadores, consegue calcular o resultado manualmente antes de rodar o código, e acerta.

**Estimativa:** 3h | **Prioridade:** Crítica

---

### US-02 — Estruturas condicionais
**Como** desenvolvedor em formação, **quero** dominar `if/else` e `switch`, **para que** eu consiga implementar regra de decisão de negócio.

**Tasks:**
- [ ] TASK-02.1 — Estudar `if / else if / else`
- [ ] TASK-02.2 — Estudar `switch/case`, quando usar em vez de `if` encadeado
- [ ] TASK-02.3 — Exercício: implementar a escada de inadimplência (dias em atraso → status) só com `if/else`
- [ ] TASK-02.4 — Exercício: reescrever o mesmo exercício com `switch` sobre uma faixa pré-calculada, comparar legibilidade

**Critério de aceite:** os dois exercícios rodam e retornam o status correto para pelo menos 5 casos de teste diferentes (incluindo caso-limite, ex: exatamente no dia de virada de status).

**Estimativa:** 3h | **Prioridade:** Crítica

---

### US-03 — Estruturas de repetição
**Como** desenvolvedor em formação, **quero** dominar `for`, `while` e `do-while`, **para que** eu consiga processar coleção de dado e evitar loop infinito.

**Tasks:**
- [ ] TASK-03.1 — Estudar `for` (inicialização, condição, incremento)
- [ ] TASK-03.2 — Estudar `while` e `do-while`, diferença entre eles
- [ ] TASK-03.3 — Estudar `break` e `continue`
- [ ] TASK-03.4 — Exercício: identificar e corrigir 3 trechos de código com loop infinito proposital
- [ ] TASK-03.5 — Exercício: somar valores de uma lista de preços, aplicando desconto condicional dentro do loop

**Critério de aceite:** identifica corretamente por que cada um dos 3 loops travava, sem rodar o código pra descobrir — só lendo.

**Estimativa:** 3h | **Prioridade:** Crítica

---

## Sprint 2 — Estruturas de Dados, Funções e Depuração (semana 1-2)

### US-04 — Coleções básicas
**Como** desenvolvedor em formação, **quero** dominar array, lista, dicionário, pilha e fila, **para que** eu consiga organizar dado de forma apropriada ao problema.

**Tasks:**
- [ ] TASK-04.1 — Estudar array (índice, tamanho fixo)
- [ ] TASK-04.2 — Estudar lista (tamanho dinâmico)
- [ ] TASK-04.3 — Estudar dicionário/mapa (chave-valor)
- [ ] TASK-04.4 — Estudar noção de pilha (LIFO) e fila (FIFO), com exemplo do dia a dia
- [ ] TASK-04.5 — Exercício: modelar um carrinho de compra como lista de itens (nome, preço, quantidade)

**Critério de aceite:** consegue explicar, sem consultar nada, quando usar dicionário em vez de lista.

**Estimativa:** 3h | **Prioridade:** Alta

---

### US-05 — Funções e escopo
**Como** desenvolvedor em formação, **quero** dominar função, parâmetro, retorno e escopo, **para que** eu consiga organizar código em blocos reutilizáveis.

**Tasks:**
- [ ] TASK-05.1 — Estudar declaração de função, parâmetro, valor de retorno
- [ ] TASK-05.2 — Estudar escopo de variável (local vs. global)
- [ ] TASK-05.3 — Estudar função pura vs. função com efeito colateral
- [ ] TASK-05.4 — Exercício: refatorar o exercício do carrinho (US-04) extraindo o cálculo de desconto para uma função pura separada

**Critério de aceite:** a função de desconto extraída não modifica nenhuma variável fora dela, só recebe parâmetro e retorna valor.

**Estimativa:** 2h | **Prioridade:** Alta

---

### US-06 — Recursão e complexidade
**Como** desenvolvedor em formação, **quero** entender recursão e ter noção de complexidade, **para que** eu reconheça quando um código vai ficar lento antes de rodar.

**Tasks:**
- [ ] TASK-06.1 — Estudar recursão (caso base, chamada recursiva) com exemplo de fatorial
- [ ] TASK-06.2 — Exercício: implementar busca simples numa lista, de forma recursiva e de forma iterativa, comparar
- [ ] TASK-06.3 — Estudar noção informal de complexidade (por que loop dentro de loop cresce mais rápido)
- [ ] TASK-06.4 — Exercício: identificar, em 3 trechos de código dados, qual tem loop aninhado desnecessário

**Critério de aceite:** explica, em uma frase, por que um loop dentro de outro loop processando a mesma lista duas vezes é mais lento que dois loops separados.

**Estimativa:** 2h | **Prioridade:** Média

---

### US-07 — Depuração
**Como** desenvolvedor em formação, **quero** saber ler mensagem de erro e usar log, **para que** eu consiga encontrar problema no meu próprio código sem depender de ajuda externa.

**Tasks:**
- [ ] TASK-07.1 — Praticar leitura de mensagem de erro (o que ela diz, onde apontar primeiro)
- [ ] TASK-07.2 — Praticar uso de `print`/log pra inspecionar valor de variável em ponto intermediário do código
- [ ] TASK-07.3 — Exercício: dado um trecho de código com erro proposital, encontrar e corrigir usando só a mensagem de erro

**Critério de aceite:** encontra o erro proposital em menos de 5 minutos, sem pedir ajuda.

**Estimativa:** 1h | **Prioridade:** Média

---

## Sprint 3 — Matemática Básica, Parte I completa (paralelo aos Sprints 1-2, mesma semana)

> **Segunda correção:** com o sumário exato (via foto, com subtópico) em mãos, o Passo 1 cobre **só a Parte I do livro** (capítulos 1-2, completos) — nada da Parte II entra aqui. A Parte II (Naturais/Inteiros/Aritmética Modular/Racionais/Aplicações Aritméticas/Sequências/Reais) é densa demais pra caber "de raspão" no Passo 1 — ela vira bloco próprio nos Passos 2-6, com destaque para uma conexão forte: o Algoritmo de Euclides (dentro do Capítulo 3) é literalmente um algoritmo recursivo, ótimo pra estudar junto com recursão (US-06). Ver [[matematica-e-desenvolvimento-integrado]] para o mapeamento completo e atualizado.

### US-08 — Linguagem Matemática (Capítulo 1 completo)
**Como** estudante de matemática, **quero** dominar a linguagem/notação matemática formal, **para que** eu consiga ler e escrever proposição, símbolo lógico e notação de conjunto corretamente.

**Tasks:**
- [ ] TASK-08.1 — Ler 1.1 Raciocínio e 1.2 Sentenças
- [ ] TASK-08.2 — Ler 1.3 Conectivos e 1.4 Quantificadores
- [ ] TASK-08.3 — Ler 1.5 Tabelas-verdade compostas, tautologias e contradições — construir tabela-verdade de `E`, `OU`, `NÃO`, condicional e bicondicional à mão
- [ ] TASK-08.4 — Comparar cada linha da tabela-verdade com o resultado do `&&`/`||`/`!` testado no código (US-01)
- [ ] TASK-08.5 — Ler 1.6 Argumentos e 1.7 Equivalências
- [ ] TASK-08.6 — Ler 1.8 Tipos de demonstração (nível de reconhecimento — não precisa dominar prova formal ainda, só saber que existem tipos diferentes)
- [ ] TASK-08.7 — Exercício: traduzir 5 frases em português pra notação lógica formal, e vice-versa

**Critério de aceite:** monta a tabela-verdade de uma proposição composta com 3 termos sem erro, identifica se um argumento é válido ou uma tautologia/contradição, e reconhece (sem precisar aplicar) os tipos de demonstração do livro.

**Estimativa:** 3h | **Prioridade:** Crítica

---

### US-09 — Teoria Ingênua dos Conjuntos (Capítulo 2 completo)
**Como** estudante de matemática, **quero** dominar conjunto, axioma, subconjunto, operação, produto cartesiano e relação, **para que** eu tenha base pra estrutura de dado e pra `JOIN` de banco de dado mais adiante.

**Tasks:**
- [ ] TASK-09.1 — Ler 2.1 Introdução e 2.2 Axiomas
- [ ] TASK-09.2 — Ler 2.3 Subconjuntos
- [ ] TASK-09.3 — Ler 2.4 Operações — exercício de união, interseção, diferença e complemento de 3+ conjuntos, com Diagrama de Venn
- [ ] TASK-09.4 — Ler 2.5 Produto cartesiano e relações
- [ ] TASK-09.5 — Relacionar 2.4 com dicionário/coleção (US-04) e 2.5 com `JOIN` de tabela (vai reaparecer no Passo 2, SQL) — anotar a conexão agora pra reconhecer depois

**Critério de aceite:** resolve exercício de operação de conjunto com 3 conjuntos simultâneos, e explica o que é produto cartesiano com exemplo próprio (ex: todas as combinações de tamanho × cor de um produto).

**Estimativa:** 3h | **Prioridade:** Crítica

---

### US-10 — Notação Científica e Unidades (Parte VIII, leitura rápida)
**Como** estudante de matemática, **quero** dominar notação científica e conversão de unidade, **para que** eu consiga representar número muito grande ou muito pequeno corretamente.

**Tasks:**
- [ ] TASK-10.1 — Ler o capítulo 21 "Notação Científica" (21.1-21.4)
- [ ] TASK-10.2 — Ler o capítulo 22 "Unidades" (22.1-22.3)
- [ ] TASK-10.3 — Exercício: converter 5 números entre notação decimal e científica

**Critério de aceite:** converte número grande (ex: população de uma cidade) pra notação científica sem erro.

**Estimativa:** 1h | **Prioridade:** Baixa (não bloqueia nada, mas é rápido — vale fazer agora)

---

### US-11 — Apêndice B: Orientações para estudar matemática
**Como** estudante autodidata, **quero** ler as orientações do próprio autor sobre como estudar o livro, **para que** eu aproveite melhor o restante do conteúdo desde o início.

**Tasks:**
- [ ] TASK-11.1 — Ler o Apêndice B completo, antes de avançar pra Parte II

**Critério de aceite:** aplica pelo menos uma recomendação do apêndice já nesta primeira semana de estudo.

**Estimativa:** 30min | **Prioridade:** Alta (barato e o autor conhece o próprio livro melhor que qualquer aproximação externa)

---

## Sprint 4 — Projeto de Consolidação (fim da semana 2/início da 3)

### US-12 — Simulação de carrinho de compra com desconto
**Critério de aceite:** dado uma lista de produtos com preço e quantidade, e uma regra de desconto (ex: 10% acima de R$200), calcula o total corretamente para pelo menos 5 cenários de teste diferentes, incluindo caso-limite. **Nota:** o cálculo de porcentagem aqui usa o conhecimento intuitivo que você já tem de escola — a fundamentação formal de porcentagem/juros (Capítulo 6 do livro) vem no Passo 2-6, não bloqueia este exercício agora.
**Estimativa:** 2h | **Prioridade:** Crítica | **Depende de:** US-01 a US-05

### US-13 — Simulação da escada de inadimplência (`aura-licensing`)
**Critério de aceite:** função recebe "dias em atraso" e retorna status (ativo/atraso/restrito/suspenso) corretamente nos 4 casos e nos limites entre eles.
**Estimativa:** 1h30 | **Prioridade:** Alta | **Depende de:** US-02

### US-14 — Simulação simplificada do rebalanceamento ARCA (AM Rendara)
**Critério de aceite:** função recebe 4 valores de quadrante e retorna quanto falta para cada um chegar a 25% do total, sem usar banco de dado, só aritmética e `if`.
**Estimativa:** 2h | **Prioridade:** Alta | **Depende de:** US-01

---

## Quadro resumo do Epic (visão de sprint board)

| Sprint | User Stories | Estimativa total | Status |
|---|---|---|---|
| Sprint 1 | US-01, US-02, US-03 | 9h | A fazer |
| Sprint 2 | US-04, US-05, US-06, US-07 | 8h | A fazer |
| Sprint 3 (paralelo) | US-08, US-09, US-10, US-11 | 7h30 | A fazer |
| Sprint 4 | US-12, US-13, US-14 | 5h30 | A fazer |
| **Total do Epic** | 14 User Stories, 32 Tasks | **~30h** | — |

Com 9h/semana, isso é **~3,3 semanas** — a Parte II inteira do livro (Teoria dos Números — Naturais/Inteiros, Aritmética Modular, Racionais, Aplicações Aritméticas, Sequências, Reais) fica **fora** deste Epic de propósito, entrando no próximo (EPIC-02, junto com Git/SQL/C#), porque é densa demais pra caber no Passo 1 sem prejudicar a profundidade.

---

# O que estudar e dominar — checklist completo de conhecimento (Definition of Done do Epic)

Esta é a resposta direta à segunda parte do seu pedido: tudo que precisa estar dominado, não só "visto", pra considerar o Passo 1 100% concluído.

## Lógica de programação
- [ ] Variável, constante, tipo primitivo
- [ ] Operador aritmético e ordem de precedência
- [ ] Operador relacional
- [ ] Operador lógico (`&&`, `||`, `!`) e tabela-verdade de cada um
- [ ] `if/else if/else`
- [ ] `switch/case`
- [ ] `for`
- [ ] `while` e `do-while`
- [ ] `break` e `continue`
- [ ] Como identificar e evitar loop infinito
- [ ] Array (índice, tamanho fixo)
- [ ] Lista (tamanho dinâmico)
- [ ] Dicionário/mapa (chave-valor)
- [ ] Noção de pilha (LIFO) e fila (FIFO)
- [ ] Função: declaração, parâmetro, retorno
- [ ] Escopo de variável (local vs. global)
- [ ] Função pura vs. função com efeito colateral
- [ ] Recursão: caso base, chamada recursiva
- [ ] Noção informal de complexidade (por que loop aninhado é mais lento)
- [ ] Leitura de mensagem de erro
- [ ] Uso de log/print para depuração

## Matemática Básica — Passo 1 (Parte I completa: Capítulos 1-2, mais leitura rápida da Parte VIII e Apêndice B)
- [ ] 1.1 Raciocínio
- [ ] 1.2 Sentenças
- [ ] 1.3 Conectivos
- [ ] 1.4 Quantificadores
- [ ] 1.5 Tabelas-verdade compostas, tautologias e contradições
- [ ] 1.6 Argumentos
- [ ] 1.7 Equivalências
- [ ] 1.8 Tipos de demonstração (nível de reconhecimento)
- [ ] 2.1 Introdução (Teoria Ingênua dos Conjuntos)
- [ ] 2.2 Axiomas
- [ ] 2.3 Subconjuntos
- [ ] 2.4 Operações (união, interseção, diferença, complemento)
- [ ] 2.5 Produto cartesiano e relações
- [ ] 21. Notação Científica
- [ ] 22. Unidades
- [ ] Apêndice B — Orientações para estudar matemática

**A Parte II inteira (Capítulos 3-8: Naturais/Inteiros, Aritmética Modular, Racionais, Aplicações Aritméticas, Sequências, Reais) e as demais Partes (III a VII) estão mapeadas por Passo futuro em [[matematica-e-desenvolvimento-integrado]] — não fazem parte do Definition of Done deste Epic, de propósito. Destaque para o Capítulo 3 (Algoritmo de Euclides, indução) e o Capítulo 4 (Aritmética Modular, com aplicação a RSA) — conexões fortes e diretas com recursão (Passo 2-3) e com o `aura-vault` (Passo 9), respectivamente.**

## Critério final de "Passo 1 = 100% concluído"
Você resolve as três simulações da Sprint 4 (carrinho, inadimplência, ARCA) sem consultar nenhum material, explicando em voz alta por que cada linha de código está ali — se travar em qualquer explicação, é sinal de que algum item do checklist acima ainda não está realmente dominado, só "visto".

---

## 🔗 Documentos relacionados
- [[CARTAO-voce-esta-aqui]] — o resumo diário do que fazer agora
- [[metodo-estudo-producao-didatica-simultanea]] — como transformar cada User Story em material de aula
- [[matematica-e-desenvolvimento-integrado]] — o mapeamento completo do livro contra todas as fases futuras
 