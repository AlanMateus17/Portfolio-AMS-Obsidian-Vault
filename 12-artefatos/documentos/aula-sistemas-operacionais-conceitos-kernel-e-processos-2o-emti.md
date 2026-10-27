# Aula — Sistemas Operacionais: Conceitos, kernel e processos

Oct 21, 2026 · @Alan Mateus

Aula de revisão e aprofundamento: retoma a apostila 01, junta com o material do kernel e o texto da prova, e prepara a turma para a avaliação. Os termos e números seguem as suas apostilas (5 funções do SO, Android como código aberto, htop no Linux). Duração sugerida: 3 aulas de 50 min (Blocos A–D, Blocos E–G e exercícios). Tudo o que os exercícios cobram está escrito no quadro.

## Alinhamento

| Item da ementa | Material que você já tem | Bloco desta aula |
| --- | --- | --- |
| Introdução a Sistemas Operacionais | Apostila 01 | A, B e C |
| Introdução a SO (arquitetura) | Texto do kernel e questionário do kernel | D |
| Área de trabalho, ferramentas e aplicativos | Apostila 04 | E |
| Gerenciamento do SO e monitoramento | Apostilas 03 e 13 | F |
| Revisão para a prova | Texto da prova de SO | Todos |

Projeto BSD: não faz parte. O Projeto Integrador é do 3º ano (Lab. Hardware + Lab. Software).

## Roteiro da aula

1. Pergunta de abertura (5 min): "Se você comprar um computador sem nenhum programa instalado, o que acontece quando ligar?"
2. Aula 1 — Blocos A a D no quadro (45 min).
3. Aula 2 — Blocos E a G no quadro (45 min). Se houver projetor, abra o Gerenciador de Tarefas e mostre os processos.
4. Aula 3 — Exercícios no caderno.

## O que escrever no quadro

**Bloco A — O que é sistema operacional (apostila 01)**

- Sistema operacional (SO) = software que gerencia os recursos do computador e serve de ponte entre o hardware e os programas do usuário.
- Sem o SO, nenhum programa consegue se comunicar com o hardware.
- **Abstração de hardware** = o SO esconde a complexidade dos circuitos e entrega funções simples para o usuário e os aplicativos.
- Sem o SO haveria uma "anarquia computacional": cada programa brigaria pelo controle da CPU, da memória e dos periféricos.

Desenhe 4 caixas empilhadas, de cima para baixo: **Usuário → Aplicativos → Sistema Operacional → Hardware**.

**Bloco B — Tipos de sistemas operacionais (apostila 01)**

| SO | Tipo | Uso principal |
| --- | --- | --- |
| Windows 10/11 | Proprietário (Microsoft) | PCs domésticos e empresas |
| Linux (Ubuntu, Debian) | Código aberto (gratuito) | Servidores, educação, desenvolvedores |
| macOS | Proprietário (Apple) | Computadores Mac |
| Android | Código aberto (Google) | Celulares e tablets |
| iOS | Proprietário (Apple) | iPhone e iPad |

- Código aberto = qualquer pessoa pode ver e estudar o código.
- Proprietário = o código é fechado e pertence a uma empresa.
- O Android é baseado no Linux.

**Bloco C — As 5 funções do SO (apostila 01)**

| Função | O que faz | Exemplo |
| --- | --- | --- |
| Gerenciar processos | Controla quais programas usam a CPU | Spotify tocando enquanto você digita |
| Gerenciar memória | Distribui a RAM entre os programas | Chrome + Word + Spotify juntos |
| Gerenciar armazenamento | Organiza arquivos e pastas no disco | Salvar um arquivo em Documentos |
| Gerenciar dispositivos | Controla o hardware por meio dos drivers | Pendrive, impressora, teclado |
| Interface com o usuário | Permite a interação com o computador | Área de trabalho, janelas, menus |

- Na memória, o SO separa um espaço para cada programa. Assim, um programa não corrompe os dados do outro.

