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

| Circle | Projeto | Fase A — sua stack (TypeScript/Node) | Fase B — nativo |
|---|---|---|---|
| 00 | `Libft` | Funções sobre `string`/`Array` | C, `malloc`/`free` |
| 01 | `get_next_line` | Buffer com `Buffer` do Node | C, buffer estático |
| 01 | `ft_printf` | Rest params / template strings | C, `va_list`/`va_arg` |
| 01 | `Born2beroot` | — (infraestrutura) | VM Linux hardened |
| 02 | `so_long` | TS + canvas simples | C + MiniLibX |
| 02 | `pipex` | `child_process` do Node | C, `fork`/`pipe`/`exec` |
| 02 | `push_swap` | Algoritmo em TypeScript | Port pra C |
| 03 | `Philosophers` | `async`/`worker_threads` (mesmo músculo do RNFT-E01) | C, `pthread`/`sem_t` |
| 03 | `minishell` | `child_process.spawn` simulando shell | C, `fork`/`execve`/`pipe`/`dup2` |
| 04 | `NetPractice` | — (infraestrutura) | Configuração de IP/rede |
| 04 | `miniRT` | TS + canvas (conecta com Geometria Analítica — ver [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md), Parte V) | C + MiniLibX |
| 04 | `CPP Module 00-08` (9 módulos) | — (OOP já dominado via TS) | C++, prática direta de sintaxe |
| 05 | `ft_containers` | — (não há o que "reimplementar" em TS, já que `Array`/`Map` já são a biblioteca padrão) | C++, reimplementar `vector`/`map`/`stack` — aqui o exercício É a linguagem, não porta de conceito já visto |
| 05 | `Inception` | — (Docker já dominado na Fase 6D; entra como auditoria de disciplina extra: só Debian, sem tag `latest`) | Mesmo, com a disciplina específica da 42 |
| 05 | `webserv` | Já feito na Fase 2.2 (`http`/`net` do Node) | C++, socket POSIX e `poll`/`epoll` |
| 05 | `ft_irc` | TS com `net.Server`, protocolo IRC | C++, socket POSIX |
| 06 | `ft_transcendence` | Nenhuma necessária — o AM Gestão já supera o que este projeto pede | NestJS — exercício comparativo contra sua própria arquitetura |

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
- [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md) — `miniRT` conecta com Geometria Analítica (Parte V); Algoritmo de Euclides (`Libft`) conecta com indução (Parte II)
- [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md) — onde C/C++ desta trilha se encaixa no panorama geral de tecnologia a estudar
- [sequencia-mestra-completa-desde-o-inicio](../99-arquivo/sequencia-mestra-completa-desde-o-inicio.md) — a ordem exata de intercalação com o portfólio próprio, Bloco a Bloco
- [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md) — roadmap.sh como auditoria cruzada específica pra C/C++ (roadmap "C" e "C++" no índice geral)


---

## Integração 42 + roadmap.sh (Akita)

### Aplicando a mesma régua de sempre: o que entra, entra no lugar certo — o resto fica de fora, com o motivo explícito

---

## Parte 1 — École 42: currículo real, mas em C/C++

### O que a 42 realmente é
Escola sem professor, aprendizado peer-to-peer, currículo em árvore de projetos. O Common Core confirmado (pesquisado agora, não de memória): `libft` (reimplementar função da biblioteca C padrão) → `born2beroot` (VM Linux hardened) → `ft_printf` → `get_next_line` → `push_swap`/`so_long`/`fract-ol` (algoritmo/gráfico) → `pipex`/`minitalk` (processo Unix) → `philosophers` (concorrência com mutex/semáforo) → `minishell` (shell próprio) → `cub3d`/`net_practice` → módulos de C++ → `webserv` (servidor HTTP do zero) → `ft_transcendence` (projeto final full stack).

### A honestidade que precisa vir primeiro
Adotar esse currículo inteiro significa **aprender C e C++ como trilha completa de sistemas**. Na nova realidade, C/C++ **entra sim** — mas pela trilha de **Sistema Operacional e Robótica** (ativa, leve), não pelo currículo inteiro da 42. Aplicando a régua de 3 perguntas (resolve problema real agora? existe forma mais simples? vai reaparecer ou é uso único?), a maior parte dos projetos da 42 **não passa** como estudo dedicado — o C/C++ que você precisa vem aplicado ao SO e aos protótipos, não em dezenas de exercícios isolados.

### O que entra — critério de valor real, baixo custo de linguagem nova

| Projeto 42 | Entra? | Por quê |
|---|---|---|
| **`born2beroot`** (VM Linux, SSH, hardening, política de senha) | ✅ Entra | Não exige C — é Linux/ops puro, e conecta direto com a Fase 6 (deploy) já existente. Fazer esse projeto de verdade antes do primeiro deploy real do AM Kaixara é preparo genuíno, não currículo por currículo |
| **`net_practice`** (configuração de rede/IP) | ✅ Entra | Mesma lógica — sem custo de linguagem nova, fortalece exatamente o tipo de conhecimento de infraestrutura que a Fase 6 e a Fase 12 (pentest) já exigem |
| **Conceito de `webserv`** (construir servidor HTTP do zero) | ⚠️ Entra, mas **não em C++** | O valor real é entender o que o Next.js/Node abstrai por baixo — dá pra fazer em TypeScript (um servidor HTTP mínimo usando só `http`/`net` do Node, sem framework), sem custo de linguagem nova |
| `libft`, `ft_printf`, `get_next_line`, `minishell`, `philosophers`, `cub3d`, módulos C++ | ❌ Não como exercício isolado | Concorrência, algoritmo e manipulação de string você já aprende dentro do próprio TS/Python; o C/C++ necessário vem aplicado na trilha de SO/robótica |

