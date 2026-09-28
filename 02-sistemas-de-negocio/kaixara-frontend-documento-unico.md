---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Kaixara — Frontend: Documento Único
### Discovery → Arquitetura da Informação → Design System → UI → Prototipação → Engenharia → Acessibilidade → QA → Performance → Segurança → Lançamento (11 etapas)
### Substitui os 5 documentos anteriores de frontend, com as correções já integradas ao raciocínio, não em anexo separado

---

## ETAPA 1 — Discovery e Pesquisa de Usuário

### 1.1 Declaração do problema

> Pequenos e médios varejistas precisam de um sistema de ponto de venda confiável, rápido e capaz de operar mesmo com internet instável, porque a venda não pode parar por causa de sistema — mas hoje a maioria usa planilha, caderno, ou sistema genérico caro que não foi pensado pra velocidade real de quem opera o caixa.

### 1.2 Personas — **hipótese fundamentada, ainda não validada com usuário real**

**Correção integrada:** as duas personas abaixo nascem de raciocínio sobre o domínio, não de entrevista real. Tratá-las como fato seria o erro que a Etapa 1 original cometeu. Elas orientam decisão de design **provisoriamente**, até validação (ver 1.5).

| Persona | Objetivo principal | Frustração com sistema tradicional | O que isso exige do design |
|---|---|---|---|
| **Operador de Caixa** | Finalizar venda rápido, sem erro, sob fila de cliente | Tela lenta, exige muito clique, trava sem internet | Interface operável por teclado *e* clique, tolerância a falha de rede, feedback imediato |
| **Gerente/Dono** | Saber se o negócio vai bem, sem interpretar dado bruto | Relatório confuso, sem visão em tempo real | Dashboard de densidade baixa, linguagem sem jargão, número grande e claro |

### 1.3 Jobs-to-be-Done

- "Quando um cliente está na fila, eu quero registrar a venda o mais rápido possível, para que a fila não cresça."
- "Quando a internet cai no meio do expediente, eu quero continuar vendendo normalmente, para que o negócio não pare de faturar."
- "Quando eu chego na loja de manhã, eu quero saber rapidamente como foi o dia anterior, para que eu decida se preciso agir em algo hoje."

### 1.4 Análise competitiva — **correção: seção nova, não existia antes**

| Concorrente | Ponto forte | Ponto fraco | Brecha real pro AM Kaixara |
|---|---|---|---|
| Sistema genérico de mercado (ex: Superlógica e afins) | Robusto, muitos recursos | Contrato pesado, onboarding lento, não pensado pra velocidade de operação | Venda direta ao pequeno lojista, sem venda consultiva, com foco em velocidade de uso, não em quantidade de funcionalidade |
| Caderno/planilha (o "concorrente" mais comum de verdade) | Zero custo, zero curva de aprendizado | Sem controle de estoque real, sem histórico confiável, erro humano constante | Substituir com curva de aprendizado baixa o suficiente pra competir com "não ter sistema nenhum" |

### 1.5 Suposições e riscos — **correção: seção nova**

| Suposição | Validada? | Como validar |
|---|---|---|
| Operador prefere atalho de teclado a clique | ❌ Não validada | 3-5 conversas reais com operador de caixa real, pergunta direta: "teclado ou tela touch?" |
| Internet cai com frequência que justifica modo offline complexo | ❌ Não validada | Perguntar a pequenos comerciantes locais sobre estabilidade real da conexão |
| Dono de negócio olha dashboard pela manhã | ❌ Não validada, é suposição de comportamento | Observação de campo — 15-20 min acompanhando rotina real de um dono de pequeno negócio |

**Ação concreta pendente, fora do documento:** as 3-5 conversas reais (Barbacena, comércio local, gente que você já conhece) precisam acontecer antes de tratar a Etapa 1 como definitivamente encerrada — o resto deste documento já pode avançar em paralelo, mas as personas continuam marcadas como hipótese até lá.

### ✅ Checklist de execução — Etapa 1
- [ ] Realizar 3-5 conversas reais com dono/operador de pequeno comércio
- [ ] Atualizar a tabela de persona (1.2) com citação real entre aspas de quem você conversou
- [ ] Marcar cada suposição da tabela 1.5 como validada ou refutada após as conversas
- [ ] Confirmar se a Análise Competitiva (1.4) precisa de mais um concorrente pesquisado

### 1.6 Fora de escopo — **correção: seção nova**

