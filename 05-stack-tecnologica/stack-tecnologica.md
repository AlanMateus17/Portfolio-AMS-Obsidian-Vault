---
tags: [stack, portfolio-ams]
tipo: stack
status: definitivo
atualizado: 2026-11-13
---

# Stack Tecnológica — Documento Único (definitivo)

> **Filosofia (Akita): stack por problema, não stack fixa.** Núcleo pequeno e dominado; cada problema usa a ferramenta certa. Substitui o antigo stack fixo em .NET.
> Fonte da verdade de tecnologia do portfólio. O plano completo está em [PLANO-UNICO-AMtech](../PLANO-UNICO-AMtech.md).

---

## 1. Núcleo (o que eu domino de verdade)

**TypeScript · Python · SQL.** Tudo gira em torno disso. Aprofundar aqui antes de espalhar.

- **Frontend:** Next.js + Tailwind.
- **Backend web:** Next.js (API/route handlers) ou NestJS quando precisar de backend TS separado.
- **Backend dados/IA:** Python + FastAPI.
- **Banco:** PostgreSQL via **Supabase** (banco + auth + storage + realtime prontos). ORM em TS: Prisma ou Drizzle.
- **Offline (PDV):** SQLite local, sincroniza quando volta a conexão.
- **Geolocalização/entrega:** PostGIS (suportado pelo Supabase).
- **Pagamentos:** Pix / Mercado Pago (Brasil) + Stripe (internacional).
- **IA de verdade:** pandas, scikit-learn, PyTorch; **pgvector** (busca semântica/RAG) + **Ollama** (modelo local).
- **Infra:** Docker · Git + GitHub Actions · deploy em Vercel (web) ou VPS.

---

## 2. Stack por problema

| Problema | Ferramenta |
|---|---|
| Site, painel, loja, app web | TypeScript + Next.js + Tailwind |
| API/backend do produto | TypeScript (Next/NestJS) |
| Dados, automação, IA/ML | Python + FastAPI |
| Banco, login, arquivos, tempo real | PostgreSQL + Supabase |
| PDV offline | SQLite |
| Entrega/rotas (geoloc) | PostGIS |
| Busca semântica / RAG / IA local | pgvector + Ollama + PyTorch |
| Robótica, sensores, protótipos | C/C++ (Arduino/ESP32) · Python (Raspberry Pi) |
| Sistema operacional / baixo nível | Linux/Arch · C/C++ · Rust |
| **Suas ferramentas, CLIs, automação, agente fiscal** | **Go** (trilha ativa — ver §3) |
| Vaga corporativa que exige .NET | **C#** (carta de reserva) |

---

## 3. Go — trilha ativa (minhas ferramentas)

Go deixou de ser reserva: é a linguagem com que eu construo **as minhas ferramentas**. Binário único, rápido, fácil de distribuir. Uso para:

- **CLIs e automação** do meu dia a dia e do dev-setup (organizar arquivos, gerar relatórios, rodar rotinas).
- **Agente local fiscal** do PDV (impressora ESC/POS, gaveta de dinheiro, TEF) — binário único no balcão.
- **Serviços de performance** quando o TS/Python não derem conta.

Passo a passo próprio em [trilha-go-ferramentas](../07-estudo-e-carreira/trilha-go-ferramentas.md).

## 3b. Carta de reserva

- **C#/.NET** — só se eu for atrás de uma vaga corporativa de .NET, ou se o agente fiscal já existir pronto nele. Não é mais a base.

> Regra: nunca adoto uma linguagem "pelo currículo". Go entrou porque resolve um problema real meu (ferramentas e o agente fiscal); o núcleo (TS+Python+SQL) continua sendo o centro.

---

## 4. O que foi aposentado (saiu do centro)

