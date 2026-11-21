# 0020 · Caderno de erros e atritos do setup

- **Status:** aceita
- **Data:** 2026-11-17

## Contexto

Errar nos exercícios e esbarrar em passos manuais do setup são as duas fontes de melhoria mais baratas, mas só servem se forem anotadas na hora, sem abrir arquivo.

## Decisão

1. `just erro ASSUNTO "o erro" --certo "o certo"` acrescenta uma linha em `07-estudo-e-carreira/caderno-de-erros.md`, no vault. O "certo" vira cartão do Anki.
2. `just atrito "o que aconteceu" --area AREA` acrescenta uma linha em `06-execucao-e-desenvolvimento/atritos-do-setup.md`. `just atritos` agrupa e marca o que apareceu 3 vezes ou mais, que pela regra do setup vira script ou automação.
3. Textos com mais de 400 caracteres são recusados: uma linha, com as palavras dele.

## Consequências

- Um arquivo só para cada registro, gerado pelo comando; ele nunca precisa abrir esses arquivos para anotar.
- O arquivo desta decisão foi escrito depois da v2.33.0, que já citava "ADR 0020" sem o arquivo existir.
