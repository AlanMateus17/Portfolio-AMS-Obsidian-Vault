---
name: aurapos
description: AM Kaixara (antigo AuraPOS) — projeto de PDV dentro do ecossistema Aura, recomeçado do zero
sources: [backfill, chat]
aliases: [AuraPOS, AM Kaixara]
---
- [stated] Antigo AuraPOS agora se chama AM Kaixara
- [stated] Decidiu recomeçar o AM Kaixara do zero: mesma stack e escopo do AuraPOS, descartando o código atual, mantendo a integração com o ecossistema Aura
- [stated] AuraPOS is a software product within the Aura ecosystem, currently at Sprint 3–4
- [stated] Sprint 2 backend fully debugged: Product CRUD, stock management, EF Core migrations, Docker volume bug resolved, ASP.NET Core validation bug with [property: Required] on records fixed
- [stated] AuraPOS frontend planning reached an 11-stage document covering Discovery, Design System (Inter + JetBrains Mono, 4px grid, Lucide icons), Frontend Engineering (TanStack Query + Zustand, OpenAPI auto-generated client), Accessibility, QA (Testing Library + Playwright + Storybook), and Security
- [stated] Decidiu desenvolver o AM Kaixara para web (admin) e balcão/caixa (PWA no mesmo Next.js), com app nativo (.NET MAUI) só se hardware físico (impressora, gaveta) exigir
- [stated] Havia divergência entre dois valores de paleta (acento #C08A3E do Aura Design System original vs. #B08D57 de um documento específico do AuraPOS); o usuário pediu para o Claude decidir, que optou pela paleta original (#C08A3E), já usada no aura-frontend-kit
