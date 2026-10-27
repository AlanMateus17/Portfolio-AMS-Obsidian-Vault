# Gabarito — Do Fluxograma ao Código

Uso do professor. Cada resposta traz o fluxograma em sequência de blocos, o código Portugol (VisuAlg) e o teste de mesa. Outras soluções corretas devem ser aceitas se o fluxograma e o código concordarem entre si.

## Sua vez e Nível 1

### Sua vez — média de três notas

**Fluxograma:** Início → Entrada: ler n1, n2, n3 → Processamento: media ← (n1 + n2 + n3) / 3 → Decisão: media >= 7? → Sim: Saída "Media - APROVADO" / Não: Saída "Media - RECUPERACAO" → Fim.

&#91;embedded content: fluxograma · Sua vez\]

```
algoritmo "MediaTresNotas"
var
   n1, n2, n3, media: real
inicio
   escreva("Digite a 1a nota: ")
   leia(n1)
   escreva("Digite a 2a nota: ")
   leia(n2)
   escreva("Digite a 3a nota: ")
   leia(n3)
   media <- (n1 + n2 + n3) / 3
   se media >= 7 entao
      escreval("Media: ", media:4:1, " - APROVADO")
   senao
      escreval("Media: ", media:4:1, " - RECUPERACAO")
   fimse
fimalgoritmo
```

| n1 | n2 | n3 | media | Saída |
| --- | --- | --- | --- | --- |
| 8 | 7 | 6 | 7,0 | Media: 7.0 - APROVADO (limite) |
| 5 | 6 | 7 | 6,0 | Media: 6.0 - RECUPERACAO |
| 9 | 9 | 9 | 9,0 | Media: 9.0 - APROVADO |

### 1. Conversor de temperatura

**Fluxograma:** Início → Entrada: ler c → Processamento: f ← c × 1,8 + 32 → Saída: mostrar f → Fim.

&#91;embedded content: fluxograma · exercício 1\]

```
algoritmo "CelsiusFahrenheit"
var
   c, f: real
inicio
   escreva("Temperatura em Celsius: ")
   leia(c)
   f <- c * 1.8 + 32
   escreval(c:5:1, " C = ", f:5:1, " F")
fimalgoritmo
```

| c | f | Saída |
| --- | --- | --- |
| 0 | 32,0 | 0.0 C = 32.0 F |
| 100 | 212,0 | 100.0 C = 212.0 F |
| 37 | 98,6 | 37.0 C = 98.6 F |

**Erro comum:** escrever `1,8` com vírgula. No VisuAlg o decimal é com ponto: `1.8`.

### 2. Pedido na lanchonete

**Fluxograma:** Início → Entrada: ler preco, qtd → Processamento: total ← preco × qtd → Saída: mostrar total → Fim.

&#91;embedded content: fluxograma · exercício 2\]

```
algoritmo "Lanchonete"
var
   preco, total: real
   qtd: inteiro
inicio
   escreva("Preco do lanche: ")
   leia(preco)
   escreva("Quantidade: ")
   leia(qtd)
   total <- preco * qtd
   escreval("Total a pagar: R$ ", total:6:2)
fimalgoritmo
```

| preco | qtd | total | Saída |
| --- | --- | --- | --- |
| 12,50 | 2 | 25,00 | Total a pagar: R$ 25.00 |
| 8,00 | 3 | 24,00 | Total a pagar: R$ 24.00 |

### 3. Tempo de jogo

**Fluxograma:** Início → Entrada: ler minutos → Processamento: horas ← minutos div 60; resto ← minutos mod 60 → Saída: mostrar horas e resto → Fim.

&#91;embedded content: fluxograma · exercício 3\]

```
algoritmo "TempoDeJogo"
var
   minutos, horas, resto: inteiro
inicio
   escreva("Minutos jogados: ")
   leia(minutos)
   horas <- minutos div 60
   resto <- minutos mod 60
   escreval(minutos, " minutos = ", horas, " horas e ", resto, " minutos")
fimalgoritmo
```

| minutos | horas | resto | Saída |
| --- | --- | --- | --- |
| 135 | 2 | 15 | 135 minutos = 2 horas e 15 minutos |
| 59 | 0 | 59 | 59 minutos = 0 horas e 59 minutos |
| 120 | 2 | 0 | 120 minutos = 2 horas e 0 minutos |

