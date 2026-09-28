---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-licensing — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Este é o primeiro serviço compartilhado do portfólio a receber RF/RNF formal — até agora só existia descrito em arquitetura.

---

## 1. Visão do produto

Motor central de licenciamento e cobrança modular, consumido por todos os sistemas do portfólio (AM Kaixara, Delivery, AM Rendara, AuraVet, AM Consertta, Momentos/Cupido, Loja Virtual). Sabe quais módulos cada `tenant_id` tem ativo, cobra por eles, e aplica penalidade graduada em caso de inadimplência.

**Diferencial de inovação:** a maioria dos SaaS pequenos trata licenciamento como on/off binário por produto inteiro. Aqui o licenciamento é **por módulo**, com grafo de dependência (não deixa ativar um módulo sem o pré-requisito técnico dele) — é o que viabiliza toda a estratégia de pacotes comerciais do restante do portfólio. Sem esse motor, nenhum outro sistema consegue vender parte de si mesmo.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Registro e verificação
- Registro de módulo ativo por `tenant_id`, por sistema
- Middleware de verificação por requisição (consumido por todos os sistemas), com cache local de 24-48h para não bloquear cliente por indisponibilidade momentânea do próprio `aura-licensing`

### 2.2 Grafo de dependência
- Validação de que uma combinação de módulos é tecnicamente consistente antes de provisionar (ex: não ativa um módulo avançado sem o módulo-base do qual ele depende)

### 2.3 Cobrança
- Integração com plataforma de cobrança recorrente (Stripe Billing/Vindi/Iugu/Asaas — decisão final pendente)
- Tentativa automática em falha de pagamento (dunning)
- Prorrateamento em troca de plano

### 2.4 Escada de penalidade por inadimplência
- Status graduado: ativo → atraso → modo restrito → suspenso → cancelado — nunca corte binário imediato

### 2.5 Conta única de cliente (adicionado no documento de Distribuição/Segurança)
- Identidade que sabe quais produtos do portfólio um mesmo cliente possui, viabilizando conexão entre sistemas (ex: AM Kaixara + AM Rendara do mesmo dono)
- Consentimento explícito e credencial de escopo mínimo para cada conexão entre sistemas

### 2.6 Reconciliação financeira (RNFT-E06)
- Rotina periódica comparando total recebido segundo o gateway vs. total registrado internamente, sinalizando divergência

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Registrar módulo ativo por `tenant_id` e por sistema | Base de dado que todo o resto do serviço depende |
| RF02 | Validar grafo de dependência antes de ativar um módulo | Impede provisionar combinação tecnicamente inconsistente |
| RF03 | Expor middleware de verificação, com cache local de 24-48h | Sistema consumidor não trava se o `aura-licensing` ficar momentaneamente indisponível |
| RF04 | Integrar com plataforma de cobrança recorrente, com tentativa automática em falha | Reduz perda de receita por falha pontual de cartão, sem intervenção manual |
| RF05 | Aplicar escada de penalidade graduada em inadimplência | Evita corte abrupto que gera disputa e cancelamento evitável |
| RF06 | Manter conta única de cliente, vinculando múltiplos `tenant_id`/produtos à mesma pessoa | Viabiliza a conexão entre sistemas do portfólio comprados pelo mesmo cliente |
| RF07 | Registrar consentimento explícito antes de qualquer conexão entre dois sistemas | Cumpre LGPD e evita ligação automática indesejada |
| RF08 | Executar reconciliação periódica entre gateway e registro interno | Detecta evento de pagamento perdido silenciosamente |
| RF09 | Expor API para os sistemas consultarem/alterarem pacote comercial contratado | Viabiliza upgrade/downgrade self-service, sem intervenção manual sua |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Cliente final (via painel de qualquer sistema do portfólio)
- **Cadastro:** herdado do sistema de origem (não tem cadastro próprio no `aura-licensing`)
- **Uso:** contrata/altera pacote, vê fatura, conecta outro produto do portfólio
- **Suporte:** canal do sistema de origem, não um canal próprio do `aura-licensing`

