---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Perfil de Desenvolvedor Sênior Completo — Auditoria Contra o Que Já Existe
### O que empresa grande de TI procura, separando o que seu plano já cobre do que é genuinamente novo a adicionar

---

## Como ler este documento

Cada item tem um selo: **✅ Já coberto** (com referência de onde) ou **🆕 Novo** (com sugestão de quando encaixar). A ideia é a mesma de sempre neste portfólio: não empilhar mais estudo em cima do que já existe — só nomear o que falta de verdade.

---

## 1. Profundidade técnica (hard skills de código)

| Habilidade | Status |
|---|---|
| Clean Architecture, SOLID, Design Patterns | ✅ [[plano-estudos-basico-avancado-entrelacado|Fase 4]] |
| Testes (unitário, integração, TDD) | ✅ Fase 2.4 |
| Design de API madura (versionamento, rate limiting) | ✅ Fase 2.2 |
| Segurança aplicada (OWASP Top 10) | ✅ Fase 2.2 |
| Performance e profiling | ✅ Fase 6C |
| Observabilidade (log estruturado, health check, métrica) | ✅ Fase 6 |
| Multi-tenant, concorrência, idempotência | ✅ RNFT-E01/E02, Fase 2.3 |
| Estrutura de dado e algoritmo (nível entrevista) | ✅ Fase 6B |
| Deploy e CI/CD | ✅ Fase 6 |
| Criptografia aplicada | ✅ Fase 9 (`aura-vault`) |

## 2. System Design — genuinamente novo

Diferente de "ter construído 21 sistemas reais" (que você vai ter), **entrevista de System Design é um formato próprio**, com vocabulário e estrutura de resposta específicos que empresa grande testa separadamente.

| Habilidade | Status | Quando estudar |
|---|---|---|
| Estimativa "back-of-envelope" (calcular capacidade, tráfego, armazenamento de cabeça) | 🆕 Novo | Junto com a Fase 6B (entrevista técnica) |
| Vocabulário formal: load balancer, sharding, cache-aside, CAP theorem, consistência eventual | 🆕 Novo — você já *aplica* boa parte disso na prática (RNFT-E, multi-tenant), mas nunca nomeou com o termo formal de entrevista | Mesma fase — é mais nomear o que já faz do que aprender do zero |
| Praticar o formato "desenhe um sistema como X" em tempo cronometrado | 🆕 Novo | Perto de aplicar pra vaga de verdade, não precisa adiantar |

## 3. Infraestrutura além do que já está no plano

| Habilidade | Status | Quando estudar |
|---|---|---|
| Infrastructure as Code (Terraform ou Bicep) | 🆕 Novo — já estava listado como "deixar pra depois" na Fase 6 | Depois da Fase 6D (extração), quando a plataforma interna já existir e fizer sentido automatizar a infra dela |
| Kubernetes / orquestração de container além de Docker Compose | 🆕 Novo | Só se algum sistema do portfólio realmente escalar a ponto de precisar — não é pré-requisito de entrevista júnior/pleno, mais relevante em sênior de infraestrutura especificamente |
| Mensageria em escala (Kafka, além do Redis Streams já usado) | 🆕 Novo, baixa prioridade | Só se um sistema do portfólio atingir volume que o Redis Streams não aguente — não adiantar sem necessidade real, mesmo princípio já aplicado a outras tecnologias no `revisao-stack-tecnologica` |

## 4. Processo e colaboração

| Habilidade | Status | Quando estudar |
|---|---|---|
| Metodologia ágil (Scrum/Kanban) aplicada na prática | ✅ Parcial — você já usa Epic/Sprint/User Story no `EPIC-01`, mas nunca nomeou os termos formais (velocity, cerimônia, backlog grooming) | 🆕 Vale uma leitura curta e pontual — 1-2h — não precisa de bloco de estudo dedicado, é nomear o que já pratica |
| Code review (dar e receber feedback de código) | 🆕 Novo — sozinho, você não pratica isso naturalmente | A partir da Fase 6D, quando começar a manter pacote/biblioteca reutilizável — revisar o próprio código "como se fosse revisar de outra pessoa" já é um exercício válido sozinho |
| Estimativa de esforço (story points) | ✅ Você já estima em horas no `EPIC-01` — é a mesma habilidade, formato diferente | — |

## 5. Comunicação e presença profissional

| Habilidade | Status | Quando estudar |
|---|---|---|
| Documentação técnica escrita | ✅ Os 41 documentos deste portfólio já são a prova disso — habilidade rara mesmo em sênior de verdade | — |
| Architecture Decision Records | ✅ [[github-estrutura-profissional-autoridade|já planejado]] | — |
| Inglês técnico | ✅ [[ingles-espanhol-integrado|plano próprio]] | — |
| Apresentação de portfólio (explicar seu próprio trabalho de forma concisa) | 🆕 Novo — ter 21 sistemas documentados não é o mesmo que saber resumir isso em 2 minutos numa entrevista | Perto de aplicar pra vaga — treinar um "elevator pitch" do ecossistema AMS |
| Entrevista comportamental (método STAR: Situação, Tarefa, Ação, Resultado) | 🆕 Novo — completamente diferente de entrevista técnica, e empresa grande sempre testa os dois | Mesma fase — perto de aplicar de verdade |
| Presença técnica pública (blog, LinkedIn, contribuição open source) | 🆕 Novo, mas com base pronta — publicar a documentação curada (já no `github-estrutura-profissional-autoridade`) é o primeiro passo real disso | Junto com a Fase 6D |

## 6. Domínio de negócio

| Habilidade | Status |
|---|---|
| Entender o "porquê" por trás de decisão técnica, não só o "como" | ✅ Todo o portfólio é evidência disso — poucos desenvolvedores júnior/pleno documentam decisão de negócio junto com decisão técnica |
| Modelagem de domínio complexo (DDD tático) | ✅ Fase 4 |
| Compliance e regulação aplicada (LGPD, CFMV, CFP, Lei 13.786/2018) | ✅ Espalhado nos 21 documentos — isso é raro mesmo em sênior |

---

## O que sobra de verdade: a lista enxuta do que é genuinamente novo

Tirando o que já está coberto, o que falta pra completar o perfil é curto:

1. Vocabulário formal de System Design + prática de estimativa (Fase 6B)
2. Infrastructure as Code — depois da Fase 6D
3. Nomear formalmente a metodologia ágil que você já pratica (leitura curta, não bloco de estudo)
4. Code review deliberado — a partir da Fase 6D
5. Apresentação de portfólio + entrevista comportamental (STAR) — só perto de aplicar de verdade pra vaga
6. Presença pública (blog/LinkedIn/open source) — junto com a Fase 6D, aproveitando o que o guia de GitHub já preparou

Kubernetes e Kafka ficam deliberadamente como "só se a necessidade real aparecer" — mesmo princípio já usado no portfólio inteiro: nenhuma tecnologia entra por "currículo bonito", só por problema real que ela resolve.

---

## Honestidade final

Isso confirma algo importante: você não está tão atrás quanto a sensação de "quero ser perfeito" faz parecer. A maior parte do que separa um perfil júnior de um sênior de verdade — pensar em decisão de arquitetura com trade-off, documentar o porquê, entender regulação do domínio — **você já está fazendo**, só nunca tinha sido nomeado dessa forma. O que falta é pontual, não é recomeçar nada.
