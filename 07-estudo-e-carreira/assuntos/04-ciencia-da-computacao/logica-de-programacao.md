---
tags: [estudo, assunto, ciencia-da-computacao, fundamentos]
area: 04 · Ciência da computação
nivel-alvo: N4
quando: M1 (semana 1)
professor: o-csharp (primeiro bloco)
prereq: []
status: estudando
atualizado: 2026-11-17
---

# Lógica de programação

> **Em uma frase:** lógica de programação é transformar um problema em **passos exatos** que uma máquina consegue seguir, usando poucas peças: guardar valores, decidir, repetir e agrupar passos com nome.
> **Nível-alvo:** N4. Você ensina isso na escola; aqui o objetivo é resolver qualquer exercício de lógica **sem travar e sem IA**, em qualquer linguagem.
> **Os 20% que resolvem 80%:** variável e tipo · condição (`if`) · laço (`for`/`while`) · função · coleção (lista e dicionário).

---

## 1. Por que isso existe (o problema e a história)

O computador só faz operações muito simples: somar, comparar, copiar um valor, pular para outra instrução. Qualquer programa, do jogo ao PDV, é uma combinação dessas operações. A lógica de programação é a ponte entre "o que eu quero" e "o que a máquina sabe fazer".

- **Ada Lovelace** (1843) escreveu o que se considera o primeiro algoritmo para uma máquina (a Máquina Analítica de Babbage), com repetição.
- **Alan Turing** (1936) mostrou que uma máquina com poucas operações (ler, escrever, mover, mudar de estado) consegue calcular tudo o que é calculável. Os livros que você comprou (*The Annotated Turing*, Sipser) contam essa história.
- **Böhm e Jacopini** (1966) provaram que qualquer programa pode ser escrito só com **sequência, decisão e repetição**. É a base da programação estruturada e de todo curso de lógica.

**A lição do Akita:** fundamentos antes de framework. Quem domina essas peças aprende qualquer linguagem em semanas, porque toda linguagem é só outra roupa para as mesmas ideias.

## 2. O que é

| Peça | O que faz | TypeScript |
|---|---|---|
| **Variável** | Dá nome a um valor guardado na memória | `let total = 0` · `const taxa = 0.1` |
| **Tipo** | Diz que tipo de valor é e o que dá para fazer com ele | `number`, `string`, `boolean` |
| **Operadores** | Aritméticos, de comparação e lógicos | `+ - * / %` · `=== !== < >` · `&& \|\| !` |
| **Condição** | Escolhe um caminho | `if (dias > 30) { ... } else { ... }` |
| **Laço** | Repete enquanto precisar | `for (const item of itens) { ... }` |
| **Função** | Agrupa passos com nome, entrada e saída | `function desconto(total: number): number { ... }` |
| **Coleção** | Guarda vários valores | lista: `[10, 20]` · dicionário: `{ nome: "pão", preco: 5 }` |
| **Recursão** | Uma função que chama a si mesma num problema menor | `fatorial(n) = n * fatorial(n - 1)` |

**Algoritmo** é a sequência finita e sem ambiguidade de passos que resolve o problema. **Pseudocódigo**, **fluxograma** e **teste de mesa** são ferramentas para pensar o algoritmo antes de escrever código.

## 3. Como funciona por baixo

- **Variável** = um endereço na memória com um nome que só existe para você. O processador vê só endereços e registradores.
- **`if`** vira, em linguagem de máquina, uma **comparação** seguida de um **salto condicional** (pule para tal instrução se a comparação deu falso).
- **Laço** é um salto **para trás**: compara, executa o corpo, volta para a comparação.
- **Função** usa a **pilha** (stack): ao chamar, o programa guarda onde estava e os parâmetros; ao terminar, desempilha e volta. Recursão sem caso de parada enche a pilha: é o famoso *stack overflow*.
- **Números com vírgula** são guardados em ponto flutuante binário, por isso `0.1 + 0.2` dá `0.30000000000000004`. Para dinheiro, use **centavos inteiros** (ver o assunto Dinheiro no código).

