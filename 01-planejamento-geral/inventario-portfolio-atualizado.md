---
tags: [planejamento, portfolio-ams]
tipo: planejamento
status: completo
---

# Inventário do Portfólio — Atualizado
### O que é sistema de negócio, o que é serviço compartilhado, e o que é documento de regra transversal

---

## 1. Sistemas de negócio — vendidos a um cliente, que atende o cliente final dele

| # | Sistema | Documento | Status |
|---|---|---|---|
| 1 | **AM Kaixara** | `kaixara-documento-projeto-final.md` | ✅ Completo — único em desenvolvimento ativo (Sprint 3-4) |
| 2 | **AM Rotara** | `rotara-documento-projeto-final.md` | ✅ Completo — planejamento, sem código |
| 3 | **AM Rendara** | `rendara-documento-projeto-final.md` | ✅ Completo — planejamento, sem código |
| 4 | **AuraVet** | `petara-requisitos-completos.md` | ✅ Completo — planejamento, sem código. Tem também `AuraVet-Apresentacao-Comercial.docx` (material comercial pra enviar a clínicas interessadas) |
| 5 | **AM Consertta** | `consertta-sistema-assistencia-tecnica.md` | ✅ Completo — planejamento, sem código |
| 6 | **Momentos/Cupido** | `vynla-documento-projeto-final.md` | ✅ Completo — existe protótipo funcional fora do stack padrão (Node/SQLite), pendência de migração registrada |
| 7 | **Loja Virtual** | `vendra-documento-projeto-final.md` | ✅ Completo — módulo dependente do AM Kaixara, nunca vendido isolado |
| 8 | **AM Predara** | `predara-documento-projeto-final.md` | ✅ Completo — único sistema com componente de controle de acesso físico |
| 9 | **AM Canteira** | `canteira-documento-projeto-final.md` | ✅ Completo — maior exposição jurídica do portfólio, recomendação de revisão por advogado registrada |
| 10 | **Gestão escolar/cursinho (AM Saberia)** | `saberia-documento-projeto-final.md` | ✅ Completo — o mais pessoal do portfólio, já nasce com as 180 apostilas como conteúdo embutido |
| 11 | **Agendamento genérico de serviço pessoal (AM Horaria)** | `horaria-documento-projeto-final.md` | ✅ Completo — o módulo de prontuário psicológico tem o requisito de isolamento de dado mais rígido de todo o portfólio |
| 12 | **AM Taskoro** | `taskoro-documento-projeto-final.md` | ✅ Completo — revisado: GraphQL via HotChocolate dentro do .NET (não mais React/Node/GraphQL separado), decisão registrada com o critério de quando um desvio de stack se justifica |
| 13 | **AM Projeta** | `projeta-documento-projeto-final.md` | ✅ Completo — diagnóstico de setup e geração de arquitetura por IA; encontrado numa conversa separada, formalizado agora; origina a série transversal RNFT-IA01-04 |

**Subtotal: 13 de 13 sistemas de negócio documentados.** Somando os 10 serviços compartilhados (seção 2), o portfólio completo soma **23 itens** — 13 sistemas de negócio + 10 serviços compartilhados, não 23 sistemas de negócio.

---

## 2. Serviços compartilhados — infraestrutura interna, consumida por vários sistemas ao mesmo tempo, nunca vendida diretamente ao cliente final (exceto quando licenciados como produto B2B à parte)

| # | Serviço | Documento | Status |
|---|---|---|---|
| 1 | **`aura-licensing`** | `aura-licensing-documento-projeto-final.md` | ✅ Completo — motor de cobrança/módulo central, único SPOF do portfólio |
| 2 | **`aura-goals`** | `aura-goals-documento-projeto-final.md` | ✅ Completo — compartilhado entre AM Rendara e Momentos/Cupido |
| 3 | **`aura-historico`** | `aura-historico-documento-projeto-final.md` | ✅ Completo — Clojure/Datomic, fora do stack .NET padrão |
| 4 | **`aura-analytics`** | `aura-analytics-documento-projeto-final.md` | ✅ Completo — Python/FastAPI, fora do stack .NET padrão |
| 5 | **`aura-copilot`** | `aura-copilot-documento-projeto-final.md` | ✅ Completo — o mais em estágio de ideia, várias decisões de provedor ainda pendentes |
| 6 | **`aura-identity`** | `aura-identity-documento-projeto-final.md` | ✅ Completo — maior prioridade real, elimina duplicação de autenticação em 7 sistemas; segundo SPOF do portfólio |
| 7 | **`aura-notifications`** | `aura-notifications-documento-projeto-final.md` | ✅ Completo — elimina duplicação de WhatsApp/push/e-mail em pelo menos 5 sistemas |
| 8 | **`aura-support`** | `aura-support-documento-projeto-final.md` | ✅ Completo — primeiro sistema do portfólio desenhado desde o início para múltiplos operadores internos |
| 9 | **`aura-logistics`** | `aura-logistics-documento-projeto-final.md` | ✅ Completo — único serviço compartilhado com dependência física indireta (produto enviado é real) |
| 10 | **`aura-vault`** | `aura-vault-documento-projeto-final.md` | ✅ Completo — nasceu da análise cruzada de AM Rendara, AuraVet, AM Horaria e AM Canteira reimplementando proteção de dado sensível cada um à sua maneira; junto com o `aura-identity`, é o núcleo de segurança crítica do portfólio |

