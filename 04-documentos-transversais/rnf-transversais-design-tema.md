---
tags: [transversal, portfolio-ams]
tipo: regra-transversal
status: completo
---

# RNF Transversais — Design e Tema
### Documento de referência única, aplicável a todo sistema do portfólio com interface visual, sem exceção

Segue o mesmo princípio dos outros RNF Transversais: não pertence a nenhum sistema específico, é referenciado pelo documento de cada um. Formaliza como personalização visual (cor de marca do cliente) convive com consistência de portfólio, sem colocar em risco a qualidade da experiência de ninguém.

---

## 0. Paleta padrão Aura (base, usada em todo painel administrativo)

**Atualização: valores exatos, corrigindo a lacuna encontrada na auditoria do frontend do AM Kaixara.** Antes desta correção, a paleta existia só como descrição ("azul petróleo", "dourado") — nenhum documento tinha o valor hexadecimal definitivo, o que significava que cada tela nova corria o risco de usar um tom levemente diferente do anterior.

| Token | Valor hex | Uso |
|---|---|---|
| `--aura-primaria` | `#0E3A45` | Cor primária de marca, todo painel administrativo do portfólio |
| `--aura-primaria-hover` | `#0A2C35` | Estado hover/ativo |
| `--aura-grafite` | `#2D3436` | Texto principal |
| `--aura-off-white` | `#F7F5F0` | Fundo de superfície |
| `--aura-acento` | `#B08D57` | Destaque pontual (dourado/cobre) — nunca dominante |
| `--aura-erro` | `#C0392B` | Semântica, fixa (RNFT-D02) |
| `--aura-sucesso` | `#2E7D5B` | Semântica, fixa |
| `--aura-alerta` | `#C99A3E` | Semântica, fixa |
| `--aura-info` | `#3B6FA0` | Semântica, fixa |

Esta é a paleta padrão de todo painel administrativo — construída uma vez, reaproveitada em todos os sistemas. Sistemas com identidade de sub-marca própria (ex: Momentos/Cupido em bordô/dourado, AM Rendara em verde-esmeralda/dourado) substituem `--aura-primaria` pela cor própria, mas mantêm a mesma estrutura de token — nunca inventam um nome de variável novo.

---

## 0.1 Valores transversais de elevação, z-index e animação — correção: nunca existiam

Aplicam-se a todo sistema do portfólio, não só ao AM Kaixara:

| Categoria | Token | Valor |
|---|---|---|
| Sombra | `--aura-sombra-sm` | `0 1px 3px rgba(14,58,69,0.08)` |
| Sombra | `--aura-sombra-lg` | `0 12px 32px rgba(14,58,69,0.22)` |
| Camada | `--z-header-fixo` | `10` |
| Camada | `--z-dropdown` | `20` |
| Camada | `--z-modal-overlay` / `--z-modal` | `30` / `31` |
| Camada | `--z-toast` | `40` |
| Animação | `--dur-rapida` / `--dur-padrao` / `--dur-lenta` | `120ms` / `220ms` / `380ms` |
| Animação | `--easing-padrao` | `cubic-bezier(0.2, 0, 0, 1)` |

---

## 0.2 Cor de estado dinâmico — correção: nunca existia, aplicável a todo sistema com dashboard ou entidade com ciclo de vida

Diferente da paleta estática (seção 0), esta cobre elemento que muda de estado em tempo real — necessário em qualquer sistema do portfólio com gráfico, badge de status ou indicador de conexão, não só o AM Kaixara.