Este sistema **não** resolve: gestão de recursos humanos, emissão de boleto de fornecedor, controle fiscal completo de grande empresa. É focado em pequeno/médio varejo de balcão — venda, estoque, caixa.

### 1.7 Jornada — estado atual vs. estado futuro

```
ATUAL: Cliente chega → preço de memória/caderno → troco calculado na mão →
        venda anotada ou não anotada → fim do dia sem precisão real de quanto vendeu

FUTURO: Cliente chega → busca de produto com foco automático → total automático →
         confirmação instantânea (UI otimista) → estoque atualiza com proteção de
         concorrência → dono vê o dia em tempo real, sem reconstruir nada
```

### 1.8 Métricas de sucesso

- Tempo médio de conclusão de uma venda (comparado ao processo manual)
- Taxa de erro de caixa (diferença entre dinheiro esperado e real ao fechar)
- Tempo de recuperação após queda de internet (sincronização sem intervenção manual)

---

## ETAPA 2 — Arquitetura da Informação

### 2.1 Inventário completo de telas

| Tela | Perfil que acessa | Ligada a qual Job-to-be-Done (1.3) |
|---|---|---|
| Login | Todos | Pré-requisito de tudo |
| **PDV (venda)** | Operador | "Registrar venda rápido" |
| Indicador de status offline/online | Operador | "Continuar vendendo sem internet" |
| Dashboard | Gerente | "Saber como foi o dia anterior" |
| Lista de produtos | Gerente/Operador com permissão | Suporte ao PDV |
| Cadastro/edição de produto | Gerente | Suporte ao PDV |
| Histórico de vendas | Gerente | Suporte ao Dashboard |
| Abertura/fechamento de caixa | Operador (abre turno) / Gerente (audita) | Suporte ao "erro de caixa" (métrica 1.8) |
| Configuração (perfil, filial) | Gerente | Suporte geral |
| Painel de atalhos (`?`) | Operador | Suporte à descoberta do diferencial (4.8) |

### 2.2 Fluxo — "Registrar venda rápido" (o fluxo mais crítico do sistema)

```
Login → PDV carrega com campo de busca já em foco
  → Operador digita/escaneia produto → resultado aparece em grid
  → Clique ou Enter adiciona ao carrinho (atualização otimista, 4.7)
  → Repete até fechar a venda
  → Atalho ou clique em "Confirmar venda"
  → Modal breve de meio de pagamento
  → Confirmação → recibo gerado → carrinho limpa, campo de busca volta ao foco
     (pronto pra próxima venda, sem passo extra de navegação)
```
**Decisão de arquitetura de informação:** depois de confirmar uma venda, o sistema **não navega pra outra tela** — volta ao estado inicial do PDV automaticamente. Isso é deliberado: cada tela extra entre uma venda e a próxima é tempo perdido pro Operador (Persona 1.2).

### 2.3 Fluxo — "Continuar vendendo sem internet"

```
Conexão cai → indicador de status muda (visível, não intrusivo) →
Operador continua usando o PDV normalmente, sem nenhuma tela ou modal de interrupção →
Conexão volta → indicador muda de novo → sincronização acontece em segundo plano,
sem exigir ação do operador
```
**Decisão de arquitetura de informação:** a queda de conexão **nunca** interrompe o fluxo de venda com modal bloqueante — só muda um indicador de status. Interromper o operador no meio da venda pra avisar "você está offline" seria pior que a própria queda de conexão.

### 2.4 Fluxo — "Saber como foi o dia anterior"

```
Login (Gerente) → Dashboard é a tela inicial (não o PDV) →
Indicador principal (faturamento do dia/período) já visível sem rolar →
Clique em indicador → navega pro Histórico de vendas filtrado automaticamente
```
**Decisão de arquitetura de informação:** login de Gerente e login de Operador levam a **telas iniciais diferentes** (Dashboard vs. PDV) — cada perfil cai direto no que resolve o job dele, sem precisar navegar até lá.

### 2.5 Navegação global (shell administrativo)

Sidebar com 4 itens no máximo visíveis por padrão (Dashboard, Produtos, Vendas, Configuração) — número pequeno de propósito, ligado à heurística de minimalismo (4.1). Itens adicionais (Caixa, Atalhos) acessíveis, mas não competindo visualmente com os 4 principais.