### Onde isso entra no plano
- `born2beroot`: antes do **Passo 10** (Produção real) do `passo-a-passo-mestre-desde-o-inicio` — fazer esse projeto como preparo direto pro primeiro deploy
- `net_practice`: mesma janela, complementar
- Servidor HTTP mínimo em TypeScript (`http`/`net` do Node): exercício de aprofundamento no **backend web** — construir o mínimo antes de usar o Next.js/NestJS completo, pra sentir o que ele resolve

---

## Parte 2 — roadmap.sh: checklist visual de lacuna, não currículo à parte

**Correção: você tinha razão em corrigir — não é Stack Overflow, é [roadmap.sh](https://roadmap.sh/roadmaps), um site diferente e mais adequado.** É um projeto open source (6º mais estrelado do GitHub) com roadmap visual, gratuito, por tecnologia/carreira — cada nó do mapa linka pra recurso curado. Confirmei a existência real e atual antes de integrar.

Diferente de currículo com progressão própria, o uso certo de roadmap.sh é como **auditoria cruzada** — verificar se o seu próprio plano já construído tem lacuna que o roadmap da comunidade aponta e você não tinha visto.

### Roadmaps diretamente relevantes ao seu plano, confirmados
| Roadmap | Link | Cruza com |
|---|---|---|
| Backend | [roadmap.sh/backend](https://roadmap.sh/backend) | Passos 3-8 (fundamento geral de backend) |
| Next.js / Node | [roadmap.sh/nodejs](https://roadmap.sh/nodejs) · [roadmap.sh/react](https://roadmap.sh/react) | Passos 3-5 — seu backend/front em TypeScript |
| Índice geral (todos os roadmaps: PostgreSQL, Docker, System Design, C, C++, Git/GitHub, SQL, DevOps, Kubernetes) | [roadmap.sh/roadmaps](https://roadmap.sh/roadmaps) | Praticamente todo o plano — use pra achar o roadmap certo de cada tecnologia específica na hora de cada Passo |

### Como usar sem virar mais uma trilha
No início de cada bloco grande (Passo 3, Passo 8, Passo 8B, Passo 10), abrir o roadmap correspondente e comparar 2 minutos contra o que já está no seu plano — se aparecer um nó que você nunca ouviu falar, essa é a lacuna real; se for tudo familiar, seguir sem desviar. Não é pra seguir o roadmap do zero, é conferência rápida contra o que você já construiu.

---

## Parte 3 — Fábio Akita: hábito de consumo contínuo, com trilha real por tema (correção: episódios específicos, não mais "1 vídeo por semana" genérico)

Canal chamado **"Akitando"**, blog **"AkitaOnRails"** (`akitaonrails.com`) — mesmo autor, conteúdo complementar (vídeo dá contexto, post costuma ter mais profundidade técnica e código).

### Playlist de início (fundamentos, sequência oficial dele)
`#36` a `#49`, mais `#54` e `#76` — playlist "Programação para Iniciantes" (começou com o nome "Começando aos 40"), cada vídeo tem post correspondente no blog.

### Trilhas temáticas, pra depois do início — episódio real, não estimativa
| Trilha | Episódios |
|---|---|
| Carreira/trajetória pessoal | `#61`, `#64`, `#83`, `#138` |
| Estrutura de Dados & Algoritmos | `#95`, `#118`, `#143`, `#144` |
| Infra/Redes/Homelab | `#98`, `#99`, `#126`, `#139`, `#146` |
| Segurança/Criptografia | `#67`, `#131`, `#147` |
| Linguagens & Comparações | `#136`, `#145` |
| IA aplicada (mais recente) | `#142`, `#148`, `#149` |

O canal tem 150+ episódios ao todo — esta lista é o recorte que cruza direto com o que você já estuda (não é o canal inteiro).

**Como encaixar sem virar mais uma trilha:** bloco fixo pequeno e recorrente, não meta de "terminar". Sugestão: 1 vídeo ou 1 post de blog por semana, no tempo de deslocamento ou pausa — mesmo princípio de "reaproveitar tempo que já existe" já usado com o inglês (ouvir em vez de ler, se for vídeo longo). Escolha a trilha temática por prioridade de fase (ex: Segurança/Criptografia quando chegar no `aura-vault` ou no Pentest, Infra/Redes quando chegar no `Born2beroot`/`NetPractice`).

**Por que vale, mesmo sem estrutura formal:** o conteúdo dele é majoritariamente sobre **contexto de carreira e indústria**, não sobre sintaxe de linguagem — complementa exatamente a lacuna de "entendimento de mercado" que apareceu antes (ex: quando expliquei as áreas de uma empresa grande). Não substitui nenhuma fase técnica, é pano de fundo cultural.

---

## Resumo — o que muda de verdade no plano

1. **Duas adições concretas de baixo custo:** `Born2beroot` e `NetPractice`, antes da Fase 6 (Produção)
2. **Um exercício adaptado, não importado:** servidor HTTP mínimo em TypeScript (Node), no backend web, em vez do `webserv` em C++
3. **roadmap.sh:** checklist de auditoria cruzada no início de cada bloco grande, não currículo próprio
4. **Fábio Akita:** consumo semanal leve, contínuo, sem fase nem critério de conclusão — cultura de indústria, não currículo técnico
5. **O resto do currículo da 42** (a maior parte, em C/C++ puro) fica de fora — não por falta de qualidade, mas porque o custo de abrir uma segunda linguagem de sistemas inteira não se paga dado o que você já tem pela frente

---

## 🔗 Documentos relacionados
