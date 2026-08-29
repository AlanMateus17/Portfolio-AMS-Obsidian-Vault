---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Ordem Concreta de Construção — RF/RNF e Telas Reaproveitáveis
### O que codar primeiro, item por item, referenciando os RFs reais já documentados — não lista genérica

---

## Como ler este documento

Cada item tem: **o RF/RNF real** (do documento onde já foi formalizado), **quantos sistemas reaproveitam** (o critério de ordenação — não é "o que é mais fácil", é "o que destrava mais coisa depois"), e **o que fazer com ele depois de pronto no AuraPOS** (extrair como biblioteca/template, conforme a Fase 6D já definida).

---

## Parte 1 — Backend: ordem de construção por RF/RNF

### Grupo 1 — Antes de qualquer funcionalidade de negócio (isso é o alicerce)

| Ordem | Item | Onde já está formalizado | Sistemas que reaproveitam | Ação após pronto |
|---|---|---|---|---|
| 1 | `tenant_id` + Row-Level Security | Padrão transversal, não um RF isolado — é decisão de schema | Todos os 19 sistemas .NET | Extrair como convenção de `DbContext` base reutilizável |
| 2 | AuraPOS RF01 — Login JWT + BCrypt, isolado por `tenant_id` | [[aurapos-documento-projeto-final]] | Todos, via `aura-identity` depois | Construir bem aqui, é o protótipo do `aura-identity` |
| 3 | AuraPOS RF02 — Controle de acesso por papel | idem | Todos | Extrair o padrão de `[Authorize(Roles=...)]`, não o papel específico |

### Grupo 2 — O padrão de CRUD com proteção (isso destrava a maioria dos sistemas de uma vez)

| Ordem | Item | Onde já está formalizado | Sistemas que reaproveitam | Ação após pronto |
|---|---|---|---|---|
| 4 | AuraPOS RF03 — CRUD de produto/categoria com `TenantId`/`FilialId` | [[aurapos-documento-projeto-final]] | Padrão de CRUD multi-tenant usado em praticamente todos | Vira o "molde" de entidade — todo sistema novo copia essa forma, não o conteúdo |
| 5 | **RNFT-E01 — Concorrência de estoque** (`RowVersion`, atualização condicional) | [[rnf-transversais-escala-seguranca-financeira]], aplicado em AuraPOS seção 6 | AuraPOS, AuraFix, Loja Virtual, AuraVet (loja), Aura Delivery, AuraCondo (reserva de área comum), AuraObra (reserva de unidade), AuraAgenda (agendamento) — **8 sistemas** | Extrair como método de extensão de repositório genérico (`UpdateWithConcurrencyCheck<T>`) |
| 6 | AuraPOS RF11 — Reserva de estoque (`ReservedQuantity`/`ReservedUntil`) | idem | AuraFix (reserva de peça por OS), Loja Virtual | Mesmo padrão de campo, reaproveitado como Value Object |

### Grupo 3 — Pagamento e cobrança (segundo maior bloco de reaproveitamento)

| Ordem | Item | Onde já está formalizado | Sistemas que reaproveitam | Ação após pronto |
|---|---|---|---|---|
| 7 | AuraPOS RF04 — Carrinho com múltiplos meios de pagamento | [[aurapos-documento-projeto-final]] | Loja Virtual, AuraFix, AuraEdu (loja material) | Extrair como componente de checkout |
| 8 | **RNFT-E02 — Idempotência de pagamento** (chave de idempotência em webhook) | [[rnf-transversais-escala-seguranca-financeira]] | Praticamente todo sistema com cobrança — **12+ sistemas** | Extrair como middleware genérico de processamento de webhook |
| 9 | `aura-licensing` RF01 — Registrar módulo ativo por `tenant_id` | [[aura-licensing-documento-projeto-final]] | Todos os 21 | Construir como serviço real assim que o AuraPOS tiver o primeiro módulo pago pra testar contra |

### Grupo 4 — Suporte e notificação (baixo esforço, altíssimo reaproveitamento)

| Ordem | Item | Onde já está formalizado | Sistemas que reaproveitam | Ação após pronto |
|---|---|---|---|---|
| 10 | `aura-notifications` RF01 — API única de envio (WhatsApp/push/e-mail) | [[aura-notifications-documento-projeto-final]] | **12+ sistemas** já preveem notificação | Construir cedo — é dos serviços mais baratos de fazer e mais usado |
| 11 | `aura-support` RF01 — Consulta consolidada de tenant | [[aura-support-documento-projeto-final]] | Todos os 21, indiretamente | Resolve a lacuna que apareceu em 9 documentos de uma vez |

