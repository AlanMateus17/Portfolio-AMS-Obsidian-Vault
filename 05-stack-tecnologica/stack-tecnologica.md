---
tags: [stack, portfolio-ams]
tipo: stack
status: completo
atualizado: 2026-10-02
---

# Stack Tecnológica — Documento Único

> **Consolida três documentos antigos** (`stack-tecnologica-por-sistema`, `stack-consolidada-estudo`, `revisao-stack-tecnologica`), em três seções:
> **A.** o que cada sistema usa · **B.** a stack consolidada por categoria (pra estudo) · **C.** a revisão (decisão de fornecedor vs. estudo genuíno).
> Os três originais foram para `99-arquivo/`.

---

# A. Stack por sistema

## Sistemas de negócio
- **AM Kaixara** — C#/.NET 10, ASP.NET Core Controllers, Clean Architecture + DDD; PostgreSQL; Redis; SignalR; Next.js/TS/Tailwind. Específico: agente local (.NET, Windows Service) com `IImpressoraFiscal` (ESC/POS), `IGavetaDinheiro`, `IBalanca`, `ITefService`; SQLite local (offline); instalador MSIX/WiX com Code Signing.
- **AM Rotara** — .NET 10; PostgreSQL + **PostGIS**; Redis; SignalR. Específico: consome `aura-analytics` (OR-Tools) p/ roteirização; apps entregador/cliente (PWA vs nativo pendente).
- **AM Rendara** — .NET 10; PostgreSQL. Específico: consome `aura-vault` (AES-256 de dado bancário), `aura-historico` (Datomic) p/ simulação "e se", `aura-analytics` (Prophet/statsmodels); motor de regra (ARCA/Barsi/Value Investing) em C# puro.
- **AuraVet** — .NET 10; PostgreSQL + PostGIS; Cloudflare R2 (laudo/exame). Específico: consome `aura-vault` (prontuário), `aura-licensing`; app tutor Next.js PWA.
- **AM Consertta** — .NET 10; PostgreSQL. Reaproveita PDV/estoque do AM Kaixara; consome `aura-logistics`, `aura-notifications`.
- **Momentos/Cupido** — alvo .NET 10 (hoje protótipo Node/Express/SQLite, migração pendente); R2 (mídia). Específico: consome `aura-goals`; moderação por hash-matching (PhotoDNA/StopNCII) + humano; player Spotify.
- **Loja Virtual** — módulo do AM Kaixara, sem stack próprio; consome `aura-logistics`.
- **AM Predara** — .NET 10; PostgreSQL. Específico: agente de portaria (interfone IP/RFID/fechadura, fornecedor pendente); votação com log imutável (candidato a `aura-historico`).
- **AM Canteira** — .NET 10; PostgreSQL. Específico: consome `aura-vault` (contrato); assinatura eletrônica (DocuSign/Clicksign/D4Sign pendente); app de campo offline básico.
- **AM Saberia** — .NET 10; PostgreSQL. Específico: videoaula síncrona (Zoom/Meet ou própria pendente); consome `aura-logistics`, `aura-licensing` (B2B).
- **AM Horaria** — .NET 10; PostgreSQL com segregação de schema p/ prontuário psicológico. Específico: consome `aura-vault` com isolamento reforçado; `aura-logistics`.

## Serviços compartilhados
- `aura-licensing` — .NET 10, PostgreSQL. Cobrança recorrente (Stripe/Vindi/Iugu/Asaas pendente).
- `aura-goals` — .NET 10, PostgreSQL. Sem dependência externa; consumido por AM Rendara e Momentos/Cupido.
- `aura-historico` — **Clojure + Datomic** (fora do .NET). Consumido via Redis Streams.
- `aura-analytics` — **Python + FastAPI** (fora do .NET). Prophet/statsmodels, Google OR-Tools.
- `aura-copilot` — provedor de LLM indefinido (externo vs auto-hospedado). Function-calling, sem RAG.
- `aura-identity` — .NET 10, PostgreSQL. JWT centralizado, 2FA opcional por tenant.
- `aura-notifications` — .NET 10, PostgreSQL. WhatsApp Business API (Meta/BSP pendente), SMS/e-mail (pendente).
- `aura-support` — .NET 10, PostgreSQL. Painel interno, acesso VPN/IP allowlist.
- `aura-logistics` — .NET 10, PostgreSQL. Correios/transportadora (pendente).
- `aura-vault` — .NET 10. KMS/HSM gerenciado (AWS KMS/Azure Key Vault/HashiCorp Vault pendente), trilha de auditoria via `aura-historico`.

