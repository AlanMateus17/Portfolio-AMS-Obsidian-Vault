---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Kaixara — Documento de Projeto Final

> **Nota de correção:** a primeira versão deste documento estava incompleta. Ao cruzar com o histórico completo de planejamento, faltavam o bloco de hardware/emissão fiscal (seção 2.7), o modo offline (seção 2.8) e o roadmap de deploy (seção 8) — todos já decididos anteriormente, só não tinham entrado na consolidação. Corrigido abaixo.

Este é o documento único de referência do AM Kaixara: tudo que o sistema vai ter ao final do desenvolvimento, consolidado a partir de tudo que já foi decidido ao longo do planejamento (stack, arquitetura, RF/RNF, pacotes comerciais) mais o que mudou agora com a auditoria de escala e segurança financeira. Serve para você avaliar de uma vez só se é exatamente isso que você quer, em vez de garimpar em documentos espalhados.

---

## 1. Visão do produto

Sistema de PDV (ponto de venda) e gestão de estoque multi-tenant, para pequeno/médio varejo, com arquitetura pensada desde o início para venda modular (pacotes comerciais diferentes por porte de cliente) e para servir de motor de estoque/venda reaproveitado por outros sistemas do portfólio (Loja Virtual, AM Consertta).

---

## 2. Funcionalidades completas (estado final)

### 2.1 Autenticação e usuários
- Login com JWT + BCrypt
- Controle de acesso por papel (operador de caixa, gerente, admin)
- Isolamento completo por `tenant_id` (Row-Level Security no banco)

### 2.2 Produtos e categorias
- CRUD completo de produto e categoria
- Campos de controle: `TenantId`, `FilialId`, `Category`, `ReservedQuantity`, `ReservedUntil`, timestamps de criação/atualização/exclusão lógica
- Suporte a múltiplas filiais por tenant

### 2.3 PDV (Ponto de Venda)
- Carrinho de venda em tempo real
- Múltiplos meios de pagamento
- Abertura e fechamento de caixa, com conferência física vs. esperado
- Emissão de recibo de venda, com suporte a impressão
- Cancelamento de venda com restauração de estoque

### 2.4 Estoque
- Controle de quantidade por produto/filial
- Reserva de estoque (`ReservedQuantity`/`ReservedUntil`) — mecanismo que também é reaproveitado pelo AM Consertta na reserva de peça por Ordem de Serviço
- Histórico de movimentação

### 2.5 Dashboard e relatórios
- Indicadores de venda, produto mais vendido, faturamento por período
- Visão consolidada multi-filial

### 2.6 Comercialização modular
- Suporte a pacotes vendáveis parciais (ex: AM Kaixara Starter, combinações com Delivery/AM Rendara) via `aura-licensing`
- Interfaces trocáveis já definidas na arquitetura: `IFonteDeEstoque`, `IEmissorFiscal`, `IFonteDeMovimentacaoBancaria` — permitem trocar implementação (ex: emissor fiscal diferente por cliente) sem alterar o núcleo do sistema

### 2.7 Hardware de PDV e emissão fiscal — **bloco que faltava na primeira versão deste documento**
Isso é o que uma nota sua de planejamento anterior descreve textualmente como "o que torna o AM Kaixara realmente vendável" — sem isso, o sistema é só um cadastro de produto e venda, não um PDV de verdade para varejo físico.
- **Agente local** (.NET, Windows Service ou app em background) expondo API HTTP em `localhost`, responsável por toda comunicação com hardware conectado ao caixa
- **`IImpressoraFiscal`** — implementação ESC/POS para cupom não-fiscal
- **`IGavetaDinheiro`** — abertura de gaveta via comando pela impressora
- **`IBalanca`** — integração via porta serial, para venda por peso
- **Emissão de NFC-e** — com modo de contingência offline; decisão pendente entre gateway fiscal terceirizado vs. implementação própria de comunicação com a SEFAZ (decisão de negócio/custo, precisa ser tomada antes de codar este módulo)
- **`ITefService`** — integração com adquirente de cartão (TEF), implementação a escolher

