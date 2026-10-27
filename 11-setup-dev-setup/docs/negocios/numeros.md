<!-- Arquivo GERADO por tools/negocios/gerar.py a partir de data/negocios.json. Não edite à mão. -->

# Números de cada negócio

[← Negócios do grupo](README.md)

> Valores de referência para Barbacena em outubro de 2026, montados a partir de anúncios de aluguel, tabelas públicas e médias de mercado. Troque cada linha por orçamento real antes de assinar qualquer contrato.

## Premissas

- Cidade: Barbacena (MG), 129.757 habitantes (IBGE, estimativa). Data de referência: 2026-10-21.
- Salário mínimo de 2026: R$ 1.621. Salário × 1,4 cobre FGTS, 13º, férias + 1/3, vale-transporte e provisão de rescisão em empresa do Simples (anexos I a III). Estimativa; o contador calcula o valor real pela convenção coletiva.
- O custo variável de cada fonte já soma CMV (insumos pela ficha técnica), embalagem, taxa de cartão (média de 2,5%), comissão do app quando houver e 3% de perdas e quebras nos negócios de comida.
- Rampa: no 1º mês o negócio fatura uma fração do alvo e cresce em linha reta até 100% no último mês da rampa. Os custos fixos são cheios desde o 1º mês. Cada negócio usa a própria rampa, indicada abaixo.
- Capital mínimo = investimento + prejuízo acumulado na rampa + reserva de 3 meses de custos fixos.
- Simples Nacional calculado por fonte, no anexo de cada atividade, com a faixa definida pela receita total (tabelas de 2026). Nos primeiros meses, a receita dos 12 meses é a média dos meses já vividos × 12, como manda a LC 123.
- Cenário conservador: o mesmo negócio vendendo 70% do alvo.

## Resumo

