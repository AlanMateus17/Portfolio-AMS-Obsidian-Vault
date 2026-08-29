---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AuraObra — Documento de Projeto Final (Nome provisório)
### Sistema de Vendas na Planta, Construção Personalizada e Gestão de Obra

Segue a estrutura fixa do [[template-documento-projeto-final]].

---

## 1. Visão do produto

Plataforma para construtora/imobiliária que cobre dois modelos de negócio ao mesmo tempo: **venda de unidade na planta** (incorporação, várias unidades, um projeto padrão) e **construção de casa personalizada** (projeto único por cliente, com customização de acabamento). É o sistema do portfólio com maior exposição jurídica — contrato de alto valor, regras legais específicas de cancelamento (Lei 13.786/2018) — e por isso o que exige mais rigor de conformidade antes de qualquer lançamento comercial.

**Diferencial de inovação:** sistemas de gestão imobiliária no mercado tratam venda na planta e construção sob encomenda como produtos separados (CRM de venda de um lado, gestão de obra de outro, sem ligação). Aqui os dois compartilham a mesma base — cliente, contrato, cronograma de pagamento, acompanhamento de obra — porque estruturalmente são o mesmo problema (venda de algo que ainda não existe fisicamente, entregue ao longo do tempo) com graus diferentes de personalização.

---

## 2. Funcionalidades completas (estado final)

### 2.1 CRM e vendas
- Funil de vendas com lead, corretor responsável, follow-up
- Catálogo de empreendimento na planta: unidades disponíveis, planta baixa, tabela de preço, simulação de financiamento
- Reserva de unidade com sinal e prazo de validade

### 2.2 Contrato e conformidade legal
- Geração de contrato de promessa de compra e venda, com **quadro-resumo** obrigatório por lei, destacando de forma clara os valores, prazos e condições de retenção em caso de distrato
- Assinatura eletrônica juridicamente válida (provedor a definir — DocuSign/Clicksign/D4Sign)
- Módulo de distrato em conformidade com a Lei 13.786/2018: cálculo de retenção (até 25%, ou até 50% se a incorporação estiver sob regime de patrimônio de afetação), prazo de devolução em até 180 dias, direito de arrependimento de 7 dias corridos se a venda ocorreu fora do estande de vendas
- Cálculo automático de tolerância de atraso de entrega de até 180 dias sem caracterizar descumprimento contratual pela construtora, com gatilho de alerta quando esse prazo se aproxima do limite

### 2.3 Pagamento e financeiro
- Fluxo de pagamento parcelado: entrada, parcelas mensais, parcelas balão (reforço anual/semestral), saldo financiado na entrega
- Emissão de boleto/carnê por parcela
- Integração de simulação de financiamento bancário (informativa, sem processar o financiamento em si)

### 2.4 Casa personalizada
- Configurador de escolha de planta/acabamento, com impacto de custo por opção selecionada
- Orçamento gerado dinamicamente conforme a customização escolhida pelo cliente

### 2.5 Gestão de obra
- Cronograma físico-financeiro por etapa de construção
- Registro de % de conclusão com evidência fotográfica por etapa
- App de campo para a equipe de obra (decisão de nativo vs. PWA pendente, mesmo padrão de outras pendências do portfólio)

### 2.6 Entrega e pós-venda
- Vistoria de entrega com checklist formal ("habite-se" / termo de entrega de chaves)
- Assistência técnica pós-entrega — especialização do mesmo módulo de Ordem de Serviço já formalizado no AuraFix/AuraVet, aqui cobrindo garantia de construção (estrutural, hidráulica, elétrica) conforme prazo legal por item

### 2.7 Portal do cliente
- Acompanhamento de % de obra, próximo pagamento, documento do contrato, abertura de chamado pós-entrega

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Funil de vendas com lead, corretor e follow-up | Organiza o processo comercial sem depender de planilha paralela |
| RF02 | Catálogo de unidade na planta com planta baixa, preço e simulação de financiamento | Dá ao cliente informação suficiente para decidir sem depender só do corretor |
| RF03 | Reserva de unidade com sinal e prazo de validade | Evita venda duplicada da mesma unidade enquanto a reserva está ativa |
| RF04 | Geração de contrato com quadro-resumo obrigatório por lei | Cumpre exigência legal de transparência, reduzindo risco de disputa por falta de clareza |
| RF05 | Assinatura eletrônica juridicamente válida do contrato | Sem isso, o processo de venda não fecha digitalmente de forma segura |
| RF06 | Cálculo de distrato conforme Lei 13.786/2018 (retenção até 25%/50%, devolução em até 180 dias) | Protege tanto o cliente quanto a construtora de cálculo incorreto ou disputa evitável |
| RF07 | Direito de arrependimento de 7 dias para venda fora do estande, com devolução integral | Cumpre exigência legal específica, com risco reputacional e jurídico real se ignorada |
| RF08 | Alerta de aproximação do prazo de tolerância de atraso de entrega (180 dias) | Dá visibilidade antecipada à construtora antes de configurar descumprimento contratual |
| RF09 | Fluxo de pagamento parcelado com emissão de boleto/carnê por parcela | Automatiza cobrança de contrato de longo prazo, reduzindo erro manual em valores altos |
| RF10 | Configurador de customização de casa personalizada com orçamento dinâmico | Formaliza o processo de escolha do cliente, hoje tipicamente feito em planilha ou e-mail solto |
| RF11 | Cronograma físico-financeiro de obra com % de conclusão e evidência fotográfica | Dá transparência ao cliente e histórico defensável em caso de disputa sobre atraso |
| RF12 | Vistoria de entrega com checklist formal | Formaliza a entrega, reduzindo disputa pós-entrega sobre o que foi ou não verificado |
| RF13 | Assistência técnica pós-entrega vinculada ao prazo legal de garantia por item construtivo | Organiza a obrigação de garantia de construção sem depender de controle manual |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Cliente comprador
- **Cadastro:** self-service ao reservar unidade, ou assistido pelo corretor
- **Uso:** portal do cliente (2.7), assinatura de contrato, acompanhamento de pagamento e obra
- **Suporte:** canal com a construtora/imobiliária — em caso de distrato, precisa de canal formal e bem documentado, dado o risco de disputa

