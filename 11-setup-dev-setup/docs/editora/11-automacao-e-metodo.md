# 11 · Automação e método

[← Editora](README.md)

## O seu método dentro do pipeline

Você vai implementar o passo a passo de criação que segue o modelo do VHSlins. Ele entra assim:

1. Cada etapa vira um item em `modelo/metodo.yaml`: nome, o que entra, o que sai e como saber que terminou.
2. O pipeline lê esse arquivo e mostra, para cada capítulo, em que etapa ele está.
3. Uma etapa só é marcada como concluída quando o critério dela passa (por exemplo, "todos os exercícios com solução").
4. As etapas que podem ser automáticas ganham um script; as que dependem de você ficam como tarefa no painel.

Use o método como processo de trabalho. O texto, os exemplos e os exercícios são seus; nada dos livros dele é copiado.

## O que é automático e o que fica com você

| Etapa | Automático | Você |
|---|---|---|
| Esqueleto do capítulo a partir do modelo | Sim | — |
| Texto, explicações e voz | Rascunhos e sugestões dos agentes | **Escreve e decide** |
| Mapa de pré-requisitos | Sim: avisa conceito usado antes de ensinado | Corrige a ordem |
| Exercícios | Sugestões de exercícios no estilo das bancas; verificação dos gabaritos | **Escolhe e escreve as soluções** |
| Questões reais de concurso | Busca e organização por banca, órgão e ano | Confere |
| Código dos exemplos | Testes gerados e executados a cada build | Revisa |
| Figuras técnicas | Geradas por script a cada build | Define o que mostrar |
| Tabelas-verdade, conversões, tabelas de operações | Geradas e conferidas por script | — |
| Busca de imagens | Busca, filtro de licença e resolução, folha de contato | **Escolhe** |
| Créditos e legendas | Gerados a partir das fichas | — |
| Ortografia, estilo e links | Sim | Aceita ou recusa |
| Matriz de editais | Cobertura calculada | Inclui editais novos |
| Diagramação (PDF, EPUB, impressão) | Sim | Aprova a prova |
| Sumário, índice remissivo, glossário | Sim | — |
| Leitura de prova pelos agentes (leitor iniciante, revisor técnico) | Sim | Decide o que mudar |
| Leitores beta e revisor técnico humano | Convites e formulário automáticos | **Lê o retorno** |
| Errata e changelog | Gerados a partir das correções | — |
| Exercícios no site am-mentor e Anki | Gerados do YAML | — |
| Aulas do curso | Roteiro sugerido por seção; narração com a voz clonada | **Grava a tela, aprova** |
| Divulgação | Cortes, posts e e-mails na esteira de marketing | Aprova |

Tudo o que é escrita, escolha e aprovação continua com você. É isso que faz o livro ter a sua voz e o seu nome.

## Exemplo funcionando

`tools/editora/tabela_verdade.py` gera a tabela-verdade de qualquer proposição (em LaTeX e Markdown) e é testado no CI do repositório. É o tipo de figura do Capítulo 1 que nunca precisa ser feita à mão:

```bash
python tools/editora/tabela_verdade.py "(p -> q) <-> (~q -> ~p)"
```
