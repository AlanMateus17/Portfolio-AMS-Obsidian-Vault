<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 16 · Negócios do grupo (Barbacena)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Os negócios do grupo usam o AM Gestão, a frota de entregas (quando existir) e o mesmo caixa de medição.

**14 blocos** · 5 precisam de conta · 12 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_neg["Negócios do grupo (Barbacena)"]
    n_nsoft["AMtech Software (projetos e SaaS)"]
    n_nloja["Loja AMtech (assistência)"]
    n_npecas["Peças sem estoque (sob encomenda)"]
    n_nponto["Ponto de retirada (Shopee e ML)"]
    n_nmaker["AMtech Maker (robótica)"]
    n_nentr["AM Entregas (moto e carro)"]
    n_nflex["Mercado Envios Flex"]
    n_ndeliv["AM Delivery (várias empresas)"]
    n_ncnpj["2 CNPJs por frente"]
    n_nplan["Planejador do Grupo"]
    n_nanatel["Anatel e Inmetro"]
    n_radar["Radar de revenda"]
    n_nseg["AMtech Segurança (pentest)"]
    n_erpnext["ERPNext (negócios físicos)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_ocatal["Portfólio de ofertas"]
    n_oesteira["Esteira de ofertas"]
  end
  subgraph L_pub["Público e canais"]
    n_ogbp["Google Perfil da Empresa"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_painel["Painel de lucro (Grafana)"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_cnpj["CNPJ (futuro)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_sites["Sites para pequenas empresas"]
  end
  subgraph L_app["Aplicação: AM Gestão e as suítes AM"]
    n_nkaix["AM Gestão · Caixa (PDV e cardápio)"]
    n_nobra["AM Obra (diário, medição, compras)"]
    n_nrot["AM Gestão · Pedidos (entregas)"]
  end
  subgraph L_obs["Observabilidade"]
    n_graf["Grafana"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_relpent["Relatório de pentest (CVSS)"]
  end
  n_nsoft -->|"constrói"| n_nkaix
  n_nsoft -->|"constrói"| n_nrot
  n_sites -->|"vira serviço da empresa"| n_nsoft
  n_ncnpj -->|"AMtech Tecnologia"| n_nsoft
  n_oesteira -->|"lança"| n_nsoft
  n_nseg -->|"mesmos clientes"| n_nsoft
  n_nobra -->|"produto"| n_nsoft
  n_nloja -->|"mesmo balcão"| n_nponto
  n_npecas -->|"vendidas no balcão"| n_nloja
  n_nmaker -->|"usa a bancada"| n_nloja
  n_nkaix -->|"ordens de serviço"| n_nloja
  n_ncnpj -->|"AMtech Tecnologia"| n_nloja
  n_ogbp -->|"presença local"| n_nloja
  n_nponto -->|"vendedores da cidade"| n_nentr
  n_nanatel -->|"homologação"| n_nmaker
  n_nentr -->|"entrega o Flex"| n_nflex
  n_nentr -->|"frota"| n_ndeliv
  n_nrot -->|"roteiriza"| n_nentr
  n_ncnpj -->|"AM Logística"| n_nentr
  n_nrot -->|"app e painel"| n_ndeliv
  n_cnpj -->|"vira"| n_ncnpj
  n_nplan -->|"portões entre fases"| n_ncnpj
  n_ocatal -->|"negócios físicos"| n_nplan
  n_graf -->|"resultado real"| n_nplan
  n_radar -->|"lucro por hora"| n_painel
  n_relpent -->|"entregável"| n_nseg
  n_erpnext -->|"referência do AM Gestão"| n_nkaix
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_nsoft,n_nloja,n_npecas,n_nponto,n_nmaker,n_nentr,n_nflex,n_ndeliv,n_ncnpj,n_nplan,n_nanatel,n_radar,n_nseg,n_erpnext desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [AMtech Software (projetos e SaaS)](#nsoft) | Remoto · futuro | Software sob encomenda, sites, manutenção e SaaS AM. Primeiro CNPJ do grupo (ME no Simples, Anexo III pelo Fator R). Ver docs/negocios/01. | passo 57.2 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Loja AMtech (assistência)](#nloja) | Físico · futuro | Loja de 30 a 50 m² com bancada técnica, mostruário e balcão de pacotes. Une assistência, peças e ponto de retirada em um aluguel só. | passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Peças sem estoque (sob encomenda)](#npecas) | Físico · futuro | Peças e acessórios comprados só depois do sinal do cliente ou enviados pelo fornecedor. A margem está no serviço, não na peça. | passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Ponto de retirada (Shopee e ML)](#nponto) | Físico · precisa de conta · futuro | Agência Shopee (R$ 0,70 a 0,60 por pacote nas primeiras faixas) e Agência Mercado Livre (valor na proposta). Rende pouco sozinho; o valor é o movimento na loja. | passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [AMtech Maker (robótica)](#nmaker) | Físico · futuro | Automação residencial, empresarial, rural e virtual, e kits de robótica educacional. Começa por serviço com aparelhos homologados; produto com rádio só depois da Anatel. | passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [AM Entregas (moto e carro)](#nentr) | Físico · futuro | Última milha em Barbacena: entregas para empresas, Flex dos vendedores locais, coleta para as agências e rotas fixas. Motofretistas pela Lei 12.009/2009. | passo 57.4 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Mercado Envios Flex](#nflex) | Remoto · precisa de conta · futuro | Entrega no mesmo dia dos vendedores do Mercado Livre da cidade, terceirizada para a AM Entregas e cobrada por pacote. | passo 57.4 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [AM Delivery (várias empresas)](#ndeliv) | Remoto · futuro | App de pedidos de restaurantes e lojas da cidade com comissão de 8% e entrega pela AM Entregas. O lucro está na comissão, não na taxa de entrega. | passo 57.5 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [2 CNPJs por frente](#ncnpj) | Remoto · precisa de conta · futuro | AMtech Tecnologia (software, Campo e Maker) e AM Logística (entregas), cada um com os seus CNAEs, conta e caixa. Holding só quando houver patrimônio. | passo 52.1 · Quando a renda pedir (começa quando: a renda passou do valor de virada definido com o contador) |
| [Planejador do Grupo](#nplan) | Remoto · futuro | Artefato e motor tools/negocios/financas.py: investimento, ponto de equilíbrio, rampa, retorno e capital mínimo de cada negócio, com o mesmo cálculo. | passo 57.1 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Anatel e Inmetro](#nanatel) | Remoto · precisa de conta · futuro | Homologação de produto próprio com Wi-Fi ou Bluetooth e, se o kit for brinquedo, certificação do Inmetro. | passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Radar de revenda](#radar) | Local | Lê os alertas de busca salvos (OLX, Mercado Livre, Facebook, Estante Virtual) que chegam ao Gmail, compara com o preço de referência e avisa no Telegram só o que passa da hora mínima. Nunca compra nem fala com vendedor. | passo 11.4 · Semana 4 · nov/2026 |
| [AMtech Segurança (pentest)](#nseg) | Remoto · futuro | Testes de segurança para empresas: laudo dos sites primeiro, pentest completo depois da OSCP, com contrato revisado, seguro e reteste. | passo 59.19 · Dez/2026 em diante: 1 bloco de 1 h por semana dentro do estudo da manhã; serviços pagos só depois dos portões (eJPT, ensaio, OSCP) |
| [ERPNext (negócios físicos)](#erpnext) | Remoto · precisa de conta | ERP aberto para os negócios físicos até o AM Gestão cobrir e referência de mercado ao desenhar o Caixa. | passo 57.8 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |

<a id="nsoft"></a>

### AMtech Software (projetos e SaaS)

*Remoto · futuro*

Software sob encomenda, sites, manutenção e SaaS AM. Primeiro CNPJ do grupo (ME no Simples, Anexo III pelo Fator R). Ver docs/negocios/01.

**Quando entra:** passo 57.2 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AM Gestão · Caixa (PDV e cardápio)](11-app.md#nkaix) | Aplicação: AM Gestão e as suítes AM | constrói |
| → envia para | [AM Gestão · Pedidos (entregas)](11-app.md#nrot) | Aplicação: AM Gestão e as suítes AM | constrói |
| ← recebe de | [Sites para pequenas empresas](17-prod.md#sites) | Produtos (o que você vende) | vira serviço da empresa |
| ← recebe de | [2 CNPJs por frente](16-neg.md#ncnpj) | Negócios do grupo (Barbacena) | AMtech Tecnologia |
| ← recebe de | [Esteira de ofertas](23-oper.md#oesteira) | Operação do grupo (esteira, marca, qualidade) | lança |
| ← recebe de | [AMtech Segurança (pentest)](16-neg.md#nseg) | Negócios do grupo (Barbacena) | mesmos clientes |
| ← recebe de | [AM Obra (diário, medição, compras)](11-app.md#nobra) | Aplicação: AM Gestão e as suítes AM | produto |

<a id="nloja"></a>

### Loja AMtech (assistência)

*Físico · futuro*

Loja de 30 a 50 m² com bancada técnica, mostruário e balcão de pacotes. Une assistência, peças e ponto de retirada em um aluguel só.

**Quando entra:** passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ponto de retirada (Shopee e ML)](16-neg.md#nponto) | Negócios do grupo (Barbacena) | mesmo balcão |
| ← recebe de | [Peças sem estoque (sob encomenda)](16-neg.md#npecas) | Negócios do grupo (Barbacena) | vendidas no balcão |
| ← recebe de | [AMtech Maker (robótica)](16-neg.md#nmaker) | Negócios do grupo (Barbacena) | usa a bancada |
| ← recebe de | [AM Gestão · Caixa (PDV e cardápio)](11-app.md#nkaix) | Aplicação: AM Gestão e as suítes AM | ordens de serviço |
| ← recebe de | [2 CNPJs por frente](16-neg.md#ncnpj) | Negócios do grupo (Barbacena) | AMtech Tecnologia |
| ← recebe de | [Google Perfil da Empresa](22-pub.md#ogbp) | Público e canais | presença local |

<a id="npecas"></a>

### Peças sem estoque (sob encomenda)

*Físico · futuro*

Peças e acessórios comprados só depois do sinal do cliente ou enviados pelo fornecedor. A margem está no serviço, não na peça.

**Quando entra:** passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Loja AMtech (assistência)](16-neg.md#nloja) | Negócios do grupo (Barbacena) | vendidas no balcão |

<a id="nponto"></a>

### Ponto de retirada (Shopee e ML)

*Físico · precisa de conta · futuro*

Agência Shopee (R$ 0,70 a 0,60 por pacote nas primeiras faixas) e Agência Mercado Livre (valor na proposta). Rende pouco sozinho; o valor é o movimento na loja.

**Quando entra:** passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AM Entregas (moto e carro)](16-neg.md#nentr) | Negócios do grupo (Barbacena) | vendedores da cidade |
| ← recebe de | [Loja AMtech (assistência)](16-neg.md#nloja) | Negócios do grupo (Barbacena) | mesmo balcão |

<a id="nmaker"></a>

### AMtech Maker (robótica)

*Físico · futuro*

Automação residencial, empresarial, rural e virtual, e kits de robótica educacional. Começa por serviço com aparelhos homologados; produto com rádio só depois da Anatel.

**Quando entra:** passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Loja AMtech (assistência)](16-neg.md#nloja) | Negócios do grupo (Barbacena) | usa a bancada |
| ← recebe de | [Anatel e Inmetro](16-neg.md#nanatel) | Negócios do grupo (Barbacena) | homologação |

<a id="nentr"></a>

### AM Entregas (moto e carro)

*Físico · futuro*

Última milha em Barbacena: entregas para empresas, Flex dos vendedores locais, coleta para as agências e rotas fixas. Motofretistas pela Lei 12.009/2009.

**Quando entra:** passo 57.4 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mercado Envios Flex](16-neg.md#nflex) | Negócios do grupo (Barbacena) | entrega o Flex |
| → envia para | [AM Delivery (várias empresas)](16-neg.md#ndeliv) | Negócios do grupo (Barbacena) | frota |
| ← recebe de | [Ponto de retirada (Shopee e ML)](16-neg.md#nponto) | Negócios do grupo (Barbacena) | vendedores da cidade |
| ← recebe de | [AM Gestão · Pedidos (entregas)](11-app.md#nrot) | Aplicação: AM Gestão e as suítes AM | roteiriza |
| ← recebe de | [2 CNPJs por frente](16-neg.md#ncnpj) | Negócios do grupo (Barbacena) | AM Logística |

<a id="nflex"></a>

### Mercado Envios Flex

*Remoto · precisa de conta · futuro*

Entrega no mesmo dia dos vendedores do Mercado Livre da cidade, terceirizada para a AM Entregas e cobrada por pacote.

**Quando entra:** passo 57.4 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [AM Entregas (moto e carro)](16-neg.md#nentr) | Negócios do grupo (Barbacena) | entrega o Flex |

<a id="ndeliv"></a>

### AM Delivery (várias empresas)

*Remoto · futuro*

App de pedidos de restaurantes e lojas da cidade com comissão de 8% e entrega pela AM Entregas. O lucro está na comissão, não na taxa de entrega.

**Quando entra:** passo 57.5 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [AM Entregas (moto e carro)](16-neg.md#nentr) | Negócios do grupo (Barbacena) | frota |
| ← recebe de | [AM Gestão · Pedidos (entregas)](11-app.md#nrot) | Aplicação: AM Gestão e as suítes AM | app e painel |

<a id="ncnpj"></a>

### 2 CNPJs por frente

*Remoto · precisa de conta · futuro*

AMtech Tecnologia (software, Campo e Maker) e AM Logística (entregas), cada um com os seus CNAEs, conta e caixa. Holding só quando houver patrimônio.

**Quando entra:** passo 52.1 · Quando a renda pedir (começa quando: a renda passou do valor de virada definido com o contador) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AMtech Software (projetos e SaaS)](16-neg.md#nsoft) | Negócios do grupo (Barbacena) | AMtech Tecnologia |
| → envia para | [AM Entregas (moto e carro)](16-neg.md#nentr) | Negócios do grupo (Barbacena) | AM Logística |
| → envia para | [Loja AMtech (assistência)](16-neg.md#nloja) | Negócios do grupo (Barbacena) | AMtech Tecnologia |
| ← recebe de | [CNPJ (futuro)](19-emp.md#cnpj) | Pessoa física: impostos e finanças | vira |
| ← recebe de | [Planejador do Grupo](16-neg.md#nplan) | Negócios do grupo (Barbacena) | portões entre fases |

<a id="nplan"></a>

### Planejador do Grupo

*Remoto · futuro*

Artefato e motor tools/negocios/financas.py: investimento, ponto de equilíbrio, rampa, retorno e capital mínimo de cada negócio, com o mesmo cálculo.

**Quando entra:** passo 57.1 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [2 CNPJs por frente](16-neg.md#ncnpj) | Negócios do grupo (Barbacena) | portões entre fases |
| ← recebe de | [Portfólio de ofertas](23-oper.md#ocatal) | Operação do grupo (esteira, marca, qualidade) | negócios físicos |
| ← recebe de | [Grafana](10-obs.md#graf) | Observabilidade | resultado real |

<a id="nanatel"></a>

### Anatel e Inmetro

*Remoto · precisa de conta · futuro*

Homologação de produto próprio com Wi-Fi ou Bluetooth e, se o kit for brinquedo, certificação do Inmetro.

**Quando entra:** passo 57.3 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AMtech Maker (robótica)](16-neg.md#nmaker) | Negócios do grupo (Barbacena) | homologação |

<a id="radar"></a>

### Radar de revenda

*Local*

Lê os alertas de busca salvos (OLX, Mercado Livre, Facebook, Estante Virtual) que chegam ao Gmail, compara com o preço de referência e avisa no Telegram só o que passa da hora mínima. Nunca compra nem fala com vendedor.

**Quando entra:** passo 11.4 · Semana 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Painel de lucro (Grafana)](21-mkt.md#painel) | Marketing, automação e medição | lucro por hora |

<a id="nseg"></a>

### AMtech Segurança (pentest)

*Remoto · futuro*

Testes de segurança para empresas: laudo dos sites primeiro, pentest completo depois da OSCP, com contrato revisado, seguro e reteste.

**Quando entra:** passo 59.19 · Dez/2026 em diante: 1 bloco de 1 h por semana dentro do estudo da manhã; serviços pagos só depois dos portões (eJPT, ensaio, OSCP) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AMtech Software (projetos e SaaS)](16-neg.md#nsoft) | Negócios do grupo (Barbacena) | mesmos clientes |
| ← recebe de | [Relatório de pentest (CVSS)](02-seg.md#relpent) | Segurança e cofre | entregável |

<a id="erpnext"></a>

### ERPNext (negócios físicos)

*Remoto · precisa de conta*

ERP aberto para os negócios físicos até o AM Gestão cobrir e referência de mercado ao desenhar o Caixa.

**Quando entra:** passo 57.8 · Fase A: 12 a 18 meses; B: mais 12 a 18 (sem restaurantes desde 20/11/2026) (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [AM Gestão · Caixa (PDV e cardápio)](11-app.md#nkaix) | Aplicação: AM Gestão e as suítes AM | referência do AM Gestão |

---

[↑ Camada 17 · Produtos (o que você vende)](17-prod.md) · [↓ Camada 15 · Editora AMS Silva (produção de livros)](15-editora.md)
