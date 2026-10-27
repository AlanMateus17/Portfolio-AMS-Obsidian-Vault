# Aula — Laboratório de Hardware: Segurança, medição e diagnóstico na máquina do Projeto BSD

Oct 21, 2026 · @Alan Mateus

Aula de aplicação: os alunos usam o que viram nas apostilas de Laboratório de Hardware para preparar, medir e diagnosticar a máquina de validação do Projeto Integrador (Casa de Apostas Provably Fair sobre a rede BSD). O conteúdo adicional de POST e bipes continua, agora junto com o boot mínimo e as 7 etapas da apostila 19. Duração sugerida: 3 aulas de 50 min (Blocos A–C, Blocos D–G e exercícios). Tudo o que os exercícios cobram está escrito no quadro.

## Alinhamento

| Item da ementa | Apostila | Onde entra no projeto |
| --- | --- | --- |
| Procedimentos de laboratório e normas de segurança | 01 | Checklist de bancada antes do teste de estresse |
| Aterramento e ESD | 02 e 03 | Pulseira e manta ligadas ao aterramento |
| Equipamentos de medição | 07, 08 e 15 | Medir a fonte e o consumo em repouso e sob carga |
| Normas de reparo e manutenção | 13, 14 e 19 | Manutenção preventiva e diagnóstico da máquina sob carga |
| Instalação de drives e drivers | 11 | Driver de vídeo para o processamento de hash |
| Adicional | 14 e 16 | POST e códigos de bipe |

## Roteiro da aula

1. Pergunta de abertura (5 min): "A máquina que valida a rede BSD vai rodar no limite por horas. O que pode dar errado com ela?"
2. Aula 1 — Blocos A a C no quadro (45 min). Se houver bancada, demonstre a pulseira e a medição com o multímetro.
3. Aula 2 — Blocos D a G no quadro (45 min).
4. Aula 3 — Exercícios no caderno.

## O que escrever no quadro

**Bloco A — Checklist de bancada segura (apostilas 01 e 03)**

Antes de abrir ou testar a máquina, nesta ordem:

1. Desligar e tirar da tomada. NR-12: máquina parada, desenergizada e bloqueada durante a manutenção.
2. Tirar anéis, relógios e correntes (risco de choque e curto-circuito).
3. Colocar a pulseira antiestática e usar a manta, as duas ligadas ao aterramento.
4. Usar ferramentas com isolamento.
5. Separar os parafusos em um recipiente.
6. Bancada limpa, seca e sem poeira.

- NR-10 = norma de segurança em eletricidade: prioridade é a prevenção.
- A pulseira iguala a carga elétrica do corpo com a do equipamento.
- Uma descarga de 10 V já pode danificar um chip. O ser humano só sente acima de 3.000 V.

**Bloco B — Medindo a fonte com o multímetro (apostilas 07 e 15)**

- Tensão contínua (fonte do PC): escala V⎓ ou VDC.
- Tensão alternada (tomada): escala V\~ ou VAC. Só com treinamento.
- Ponta preta no fio preto (GND = 0 V) e ponta vermelha no fio que será medido.

| Cor do fio | Tensão esperada |
| --- | --- |
| Amarelo | +12 V |
| Vermelho | +5 V |
| Laranja | +3,3 V |
| Preto | 0 V (GND) |

- Pontas de prova finas e isoladas; mão firme para não encostar em dois pinos ao mesmo tempo.

**Bloco C — Consumo da máquina: repouso e estresse (apostila 08)**

- Potência: **P = V × I** (watts = volts × ampères). Ex.: 12 V × 10 A = 120 W.
- O consumo total é medido com um wattímetro de tomada.
- Medir duas vezes: em repouso e durante o teste de estresse. Anotar em docs/HARDWARE\_SETUP.md.
- A fonte precisa suportar o consumo sob estresse + 20% de margem. Ex.: 300 W × 1,2 = 360 W.
- Sem wattímetro ou multímetro: fazer o POP (impedimento, passo a passo e justificativa).

**Bloco D — POST e códigos de bipe (conteúdo adicional, apostilas 14 e 16)**

- POST = Power-On Self Test (autoteste ao ligar), feito pela BIOS/UEFI.
- Testa processador, memória RAM, placa de vídeo e teclado.
- Passou → 1 bipe curto (na maioria das placas). Falhou → sequência de bipes ou LED de erro.

| Sinal ao ligar | Provável problema |
| --- | --- |
| 1 bipe curto | Tudo OK |
| Nada liga (sem luz e sem ventoinha) | Fonte, cabo ou tomada |
| Bipes curtos repetidos | Memória RAM |
| 1 longo + 2 ou 3 curtos | Placa de vídeo |

- Os códigos mudam por fabricante: sempre confira o manual da placa-mãe.

**Bloco E — Diagnóstico profissional em 7 etapas (apostilas 14 e 19)**