### 2.8 Modo offline — **também faltava na primeira versão**
- SQLite local (via `Microsoft.Data.Sqlite`) rodando no agente local, como fila de vendas pendentes
- Padrão outbox: venda feita offline entra na fila local e sincroniza automaticamente quando a conexão voltar
- Requisito de resiliência formal: o sistema precisa aguentar **pelo menos 4 horas offline sem perda de dado** (RNF04) — isso cobre o cenário real de queda de internet no meio do expediente de venda

### 2.9 Integrações de infraestrutura compartilhada
- `aura-licensing` — verificação de módulo ativo por `tenant_id`, com cache local de 24-48h para não bloquear cliente por indisponibilidade momentânea do serviço
- `aura-historico` (opcional, Clojure/Datomic) — registro imutável de eventos, quando ativado
- `aura-analytics` (opcional, Python) — previsão de demanda via Prophet/statsmodels, consumida pelo dashboard

---

## 3. Requisitos Funcionais (RF)

| ID   | Requisito                                                                                                                                   | Para que serve                                                                                                                       |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| RF01 | Login com JWT + BCrypt, isolado por `tenant_id`                                                                                             | Garante que cada lojista só acessa seus próprios dados, e que senha nunca fica em texto plano                                        |
| RF02 | Controle de acesso por papel (operador, gerente, admin)                                                                                     | Operador de caixa não deve conseguir alterar preço ou ver relatório consolidado — limita dano de erro humano ou uso indevido         |
| RF03 | CRUD de produto e categoria, com campos de controle (`TenantId`, `FilialId`, `ReservedQuantity`, `ReservedUntil`)                           | Base de dado para venda, estoque e reserva funcionarem de forma consistente entre filiais                                            |
| RF04 | Carrinho de venda com múltiplos meios de pagamento                                                                                          | Cobre o cenário real de PDV, onde o cliente pode pagar parte em dinheiro e parte em cartão                                           |
| RF05 | Abertura/fechamento de caixa com conferência física vs. esperado                                                                            | Detecta divergência de caixa (falta ou sobra) no mesmo dia, não semanas depois numa auditoria                                        |
| RF06 | Cancelamento de venda com restauração automática de estoque                                                                                 | Evita que um cancelamento gere estoque fantasma (vendido no sistema, mas fisicamente ainda na loja)                                  |
| RF07 | Emissão de NFC-e com contingência offline                                                                                                   | Obrigação fiscal — sem isso, o lojista não pode operar legalmente; contingência evita parar de vender quando a SEFAZ está fora do ar |
| RF08 | Integração `ITefService` com adquirente de cartão                                                                                           | Permite pagamento com cartão direto no fluxo de venda, sem processo manual paralelo                                                  |
| RF09 | Agente local com `IImpressoraFiscal`, `IGavetaDinheiro`, `IBalanca`                                                                         | Sem isso o sistema não controla o hardware físico do caixa — é o que torna o AM Kaixara um PDV de verdade, não só um cadastro           |
| RF10 | Modo offline com fila local (SQLite) e sincronização automática                                                                             | Loja não pode parar de vender por causa de instabilidade de internet — resiliência mínima de 4h (RNF04)                              |
| RF11 | Reserva de estoque (`ReservedQuantity`/`ReservedUntil`)                                                                                     | Permite que outro sistema (AM Consertta) reserve peça sem vender de fato — pré-requisito para o reaproveitamento entre sistemas           |
| RF12 | Dashboard com indicador de venda, produto mais vendido, faturamento por período                                                             | Dá ao lojista visibilidade de negócio sem precisar exportar dado pra planilha                                                        |
| RF13 | Ativação de módulo comercial via `aura-licensing`                                                                                           | Viabiliza vender pacote parcial (Starter, Standard) sem manter versões de código separadas por pacote                                |
| RF14 | Histórico de movimentação de estoque (entrada, saída, ajuste) por produto/filial                                                            | Permite auditoria de "por que o estoque está diferente do esperado", essencial pra investigar divergência                            |
| RF15 | Emissão de recibo de venda não-fiscal, com suporte a impressão via `IImpressoraFiscal`                                                      | Comprovante imediato pro cliente, independente do ciclo de emissão fiscal (NFC-e)                                                    |
| RF16 | Integração opcional com `aura-historico` (registro imutável de evento) e `aura-analytics` (previsão de demanda) quando ativados pelo tenant | Sem RF explícito, a ativação condicional desses serviços fica sem contrato formal de comportamento esperado                          |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Operador de caixa
- **Cadastro:** criado pelo gerente/admin do tenant, sem autocadastro
- **Uso:** tela de PDV (2.3), sem acesso a relatório consolidado ou configuração
- **Suporte:** canal interno do próprio lojista (não chega ao seu suporte diretamente) — se o operador tem dúvida, é o gerente quem resolve, não o Grupo AMtech