---

## Parte 2 — Frontend: ordem de construção por tela

Esta é a resposta direta à sua pergunta sobre páginas. Ordenado pelo mesmo critério: quanto cada tela destrava.

| Ordem | Tela/componente | Reaproveitada por | Por que vem nessa posição |
|---|---|---|---|
| 1 | **Tela de login** | Todos os sistemas — via `aura-identity`, pode virar até uma única tela compartilhada, não replicada | É a primeira tela que qualquer sistema precisa, e a mais fácil de tornar 100% genérica |
| 2 | **Shell do painel administrativo** (sidebar, header, menu, área de conteúdo) | AuraPOS, AuraVet, AuraFix, AuraCondo, AuraObra, AuraEdu, AuraAgenda — **7 painéis administrativos** | É a "moldura" de todo sistema — construir uma vez como layout genérico, cada sistema só injeta seus próprios itens de menu |
| 3 | **Tabela genérica com busca/filtro/paginação** | Produto (AuraPOS), aluno (AuraEdu), morador (AuraCondo), cliente (AuraAgenda), unidade (AuraObra) — qualquer listagem de qualquer sistema | Praticamente toda tela do portfólio lista algo — este é o componente de maior reaproveitamento bruto de todo o front-end |
| 4 | **Formulário de cadastro/edição genérico** | Mesmo alcance da tabela — todo CRUD do portfólio | Junto com o item 3, resolve a maioria das telas administrativas simples |
| 5 | **Dashboard com card de indicador** | AuraPOS RF12, e o equivalente em praticamente todo sistema com painel administrativo | Layout de card + gráfico simples, conteúdo troca, estrutura não |
| 6 | **Checkout/carrinho** | AuraPOS, Loja Virtual, AuraFix (loja online), AuraVet (loja), AuraEdu (loja material) — **5 sistemas com loja** | Constrói uma vez no AuraPOS, reaproveita em todo sistema com componente de venda de produto |
| 7 | **Shell do portal do cliente final** (diferente do admin — mais simples, focado em self-service) | Portal do tutor (AuraVet), portal do morador (AuraCondo), portal do cliente (AuraObra), portal do aluno (AuraEdu) — **4 portais externos** | Layout mais simples que o admin, mas também genérico o bastante pra reaproveitar integralmente |
| 8 | **Linha do tempo de status** (acompanhamento de OS/pedido/processo com etapas visuais) | AuraFix (status de OS), AuraVet (internação), Aura Delivery (pedido), AuraObra (obra), AuraCondo (chamado de manutenção) | Componente visual específico, mas usado por 5 sistemas diferentes com a mesma lógica de "etapas com status" |
| 9 | **Tela de agenda/calendário** | AuraVet, AuraEdu, AuraAgenda, AuraCondo (reserva de área comum), Aura Delivery (indiretamente) | Vem depois porque é mais complexa que as anteriores, mas ainda de alto reaproveitamento |

---

## O que isso significa na prática, junto com a Fase 6D já definida

Os itens 1-6 da Parte 1 e 1-5 da Parte 2 **cabem inteiramente dentro do próprio desenvolvimento do AuraPOS** (Fases 2-3 do plano de estudo) — não são trabalho extra, são a ordem correta de construir o que você já ia construir de qualquer forma. A diferença é só a **prioridade dentro do AuraPOS**: construir esses itens primeiro, com atenção deliberada de "isso vai virar reaproveitável depois", em vez de construir na ordem que parecer mais natural no momento.

Os itens 7-11 da Parte 1 e 6-9 da Parte 2 são o que efetivamente entra na **Fase 6D (extração)** e no início do segundo sistema — não fazem sentido antes do AuraPOS ter, pelo menos, produto/venda/carrinho funcionando de verdade.

---

## Resumo em uma frase

Construa produto+carrinho+login+concorrência+tabela genérica+formulário genérico primeiro dentro do AuraPOS — isso sozinho já destrava reaproveitamento em praticamente todos os 21 sistemas, antes mesmo da Fase 6D de extração formal existir.
