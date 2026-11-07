# 0006 · Contratos na borda: OpenAPI no backend, Zod no front

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O contexto mestre exige "contratos estritos de dados em tempo de execução via Zod" em todo o sistema. Zod é uma biblioteca de TypeScript: no backend .NET 10 do Aura ela não existe. Adotar Zod no backend obrigaria a trocar o ASP.NET Core por Node (Fastify), abrindo uma segunda stack.

O que o contexto mestre quer de verdade é: nenhum dado entra ou sai do sistema sem ser validado contra um contrato.

## Decisão

1. **Backend (.NET 10):** o contrato é o documento OpenAPI gerado pela API (Scalar para ler). A validação de entrada fica nos DTOs da API, e o domínio só aceita objetos válidos (Clean Architecture + DDD). Nada de `object`, `dynamic` ou `JsonElement` atravessando camada.
2. **Front (Next.js + TypeScript):** **Zod** valida tudo o que chega da API e dos formulários antes de virar estado. `strict` no `tsconfig` e nenhum `any`.
3. **Qualidade do front:** **Biome** (lint e formatação num binário só, no lugar de ESLint + Prettier) e **Vitest** para as regras do front. Playwright e k6 continuam como estavam.
4. O `just check` de cada sistema roda o Biome e o Vitest junto com o `dotnet test`.

## Consequências

- O mesmo rigor do contexto mestre, sem uma segunda linguagem de backend.
- Quando a API muda o contrato, o esquema Zod do front quebra no teste, não em produção.
- Gerar os esquemas Zod a partir do OpenAPI automaticamente fica para quando houver mais de um front consumindo a mesma API.
