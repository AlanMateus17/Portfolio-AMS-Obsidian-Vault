# Sistemas e medição do grupo

[← Negócios do grupo](README.md)

Os negócios do grupo são o primeiro cliente dos sistemas AM. Cada problema resolvido na loja ou na logística do grupo vira funcionalidade vendida pela [AMtech Software](01-software-house.md).

## Qual sistema roda onde

| Sistema | O que faz | Loja | Maker | Entregas | Delivery |
|---|---|:---:|:---:|:---:|:---:|
| **AM Gestão · Caixa** (ex-Kaixara) | PDV, ordem de serviço, estoque | ✓ | ✓ | | |
| **AM Gestão · Pedidos** (ex-Rotara) | Pedidos, roteirização, app do entregador, prova de entrega, repasse | | | ✓ | ✓ |
| **AM Gestão · Financeiro** (ex-Rendara) | Contas a pagar e receber, fluxo de caixa, DRE por negócio | ✓ | ✓ | ✓ | ✓ |
| **Painel do grupo** (Grafana) | Indicadores de todos os negócios num lugar só | ✓ | ✓ | ✓ | ✓ |
| **Emissor fiscal** (API de NF-e e NFS-e) | Nota automática em cada venda | ✓ | ✓ | ✓ | ✓ |

## Como os dados correm

```mermaid
flowchart LR
  K["AM Gestão · Caixa<br/>vendas, OS, estoque"] --> DB[("PostgreSQL<br/>multi-tenant")]
  R["AM Gestão · Pedidos<br/>entregas, pedidos"] --> DB
  F["AM Gestão · Financeiro<br/>caixa, contas"] --> DB
  B["Bancos e adquirentes<br/>extratos"] --> F
  DB --> G["Painel do grupo<br/>Grafana"]
  G --> P["Portões entre fases<br/>decididos por número"]
```

Cada negócio é um tenant. O painel do grupo lê todos, com permissão só para você e o contador.

## Os números que decidem

| Indicador | Onde se aplica | Meta inicial |
|---|---|---|
| Receita × ponto de equilíbrio | Todos | Acima por 3 meses seguidos (portão) |
| Margem de contribuição por fonte | Todos | Igual ou acima da prevista em [Números](numeros.md) |
| Ticket médio e pedidos por dia | Delivery | Crescendo mês a mês na rampa |
| Conversão do ponto de retirada | Loja | 3% das retiradas viram venda |
| Entregas por rota e custo por entrega | Entregas | 20 ou mais pacotes por rota de Flex |
| Lojistas ativos e pedidos por lojista | Delivery | 20 lojistas e 75 pedidos por lojista |
| MRR e churn | Software | Churn abaixo de 3% ao mês |
| Prazo médio de recebimento e de pagamento | Todos | Receber antes de pagar |
| Caixa em dias de custo fixo | Todos | 90 dias (a reserva do planejador) |

## Fechamento do mês

1. Extratos conciliados no Financeiro do AM Gestão (o banco é a verdade).
2. Inventário da loja e do Maker.
3. DRE por negócio: receita, variáveis, impostos, margem, fixos, lucro.
4. Comparação com o cenário de [Números](numeros.md) e atualização do `data/negocios.json` com o realizado.
5. Decisão do mês: seguir, corrigir (preço, equipe, rota) ou parar.
