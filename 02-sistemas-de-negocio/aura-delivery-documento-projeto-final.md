---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# Aura Delivery — Documento de Projeto Final

> **Nota de reconciliação:** este documento trata o Aura Delivery como o sistema de logística completo (pedido, roteirização, entregador, rastreamento), distinto da "Loja Virtual" (módulo de catálogo/checkout simples, dependente do AuraPOS) — ver seção 11. Segue a estrutura fixa definida no [[template-documento-projeto-final]].

---

## 1. Visão do produto

Plataforma de logística de entrega multi-tenant, conectada nativamente ao AuraPOS como fonte única de verdade de produto/estoque/pedido.

**Diferencial de inovação:**
- **Roteirização real via otimização matemática (OR-Tools), não "entregador mais próximo"** — resolve como problema de roteirização de veículos (VRP), permitindo lote de múltiplas entregas numa rota otimizada
- **Estoque nunca diverge** — pedido no Delivery debita o mesmo estoque do balcão físico em tempo real, por ser o mesmo dado do AuraPOS, não uma cópia sincronizada por webhook de terceiro
- **Comissão pensada para o pequeno lojista** — sem o peso de operação nacional financiada a bilhões (iFood/Rappi historicamente cobram entre 12-27% dependendo do plano), pode se posicionar com comissão menor como diferencial direto
- **Fidelidade cruzada no ecossistema** — pontos ganhos numa compra futuramente resgatáveis em outro produto Aura (AuraVet, AuraFix), diferencial que nenhuma plataforma isolada do mercado consegue oferecer

---

## 2. Funcionalidades completas (estado final)

### 2.1 Bloco 1 — MVP (pedido + geolocalização)
- Cadastro de conta PF/PJ com autenticação JWT (mesma base do resto do ecossistema)
- Catálogo de pedido conectado ao AuraPOS (mesma fonte de produto/estoque/preço)
- Geolocalização do endereço de entrega e da loja de origem (PostGIS)
- Checkout com pagamento online

### 2.2 Bloco 2 — Tempo real e notificação
- Rastreamento de entregador em tempo real (SignalR)
- Notificação automática de status do pedido (preparando → a caminho → entregue)
- Painel de gestão de pedido para o lojista

### 2.3 Bloco 3 — Roteirização e expansão
- Roteirização otimizada de múltiplas entregas por rota (`aura-analytics`, Google OR-Tools)
- Cadastro e gestão de entregador (cadastro, disponibilidade, avaliação)
- Split automático de pagamento entre lojista, entregador e plataforma
- Expansão multi-região

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Cadastro de conta PF/PJ com autenticação JWT | Base de identidade compartilhada com o resto do ecossistema, sem duplicar cadastro |
| RF02 | Catálogo de pedido conectado ao AuraPOS (mesma fonte de produto/estoque/preço) | Evita divergência de preço/estoque entre canal de venda e operação de entrega |
| RF03 | Geolocalização de endereço de entrega e loja de origem | Pré-requisito para cálculo de distância, roteirização e estimativa de tempo |
| RF04 | Checkout com pagamento online | Permite fechar o pedido sem depender de pagamento na entrega |
| RF05 | Rastreamento de entregador em tempo real | Reduz ansiedade do cliente e ligação de suporte perguntando "cadê meu pedido" |
| RF06 | Notificação automática de status do pedido | Mantém lojista e cliente informados sem exigir consulta manual ao sistema |
| RF07 | Roteirização otimizada de múltiplas entregas por rota (VRP via OR-Tools) | Permite lote de entregas numa rota eficiente, em vez de uma de cada vez — é o diferencial competitivo central deste sistema |
| RF08 | Cadastro e gestão de entregador, com onboarding e verificação de documento | Impede que qualquer pessoa vire entregador sem nenhum controle — risco de segurança e legal |
| RF09 | Split automático de pagamento entre lojista, entregador e plataforma | Elimina acerto manual de comissão, que é fonte comum de erro e disputa |
| RF10 | Painel de suporte interno com reatribuição manual de pedido e fila de disputa | Permite resolver o que sai do fluxo automático — entregador que não aparece, item errado, pagamento contestado |
| RF11 | Painel de gestão de pedido para o lojista (aceitar/recusar, tempo estimado de preparo, status) | Dá ao lojista controle direto sobre o pedido recebido, sem depender de você como intermediário |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