| Negócio | Investimento | Custos fixos/mês | Receita-alvo/mês | Lucro no alvo | Lucro a 70% | Ponto de equilíbrio | Retorno | Capital mínimo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| [AMtech Software (projetos, SaaS e plataformas)](#software) | R$ 3.100 | R$ 4.960 | R$ 12.725 | R$ 5.954 (46,8%) | R$ 2.679 | R$ 5.783 (45,4% do alvo) | mês 7 | R$ 21.605 |
| [Loja AMtech (assistência, peças sem estoque e ponto de retirada)](#loja) | R$ 24.700 | R$ 7.760 | R$ 29.144 | R$ 5.519 (18,9%) | R$ 1.720 | R$ 16.443 (56,4% do alvo) | mês 11 | R$ 52.847 |
| [AMtech Maker (robótica e automação próprias)](#produtos) | R$ 8.350 | R$ 500 | R$ 14.900 | R$ 5.193 (34,9%) | R$ 3.485 | R$ 1.309 (8,8% do alvo) | mês 6 | R$ 9.850 |
| [AM Entregas (motofrete, carro e logística de marketplaces)](#entregas) | R$ 12.200 | R$ 5.950 | R$ 31.700 | R$ 2.864 (9,0%) | R$ 482 | R$ 20.299 (64,0% do alvo) | mês 15 | R$ 41.436 |
| [AM Delivery (app de pedidos de várias empresas)](#delivery) | R$ 14.200 | R$ 8.720 | R$ 37.500 | R$ 5.402 (14,4%) | R$ 1.521 | R$ 22.031 (58,7% do alvo) | mês 16 | R$ 64.421 |
| [Sushi (delivery primeiro, balcão de retirada)](#sushi) | R$ 65.300 | R$ 17.400 | R$ 72.700 | R$ 14.054 (19,3%) | R$ 5.071 | R$ 38.783 (53,3% do alvo) | mês 9 | R$ 124.635 |
| [Cafeteria (cafés especiais de Minas)](#cafeteria) | R$ 68.300 | R$ 15.980 | R$ 53.350 | R$ 12.650 (23,7%) | R$ 4.408 | R$ 28.836 (54,1% do alvo) | mês 10 | R$ 123.354 |
| [Padaria com café da manhã e almoço](#padaria) | R$ 164.200 | R$ 49.400 | R$ 209.100 | R$ 49.977 (23,9%) | R$ 22.216 | R$ 99.745 (47,7% do alvo) | mês 9 | R$ 328.239 |
| **Todos** | **R$ 360.350** | | | | | | | **R$ 766.387** |

O retorno é o mês em que o caixa acumulado, já descontado o investimento, volta a zero.

<a id="software"></a>

## AMtech Software (projetos, SaaS e plataformas)

A · Tecnologia · rampa de 9 meses, começando em 25,0% do alvo.

> Pró-labore de R$ 3.600 mantém o Fator R em 28% ou mais e a empresa no Anexo III (6%). Sem ele, cai no Anexo V (15,5%). O pró-labore é seu: entra como custo, mas é a sua renda.

### Investimento inicial

| Item | Valor |
|---|---:|
| Abertura do CNPJ, inscrição municipal e alvará (via contador) | R$ 1.500 |
| Certificado digital e-CNPJ A1 | R$ 220 |
| Domínio, e-mail profissional e site (1º ano) | R$ 480 |
| Contrato padrão, termos e política de privacidade (revisão jurídica) | R$ 900 |
| **Total** | **R$ 3.100** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Contador (serviços, Simples) | R$ 400 |
| Nuvem (Azure/VPS) dos SaaS em produção | R$ 300 |
| Ferramentas da empresa (repositórios, e-mail, monitoramento) | R$ 200 |
| API de nota fiscal (NFS-e) | R$ 60 |
| Marketing (anúncios locais e conteúdo) | R$ 400 |
| Pró-labore (seu) | R$ 3.600 |
| **Total** | **R$ 4.960** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Sistemas sob encomenda | 1 × R$ 4.500,00 | R$ 4.500 | R$ 450 (10,0%) | R$ 270 (Anexo III) | R$ 3.780 |
| Sites e lojas para pequenas empresas | 2 × R$ 1.500,00 | R$ 3.000 | R$ 150 (5,0%) | R$ 180 (Anexo III) | R$ 2.670 |
| SaaS AM (assinaturas) | 25 × R$ 149,00 | R$ 3.725 | R$ 298 (8,0%) | R$ 224 (Anexo III) | R$ 3.204 |
| Manutenção e hospedagem mensal | 6 × R$ 250,00 | R$ 1.500 | R$ 150 (10,0%) | R$ 90 (Anexo III) | R$ 1.260 |
| **Total** | | **R$ 12.725** | **R$ 1.048** | **R$ 764** | **R$ 10.914** (85,8%) |

Margem de contribuição R$ 10.914 − custos fixos R$ 4.960 = **lucro de R$ 5.954 por mês** no alvo e R$ 2.679 vendendo 70%. Empata com R$ 5.783 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 25,0% | R$ 3.181 | −R$ 2.232 | −R$ 5.332 |
| 2 | 34,4% | R$ 4.374 | −R$ 1.208 | −R$ 6.540 |
| 3 | 43,8% | R$ 5.567 | −R$ 185 | −R$ 6.725 |
| 4 | 53,1% | R$ 6.760 | R$ 838 | −R$ 5.888 |
| 5 | 62,5% | R$ 7.953 | R$ 1.861 | −R$ 4.027 |
| 6 | 71,9% | R$ 9.146 | R$ 2.884 | −R$ 1.143 |
| 7 | 81,2% | R$ 10.339 | R$ 3.907 | R$ 2.765 |
| 8 | 90,6% | R$ 11.532 | R$ 4.930 | R$ 7.695 |
| 9 | 100,0% | R$ 12.725 | R$ 5.954 | R$ 13.648 |
| 10 | 100,0% | R$ 12.725 | R$ 5.954 | R$ 19.602 |
| 11 | 100,0% | R$ 12.725 | R$ 5.954 | R$ 25.555 |
| 12 | 100,0% | R$ 12.725 | R$ 5.954 | R$ 31.509 |

Pior caixa: −R$ 6.725. Capital mínimo: investimento R$ 3.100 + prejuízo da rampa R$ 3.625 + reserva R$ 14.880 = **R$ 21.605**.

<a id="loja"></a>

## Loja AMtech (assistência, peças sem estoque e ponto de retirada)

A · Tecnologia · rampa de 8 meses, começando em 35,0% do alvo.

> Os pacotes rendem pouco sozinhos (cerca de R$ 1.140 por mês aqui). O ganho real é o movimento: cada retirada é um cliente dentro da loja.

### Investimento inicial

| Item | Valor |
|---|---:|
| Caução e 1º aluguel (loja de 30 a 50 m², R$ 1.800) | R$ 3.600 |
| Pintura, fachada e elétrica | R$ 4.000 |
| Balcão e prateleiras numeradas para pacotes | R$ 3.500 |
| Bancada e ferramentas (estação de retrabalho, solda, multímetro, fonte, ultrassom, kit ESD) | R$ 4.500 |
| Computador do balcão, leitor de código de barras e impressora de etiquetas | R$ 2.500 |
| Câmeras e alarme | R$ 1.200 |
| Mostruário de giro rápido (cabos, carregadores, SSD, mouses) | R$ 3.000 |
| Licenças, bombeiros (processo simplificado) e extintores | R$ 2.400 |
| **Total** | **R$ 24.700** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Aluguel | R$ 1.800 |
| IPTU e taxas | R$ 150 |
| Energia | R$ 300 |
| Internet | R$ 130 |
| Contador (comércio + serviços) | R$ 500 |
| Marketing local (Google Perfil, anúncios, panfletos) | R$ 400 |
| Seguro do ponto e monitoramento | R$ 220 |
| Limpeza e consumo | R$ 200 |
| Técnico-atendente (abre a loja de segunda a sábado) (1 × salário R$ 2.000 × 1,4) | R$ 2.800 |
| Auxiliar de meio período (sábado e horário de almoço) (1 × salário R$ 900 × 1,4) | R$ 1.260 |
| **Total** | **R$ 7.760** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Serviços técnicos (formatação, limpeza, reparo, upgrade) | 70 × R$ 160,00 | R$ 11.200 | R$ 1.344 (12,0%) | R$ 955 (Anexo III) | R$ 8.901 |
| Peças e acessórios sob encomenda (sem estoque) | 60 × R$ 220,00 | R$ 13.200 | R$ 10.296 (78,0%) | R$ 739 (Anexo I) | R$ 2.165 |
| Mostruário de giro rápido | 80 × R$ 45,00 | R$ 3.600 | R$ 2.232 (62,0%) | R$ 202 (Anexo I) | R$ 1.166 |
| Ponto de retirada Shopee (R$ 0,70 a 0,60 por pacote) | 1.200 × R$ 0,62 | R$ 744 | R$ 0 (0,0%) | R$ 63 (Anexo III) | R$ 681 |
| Agência Mercado Livre (valor a confirmar na proposta) | 800 × R$ 0,50 | R$ 400 | R$ 0 (0,0%) | R$ 34 (Anexo III) | R$ 366 |
| **Total** | | **R$ 29.144** | **R$ 13.872** | **R$ 1.993** | **R$ 13.279** (45,6%) |

Margem de contribuição R$ 13.279 − custos fixos R$ 7.760 = **lucro de R$ 5.519 por mês** no alvo e R$ 1.720 vendendo 70%. Empata com R$ 16.443 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 35,0% | R$ 10.200 | −R$ 2.909 | −R$ 27.609 |
| 2 | 44,3% | R$ 12.907 | −R$ 1.622 | −R$ 29.232 |
| 3 | 53,6% | R$ 15.613 | −R$ 335 | −R$ 29.567 |
| 4 | 62,9% | R$ 18.319 | R$ 952 | −R$ 28.615 |
| 5 | 72,1% | R$ 21.025 | R$ 2.205 | −R$ 26.411 |
| 6 | 81,4% | R$ 23.732 | R$ 3.413 | −R$ 22.998 |
| 7 | 90,7% | R$ 26.438 | R$ 4.616 | −R$ 18.382 |
| 8 | 100,0% | R$ 29.144 | R$ 5.815 | −R$ 12.567 |
| 9 | 100,0% | R$ 29.144 | R$ 5.769 | −R$ 6.798 |
| 10 | 100,0% | R$ 29.144 | R$ 5.735 | −R$ 1.063 |
| 11 | 100,0% | R$ 29.144 | R$ 5.709 | R$ 4.646 |
| 12 | 100,0% | R$ 29.144 | R$ 5.689 | R$ 10.336 |

Pior caixa: −R$ 29.567. Capital mínimo: investimento R$ 24.700 + prejuízo da rampa R$ 4.867 + reserva R$ 23.280 = **R$ 52.847**.

<a id="produtos"></a>

## AMtech Maker (robótica e automação próprias)

A · Tecnologia · rampa de 12 meses, começando em 20,0% do alvo.

> Roda dentro da Loja AMtech e do mesmo CNPJ: usa a bancada e o técnico dela. A mão de obra das instalações já está no custo variável (paga por serviço).

> Produto próprio com Wi-Fi ou Bluetooth só depois da homologação na Anatel; o orçamento sai com um organismo certificador.

### Investimento inicial

| Item | Valor |
|---|---:|
| Impressora 3D e filamentos | R$ 3.500 |
| Componentes para protótipos e primeiro lote | R$ 3.500 |
| Fotos, embalagem e manual dos kits | R$ 900 |
| Registro de marca no INPI (uma classe) | R$ 450 |
| **Total** | **R$ 8.350** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Marketing e conteúdo dos kits | R$ 400 |
| Loja virtual e anúncios em marketplaces | R$ 100 |
| **Total** | **R$ 500** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Kits de robótica educacional sem rádio | 20 × R$ 290,00 | R$ 5.800 | R$ 3.190 (55,0%) | R$ 261 (Anexo II) | R$ 2.349 |
| Automação residencial (instalação com aparelhos homologados) | 3 × R$ 1.200,00 | R$ 3.600 | R$ 2.160 (60,0%) | R$ 216 (Anexo III) | R$ 1.224 |
| Automação rural (irrigação, caixa d'água, sensores) | 1 × R$ 2.500,00 | R$ 2.500 | R$ 1.550 (62,0%) | R$ 150 (Anexo III) | R$ 800 |
| Oficinas e kits para escolas | 1 × R$ 3.000,00 | R$ 3.000 | R$ 1.500 (50,0%) | R$ 180 (Anexo III) | R$ 1.320 |
| **Total** | | **R$ 14.900** | **R$ 8.400** | **R$ 807** | **R$ 5.693** (38,2%) |

Margem de contribuição R$ 5.693 − custos fixos R$ 500 = **lucro de R$ 5.193 por mês** no alvo e R$ 3.485 vendendo 70%. Empata com R$ 1.309 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 20,0% | R$ 2.980 | R$ 639 | −R$ 7.711 |
| 2 | 27,3% | R$ 4.064 | R$ 1.053 | −R$ 6.659 |
| 3 | 34,5% | R$ 5.147 | R$ 1.467 | −R$ 5.192 |
| 4 | 41,8% | R$ 6.231 | R$ 1.881 | −R$ 3.311 |
| 5 | 49,1% | R$ 7.315 | R$ 2.295 | −R$ 1.017 |
| 6 | 56,4% | R$ 8.398 | R$ 2.709 | R$ 1.692 |
| 7 | 63,6% | R$ 9.482 | R$ 3.123 | R$ 4.815 |
| 8 | 70,9% | R$ 10.565 | R$ 3.537 | R$ 8.352 |
| 9 | 78,2% | R$ 11.649 | R$ 3.951 | R$ 12.303 |
| 10 | 85,5% | R$ 12.733 | R$ 4.365 | R$ 16.668 |
| 11 | 92,7% | R$ 13.816 | R$ 4.779 | R$ 21.447 |
| 12 | 100,0% | R$ 14.900 | R$ 5.193 | R$ 26.640 |

Pior caixa: −R$ 8.350. Capital mínimo: investimento R$ 8.350 + prejuízo da rampa R$ 0 + reserva R$ 1.500 = **R$ 9.850**.

<a id="entregas"></a>

## AM Entregas (motofrete, carro e logística de marketplaces)

B · Logística · rampa de 10 meses, começando em 20,0% do alvo.

> Entregadores MEI com rota, horário e uniforme impostos podem virar vínculo de emprego na Justiça do Trabalho. O contrato e a operação precisam ser desenhados com advogado.

### Investimento inicial

| Item | Valor |
|---|---:|
| Abertura do CNPJ de logística e licenças | R$ 1.800 |
| Caução e 1º aluguel (sala de 25 m², base de despacho) | R$ 2.400 |
| Baús e bags com a marca (10 unidades, em comodato) | R$ 2.500 |
| Celular de despacho, impressora de etiquetas e móveis | R$ 2.500 |
| Lançamento: visitas comerciais, adesivos, panfletos | R$ 3.000 |
| **Total** | **R$ 12.200** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Sala de despacho | R$ 1.200 |
| Contador | R$ 500 |
| Nuvem, mapas e WhatsApp Business API (AM Rotara) | R$ 450 |
| Seguro de carga e responsabilidade civil | R$ 300 |
| Telefone e internet | R$ 200 |
| Marketing B2B | R$ 500 |
| Despachante (turno de 8h às 17h) (1 × salário R$ 2.000 × 1,4) | R$ 2.800 |
| **Total** | **R$ 5.950** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Entregas avulsas para empresas (farmácias, laboratórios, autopeças, cartórios) | 1.200 × R$ 10,00 | R$ 12.000 | R$ 8.400 (70,0%) | R$ 1.064 (Anexo III) | R$ 2.536 |
| Mercado Envios Flex para vendedores locais | 900 × R$ 11,00 | R$ 9.900 | R$ 5.544 (56,0%) | R$ 877 (Anexo III) | R$ 3.479 |
| Coleta nos vendedores e entrega nas agências | 120 × R$ 35,00 | R$ 4.200 | R$ 2.100 (50,0%) | R$ 372 (Anexo III) | R$ 1.728 |
| Rotas fixas por contrato (carro, mensal) | 2 × R$ 2.800,00 | R$ 5.600 | R$ 4.032 (72,0%) | R$ 496 (Anexo III) | R$ 1.072 |
| **Total** | | **R$ 31.700** | **R$ 20.076** | **R$ 2.809** | **R$ 8.814** (27,8%) |

Margem de contribuição R$ 8.814 − custos fixos R$ 5.950 = **lucro de R$ 2.864 por mês** no alvo e R$ 482 vendendo 70%. Empata com R$ 20.299 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 20,0% | R$ 6.340 | −R$ 4.006 | −R$ 16.206 |
| 2 | 28,9% | R$ 9.158 | −R$ 3.141 | −R$ 19.347 |
| 3 | 37,8% | R$ 11.976 | −R$ 2.277 | −R$ 21.624 |
| 4 | 46,7% | R$ 14.793 | −R$ 1.413 | −R$ 23.037 |
| 5 | 55,6% | R$ 17.611 | −R$ 549 | −R$ 23.586 |
| 6 | 64,4% | R$ 20.429 | R$ 315 | −R$ 23.271 |
| 7 | 73,3% | R$ 23.247 | R$ 1.179 | −R$ 22.091 |
| 8 | 82,2% | R$ 26.064 | R$ 1.943 | −R$ 20.148 |
| 9 | 91,1% | R$ 28.882 | R$ 2.685 | −R$ 17.463 |
| 10 | 100,0% | R$ 31.700 | R$ 3.424 | −R$ 14.040 |
| 11 | 100,0% | R$ 31.700 | R$ 3.349 | −R$ 10.690 |
| 12 | 100,0% | R$ 31.700 | R$ 3.294 | −R$ 7.397 |

Pior caixa: −R$ 23.586. Capital mínimo: investimento R$ 12.200 + prejuízo da rampa R$ 11.386 + reserva R$ 17.850 = **R$ 41.436**.

<a id="delivery"></a>

## AM Delivery (app de pedidos de várias empresas)

B · Logística · rampa de 12 meses, começando em 10,0% do alvo.

> 3.000 pedidos por mês exige cerca de 40 lojistas ativos. Concorre com o iFood (12% a 23% de comissão), que já tem os clientes: o plano começa pelos restaurantes do grupo e pelos lojistas que pagam caro no iFood.

### Investimento inicial

| Item | Valor |
|---|---:|
| Publicação nas lojas de apps (Apple e Google) | R$ 700 |
| Cupons de lançamento para os primeiros clientes | R$ 8.000 |
| Equipe comercial de lançamento (2 meses de visitas) | R$ 4.000 |
| Material dos lojistas (displays, adesivos, QR code) | R$ 1.500 |
| **Total** | **R$ 14.200** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Nuvem, mapas, notificações e SMS | R$ 700 |
| Marketing contínuo (anúncios, cupons, influenciadores locais) | R$ 2.500 |
| Contador (incremental, mesmo CNPJ da AM Entregas) | R$ 200 |
| Suporte e despacho noturno (18h às 23h) (1 × salário R$ 1.800 × 1,4) | R$ 2.520 |
| Comercial (cadastra e cuida dos lojistas) (1 × salário R$ 2.000 × 1,4) | R$ 2.800 |
| **Total** | **R$ 8.720** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Comissão dos lojistas (8% do pedido; pagamento repassado à parte) | 3.000 × R$ 4,40 | R$ 13.200 | R$ 660 (5,0%) | R$ 1.265 (Anexo III) | R$ 11.275 |
| Taxa de entrega paga pelo cliente | 3.000 × R$ 7,50 | R$ 22.500 | R$ 19.125 (85,0%) | R$ 2.156 (Anexo III) | R$ 1.219 |
| Destaque pago no app (lojistas) | 15 × R$ 120,00 | R$ 1.800 | R$ 0 (0,0%) | R$ 172 (Anexo III) | R$ 1.628 |
| **Total** | | **R$ 37.500** | **R$ 19.785** | **R$ 3.593** | **R$ 14.122** (37,7%) |

Margem de contribuição R$ 14.122 − custos fixos R$ 8.720 = **lucro de R$ 5.402 por mês** no alvo e R$ 1.521 vendendo 70%. Empata com R$ 22.031 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 10,0% | R$ 3.750 | −R$ 7.174 | −R$ 21.374 |
| 2 | 18,2% | R$ 6.818 | −R$ 5.908 | −R$ 27.282 |
| 3 | 26,4% | R$ 9.886 | −R$ 4.643 | −R$ 31.925 |
| 4 | 34,5% | R$ 12.955 | −R$ 3.378 | −R$ 35.302 |
| 5 | 42,7% | R$ 16.023 | −R$ 2.112 | −R$ 37.414 |
| 6 | 50,9% | R$ 19.091 | −R$ 847 | −R$ 38.261 |
| 7 | 59,1% | R$ 22.159 | R$ 418 | −R$ 37.843 |
| 8 | 67,3% | R$ 25.227 | R$ 1.684 | −R$ 36.159 |
| 9 | 75,5% | R$ 28.295 | R$ 2.855 | −R$ 33.304 |
| 10 | 83,6% | R$ 31.364 | R$ 3.977 | −R$ 29.327 |
| 11 | 91,8% | R$ 34.432 | R$ 5.096 | −R$ 24.231 |
| 12 | 100,0% | R$ 37.500 | R$ 6.213 | −R$ 18.018 |

Pior caixa: −R$ 38.261. Capital mínimo: investimento R$ 14.200 + prejuízo da rampa R$ 24.061 + reserva R$ 26.160 = **R$ 64.421**.

<a id="sushi"></a>

## Sushi (delivery primeiro, balcão de retirada)

C · Alimentação · rampa de 6 meses, começando em 35,0% do alvo.

> O cenário conta com você como sushiman principal sem pró-labore. Se não puder estar lá de quarta a domingo à noite, some um sushiman de R$ 3.000 (custo de cerca de R$ 4.200).

### Investimento inicial

| Item | Valor |
|---|---:|
| Caução e 1º aluguel (40 a 50 m², R$ 2.200) | R$ 4.400 |
| Reforma da cozinha nas regras da RDC 216 (piso, azulejo, ralo sifonado, tela, pia de mãos) | R$ 18.000 |
| Exaustão e coifa | R$ 6.000 |
| Vitrine refrigerada de sushi | R$ 4.500 |
| Geladeira e freezer industriais | R$ 8.000 |
| Panela de arroz industrial, fritadeira e seladora | R$ 3.900 |
| Mesas de inox, facas e utensílios | R$ 5.500 |
| Ar-condicionado da área de manipulação | R$ 3.000 |
| Projeto, alvarás, bombeiros e vigilância sanitária | R$ 4.000 |
| Estoque inicial e embalagens | R$ 4.000 |
| Lançamento (fotos, anúncios, degustação) | R$ 4.000 |
| **Total** | **R$ 65.300** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Aluguel | R$ 2.200 |
| Energia (refrigeração 24 h) | R$ 1.200 |
| Gás e água | R$ 500 |
| Internet | R$ 130 |
| Contador (restaurante) | R$ 600 |
| Controle de pragas, manutenção e análise da água | R$ 250 |
| Marketing | R$ 1.000 |
| Uniformes, EPI e limpeza | R$ 300 |
| Manutenção de equipamentos e reposição de utensílios | R$ 300 |
| Sushiman auxiliar (1 × salário R$ 2.400 × 1,4) | R$ 3.360 |
| Auxiliar de cozinha (2 × salário R$ 1.800 × 1,4) | R$ 5.040 |
| Atendente e caixa (1 × salário R$ 1.800 × 1,4) | R$ 2.520 |
| **Total** | **R$ 17.400** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Delivery próprio (app e WhatsApp, entrega AM Entregas) | 450 × R$ 90,00 | R$ 40.500 | R$ 17.415 (43,0%) | R$ 3.289 (Anexo I) | R$ 19.796 |
| iFood (plano Entrega: 23% + 3,2%) | 200 × R$ 95,00 | R$ 19.000 | R$ 12.635 (66,5%) | R$ 1.543 (Anexo I) | R$ 4.822 |
| Balcão e retirada | 120 × R$ 80,00 | R$ 9.600 | R$ 3.744 (39,0%) | R$ 780 (Anexo I) | R$ 5.076 |
| Festas e eventos (barca, sushiman em casa) | 3 × R$ 1.200,00 | R$ 3.600 | R$ 1.548 (43,0%) | R$ 292 (Anexo I) | R$ 1.760 |
| **Total** | | **R$ 72.700** | **R$ 35.342** | **R$ 5.904** | **R$ 31.454** (43,3%) |

Margem de contribuição R$ 31.454 − custos fixos R$ 17.400 = **lucro de R$ 14.054 por mês** no alvo e R$ 5.071 vendendo 70%. Empata com R$ 38.783 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 35,0% | R$ 25.445 | −R$ 5.687 | −R$ 70.987 |
| 2 | 48,0% | R$ 34.896 | −R$ 1.447 | −R$ 72.435 |
| 3 | 61,0% | R$ 44.347 | R$ 2.643 | −R$ 69.791 |
| 4 | 74,0% | R$ 53.798 | R$ 6.702 | −R$ 63.089 |
| 5 | 87,0% | R$ 63.249 | R$ 10.740 | −R$ 52.349 |
| 6 | 100,0% | R$ 72.700 | R$ 14.763 | −R$ 37.586 |
| 7 | 100,0% | R$ 72.700 | R$ 14.652 | −R$ 22.934 |
| 8 | 100,0% | R$ 72.700 | R$ 14.579 | −R$ 8.355 |
| 9 | 100,0% | R$ 72.700 | R$ 14.526 | R$ 6.171 |
| 10 | 100,0% | R$ 72.700 | R$ 14.486 | R$ 20.657 |
| 11 | 100,0% | R$ 72.700 | R$ 14.455 | R$ 35.113 |
| 12 | 100,0% | R$ 72.700 | R$ 14.418 | R$ 49.531 |

Pior caixa: −R$ 72.435. Capital mínimo: investimento R$ 65.300 + prejuízo da rampa R$ 7.135 + reserva R$ 52.200 = **R$ 124.635**.

<a id="cafeteria"></a>

## Cafeteria (cafés especiais de Minas)

C · Alimentação · rampa de 6 meses, começando em 35,0% do alvo.

> Dentro da padaria, a cafeteria dispensa aluguel, reforma, contador e boa parte da equipe: o investimento cai para cerca de R$ 30 mil.

### Investimento inicial

| Item | Valor |
|---|---:|
| Caução e 1º aluguel (30 a 40 m², R$ 2.000) | R$ 4.000 |
| Reforma e balcão | R$ 12.000 |
| Máquina de espresso 2 grupos (seminova) e moedor | R$ 23.000 |
| Filtro de água, liquidificador e utensílios | R$ 3.300 |
| Geladeira expositora e vitrine de doces | R$ 8.500 |
| Forno elétrico (pão de queijo e assados) | R$ 3.500 |
| Mesas e cadeiras (6 mesas) | R$ 5.000 |
| Licenças, bombeiros e vigilância sanitária | R$ 3.500 |
| Estoque inicial | R$ 2.500 |
| Lançamento | R$ 3.000 |
| **Total** | **R$ 68.300** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Aluguel | R$ 2.000 |
| Energia | R$ 700 |
| Água e internet | R$ 280 |
| Contador | R$ 550 |
| Manutenção da máquina e controle de pragas | R$ 300 |
| Marketing | R$ 600 |
| Música ambiente (ECAD) e limpeza | R$ 350 |
| Barista líder (encarregada) (1 × salário R$ 2.400 × 1,4) | R$ 3.360 |
| Barista (1 × salário R$ 2.000 × 1,4) | R$ 2.800 |
| Atendente (2 × salário R$ 1.800 × 1,4) | R$ 5.040 |
| **Total** | **R$ 15.980** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Balcão e mesas (café + salgado ou doce) | 1.500 × R$ 24,00 | R$ 36.000 | R$ 12.780 (35,5%) | R$ 2.641 (Anexo I) | R$ 20.579 |
| Delivery próprio | 250 × R$ 35,00 | R$ 8.750 | R$ 3.412 (39,0%) | R$ 642 (Anexo I) | R$ 4.696 |
| Coffee break para empresas e eventos | 4 × R$ 800,00 | R$ 3.200 | R$ 1.536 (48,0%) | R$ 235 (Anexo I) | R$ 1.429 |
| Café em grão e presentes (marca própria) | 120 × R$ 45,00 | R$ 5.400 | R$ 3.078 (57,0%) | R$ 396 (Anexo I) | R$ 1.926 |
| **Total** | | **R$ 53.350** | **R$ 20.806** | **R$ 3.913** | **R$ 28.630** (53,7%) |

Margem de contribuição R$ 28.630 − custos fixos R$ 15.980 = **lucro de R$ 12.650 por mês** no alvo e R$ 4.408 vendendo 70%. Empata com R$ 28.836 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 35,0% | R$ 18.672 | −R$ 5.458 | −R$ 73.758 |
| 2 | 48,0% | R$ 25.608 | −R$ 1.656 | −R$ 75.414 |
| 3 | 61,0% | R$ 32.544 | R$ 2.125 | −R$ 73.289 |
| 4 | 74,0% | R$ 39.479 | R$ 5.892 | −R$ 67.397 |
| 5 | 87,0% | R$ 46.414 | R$ 9.571 | −R$ 57.826 |
| 6 | 100,0% | R$ 53.350 | R$ 13.206 | −R$ 44.619 |
| 7 | 100,0% | R$ 53.350 | R$ 13.096 | −R$ 31.523 |
| 8 | 100,0% | R$ 53.350 | R$ 13.023 | −R$ 18.501 |
| 9 | 100,0% | R$ 53.350 | R$ 12.970 | −R$ 5.531 |
| 10 | 100,0% | R$ 53.350 | R$ 12.930 | R$ 7.399 |
| 11 | 100,0% | R$ 53.350 | R$ 12.899 | R$ 20.298 |
| 12 | 100,0% | R$ 53.350 | R$ 12.874 | R$ 33.173 |

Pior caixa: −R$ 75.414. Capital mínimo: investimento R$ 68.300 + prejuízo da rampa R$ 7.114 + reserva R$ 47.940 = **R$ 123.354**.

<a id="padaria"></a>

## Padaria com café da manhã e almoço

C · Alimentação · rampa de 8 meses, começando em 35,0% do alvo.

> Começa com massa congelada de fornecedor (padaria de finalização): dispensa masseira, modeladora, cilindro, câmara de fermentação e padeiro de madrugada. Produção própria vem depois, com o caixa da operação.

### Investimento inicial

| Item | Valor |
|---|---:|
| Caução e 1º aluguel (100 a 120 m², R$ 4.200) | R$ 8.400 |
| Reforma de cozinha, produção e salão | R$ 40.000 |
| Exaustão e coifa | R$ 12.000 |
| Forno turbo a gás e batedeira planetária | R$ 17.500 |
| Fogão industrial, mesas de inox e utensílios | R$ 13.500 |
| Freezers e geladeiras (massa congelada e cozinha) | R$ 12.000 |
| Vitrine refrigerada, estufa e balcão | R$ 14.000 |
| Balcão térmico de self-service e balança aferida | R$ 13.800 |
| Mesas e cadeiras (12 mesas) | R$ 9.000 |
| Dois caixas (PDV) | R$ 3.000 |
| Projeto, alvarás, bombeiros e vigilância sanitária | R$ 7.000 |
| Estoque inicial | R$ 8.000 |
| Lançamento | R$ 6.000 |
| **Total** | **R$ 164.200** |

### Custos fixos por mês

| Item | Valor |
|---|---:|
| Aluguel | R$ 4.200 |
| IPTU | R$ 250 |
| Energia | R$ 2.200 |
| Gás | R$ 900 |
| Água e internet | R$ 580 |
| Contador | R$ 800 |
| Controle de pragas e manutenção | R$ 400 |
| Marketing | R$ 1.200 |
| ECAD, seguro e limpeza | R$ 750 |
| Manutenção de equipamentos e reposição | R$ 600 |
| Gerente da casa (1 × salário R$ 3.500 × 1,4) | R$ 4.900 |
| Cozinheira (2 × salário R$ 2.300 × 1,4) | R$ 6.440 |
| Auxiliar de cozinha (2 × salário R$ 1.800 × 1,4) | R$ 5.040 |
| Padeiro-confeiteiro (finalização) (2 × salário R$ 2.200 × 1,4) | R$ 6.160 |
| Balconista (3 × salário R$ 1.800 × 1,4) | R$ 7.560 |
| Caixa (2 × salário R$ 1.800 × 1,4) | R$ 5.040 |
| Auxiliar de limpeza (1 × salário R$ 1.700 × 1,4) | R$ 2.380 |
| **Total** | **R$ 49.400** |

### Fontes de receita no alvo

| Fonte | Volume × preço | Receita | Custo variável | Simples | Margem de contribuição |
|---|---|---:|---:|---:|---:|
| Padaria de balcão (pães, pão de queijo, frios) | 6.000 × R$ 14,00 | R$ 84.000 | R$ 33.600 (40,0%) | R$ 9.089 (Anexo I) | R$ 41.311 |
| Café da manhã mineiro (combo ou buffet) | 1.000 × R$ 28,00 | R$ 28.000 | R$ 10.080 (36,0%) | R$ 3.030 (Anexo I) | R$ 14.890 |
| Almoço por quilo e prato executivo | 2.200 × R$ 32,00 | R$ 70.400 | R$ 30.976 (44,0%) | R$ 7.618 (Anexo I) | R$ 31.806 |
| Marmitas e almoço para empresas | 800 × R$ 24,00 | R$ 19.200 | R$ 9.216 (48,0%) | R$ 2.078 (Anexo I) | R$ 7.906 |
| Encomendas (bolos, salgados de festa, coffee break) | 30 × R$ 250,00 | R$ 7.500 | R$ 3.225 (43,0%) | R$ 812 (Anexo I) | R$ 3.463 |
| **Total** | | **R$ 209.100** | **R$ 87.097** | **R$ 22.626** | **R$ 99.377** (47,5%) |

Margem de contribuição R$ 99.377 − custos fixos R$ 49.400 = **lucro de R$ 49.977 por mês** no alvo e R$ 22.216 vendendo 70%. Empata com R$ 99.745 de receita por mês.

### Primeiros 12 meses

| Mês | Ritmo | Receita | Lucro do mês | Caixa acumulado |
|---:|---:|---:|---:|---:|
| 1 | 35,0% | R$ 73.185 | −R$ 12.655 | −R$ 176.855 |
| 2 | 44,3% | R$ 92.601 | −R$ 3.184 | −R$ 180.039 |
| 3 | 53,6% | R$ 112.018 | R$ 6.241 | −R$ 173.798 |
| 4 | 62,9% | R$ 131.434 | R$ 15.633 | −R$ 158.165 |
| 5 | 72,1% | R$ 150.851 | R$ 25.000 | −R$ 133.164 |
| 6 | 81,4% | R$ 170.267 | R$ 34.349 | −R$ 98.815 |
| 7 | 90,7% | R$ 189.684 | R$ 43.684 | −R$ 55.131 |
| 8 | 100,0% | R$ 209.100 | R$ 53.007 | −R$ 2.124 |
| 9 | 100,0% | R$ 209.100 | R$ 52.866 | R$ 50.742 |
| 10 | 100,0% | R$ 209.100 | R$ 52.533 | R$ 103.275 |
| 11 | 100,0% | R$ 209.100 | R$ 52.228 | R$ 155.503 |
| 12 | 100,0% | R$ 209.100 | R$ 51.989 | R$ 207.492 |

Pior caixa: −R$ 180.039. Capital mínimo: investimento R$ 164.200 + prejuízo da rampa R$ 15.839 + reserva R$ 148.200 = **R$ 328.239**.
