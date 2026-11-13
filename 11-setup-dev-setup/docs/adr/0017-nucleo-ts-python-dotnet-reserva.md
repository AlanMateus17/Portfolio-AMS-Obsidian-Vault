# 0017 · Núcleo TypeScript + Python + SQL; .NET vira carta de reserva

- **Status:** aceita
- **Data:** 2026-11-13
- **Atualiza:** [0007 (poliglota por função)](0007-poliglota-por-funcao.md), [0003 (Azure primeiro)](0003-azure-primeiro.md), [0009 (núcleo AMtech)](0009-nucleo-amtech.md)

## Contexto

A ADR 0007 adotou "a melhor ferramenta para cada trabalho", mas ainda fixava **C#/.NET 10 como base** dos sistemas AM e como base de carreira, com o ecossistema Aura em .NET. Revisando mercado e a forma como o Alan quer trabalhar (construir e vender produto sozinho, com IA de verdade, maximizando renda e vagas), o .NET no centro passou a custar mais do que entrega: TS cobre front e back com uma linguagem só, e Python é o motor de dados/IA. A decisão de 13/11 leva o "stack por problema" até o fim — inclusive para o núcleo.

## Decisão

1. **Núcleo = TypeScript + Python + SQL.** É o que se domina a fundo antes de espalhar.
2. **.NET/C# vira carta de reserva** — puxada só para vaga corporativa que exija .NET, ou para o agente fiscal local do PDV (onde **Go** também serve, como binário único). Não é mais a base de carreira nem dos sistemas.
3. **Um produto, não um império:** o ecossistema Aura / 23 sistemas é substituído por **um produto único, AM Gestão** (PDV + Pedidos + Financeiro + Loja). Supersede a lógica multi-sistema da 0009.
4. **Aposentados** (saem do centro): ASP.NET Core Controllers, Clojure/Datomic, SignalR, EF Core, GraphQL/HotChocolate, Redis como peça fixa.
5. **Entram:** Supabase (banco/auth/realtime), pgvector + Ollama + PyTorch (IA/RAG), Pix/Mercado Pago/Stripe. **Rust** e **C/C++** entram pela trilha de SO e robótica (0016). **Go** segue como carta de performance/CLI/agente fiscal.
6. **Nuvem:** com o núcleo em TS/Python, o deploy primário é **Vercel (web) + VPS**; Azure deixa de ser "primeira nuvem por combinar com .NET" (atualiza a 0003). AWS/Azure entram como estudo/portfólio, não como padrão.

## Consequências

- A tabela "onde cada linguagem é primeira escolha" da 0007 muda: **Sistemas AM → TypeScript (Next/NestJS) + Python/FastAPI + PostgreSQL (Supabase)**; o resto (Astro p/ conteúdo, Go p/ CLI, Rust p/ firmware, Python p/ dados) continua.
- A trilha de estudo passa a ter TS e Python como espinha; .NET sai da base e vira eletiva de reserva.
- Fonte da verdade de tecnologia: `portfolio-ams/05-stack-tecnologica/stack-tecnologica.md` e `PLANO-UNICO-AMtech.md`.
