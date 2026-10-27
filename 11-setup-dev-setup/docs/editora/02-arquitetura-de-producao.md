# 2 · Arquitetura de produção

[← Editora](README.md)

## O livro como repositório

Um repositório por livro na organização da editora (ex.: `editora-ams-silva/logica-e-maquina`).

```
capitulos/
  v1a/01-proposicao/
    texto.md            teoria, exemplos e pranchas (Markdown com extensões)
    exercicios.yaml     enunciado, nível, fonte, gabarito, solução, habilidade
    codigo/             exemplos em C#, TypeScript, Python, C (com testes)
    figuras/            TikZ, SVG, Mermaid (fonte, nunca só a imagem)
modelo/                 o seu modelo de criação: template de capítulo e regras
estilo/
  livro.cls             classe LaTeX com a identidade visual
  epub.css              estilo do ebook
  vale/                 regras de estilo de escrita
referencias.bib         bibliografia
glossario.yaml          termos e definições (geram o glossário e o índice)
errata.md               correções públicas por edição
CHANGELOG.md            o que mudou em cada edição
```

## Uma fonte, várias saídas

| Ferramenta | Papel |
|---|---|
| **Markdown + Pandoc** (ou Quarto) | Converte a fonte única em LaTeX, EPUB e HTML |
| **LaTeX (TeX Live, já no setup)** | PDF de leitura e PDF de impressão com sangria, marcas de corte e fontes embutidas |
| **TikZ e SVG** | Pranchas técnicas e diagramas vetoriais, versionados como código |
| **YAML de exercícios** | Gera a lista do capítulo, o gabarito no fim do volume, o site am-mentor e os baralhos Anki, todos a partir do mesmo arquivo |
| **GitHub Actions** | Compila tudo a cada mudança e publica os arquivos de cada versão |
| **Imagens e figuras** | Busca em acervos com filtro de licença e figuras geradas por código: ver [Imagens e figuras](10-imagens-e-figuras.md) |

## O que o pipeline confere a cada mudança

1. **Código:** todo exemplo é compilado e testado. Se o livro diz que um programa imprime "42", o teste confere.
2. **Gabaritos:** exercícios com resposta calculável têm o gabarito verificado por script.
3. **Texto:** ortografia (LanguageTool) e estilo (Vale) com as regras da editora.
4. **Referências:** cada citação existe na bibliografia; cada figura e exercício referenciado existe.
5. **Links:** URLs do livro e do site respondem.
6. **Impressão:** fontes embutidas, imagens com resolução de impressão, margens e sangria dentro da especificação da gráfica.

O resultado é um selo no repositório (build verde) e os arquivos prontos para cada canal.

## Onde roda

- Escrita no Obsidian ou no VS Code, dentro do WSL, como o resto do setup.
- Compilação local com TeX Live e no GitHub Actions.
- Arquivos finais guardados no GitHub (releases) e no backup 3-2-1.
- Agentes do Claude Code ajudam a revisar exercícios, gerar testes do código e conferir consistência entre capítulos, sempre com revisão sua.

## Agentes da editora

| Agente | O que faz |
|---|---|
| `revisor-tecnico` | Confere definições, notação e exemplos contra o glossário e as referências |
| `gerador-de-testes` | Escreve testes para os exemplos de código de cada capítulo |
| `verificador-de-gabarito` | Resolve cada exercício por conta própria e aponta divergências com o gabarito |
| `leitor-iniciante` | Lê como um aluno do ensino médio e marca onde o texto pula um passo |
| `consistencia` | Procura termos, símbolos e nomes usados de jeitos diferentes entre capítulos |

Eles apontam problemas; quem decide e escreve é você.
