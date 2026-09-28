---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Horaria — Documento de Projeto Final (Nome provisório)
### Sistema de Agendamento Genérico para Serviço Pessoal (salão, clínica, academia, psicólogo)

Segue a estrutura fixa do [[template-documento-projeto-final]].

---

## 1. Visão do produto

Motor genérico de agendamento + histórico de cliente + venda de produto + assinatura recorrente, generalizado do mesmo padrão validado no AuraVet, removendo tudo que é específico de veterinária. Serve salão de beleza, clínica de estética, academia, consultório de psicologia, personal trainer, esteticista autônoma — qualquer negócio baseado em atendimento marcado com cliente recorrente.

**Diferencial de inovação:** diferente do AuraVet (nicho profundo, com verticais regulatórias complexas como reprodução animal), aqui o valor não está em profundidade de nicho — está em mercado amplo com implantação rápida e pacote de funcionalidade honesto pro que a maioria desses negócios realmente usa no dia a dia, sem custo de sistema genérico caro (tipo grandes plataformas de gestão de salão/academia com contrato pesado).

---

## 2. Funcionalidades completas (estado final)

### 2.1 Cadastro e agendamento
- Cadastro de cliente
- Agendamento self-service (cliente marca sozinho) e por recepção, com validação de conflito de horário/profissional
- Lembrete automático de agendamento via `aura-notifications`

### 2.2 Histórico e ficha por segmento
- Ficha de anamnese (estética/salão), ficha de treino (academia/personal), **prontuário psicológico** (psicologia) — mesmo motor de histórico do AuraVet, com campos específicos habilitados conforme o segmento contratado
- **Módulo de prontuário psicológico com regras próprias, mais rígidas que o padrão do resto do sistema** (ver seção 5 e 6) — retenção mínima de 5 anos após encerramento do atendimento (podendo chegar a 20 anos conforme orientação do CFP), acesso restrito exclusivo ao profissional responsável, nunca compartilhado com outro profissional do mesmo estabelecimento sem autorização formal

### 2.3 Pacote e assinatura
- Pacote de sessões pré-pago (ex: 10 sessões de fisioterapia/estética)
- Assinatura recorrente (plano mensal de academia, plano de manutenção de salão)

### 2.4 Loja de produto
- Venda de cosmético, suplemento, produto de manutenção — mesmo padrão de loja já validado em outros sistemas, com envio via `aura-logistics` quando aplicável

### 2.5 Multi-profissional e comissionamento
- Suporte a estabelecimento com múltiplos profissionais, cada um com agenda própria
- Comissionamento por profissional/serviço — mesmo padrão do AM Consertta

### 2.6 Portal do cliente
- Agendamento, histórico de sessão (exceto conteúdo sigiloso de prontuário psicológico, que segue regra própria), compra de pacote/produto

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Cadastro de cliente com agendamento self-service e por recepção | Reduz carga de recepção e permite o cliente marcar fora do horário comercial |
| RF02 | Validação de conflito de horário/profissional na agenda | Evita dois clientes marcados no mesmo horário com o mesmo profissional |
| RF03 | Lembrete automático de agendamento via `aura-notifications` | Reduz falta/atraso, problema comum e caro para negócio de horário marcado |
| RF04 | Ficha de histórico configurável por segmento (anamnese, treino, prontuário) | Um único motor atende múltiplos tipos de negócio sem reescrever para cada um |
| RF05 | Prontuário psicológico com controle de acesso exclusivo ao profissional responsável, retenção mínima de 5 anos | Cumpre a Resolução CFP nº 01/2009 e nº 06/2019 — sigilo profissional não é opcional, é obrigação ética e legal |
| RF06 | Registro de entrega de cópia de prontuário psicológico ao paciente/responsável, com confirmação de recebimento | Cumpre exigência específica do CFP de que a entrega seja registrada e assinada |
| RF07 | Venda de pacote de sessão pré-pago, com controle de saldo de sessão restante | Formaliza o modelo de venda mais comum de estética/fisioterapia |
| RF08 | Assinatura recorrente com cobrança automática | Sustenta receita previsível, mesmo padrão de plano de saúde pet do AuraVet |
| RF09 | Loja de produto integrada, com envio via `aura-logistics` quando aplicável | Reaproveita módulo compartilhado em vez de reconstruir |
| RF10 | Agenda multi-profissional com comissionamento por atendimento | Permite crescer além de um profissional autônomo sem trocar de sistema |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Cliente
- **Cadastro:** self-service
- **Uso:** portal do cliente (2.6)
- **Suporte:** canal do estabelecimento, mesma lógica já aplicada a outros sistemas do portfólio

### 4.2 Profissional (esteticista, personal trainer, psicólogo, etc.)
- **Cadastro:** criado pelo dono do estabelecimento, ou self-service se for autônomo
- **Uso:** agenda própria, ficha de atendimento — **no caso do psicólogo, acesso ao prontuário é exclusivo dele, mesmo que outros profissionais do mesmo estabelecimento tenham acesso administrativo ao restante do sistema**
- **Suporte:** canal do dono do estabelecimento, ou direto com o Grupo AMtech se for autônomo

