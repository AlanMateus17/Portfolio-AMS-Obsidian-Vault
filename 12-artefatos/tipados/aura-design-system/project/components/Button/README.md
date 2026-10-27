# Button

Dispara uma ação; o rótulo diz exatamente o que acontece ("Emitir nota", "Salvar produto").

- **Primário** (`aura-btn aura-btn--primary`): a ação principal da tela. No máximo um por área. Fundo `aura-900`, texto `on-aura`.
- **Secundário** (`aura-btn--secondary`): ações alternativas. Fundo `surface`, borda `line`, texto `aura-900`.
- **Fantasma** (`aura-btn--ghost`): ações de menor peso, como "Cancelar".
- **Perigo** (`aura-btn--danger`): excluir ou desfazer algo irreversível; sempre com confirmação na própria tela.

Altura mínima de 40px para toque, `radius-md`, anel de foco em `gold-500`. Nas superfícies públicas o primário usa `brand-tenant` no lugar de `aura-900`, depois da checagem de contraste.

Quem usa fornece: o rótulo (verbo + objeto), o estado desabilitado quando a ação não é possível e o tratamento de carregamento.