### 4.2 Corretor/vendedor
- **Cadastro:** criado pela imobiliária/construtora
- **Uso:** CRM (2.1), geração de proposta e contrato
- **Suporte:** canal interno da própria construtora

### 4.3 Equipe de obra
- **Cadastro:** criado pela construtora
- **Uso:** app de campo (2.5), registro de progresso
- **Suporte:** canal interno

### 4.4 Financeira/banco (integração, não usuário direto)
- Recebe dado de simulação de financiamento; não tem conta no sistema — é integração, não perfil de usuário

### 4.5 Suporte técnico interno
- Mesma lacuna recorrente do portfólio — aqui com peso adicional, porque disputa de distrato exige histórico completo e acessível rapidamente, dado o valor financeiro envolvido

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no AuraObra | Para que serve |
|---|---|---|
| RNFT-E01 (concorrência) | Reserva de unidade não pode aceitar duas reservas simultâneas da mesma unidade | Evita venda duplicada, problema com consequência jurídica real neste sistema |
| RNFT-E02 (idempotência de pagamento) | Cobrança de parcela recorrente | Evita cobrança duplicada em valor alto — erro aqui é caro de verdade |
| RNFT06 (LGPD) | Dado financeiro e documento pessoal do comprador (para contrato e financiamento) | Cumpre obrigação legal sobre dado sensível de alto valor |
| Precisão de cálculo financeiro (próprio) | Cálculo de distrato, parcela e retenção deve ter cobertura de teste próxima de 100%, mesmo padrão de rigor do motor determinístico do AuraWealth | Erro de cálculo aqui tem consequência financeira e jurídica direta, em valores tipicamente muito acima de qualquer outro sistema do portfólio |
| Auditabilidade contratual (próprio) | Toda alteração de contrato, aprovação e cálculo de distrato deve ser registrada de forma imutável | É evidência formal em caso de disputa judicial — o sistema pode ser chamado como prova |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no AuraObra |
|---|---|
| Dados | Documento pessoal e dado financeiro de alto valor — nível de sensibilidade próximo ao do AuraWealth. **RESOLVIDO/atualizado:** implementado via `aura-vault`, o serviço compartilhado de proteção de dado extra-sensível |
| Assinatura eletrônica | Precisa de provedor com validade jurídica reconhecida (ICP-Brasil ou equivalente comercial reconhecido pelos tribunais), não uma implementação própria informal |
| Auditoria externa (RNFT-S06) | Prioridade máxima, no mesmo nível do AuraWealth — é o segundo sistema do portfólio (depois do AuraWealth) onde uma falha tem consequência financeira direta e alta, mais o agravante de exposição jurídica contratual |

---

## 7. Hardware, instalador e distribuição

**Majoritariamente não aplicável** — SaaS puro. Exceção parcial: o app de campo da equipe de obra (2.5) roda em dispositivo móvel comum, sem hardware dedicado, mas com dependência de conectividade em canteiro de obra (possível área com sinal fraco) — vale considerar modo offline básico para registro de evidência fotográfica, sincronizando quando a conexão voltar, mesmo princípio já aplicado ao AuraPOS.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Dado o nível de exposição jurídica do sistema, vale considerar ambiente de produção com backup mais frequente que o padrão — perda de histórico de contrato/pagamento aqui tem consequência maior que na maioria dos outros sistemas.

---

## 9. Modelo de receita — todas as formas de venda

| Fonte | Modelo |
|---|---|
| Assinatura SaaS por empreendimento ativo | Mensalidade proporcional ao número de unidades em comercialização |
| Assinatura por unidade vendida | Alternativa de precificação por transação, para construtora de menor volume |
| Taxa de setup/onboarding | Cobrança única na implantação |
| Módulo de configurador de casa personalizada | Add-on vendido separadamente, para construtora que só atua com incorporação padrão pode não precisar dele |
| Comissão sobre financiamento intermediado | Se o sistema evoluir para intermediação real com parceiro financeiro, não só simulação informativa |
| **Canal B2B — pequena construtora local vs. incorporadora de maior porte** | Dois perfis de cliente com ticket muito diferente; vale desenhar dois pacotes comerciais desde já, não um único preço para os dois portes |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização completa deste sistema.

---

## 11. Pendências e decisões em aberto

1. **Validação jurídica formal do módulo de distrato** — mesmo com a pesquisa regulatória já incorporada a este documento, recomendo revisão por advogado especializado em direito imobiliário antes de tratar o RF06/RF07 como pronto para produção — é o requisito de maior risco legal de todo o portfólio se implementado incorretamente.
2. **Provedor de assinatura eletrônica** — DocuSign, Clicksign ou D4Sign, decisão ainda não tomada.
3. **Modo offline do app de campo** (seção 7) — ainda não especificado com detalhe.
4. **Precificação diferenciada por porte de construtora** (seção 9) — ainda não desenhada.
5. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado, mantendo o cuidado de acesso justificado e logado dado o valor financeiro em disputas contratuais.
6. **Integração de financiamento bancário** — hoje só simulação informativa (2.3); decisão de evoluir para intermediação real ainda não tomada.
