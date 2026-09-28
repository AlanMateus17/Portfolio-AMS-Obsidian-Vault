---
tags: [planejamento, portfolio-ams]
tipo: planejamento
status: completo
---

# Plano Mestre — Frentes de Estudo, Negócio e Renda

**Objetivo:** mapear todas as frentes ativas e potenciais, definir produtos/serviços e fontes de renda de cada uma, estimar escalabilidade, e a partir disso decidir prioridade de abertura formal, prioridade de execução e o ponto em que compensa contratar funcionário — tudo isso respeitando sua restrição real: ~9h/semana livres, carga de professor EMTI, e duas graduações em andamento (ADS + Licenciatura em Matemática).

---

## 0. Como este plano está organizado

Cada frente tem:
- **O que é / produtos e serviços**
- **Fontes de renda** (como o dinheiro entra)
- **Como especular a escalabilidade** (o método pra você mesmo estimar teto de crescimento)
- **Capital e formalização necessários**
- **Prioridade de abertura** (1 = abrir primeiro)
- **Prioridade de execução** (1 = dedicar tempo primeiro)
- **Gatilho para contratar funcionário**

No final: matriz-resumo, cronograma de fases, e a lógica de por que essa ordem.

---

## 1. Carreira Pública — Professor Estadual (Informática + Matemática)

**O que é:** sua base de estabilidade. Já atua no EMTI de Informática em Barbacena; a Licenciatura em Matemática abre uma segunda porta de entrada (dobra a superfície de vagas/PSS/concursos possíveis).

**Produtos e serviços:** aulas, as 180 apostilas já produzidas (ativo reaproveitável em outras frentes — ver Frente 4).

**Fontes de renda:** salário fixo (designação/PSS até concursar), possibilidade futura de dobrar carga horária ou lecionar em duas disciplinas quando tiver as duas licenciaturas.

**Escalabilidade:** baixa por natureza (teto = carga horária + tabela salarial), mas é o que sustenta seu fluxo de caixa pessoal enquanto as empresas ainda não pagam por si. Não pense nela como "frente de crescimento" — pense como **piso de segurança** que compra seu tempo pra escalar as outras.

**Capital/formalização:** nenhum. Prioridade é **concluir a Licenciatura em Matemática**, não abrir nada.

**Prioridade de abertura:** N/A.
**Prioridade de execução:** **Alta e contínua** — nunca abandonar até que ao menos uma frente empresarial substitua esse piso com folga (regra de bolso: renda líquida da empresa > 2x seu salário atual, sustentada por 6 meses seguidos, antes de considerar redução de carga na docência).
**Funcionário:** não se aplica.

---

## 2. Grupo AMtech Digital — Assistência Técnica (conserto de celulares)

**O que é:** a frente mais tangível e a que gera caixa mais rápido. Reparo de celulares com foco Apple/Xiaomi, já com plano detalhado (ferramentas por nível, softwares, fluxo de atendimento em 6 etapas).

**Produtos e serviços:** troca de tela/bateria, diagnóstico, desbloqueio, reparo de placa (nível avançado = microssolda, maior margem), venda de peças e acessórios, planos de manutenção preventiva para pequenas empresas locais (frotas de celular corporativo).

**Fontes de renda:** valor por serviço (ticket médio + peça), venda de peças/acessórios avulsa, contratos recorrentes de manutenção B2B.

**Como especular a escalabilidade:** escalabilidade **física e de tempo**, não digital — o teto é (nº de aparelhos que cabem na fila) × (ticket médio) × (dias úteis). Para estimar: pegue o tempo médio de reparo por categoria (troca de tela ≈ 30-40min; microssolda ≈ 2-4h) e calcule quantos atendimentos cabem nas horas que você (ou um técnico) tem disponíveis por semana. Isso te dá o teto de faturamento por pessoa na bancada — a escala real só vem multiplicando pessoas/bancadas.

**Capital/formalização:** baixo-médio (ferramentas nível 1 já mapeadas). **MEI, CNAE 95.21-5/00**, é rápido, barato e você já tem o passo a passo pronto.

**Prioridade de abertura:** **1 (mais alta do grupo empresarial)** — é a que exige menos capital, menos tempo de maturação e gera caixa em semanas, não meses.
**Prioridade de execução:** **Alta no curto prazo** — mas com teto de tempo definido: não deixe ela consumir as horas que precisam ir para o AM Kaixara. Trate como "motor de caixa", não como projeto de vida.
**Funcionário:** este é o candidato mais provável a **primeiro funcionário do grupo inteiro**. Gatilho objetivo: fila de espera consistente acima de 5-7 dias úteis por 3 meses seguidos, ou perda de clientes por falta de capacidade — nesse ponto, contratar um técnico júnior paga a própria conta rápido porque o serviço é imediatamente faturável.