### 4.2 Gerente/Admin do tenant (dono do negócio ou responsável)
- **Cadastro:** criado na configuração inicial pós-compra (painel de configuração pós-compra, ver seção 7)
- **Uso:** dashboard (2.5), gestão de produto/estoque/filial, contratação de módulo adicional via `aura-licensing`
- **Suporte:** canal com o Grupo AMtech Digital — precisa existir um caminho formal (WhatsApp Business, ticket, e-mail) para dúvida técnica ou problema de cobrança; hoje isso não está formalizado em nenhum RF

### 4.3 Suporte técnico interno (você/futuro time do Grupo AMtech)
- **Cadastro:** não se aplica — é você mesmo, com acesso administrativo elevado
- **Uso:** precisa de um painel/acesso que permita ver o estado de qualquer tenant (sem ver dado sensível de venda além do necessário para diagnosticar problema), reprocessar uma sincronização travada, verificar status de licença
- **Lacuna real:** este painel de suporte interno **não existe em nenhum documento do AM Kaixara até agora** — mesmo ponto cego identificado no AM Rotara, mas ainda não corrigido aqui. Sem ele, um problema relatado por um lojista só pode ser investigado direto no banco de dados, o que não escala além de poucos clientes.

---

## 5. Requisitos Não Funcionais — próprios + transversais

Além dos RNF específicos já definidos no documento `requisitos-funcionais-e-nao-funcionais.md` do ecossistema, o AM Kaixara agora referencia formalmente os seguintes itens do documento **RNF Transversais — Escala e Segurança Financeira**:

| ID transversal | Aplicação no AM Kaixara | Para que serve |
|---|---|---|
| RNFT-E01 | Controle de concorrência na baixa de estoque durante a venda — **ver seção 10, é o item com maior impacto no código já escrito** | Impede que dois canais vendam a última unidade do mesmo produto ao mesmo tempo |
| RNFT-E02 | Idempotência em qualquer integração futura de pagamento via gateway online (hoje o PDV é presencial/manual; passa a valer no momento em que o AM Kaixara aceitar pagamento processado por webhook) | Evita cobrança duplicada se o gateway reenviar a mesma confirmação de pagamento |
| RNFT-E03 | Fila para desacoplar confirmação de venda de emissão fiscal/notificação | Impede que uma falha na emissão fiscal trave a confirmação da venda ao cliente |
| RNFT-E04 | Índice composto por `tenant_id` nas tabelas de maior volume (produto, venda) | Evita que a consulta de um tenant fique lenta por causa do volume de dado de outro tenant |
| RNFT-E05 | Log estruturado de operação financeira + alerta de divergência | Permite descobrir um problema financeiro antes do lojista reclamar, não depois |
| RNFT-E06 | Reporta dados de venda para a reconciliação financeira central do `aura-licensing` (não é o dono do requisito, mas precisa expor os dados) | Permite detectar se algum evento de venda se perdeu silenciosamente numa falha de rede |