Episódios do Akita que mostram isso por dentro: [#80 Guia hardcore de introdução à computação](https://akitaonrails.com/2020/06/04/akitando-80-o-guia-hardcore-de-introducao-a-computacao/) e [#81 Computadores com Super Mario](https://akitaonrails.com/2020/06/18/akitando-81-aprendendo-sobre-computadores-com-super-mario-do-jeito-hardcore/).

## 4. Conceitos que você precisa dominar

- [ ] Declarar variável com `let` e `const`, e quando usar cada uma.
- [ ] Tipos primitivos e conversão (`Number("10")`, `String(10)`).
- [ ] Operadores de comparação estrita (`===`) e por que evitar `==` em JavaScript.
- [ ] `if / else if / else` e `switch`; condições compostas com `&&` e `||`.
- [ ] Casos-limite: o valor exatamente na fronteira (`>` ou `>=`?).
- [ ] `for`, `for...of`, `while`; quando cada um é mais claro.
- [ ] Laço infinito: como acontece e como evitar.
- [ ] Função com parâmetros e retorno; **função pura** (não mexe em nada fora dela).
- [ ] Escopo: variável dentro e fora do bloco.
- [ ] Lista (array): acessar, adicionar, percorrer, somar.
- [ ] Dicionário (objeto ou `Map`): quando usar em vez de lista.
- [ ] Recursão com caso de parada.
- [ ] Teste de mesa: executar o algoritmo à mão, linha a linha, anotando as variáveis.
- [ ] Decompor um problema grande em funções pequenas.

## 5. Qualidades

- Vale para **qualquer linguagem**: TypeScript, Python, Go, C.
- Treina o pensamento preciso, que também serve para matemática (lógica proposicional, conjuntos) e para revisar código da IA.
- É a base de tudo que vem depois: algoritmos, estruturas de dados, POO, SQL.

## 6. Defeitos, limites e críticas

- Lógica sozinha não faz software: falta organização (funções, módulos), testes e conhecimento do domínio.
- Exercício solto cansa e não fica. Por isso os seus exercícios são do seu domínio (carrinho, inadimplência, ARCA) e viram ativo.
- Cursos de lógica com pseudocódigo em português (Portugol) ajudam no começo, mas atrasam se você ficar muito tempo neles. Você já está pronto para a linguagem real.

## 7. Quando usar e quando não usar

Sempre. A pergunta não é "se", é **quanto tempo ficar só nisso**: o critério de pronto é resolver os 3 exercícios sem travar. Depois disso, a lógica continua sendo treinada dentro dos projetos.

## 8. Erros comuns

- Errar a fronteira: `dias > 30` quando a regra era "a partir de 30 dias".
- Mudar a lista enquanto percorre.
- Função que imprime em vez de **retornar** o valor (aí não dá para testar).
- Variável global usada por todo mundo.
- Não testar o caso vazio (carrinho sem itens) nem o caso-limite.
- Copiar a resposta da IA e não conseguir explicar cada linha.

## 9. No seu setup e no AM Gestão

- **Os 3 exercícios do Mês 1** são miniaturas de regras reais:
  - **Carrinho com desconto** → o total do pedido no módulo Caixa do AM Gestão.
  - **Escada de inadimplência** → a regra de status por dias em atraso (ativo, atraso, restrito, suspenso) da cobrança.
  - **Rebalanceamento ARCA simplificado** → quanto falta para cada um dos 4 quadrantes chegar a 25% (módulo financeiro e sua metodologia de investimento).
- Ficam no repositório `logica-ts`, com testes, e entram no portfólio.
- **Professor:** é o primeiro bloco do módulo `o-csharp` (TypeScript do zero ao confortável). Feche cada bloco com `just professor fechar ID MINUTOS`.

## 10. O que o mercado cobra

- **Júnior:** resolver problemas pequenos sem ajuda e explicar o raciocínio; os testes técnicos de entrada costumam ser exatamente isso.
- **Pleno e sênior:** a lógica vira base para algoritmos de entrevista (resolver em 30–40 minutos falando em voz alta) e para revisar código gerado por IA.
- **Perguntas comuns:** inverter uma string; achar o maior valor de uma lista sem `Math.max`; contar quantas vezes cada palavra aparece; FizzBuzz; validar CPF.

## 11. Exercícios

Sem IA. Use o [TS Playground](https://www.typescriptlang.org/play) até o setup ficar pronto.

- **N1 (reconhecer):** em 5 trechos de código, diga qual é a variável, a condição, o laço e a função. Faça o teste de mesa de um deles.
- **N2 (aplicar):** função que recebe a nota e devolve "aprovado", "recuperação" ou "reprovado"; função que soma uma lista de preços.
- **N3 (combinar e achar o erro):**
  - **Escada de inadimplência:** recebe dias em atraso e devolve o status nos 4 casos e nas fronteiras. Faça com `if/else` e depois com `switch`, e compare.
  - **Ache o erro:** uma função de desconto que usa `>` onde a regra diz "a partir de R$ 200".
- **N4 (mini-projeto real):**
  - **Carrinho com desconto:** lista de itens (nome, preço, quantidade) e regra de 10% acima de R$ 200, com o desconto numa **função pura** separada e 5 cenários de teste, incluindo carrinho vazio e o valor exato de R$ 200.
  - **ARCA simplificado:** recebe 4 valores e devolve quanto falta para cada um chegar a 25% do total.
  - Os três no repositório `logica-ts`, com README explicando cada um.

## 12. Fontes (na ordem de uso)

1. **Oficial:** [TypeScript Handbook: The Basics](https://www.typescriptlang.org/docs/handbook/2/basic-types.html) · [MDN: guia de JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide)
2. **Akita:** [#38 Conhecimentos básicos para iniciantes](https://akitaonrails.com/2019/02/06/akitando-38-conhecimentos-basicos-para-iniciantes-em-programacao-serie-comecando-aos-40/) · [#76 Aprendendo a aprender](https://akitaonrails.com/2020/04/01/akitando-76-guia-definitivo-de-aprendendo-a-aprender-a-maior-bronca-da-sua-vida-rated-r/) · #80 e #81 (seção 3)
3. **Alura:** "Lógica de programação: mergulhe em programação com JavaScript"
4. **Livro:** VHSlins, *Matemática Básica*, Parte I (lógica e conjuntos), estudada junto

## 13. Como saber que dominou

- [ ] Resolvo os 3 exercícios do N4 **de cabeça**, com o material fechado, explicando em voz alta por que cada linha está ali.
- [ ] Explico em 3 a 5 frases o que acontece na memória quando uma função é chamada.
- [ ] Escrevo os testes de fronteira antes de rodar.
- [ ] **Registro de entrevista:** contexto (regra de inadimplência), decisão (`if/else` com fronteiras testadas), alternativa descartada (`switch` sobre faixa), resultado (5 casos-limite passando).
- [ ] **N4:** usei os 3 exercícios numa aula de Lógica de Programação. Onde e quando: ______
