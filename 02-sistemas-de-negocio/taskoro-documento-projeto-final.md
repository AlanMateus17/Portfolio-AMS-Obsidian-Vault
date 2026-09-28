---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Taskoro — Documento de Projeto Final
### 22º sistema do portfólio — plataforma de gestão de projeto (Kanban/Scrum/RAD), .NET com GraphQL híbrido

---

## 1. Visão do produto

Plataforma de gerenciamento de projeto full-stack, suportando **Kanban, Scrum e RAD** nativamente, selecionável por workspace/projeto — não força uma metodologia única, ao contrário da maioria das ferramentas do mercado que assumem uma metodologia fixa.

**Diferencial:** metodologia plugável por projeto dentro do mesmo workspace (um time pode rodar Kanban puro enquanto outro roda Scrum com sprint/burndown, sem trocar de ferramenta) + automação de fluxo configurável sem código.

**Público-alvo:** times de desenvolvimento pequenos/médios, freelancers gerenciando múltiplos clientes ao mesmo tempo, agências — e uso interno da própria AMtech Digital pra gerenciar o desenvolvimento dos outros 21 sistemas do portfólio (dogfooding real, vira case de uso próprio documentável).

---

## 2. Funcionalidades completas (estado final)

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Workspace | Organização por time/projeto, convite de membro, papel (admin/membro/convidado) | Novo |
| Quadro Kanban | Coluna configurável, WIP limit por coluna, card com subtarefa | Novo |
| Backlog & Sprint | Backlog priorizável, sprint com Burndown Chart, velocity | Novo |
| Ciclos RAD | Protótipo versionado + coleta de feedback estruturado do cliente | Novo |
| Colaboração em tempo real | Múltiplos usuários editando quadro/card simultaneamente | Novo (SignalR) |
| Automação de fluxo | Regra configurável ("quando card entra em X, faça Y") sem código | Novo |
| Integrações externas | GitHub (PR vinculado a card), Slack/Discord (notificação), Figma (embed de protótipo) | Novo |
| Relatórios & métricas | Cycle time, lead time, velocity histórico, burndown | Novo |
| API GraphQL | Consulta/mutação granular do quadro, subscription pra sync em tempo real | Novo (HotChocolate) |
| Autenticação | Login de workspace e membro | 100% reaproveitado — `aura-identity` |
| Cobrança recorrente | Assinatura por workspace/membro ativo | 100% reaproveitado — `aura-licensing` |
| Notificação | Alerta de menção, prazo, mudança de status | 100% reaproveitado — `aura-notifications` |

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Criação de workspace com convite de membro por e-mail/link | Permite múltiplos times/clientes isolados na mesma conta, sem misturar dado |
| RF02 | Quadro Kanban com coluna configurável e WIP limit | Impede acúmulo de trabalho "em andamento" além da capacidade real do time |
| RF03 | Card com subtarefa, responsável, prazo e anexo | Cobre o nível de detalhe que um card real de trabalho precisa, não só título |
| RF04 | Backlog priorizável com sprint e Burndown Chart | Dá ao time que usa Scrum a visão de progresso que a metodologia exige |
| RF05 | Ciclo RAD com protótipo versionado e feedback estruturado do cliente | Suporta o time que prefere iteração rápida com validação de cliente em vez de sprint fixo |
| RF06 | Seleção de metodologia (Kanban/Scrum/RAD) por projeto dentro do mesmo workspace | É o diferencial central do produto — nenhum time é forçado a uma metodologia que não usa |
| RF07 | Sincronização em tempo real de mudança de card/quadro entre usuários conectados | Evita que dois membros editem o mesmo card com dado desatualizado na tela |
| RF08 | Motor de automação de fluxo configurável sem código ("quando X, faça Y") | Reduz trabalho manual repetitivo (mover card, notificar, atribuir) sem exigir script |
| RF09 | Integração com GitHub — PR vinculado a card, status refletido automaticamente | Elimina atualização manual de status quando o código já diz onde a tarefa está |
| RF10 | Integração com Slack/Discord — notificação de evento do quadro | Leva a notificação pro canal que o time já usa, sem exigir que abram o AM Taskoro toda hora |
| RF11 | Embed de protótipo Figma dentro do card RAD | Centraliza a validação de design junto do card, sem alternar de ferramenta |
| RF12 | Relatório de cycle time, lead time e velocity histórico | Dá ao Product Owner dado real de ritmo do time, não estimativa |
| RF13 | API GraphQL com query granular por campo e subscription | Permite que o próprio cliente (ou integração futura) consuma só o dado que precisa, sem over-fetching |
| RF14 | Login de workspace e membro | Protege acesso ao quadro e dado do time |
| RF15 | Cobrança recorrente por workspace/membro ativo | Sustenta o modelo de receita via assinatura |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