### ✅ Checklist de execução — Etapa 2
- [ ] Confirmar que o roteamento (Next.js App Router) reflete exatamente as 9 telas do inventário, nenhuma a mais nem a menos no MVP
- [ ] Implementar redirecionamento por perfil no login (Gerente → Dashboard, Operador → PDV)
- [ ] Implementar retorno automático ao estado inicial do PDV após confirmar venda
- [ ] Implementar indicador de status online/offline não-bloqueante

---

## ETAPA 3 — Fundamentos de Design System

### 3.1 Paleta — correção: valores exatos, não mais descrição

| Token | Valor hex | Uso |
|---|---|---|
| `--aura-primaria` | `#0E3A45` | Cor primária do painel administrativo (azul petróleo/marinho) |
| `--aura-primaria-hover` | `#0A2C35` | Estado hover/ativo da cor primária (10% mais escura) |
| `--aura-grafite` | `#2D3436` | Texto principal, ícone padrão |
| `--aura-off-white` | `#F7F5F0` | Fundo de superfície, cartão |
| `--aura-acento` | `#B08D57` | Dourado — call-to-action, destaque, nunca dominante |
| `--aura-acento-hover` | `#98753F` | Estado hover do acento |
| `--aura-neutro-borda` | `#E4E0D5` | Borda de cartão, divisor |
| `--aura-neutro-texto-fraco` | `#7A8A8C` | Texto secundário, legenda |

Esses são os valores oficiais e definitivos — qualquer tela nova consulta esta tabela, nunca reinventa "um azul parecido". Nunca personalizável no painel interno, só nas superfícies públicas (loja online, portal do cliente), conforme já definido no RNFT-D.

### 3.2 Tipografia
| Uso | Fonte | Peso | Tamanho |
|---|---|---|---|
| Título de página | Inter | 600 | 24px |
| Corpo de texto | Inter | 400 | 14px |
| **Dado numérico (preço, quantidade)** | **Monoespaçada (JetBrains Mono)** | 500 | 14-16px |

Fonte monoespaçada só em número: alinha dígito por dígito, tornando R$ 19,90 e R$ 119,90 visualmente distintos de relance — decisão pensada pra quem escaneia preço sob pressão de fila, não decoração.

### 3.3 Espaçamento, elevação, ícone
Grade de 4px como unidade base. Sombra sutil em cartão (`shadow-sm`), mais forte em modal (`shadow-lg`). Borda 8px padrão, 4px em elemento pequeno. Um único conjunto de ícone (Lucide) em todo o sistema, nunca misturado.

### 3.4 Cores semânticas
Erro, sucesso, alerta e informação **sempre fixas**, nunca personalizáveis por tenant — mesmo que a cor de marca do cliente seja parecida, não pode gerar confusão visual entre "isso é a marca" e "isso é um erro" (RNFT-D02).

| Token | Valor hex |
|---|---|
| `--aura-erro` | `#C0392B` |
| `--aura-sucesso` | `#2E7D5B` |
| `--aura-alerta` | `#C99A3E` |
| `--aura-info` | `#3B6FA0` |

### 3.5 Escala de sombra (elevação) — correção: valor exato, não só nome de classe Tailwind
| Token | Valor CSS |
|---|---|
| `--aura-sombra-sm` (cartão) | `0 1px 3px rgba(14,58,69,0.08)` |
| `--aura-sombra-lg` (modal/dropdown) | `0 12px 32px rgba(14,58,69,0.22)` |

### 3.6 Z-index — correção: nunca tinha sido definido, risco real de conflito de camada
| Token | Valor | Uso |
|---|---|---|
| `--z-conteudo` | `1` | Conteúdo normal da página |
| `--z-header-fixo` | `10` | Barra de atalho fixa, cabeçalho |
| `--z-dropdown` | `20` | Menu suspenso, autocomplete de busca |
| `--z-modal-overlay` | `30` | Fundo escurecido atrás de modal |
| `--z-modal` | `31` | Conteúdo do modal (sempre 1 acima do overlay) |
| `--z-toast` | `40` | Notificação — sempre acima de tudo, inclusive modal |

### 3.7 Animação — correção: biblioteca já estava escolhida (Framer Motion), valores nunca foram
| Token | Valor | Uso |
|---|---|---|
| `--dur-rapida` | `120ms` | Hover, feedback de clique (adicionar item ao carrinho) |
| `--dur-padrao` | `220ms` | Abertura de modal, transição de tela |
| `--dur-lenta` | `380ms` | Entrada de notificação toast |
| `--easing-padrao` | `cubic-bezier(0.2, 0, 0, 1)` | Curva padrão pra toda transição — sensação de "chegada suave", nunca linear |