| Saiu | Era | Virou |
|---|---|---|
| C# como base (19/21 sistemas) | coração de tudo | carta de reserva |
| ASP.NET Core Controllers | backend fixo | Next/NestJS + FastAPI |
| Clojure + Datomic (`aura-historico`) | histórico temporal | cortado (1 produto só não justifica) |
| SignalR | tempo real .NET | realtime do Supabase |
| Redis / Redis Streams | peça fixa | opcional (só com necessidade real) |
| EF Core | ORM fixo | Prisma / Drizzle + cliente Supabase |
| GraphQL / HotChocolate | AM Taskoro | saiu junto com o Taskoro |
| "stack fixa, sem exceção nos 21 docs" | regra central | **stack por problema** |
| Mandarim | trilha de idioma | removido (foco: inglês + espanhol) |
| Império de 23 sistemas | portfólio | **1 produto: AM Gestão** |

Entrou de novo: **Supabase, Go, Rust** (antes proibido), **C/C++**, **pgvector/Ollama/PyTorch** (IA real) e **Pix/Mercado Pago/Stripe** (gateway antes pendente).

---

## 5. Único produto: AM Gestão

Em vez de 23 sistemas, **um** produto completo, lançado como MVP e vendido:

- **Caixa (PDV)** — era Kaixara. TS + SQLite offline + agente fiscal (Go/C#).
- **Pedidos/Entrega** — era Rotara. TS + PostGIS.
- **Financeiro** — era Rendara. TS + Python para análise.
- **Loja online** — módulo Vendra. Next.js.

MVP = Caixa + Pedidos + Financeiro. Clientes já com procura: restaurantes e vendas online.

---

## 6. O que estudar em cada ferramenta (resumo)

> O caminho dia a dia está no [PLANO-PASSO-A-PASSO](../07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md). O detalhe profundo, no [currículo sênior](../07-estudo-e-carreira/curriculo-dev-senior-completo.md). Esta tabela é a consulta rápida.

| Ferramenta | O que estudar nela |
|---|---|
| **TypeScript** | Tipos e narrowing, generics, `async/await`, módulos, `map/filter/reduce`, tratamento de erros |
| **Python** | Sintaxe, estruturas, funções, OOP, `venv`/pip, async |
| **SQL** | `SELECT/WHERE/JOIN`, `GROUP BY`, window functions, índices, transações, isolamento, N+1 |
| **Next.js** | App Router, componentes, rotas de API, Server Actions, SSR/SSG |
| **Tailwind** | Utilitários, responsividade, temas |
| **NestJS** | Módulos, injeção de dependência, controllers, providers |
| **FastAPI** | Endpoints, Pydantic (validação), async, dependências |
| **PostgreSQL** | Modelagem, constraints, transações, isolamento, índices |
| **Supabase** | Auth, Row-Level Security, storage, realtime, client |
| **Prisma/Drizzle** | Schema, migrations, relations, queries |
| **SQLite** | Banco local, offline, sincronização |
| **PostGIS** | Geolocalização, rotas · **pgvector** | busca semântica/RAG |
| **Go** | `flag`, `os`/`filepath`, `encoding`, `os/exec`, `net/http`, goroutines/channels, cross-compile, agente fiscal |
| **pandas** | DataFrames, limpeza, agregação · **scikit-learn** | pipelines, modelos, avaliação |
| **PyTorch** | Tensores, redes, treino · **Ollama** | modelo local, RAG |
| **Docker** | Dockerfile, compose, volumes, redes |
| **Git + GitHub Actions** | Branches, PR, workflows CI |
| **Vitest/pytest** | Testes de unidade, mocks, cobertura · **Playwright** | E2E |
| **Pix/Mercado Pago/Stripe** | Cobrança, webhooks, idempotência |
| **Linux/Arch** | Instalação, pacotes, systemd, shell, dotfiles |
| **C/C++** | Ponteiros, memória, Arduino/ESP32 · **Rust** | ownership, cargo, embarcado |
| **Raspberry Pi** | GPIO, sensores, serial · **React Native** (2028) | componentes, navegação |
| **C# (reserva)** | Só se for atrás de vaga corporativa .NET |

---

## 🔗 Relacionados
- [PLANO-UNICO-AMtech](../PLANO-UNICO-AMtech.md) · [trilha-engenharia-software](../07-estudo-e-carreira/trilha-engenharia-software.md) · [trilha-dados-ia](../07-estudo-e-carreira/trilha-dados-ia.md) · [fontes de renda (PLANO-UNICO §6)](../PLANO-UNICO-AMtech.md)
