---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Sequência Mestra Completa — Desde o Início
### Fundação + Portfólio próprio + 42 em C/C++ + 42 na sua Stack + Matemática + Física + Idiomas, tudo numa ordem só

> ℹ️ **Para o dia a dia, use [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]]** — este documento continua aqui como referência de detalhe, mas não precisa mais ser aberto pra saber "o que vem agora".


> Este documento intercala a Trilha 42 bloco a bloco dentro da numeração — é a referência pra ver exatamente onde cada projeto da 42 entra em relação ao portfólio. Pra uso diário, veja [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]].

---

## Como este documento resolve o que você pediu

Você pediu 5 coisas específicas — cada uma tem uma coluna própria na tabela principal, pra você conferir que nada ficou de fora:
1. Projeto da 42 na tecnologia nativa (C/C++)
2. O mesmo projeto repetido na sua stack (C#/.NET)
3. Conexão com o desenvolvimento dos seus próprios sistemas (AM Kaixara, AM Rotara, etc.)
4. Matemática básica (livro já comprado)
5. Física básica (livro ainda a comprar) — entra com estrutura provisória, corrigida assim que você tiver o sumário real, do mesmo jeito que já fizemos com matemática

---

## FUNDAÇÃO (Blocos 1-8) — antes de qualquer coisa começar a se ramificar

| Bloco | Portfólio próprio | Matemática | Física | Idioma |
|---|---|---|---|---|
| 1 | Lógica de programação | Parte I (Lógica, Conjuntos) | — | Inglês Fase A (nivelamento) |
| 2 | Git, SQL, Docker | Parte II início (Naturais/Inteiros) | — | continua |
| 3 | C# Fundamentals | Parte II (Aritmética Modular/RSA) | — | continua |
| 4 | API + Autenticação | continua | — | Inglês Fase B (fonte técnica em inglês) |
| 5 | EF Core + CRUD molde | Parte II fim (Racionais, Aplicações Aritméticas, Sequências, Reais) | — | continua |
| 6 | Teste (backend + frontend) | — | — | continua |
| 7 | Frontend completo (11 etapas já detalhadas) | — | — | continua |
| 8 | Arquitetura (SOLID, Clean Architecture) | — | — | continua |

**Física entra a partir daqui, em paralelo, começando pelo fundamento** (Etapa 0 típica de física básica: grandeza, unidade, notação científica, cinemática introdutória) — mas o conteúdo exato só fica definitivo quando você comprar o livro e eu vir o sumário real, exatamente como aconteceu com matemática. Até lá, trate como "reserve o mesmo tipo de bloco de tempo pequeno que a matemática usou no início".

---

## A PARTIR DO BLOCO 9 — Portfólio e Trilha 42 alternando, cada projeto 42 com os dois pares (C/C++ e sua stack)

### Bloco 9 — Portfólio: AM Rotara, Bloco 1 (pedido + geolocalização)
PostGIS, Redis, SignalR. Ver `passo-a-passo-mestre`, Passo 9.

### Bloco 10 — 42: Fundamento (libft, born2beroot, ft_printf, get_next_line)
| Projeto | Sua stack (C#) primeiro | Nativo (C) depois |
|---|---|---|
| `libft` | Método estático sobre `char[]` | `malloc`/`free`, ponteiro real |
| `born2beroot` | — (infraestrutura, sem par) | VM Linux hardened |
| `ft_printf` | `params object[]` | `va_list`/`va_arg` |
| `get_next_line` | Buffer mantido em C# | Buffer estático em C |

### Bloco 11 — Portfólio: Deploy real do AM Kaixara + Delivery (Passo 10)
CI/CD, observabilidade, primeiro sistema em produção de verdade.

### Bloco 12 — 42: Algoritmo e gráfico (push_swap, so_long, fract-ol, fdf, pipex, minitalk)
| Projeto | Sua stack primeiro | Nativo depois |
|---|---|---|
| `push_swap` | Algoritmo em C# | Port pra C |
| `so_long` | C# + biblioteca gráfica simples | C + MiniLibX |
| `fract-ol` | C# + SkiaSharp (conecta com Números Complexos, Parte VI) | C + MiniLibX |
| `fdf` | C# + SkiaSharp (conecta com Geometria Espacial, Parte V) | C + MiniLibX |
| `pipex` | `System.Diagnostics.Process` | `fork`/`pipe`/`exec` |
| `minitalk` | `EventWaitHandle` simulando sinal | `signal`/`kill` real |

### Bloco 13 — Portfólio: Performance real (Passo 11) + início da Fase 6D (Passo 12)
Extração da plataforma interna — template, `aura-identity`, biblioteca de multi-tenancy.

### Bloco 14 — 42: Concorrência e shell (philosophers, minishell)
| Projeto | Sua stack primeiro | Nativo depois |
|---|---|---|
| `philosophers` | `Thread`/`SemaphoreSlim` (mesmo músculo do RNFT-E01) | `pthread`/`sem_t` |
| `minishell` | `Process.Start` simulando shell | `fork`/`execve`/`pipe`/`dup2` reais |

### Bloco 15 — Portfólio: segundo sistema completo (AM Rotara em produção) + início do terceiro (AM Rendara ou próximo da fila)

### Bloco 16 — 42: Rede, 3D, início de C++ (cub3d, miniRT, net_practice, CPP 00-04)
| Projeto | Sua stack primeiro | Nativo depois |
|---|---|---|
| `cub3d` | C# + SkiaSharp | C + MiniLibX |
| `miniRT` | C# + SkiaSharp (conecta com Geometria Analítica, Parte V) | C + MiniLibX |
| `net_practice` | — (infraestrutura, sem par) | Configuração de IP/rede |
| CPP 00-04 | — (conceito de OOP já dominado via C#) | Prática direta de sintaxe C++ |

### Bloco 17 — Portfólio: continua a fila de sistemas (AuraVet, AM Consertta, conforme prioridade já definida)

### Bloco 18 — 42: C++ avançado (CPP 05-09)
Exceção, template (≈ generics de C#), STL, herança múltipla — prática direta, sem par C#.

### Bloco 19 — Portfólio: continua a fila (Momentos/Cupido, Loja Virtual, AM Predara, AM Canteira, AM Saberia, AM Horaria)

### Bloco 20 — 42: Containerização e servidor (inception, webserv, ft_irc)
| Projeto | Sua stack primeiro | Nativo depois |
|---|---|---|
| `inception` | — (Docker já dominado na Fase 6D; aqui só a regra rígida específica da 42 como auditoria: só Debian, sem tag `latest`) | Mesmo, com a disciplina extra |
| `webserv` | Já feito na Fase 2.2 (`TcpListener`) | C++ com socket POSIX e `poll`/`epoll` — fecha o ciclo do que o Kestrel faz por baixo |
| `ft_irc` | C# com `TcpListener`, protocolo IRC | C++ com socket POSIX |

### Bloco 21 — 42: Projeto final (ft_transcendence)
Fase A: nenhuma necessária — o AM Kaixara já é a versão mais completa desse conceito. Fazer mesmo assim, comparando sua própria arquitetura contra o desenho de referência da 42, como exercício de análise comparativa.

### Bloco 21B — Portfólio: AM Taskoro (22º sistema) — GraphQL híbrido, sem sair do stack fixo
**Estudar antes de codar:** GraphQL como paradigma (schema, resolver, query vs. mutation, subscription — diferente de REST, que é tudo que você já fez até aqui) aplicado via **HotChocolate**, dentro do próprio .NET — não é runtime novo, é uma biblioteca a mais no ecossistema que você já domina.
**Desenvolver:** o AM Taskoro completo — workspace, quadro Kanban com WIP limit, backlog/sprint com Burndown, ciclos RAD, colaboração em tempo real via GraphQL Subscription (sobre o SignalR/WebSocket já usado no resto do portfólio, não um mecanismo novo).
**Por que só agora, não antes:** GraphQL como paradigma rende mais depois de você já ter construído REST o bastante pra sentir a diferença real entre os dois — não porque exige stack nova (não exige mais).
**✅ Sinal de conclusão:** AM Taskoro em produção, com as 3 metodologias (Kanban/Scrum/RAD) funcionando, herdando Design System/auth/CI-CD do resto do portfólio normalmente — ver [[taskoro-documento-projeto-final]].

### Bloco 21C — Portfólio: AM Projeta (23º sistema) — diagnóstico de setup por IA
**Pré-requisito real, não só cronológico:** `aura-copilot` já validado com uso real em outro sistema (ex: AM Kaixara) **e** `aura-licensing` já cobrando de verdade em pelo menos um sistema — trava formal registrada em [[projeta-documento-projeto-final]], seção 11. Se ao chegar aqui isso ainda não estiver satisfeito, resolva primeiro antes de avançar o bloco.
**Estudar antes de codar:** `DocumentFormat.OpenXml` (geração de `.docx`), `QuestPDF` (PDF), `FluentValidation` aplicado à saída de IA, `Hangfire` ou `Quartz.NET` com armazenamento Redis (job agendado) — quatro adições específicas sobre o padrão do portfólio, todas dentro do .NET já dominado, sem stack nova.
**Desenvolver:** os 18 RF do sistema (ver documento completo) — formulário adaptativo de diagnóstico, Base de Conhecimento versionada com fluxo de aprovação, orquestração de chamada ao `aura-copilot` e montagem do relatório, QA automático, renderização `.docx`/PDF, Config Forge, gestão de kit físico via `aura-logistics`, follow-up agendado 7/30/90 dias.
**Fase jurídica específica, em paralelo — não depois:** CNPJ, contrato, seguro de responsabilidade profissional, LGPD — roda junto da maturação técnica acima, não como etapa posterior.
**✅ Sinal de conclusão:** relatório gerado e validado contra a Base de Conhecimento (RNFT-IA01), com pelo menos um follow-up agendado disparando de verdade.

### Bloco 22 em diante — Portfólio: os sistemas restantes, na ordem de prioridade de negócio já definida, sem mais bloco de 42 interrompendo (trilha 42 encerrada)

---

## Trilhas contínuas, rodando por baixo de todos os blocos acima (nunca bloqueiam, nunca são esquecidas)

| Trilha | Gatilho de entrada | Onde aprofundar |
|---|---|---|
| **Matemática avançada** (Partes III, IV, VII, VIII do livro) | Cada capítulo já tem gatilho próprio (Estatística → Performance; Combinatória/Probabilidade → Python/Fase 7) | `matematica-e-desenvolvimento-integrado` |
| **Física básica** (livro a comprar) | Desde o Bloco 1, em paralelo, revisado quando o livro chegar | *(documento a criar quando você comprar o livro — mesmo tratamento dado à matemática)* |
| **Espanhol** | Depois do Inglês atingir B1-B2 (por volta do Bloco 13) | `ingles-espanhol-integrado` |
| **Python + OR-Tools** (Fase 7) | Quando o AM Rotara (Bloco 9) chegar no bloco de roteirização | `passo-a-passo-mestre-desde-o-inicio` |
| **Pentest/OSCP** | A partir do Bloco 8 (arquitetura consolidada), mesmo ponto de entrada da Trilha 42 | `passo-a-passo-mestre-desde-o-inicio` |
| **roadmap.sh** (auditoria cruzada) | Início de cada Bloco grande | `integracao-42-roadmap-akita` |
| **Fábio Akita** (consumo contínuo) | Desde já, 1 conteúdo/semana | `integracao-42-roadmap-akita` |
| **Perfil sênior** (System Design, IaC) | A partir do Bloco 13 (Fase 6D) | `perfil-senior-completo-auditoria` |

---

## Checklist de verificação — confira item por item contra o que você pediu

- [x] **Todos os projetos da 42 na tecnologia nativa deles (C/C++)** — 25 entregáveis (estrutura oficial de Circles, verificada), Blocos 10-21, coluna "Nativo depois"
- [x] **Os mesmos projetos repetidos na sua stack (C#/.NET)** — mesma tabela, coluna "Sua stack primeiro", com nota explícita onde não se aplica (`Born2beroot`, `NetPractice`, `Inception` são infraestrutura, sem versão de linguagem)
- [x] **Conexão com o desenvolvimento dos seus próprios sistemas** — Blocos 9, 11, 13, 15, 17, 19, 21B, 21C, 22+ intercalados entre os blocos de 42, cobrindo AM Rotara, extração de plataforma, AM Taskoro, AM Projeta, e a fila completa dos 13 sistemas de negócio
- [x] **Matemática básica do livro** — Blocos 1-5 (Parte I-II) + trilha contínua (Partes III-VIII com gatilho por capítulo)
- [x] **Física básica do livro (a comprar)** — inserida como trilha contínua desde o Bloco 1, com nota honesta de que a estrutura exata aguarda o sumário real
- [x] **Ordem de qual projeto fazer depois do outro, desde o início** — blocos numerados sequencialmente, do Bloco 1 até o fim da Trilha 42 e do AM Taskoro (Bloco 21B)
- [x] Idiomas (Inglês/Espanhol), roadmap.sh, Akita, Pentest, Python, Perfil sênior — todos presentes na seção de trilhas contínuas, com gatilho de entrada explícito
- [x] **AM Taskoro (22º sistema, GraphQL híbrido via HotChocolate — dentro do .NET)** — Bloco 21B, revisado: não exige mais estudo de React/Node/GraphQL como stack separada, só GraphQL como paradigma
- [x] **AM Projeta (23º sistema, diagnóstico por IA)** — Bloco 21C, com o pré-requisito real (`aura-copilot` validado + `aura-licensing` cobrando) registrado explicitamente, não só a posição na sequência

**O que fica pendente de verdade, não por esquecimento:** o conteúdo exato de Física só fecha quando o livro chegar — assim que tiver o sumário, me mostre (foto do índice, igual fizemos com matemática) e eu reconstruo a trilha de Física com a mesma precisão, substituindo a estrutura provisória por capítulo real.

---

## 🔗 Documentos relacionados
- [[metodologia-aprendizado-cientifica]] — como estudar cada bloco acima pra reter de verdade, com protocolo de fim de bloco