---

## 3. Grupo AMtech Digital — Ecossistema Aura (Software / SaaS)

Esta é uma frente com 5 produtos que compartilham ~85% da base técnica. Vou detalhar cada um, mas a decisão de prioridade é sobre o conjunto.

### 3.1 AM Kaixara (carro-chefe)
**O que é:** PDV + gestão de estoque, multi-tenant, já em Sprint 3-4 (rumo a JWT).
**Produtos:** módulos por pacote comercial (venda, estoque, dashboard, fiscal), possivelmente pacotes por porte de cliente.
**Renda:** assinatura mensal recorrente (SaaS/MRR) por tenant, possível taxa de setup/onboarding para pequenos comércios locais.
**Escalabilidade:** **alta** — é software, custo marginal por cliente novo é quase zero depois de pronto. Para especular o teto: estime nº de pequenos comércios em Barbacena/região que usam PDV manual ou concorrente fraco, multiplique por sua mensalidade-alvo. Isso te dá o SOM (mercado que você realmente alcança) local antes de pensar em expandir região.
**Prioridade:** é o produto de maior potencial de renda recorrente do portfólio inteiro — deve continuar recebendo a maior fatia das suas horas de desenvolvimento.

### 3.2 aura-licensing (infraestrutura interna)
**O que é:** motor de cobrança/gating de módulos usado por todos os outros produtos.
**Renda:** não gera receita direta — é o que viabiliza cobrança recorrente dos outros. Trate como pré-requisito técnico, não como "produto" separado na priorização comercial.

### 3.3 AM Rotara
**O que é:** compartilha 70-85% da base do AM Kaixara.
**Renda:** assinatura + possível comissão por pedido, dependendo do modelo escolhido.
**Escalabilidade:** alta, mas **dependente do AM Kaixara estar maduro primeiro** (reaproveitamento de base é a vantagem competitiva dele — lançar antes disso desperdiça a economia de escala).

### 3.4 AM Rendara
**O que é:** finanças pessoais/corporativas com ARCA, Barsi, Value Investing; camada de consultoria premium.
**Renda:** assinatura do app (self-service) + consultoria paga (bloqueada até certificação).
**Escalabilidade:** alta no tier self-service; o tier de consultoria tem teto humano (1 pessoa = X clientes atendidos por mês), a menos que você contrate outros consultores certificados depois.
**Bloqueio regulatório:** para a camada de consultoria, você precisa de **CEA ou CFP** (mais rápido que qualquer pós) e registro como Consultor de Valores Mobiliários pessoa física na CVM (registro gratuito). Sem isso, só dá pra vender a ferramenta, não a consultoria.

### 3.5 Momentos/Cupido
**O que é:** plataforma B2C de relacionamento (motor de compatibilidade, sites de casal, cartão NFC físico).
**Renda:** modelo de afiliados inspirado em Zola, venda do cartão NFC físico, possíveis assinaturas para recursos premium.
**Escalabilidade:** alta em tese (B2C digital), mas é a frente com **maior dependência de marketing/aquisição de usuários** — diferente do AM Kaixara, que pode crescer por venda direta local, este precisa de tração de público, o que é um tipo de esforço diferente do que você tem feito até aqui.

**Capital/formalização do conjunto Aura:** baixo capital financeiro, alto capital de tempo. Formalização: **PJ (ME/Simples Nacional)** — SaaS B2B com faturamento recorrente tende a estourar o teto do MEI rápido se dois ou três produtos decolarem juntos, então vale já nascer em ME quando a primeira assinatura for fechada, para não ter que migrar no meio de contratos. Detalhamento completo de CNAE e custo em [[estrutura-juridica-amtech]].

**Prioridade de abertura formal:** **2** — depois da assistência técnica (que é mais rápida/barata de formalizar), mas antes de qualquer outra frente, porque é aqui que está o maior potencial de receita recorrente do grupo todo.

**Prioridade de execução dentro do conjunto Aura:**
1. AM Kaixara até MVP vendável (prioridade máxima — é o que já está andando)
2. aura-licensing (pré-requisito técnico, desenvolver junto)
3. AM Rotara (só depois do AM Kaixara maduro, para aproveitar a base)
4. AM Rendara self-service (pode rodar em paralelo, ritmo mais lento)
5. AM Rendara consultoria (só após CEA/CFP — planejar como marco de médio prazo)
6. Momentos/Cupido (menor prioridade agora — exige esforço de marketing que compete com as outras frentes por tempo)