**Subtotal: 10 de 10 serviços compartilhados documentados. Nenhum pendente.**

---

## 3. Documentos transversais — não são sistemas, são regras que os sistemas referenciam

| Documento | O que define |
|---|---|
| `template-documento-projeto-final.md` | A estrutura fixa de 11 seções que todo Documento de Projeto Final segue |
| `rnf-transversais-escala-seguranca-financeira.md` | RNFT-E01 a E06 — concorrência de estoque, idempotência de pagamento, fila, escala de banco, observabilidade, reconciliação |
| `distribuicao-licenciamento-seguranca.md` | RNFT-S01 a S06 — instalador assinado, licenciamento com tolerância offline, conexão entre sistemas, segurança de código/rede/dados, auditoria externa |
| `rnf-transversais-design-tema.md` | RNFT-D01 a D07 — paleta padrão Aura, cores semânticas fixas, escopo de personalização por tipo de tela |
| `auditoria-escalabilidade-seguranca-financeira.md` | O documento que originou a série RNFT-E — análise dos riscos antes de virarem requisito formal |

---

## 4. Documentos de planejamento geral — visão do portfólio como um todo, não de um sistema específico

| Documento | Conteúdo |
|---|---|
| `plano-mestre-frentes-alan.md` | O documento raiz — todas as frentes de renda/negócio, prioridade de abertura e execução, incluindo docência, assistência técnica, freela, dropshipping |
| `status-planejamento-portfolio.md` | Levantamento histórico do que já existia documentado antes desta rodada de consolidação (24 documentos do índice mestre original) |
| `acao-imediata-portfolio.md` | O que fazer agora vs. curto prazo vs. médio prazo, e o que **não** fazer agora |

---

## 5. Ideias registradas, conscientemente não desenvolvidas

- **Gestão de imobiliária/locação** (proprietário, inquilino, imobiliária) — mencionada durante o planejamento do AM Predara/AM Canteira como segundo lugar de reaproveitamento (OS para manutenção do imóvel, cobrança recorrente de aluguel), mas nunca formalizada. Registrada aqui para não se perder de novo, sem compromisso de desenvolvimento.

---

## 6. Fora do escopo, de propósito

- **AuraTest** — projeto de prática/aprendizado pessoal, nunca entra no padrão de Documento de Projeto Final, porque não é produto comercial.

---

## Resumo executivo

| Categoria | Completo | Pendente | Total |
|---|---|---|---|
| Sistemas de negócio | 13 | 0 | 13 |
| Serviços compartilhados | 10 | 0 | 10 |
| Documentos transversais (regra) | 6 | 0 | 6 |
| **Portfólio de sistemas/serviços** | **23** | **0** | **23** |

**Portfólio 100% documentado.** Uma ideia registrada sem desenvolvimento (gestão de imobiliária/locação, seção 5) e as decisões-bloqueio já identificadas (migração de stack do Momentos/Cupido, validações jurídicas/éticas do AM Canteira/AM Saberia/AM Horaria, escolhas de fornecedor do `aura-licensing` e agora do `aura-vault`) são o que resta antes de qualquer sistema ir a código com segurança total.

---

## 🔗 Documentos relacionados
- [[passo-a-passo-mestre-desde-o-inicio]] — o plano de execução que usa este inventário como ponto de partida
- [[plano-mestre-frentes-alan]] — o documento raiz que originou este inventário
- [[template-documento-projeto-final]] — a estrutura que todo item completo aqui segue