1. Entrevista: quando começou, o que mudou, qual o sintoma.
2. Verificação visual: poeira, cabos soltos, capacitores estourados.
3. Boot mínimo: só placa-mãe + CPU + 1 pente de RAM.
4. Testar componentes: adicionar um por vez até o problema voltar. O último adicionado é o suspeito.
5. Ferramentas de software: CrystalDiskInfo (disco), HWMonitor (temperatura e tensões), Memtest86 (RAM).
6. Confirmar e reparar: trocar a peça e testar de novo.
7. Documentar: problema, causa e solução.

**Bloco F — Manutenção sob carga e driver de vídeo (apostilas 13 e 15)**

- Poeira funciona como isolante térmico → temperatura sobe e o desempenho cai (thermal throttling).
- Acompanhar a temperatura com o HWMonitor durante o teste de estresse.
- Pasta térmica: reaplicar a cada 2 a 3 anos ou quando a temperatura subir sem motivo.
- Desliga sozinho depois de um tempo → suspeitar de superaquecimento ou de fonte sem potência.
- Driver = programa que faz o sistema conversar com a peça. Para a placa de vídeo processar hash, instalar o driver do site do fabricante.

**Bloco G — Analogias, erros comuns e pergunta para a turma**

- POST = check-up do PC. Bipes = o PC "dizendo onde dói".
- Boot mínimo = tirar tudo e ir devolvendo peça por peça até achar o culpado.
- Erro 1: abrir a máquina ligada na tomada → risco de choque.
- Erro 2: trabalhar sem pulseira → a descarga pode queimar a peça sem ninguém sentir.
- Erro 3: trocar várias peças de uma vez → não dá para saber qual era o defeito.
- Erro 4: medir só em repouso → a máquina do projeto trabalha sob carga, e é aí que a fonte e o cooler são exigidos.
- Pergunta: a máquina dá bipes curtos repetidos. Em qual etapa do diagnóstico você tira os pentes de RAM?

## Exercícios

1. Escreva, na ordem, os 6 passos do checklist de bancada segura.
2. O que a NR-12 exige durante a manutenção? E qual a prioridade da NR-10?
3. Por que é proibido usar anéis e relógios na bancada?
4. Qual a função da pulseira antiestática? Onde ela deve estar ligada?
5. Uma descarga de quantos volts já pode danificar um chip? A partir de quantos volts o ser humano sente?
6. Qual escala do multímetro você usa para medir a fonte do PC?
7. Qual a tensão esperada nos fios amarelo, vermelho, laranja e preto?
8. Calcule a potência: 12 V e 8 A.
9. A máquina consome 250 W sob estresse. Qual a potência mínima da fonte com 20% de margem?
10. Por que o consumo deve ser medido em repouso e também sob estresse?
11. O que significa POST e quem o realiza?
12. O que indicam bipes curtos repetidos? E 1 bipe longo + 3 curtos?
13. Por que é preciso consultar o manual da placa-mãe ao ouvir os bipes?
14. Escreva as 7 etapas do diagnóstico profissional.
15. O que é boot mínimo? Quais peças ficam conectadas?
16. Por que a poeira causa superaquecimento? O que é thermal throttling?
17. Para que serve o driver de vídeo no projeto e de onde ele deve ser baixado?
18. **Desafio:** Durante o teste de estresse, a máquina de validação desliga sozinha depois de 20 minutos. Usando as 7 etapas e os Blocos C e F, descreva o que você verificaria e em que ordem.

## Conteúdo complementar — itens da ementa que faltavam

Estes blocos completam a ementa de Laboratório de Hardware e seguem as apostilas 02, 04, 11 e 12. Sugestão: mais 1 aula de 50 min. Tudo o que a avaliação cobra está nestes blocos ou nos Blocos A a G.

**Bloco H — Aterramento (apostilas 02 e 03)**

- Aterramento = ligação do equipamento à terra por um fio, o fio terra.
- Função: levar para a terra a corrente que "escapa" (corrente de fuga) e a eletricidade estática.
- Tomada do padrão brasileiro: 3 pinos = **fase, neutro e terra**. O terra é o **pino do meio**.
- Sem aterramento: risco de choque ao tocar o gabinete e mais danos por ESD.
- Na bancada: a pulseira e a manta antiestática só funcionam ligadas ao terra.
- Nunca ligar o fio terra no neutro ("gambiarra"): o equipamento fica sem proteção.
- Conferência (feita pelo professor ou por eletricista): entre neutro e terra, o multímetro em VAC deve marcar perto de 0 V (até cerca de 5 V).

**Bloco I — Componentes e montagem profissional (apostilas 04 e 12)**

| Componente | Onde fica |
| --- | --- |
| CPU | Centro da placa-mãe, sob o cooler |
| RAM | Slots paralelos na placa-mãe |
| SSD M.2 | Slot horizontal na placa-mãe |
| GPU | Slot PCIe da placa-mãe |
| HD/SSD SATA | Baia de drives do gabinete |
| Fonte | Parte superior ou inferior do gabinete |

Sequência de montagem (de fora para dentro do gabinete):