---

## 6. Segurança de nível profissional

Aplicação concreta do checklist geral ([distribuicao-licenciamento-seguranca](../04-documentos-transversais/distribuicao-licenciamento-seguranca.md)) a este sistema:

| Categoria | Aplicação específica no AM Kaixara |
|---|---|
| Instalador/agente local (RNFT-S01) | O agente local que fala com hardware (impressora, gaveta, balança, TEF) é a maior superfície de ataque física do sistema — precisa rodar com menor privilégio possível, nunca exigir admin além do estritamente necessário |
| Licenciamento (RNFT-S02) | Ativação online com tolerância offline de pelo menos 7 dias — nunca travar o caixa por falha de verificação de licença no meio do expediente |
| Rede/API | Rate limiting em login e em qualquer endpoint que decremente estoque, para mitigar tanto força bruta quanto abuso de concorrência |
| Dados | Dado de cliente/venda protegido por `tenant_id` + RLS; dado de cartão nunca trafega nem é armazenado diretamente — sempre via `ITefService` do adquirente |
| Código/SDLC (RNFT-S05) | Scan de dependência automatizado — já validado como necessário na prática: 2 CVEs reais foram encontrados e corrigidos no início do desenvolvimento (Microsoft.OpenApi, System.Security.Cryptography.Xml) |
| Auditoria externa (RNFT-S06) | É o sistema com maior prioridade de pentest externo antes de venda pública, por ser o primeiro a ser distribuído como instalador executável (ver seção 7) |

---

## 7. Hardware, instalador e distribuição

O AM Kaixara é o sistema piloto da distribuição híbrida do portfólio (SaaS + instalador executável), detalhada no documento [distribuicao-licenciamento-seguranca](../04-documentos-transversais/distribuicao-licenciamento-seguranca.md). Resumo aplicado aqui:
- Empacotamento como instalador Windows (MSIX ou WiX — decisão pendente, ver seção 11), contendo o agente local (2.7) já assinado digitalmente (Code Signing/Authenticode)
- Ativação de licença online na instalação, vinculada ao `tenant_id`, com tolerância offline
- Painel de configuração pós-compra (web) provisionando o tenant antes mesmo do instalador rodar localmente pela primeira vez
- Conexão com outros sistemas do portfólio comprados pelo mesmo cliente (ex: AM Rendara) via consentimento explícito e credencial de escopo limitado

---

## 8. Deploy e CI/CD (estado final)
- Dockerfile da API em multi-stage build
- Dockerfile do frontend
- `docker-compose.yml` de produção (separado dos de desenvolvimento já existentes)
- Pipeline GitHub Actions: build → teste → deploy automático
- Deploy em serviço gerenciado (AWS ou Azure — decisão final ainda em aberto entre as duas)
- README do repositório usando o template já definido no guia de organização do GitHub do portfólio

## 9. Modelo de receita

- Assinatura SaaS mensal por `tenant_id`, com valor variando por pacote comercial contratado
- Possível taxa de setup/onboarding
- Módulos adicionais vendidos separadamente via `aura-licensing` (ex: dashboard avançado, integração com `aura-analytics`)

---

## 10. Status atual de desenvolvimento — o que mudou e o que isso afeta no que já foi desenvolvido

Isso é o que você pediu para deixar mais claro. O AM Kaixara é o único sistema do portfólio com código já em produção-alvo (Sprint 3-4), então é o único onde "o que mudou" tem custo real de retrofit, não só de planejamento.

### 10.1 O que mudou
A auditoria de escala e segurança financeira identificou que o controle de concorrência em operação de estoque (RNFT-E01) não estava formalizado como requisito em nenhum documento até agora — inclusive no que já foi desenvolvido.

