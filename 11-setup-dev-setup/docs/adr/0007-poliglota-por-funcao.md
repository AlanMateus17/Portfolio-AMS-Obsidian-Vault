# 0007 · Poliglota por função: a melhor ferramenta para cada trabalho

- **Status:** aceita
- **Data:** 2026-11-06
- **Substitui:** a lista de tecnologias rejeitadas (Bun, Hono, Rust, Tauri, gRPC) e a regra de stack única

## Contexto

Até aqui o setup tinha uma stack fixa (.NET 10 com Next.js) e uma lista de tecnologias proibidas. O Alan decidiu (06/11/2026) que não quer limite de linguagem para desenvolver e empreender: quer ser produtivo com a melhor ferramenta para cada trabalho.

## Decisão

1. **Nada é proibido por linguagem.** O que decide é a triagem (`just triagem`): subir pronto, colar ou construir, e com qual ferramenta.
2. **Aura continua em .NET 10** (Clean Architecture + DDD, PostgreSQL, Next.js): não há ganho em reescrever o que já está desenhado.
3. **Onde cada linguagem é a primeira escolha:**

| Trabalho | Primeira escolha |
|---|---|
| Sistemas AM (SaaS, multi-tenant) | C#/.NET 10 + Next.js |
| Site de conteúdo, blog, landing page, catálogo | Astro |
| App pequeno e interativo, MVP com PocketBase | SvelteKit |
| Validação rápida (MVP antes de construir) | PocketBase + Litestream |
| CLI do setup ou produto em binário único | Go (bubbletea, GoReleaser) |
| Firmware, ferramenta que precisa de desempenho | Rust (probe-rs, cargo-dist) |
| Dados, IA e scripts do setup | Python (uv) |
| E-mail transacional | React Email nos modelos |

4. **Cada sistema com a mesma árvore,** em repositório próprio: `apps/web`, `apps/api`, `packages/core` (regras puras), `packages/db` e `config/deploy.yml`.

## Consequências

- Mais linguagens para manter atualizadas; o mise instala e fixa a versão de todas.
- Cada linguagem nova num produto passa pela triagem e ganha um ADR, para não virar coleção.
- A trilha de estudo ganha Go e Rust como eletivas; .NET continua a base de carreira.