**Erro comum:** declarar as variáveis como `real`. `div` e `mod` só funcionam com `inteiro`.

## Nível 2 — Decisão

### 4. Par ou ímpar

**Fluxograma:** Início → Entrada: ler numero → Decisão: numero mod 2 = 0? → Sim: Saída "PAR" / Não: Saída "IMPAR" → Fim.

&#91;embedded content: fluxograma · exercício 4\]

```
algoritmo "ParOuImpar"
var
   numero: inteiro
inicio
   escreva("Digite um numero inteiro: ")
   leia(numero)
   se numero mod 2 = 0 entao
      escreval(numero, " e PAR")
   senao
      escreval(numero, " e IMPAR")
   fimse
fimalgoritmo
```

| numero | numero mod 2 | Saída |
| --- | --- | --- |
| 4 | 0 | 4 e PAR |
| 7 | 1 | 7 e IMPAR |
| 0 | 0 | 0 e PAR |

### 5. O maior número

**Fluxograma:** Início → Entrada: ler a, b → Decisão 1: a > b? → Sim: Saída "maior é a" / Não: Decisão 2: b > a? → Sim: Saída "maior é b" / Não: Saída "iguais" → Fim.

&#91;embedded content: fluxograma · exercício 5\]

```
algoritmo "MaiorNumero"
var
   a, b: real
inicio
   escreva("Primeiro numero: ")
   leia(a)
   escreva("Segundo numero: ")
   leia(b)
   se a > b entao
      escreval("O maior e ", a)
   senao
      se b > a entao
         escreval("O maior e ", b)
      senao
         escreval("Os numeros sao iguais")
      fimse
   fimse
fimalgoritmo
```

| a | b | a > b? | b > a? | Saída |
| --- | --- | --- | --- | --- |
| 9 | 4 | Sim | — | O maior e 9 |
| 3 | 8 | Não | Sim | O maior e 8 |
| 5 | 5 | Não | Não | Os numeros sao iguais |

### 6. Desconto no restaurante

**Fluxograma:** Início → Entrada: ler conta → Processamento: desconto ← 0 → Decisão: conta > 100? → Sim: desconto ← conta × 0,10 / Não: segue → Processamento: final ← conta − desconto → Saída: mostrar desconto e final → Fim.

&#91;embedded content: fluxograma · exercício 6\]

```
algoritmo "DescontoRestaurante"
var
   conta, desconto, final: real
inicio
   escreva("Valor da conta: ")
   leia(conta)
   desconto <- 0
   se conta > 100 entao
      desconto <- conta * 0.10
   fimse
   final <- conta - desconto
   escreval("Desconto: R$ ", desconto:6:2)
   escreval("Valor final: R$ ", final:6:2)
fimalgoritmo
```

| conta | conta > 100? | desconto | final |
| --- | --- | --- | --- |
| 150,00 | Sim | 15,00 | 135,00 |
| 100,00 | Não | 0,00 | 100,00 (limite) |
| 80,00 | Não | 0,00 | 80,00 |

### 7. Faixa etária

**Fluxograma:** Início → Entrada: ler idade → Decisão 1: idade <= 11? → Sim: Saída "CRIANCA" / Não: Decisão 2: idade <= 17? → Sim: Saída "ADOLESCENTE" / Não: Saída "ADULTO" → Fim.

&#91;embedded content: fluxograma · exercício 7\]

```
algoritmo "FaixaEtaria"
var
   idade: inteiro
inicio
   escreva("Idade: ")
   leia(idade)
   se idade <= 11 entao
      escreval("CRIANCA")
   senao
      se idade <= 17 entao
         escreval("ADOLESCENTE")
      senao
         escreval("ADULTO")
      fimse
   fimse
fimalgoritmo
```

| idade | idade <= 11? | idade <= 17? | Saída |
| --- | --- | --- | --- |
| 11 | Sim | — | CRIANCA (limite) |
| 12 | Não | Sim | ADOLESCENTE (limite) |
| 17 | Não | Sim | ADOLESCENTE (limite) |
| 18 | Não | Não | ADULTO (limite) |

**Erro comum:** testar `idade >= 12` e `idade <= 17` separados, sem `senao`. Funciona, mas o aluno costuma esquecer um dos lados e a idade 12 ou 17 cai na faixa errada.

