---
tags: [transversal, portfolio-ams]
tipo: regra-transversal
status: completo
---

# Auditoria de Escalabilidade e Segurança Financeira — Portfólio Aura

**Pergunta que este documento responde:** os sistemas já planejados suportam vender produto e serviço para todo o Brasil, em volume, sem bug e sem problema financeiro?

**Resposta honesta antes de entrar no detalhe:** a arquitetura que você já fixou (Clean Architecture, `tenant_id` + RLS, PostgreSQL, Redis, Docker, aura-licensing) é uma base sólida e correta para isso — mas "suportar escala" não é uma propriedade que a arquitetura garante sozinha, é uma lista específica de mecanismos que precisam existir por cima dela. Nenhum sistema do mundo é livre de bug garantido; o que dá pra garantir é que as categorias de erro que **custam dinheiro de verdade** (vender o mesmo estoque duas vezes, cobrar o cliente duas vezes, perder uma venda por falha de rede) tenham proteção específica. Esta auditoria separa o que já está coberto do que ainda não está.

---

## 1. O que já está bem resolvido na base atual

| Fundamento | Por que já ajuda a escalar |
|---|---|
| **Clean Architecture + DDD** | Separação de camadas evita que regra de negócio fique espalhada — bug de escala geralmente nasce de lógica duplicada em lugares diferentes, e isso já é estruturalmente evitado |
| **`tenant_id` + Row-Level Security** | Isolamento correto entre clientes/lojas desde a base do banco, não só na aplicação — evita a categoria de bug mais grave em multi-tenant (vazamento de dado entre contas) |
| **Redis para cache/sessão** | Reduz carga direta no banco em picos de acesso |
| **Docker + GitHub Actions** | Deploys reproduzíveis e testáveis — reduz "funciona na minha máquina" na hora de escalar time/servidores |
| **`aura-licensing` com escada de penalidade graduada** | Evita que falha de pagamento vire corte binário abrupto (o que geraria disputa e reembolso) — já é uma decisão de design pensando em segurança financeira |

---

## 2. Riscos reais que ainda precisam de mecanismo explícito

Esta é a parte que importa mais — não são falhas do que você já fez, são lacunas que qualquer sistema nesse estágio de planejamento naturalmente ainda tem, e que precisam virar requisito antes de operar em volume nacional.

### 2.1 Concorrência de estoque entre canais (o risco mais provável de virar prejuízo real)
**O problema:** você já tem estoque compartilhado entre loja física, loja online e reserva de OS (AM Consertta), e entre loja e Delivery (AM Kaixara). Sem controle de concorrência explícito, dois canais podem vender a última unidade do mesmo item ao mesmo tempo — isso não é hipotético, é o bug mais comum em sistema de estoque multicanal, e o resultado é literalmente vender algo que você não tem, com reembolso e cliente insatisfeito.
**O que falta:** controle de concorrência otimista (versionamento de linha) ou reserva pessimista com lock de curta duração no momento do checkout, em toda operação que decrementa estoque — não é uma feature nova, é um requisito não funcional que precisa estar em cada sistema que mexe em estoque (AM Kaixara, AM Consertta, AuraVet, Loja Virtual, Delivery).

### 2.2 Idempotência em pagamento e webhook de gateway
**O problema:** gateways de pagamento (Pix, cartão) confirmam transação por webhook, e webhooks podem chegar duplicados ou atrasados por natureza da própria infraestrutura de rede — isso é comportamento normal do protocolo, não uma falha do gateway. Sem tratamento, um webhook duplicado pode gerar cobrança dupla ou baixa dupla de estoque.
**O que falta:** toda operação disparada por webhook de pagamento precisa de chave de idempotência (processar o mesmo evento duas vezes deve ter o mesmo efeito de processar uma vez só) — isso não estava formalizado em nenhum dos documentos de RF/RNF revisados até agora.

### 2.3 Falta de fila/processamento assíncrono para picos de venda
**O problema:** se um sistema processa pedido, baixa de estoque, emissão fiscal e notificação tudo de forma síncrona numa única requisição, um pico de vendas (ex: campanha, Black Friday, ou só o volume normal de "todo o Brasil") pode travar o checkout inteiro se qualquer uma dessas etapas ficar lenta.
**O que falta:** fila de processamento (Redis Streams, que você já cogitou para o `aura-historico`, serve bem aqui) para desacoplar "confirmar a venda pro cliente" de "processar emissão fiscal e notificação" — o cliente recebe confirmação rápida, o resto processa em segundo plano com re-tentativa automática em caso de falha.