### 3.8 Escala de ícone — correção: nunca especificado
| Token | Valor | Uso |
|---|---|---|
| `--icone-sm` | `16px` | Ícone dentro de botão pequeno, badge |
| `--icone-md` | `20px` | Ícone padrão (menu, campo de busca) |
| `--icone-lg` | `28px` | Ícone de destaque (estado vazio, cabeçalho de card) |

### 3.9 Cor de estado dinâmico — correção: página "não estática" nunca tinha token próprio

Tudo até a seção 3.8 cobre cor **estática** (primária, neutro, semântica fixa). Elemento que muda de estado em tempo real — badge, gráfico, indicador de conexão — nunca tinha cor formalizada, e cada demonstração visual inventava valor novo sem virar padrão.

**Paleta de visualização de dado (gráfico com múltiplas séries)** — usada em qualquer dashboard do portfólio, não só AM Kaixara:
| Token | Valor hex |
|---|---|
| `--viz-1` | `#B08D57` (dourado — série principal) |
| `--viz-2` | `#4A9DD6` (azul) |
| `--viz-3` | `#C96A3F` (terracota) |
| `--viz-4` | `#8A6FD6` (roxo) |
| `--viz-5` | `#5AA88A` (verde-azulado) |

Ordem fixa — a primeira série de qualquer gráfico novo usa sempre `--viz-1`, nunca escolhida ao acaso pela pessoa que constrói a tela naquele dia.

**Badge de status** (venda, produto, OS — qualquer entidade com ciclo de vida):
| Status | Token | Valor |
|---|---|---|
| Aberta / em andamento | `--status-aberta` | `#3B6FA0` (mesmo tom de `--aura-info`) |
| Confirmada / concluída | `--status-confirmada` | `#2E7D5B` (mesmo tom de `--aura-sucesso`) |
| Cancelada | `--status-cancelada` | `#7A8A8C` (neutro — cancelado não é "erro", é neutro) |
| Com divergência / atenção | `--status-divergencia` | `#C99A3E` (mesmo tom de `--aura-alerta`) |

**Anel de foco (acessibilidade, Etapa 7):**
| Token | Valor |
|---|---|
| `--foco-anel` | `2px solid #4A9DD6` com `offset: 2px` — nunca a cor primária (contraste insuficiente em fundo escuro do header) |

**Indicador de conexão (online/offline):**
| Estado | Token | Valor |
|---|---|
| Online | `--conexao-online` | `#2E7D5B`, ponto sólido |
| Offline | `--conexao-offline` | `#C99A3E`, ponto pulsante (usa `--dur-lenta` já definida em 3.7) |

**Shimmer de skeleton screen:**
| Token | Valor |
|---|---|
| `--skeleton-base` | `#EEECE5` |
| `--skeleton-shimmer` | gradiente animado de `#EEECE5` → `#F7F5F0` → `#EEECE5`, usando `--dur-lenta` e `--easing-padrao` |

### ✅ Checklist de execução — Etapa 3 (atualizado)
- [ ] Criar arquivo único de tokens (CSS custom properties) com as variáveis de 3.1-3.9, nenhuma cor/sombra/z-index/duração fora dele
- [ ] Configurar fonte monoespaçada como classe utilitária reaproveitável (`.tabular-nums` ou equivalente)
- [ ] Validar contraste de cada combinação de cor semântica contra fundo (WCAG AA), não só a cor de marca
- [ ] Importar o único conjunto de ícone (Lucide) e remover qualquer outro que apareça no projeto
- [ ] Configurar `z-index` de todo componente sobreposto usando exclusivamente os tokens de 3.6
- [ ] Implementar o componente de badge de status usando os 4 tokens de 3.9, reaproveitável em qualquer entidade com ciclo de vida (venda, OS, produto)
- [ ] Aplicar `--foco-anel` globalmente via CSS, testado com navegação por Tab

---

## ETAPA 4 — Design Visual e Usabilidade

### 4.1 Heurísticas de Nielsen aplicadas ao AM Kaixara