| Categoria | Token | Valor |
|---|---|---|
| Visualização de dado (série 1-5) | `--viz-1` a `--viz-5` | `#B08D57` `#4A9DD6` `#C96A3F` `#8A6FD6` `#5AA88A` |
| Status: aberto/andamento | `--status-aberta` | `#3B6FA0` |
| Status: confirmado/concluído | `--status-confirmada` | `#2E7D5B` |
| Status: cancelado | `--status-cancelada` | `#7A8A8C` |
| Status: divergência/atenção | `--status-divergencia` | `#C99A3E` |
| Anel de foco (acessibilidade) | `--foco-anel` | `2px solid #4A9DD6`, offset 2px |
| Conexão online/offline | `--conexao-online` / `--conexao-offline` | `#2E7D5B` / `#C99A3E` |
| Skeleton loading | `--skeleton-base` / `--skeleton-shimmer` | `#EEECE5` / gradiente animado |

Todo sistema com dashboard (AM Rendara, AuraVet, AM Predara, AM Consertta) usa **exatamente** essa paleta de visualização de dado, na mesma ordem de série — nunca inventa cor nova pra gráfico próprio.

---

## RNFT-D01 — Base fixa de design (tipografia, espaçamento, layout, comportamento)

**Requisito:** tipografia, escala de espaçamento, grid de layout e comportamento de componente (como um botão reage a hover/clique, como um modal abre) são fixos e idênticos em todo o portfólio — nunca variam por tenant, nunca são personalizáveis.

**Critério de verificação:** dois sistemas diferentes do portfólio, renderizados lado a lado, devem ter a mesma fonte, o mesmo espaçamento e o mesmo comportamento de componente — só a cor de marca (RNFT-D03) pode diferir.

**Aplica-se a:** todos os sistemas com interface visual, sem exceção.

---

## RNFT-D02 — Cores semânticas fixas

**Requisito:** cor de erro, sucesso, alerta e informação nunca são personalizáveis por tenant, independente de qual cor de marca o cliente escolher.

**Critério de verificação:** um cliente com cor de marca vermelha não pode fazer o botão "comprar" (marca) e a mensagem de erro do sistema ficarem visualmente parecidos — cor semântica sempre distinta da cor de marca escolhida.

**Aplica-se a:** todos os sistemas, sem exceção.

**Por que existe:** confundir cor de significado com cor de marca é o tipo de erro que parece pequeno no design e vira problema real de uso (cliente não percebe que algo deu errado).

---

## RNFT-D03 — Escopo de personalização por tipo de tela

**Requisito:** painel administrativo (quem opera o sistema) usa sempre a paleta padrão Aura (seção 0), nunca personalizado. Personalização de cor de marca só se aplica a superfícies expostas ao cliente final do cliente (loja online, portal do morador, portal do tutor, site da vida a dois, página pública de agendamento).

**Critério de verificação:** logar como lojista/síndico/veterinária no painel administrativo deve mostrar sempre a mesma paleta Aura, independente do tenant; acessar a loja online/portal público do mesmo tenant pode mostrar cor de marca diferente.

**Aplica-se a:** todo sistema com mais de um tipo de superfície (admin vs. público). Sistemas sem superfície pública (AM Rendara, painéis internos de serviço compartilhado) usam só a paleta padrão, sem exceção nem necessidade de suporte a tema.

---

## RNFT-D04 — Geração automática de paleta com validação de contraste

**Requisito:** o cliente nunca escolhe cor livremente digitando um código hexadecimal sem validação — ele escolhe uma cor base, e o sistema gera a paleta completa (variações de tom, texto sobre fundo) automaticamente, validando contraste mínimo WCAG AA em cada combinação antes de aplicar.

**Critério de verificação:** se a cor escolhida pelo cliente falhar no teste de contraste em qualquer combinação usada na interface, o sistema deve rejeitar ou ajustar automaticamente para a variação mais próxima que passa — nunca permitir salvar uma configuração que resulte em texto ilegível.

**Aplica-se a:** todo sistema com tema personalizável (RNFT-D03).

---

## RNFT-D05 — Validação de upload de logo

**Requisito:** upload de logo do cliente deve validar formato, resolução mínima e área de segurança (margem ao redor do logo) antes de aceitar.

**Critério de verificação:** um arquivo com resolução abaixo do mínimo ou proporção incompatível deve ser rejeitado no upload, com mensagem clara do motivo, não aceito silenciosamente para quebrar o layout depois.