## Nível 3 — Repetição e leitura reversa

### 8. Tabuada

**Fluxograma:** Início → Entrada: ler n → Processamento: i ← 1 → Decisão: i <= 10? → Sim: Saída "n x i = n×i" → Processamento: i ← i + 1 → seta volta para a decisão / Não: Fim.

&#91;embedded content: fluxograma · exercício 8\]

```
algoritmo "Tabuada"
var
   n, i: inteiro
inicio
   escreva("Numero da tabuada: ")
   leia(n)
   para i de 1 ate 10 faca
      escreval(n, " x ", i, " = ", n * i)
   fimpara
fimalgoritmo
```

| n | i | n \* i | Saída |
| --- | --- | --- | --- |
| 5 | 1 | 5 | 5 x 1 = 5 |
| 5 | 2 | 10 | 5 x 2 = 10 |
| 5 | … | … | … |
| 5 | 10 | 50 | 5 x 10 = 50 |
| 5 | 11 | — | (sai do laço) |

**Para o professor:** no fluxograma, o `para` aparece como inicialização (i ← 1), decisão (i <= 10?) e incremento (i ← i + 1). O `para` faz o incremento sozinho; o aluno não deve escrever `i <- i + 1` dentro dele.

### 9. Soma até o zero

**Fluxograma:** Início → Processamento: soma ← 0 → Entrada: ler num → Decisão: num <> 0? → Sim: Processamento: soma ← soma + num → Entrada: ler num → seta volta para a decisão / Não: Saída: mostrar soma → Fim.

&#91;embedded content: fluxograma · exercício 9\]

```
algoritmo "SomaAteZero"
var
   num, soma: real
inicio
   soma <- 0
   escreva("Digite um numero (0 para parar): ")
   leia(num)
   enquanto num <> 0 faca
      soma <- soma + num
      escreva("Digite um numero (0 para parar): ")
      leia(num)
   fimenquanto
   escreval("Soma: ", soma)
fimalgoritmo
```

| Caso | Números digitados | soma (passo a passo) | Saída |
| --- | --- | --- | --- |
| 1 | 5, 3, 2, 0 | 0 → 5 → 8 → 10 | Soma: 10 |
| 2 | 0 | 0 (não entra no laço) | Soma: 0 |
| 3 | 10, -4, 0 | 0 → 10 → 6 | Soma: 6 |

**Erro comum:** esquecer o segundo `leia(num)` dentro do laço. O número nunca muda e o programa entra em *loop* infinito.

### 10. Senha com três tentativas

**Fluxograma:** Início → Processamento: tentativas ← 0; acertou ← falso → Decisão: tentativas < 3 e não acertou? → Sim: Entrada: ler senha → Processamento: tentativas ← tentativas + 1 → Decisão: senha = 1234? → Sim: acertou ← verdadeiro / Não: Saída "Tentativas restantes" → seta volta para a primeira decisão / Não (saiu do laço): Decisão: acertou? → Sim: Saída "Acesso liberado" / Não: Saída "Acesso bloqueado" → Fim.

&#91;embedded content: fluxograma · exercício 10\]

```
algoritmo "SenhaTresTentativas"
var
   senha, tentativas: inteiro
   acertou: logico
inicio
   tentativas <- 0
   acertou <- falso
   enquanto (tentativas < 3) e (nao acertou) faca
      escreva("Digite a senha: ")
      leia(senha)
      tentativas <- tentativas + 1
      se senha = 1234 entao
         acertou <- verdadeiro
      senao
         escreval("Senha incorreta. Tentativas restantes: ", 3 - tentativas)
      fimse
   fimenquanto
   se acertou entao
      escreval("Acesso liberado")
   senao
      escreval("Acesso bloqueado")
   fimse
fimalgoritmo
```

| Caso | Senhas digitadas | Mensagens durante o laço | Saída final |
| --- | --- | --- | --- |
| 1 | 1234 | — | Acesso liberado |
| 2 | 1111, 1234 | Tentativas restantes: 2 | Acesso liberado |
| 3 | 1, 2, 3 | Restantes: 2, depois 1, depois 0 | Acesso bloqueado |

**Para o professor:** aceite soluções com `repita ... ate` ou com contador e `se` dentro do laço, desde que parem ao acertar e mostrem as tentativas restantes.

