# 2 · Perfil sênior: erros, regras e formulário de pedido

[← Motor de decisão](README.md) · Versão editável: [Plano de Perfil Sênior](https://claude.ai/artifact/NH2Y9FNG9L7FvWkZcn9cVi)

O maior gasto de tokens não vem do modelo nem do prompt mal escrito. Vem de pedir escopo infinito e de replanejar mais do que executar.

## Os 7 erros recorrentes

| # | Erro | Evidência |
|---|---|---|
| 1 | Escopo absoluto ("tudo", "100%", "sem deixar nada de fora") | 108+ frentes, 23 camadas, 129 contas, 396+ passos, 40 versões em 8 dias |
| 2 | Planejar no lugar de executar | Repositório é a planta, não a casa; nenhuma oferta paga lançada |
| 3 | Mudar a direção depois de decidida | Stack fixa e depois liberada; nomes Aura* → AM*; SO pausado e replanejado |
| 4 | Pedido sem entregável, formato e critério | "Faltaram as teóricas", gabarito em aba e depois em arquivo |
| 5 | Perguntar "está tudo 100% conectado?" | Auditorias repetidas do repositório inteiro |
| 6 | Conversas gigantes de vários dias | Só continuam graças ao CONTINUAR.md |
| 7 | Premissa não verificada | "Vi que lançaram um sistema operacional" |

Manter: exigir prova (CI, git status), pedir honestidade, regras de dinheiro e horas, validar antes de construir, CONTINUAR.md.

## As 10 regras

1. Um pedido, um entregável.
2. Escopo com número ("as 3 primeiras", "versão 0.1").
3. Planejar e adicionar camadas é livre; na execução, terminar o que começou antes de pular para a próxima.
4. Decisão tomada fica tomada por 30 dias; mudar antes só com ADR.
5. Critério de pronto escrito no pedido.
6. Verificação pontual ("a fase 6 passa no `just verificar`?"), não geral.
7. Conversa nova por tarefa, aberta com o CONTINUAR.md ou um resumo de 5 linhas.
8. Fonte junto da premissa (mandar o link).
9. Modelo e lugar certos (skill `arquiteto-de-prompt`).
10. Toda semana, pelo menos uma tarefa aproxima uma oferta paga da venda.

## Formulário de pedido

```markdown
TAREFA*: [um verbo + um entregável]
PARA QUE*: [o resultado real]
ENTREGÁVEL*: [formato e onde fica]
ESCOPO*: [limite com número]
FORA DO ESCOPO: [o que NÃO fazer agora]
CONTEXTO: [arquivo, repositório ou link]
RESTRIÇÕES: [stack, prazo, custo, regras]
PRONTO QUANDO*: [critério verificável]
PREMISSA/FONTE: [link, se houver]
MODO: [perguntar antes | decidir e me avisar]
```

Se não dá para preencher PRONTO QUANDO, a tarefa não está madura: o pedido certo é "me ajude a definir o critério de pronto de X".

## O que o setup preenche e o que é do Alan

| Quem | Campos ou funções |
|---|---|
| Setup sozinho | CONTEXTO (ripgrep, CONTINUAR.md, ESTADO.md, memória), RESTRIÇÕES (regras já registradas), FORA DO ESCOPO (limite de 3 frentes "agora" na execução), ENTREGÁVEL (padrão por tipo), PREMISSA (pesquisa), MODELO e LUGAR (roteador) |
| Setup sugere, Alan confirma com "ok" | ESCOPO, PRONTO QUANDO, PARA QUE |
| Só o Alan | Decidir o que importa e quando parar; aprovar o que é público, gasta dinheiro ou fala com cliente; testar no mundo real; vender; julgar o resultado; trazer o conhecimento local que torna o resultado único |

Fluxo: o Alan escreve do jeito dele → o setup monta o formulário e mostra só os campos que adivinhou (3 a 4 linhas) → "ok" ou correção → execução.

## Skill `arquiteto-de-prompt`

Proposta em 11/11/2026: especificação profissional → no máximo 3 perguntas → onde rodar e com qual modelo → prompt pronto (parte fixa primeiro, para cache) → execução → lista do que o especialista acrescentou e o que o Alan deve conferir. Próxima melhoria proposta: preencher o formulário sozinha e pedir só confirmação.

## Plano de 30 dias (11/11 a 11/12/2026)

- **Semana 1:** salvar a skill e usar o formulário; registrar as frentes novas (todas ativas, nada congelado); escolher UMA oferta para ser a primeira na ordem de execução (site para pequeno negócio, minicurso de Lógica ou planilha AM Rendara).
- **Semana 2:** `just instalar` e só as fases que a oferta usa; critério de pronto em uma linha.
- **Semana 3:** versão 0.1 vendável; uma conversa por tarefa.
- **Semana 4:** à venda, mostrada a 10 pessoas do público certo; revisão (mudanças de decisão, uso do formulário, renda).

Sinal de sucesso: menos mensagens por tarefa, nenhum "está tudo 100%?", link de venda no ar até 11/12.