**Aplica-se a:** todo sistema com superfície de marca personalizável.

---

## RNFT-D06 — Proibição de cor fixa fora do arquivo de tokens

**Requisito:** nenhuma cor pode ser escrita diretamente no código de uma tela (hardcoded) — toda cor usada na interface deve vir do arquivo central de tokens de design, sem exceção, mesmo para telas que hoje só existem no tema padrão.

**Critério de verificação:** revisão de código deve rejeitar qualquer merge que introduza valor de cor fora do arquivo de tokens — o mesmo princípio de gate automático já usado para segredo exposto em texto plano (RNFT-S05), aplicado aqui a cor.

**Aplica-se a:** todo sistema com interface visual, sem exceção. É o requisito que evita a degradação silenciosa ao longo do tempo — o risco real de verdade, mais do que qualquer erro de configuração pontual.

---

## RNFT-D07 — Teste de tela nova contra múltiplas paletas

**Requisito:** toda tela nova deve ser testada visualmente contra pelo menos duas ou três paletas de cliente diferentes (não só a paleta padrão) antes de ser considerada pronta.

**Critério de verificação:** checklist de "pronto" de qualquer tela nova inclui captura de tela com pelo menos duas cores de marca diferentes, revisando legibilidade e hierarquia visual em cada uma.

**Aplica-se a:** todo sistema com tema personalizável (RNFT-D03).

---

## Contrato técnico de tokens

Para que um sistema novo reaproveite esta arquitetura sem reconstruir nada, ele deve expor as cores de interface como variáveis (CSS custom properties ou equivalente do framework), nunca como valor fixo:

```
--aura-cor-primaria       (fixa no admin, themeable no público)
--aura-cor-primaria-texto (calculada automaticamente para contraste)
--aura-cor-semantica-erro     (sempre fixa)
--aura-cor-semantica-sucesso  (sempre fixa)
--aura-cor-semantica-alerta   (sempre fixa)
--aura-cor-semantica-info     (sempre fixa)
--aura-cor-neutro-fundo
--aura-cor-neutro-texto
```

Qualquer sistema que seguir essa nomenclatura de variável herda automaticamente a arquitetura de tema, sem trabalho de reconstrução — é o mesmo princípio de reaproveitamento por configuração que já rege o `aura-licensing`.

---

## Tabela de aplicabilidade por sistema

| Sistema | Painel admin (sempre padrão Aura) | Superfície pública themeable |
|---|---|---|
| AM Kaixara | Sim | Loja online (quando ativa) |
| AM Rotara | Sim | Não — app do cliente final reflete a marca do Delivery em si, não do lojista, mesma lógica de mercado do iFood |
| AM Rendara | Sim | Não tem superfície pública — só a paleta padrão se aplica |
| AuraVet | Sim | Portal do tutor, página pública de agendamento |
| AM Consertta | Sim | Loja online (reaproveitada da Loja Virtual) |
| Momentos/Cupido | Não se aplica no sentido tradicional | Site da Vida a Dois, Mural do Amor — aqui quem personaliza é o casal, não uma empresa |
| Loja Virtual | Sim (painel do lojista) | Catálogo/checkout público |
| AM Predara | Sim | Portal do morador |
| AM Canteira | Sim | Portal do cliente comprador |
| `aura-licensing`, `aura-goals`, `aura-historico`, `aura-analytics`, `aura-copilot` | Sem interface própria hoje — se algum vier a ter painel próprio no futuro, segue a paleta padrão Aura sem exceção | Não aplicável |

---

## Nota final sobre "perfeição"

Estes 7 requisitos reduzem o risco de qualidade de experiência a próximo de zero, mas não eliminam a necessidade de disciplina contínua — o RNFT-D06 e o D07 são processo, não configuração que se define uma vez e esquece. A garantia real não vem de nenhum requisito isolado, vem do conjunto sendo seguido em todo sistema novo, desde a primeira tela.