| Heurística | Aplicação concreta |
|---|---|
| Visibilidade do status | Toda ação tem feedback visual imediato |
| Controle do usuário | Cancelamento de venda sempre visível, nunca escondido |
| Consistência | `Esc` sempre cancela/fecha, em qualquer tela |
| Prevenção de erro | Ação destrutiva exige confirmação rápida, com nome específico do que será afetado |
| Reconhecimento > memorização | Busca mostra resultado ao digitar; atalho fica visível em barra fixa |
| Flexibilidade | Mouse e teclado sempre disponíveis, nenhum exclui o outro |
| Minimalismo | Tela de PDV mostra só o que a venda atual precisa |
| Recuperação de erro | Mensagem específica e acionável ("Estoque insuficiente — restam 3"), nunca genérica |

### 4.2 Densidade de informação — variável por contexto, de propósito

- **Tela de PDV:** densidade alta — várias linhas visíveis sem rolar, número grande, pouco espaço em branco — justificado pela Persona Operador (1.2), que usa sob pressão de tempo
- **Dashboard:** densidade baixa, mais respiro visual — justificado pela Persona Gerente (1.2), que analisa com calma

### 4.3 Layout — Tela de PDV
```
┌─────────────────────────────────────────────┐
│ Barra de atalhos fixa (sempre visível)       │
├──────────────────────────┬────────────────────┤
│ Busca de produto           │ Carrinho da venda   │
│ (foco automático)          │ (densidade alta)    │
│ Grid de resultado           │ Total (fonte mono,  │
│                             │  tamanho grande)     │
│                             │ [Confirmar venda]    │
└──────────────────────────┴────────────────────┘
```
Duas colunas, nunca empilhado — carrinho sempre visível, sem precisar rolar durante o fluxo de venda.

### 4.4 Layout — Shell administrativo
Sidebar fixa à esquerda, header com contexto (filial/usuário), conteúdo com densidade baixa — convenção de painel administrativo, porque aqui a convenção ajuda mais do que atrapalha.

### 4.5 Responsivo e alvo de toque

| Breakpoint | Uso |
|---|---|
| `< 768px` | Não prioridade pro fluxo de venda; portal do cliente precisa funcionar |
| `768-1024px` (tablet) | **Caso de uso real do PDV** — layout de duas colunas precisa continuar funcionando |
| `> 1024px` | Layout padrão |

Alvo de toque mínimo 44x44px em qualquer elemento clicável que possa rodar em tablet.

### 4.6 Estados de componente
Todo elemento interativo precisa dos 5 estados: `padrão → hover → foco → ativo → desabilitado` — documentado uma vez, aplicado em todo componente novo, evitando inconsistência.

### 4.7 Padrões de interação
- Formulário valida em tempo real (ao perder foco), nunca só ao submeter
- Confirmação destrutiva com nome específico do afetado ("Cancelar venda de R$ 45,90?")
- Feedback de sucesso via notificação discreta (toast), nunca modal bloqueante
- Loading via skeleton screen, nunca spinner sem contexto
- **UI otimista no carrinho** — tela atualiza antes da confirmação do servidor chegar, reverte só se rejeitado
- Folha de estilo `@media print` dedicada pro recibo (RF15) — remove navegação, formata pra papel de impressora térmica

### 4.8 Descoberta do diferencial central
**PDV operável 100% por teclado** é o diferencial mais forte do sistema (ligado à Persona Operador). Pra não ficar escondido: tecla `?` abre painel com todos os atalhos disponíveis a qualquer momento, padrão já usado por Gmail/Linear.

### 4.9 Primeira experiência (tenant novo, banco vazio)
Estado vazio sempre com chamada de ação clara ("Cadastre seu primeiro produto"), nunca tabela em branco sem contexto.

### 4.10 Tom de voz (microcopy)
Direto e sem jargão, nunca robótico nem engraçadinho — "Estoque insuficiente", não "Ops! 😅" nem "ERRO: QTD_INVALIDA".

### ✅ Checklist de execução — Etapa 4
- [ ] Implementar as 8 heurísticas (4.1) como checklist de revisão antes de considerar qualquer tela "pronta"
- [ ] Construir o layout de PDV (4.3) e o shell administrativo (4.4) como os dois primeiros componentes de página
- [ ] Testar o layout de PDV especificamente no breakpoint de tablet (4.5) antes de dar como pronto
- [ ] Documentar os 5 estados (4.6) num componente de botão primeiro, reaproveitar o padrão nos demais
- [ ] Implementar a folha `@media print` do recibo (4.7) como item isolado, testável sem depender do resto da tela
- [ ] Implementar o painel de atalhos (`?`) da seção 4.8 — sem isso, o diferencial central do sistema fica invisível
- [ ] Escrever um guia curto de tom de voz (4.10) com 5-10 exemplos de mensagem, pra manter consistência conforme o sistema crescer