### 2.4 Sem estratégia formal de escala de banco de dados
**O problema:** os documentos de arquitetura definem PostgreSQL, mas não há decisão registrada sobre o que fazer quando o volume de leitura crescer (múltiplos tenants, catálogo nacional) — se toda leitura for direto no banco principal, ele vira gargalo único.
**O que falta:** não é urgente agora (você não está nesse volume ainda), mas vale registrar a decisão futura: réplica de leitura, connection pooling (PgBouncer), e índices corretos por `tenant_id` desde o desenho da tabela — mais barato desenhar certo agora do que migrar depois.

### 2.5 Sem observabilidade/monitoramento formalizado
**O problema:** nenhum dos documentos revisados até agora define como você vai *saber* que algo deu errado em produção antes do cliente reclamar — isso é crítico especialmente para os riscos financeiros acima (estoque duplicado, pagamento duplicado), porque esses bugs são silenciosos até virar prejuízo acumulado.
**O que falta:** logging estruturado + alerta automático (mesmo que simples no início — um alerta no WhatsApp/e-mail quando uma reconciliação financeira não bate) antes de operar em escala nacional sem supervisão presencial constante.

### 2.6 Reconciliação financeira periódica
**O problema:** com múltiplos canais de venda e um serviço de cobrança central (`aura-licensing`), é fácil um evento se perder silenciosamente numa falha de rede pontual, sem que nada "quebre" visivelmente.
**O que falta:** uma rotina (diária ou semanal) que compara o que o gateway de pagamento diz que recebeu com o que o sistema registrou como recebido, sinalizando divergência — isso é o que realmente garante "sem problema financeiro" no sentido que você pediu, mais do que qualquer proteção só no momento da transação.

---

## 3. Isso não é urgente igual em todos os sistemas

Vale calibrar esforço pelo estágio real de cada um, não tratar tudo como emergência:

| Sistema | Prioridade de aplicar essas proteções |
|---|---|
| **AM Kaixara** | Alta — já está em desenvolvimento ativo, é onde vale corrigir a concorrência de estoque e idempotência de pagamento primeiro, antes de ir pra produção |
| **AM Consertta** | Alta — planejamento ainda fresco, mais barato incluir agora do que depois; herda diretamente o risco de estoque compartilhado do AM Kaixara |
| **AM Rotara / AuraVet / Loja Virtual** | Média — ainda em planejamento, mas sem código; dá pra já nascerem com esses requisitos formalizados, sem custo de retrabalho |
| **Momentos/Cupido** | Baixa nesse recorte específico — o risco de estoque/concorrência financeira é bem menor num produto B2C de conteúdo/assinatura do que num sistema de venda de produto físico |
| **`aura-licensing`** | Alta indireta — como ele centraliza cobrança de todos os outros, qualquer falha de idempotência aqui se propaga para o portfólio inteiro; é o candidato certo pra receber a reconciliação financeira periódica (item 2.6) como responsabilidade própria dele |

---

## 4. O que fazer com isso na prática

Não é uma lista de "features" — é uma lista de **requisitos não funcionais transversais** que precisam entrar no documento de RF/RNF de cada sistema que ainda não tem código escrito, e virar item de revisão técnica no que já está em desenvolvimento (AM Kaixara). Sugiro:

1. Criar um documento único de **"Requisitos Não Funcionais Transversais de Escala e Segurança Financeira"**, com os 6 itens da seção 2 detalhados como RNF formais (com ID, igual ao padrão que você já usa) — e referenciar esse documento a partir de todos os outros, em vez de repetir o conteúdo em cada um
2. Revisar o AM Kaixara (que já está em código) contra os itens 2.1 e 2.2 antes de avançar mais sprints — são os dois com maior custo de retrofit depois de pronto
3. Os demais sistemas (ainda em papel) simplesmente herdam esse documento transversal por referência, sem precisar reescrever nada

Quer que eu já monte esse documento de RNF transversal agora, no mesmo padrão dos outros (com IDs formais), para você plugar em cada sistema?