### 4.2 Você (dono do portfólio)
- **Uso:** visão consolidada de receita recorrente de todo o portfólio, status de inadimplência agregado
- **Lacuna:** não existe hoje um painel formal para isso — é o painel de suporte/operação interna transversal, aqui com responsabilidade adicional de visão financeira agregada

### 4.3 Suporte técnico interno
- Mesma lacuna recorrente do portfólio inteiro — aqui com peso extra, porque é o único sistema com visão financeira de todos os outros ao mesmo tempo

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-licensing | Para que serve |
|---|---|---|
| RNFT-E02 (idempotência de pagamento) | Crítico — é o motor central de cobrança de todo o portfólio | Falha de idempotência aqui se propaga para todos os sistemas consumidores |
| RNFT-E06 (reconciliação) | É o **dono** deste requisito para todo o portfólio, não só reporta dado | Centraliza a única fonte de verdade de "quanto realmente entrou" |
| RNFT-S03/S04 (conexão entre sistemas) | É o serviço que implementa o consentimento e o escopo mínimo para todos os outros | Sem isso formalizado aqui, cada sistema reimplementaria a regra de forma inconsistente |
| Alta disponibilidade | Indisponibilidade prolongada bloqueia verificação de módulo em todo o portfólio simultaneamente | É o único ponto de falha único (SPOF) de todo o ecossistema — cache local (RF03) mitiga, mas não elimina |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-licensing |
|---|---|
| Dados | Concentra dado de cobrança de todos os clientes de todos os sistemas — é, depois do AM Rendara, o segundo maior alvo de valor para um atacante |
| Rede/API | Todo sistema consumidor autentica com credencial própria, nunca compartilhada entre sistemas — comprometer um sistema não deve comprometer o acesso de outro ao `aura-licensing` |
| Auditoria externa (RNFT-S06) | Prioridade máxima, mesmo nível do AM Rendara — é o SPOF financeiro do portfólio inteiro |

---

## 7. Hardware, instalador e distribuição

**Não aplicável no sentido tradicional.** É um serviço interno, sem instalador nem distribuição direta ao cliente final. **Mas há uma forma de venda que muda isso** — ver seção 9.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml` de produção, pipeline GitHub Actions. Dado o papel de SPOF (seção 5), vale considerar deploy com redundância (mais de uma instância) antes dos outros sistemas do portfólio, já que uma falha aqui afeta todos ao mesmo tempo.

---

## 9. Modelo de receita — incluindo forma de venda nova

O `aura-licensing` não é vendido ao cliente final — ele é o motor que cobra pelos outros produtos. **Mas ele mesmo pode virar produto**, vendido a **outras empresas de software** que também querem vender por módulo e não têm esse motor pronto:

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — habilita a receita recorrente de todo o resto do portfólio |
| **Licenciamento white-label do próprio `aura-licensing`** | Venda como produto B2B para outras empresas de software que precisam de billing modular e não querem construir do zero — mensalidade ou percentual sobre volume processado |

Essa segunda forma de venda é genuinamente nova neste documento — nenhum outro serviço do portfólio até agora tinha esse ângulo de "vender a própria infraestrutura interna".

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Existe descrição arquitetural detalhada (registro de módulo, grafo de dependência, middleware, escada de penalidade), mas este é o primeiro documento a formalizar RF/RNF.

---

## 11. Pendências e decisões em aberto

1. **Escolha da plataforma de cobrança recorrente** (Stripe Billing/Vindi/Iugu/Asaas) — decisão pendente há tempo, agora com maior urgência por ser pré-requisito de RF04.
2. **Redundância de deploy** (seção 8) — decisão de infraestrutura específica, dado o papel de SPOF.
3. **Avaliar seriamente o licenciamento white-label** (seção 9) — é uma linha de negócio nova, vale decidir se entra no roadmap comercial ou fica só como uso interno por enquanto.
4. **Painel de visão financeira agregada** (seção 4.2) — ainda não especificado como RF formal.