---

## ETAPA 5 — Prototipação e Validação

### 5.1 Nível de fidelidade certo pra quem trabalha sozinho

Empresa grande prototipa em ferramenta separada (Figma) antes de codar. Pra você, sozinho, isso teria custo maior que benefício — a decisão certa é **prototipar direto nos componentes reais** (o próprio Storybook, já planejado na Etapa 8), o que economiza retrabalho de "desenhar duas vezes" (uma no Figma, outra no código).

**Exceção:** o fluxo do PDV (2.2) — por ser o mais crítico — vale um rascunho rápido em papel ou ferramenta gratuita simples (Excalidraw, Figma free tier) **antes** de virar componente, só pra testar a sequência de clique/atalho sem custo de código.

### 5.2 Teste de usabilidade — adaptado pra validação leve, não formal

Regra de mercado (Nielsen): **5 usuários já revelam ~85% dos problemas de usabilidade** — não precisa de amostra grande. Combinado com a Etapa 1.5 (validação de persona), isso pode ser a mesma rodada de conversa:

1. Pegar as mesmas 3-5 pessoas da validação de persona (1.5)
2. Mostrar o protótipo/rascunho do fluxo de PDV (2.2)
3. Pedir pra "pensar em voz alta" enquanto tenta registrar uma venda fictícia
4. Anotar onde travou, hesitou, ou fez diferente do esperado — não corrigir na hora, só observar

### 5.3 Roteiro de tarefa pro teste

| Tarefa dada à pessoa | O que você está observando |
|---|---|
| "Registre a venda de 2 unidades do produto X" | Encontra a busca sem ajuda? Usa teclado ou clica? |
| "Agora cancele essa venda" | Encontra a opção de cancelar sem procurar muito? |
| "O sistema perdeu internet no meio de uma venda — o que você faria?" | Entende o indicador de status, ou fica em pânico/confuso? |

### 5.4 Critério de sucesso do teste

Se 4 de 5 pessoas completam a tarefa 1 sem pedir ajuda, o fluxo do PDV está validado o suficiente pra seguir pra implementação real. Se menos que isso, revisar a Etapa 2.2 antes de continuar — mais barato ajustar um rascunho que reescrever código.

### ✅ Checklist de execução — Etapa 5
- [ ] Rascunhar o fluxo do PDV em papel ou Excalidraw antes de codar (não precisa ser bonito, precisa ser testável)
- [ ] Combinar a validação de usabilidade com a mesma rodada de conversa da Etapa 1.5, uma única vez, não duas
- [ ] Aplicar o roteiro de 3 tarefas (5.3) com pelo menos 3 pessoas
- [ ] Registrar resultado contra o critério de sucesso (5.4) antes de considerar o fluxo do PDV fechado

---

## ETAPA 6 — Engenharia Frontend

### 6.1 Estado
| Tipo | Ferramenta |
|---|---|
| Estado de servidor | TanStack Query (React Query) |
| Estado de UI local | Zustand |
| Tempo real (SignalR) | Hook customizado conectando SignalR ao React Query |

### 6.2 Performance
Server Components por padrão (só `"use client"` onde precisa de interatividade). Meta: LCP < 2.5s, INP < 200ms, CLS < 0.1, medido via Lighthouse.

### 6.3 Modo escuro
Extensão barata do sistema de tokens já existente — trocar valor de variável, não reconstruir.

### 6.4 Cliente de API — correção: não especificado antes
O cliente HTTP não é escrito manualmente endpoint por endpoint — é **gerado automaticamente a partir do contrato OpenAPI** já definido em `kaixara-especificacao-tecnica-completa` (seção 2). Isso garante que o contrato (backend) e o cliente (frontend) nunca ficam dessincronizados — se o backend mudar um campo, o cliente gerado quebra a build, avisando o problema em tempo de desenvolvimento, não em produção.

### 6.5 Carregamento de tema por tenant em runtime — correção: não especificado antes
Ao abrir o sistema, antes de renderizar qualquer tela: identificar o tenant (por subdomínio, ex: `lojadojoao.kaixara.com`, ou por token já autenticado) → buscar a configuração de tema daquele tenant (cor de marca, logo) → aplicar os tokens (RNFT-D) antes da primeira renderização visível, evitando "flash" de tema padrão trocando pro tema real um instante depois.