## Ferramentas pessoais
`aura-status` (console .NET, sem banco, lê Git/log/`gh`) · `aura-queue` (memória ou Redis) · `aura-secrets` (.NET, PostgreSQL, cripto local) · `aura-oncall` (extensão do `aura-notifications`).

## Fora do portfólio (decisão tomada)
Bun, Hono, Rust, Tauri, gRPC — nenhuma exceção nos 21 documentos.

---

# B. Stack consolidada por categoria (pra estudo)

**1. Linguagens:** C# (base, 19/21) · TypeScript (frontend) · Clojure (`aura-historico`, novo de verdade) · Python (`aura-analytics`, foco nas libs).
**2. Runtimes:** .NET 10 · Node.js · JVM (Clojure) · Python 3.x.
**3. Backend:** ASP.NET Core Controllers (fixo, nunca Minimal API) · FastAPI (único Python).
**4. Frontend:** Next.js · Tailwind (+ tokens RNFT-D) · React Native (só se decidir nativo; padrão PWA).
**5. Libs que exigem estudo:** Google OR-Tools (VRP) · Prophet/statsmodels (série temporal) · Datomic client · cripto de campo (.NET) · SQLCipher (SQLite) · ESC/POS (impressora).
**6. Dados:** PostgreSQL · PostGIS · Datomic · SQLite (offline) · Redis · Redis Streams (mensageria).
**7. Tempo real/assíncrono:** SignalR · Redis Streams (fila única, evita RabbitMQ/Kafka sem necessidade).
**8. Auth/segurança:** JWT + BCrypt (centralizar em `aura-identity`) · 2FA TOTP (obrigatório no `aura-support`) · KMS/HSM (`aura-vault`) · Code Signing (AM Kaixara).
**9. Testes:** xUnit · teste de contrato · pytest (provável, `aura-analytics`) · clojure.test.
**10. Infra/CI-CD:** Docker/compose · GitHub Actions · AWS ou Azure (pendente) · MSIX/WiX.
**11. Mídia:** Cloudflare R2 (AuraVet, Momentos/Cupido).
**12. Integrações externas:** pagamento · WhatsApp · SMS/e-mail · transportadora · assinatura eletrônica · videoaula · fiscal (NFC-e/NFSe) · LLM · hardware de portaria.
**13. Padrões transversais:** Clean Architecture + DDD · multi-tenant (`tenant_id` + RLS) · Outbox · otimização combinatória.

---

# C. Revisão — decisão de fornecedor vs. estudo genuíno

**C.1 Stack fixo:** .NET 10, ASP.NET Core Controllers, Clean Arch + DDD, EF Core, PostgreSQL, Redis, SignalR, JWT+BCrypt, Docker, xUnit, GitHub Actions, TS/Next/Tailwind. **PostGIS** virou fixo (AM Rotara, AuraVet, potenc. AM Canteira).

**C.2 Desvios conscientes:** Clojure+Datomic (`aura-historico`, consulta temporal) · Python+FastAPI (`aura-analytics`, ecossistema ML) · GraphQL via HotChocolate (AM Taskoro, dentro do .NET). **Critério:** só desviar quando o .NET literalmente não resolver com maturidade igual — nunca por valor de currículo.

**C.3 Decisões de fornecedor (escolher/integrar, não estudar):** gateway de pagamento · AWS vs Azure · WhatsApp · SMS/e-mail · transportadora · assinatura eletrônica (peso jurídico) · videoaula · hardware · KMS/HSM · Code Signing.

**C.4 Estudo genuíno:**
1. Otimização combinatória / OR-Tools (VRP) — AM Rotara. Maior sinergia com Matemática.
2. ML de série temporal (Prophet/statsmodels) — overfitting/sazonalidade.
3. Criptografia aplicada e gestão de chave — `aura-vault`.
4. Assinatura eletrônica e validade jurídica (ICP-Brasil vs simples/avançada) — AM Canteira/Predara.
5. Function-calling pra IA (sem RAG) — `aura-copilot`.
6. Acessibilidade web (WCAG) — transversal (RNFT-D04).

**C.5 Fora, por decisão:** mobile nativo (PWA basta); blockchain/Web3 no Aura (ByteSDCoin é projeto educacional à parte — [[projeto-apostas-blockchain-educacional]]).

**C.6 Ordem de estudo:** 1) OR-Tools 2) criptografia 3) assinatura eletrônica 4) ML/function-calling 5) acessibilidade (contínua).

---

## 🔗 Relacionados
- [[00-PLANO-UNIFICADO]] · [[inventario-portfolio-atualizado]] · [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] · [[trilha-42-circles-oficial-verificado]] · [[kaixara-documento-projeto-final|AM Kaixara]]