### 10.2 O que isso afeta especificamente no código já escrito
- **Entidade `Product`**: já tem `ReservedQuantity` e `ReservedUntil`, o que ajuda, mas precisa ganhar uma coluna de controle de concorrência (`RowVersion`/token de concorrência do EF Core, ou uso do `xmin` nativo do PostgreSQL) — isso é uma migration nova, não uma reescrita.
- **`ProductRepository`**: os métodos de atualização de quantidade (usados no fluxo de venda) precisam passar a usar atualização condicional (`UPDATE ... WHERE Id = @id AND RowVersion = @versaoLida`) em vez de ler-e-depois-escrever sem verificação — é o ponto exato onde duas vendas simultâneas do último item poderiam hoje, sem essa mudança, ambas serem confirmadas.
- **Fluxo de venda no `SalesController`**: precisa tratar o caso de conflito de concorrência (zero linhas afetadas na atualização) como "estoque insuficiente, tente novamente" em vez de assumir sucesso.
- **O que NÃO muda**: autenticação/JWT em andamento não é afetada por este ponto — pode continuar a implementação atual do Sprint 3-4 normalmente. A auditoria só afeta a camada de estoque/venda, não a de autenticação.

### 10.3 O que fica como recomendação futura, sem ação imediata no código atual
- RNFT-E02 (idempotência de pagamento) só passa a exigir mudança de código quando o AM Kaixara integrar um gateway de pagamento online — o PDV presencial atual não está exposto a esse risco do mesmo jeito.
- RNFT-E03, E05, E06 são aditivos (fila, log, reconciliação) — não exigem alterar lógica já escrita, só adicionar camada por cima, quando o volume justificar.
- RNFT-E04 (índice por `tenant_id`) vale uma verificação rápida no schema atual, mas não é uma mudança estrutural se os índices já foram pensados com `tenant_id` desde o início (como o padrão do ecossistema sugere que foram).

### 10.4 Ordem recomendada
1. Adicionar a coluna de concorrência ao `Product` (migration simples)
2. Ajustar `ProductRepository` para atualização condicional
3. Ajustar `SalesController` para tratar conflito de concorrência
4. Continuar o Sprint 3-4 (JWT) normalmente — não depende do acima
5. Verificar índices por `tenant_id` como item de checklist, não bloqueante

---

## 🔗 Documentos relacionados
- [kaixara-especificacao-tecnica-completa](kaixara-especificacao-tecnica-completa.md) — schema, contrato de API, fluxos de sequência e threat model
- [kaixara-frontend-documento-unico](kaixara-frontend-documento-unico.md) — plano de frontend completo, do Discovery à Engenharia
- [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md) — detalhamento da stack usada neste sistema
- [passo-a-passo-mestre-desde-o-inicio](../99-arquivo/passo-a-passo-mestre-desde-o-inicio.md) — a sequência de construção que usa o AM Kaixara como base

---

## 11. Pendências e decisões em aberto

1. **AWS vs. Azure** — decisão de infraestrutura ainda não fechada, única para todo o portfólio.
2. **MSIX vs. WiX Toolset** para o instalador — ambos válidos, falta decidir.
3. **Gateway fiscal terceirizado vs. implementação própria de comunicação com a SEFAZ** — decisão de negócio/custo que trava o início do módulo de NFC-e (seção 2.7).
4. **Adquirente de cartão (TEF)** — implementação de `ITefService` depende de qual adquirente for escolhido.
5. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado como serviço compartilhado (ver [aura-support-documento-projeto-final](../03-servicos-compartilhados/aura-support-documento-projeto-final.md)), com painel de reprocessamento e correção manual para qualquer tenant do AM Kaixara.
6. **Canal formal de suporte ao lojista** (seção 4.2) — WhatsApp Business, ticket ou e-mail; hoje não está formalizado em nenhum RF.
7. **Certificado de assinatura de código** — precisa ser adquirido de uma autoridade reconhecida antes do primeiro instalador público.
