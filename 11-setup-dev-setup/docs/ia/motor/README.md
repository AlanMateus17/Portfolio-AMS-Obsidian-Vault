# Motor de decisão e custo mínimo de IA

[← Arquitetura de IA](../README.md) · Decisão registrada no [ADR 0014](../../adr/0014-motor-de-decisao-e-custo-minimo.md)

Planejado na conversa de 11/11/2026. O objetivo: o Alan continua escrevendo do jeito dele, e o setup decide sozinho **quem** faz cada pedido (ferramenta pronta, código, automação, IA local, IA online ou o próprio Alan), gastando o mínimo e com a mesma régua de qualidade em programação, sistemas, empreendedorismo e finanças.

Regra-mãe: **a IA propõe, o código decide e verifica.**

## Arquivos de contexto

| # | Arquivo | O que guarda |
|---|---|---|
| 1 | [01-modelos-e-api.md](01-modelos-e-api.md) | Fable 5.2 e os outros modelos, chat x API, técnicas de economia de tokens |
| 2 | [02-perfil-senior-e-formulario.md](02-perfil-senior-e-formulario.md) | Os 7 erros recorrentes, as 10 regras, o formulário de pedido, o que é automático e o que é manual, plano de 30 dias |
| 3 | [03-escada-e-roteador.md](03-escada-e-roteador.md) | A escada de 5 degraus, o que é determinístico, o roteador local, o papel de cada ferramenta |
| 4 | [04-regra-de-tres.md](04-regra-de-tres.md) | Tarefa repetida 3 vezes vira cache, template ou script |
| 5 | [05-qualidade-e-seguranca.md](05-qualidade-e-seguranca.md) | As 6 peças anti-erro, as 7 lacunas de sênior e as técnicas para cada uma |
| 6 | [06-engenharia-reversa-e-ferramentas.md](06-engenharia-reversa-e-ferramentas.md) | Dissecação em 4 níveis, construir x usar, as 3 camadas, Hugging Face |
| 7 | [07-nuvem-barata.md](07-nuvem-barata.md) | O que vai para a nuvem, fase 0 grátis e fase 1 paga |

Documento complementar (Claude Docs): [Plano de Perfil Sênior](https://claude.ai/artifact/NH2Y9FNG9L7FvWkZcn9cVi). Skill proposta no chat: `arquiteto-de-prompt` (confirmar se foi salva).

## Versão 0.1: pronta (v2.27, 11/11/2026)

| Comando | O que faz |
|---|---|
| `just motor "pedido"` | Desce a escada sem chamar IA: degrau, destino, motivo, aviso de dado sensível e o formulário pré-preenchido |
| `just motor-custo claude sonnet --entrada N --saida N --usd X --decisao ID` | Registra o gasto de uma chamada de IA |
| `just motor-ok ID` / `just motor-refazer ID` | Diz se a decisão deu certo (alimenta a regra de três) |
| `just motor-relatorio` | Decisões por degrau, gasto por ferramenta e pedidos de IA aprovados 3+ vezes |

- **Escada:** `tools/motor/motor.py`, com as regras em `data/motor/regras.json` (palavras por degrau, modelos, tipos, entregáveis, padrões de dado sensível). Mudar uma regra é editar o JSON.
- **Catálogo:** as rotas de `data/recursos.json` e os blocos de `data/ecossistema.json` (degrau 1).
- **Registro:** eventos `motor.decisao`, `motor.custo` e `motor.resultado` no Núcleo AMtech (precisa de `nucleo.py iniciar`; sem banco, a decisão funciona igual e só não é registrada).
- O `just triagem` continua para "montar, colar ou construir" dentro do degrau 1 a 3.

## Próximos passos

1. Rodar no notebook: `python3 tools/nucleo/nucleo.py iniciar` e usar `just motor` antes de cada tarefa.
2. Preenchimento automático do formulário pelo modelo local (Ollama), regra de três gerando o script, guardas de segurança no CI, nuvem.
3. Depois de 2 a 3 semanas de uso: ajustar as palavras de `data/motor/regras.json` pelo que o relatório mostrar.

## Ordem original

1. **Escada** (estender o `just triagem` atual, sem criar ferramenta nova).
2. **Catálogo único de capacidades** (evoluir `data/recursos.json`).
3. **Registro de cada decisão e custo** (no Núcleo AMtech).
4. Em seguida: preenchimento automático do formulário pelo modelo local, regra de três, guardas de segurança no CI, nuvem.

## Pendências (decisão do Alan)

- [x] **Calendário (decidido em 11/11/2026):** nada fica congelado. O motor e as frentes novas entram agora; a execução segue a ordem do roteiro e o limite de 3 frentes "agora".
- [x] Skill `arquiteto-de-prompt` salva na conta.
- [x] Linguagem do roteador: Python, como o resto de `tools/`.