### 11. Leitura reversa (algoritmo "Misterio")

**O que faz:** diz se o número digitado é **primo**. Ele conta quantos divisores o número tem; se forem exatamente 2 (o 1 e ele mesmo), mostra SIM.

**Fluxograma:** Início → Entrada: ler n → Processamento: cont ← 0; i ← 1 → Decisão: i <= n? → Sim: Decisão: n mod i = 0? → Sim: cont ← cont + 1 / Não: segue → i ← i + 1 → seta volta para "i <= n?" / Não (saiu do laço): Decisão: cont = 2? → Sim: Saída "SIM" / Não: Saída "NAO" → Fim.

&#91;embedded content: fluxograma · exercício 11\]

| n | Divisores encontrados | cont | Saída |
| --- | --- | --- | --- |
| 7 | 1, 7 | 2 | SIM |
| 6 | 1, 2, 3, 6 | 4 | NAO |
| 1 | 1 | 1 | NAO |

## Desafio — Caixa da cantina

**Fluxograma:** Início → Processamento: subtotal ← 0 → (início do laço) Saída: mostrar cardápio → Entrada: ler codigo → Decisão: codigo = 0? → Sim: sai do laço / Não: Decisão: codigo entre 1 e 3? → Não: Saída "Item invalido" → volta ao cardápio / Sim: Entrada: ler qtd → Decisão: qtd <= 0? → Sim: Saída "Quantidade invalida" → volta ao cardápio / Não: Decisões do preço (1 → 6; 2 → 4; 3 → 5) → Processamento: subtotal ← subtotal + preco × qtd → volta ao cardápio. Depois do laço: Decisão: subtotal = 0? → Sim: Saída "Nenhum item comprado" / Não: desconto ← 0 → Decisão: subtotal > 30? → Sim: desconto ← subtotal × 0,05 → total ← subtotal − desconto → Saída: subtotal, desconto e total → Fim.

&#91;embedded content: fluxograma · desafio da cantina\]

```
algoritmo "CaixaCantina"
var
   codigo, qtd: inteiro
   preco, subtotal, desconto, total: real
inicio
   subtotal <- 0
   repita
      escreval("1 - Salgado (R$ 6,00)")
      escreval("2 - Suco (R$ 4,00)")
      escreval("3 - Bolo (R$ 5,00)")
      escreval("0 - Encerrar compra")
      escreva("Codigo do item: ")
      leia(codigo)
      se codigo <> 0 entao
         se (codigo < 1) ou (codigo > 3) entao
            escreval("Item invalido")
         senao
            escreva("Quantidade: ")
            leia(qtd)
            se qtd <= 0 entao
               escreval("Quantidade invalida")
            senao
               se codigo = 1 entao
                  preco <- 6
               senao
                  se codigo = 2 entao
                     preco <- 4
                  senao
                     preco <- 5
                  fimse
               fimse
               subtotal <- subtotal + preco * qtd
            fimse
         fimse
      fimse
   ate codigo = 0
   se subtotal = 0 entao
      escreval("Nenhum item comprado")
   senao
      desconto <- 0
      se subtotal > 30 entao
         desconto <- subtotal * 0.05
      fimse
      total <- subtotal - desconto
      escreval("Subtotal: R$ ", subtotal:6:2)
      escreval("Desconto: R$ ", desconto:6:2)
      escreval("Total a pagar: R$ ", total:6:2)
   fimse
fimalgoritmo
```

| Caso | Entradas (código × quantidade) | subtotal | desconto | Saída final |
| --- | --- | --- | --- | --- |
| 1 | 1×3, 2×2, 3×2, 0 | 36,00 | 1,80 | Subtotal 36.00, Desconto 1.80, Total 34.20 |
| 2 | 1×5, 0 | 30,00 | 0,00 | Subtotal 30.00, Desconto 0.00, Total 30.00 (limite) |
| 3 | 9, 2×0, 2×5, 0 | 20,00 | 0,00 | "Item invalido", "Quantidade invalida", depois Total 20.00 |
| 4 | 0 | 0,00 | — | Nenhum item comprado |

**Para o professor:** aceite `escolha ... caso` no lugar dos `se` do preço, ou `enquanto` no lugar de `repita`, desde que o código 0 encerre sem pedir quantidade.
