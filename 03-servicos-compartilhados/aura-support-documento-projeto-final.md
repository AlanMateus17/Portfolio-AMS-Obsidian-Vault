---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-support — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Terceiro dos 4 serviços compartilhados pendentes — a lacuna mais validada de toda a auditoria: apareceu em 9 dos 14 documentos de sistema já produzidos.

---

## 1. Visão do produto

Painel central de suporte técnico e operação interna, com visão cruzada de todos os tenants de todos os sistemas do portfólio. Resolve o problema que, sistema por sistema, sempre ficava registrado como "lacuna, sem RF formal" — em vez de resolver 9 vezes separadas, resolve uma vez, compartilhado.

**Diferencial de inovação:** diferente de uma ferramenta de suporte genérica (Zendesk, Freshdesk), este painel entende a estrutura específica do ecossistema Aura — sabe que um problema pode envolver mais de um sistema ao mesmo tempo (ex: uma meta compartilhada do `aura-goals` que envolve tanto AuraWealth quanto Momentos/Cupido), o que nenhuma ferramenta de mercado tem contexto pra fazer sem configuração manual extensa.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Visão consolidada de tenant
- Consulta rápida do estado de qualquer tenant, em qualquer sistema, sem precisar acessar banco de dado diretamente

### 2.2 Reprocessamento e correção manual
- Reatribuir pedido/OS, forçar reembolso, reprocessar sincronização travada — ações que hoje, sem esse painel, exigiriam acesso direto ao banco

### 2.3 Fila de disputa e moderação
- Reaproveita o conceito já formalizado no Momentos/Cupido (moderação de conteúdo) e no Aura Delivery (fila de disputa) — generaliza para qualquer sistema que precise de fila de revisão humana

### 2.4 Visão financeira agregada
- Reaproveita o que já foi apontado como necessário no `aura-licensing` (seção 4.2 daquele documento) — receita recorrente consolidada de todo o portfólio, status de inadimplência agregado

### 2.5 Log de auditoria de ação de suporte
- Toda ação manual feita por você (ou futura equipe) através deste painel fica registrada — quem fez o quê, quando, em qual tenant

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Consultar estado consolidado de qualquer tenant em qualquer sistema | Elimina a necessidade de acesso direto a banco de dado para diagnosticar problema relatado |
| RF02 | Reatribuir pedido/OS manualmente entre entregador/técnico/profissional | Resolve o que sai do fluxo automático — a razão de existir mais citada em todos os documentos anteriores |
| RF03 | Forçar reembolso/estorno fora do fluxo automático | Cobre o caso de disputa que o fluxo padrão de pagamento não resolve sozinho |
| RF04 | Reprocessar evento/sincronização travada entre sistemas | Reduz tempo de resolução de bug de integração sem precisar de deploy de correção emergencial |
| RF05 | Manter fila de disputa/moderação, com histórico de decisão | Generaliza o conceito já usado no Momentos/Cupido e no Delivery para qualquer sistema que precisar |
| RF06 | Exibir visão financeira agregada de receita recorrente de todo o portfólio | Dá a você (ou futuro sócio/investidor) visão de negócio sem precisar consultar sistema por sistema |
| RF07 | Registrar log de auditoria de toda ação manual feita através do painel | Rastreabilidade de quem alterou o quê — essencial se algum dia houver mais de uma pessoa com acesso a este painel |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Você (hoje, único usuário)
- **Cadastro:** acesso administrativo direto, sem fluxo de autoatendimento
- **Uso:** todas as funcionalidades da seção 2
- **Suporte:** não se aplica — você é quem presta suporte, não quem recebe

### 4.2 Futuro funcionário de suporte
- **Cadastro:** criado por você, com controle de acesso por sistema/tenant (um futuro atendente de suporte do AuraFix não precisa necessariamente ver dado do AuraWealth)
- **Uso:** mesmo painel, com escopo de acesso limitado ao que a função exige
- **Observação:** este é o primeiro documento do portfólio pensado desde o início para múltiplos operadores internos, diferente dos outros sistemas onde "suporte" ainda significa só você

### 4.3 Sistema consumidor (todos os do portfólio)
- Expõe endpoint que o `aura-support` consulta/aciona — máquina a máquina, sem usuário humano direto neste papel

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-support | Para que serve |
|---|---|---|
| RNFT07 (BOLA) | Controle de acesso por sistema/tenant deve ser rigoroso mesmo internamente — futuro atendente não deve ver além do escopo da própria função | Reduz superfície de erro/vazamento interno, não só externo |
| Log de auditoria elevado a RNF (RF07) | Toda ação deve ser rastreável de forma imutável | Este painel tem poder de alterar dado real (reembolso, reatribuição) — exige o mesmo rigor de auditabilidade de um sistema financeiro |
| RNFT06 (LGPD) | Acesso a dado de cliente para diagnóstico exige justificativa registrada, não acesso livre | Mesmo em uso interno, dado pessoal exige minimização de acesso |
| Alta disponibilidade (moderada) | Diferente do `aura-identity`/`aura-licensing`, uma indisponibilidade aqui atrasa resolução de problema, mas não impede operação principal de nenhum sistema | Prioridade de disponibilidade mais baixa que os dois SPOFs do portfólio, mas ainda relevante |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-support |
|---|---|
| Poder de ação elevado | Este painel pode alterar dado real (reembolso, reatribuição) em qualquer sistema — exige autenticação forte (2FA obrigatório, não opcional, diferente do padrão geral do `aura-identity`) |
| Controle de acesso granular | Essencial a partir do momento em que houver mais de um operador (seção 4.2) |
| Auditoria externa | Prioridade alta — é o painel com maior poder de ação sobre dado real de cliente de todo o portfólio, mesmo sendo de uso interno |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Painel web interno, sem instalador nem distribuição a cliente externo.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Acesso restrito por rede (VPN ou IP allowlist), diferente de qualquer sistema voltado a cliente externo — este nunca deveria estar publicamente acessível na internet aberta.

---

## 9. Modelo de receita

Não gera receita direta e não tem ângulo de venda B2B — diferente do `aura-identity`/`aura-licensing`, um painel de suporte interno específico da arquitetura do ecossistema Aura não é genérico o suficiente para licenciar a terceiros sem adaptação profunda, o que descaracterizaria a vantagem de reaproveitamento que o torna barato de manter aqui dentro.

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização deste serviço — mas é o mais validado de todos os 4 pendentes, dado que apareceu como lacuna repetida em 9 documentos diferentes antes de virar sistema próprio.

---

## 11. Pendências e decisões em aberto

1. **2FA obrigatório** (seção 6) — decisão já inclinada a "sim, sempre", diferente do padrão opcional do `aura-identity`; formalizar como requisito, não intenção.
2. **Modelo de controle de acesso por escopo** (4.2) — ainda não desenhado com detalhe, relevante só quando houver mais de um operador.
3. **VPN vs. IP allowlist** (seção 8) — decisão de infraestrutura de rede ainda em aberto.
4. **Prioridade de implementação real** — dado que é a lacuna mais repetida, vale considerar se este deveria vir antes do `aura-notifications` na ordem de execução, mesmo com `aura-identity` mantendo a prioridade máxima.
