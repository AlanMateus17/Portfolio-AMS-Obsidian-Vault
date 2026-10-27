# 4 · Tráfego pago

[← Marketing](README.md)

## Antes do primeiro real

1. O produto já vendeu no orgânico (pelo menos 10 vendas sem anúncio).
2. A [calculadora](07-medicao-e-lucro.md) mostra o **CPA máximo de empate** e o **ROAS de empate** do produto.
3. Pixel e API de Conversões (CAPI) instalados juntos, com deduplicação por `event_id`; a compra chega pelo webhook da plataforma.
4. Todo link com UTM no padrão: `utm_source=meta&utm_medium=pago&utm_campaign=<produto>-<teste>&utm_content=<criativo>`.

## Como testar gastando pouco

- **Orçamento do primeiro teste:** um valor que você aceita perder inteiro (ex.: R$ 300), dividido em 7 a 10 dias.
- **Estrutura (Meta):** uma campanha de Vendas, 1 ou 2 conjuntos com público amplo, 3 a 5 criativos por conjunto.
- **O criativo é a alavanca principal.** Teste ganchos diferentes nos 3 primeiros segundos, não cores de botão.
- **Fase de aprendizado:** o conjunto precisa de cerca de 50 conversões por semana para estabilizar. Com orçamento pequeno isso não acontece; otimize primeiro para um evento anterior (início de checkout) e passe para Compra quando houver volume.
- **Mudanças de orçamento:** no máximo 10 a 20% a cada 3 ou 4 dias.
- **Janela de atribuição:** a padrão da Meta é 7 dias após clique e 1 dia após visualização. Compare sempre com as vendas reais da plataforma.

## Regras de corte (automáticas no painel)

| Situação | Ação |
|---|---|
| Gastou 1× o CPA de empate e nenhuma venda | Pausar o criativo |
| CPA dos últimos 3 dias acima do empate | Pausar o conjunto |
| CPA abaixo do CPA da margem desejada por 5 dias | Subir 15% do orçamento |
| Frequência acima de 3 a 4 | Trocar o criativo (público cansado) |
| ROAS abaixo do de empate na semana | Parar e revisar oferta, página ou preço |

## Canais, em ordem

Todos os canais, com o limite de custo de cada um: [Canais de anúncio](11-canais-de-anuncio.md). Lembre: desde jan/2026 a fatura da Meta tem +12,15% de impostos sobre a mídia, e o TikTok exige pelo menos US$ 20/dia por grupo de anúncios.


1. **Meta (Instagram e Facebook):** melhor para infoproduto de entrada no Brasil.
2. **YouTube Ads:** para os vídeos longos que já convertem no orgânico.
3. **Google Pesquisa:** para buscas com intenção ("curso de lógica de programação").
4. **TikTok Ads:** depois que os cortes orgânicos mostrarem tração.
5. **Udemy:** sempre divulgue pelo seu cupom. A venda pelo seu link rende 97% para você; a orgânica da Udemy, 37%.

## O que não fazer

- Impulsionar post pelo botão do Instagram (otimiza para curtida, não para venda).
- Promessa de renda ou resultado garantido em anúncio (reprovação e risco de bloqueio da conta).
- Mais de uma conta de anúncio ou de perfil para "escalar" (bloqueio em cadeia).
