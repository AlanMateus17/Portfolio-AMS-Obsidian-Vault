---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Kaixara — Especificação Técnica Completa
### Nível arquiteto/staff engineer — modelo de dados, contrato de API, fluxos, padrões de erro, threat model

---

## 1. Modelo de Dados Completo

Até agora as entidades eram citadas por nome (`Product`, `Category`, `Sale`). Aqui está o schema real, com tipo, constraint e relacionamento:

```sql
CREATE TABLE tenant (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    nome VARCHAR(200) NOT NULL,
    cnpj VARCHAR(14) UNIQUE,
    criado_em TIMESTAMPTZ NOT NULL DEFAULT now(),
    ativo BOOLEAN NOT NULL DEFAULT true
);

CREATE TABLE filial (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    nome VARCHAR(200) NOT NULL,
    endereco VARCHAR(500),
    criado_em TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE categoria (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    nome VARCHAR(120) NOT NULL,
    categoria_pai_id UUID REFERENCES categoria(id),
    UNIQUE (tenant_id, nome)
);

CREATE TABLE produto (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    filial_id UUID NOT NULL REFERENCES filial(id),
    categoria_id UUID REFERENCES categoria(id),
    sku VARCHAR(50) NOT NULL,
    nome VARCHAR(200) NOT NULL,
    preco NUMERIC(12,2) NOT NULL CHECK (preco >= 0),
    quantidade_estoque INT NOT NULL DEFAULT 0 CHECK (quantidade_estoque >= 0),
    quantidade_reservada INT NOT NULL DEFAULT 0,
    reservada_ate TIMESTAMPTZ,
    row_version BYTEA NOT NULL DEFAULT gen_random_bytes(8),  -- RNFT-E01: concorrência otimista
    excluido_em TIMESTAMPTZ,  -- soft delete
    UNIQUE (tenant_id, filial_id, sku)
);
CREATE INDEX idx_produto_tenant_filial ON produto (tenant_id, filial_id) WHERE excluido_em IS NULL;

CREATE TABLE venda (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    tenant_id UUID NOT NULL REFERENCES tenant(id),
    filial_id UUID NOT NULL REFERENCES filial(id),
    operador_id UUID NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'aberta',  -- aberta|confirmada|cancelada
    total NUMERIC(12,2) NOT NULL DEFAULT 0,
    chave_idempotencia VARCHAR(100) UNIQUE,  -- RNFT-E02
    criado_em TIMESTAMPTZ NOT NULL DEFAULT now(),
    confirmado_em TIMESTAMPTZ,
    cancelado_em TIMESTAMPTZ
);
CREATE INDEX idx_venda_tenant ON venda (tenant_id, criado_em DESC);

CREATE TABLE venda_item (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    venda_id UUID NOT NULL REFERENCES venda(id),
    produto_id UUID NOT NULL REFERENCES produto(id),
    quantidade INT NOT NULL CHECK (quantidade > 0),
    preco_unitario NUMERIC(12,2) NOT NULL  -- snapshot do preço no momento da venda, nunca recalcular depois
);
```

**Decisão deliberada:** `preco_unitario` é gravado como snapshot no item de venda, nunca recalculado a partir do produto depois — se o preço do produto mudar amanhã, a venda de ontem continua correta historicamente. Erro comum de quem modela isso pela primeira vez é referenciar o preço atual do produto em vez de congelar o valor no momento da transação.

---

## 2. Contrato de API (recorte dos endpoints centrais)

| Método | Rota | Request | Resposta 200 | Erros possíveis |
|---|---|---|---|---|
| `POST` | `/v1/auth/login` | `{ email, senha }` | `{ token, expiraEm }` | 401 credencial inválida, 429 rate limit |
| `GET` | `/v1/produtos?pagina=1&tamanho=20` | — | `{ itens: [...], total, pagina }` | 401 sem token |
| `POST` | `/v1/vendas` | `{ chaveIdempotencia, itens: [{produtoId, quantidade}] }` | `{ vendaId, total, status: "aberta" }` | 409 conflito de estoque (RNFT-E01), 422 item inválido |
| `POST` | `/v1/vendas/{id}/confirmar` | `{ meioPagamento }` | `{ status: "confirmada", reciboUrl }` | 409 venda já confirmada/cancelada |
| `POST` | `/v1/vendas/{id}/cancelar` | — | `{ status: "cancelada" }` | 409 venda já confirmada |

**Padrão de versionamento:** `/v1/` no path — quando houver mudança incompatível, nasce `/v2/` convivendo com `/v1/` por um período de transição documentado, nunca substituição abrupta.

**Padrão de erro (RFC 7807 — Problem Details), usado em toda resposta de erro da API, sem exceção:**
```json
{
  "type": "https://kaixara.dev/erros/estoque-insuficiente",
  "title": "Estoque insuficiente",
  "status": 409,
  "detail": "Restam 3 unidades do produto 'Camiseta P', solicitado 5.",
  "instance": "/v1/vendas/a1b2c3"
}
```
Isso substitui a mensagem genérica "Erro 400" por erro estruturado, legível por máquina (o frontend decide o que mostrar) e por humano ao mesmo tempo — é padrão real de API madura, não invenção própria.

---

