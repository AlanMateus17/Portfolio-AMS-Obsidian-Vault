---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AgileFlow — Decisão de Stack e Entrada no Portfólio
### 22º sistema do portfólio — decisão de stack revisada: híbrido, sem sair do .NET

---

## O que é

Plataforma de gerenciamento de projeto full-stack, suportando **Kanban, Scrum e RAD** nativamente, selecionável por projeto — não força uma metodologia única. Workspaces, quadro Kanban com WIP limit, backlog/sprint com Burndown, ciclos RAD com feedback de protótipo, colaboração em tempo real, automação de fluxo, integração externa (GitHub, Slack/Discord, Figma).

---

## Decisão de stack — revisada (versão anterior propunha React/Node/TS/GraphQL completo)

| | |
|---|---|
| **Stack decidida** | **.NET (igual ao resto do portfólio)** + **GraphQL via HotChocolate**, no lugar de REST puro |
| **Desvio do padrão fixo Aura** | Só no paradigma de API (GraphQL em vez de REST) — **runtime, linguagem, ORM, autenticação, Design System: tudo igual ao resto** |
| **Por que a versão anterior (Node/React/TS/GraphQL) foi revisada** | A justificativa original ("GraphQL resolve sync granular melhor que SignalR") não se sustenta — SignalR consegue sync campo-a-campo com um protocolo de patch bem desenhado, e GraphQL como paradigma **não exige Node**: HotChocolate é um servidor GraphQL maduro pra .NET. A troca de stack completa não passa no critério de desvio (ver `revisao-stack-tecnologica`) — era motivada por valor de currículo isolado, não por limitação técnica real do .NET |
| **O que se ganha mantendo híbrido** | GraphQL de verdade no currículo (schema design, resolver, N+1/DataLoader, subscription — o que cai em entrevista) **+** reaproveitamento total: `aura-identity`, multi-tenancy, Design System, CI/CD, tudo herdado igual aos outros 21 sistemas |
| **Precedente** | Mesmo critério já aplicado a `aura-historico` (Clojure/Datomic) e `aura-analytics` (Python/FastAPI) — desvio aceito só quando o .NET literalmente não tem equivalente maduro; GraphQL tem (HotChocolate), então o desvio fica restrito à API, não ao runtime inteiro |

---

## Onde entra no portfólio

**22º sistema de negócio**, elevando o total de 21 pra 22 — mas agora **herda o Design System C#/Next.js normalmente**, como qualquer outro sistema. Reaproveita todos os serviços compartilhados sem precisar de integração via API externa (`aura-identity`, `aura-notifications` incluídos nativamente).

---

## Onde entra na sequência de estudo

Não abre mais uma trilha de linguagem nova — o estudo de GraphQL/HotChocolate entra como um tópico dentro do .NET já em andamento, não como pré-requisito de um runtime novo. Posição recomendada: continua depois de 2-3 sistemas do portfólio principal em produção (mesma posição de antes), só que agora sem o custo de aprender Node/TS/React antes.

---

## 🔗 Documentos relacionados
- [[sequencia-mestra-completa-desde-o-inicio]] — onde este sistema entra na ordem real de estudo
- [[biblioteca-recursos-por-passo]] — recursos oficiais de GraphQL e HotChocolate
- [[revisao-stack-tecnologica]] — critério geral de quando um desvio de stack é aceito
- [[mapa-mestre-prioridade-total]] — posição de prioridade deste sistema