| Perfil | Interface/fluxo | Caminho completo |
|---|---|---|
| Admin do workspace | Painel de configuração | Cria workspace → convida membro → define metodologia por projeto → configura automação |
| Membro do time | Quadro de trabalho | Login → seleciona projeto → move card / atualiza sprint → recebe notificação de menção |
| Cliente/Stakeholder (RAD) | Área de feedback do protótipo | Recebe link → visualiza protótipo Figma embutido → deixa feedback estruturado no card |
| Alan/Admin da plataforma | Uso interno — gestão do próprio portfólio | Mesmo workspace usado pra gerenciar o backlog dos outros 21 sistemas (`EPIC-01` e futuros) |

---

## 5. Requisitos Não Funcionais (RNF) — próprios e transversais

| ID | Aplicação no AM Taskoro | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado de membro (nome, e-mail) e conteúdo de card são dado pessoal/de negócio do cliente | Cumpre obrigação legal sobre dado de contato e conteúdo de trabalho |
| RNFT07 (BOLA) | Toda query/mutation GraphQL que recebe ID de card/workspace deve validar que o usuário autenticado pertence àquele workspace | Impede que um membro de um workspace veja/edite card de outro só trocando o ID na query |
| RNFT-S03 (consentimento explícito de integração) | Conexão com GitHub/Slack/Discord/Figma exige autorização OAuth explícita do usuário, nunca automática | Impede acesso a repositório/canal do usuário sem consentimento claro |
| RNFT-S04 (escopo mínimo de credencial) | Token OAuth de integração externa armazenado com escopo mínimo necessário (ex: GitHub só leitura de PR, não repositório inteiro) | Reduz o dano possível se um token vazar |
| RNFT-E01 (concorrência) — adaptado | Duas edições simultâneas do mesmo card (ex: mover coluna) resolvidas por versionamento otimista, não last-write-wins silencioso | Evita que a mudança de um membro apague a de outro sem aviso |
| RNFT-E05 (observabilidade) | Falha de sincronização em tempo real (SignalR) ou de integração externa deve gerar log estruturado + alerta | Permite descobrir que uma integração parou de funcionar antes do time reclamar |
| **Específico de GraphQL — limite de profundidade/complexidade de query** | Toda query GraphQL tem profundidade e complexidade máxima configurada no HotChocolate | Sem isso, uma query aninhada demais vira vetor de negação de serviço — risco específico do paradigma GraphQL que REST não tem |

---

## 6. Segurança de nível profissional

`tenant_id` + Row-Level Security por workspace, no mesmo padrão do resto do portfólio. Autenticação via `aura-identity` (JWT + BCrypt). Autorização em GraphQL validada por diretiva a nível de campo (não só na rota, como seria em REST) — cada resolver sensível revalida pertencimento ao workspace, não confia só no filtro da query. Token de integração externa (GitHub/Slack/Figma) armazenado criptografado. Limite de profundidade/complexidade de query (RNF acima) ativo desde o primeiro deploy, não como correção posterior.

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** AM Taskoro é SaaS puro (backend + frontend web), sem componente físico e sem modelo de instalador executável. Distribuição comercial segue o padrão de pacotes + `aura-licensing`, como qualquer outro sistema do portfólio sem hardware.

---

## 8. Deploy e CI/CD

Padrão do portfólio, sem desvio: Docker multi-stage, GitHub Actions, deploy gerenciado, observabilidade (log estruturado, health check). Por ser .NET como o resto do ecossistema, reaproveita o pipeline de CI/CD já extraído no Passo 12 da sequência de estudo, sem pipeline próprio a manter.

---

## 9. Modelo de receita

| Fonte | Modelo |
|---|---|
| Assinatura por workspace | Tier gratuito limitado (nº de membros/projetos) + tier pago por membro ativo, via `aura-licensing` |
| Combo de portfólio | Desconto quando combinado com outro sistema Aura contratado pelo mesmo cliente |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito.** Decisão de stack revisada nesta sessão (28-29/08/2026) — de React/Node/GraphQL completo para híbrido GraphQL-via-HotChocolate dentro do .NET. Este é o primeiro documento de projeto final completo do sistema; antes só existia o documento de decisão de stack.

---

## 11. Pendências e decisões em aberto

1. **Limite exato do tier gratuito** (nº de workspaces/membros/projetos) — não decidido ainda, depende de benchmark de concorrente na hora de precificar
2. **Profundidade máxima de query GraphQL** (RNF de segurança acima) — valor específico não definido, decidir na implementação do HotChocolate
3. **Prioridade de integração externa no MVP** — GitHub entra primeiro (mais valor pro uso interno de gerenciar o próprio portfólio); Slack/Discord e Figma podem esperar uma fase 2

---

## 🔗 Documentos relacionados
- [[taskoro-decisao-stack-portfolio]] — a decisão de stack em detalhe, com o critério geral de quando aceitar desvio
- [[sequencia-mestra-completa-desde-o-inicio]] — onde este sistema entra na ordem real de estudo
- [[revisao-stack-tecnologica]] — critério geral de desvio de stack, aplicado aqui
- [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] — posição deste sistema na trilha de estudo
