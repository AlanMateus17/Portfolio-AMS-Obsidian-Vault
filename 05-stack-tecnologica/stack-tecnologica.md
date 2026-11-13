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
| Performance extrema / CLI / agente local | **Go** (carta de reserva) |
| Vaga corporativa que exige .NET | **C#** (carta de reserva) |

---

## 3. Cartas de reserva (não estudo agora, puxo quando o problema aparecer)

- **Go** — binário único, ótimo para ferramentas de linha de comando e para o **agente local fiscal** do PDV (impressora ESC/POS, gaveta de dinheiro, TEF). É o lugar onde "desktop no balcão" realmente precisa de algo fora do TS.
- **C#/.NET** — só se eu for atrás de uma vaga corporativa de .NET, ou se o agente fiscal já existir pronto nele. Não é mais a base.

> Regra: nunca adoto uma linguagem "pelo currículo". Só quando o núcleo não resolve com maturidade igual.

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

## 🔗 Relacionados
- [PLANO-UNICO-AMtech](../PLANO-UNICO-AMtech.md) · [trilha-engenharia-software](../07-estudo-e-carreira/trilha-engenharia-software.md) · [trilha-dados-ia](../07-estudo-e-carreira/trilha-dados-ia.md) · [fontes-de-renda-completas](../01-planejamento-geral/fontes-de-renda-completas.md)