O Delivery tem quatro perfis de usuário reais, e cada um precisa de caminho completo — cadastro, uso do dia a dia, e suporte quando algo dá errado. Um sistema de entrega que só pensa no "pedido feito com sucesso" e não nesses quatro caminhos completos é exatamente o que trava usuário na prática.

### 4.1 Lojista (parcialmente coberto pelo AuraPOS)
- **Cadastro:** já resolvido via conta AuraPOS existente — não precisa de cadastro duplicado
- **Uso:** painel de gestão de pedido Delivery (aceitar/recusar pedido, tempo estimado de preparo, status), configuração de área de entrega e taxa
- **Suporte:** canal para contestar cobrança de comissão, reportar problema com entregador específico

### 4.2 Entregador — **perfil sem sistema de onboarding definido até agora**
- **Cadastro:** precisa de fluxo próprio de onboarding — cadastro de documento (CNH/CPF), dado de veículo, verificação básica antes da aprovação (sem isso, qualquer pessoa entra na plataforma sem nenhum controle, o que é tanto risco de segurança quanto risco legal/reputacional)
- **Uso:** app com toggle de disponibilidade (online/offline), recebimento de pedido com opção de aceitar/recusar, navegação até o ponto de coleta e de entrega, confirmação de entrega (foto ou assinatura), visão de ganho do dia/período
- **Suporte:** canal de contestação (pedido cancelado no meio do caminho, cliente ausente na entrega), consulta de repasse financeiro

### 4.3 Cliente final
- **Cadastro:** conta própria ou checkout como convidado (decisão a tomar — convidado reduz fricção de primeira compra, conta facilita recompra e rastreamento de histórico)
- **Uso:** fazer pedido, pagar, acompanhar em tempo real, avaliar depois da entrega
- **Suporte:** canal de contestação de pedido (item errado, atraso, não entregue), reembolso

### 4.4 Suporte/Operação interna — **perfil completamente ausente do planejamento até agora**
Este é o mais importante dos quatro para "ninguém ficar barrado", porque é o que resolve quando algo sai do fluxo feliz — e em qualquer plataforma de entrega, algo sai do fluxo feliz o tempo todo (entregador não aparece, pedido chega errado, pagamento falha no meio do processo).
- Painel interno (você, ou futuro funcionário de suporte) com visão de todos os pedidos em andamento, cruzando os três outros perfis
- Capacidade de reatribuir pedido a outro entregador manualmente, quando o original não completa
- Capacidade de forçar reembolso/estorno fora do fluxo automático
- Fila de disputas abertas (lojista vs. entregador, cliente vs. lojista) com histórico de decisão

---

## 5. Requisitos Não Funcionais — próprios + transversais

| ID | Aplicação no Delivery | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado de cliente e de entregador, incluindo geolocalização — categoria sensível | Cumprir obrigação legal e evitar exposição indevida de localização de pessoa física |
| RNFT07 (BOLA) | Toda rota que recebe ID de pedido deve validar que o usuário autenticado tem permissão sobre aquele pedido específico | Impede que um cliente veja/altere o pedido de outro só trocando o ID na URL |
| RNFT09 (idempotência de escrita) | Criação de pedido e confirmação de pagamento devem aceitar chave de idempotência | Evita pedido duplicado se o app reenviar a requisição por instabilidade de rede |
| RNFT-E01 (concorrência de estoque) | Pedido no Delivery decrementa o mesmo estoque do AuraPOS — mesmo risco de concorrência multicanal já mapeado | Impede vender o mesmo item por dois canais ao mesmo tempo |
| RNFT-E02 (idempotência de pagamento) | Processa pagamento online | Evita cobrança duplicada em caso de webhook reenviado |
| RNFT-E03 (fila para picos) | Especialmente relevante em horário de pico de almoço/jantar | Evita que o checkout trave inteiro por lentidão em etapa não crítica (emissão fiscal, notificação) |
| RNFT-E04 (índice por tenant) | Consultas de pedido/rota devem indexar por `tenant_id` | Evita que consulta de um lojista fique lenta pelo volume de outro |
| RNFT-E05 (observabilidade) | Log estruturado de falha de roteirização/pagamento, com alerta | Permite descobrir problema antes do cliente reclamar |
| RNFT-E06 (reconciliação) | Reporta dados de venda para reconciliação central do `aura-licensing` | Detecta se algum pedido/pagamento se perdeu silenciosamente |

**Requisito específico de segurança de geolocalização:** a posição exata do entregador é dado sensível de localização — nunca expor coordenadas exatas além do necessário, e apenas durante a entrega ativa (sem manter histórico de rota visível ao cliente após a entrega concluída).