## 3. Fluxo crítico — Confirmar venda com concorrência de estoque (sequência exata)

```
1. Frontend → POST /v1/vendas/{id}/confirmar
2. API inicia transação de banco
3. Para cada item da venda:
     UPDATE produto
     SET quantidade_estoque = quantidade_estoque - :qtd,
         row_version = gen_random_bytes(8)
     WHERE id = :produtoId
       AND row_version = :rowVersionLido
       AND quantidade_estoque >= :qtd
4. Se QUALQUER update afetar 0 linhas → ROLLBACK, retorna 409 (Problem Details acima)
5. Se todos afetarem 1 linha → grava venda.status = 'confirmada', COMMIT
6. Publica evento VendaConfirmada (fila assíncrona, RNFT-E03) para:
     - aura-notifications (avisar operador/gerente)
     - aura-historico (auditoria)
7. Retorna 200 pro frontend com o recibo
```

Esse é o desenho exato que faz o RNFT-E01 funcionar na prática, não só o conceito — a condição `row_version = :rowVersionLido AND quantidade_estoque >= :qtd` na mesma cláusula `WHERE` é o que garante atomicidade sem precisar de lock explícito de tabela.

---

## 4. Fluxo crítico — Modo offline (agente local)

```
1. Agente local perde conexão com a nuvem
2. Venda continua sendo aceita normalmente pela API LOCAL (rodando no próprio agente, SQLite)
3. Cada venda offline recebe um GUID gerado localmente (nunca sequencial — evita colisão ao sincronizar)
4. Venda entra na fila de sincronização (tabela local `fila_sincronizacao`)
5. A cada 30s, o agente tenta reconectar; ao conseguir:
     - Envia lote de vendas pendentes pra API real, cada uma com sua chave de idempotência
     - API real aplica o mesmo fluxo da seção 3 pra cada venda do lote
     - Se der conflito de estoque numa venda offline (vendeu mais do que existia, porque
       duas filiais venderam offline ao mesmo tempo): venda entra em status "confirmada com
       divergência", sinalizada pro `aura-support` resolver manualmente — não trava a fila inteira
6. Confirmação de sincronização volta pro agente, remove da fila local
```

**Decisão deliberada:** conflito offline nunca trava a fila inteira nem é descartado silenciosamente — vira uma exceção sinalizada, porque perder uma venda real (mesmo com problema) é pior que ter que resolver manualmente depois.

---

## 5. Modelo de domínio tático (DDD)

- **Aggregate Root:** `Venda` — nenhuma alteração em `VendaItem` acontece direto, sempre através do agregado `Venda`, que garante a regra "venda confirmada não pode mais ser alterada"
- **Domain Event:** `VendaConfirmadaEvent`, `VendaCanceladaEvent`, `EstoqueInsuficienteEvent` — disparados de dentro do domínio, consumidos pela camada de aplicação pra publicar na fila (nunca o domínio conhece Redis ou fila diretamente — isso é Infrastructure)
- **Value Object:** `Dinheiro` (não usar `decimal` solto pra valor monetário — encapsular em tipo próprio evita erro de arredondamento inconsistente espalhado pelo código)

---

## 6. Threat Model (STRIDE aplicado ao AM Kaixara)

| Categoria STRIDE | Ameaça específica do AM Kaixara | Mitigação já prevista |
|---|---|---|
| **S**poofing | Alguém se passar por outro operador | JWT assinado + BCrypt (RF01) |
| **T**ampering | Manipular `row_version` pra burlar concorrência | Validação sempre no banco (WHERE clause), nunca confiar em valor vindo do cliente |
| **R**epudiation | Operador negar ter cancelado uma venda | Log de auditoria via `aura-historico`, com identidade de quem executou cada ação |
| **I**nformation Disclosure | Vazamento de preço de custo ou dado de outro tenant | RLS por `tenant_id` no banco, nunca só filtro em nível de aplicação |
| **D**enial of Service | Rajada de requisição de venda derrubando o serviço | Rate limiting (RNFT-S) + fila assíncrona (RNFT-E03) absorvendo pico |
| **E**levation of Privilege | Operador de caixa acessando rota de gerente | `[Authorize(Roles = "Gerente")]` verificado no backend, nunca só escondido no frontend |

---

## 7. O que fica deliberadamente fora por enquanto — e por quê

Ser "o profissional mais perfeito em design de software" inclui saber a hora certa de cada decisão, não maximizar documentação. Estes itens são reais, mas prematuros:

- **Capacidade real (requisições/segundo, volume de dado projetado)** — não faz sentido dimensionar capacidade antes do primeiro cliente real gerar dado de uso pra calibrar a estimativa
- **Topologia de múltiplas instâncias/load balancer** — só relevante quando uma instância única já não bastar; documentar isso agora seria desenhar solução pra problema que ainda não existe
- **Estimativa de custo de infraestrutura em produção** — depende de volume real, que só aparece depois do primeiro cliente
- **API Gateway/BFF dedicado** — hoje o frontend consome a API diretamente; isso só vira necessidade real se mais de um tipo de cliente (mobile nativo, integração de terceiro) precisar de agregação diferente

Documentar esses cinco agora seria o mesmo erro já corrigido antes nesta conversa com Clojure/Datomic — sofisticação sem problema real por trás ainda.