**Funcionário:** gatilho é **financeiro, não de volume de tarefas** — contrate o primeiro desenvolvedor quando o MRR (receita recorrente mensal) do AM Kaixara cobrir o salário dele com folga (regra de bolso: MRR ≥ 3x o custo do salário, pra sobrar caixa de segurança). Antes disso, contratar dev é queimar caixa que ainda não existe. Suporte técnico/atendimento a cliente pode vir antes do segundo dev, se o volume de tickets começar a tomar seu tempo de desenvolvimento.

---

## 4. Grupo AMtech Digital — Educação (apostilas, cursos, mentoria)

**O que é:** monetizar o que você já produziu (180 apostilas EMTI) e sua experiência como professor + desenvolvedor.

**Produtos e serviços:** venda das apostilas/material didático, cursos preparatórios (concurso, lógica de programação básica), mentoria paga para devs juniores, parcerias com escolas/cursinhos.

**Fontes de renda:** venda direta (Hotmart/plataforma própria), mentorias avulsas, parcerias institucionais.

**Como especular a escalabilidade:** **média-alta** porque o produto (apostila/curso gravado) já existe — o custo marginal de vender pra mais uma pessoa é quase zero. O teto real é de audiência/distribuição, não de produção. Estime pelo tamanho do público que você já alcança (alunos, redes do grupo, comunidade de concurseiros) vs preço unitário.

**Capital/formalização:** baixíssimo. Pode operar via MEI (mesmo CNPJ da assistência técnica, se o CNAE permitir, ou CNAE secundário de "outras atividades de ensino").

**Prioridade de abertura:** **3** — simples de formalizar, mas não é urgente porque não depende de estrutura física.
**Prioridade de execução:** **média** — é "dinheiro parado" no sentido de que o material já existe; vale um sprint curto e isolado (ex: 1 fim de semana) para transformar as apostilas em um produto vendável, sem tirar foco do AM Kaixara no dia a dia.
**Funcionário:** raramente necessário; se escalar, terceirize edição/design/gravação em vez de contratar CLT.

---

## 5. Freelance Web Dev (sites para pequenos negócios locais)

**O que é:** já mapeado com Claude anteriormente — WooCommerce + Hostinger + Mercado Pago, preservando receita de revenda de hospedagem.

**Produtos e serviços:** criação de sites/lojas, manutenção mensal, revenda de hospedagem/domínio.

**Fontes de renda:** projeto fechado (pagamento único) + recorrência de hospedagem/manutenção.

**Como especular a escalabilidade:** **baixa-média** enquanto for você sozinho fazendo (teto = nº de projetos que cabem no seu tempo livre × ticket médio). Escala de verdade só viraria "agência" com subcontratação — o que competiria diretamente pelo seu tempo de gestão com o Aura.

**Capital/formalização:** baixo. MEI simples (mesmo CNPJ pode ter esse CNAE como secundário).

**Prioridade de abertura:** **4** — fácil de formalizar, mas não corre risco de "perder a janela" se atrasar.
**Prioridade de execução:** **média-baixa** — é uma boa frente de caixa rápido por projeto pontual, mas cada projeto puxa horas diretamente do desenvolvimento do Aura. Recomendo tratá-la como **oportunista** (aceitar projetos quando aparecerem via indicação, sem prospecção ativa) até o AM Kaixara estar gerando receita própria.
**Funcionário:** subcontratar freelancer pontual apenas se o pipeline de projetos exceder sua capacidade — não vale contratar CLT para isso.

---

## 6. Dropshipping / Marketing de Afiliados

**O que é:** já mapeado — operação em Mercado Livre, Amazon, Shopee (dropship) + afiliados (Amazon Associados, ML Afiliados, Hotmart etc).

**Produtos e serviços:** revenda sem estoque próprio, comissão por indicação de produtos de terceiros.

**Fontes de renda:** margem de revenda (dropship) ou comissão (afiliados).

**Como especular a escalabilidade:** **alta em tese, mas mercado saturado e dependente de tráfego pago constante** — diferente das outras frentes, aqui o "produto" não é seu, então a vantagem competitiva é só operacional/marketing. Estimativa de teto exige simular CAC (custo de aquisição por cliente) vs margem por venda; se a margem não cobrir o CAC com folga, a operação não escala, só queima caixa.

