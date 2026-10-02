---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Trilha 42 — Estrutura Oficial Verificada (25 entregáveis + 5 Exam Rank)
### Substitui a versão anterior de "29 entregáveis" — corrigida contra fonte real (repositório de ex-aluno, cruzado com 4 fontes independentes)

---

## O que mudou, e por quê

A versão anterior (`trilha-42-circles-oficial-verificado`) tinha 3 erros reais:
1. **Faltava `ft_containers`** (reimplementação de container da STL em C++) — projeto real do Circle 05, esquecido por completo
2. **Módulos C++ contados errado** — são 00 a 08 (9 módulos), não 00 a 09 (10)
3. **`fract-ol`, `fdf`, `minitalk`, `cub3d` tratados como "escolha 1 de 2"** quando na estrutura oficial verificada eles **não aparecem** — são variação de campus específico (algumas unidades da 42 têm currículo local levemente diferente), não fazem parte do Common Core universal. Os projetos de cada Circle são **todos obrigatórios juntos**, não pares de escolha.

**Fonte:** `github.com/LeonMoreno/00_42cursus`, cruzada com mais 4 repositórios de ex-alunos de campus diferentes (Seul, Barcelona) — a estrutura de Circle 00-06 abaixo é a que se repete de forma consistente entre eles.

---

## Estrutura oficial por Circle (🔑 = gate, só avança depois de completar)

### Circle 00
**`Libft`** (C) — reimplementar função da libc.

🔑

### Circle 01
**`get_next_line`** (C) · **`ft_printf`** (C) · **`Born2beroot`** (SysAdmin/NetAdmin)

🔑

### Circle 02
**Exam Rank 02** (avaliação, não projeto) · **`so_long`** (C, gráficos) · **`pipex`** (C) · **`push_swap`** (C)

🔑

### Circle 03
**Exam Rank 03** · **`Philosophers`** (C, concorrência) · **`minishell`** (C, Bash)

🔑

### Circle 04
**`NetPractice`** (redes) · **`miniRT`** (C, ray tracing) · **`CPP Module 00` a `08`** (C++, progressivo — 9 módulos) · **Exam Rank 04**

🔑

### Circle 05
**`ft_containers`** (C++, reimplementação de container da STL — `vector`, `map`, `stack`) · **`Inception`** (Docker) · **`webserv`** (C++, servidor HTTP) · **`ft_irc`** (C++, servidor IRC) · **Exam Rank 05**

🔑

### Circle 06 (fim do Common Core)
**`ft_transcendence`** (**JavaScript** — único projeto do Common Core que sai de C/C++, tipicamente NestJS/React/PostgreSQL) · **Exam Rank 06**

🔑 fim do Common Core, libera estágio e Outer Core (especialização eletiva)

---

## Tabela completa — Sua Stack primeiro (Fase A) → Nativo depois (Fase B)

| Circle | Projeto | Fase A — sua stack (C#) | Fase B — nativo |
|---|---|---|---|
| 00 | `Libft` | Método estático sobre `char[]` | C, `malloc`/`free` |
| 01 | `get_next_line` | Buffer mantido em C# | C, buffer estático |
| 01 | `ft_printf` | `params object[]` | C, `va_list`/`va_arg` |
| 01 | `Born2beroot` | — (infraestrutura) | VM Linux hardened |
| 02 | `so_long` | C# + biblioteca gráfica simples | C + MiniLibX |
| 02 | `pipex` | `System.Diagnostics.Process` | C, `fork`/`pipe`/`exec` |
| 02 | `push_swap` | Algoritmo em C# | Port pra C |
| 03 | `Philosophers` | `Thread`/`SemaphoreSlim` (mesmo músculo do RNFT-E01) | C, `pthread`/`sem_t` |
| 03 | `minishell` | `Process.Start` simulando shell | C, `fork`/`execve`/`pipe`/`dup2` |
| 04 | `NetPractice` | — (infraestrutura) | Configuração de IP/rede |
| 04 | `miniRT` | C# + SkiaSharp (conecta com Geometria Analítica — ver [[matematica-e-desenvolvimento-integrado]], Parte V) | C + MiniLibX |
| 04 | `CPP Module 00-08` (9 módulos) | — (OOP já dominado via C#) | C++, prática direta de sintaxe |
| 05 | `ft_containers` | — (STL não tem equivalente direto de "reimplementar" em C#, já que `List<T>`/`Dictionary<K,V>` já são a biblioteca padrão) | C++, reimplementar `vector`/`map`/`stack` — aqui o exercício É a linguagem, não porta de conceito já visto |
| 05 | `Inception` | — (Docker já dominado na Fase 6D; entra como auditoria de disciplina extra: só Debian, sem tag `latest`) | Mesmo, com a disciplina específica da 42 |
| 05 | `webserv` | Já feito na Fase 2.2 (`TcpListener`) | C++, socket POSIX e `poll`/`epoll` |
| 05 | `ft_irc` | C# com `TcpListener`, protocolo IRC | C++, socket POSIX |
| 06 | `ft_transcendence` | Nenhuma necessária — o AM Kaixara já supera o que este projeto pede | JavaScript/NestJS — fazer como exercício comparativo contra sua própria arquitetura |

**Total: 25 entregáveis + 5 Exam Rank (avaliação de gate, não projeto de estudo — mas real, cronometrado, sem consulta).**

---

## Por que a ordem C→C++ já está resolvida, sem precisar escolher entre duas lógicas

A estrutura oficial **já é** C puro do Circle 00 ao 03, C++ começando a se misturar no Circle 04 (junto com `miniRT`, ainda C), e C++ puro só a partir do Circle 05. Isso bate com a recomendação de "C antes de C++ por motivo de segurança ofensiva" identificada na conversa sobre Akita — as duas lógicas convergem pro mesmo resultado, não são conflitantes.

---

## Cronograma revisado

| Circle | Entregáveis | Duração estimada |
|---|---|---|
| 00-01 (fundamento) | 4 | 5-7 semanas |
| 02 (algoritmo/gráfico/processo) | 3 | 6-8 semanas |
| 03 (concorrência/shell) | 2 | 6-8 semanas — o mais denso |
| 04 (rede, ray tracing, C++ início) | 11 (2 + 9 módulos) | 10-12 semanas |
| 05 (C++ avançado, container, servidor) | 4 | 8-10 semanas |
| 06 (projeto final) | 1 | 4-6 semanas |
| **Total** | **25** | **~9-11 meses** |

Praticamente igual ao cronograma anterior (10-12 meses), só que agora contando o trabalho certo.

---

## 🔗 Documentos relacionados
- [[matematica-e-desenvolvimento-integrado]] — `miniRT` conecta com Geometria Analítica (Parte V); Algoritmo de Euclides (`Libft`) conecta com indução (Parte II)
- [[stack-tecnologica]] — onde C/C++ desta trilha se encaixa no panorama geral de tecnologia a estudar
- [[sequencia-mestra-completa-desde-o-inicio]] — a ordem exata de intercalação com o portfólio próprio, Bloco a Bloco
- [[integracao-42-roadmap-akita]] — roadmap.sh como auditoria cruzada específica pra C/C++ (roadmap "C" e "C++" no índice geral)