1. Instalar a CPU na placa-mãe, fora do gabinete.
2. Aplicar pasta térmica e instalar o cooler.
3. Instalar a RAM.
4. Instalar o SSD M.2.
5. Colocar o backplate e os espaçadores (standoffs) no gabinete.
6. Fixar a placa-mãe.
7. Instalar a fonte.
8. Instalar HD/SSD SATA.
9. Conectar os cabos.
10. Instalar a GPU (último componente grande).
11. Testar antes de fechar o gabinete.

- Espaçadores (standoffs): sem eles a placa-mãe encosta no metal do gabinete e causa curto-circuito.
- Desmontagem: o caminho inverso, sempre com a máquina desligada da tomada e os parafusos separados.

**Bloco J — Instalação de drives: HD e SSD (apostila 11)**

| Tipo | Instalação | Velocidade |
| --- | --- | --- |
| HD 3,5" | Baia + cabo SATA de dados + cabo de energia SATA | 100–150 MB/s |
| SSD 2,5" SATA | Baia + cabo SATA de dados + cabo de energia SATA | \~500 MB/s |
| SSD M.2 SATA | Direto no slot M.2, sem cabo | \~500 MB/s |
| SSD M.2 NVMe | Direto no slot M.2, sem cabo | 3.000–7.000 MB/s |

- HD SATA: fixar na baia com parafusos, ligar o cabo de dados (conector em L) e o cabo de energia SATA de 15 pinos.
- SSD M.2: inserir no slot em ângulo de cerca de 30°, pressionar e fixar com o parafuso.
- O número 2280 = 22 mm de largura e 80 mm de comprimento.
- **Drive** = peça de armazenamento (HD, SSD). **Driver** = programa que faz o SO conversar com a peça (Bloco F).
- No projeto: SSD NVMe na máquina de validação, para o banco e o sistema responderem rápido.

**Bloco K — Erros comuns dos blocos complementares**

- Erro 1: confundir drive com driver → drive é peça; driver é programa.
- Erro 2: montar sem espaçadores → curto-circuito na placa-mãe.
- Erro 3: instalar a GPU antes de fixar a placa-mãe → a ordem certa deixa a GPU por último.
- Erro 4: usar pulseira sem ligação ao terra → ela não protege contra ESD.
- Pergunta: em qual pino da tomada de 3 pinos fica o terra?

## Avaliação — Laboratório de Hardware

Nome: ..................................................   Turma: ..............   Data: ...... / ...... / ............

Marque apenas uma alternativa em cada questão.

1. Qual é o primeiro passo antes de abrir a máquina? a) Desligar e tirar da tomada b) Aplicar pasta térmica c) Ligar o multímetro d) Instalar o driver de vídeo
2. Qual é a função da pulseira antiestática? a) Aumentar a carga elétrica do corpo b) Medir a tensão da fonte c) Igualar a carga elétrica do corpo com a do equipamento d) Segurar os parafusos
3. Na tomada de 3 pinos do padrão brasileiro, o pino do meio é: a) A fase b) O terra c) O neutro d) Um pino sem função
4. Qual tensão o fio amarelo da fonte deve ter? a) 0 V b) +3,3 V c) +5 V d) +12 V
5. Qual escala do multímetro é usada para medir a fonte do PC? a) VAC b) Ω (resistência) c) VDC d) Continuidade
6. A máquina consome 250 W sob estresse. Qual é a potência mínima da fonte com 20% de margem? a) 300 W b) 270 W c) 250 W d) 200 W
7. Bipes curtos repetidos ao ligar indicam problema em qual peça? a) Fonte b) Teclado c) Placa de vídeo d) Memória RAM
8. Quais peças ficam ligadas no boot mínimo? a) Todas as peças do computador b) Placa-mãe, CPU e 1 pente de RAM c) Só a fonte d) Placa de vídeo e HD
9. O que a poeira acumulada causa no computador? a) Aumento da velocidade b) Superaquecimento e thermal throttling c) Mais memória disponível d) Bipes ao ligar
10. Para que servem os espaçadores (standoffs)? a) Prender o cooler na CPU b) Ligar a fonte na tomada c) Conectar o HD na placa-mãe d) Evitar que a placa-mãe encoste no metal do gabinete e cause curto
11. Qual tipo de armazenamento é o mais rápido? a) SSD M.2 NVMe b) HD 3,5" c) SSD 2,5" SATA d) SSD M.2 SATA
12. Qual é o primeiro passo da montagem profissional? a) Instalar a placa de vídeo b) Fixar a placa-mãe no gabinete c) Instalar a CPU na placa-mãe, fora do gabinete d) Fechar o gabinete

**Questão Extra** — O que significa o número 2280 em um SSD M.2?

- a) A velocidade em MB/s
- b) 22 mm de largura e 80 mm de comprimento
- c) A capacidade em GB
- d) O ano de fabricação

**Desafio** — Você vai montar do zero a máquina de validação do projeto BSD e deixá-la pronta para o teste de estresse. Usando os Blocos A, C, H e I, descreva em ordem: o que conferir na bancada, a sequência de montagem e as medições que você faria depois.

...........................................................................................................................

...........................................................................................................................

...........................................................................................................................

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
