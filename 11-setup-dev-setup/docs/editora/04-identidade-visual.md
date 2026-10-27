# 4 · Identidade visual e referências

[← Editora](README.md)

## Duas identidades, de propósito

| | Editora AMS Silva | Livro Lógica e Máquina |
|---|---|---|
| Papel | Marca da editora (logo, site, lombada) | Miolo e capa de cada livro |
| Visual | A definir no Design System da editora | Papel creme, tinta escura, verdigris e latão; Cormorant Garamond, EB Garamond, IBM Plex Mono |
| Onde fica | Artefato Design System + `estilo/` de cada livro | `estilo/livro.cls` e `estilo/epub.css` |

O site am-mentor tem paleta própria (azul-marinho, dourado, rosa, azul-aço). Vale decidir se ele adota a identidade do livro ou se continua diferente de propósito.

## Sistema visual do livro

- **Grade e tipografia:** tamanhos de página, margens e escala de títulos definidos uma vez na classe LaTeX.
- **Pranchas técnicas numeradas:** código e diagramas com moldura, numeração por capítulo e legenda.
- **Caixas com função fixa:** Definição, Exemplo, Contraexemplo, Atenção, História, Na prática (sistema real). Cada uma com a mesma forma em todo o livro.
- **Abertura de parte:** como o retrato de matemático do VHSlins, uma figura histórica da computação ou da matemática, com uma linha sobre ela.
- **Cores com significado:** verdigris para teoria, latão para prática; nunca como enfeite.

## Quadro de referências

Um quadro (Whiteboard ou artefato Design) com:
- livros de referência pelo design (didáticos clássicos, manuais técnicos, livros de arte e tipografia);
- exemplos de pranchas, caixas e aberturas de capítulo;
- paletas e tipos testados em impressão real (imprima uma página antes de decidir).

## Imagens de IA

- **Podem:** rascunhos de ideia, ilustrações de conceito e texturas, sempre revisadas e retocadas.
- **Não podem:** substituir diagramas técnicos (esses são feitos em TikZ ou SVG, para estarem corretos) nem imitar o estilo de um artista vivo.
- **Licença:** confira os termos de uso comercial da ferramenta antes de imprimir.
- **Retratos históricos:** prefira obras em domínio público ou gravuras próprias.

## O seu modelo de criação

Quando você enviar o modelo, ele vira:
1. o template de capítulo em `modelo/`;
2. regras automáticas no pipeline (seções obrigatórias, ordem, tipos de caixa);
3. o checklist do documento de rigor.