**Bloco D — Kernel: o núcleo do SO (texto do kernel)**

- Kernel (núcleo) = o programa mais importante do SO. É o primeiro a carregar quando o PC liga e o último a desligar.
- Função: gerenciar os recursos do hardware e garantir a segurança.

| Modo | Quem roda | O que acontece se travar |
| --- | --- | --- |
| Modo Usuário | Aplicativos (privilégio limitado) | Só o programa fecha |
| Modo Kernel | O kernel (acesso total ao hardware) | O PC inteiro trava: tela azul (Windows) ou kernel panic (Linux) |

- **System Call** (chamada de sistema) = o pedido que o aplicativo faz ao kernel para usar o hardware (ex.: ler um arquivo do disco).

**Bloco E — Interface e drivers (apostila 04 e texto da prova)**

- **GUI (interface gráfica)** = janelas, ícones e mouse. Ex.: Área de Trabalho do Windows, GNOME no Ubuntu.
- **CLI (linha de comando)** = o usuário digita comandos. Ex.: cmd e PowerShell (Windows), Terminal/bash (Linux).
- **Driver** = programa que faz o SO conversar com um dispositivo. Funciona como um tradutor entre o SO e a peça.

**Bloco F — Processos, multitarefa e monitoramento (apostila 13 e texto da prova)**

- **Programa** = arquivo parado no disco.
- **Processo** = programa em execução. Abrir o mesmo programa 2 vezes = 2 processos.
- **Escalonamento** = o SO organiza e prioriza qual processo usa a CPU.
- **Multitarefa** = a CPU alterna entre os processos tão rápido que parece que tudo roda ao mesmo tempo.
- Ver os processos e o uso de CPU e RAM: **Gerenciador de Tarefas (Ctrl + Shift + Esc)** no Windows e **htop** no Linux.

**Bloco G — Analogias, erros comuns e pergunta para a turma**

- Analogia do maestro: o SO é o maestro; cada músico (hardware e aplicativos) toca sua parte, e o maestro organiza para tudo dar certo junto.
- Analogia do banco blindado: o aplicativo não entra no cofre (hardware); ele faz o pedido no balcão (System Call) e o kernel busca para ele.
- Erro 1: achar que o Chrome ou o Word são sistemas operacionais → são aplicativos que rodam sobre o SO.
- Erro 2: confundir programa com processo → programa está parado; processo está em execução.
- Erro 3: esquecer a interface com o usuário → são 5 funções, não 4.
- Erro 4: achar que só o Linux é código aberto → o Android também é.
- Pergunta: um aplicativo trava no Modo Usuário. O computador inteiro trava?

## Exercícios

1. O que é um sistema operacional?
2. O que é abstração de hardware?
3. O que seria a "anarquia computacional" sem o SO?
4. Escreva, de cima para baixo, as 4 camadas do desenho do quadro.
5. Quais SOs da tabela são de código aberto? Quais são proprietários?
6. Qual a diferença entre código aberto e proprietário?
7. Escreva as 5 funções do SO.
8. Para cada situação, diga a função do SO: (a) conectar um pendrive, (b) abrir 3 programas juntos, (c) salvar um arquivo em Documentos.
9. Por que o SO separa um espaço da memória para cada programa?
10. O que é o kernel? Quando ele carrega e quando desliga?
11. Qual a diferença entre Modo Usuário e Modo Kernel?
12. O que é uma System Call? Explique usando a analogia do banco blindado.
13. Qual a diferença entre GUI e CLI? Dê um exemplo de cada.
14. O que é um driver?
15. Qual a diferença entre programa e processo?
16. O que é escalonamento? E multitarefa?
17. Como ver os processos no Windows? E no Linux?
18. **Desafio:** O computador mostrou a tela azul. Usando os Blocos D e E, explique em qual modo o erro aconteceu e por que o sistema inteiro parou, e não só um programa.
