# 0019 · Biblioteca e registro de leitura

- **Status:** aceita
- **Data:** 2026-11-17

## Contexto

O Alan quer que tudo o que ele lê fique registrado no setup, para que o Professor, o Recrutador, as fichas e a produção de conteúdo possam usar. Ao mesmo tempo, a regra do setup proíbe que página de livro ou texto de curso pago vá para a IA ou para o Git.

## Decisão

1. **Catálogo em `data/biblioteca.json`:** cada livro com título, autor, edição, ISBN, situação (`tenho`, `comprar`, `gratis-online`, `emprestado`) e os assuntos do [mapa de estudo](https://github.com/AlanMateus17/mapa-de-estudo) em que entra. `docs/biblioteca.md` é gerado a partir dele e conferido no `just check`.
2. **Registro no vault:** `just livros ler` acrescenta uma linha em `07-estudo-e-carreira/leituras.md` (data, livro, trecho, minutos, assunto e uma nota com as palavras dele). Nota com mais de 600 caracteres é recusada, porque costuma ser texto copiado.
3. **Comandos:** `just livros para ETAPA` (o que ler para um assunto e o que falta comprar), `just livros comprar` (na ordem em que vai precisar), `just livros lidos`, `just livros marcar LIVRO tenho`.

## Consequências

- O registro mostra minutos de leitura por livro e por assunto, que entram no "tempo real" do método de estudo.
- A ligação do registro com o Professor (trecho do livro sugerido antes da aula) fica para depois, quando os módulos do Professor usarem os números do mapa.