---

## 6. Segurança de nível profissional

Aplicação concreta do checklist geral ([[distribuicao-licenciamento-seguranca]]) a este sistema:

| Categoria | Aplicação específica no Delivery |
|---|---|
| Código/SDLC (RNFT-S05) | Scan de dependência automatizado no pipeline, mesmo padrão do AuraPOS |
| Rede/API | Autenticação JWT + rate limiting em endpoints de criação de pedido e atualização de localização (superfície de abuso real: spam de pedido falso, spoofing de localização de entregador) |
| Dados | Geolocalização tratada como dado sensível (já detalhado na seção 5); retenção limitada — não guardar histórico de rota além do necessário para disputa/suporte |
| Conexão entre sistemas (RNFT-S03/S04) | Ligação Delivery ↔ AuraPOS de um mesmo cliente segue consentimento explícito e escopo mínimo, mesmo padrão do resto do portfólio |
| Auditoria externa (RNFT-S06) | Antes de lançamento público, pentest de escopo definido deve cobrir especificamente o endpoint de atualização de localização e o fluxo de pagamento/split — são os dois pontos de maior superfície de abuso deste sistema em particular |

---

## 7. Hardware, instalador e distribuição

**Não aplicável no sentido do AuraPOS/AuraFix.** O Delivery é SaaS puro (backend + apps móveis), sem componente físico de hardware e sem necessidade do modelo de instalador executável. A única distribuição física indireta é o app do entregador/cliente rodando em dispositivo móvel comum (sem hardware dedicado como impressora fiscal ou balança).

Distribuição comercial segue o padrão de pacotes + `aura-licensing`: cliente escolhe entre Delivery isolado, combinado com AuraPOS, ou parte de um combo maior (ver seção 9).

---

## 8. Deploy e CI/CD

- Backend: mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml` de produção, pipeline GitHub Actions (build → teste → deploy)
- Apps móveis (entregador/cliente): pipeline de build/distribuição próprio, a definir junto com a decisão de plataforma (PWA vs. nativo) — PWA reaproveita o mesmo pipeline web; nativo exigiria pipeline de loja de aplicativo (Google Play/App Store) separado
- Deploy em serviço gerenciado (AWS ou Azure), mesma decisão pendente registrada no AuraPOS

---

## 9. Modelo de receita

| Fonte | Modelo |
|---|---|
| Comissão por pedido online | Percentual sobre cada venda feita pelo canal Delivery |
| Taxa de entrega | Repassada ou compartilhada entre lojista e entregador, via split automático (2.3) |
| Pacote "Integrado" com o AuraPOS | Delivery como módulo adicional dentro de um pacote comercial maior |
| Delivery standalone | Vendável sozinho para quem só precisa da logística — depende da decisão pendente na seção 11 |

---

## 10. Status atual de desenvolvimento

**Nenhum código foi escrito ainda para o Aura Delivery.** Diferente do AuraPOS (Sprint 3-4 em andamento), este sistema está inteiramente em estágio de planejamento — RF/RNF, checklist de execução do MVP e README já existem como documentos, mas nenhuma linha de código do backend ou dos apps foi iniciada. Isso é uma vantagem real neste momento: toda a auditoria de escala/segurança/distribuição pode ser incorporada ao design desde o primeiro commit, sem custo de retrofit como aconteceu no AuraPOS.

---

## 11. Pendências e decisões em aberto

1. **Resolver a ambiguidade Delivery vs. Loja Virtual** — confirmar que são produtos diferentes, conforme a nota no topo deste documento.
2. **App nativo vs. PWA** para entregador e cliente final — mesma decisão pendente do AuraVet; vale decidir uma vez para os dois casos, não separadamente.
3. **Delivery vendável isolado ou só como módulo do AuraPOS** — muda o RF/RNF de "standalone" citado na seção 9.
4. **AWS vs. Azure** — mesma pendência do AuraPOS, decisão única para todo o portfólio, não por sistema.
5. **Critério de verificação do entregador no onboarding** (seção 4.2) — decisão de negócio (que nível de checagem de documento é exigido antes de aprovar um entregador) precisa ser tomada antes de formalizar o RF desse fluxo.
6. **Painel de suporte interno** — RESOLVIDO: o RF10 acima já cobre a necessidade local, mas a visão cruzada entre sistemas (ex: um pedido com problema de estoque compartilhado com o AuraPOS) agora é responsabilidade do `aura-support`, já formalizado como serviço compartilhado.