**Capital/formalização:** afiliados pode começar com CPF; dropship recorrente exige **MEI (só nacional) ou ME (se usar fornecedor internacional tipo AliExpress/CJ)**.

**Prioridade de abertura:** **5** — mais barato formalizar (afiliado nem precisa de CNPJ pra começar), mas também o menor retorno esperado dado seu tempo disponível.
**Prioridade de execução:** **baixa** — não é sua competência central e compete por tempo de marketing/tráfego que você não tem sobrando. Só vale retomar se sobrar tempo real depois que as frentes acima estiverem estáveis, ou se quiser rodar em paralelo como afiliado (CPF, zero fricção) sem se comprometer com estoque/logística de dropship.
**Funcionário:** só faria sentido contratar gestor de tráfego se a operação já estivesse validada e lucrativa — não antes.

---

## 7. Matriz-resumo de prioridades

| Frente | Prioridade de abertura | Prioridade de execução | Escalabilidade | 1º gatilho de contratação |
|---|---|---|---|---|
| Carreira docente (Matemática) | — | Alta (contínua) | Baixa | N/A |
| Assistência técnica | **1** | Alta (curto prazo) | Baixa-média (física) | Fila > 5-7 dias por 3 meses |
| Ecossistema Aura (AM Kaixara primeiro) | **2** | **Máxima** | Alta | MRR ≥ 3x salário de um dev |
| Educação (apostilas/cursos) | 3 | Média | Média-alta | Raramente necessário |
| Freelance web dev | 4 | Média-baixa (oportunista) | Baixa-média | Só subcontratação pontual |
| Dropshipping/afiliados | 5 | Baixa | Alta em tese, arriscada | Só se validado e lucrativo |
| AM Rendara consultoria | (depende de CEA/CFP) | Baixa por ora | Alta (limitada por pessoa) | Após certificação + demanda |

---

## 8. Cronograma sugerido por fases

**Fase 0 — Agora até ~3 meses:**
- Formalizar MEI com CNAE 95.21-5/00 (assistência técnica) — abre caixa rápido.
- Continuar AM Kaixara até fechar autenticação JWT e MVP vendável.
- Sprint curto (1 fim de semana) para empacotar as apostilas como produto vendável (Frente 4) — baixo esforço, ativo já pronto.
- Freelance web dev e afiliados: só aceitar oportunidades que aparecerem sem prospecção ativa.

**Fase 1 — ~3 a 9 meses:**
- Primeiros clientes pagantes do AM Kaixara (comércios locais em Barbacena/região).
- Avaliar abrir ME (Simples Nacional) para o CNPJ de software assim que a primeira assinatura recorrente for fechada.
- Observar fila da assistência técnica — se estourar 5-7 dias, iniciar processo de contratação do primeiro técnico.

**Fase 2 — ~9 a 18 meses:**
- Expandir base de clientes AM Kaixara; iniciar AM Rotara reaproveitando a base técnica.
- Avaliar início do estudo para CEA (mais rápido que CFP) visando destravar AM Rendara Consultoria.
- Decidir sobre primeiro dev contratado, com base na regra de MRR ≥ 3x salário.

**Fase 3 — 18+ meses:**
- AM Rendara Consultoria (pós-certificação), Momentos/Cupido (se houver capacidade de marketing dedicada).
- Reavaliar se compensa reduzir carga horária da docência, só depois que a renda empresarial líquida sustentar 2x o salário atual por 6 meses seguidos.

---

## 9. Lógica por trás da ordem

A ordem não segue "maior potencial primeiro" — segue **tempo até o primeiro real (caixa) vs seu tempo disponível (9h/semana)**. Assistência técnica entra primeiro porque de todas as frentes é a que menos depende de você ter tempo de desenvolvimento sobrando: uma vez formalizada e com ferramenta básica, ela gera caixa por conta própria. O Aura entra em segundo lugar não porque tem menos potencial — pelo contrário, é a maior aposta de longo prazo — mas porque o tempo de maturação até o primeiro cliente pagante é mais longo, então ela precisa começar a rodar em paralelo desde já, sem esperar a assistência técnica "terminar" (ela nunca termina, é operação contínua).

As frentes de menor prioridade (freela, dropship) não são descartadas — são tratadas como **oportunistas**: você aproveita se aparecer, mas não investe prospecção ativa nelas, porque cada hora ali é uma hora a menos no AM Kaixara, que é onde está o maior efeito composto (uma vez pronto, o produto vende pra mais um cliente sem custo adicional de desenvolvimento — o que nenhuma das outras frentes, exceto educação digital, tem).
