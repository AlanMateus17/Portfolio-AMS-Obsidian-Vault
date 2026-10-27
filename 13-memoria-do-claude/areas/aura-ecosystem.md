---
name: aura-ecosystem
description: The Aura ecosystem — architecture, stack, and shared services for AMtech's interconnected software systems
sources: [backfill]
aliases: [Aura]
---
- [stated] Aura ecosystem architecture: multi-tenant SaaS with tenant_id + Row-Level Security, four swappable interfaces (IFonteDeEstoque, IEmissorFiscal, IFonteDeMovimentacaoBancaria, IFonteDeReceita), aura-licensing for module-gated billing, and 19 commercial packages
- [stated] Produced full Project Final Documents (11-section template) for 23 interconnected software systems (13 business systems including AgileFlow and AuraArquiteto, plus 10 shared services) under the Aura ecosystem
- [stated] AuraArquiteto (AI-powered setup diagnosis and architecture generation system) is now fully merged into the portfolio vault with its own Project Final Document; it originates the transversal RNFT-IA01–04 AI-generation-governance series
- [stated] Fixed stack: C#/.NET 10, ASP.NET Core Controllers, Clean Architecture + DDD, PostgreSQL, Redis, SignalR, TypeScript/Next.js/Tailwind, Docker, GitHub Actions
- [stated] Intentional stack deviations: Clojure/Datomic for aura-historico, Python/FastAPI for aura-analytics
- [stated] .NET version fixed at 10 (LTS through 2028)
- [stated] Technologies explicitly rejected: Bun, Hono, Rust, Tauri, gRPC
- [stated] Prefers Controllers over Minimal API in ASP.NET Core
- [stated] Three transversal RNF document sets created: scale/financial security, distribution/security, design/theming (RNFT-D01–D07)
- [stated] Transversal AI governance series RNFT-IA01–04 created for any Aura system using aura-copilot for client-facing output
- [stated] GitHub Organization structure (grupo-amtech-digital) documented with ADRs, GitHub Projects mirroring EPIC-01, Conventional Commits, and MkDocs Pages
- [stated] Approximately 23 GitHub repositories across 12 business systems, 10 shared services, and AuraTest
- [stated] Rule confirmed: only the 10 existing shared services are reused — no invented service names
- [stated] Repository naming convention decided: business-system repos use the portfolio product name in lowercase-hyphen form (e.g. am-kaixara, am-rotara, am-rendara); "AM" is a real portfolio brand prefix (confirmed by AM Kaixara, AM Rotara, AM Rendara), not unique to Kaixara; shared services keep their existing aura- prefix
- [stated] GitHub org is grupo-amtech-digital; creating am-kaixara, am-rotara, and am-rendara there as the first three repos, each as a fully separate repository (not a monorepo)
- [stated] Frontend design system (Aura Design System, RNFT-D01–D07) documented: admin panels use fixed Aura palette (#0E3A45, #C08A3E, #F7F5F0); public surfaces inherit tenant brand color at runtime via CSS variables
- [stated] Next.js + TypeScript + Tailwind frontend kit (aura-frontend-kit.zip) produced with tailwind.config.ts, globals.css, contrast utility, MarcaThemeProvider, and typed components for 5 screen types
- [stated] Four-phase frontend roadmap: Phase 1 (AuraPOS — builds 6 foundational reusable blocks), Phase 2 (Aura Delivery + Loja Virtual), Phase 3 (AuraWealth + Momentos & Cupido), Phase 4 (vertical services portfolio)
- [stated] CEA or CFP certification recommended to unblock AuraWealth Consultoria tier
- [stated] Encontrou uma pessoa que vai ter as certificações CEA/CFP, potencialmente destravando o tier de consultoria do AuraWealth
- [stated] Essa pessoa será sócia fixa (não contratação pontual), vai começar a estudar para a certificação, e o plano é ela assumir a consultoria do AuraWealth
- [stated] Nomenclatura canônica dos 13 sistemas de negócio, padrão "AM" (renomeação dos nomes Aura* antigos): AM Kaixara (PDV, ex-AuraPOS), AM Rendara (finanças/ARCA, ex-AuraWealth), AM Rotara (pedidos+geolocalização, ex-Aura Delivery), AM Taskoro (Kanban/Scrum, ex-AgileFlow), AM Projeta (diagnóstico+arquitetura por IA, ex-AuraArquiteto), AM Predara (condomínios, ex-AuraCondo), AM Canteira (obras/construção, ex-AuraObra), AM Consertta (assistência técnica, ex-AuraFix), AM Horaria (agendamentos, ex-AuraAgenda), AM Saberia (educacional, ex-AuraEdu), AM Petara (veterinária, ex-sistema-veterinário), AM Vendra (e-commerce, ex-Loja Virtual), AM Vynla (relacionamentos/timeline/NFC, ex-Momentos & Cupido). Serviços compartilhados e ferramentas pessoais mantêm o prefixo aura-.
