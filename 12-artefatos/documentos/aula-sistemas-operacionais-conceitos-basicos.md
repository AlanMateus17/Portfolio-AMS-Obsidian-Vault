# Aula — Sistemas Operacionais: Conceitos básicos

Oct 20, 2026 · @Alan Mateus

Os alunos saem sabendo o que é um sistema operacional, exemplos, as 4 funções principais, o que é kernel, os tipos de interface e o que é processo. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios). Todo o conteúdo necessário para os exercícios está nos blocos do quadro.

## Roteiro da aula

1. Pergunta de abertura (5 min): "Se você comprar um computador sem nenhum programa instalado, o que acontece quando ligar?"
2. Quadro + explicação (40 min): blocos A a F abaixo, nessa ordem.
3. Demonstração rápida, se houver projetor: abrir o Gerenciador de Tarefas e mostrar os processos (5 min).
4. Exercícios no caderno (aula seguinte ou restante do tempo).

## O que escrever no quadro

**Bloco A — O que é sistema operacional (SO)**

- Sistema operacional = programa principal do computador, que controla o hardware.
- Ele faz a ponte entre o usuário, os aplicativos e o hardware.
- É o primeiro programa a carregar quando o computador liga.
- Sem sistema operacional, o computador liga, mas não dá para usar.

Desenhe 4 caixas empilhadas, de cima para baixo: **Usuário → Aplicativos → Sistema Operacional → Hardware**.

**Bloco B — Exemplos de sistemas operacionais**

| Onde é usado | Exemplos |
| --- | --- |
| Computadores | Windows, Linux (Ubuntu, Mint), macOS |
| Celulares | Android, iOS |

- **Software livre:** Linux (gratuito e com código aberto).
- **Proprietário:** Windows, macOS e iOS (código fechado, pertencem a uma empresa).

**Bloco C — As 4 funções principais do SO**

| Função | O que faz | Exemplo |
| --- | --- | --- |
| Gerência de processos | Controla os programas em execução | Ouvir música enquanto digita |
| Gerência de memória | Divide a memória RAM entre os programas | Cada aba do navegador usa um pouco de RAM |
| Gerência de arquivos | Organiza arquivos e pastas no disco | Criar, copiar, apagar arquivos |
| Gerência de dispositivos | Controla teclado, mouse, impressora, etc. | Reconhecer um pendrive conectado |

**Bloco D — Kernel e interface**

- **Kernel (núcleo)** = parte central do SO. É ele que conversa diretamente com o hardware.
- **Interface** = a parte que o usuário vê e usa.
- **GUI (interface gráfica)** = usa janelas, ícones e mouse. Ex.: Área de Trabalho do Windows.
- **CLI (linha de comando)** = o usuário digita comandos. Ex.: Prompt de Comando (Windows) e Terminal (Linux).

**Bloco E — Processos e multitarefa**

- **Programa** = arquivo guardado no disco, parado.
- **Processo** = programa em execução (aberto e funcionando).
- Se abrir o mesmo programa 2 vezes, são 2 processos.
- **Multitarefa** = o SO executa vários processos ao mesmo tempo, alternando entre eles muito rápido.
- Ver os processos: **Gerenciador de Tarefas** no Windows (Ctrl + Shift + Esc) e comando **top** no Linux.

**Bloco F — Analogias, erros comuns e pergunta para a turma**

- Analogia do maestro: o SO é o maestro da orquestra. Cada músico (hardware e aplicativos) toca sua parte, e o maestro organiza tudo para dar certo junto.
- Erro 1: achar que o Google Chrome ou o Word são sistemas operacionais → são aplicativos que rodam em cima do SO.
- Erro 2: confundir programa com processo → programa está parado no disco; processo está em execução.
- Erro 3: achar que Linux é só para programador → o Android, usado em milhões de celulares, é baseado em Linux.
- Pergunta: estou ouvindo música, com o navegador aberto e digitando no Word. Quantos processos estão rodando no mínimo?

## Exercícios

1. O que é um sistema operacional?
2. O que acontece se o computador não tiver sistema operacional?
3. Escreva, de cima para baixo, as 4 camadas do desenho do quadro.
4. Cite 2 sistemas operacionais de computador e 2 de celular.
5. Qual sistema operacional é software livre? Cite 2 que são proprietários.
6. Cite as 4 funções principais do sistema operacional.
7. Qual função do SO é responsável por reconhecer um pendrive conectado?
8. Qual função do SO divide a memória RAM entre os programas?
9. O que é o kernel?
10. Qual a diferença entre GUI e CLI? Dê um exemplo de cada.
11. Qual a diferença entre programa e processo?
12. O que é multitarefa?
13. Como ver os processos em execução no Windows? E no Linux?
14. O Google Chrome é um sistema operacional? Justifique.
15. **Desafio:** Usando a analogia do maestro, explique o papel do sistema operacional e dê um exemplo de multitarefa do seu dia a dia.