### 6.6 Feature flag ligado ao `aura-licensing` — correção: não especificado antes
O menu de navegação (Etapa 2.5) não é fixo — cada item consulta se o módulo correspondente está ativo pro tenant (via `aura-licensing`) antes de aparecer. Um tenant sem o módulo de Dashboard avançado, por exemplo, simplesmente não vê esse item no menu — não é "aparece desabilitado", é "não aparece", evitando poluição visual com funcionalidade que o cliente não contratou.

### ✅ Checklist de execução — Etapa 6
- [ ] Configurar TanStack Query com tempo de cache padrão definido (não usar o default genérico sem pensar)
- [ ] Configurar Zustand só pro estado que realmente precisa ser global (carrinho em edição) — não usar pra tudo
- [ ] Implementar o hook customizado de SignalR + React Query, testado no Dashboard primeiro
- [ ] Medir Core Web Vitals com Lighthouse antes de considerar qualquer tela pronta, não só no fim
- [ ] Implementar modo escuro só depois do modo claro estar 100% consistente — não construir os dois em paralelo
- [ ] Configurar geração automática do cliente de API a partir do OpenAPI, nunca escrever chamada HTTP manual
- [ ] Implementar a busca de configuração de tema antes da primeira renderização (evitar flash de tema padrão)
- [ ] Implementar o menu condicional por módulo ativo (`aura-licensing`), testado com pelo menos 2 combinações de módulo diferentes

---

## ETAPA 7 — Acessibilidade

Navegação completa por teclado (já central ao diferencial, 4.8). `aria-label` em todo elemento interativo sem texto visível. Testado com leitor de tela real (NVDA), nota no README. Foco visível e gerenciado em modal/dropdown.

### ✅ Checklist de execução — Etapa 7
- [ ] Percorrer o fluxo completo de venda (2.2) usando só teclado, sem mouse nenhuma vez
- [ ] Instalar o NVDA (gratuito) e testar o mesmo fluxo com o leitor de tela ligado
- [ ] Auditar todo botão/ícone sem texto visível e adicionar `aria-label`
- [ ] Testar o foco de todo modal — abre com foco dentro, fecha devolvendo foco pro elemento que abriu

---

## ETAPA 8 — QA e Teste

Testing Library pra componente. Playwright pra pelo menos um E2E real (login até recibo). Storybook publicado documentando o design system visualmente, via GitHub Pages.

### ✅ Checklist de execução — Etapa 8
- [ ] Escrever teste de componente pro carrinho de venda primeiro (é o mais crítico)
- [ ] Escrever o E2E completo (2.2) com Playwright — login → busca → adicionar item → confirmar → recibo
- [ ] Publicar Storybook com pelo menos os componentes de 4.6 (botão nos 5 estados) e 4.3 (layout de PDV)
- [ ] Adicionar badge de teste passando no README, junto com o de CI já planejado no backend

---

## ETAPA 9 — Performance (aprofundamento)

Coberto em 6.2 — meta explícita de Core Web Vitals, não acidente.

### ✅ Checklist de execução — Etapa 9
- [ ] Rodar Lighthouse na tela de PDV e no Dashboard separadamente — são perfis de uso diferentes, podem ter resultado diferente
- [ ] Documentar o resultado do Lighthouse com print no README (prova visual, não só afirmação)
- [ ] Revisitar a meta de Core Web Vitals depois do deploy real, com uso de verdade, não só ambiente local

---

## ETAPA 10 — Segurança de Frontend

**Gap identificado e corrigido:** esta etapa tinha sido nomeada como área de empresa grande, mas nunca voltou pro documento único até agora.

### 10.1 Sanitização de dado exibido
Todo dado que vem do backend e é exibido na tela (nome de produto, nota de venda) passa por sanitização antes de renderizar — mesmo sendo dado do próprio tenant, nunca confiar cegamente que texto livre digitado por um usuário não contém tentativa de injeção de script.

### 10.2 Content Security Policy (CSP)
Cabeçalho configurado restringindo de onde o navegador pode carregar script, evitando que uma eventual falha de sanitização vire execução de código malicioso de verdade.

### 10.3 Armazenamento de dado sensível no cliente
Token de autenticação nunca em `localStorage` puro sem proteção — usar cookie `httpOnly` (inacessível a JavaScript, reduzindo superfície de roubo de token via XSS) sempre que a arquitetura permitir.

