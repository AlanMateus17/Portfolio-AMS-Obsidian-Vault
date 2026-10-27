# Aura Design System

A identidade visual dos sistemas AM e de tudo que a Grupo AMtech Digital publica: painéis administrativos, sites, diagramas, apostilas e apresentações. Teal profundo, dourado e papel claro; bordas finas no lugar de sombras; tipografia editorial nos títulos e técnica nos dados.

## Onde se aplica

- **Painéis administrativos dos sistemas AM** (AM Kaixara, AM Rendara, AM Rotara e os demais): paleta Aura fixa, sem exceção.
- **Superfícies públicas** (loja, cardápio, página de agendamento de um cliente): mesma estrutura, mas a cor principal vem do cliente pelo token `brand-tenant`, trocado em tempo de execução pelo `MarcaThemeProvider` do aura-frontend-kit. Antes de aplicar, o utilitário de contraste confere se o texto `on-aura` continua legível; se não passar, a cor do cliente fica só em detalhes e o botão volta para `aura-900`.
- **Materiais da marca**: Instituto AMS, site da AMtech, diagramas, slides de aula e o livro Lógica e Máquina.

Estas regras resumem a série de requisitos de design RNFT-D01 a D07 do ecossistema Aura.

## Voz e conteúdo

- Português do Brasil, direto, na segunda pessoa ("você"). Frases curtas.
- Nomeie as coisas pelo que a pessoa reconhece: "Pedidos", não "OrderAggregate".
- Botão diz o que acontece: "Emitir nota", "Salvar produto". A confirmação repete o verbo: "Nota emitida".
- Erro explica o que houve e como resolver, sem pedir desculpas: "O CPF tem 11 dígitos. Confira e tente de novo."
- Números com vírgula decimal e R$ antes do valor: R$ 1.234,56.
- Nomes de produto sempre no padrão AM com maiúsculas: AM Kaixara, AM Rendara. Serviços compartilhados em minúsculas com prefixo: `aura-licensing`.

## Fundamentos visuais

**Cor.** A página é `paper`; cartões e campos são `surface` com borda `line`. Texto em `ink`, apoio em `muted`. A marca aparece em `aura-900` (ação principal, título, seleção) e o acento em `gold-500` (rótulos, linhas pontilhadas, destaque). Para texto pequeno dourado use sempre `gold-ink`: o `gold-500` não passa 4.5:1 sobre `paper`. Estados usam pares de texto e fundo: `success`/`success-tint`, `warning`/`warning-tint`, `danger`/`danger-tint`. Estado nunca é só cor: o selo também tem texto.

**Tipografia.** Fraunces nos títulos (`display`, `heading`), IBM Plex Sans no texto (`title`, `body`, `small`) e IBM Plex Mono em rótulos e dados (`eyebrow`, `code`). As três vêm do Google Fonts. Números em colunas usam algarismos tabulares.

**Espaço e forma.** Escala de 4px: `space-1` a `space-8`. Cartões com `radius-lg`, controles com `radius-md`, selos com `radius-sm`, filtros com `radius-pill`. Separação por `border-hairline` na cor `line`; a Aura não usa sombra para separar camadas.

**Foco e acessibilidade.** Todo elemento interativo mostra anel de foco de `border-focus` em `gold-500`. Texto passa 4.5:1 nos dois temas; os pares de estado foram escolhidos para isso.

**Tema escuro.** Todos os tokens de cor têm valor claro e escuro. No escuro, `aura-900` vira o teal claro e `on-aura` vira o fundo escuro, para o botão principal continuar legível.

## Iconografia

Ainda não há um conjunto de ícones definido. Até lá: rótulos em texto, setas tipográficas (→ ←) e indicadores feitos de forma simples (ponto dourado = precisa de conta; borda tracejada = futuro), como no diagrama do ecossistema.

## O que foi assumido nesta primeira versão

Esta versão foi montada a partir da paleta fixa do Aura (#0E3A45, #C08A3E, #F7F5F0), das regras de superfície pública com cor do cliente e dos artefatos já publicados (Mapa do Setup e Ecossistema AMtech). O código do aura-frontend-kit não estava disponível aqui. Ao sincronizar com ele, confira e substitua: os valores do tema escuro, a escala de tipografia e de espaçamento, e os componentes (Button, Badge e Card são uma primeira proposta).