### 4.3 Dono do estabelecimento/administrador
- **Cadastro:** self-service ou onboarding assistido
- **Uso:** gestão financeira, alocação de profissional — **sem acesso ao conteúdo do prontuário psicológico de nenhum paciente, mesmo sendo administrador do sistema** (ver seção 6)
- **Suporte:** canal com o Grupo AMtech Digital

### 4.4 Suporte técnico interno
- Reaproveita o `aura-support` já formalizado — com uma exceção importante: **suporte técnico não deve ter acesso ao conteúdo de prontuário psicológico para diagnosticar problema**, só a metadado (existe registro, data, sem conteúdo). Isso é uma restrição específica deste sistema que o `aura-support` precisa respeitar quando consultado sobre este domínio.

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no AM Horaria | Para que serve |
|---|---|---|
| RNFT-E01 (concorrência) | Agendamento não pode aceitar dois clientes no mesmo horário/profissional simultaneamente | Mesmo princípio já aplicado a estoque e a reserva de área comum do AM Predara |
| RNFT-E02 (idempotência de pagamento) | Cobrança de assinatura e de pacote de sessão | Evita cobrança duplicada em reenvio de webhook |
| RNFT06 (LGPD) | Dado de saúde/estética é categoria sensível | Cumpre obrigação legal geral |
| **Sigilo profissional psicológico (próprio, mais rígido que o RNFT06 geral)** | Prontuário psicológico deve ser tecnicamente isolado — nem o administrador do sistema, nem outro profissional do estabelecimento, nem o suporte técnico têm acesso ao conteúdo, só o psicólogo responsável | É a exigência mais rígida de todo o portfólio em termos de isolamento de dado — mais restrita até que o prontuário veterinário do AuraVet, porque aqui a lei protege sigilo entre profissional e paciente mesmo dentro da própria instituição |
| Retenção de prontuário psicológico (próprio) | Mínimo 5 anos após encerramento do atendimento, podendo chegar a 20 anos conforme orientação do CFP e a Lei nº 13.787/2018 | Cumpre prazo legal de guarda — descartar antes do prazo é falta ética documentada |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no AM Horaria |
|---|---|
| Isolamento de prontuário psicológico | **É o requisito de segurança mais importante deste sistema.** Tecnicamente, o prontuário psicológico precisa estar numa camada de acesso separada até do próprio administrador do estabelecimento — diferente de qualquer outro dado do portfólio, onde o dono do negócio normalmente tem visão completa. **RESOLVIDO/atualizado:** implementado via `aura-vault`, que já formaliza exatamente essa restrição (RF07 daquele documento: impede até o `aura-support` de acessar conteúdo protegido por categoria restrita) |
| Dados | Ficha de anamnese/treino é sensível, mas de nível de proteção padrão (RNFT06); prontuário psicológico exige camada adicional (acima) |
| Auditoria externa | Prioridade alta especificamente pelo módulo de psicologia — um vazamento de prontuário psicológico é o tipo de falha com maior dano possível a uma pessoa de todo o portfólio, mais até que dado financeiro |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** SaaS puro, sem componente físico.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Dado o isolamento exigido pelo módulo de psicologia (seção 6), vale considerar segregação de banco/schema para esse módulo específico, não só controle de acesso em nível de aplicação — defesa em profundidade real, não só uma camada.

---

## 9. Modelo de receita — todas as formas de venda

| Fonte | Modelo |
|---|---|
| Assinatura SaaS por profissional ou por estabelecimento | Mensalidade recorrente, escalando com o número de profissionais ativos |
| Taxa de setup/onboarding | Cobrança única na implantação |
| Módulo de prontuário psicológico | Pode ser precificado como add-on de conformidade, dado o nível extra de proteção exigido — justifica ticket mais alto que o módulo de anamnese/treino padrão |
| Loja de produto | Comissão/margem sobre venda de cosmético/suplemento |
| **Segmentação por vertical** | Pacotes diferentes por tipo de negócio (salão, academia, psicologia) — mesmo produto técnico, precificação e nome comercial adaptados por segmento |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização completa deste sistema, adiado conscientemente até a infraestrutura compartilhada estar pronta — condição já cumprida.

---

## 11. Pendências e decisões em aberto

1. **Arquitetura de segregação do módulo de psicologia** (seção 8) — em grande parte RESOLVIDO pelo `aura-vault` (controle de acesso reforçado por categoria de dado, RF03 daquele documento); resta só decidir se ainda vale segregação física de schema além do que o `aura-vault` já garante, ou se é redundante.
2. **Validação por psicólogo ou consultor jurídico especializado em ética profissional** antes de tratar o RF05/RF06 como pronto para produção — mesmo padrão de cautela já aplicado ao AM Canteira (advogado) e sugerido ao AM Saberia (gestão educacional).
3. **Nome comercial por vertical** (seção 9) — decisão de marketing, não técnica, mas relevante para a estratégia de venda segmentada.
4. **Provedor de gateway de pagamento** — mesma pendência transversal do restante do portfólio.