### 10.4 Dependência de terceiro
Toda biblioteca nova (Framer Motion, TanStack Query, etc.) passa por checagem de vulnerabilidade conhecida antes de entrar no projeto — mesmo princípio já usado no backend (RNFT-S05), aplicado aqui ao `npm`/`package.json`.

### ✅ Checklist de execução — Etapa 10
- [ ] Configurar sanitização de saída em qualquer campo que renderize texto vindo do backend
- [ ] Configurar cabeçalho CSP no Next.js
- [ ] Migrar armazenamento de token pra cookie `httpOnly`
- [ ] Configurar scan automatizado de dependência vulnerável (Dependabot ou equivalente) no repositório de frontend

---

## ETAPA 11 — Lançamento e Operação

**Gap identificado e corrigido:** a sequência original sempre teve esta etapa; o documento consolidado tinha parado na Etapa 9 sem ela.

### 11.1 Estratégia de build e cache
Next.js gerando páginas estáticas onde possível (catálogo público, se existir) e Server-Side Rendering onde o dado precisa ser sempre atual (PDV, Dashboard). CDN na frente dos assets estáticos (JS, CSS, imagem), nunca do conteúdo dinâmico.

### 11.2 Invalidação de cache pós-deploy
Cada novo deploy gera hash novo de arquivo estático — o navegador do usuário nunca fica preso numa versão antiga em cache, porque o nome do arquivo muda, não só o conteúdo.

### 11.3 Configuração por ambiente
URL da API, chave pública de serviço externo — tudo via variável de ambiente, nunca hardcoded, com valor diferente entre desenvolvimento/produção claramente documentado no README.

### 11.4 Plano de rollback específico de frontend
Se um deploy novo quebrar algo visualmente (diferente de bug de backend), o rollback do frontend precisa ser independente do rollback de backend — os dois podem falhar em momentos diferentes, não devem estar acoplados um ao outro.

### 11.5 Instrumentação e telemetria — fecha o ciclo aberto na Etapa 1.8
As métricas de sucesso definidas no Discovery (tempo médio de venda, taxa de erro de caixa, tempo de recuperação offline) só existem de verdade se forem **medidas em produção**, não só aspiração de design. Ferramenta leve e gratuita (ex: Plausible self-hosted, ou evento customizado registrado via `aura-historico` já existente no backend) capturando: tempo entre abertura do PDV e confirmação de venda, ocorrência de erro de concorrência de estoque, tempo entre queda e recuperação de conexão.

### ✅ Checklist de execução — Etapa 11
- [ ] Configurar CDN pra asset estático, separado do conteúdo dinâmico
- [ ] Confirmar que hash de arquivo muda a cada deploy (invalidação automática de cache do navegador)
- [ ] Documentar toda variável de ambiente necessária, com exemplo, no README
- [ ] Testar o rollback de frontend isoladamente, sem depender de rollback de backend acontecer junto
- [ ] Instrumentar os 3 eventos de telemetria ligados às métricas da Etapa 1.8, antes de declarar o sistema "lançado"

---

## Definition of Done — critério de aceite geral do frontend

O frontend do AM Kaixara está pronto pra apresentação quando, e só quando:

- [ ] As 11 etapas têm todo checklist de execução marcado
- [ ] O fluxo crítico (2.2) passa no teste de usabilidade com pelo menos 4 de 5 pessoas (5.4)
- [ ] Teste E2E (8) passa no CI a cada push
- [ ] Lighthouse (9) documentado com print real no README
- [ ] Leitor de tela (7) testado no fluxo crítico, não só em tela isolada
- [ ] CSP e sanitização (10) configurados, não pendentes
- [ ] Deploy real (11) com link funcionando, testado a partir de navegador limpo, sem cache antigo
- [ ] As 3 métricas de sucesso (1.8) sendo capturadas de verdade, com pelo menos alguns dias de dado real depois do lançamento

## O que este documento único resolve

Substitui a necessidade de navegar entre 5 documentos separados — o raciocínio é linear, do problema até o lançamento, com as correções dentro do fluxo principal, cobrindo agora as **11 etapas completas**, cada uma com checklist de execução próprio, fechando com o Definition of Done acima.

**Pendência real que nenhum checklist substitui:** a validação de persona com gente real (1.5/checklist da Etapa 1) — é o único item que depende de sair do documento e conversar com alguém de verdade antes de tratar o sistema como "descentemente" fundamentado, não só bem planejado no papel.
