# Aula — Laboratório de Hardware: Diagnóstico de falhas (POST, bipes e sintomas)

Oct 20, 2026 · @Alan Mateus

Os alunos saem sabendo o que é o POST, como ler os bipes e qual peça testar primeiro em cada sintoma. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios).

## Roteiro da aula

1. Pergunta de abertura (5 min): "O PC liga, a ventoinha gira, mas a tela fica preta. O que vocês fariam?"
2. Quadro + explicação (35 min): blocos A a E abaixo, nessa ordem.
3. Demonstração em bancada, se houver uma máquina de sucata (10 min): tire a memória RAM, ligue e deixe a turma ouvir os bipes.
4. Exercícios no caderno.

## O que escrever no quadro

**Bloco A — O que é o POST**

- POST = Power-On Self Test (autoteste ao ligar).
- É feito pela BIOS/UEFI toda vez que o computador liga.
- Testa: processador, memória RAM, placa de vídeo e teclado.
- Passou no teste → 1 bipe curto (na maioria das placas) e o sistema carrega.
- Falhou → sequência de bipes ou LED de erro na placa-mãe.

**Bloco B — Códigos de bipe comuns (BIOS AMI)**

| Bipes | Provável problema |
| --- | --- |
| 1 curto | Tudo OK |
| Nenhum bipe e nada liga | Fonte, cabo de energia ou botão |
| Bipes curtos repetidos | Memória RAM |
| 1 longo + 2 ou 3 curtos | Placa de vídeo |
| Bipe contínuo | Memória RAM ou fonte |

Anote embaixo: "Os códigos mudam de fabricante para fabricante. Sempre confira o manual da placa-mãe."

**Bloco C — Sintomas e primeiro teste**

| Sintoma | Testar primeiro |
| --- | --- |
| Não liga nada (sem luz, sem ventoinha) | Tomada, cabo, chave da fonte, fonte |
| Liga, mas tela preta | Cabo do monitor, memória RAM, placa de vídeo |
| Desliga sozinho depois de um tempo | Superaquecimento (cooler e pasta térmica) |
| Hora e data sempre erradas | Bateria da placa-mãe (CR2032) |
| "No boot device" na tela | HD/SSD ou cabo SATA |

**Bloco D — Método de diagnóstico (passo a passo)**

1. Observar: ouvir bipes, ver LEDs, ler mensagens na tela.
2. Começar pelo mais simples: cabos, tomada, conexões.
3. Testar uma peça por vez.
4. Trocar por uma peça que funciona (teste de substituição).
5. Anotar o que foi testado e o resultado.

**Bloco E — Analogias, erros comuns e dicas**

- POST = check-up do PC. Bipes = o PC "dizendo onde dói".
- Regra de ouro: do mais simples para o mais complexo → muitas vezes é só cabo solto.
- Erro 1: trocar várias peças de uma vez → não dá para saber qual era o defeito.
- Erro 2: mexer no PC ligado na tomada → sempre desligar e tirar o cabo antes de abrir.
- Erro 3: achar que a tabela de bipes é igual em toda placa → muda por fabricante.
- Dica: tela preta? Limpe os contatos da memória RAM com borracha branca.
- Pergunta: o PC dá bipes curtos repetidos. Qual peça você tira primeiro?

## Exercícios

1. O que significa a sigla POST?
2. Quem faz o POST quando o computador liga?
3. Cite 3 componentes testados no POST.
4. Na maioria das placas, o que significa 1 bipe curto?
5. O computador dá bipes curtos repetidos. Qual peça provavelmente está com problema?
6. O computador não acende nenhuma luz e a ventoinha não gira. Cite 2 coisas para verificar primeiro.
7. A data e a hora do computador voltam sempre para 2010. Qual peça deve ser trocada?
8. O PC desliga sozinho depois de 20 minutos de uso. Qual a causa mais provável e o que deve ser verificado?
9. Aparece "No boot device" na tela. Qual componente deve ser testado?
10. Por que não se deve trocar várias peças ao mesmo tempo durante um diagnóstico?
11. Escreva, na ordem, os 5 passos do método de diagnóstico.
12. Por que é importante consultar o manual da placa-mãe ao ouvir os bipes?
13. **Desafio:** Um cliente diz: "Meu PC liga, faz barulho de ventoinha, dá 1 bipe longo e 3 curtos e a tela fica preta." Descreva o que você testaria e em que ordem.
