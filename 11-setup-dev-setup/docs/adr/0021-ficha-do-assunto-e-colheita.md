# 0021 · Ficha do assunto, diagnóstico e colheita

- **Status:** aceita
- **Data:** 2026-11-17

## Contexto

O Alan quer fazer cada coisa uma vez só: o estudo de um assunto do [mapa de estudo](https://github.com/AlanMateus17/mapa-de-estudo) precisa virar, sem retrabalho, aula da escola (repositório `ensino-ti`), trecho do livro *Lógica e Máquina*, minicurso, exercícios do AM Mentor, baralho do Anki e banco de questões. Antes, a ficha dupla do Professor, o pipeline de conteúdo e o banco de exercícios não se falavam.

## Decisão

1. **Diagnóstico registrado:** `just diag ETAPA c3 x2 c1 --min N` grava em `07-estudo-e-carreira/diagnosticos.md`. Cada resposta é certo ou errado mais a certeza (1 chute, 2 acho, 3 certeza). Acertar no chute conta como não saber; erro com certeza 3 é mandado para o caderno de erros na hora (efeito de hipercorreção, Butterfield e Metcalfe 2001). A decisão sai sozinha: modo rápido só se todas estiverem certas com certeza 2 ou 3.
2. **Uma ficha por assunto:** `just ficha ETAPA` cria `09-material-producao-simultanea/fichas/ETAPA-slug.md` no vault, com as seções Explicação, Exemplo resolvido, Exercícios (tabela Nível | Pergunta | Resposta), Aula (50 minutos: objetivo, abertura, explicação, prática, verificação), Registro de entrevista e Ideias. Ele escreve depois de estudar, sem abrir o arquivo do mapa.
3. **Colheita:** `just colher ETAPA` confere a ficha e entrega cada seção no seu destino: capítulo em `~/AMtech/entrada/capitulos/` (pipeline), exercícios em `~/AMtech/banco/exercicios/ETAPA.yaml` e `~/AMtech/banco/anki/ETAPA.tsv`, plano de aula em `ensino-ti/<componente>/planos-de-aula/` de cada componente ligado à etapa, e ideias em `~/AMtech/entrada/ideias/`. Destinos já existentes e diferentes não são reescritos sem `--forcar`; `--seco` mostra o que faria.
4. **O mapa das ligações em `data/aulas.json`:** etapa → título, módulo do Professor e componentes do `ensino-ti`; seção da ficha → ofertas do `portfolio.json`.
5. **Professor:** em módulo ligado a uma etapa, `just professor fechar` aponta para a ficha do assunto em vez de criar a ficha dupla.

## Consequências

- Cada etapa nova do mapa só precisa de uma entrada em `data/aulas.json`.
- A seção Aula vai para um repositório público: a ficha nunca leva nome, nota ou dado de aluno.
- O plano de aula sai no formato do setup; adaptar ao modelo oficial da escola continua manual (a Fábrica de documentos é o próximo passo).
