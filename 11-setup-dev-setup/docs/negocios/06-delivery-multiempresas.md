# 6 · AM Delivery: pedidos de várias empresas

[← Negócios do grupo](README.md) · [Números](numeros.md#delivery)

Um app de pedidos para restaurantes, mercados, farmácias e lojas de Barbacena, com entrega pela frota da [AM Entregas](05-logistica-e-entregas.md). A meta é **alta adesão de lojistas** com comissão bem menor que a do iFood e **lucro na comissão, não na entrega**.

## O concorrente que já está lá

| | iFood Básico | iFood Entrega | AM Delivery |
|---|---:|---:|---:|
| Quem entrega | A loja | Entregador do iFood | AM Entregas |
| Comissão por pedido | 12% | 23% | **8%** |
| Taxa sobre pagamento on-line | 3,2% | 3,2% | repasse do custo real do gateway |
| Mensalidade | R$ 110 | até R$ 150 | zero no 1º ano |

Planos do iFood em junho de 2026 ([Diário do Pará](https://diariodopara.com.br/seu-bolso/veja-como-cadastrar-uma-loja-escolher-plano-e-calcular-taxas-no-ifood/)). O aiqfome, forte em cidades do interior de Minas, também pode chegar ([GiroNews](https://gironews.com/food-service/aiqfome-pretende-chegar-a-117-cidades-em-minas-gerais-ate-2026/)).

## Por que a conta fecha na comissão

No cenário-alvo, a taxa de entrega é 60% da receita e só 9% da margem: quase tudo vai para o entregador. A comissão é 35% da receita e 80% da margem ([números](numeros.md#delivery)). Consequências:

- **Nunca subsidiar entrega para competir em preço.** O cupom é para o primeiro pedido, com teto mensal no orçamento de marketing.
- **Crescer em número de lojistas ativos e em pedidos por lojista**, que é onde a comissão aumenta.
- **Destaque pago** no app é margem quase pura, depois que houver tráfego.

## Como ganhar adesão, de verdade

"Dominar o mercado" contra o iFood não se faz no primeiro ano. O que funciona numa cidade de 130 mil habitantes:

1. **Começar pelos próprios restaurantes do grupo** (quando existirem) e por 10 lojistas âncora que pagam 23% no iFood e querem sair. Eles recebem o app da loja com a marca deles (o mesmo sistema, com o cardápio deles), e o AM Delivery é a vitrine coletiva.
2. **Categorias que o iFood atende mal na cidade:** farmácias, mercados de bairro, pet shops, floriculturas, autopeças, lanchonetes de bairro.
3. **Pedido pelo WhatsApp com link do cardápio** para quem não quer baixar app: o cliente pede em 3 toques, sem cadastro.
4. **Repasse rápido ao lojista** (D+1 por Pix) como argumento contra o prazo das grandes plataformas.
5. **Dados do cliente são do lojista também**: ele pode fazer campanha para a própria base, o que o iFood não permite.
6. **Programa de fidelidade da cidade**: pontos que valem em qualquer loja do app.

## Pagamento

O app recebe por Pix e cartão por um intermediador de pagamento com split (a parte do lojista cai direto para ele). Isso evita que o dinheiro do lojista passe pelo caixa da AM Logística, reduz imposto sobre valores de terceiros e simplifica a nota. A comissão de 8% é a receita da AM Logística e é sobre ela que sai a nota fiscal. Confirme o desenho fiscal com o contador.

## Produto

- **App do cliente** (Next.js como PWA primeiro; loja de apps quando houver volume), **painel do lojista** (cardápio, horários, pausa, pedidos em tempo real por SignalR) e **app do entregador**, todos do mesmo AM Rotara.
- Cardápio com foto, adicionais, tempo de preparo e estoque do dia.
- Impressão automática do pedido na cozinha do lojista.

## Riscos

- **Galinha e ovo:** sem lojistas não há clientes, sem clientes não há lojistas. Por isso a rampa é de 12 meses começando em 10% e o capital mínimo é alto para o tamanho do investimento.
- **Reação do concorrente:** cupons agressivos na cidade. A resposta é a comissão menor e o relacionamento local, não guerra de cupom.
- **Lei do consumidor:** o app responde junto com o lojista por problemas no pedido. Termos de uso e política de reembolso claros.
