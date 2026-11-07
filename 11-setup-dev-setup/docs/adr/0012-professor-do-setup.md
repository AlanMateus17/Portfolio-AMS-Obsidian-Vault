# 0012 · Professor do setup: aula, prática, prova e revisão espaçada

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O Alan quer que o setup seja o professor mais qualificado possível em tudo o que ele precisa dominar para operar o próprio setup e subir no eixo (ADR 0011): teoria, prática, método e acompanhamento. Até aqui o setup tinha peças soltas (Anki, base de notas, NotebookLM, Escola Akita, plano de estudos no vault), mas nenhum professor: ninguém dizia o que estudar hoje, ensinava, cobrava prova e trazia de volta na hora de revisar.

## Decisão

1. **Currículo como dado:** `data/professor/curriculo.json` traz os módulos com trilha (ofício, operar o setup, finanças), trimestre, objetivos verificáveis, pré-requisitos, prática no setup e fontes oficiais. Começa com os 19 módulos do trimestre 1 e cresce a cada trimestre.
2. **O método fixo de cada aula:** objetivo único; perguntas diagnósticas antes da explicação; três blocos de 25 minutos (intuição, modelo, detalhes e erros); exemplo resolvido seguido de exemplo com lacunas; prática no setup dele com critério de pronto; perguntas de recuperação; cartões; fontes oficiais. São as técnicas com mais evidência em aprendizagem (prática de recuperação, espaçamento, exemplos resolvidos com retirada gradual de apoio, intercalação entre trilhas), e os blocos curtos com objetivo único funcionam melhor com TDAH.
3. **Domínio medido de 0 a 4** (nada, viu a aula, fez a prática, passou na prova, ensinou), guardado no núcleo. A prova é discursiva, corrigida com rubrica, e aprova a partir de 80. A revisão espaçada segue 1, 3, 7, 21, 60 e 120 dias; reprovar volta para 1 dia. Um módulo só abre quando os pré-requisitos passaram na prova.
4. **Token econômico:** a aula é gerada uma vez e fica no Obsidian; reler é grátis. O Claude escreve e corrige (é o melhor professor disponível); o Ollama é a opção grátis, mais fraca para ensinar.
5. **Contexto real:** cada aula recebe o resumo do setup e o que o núcleo já sabe sobre o assunto (ADRs, regras do Akita aprovadas, lições), para ensinar o setup dele, não um genérico.
6. **Exceção ao congelamento do ADR 0011:** o Professor não abre área nova; ele serve ao eixo e à operação do que já existe.
7. **O método junta a ciência e os planos do Alan** (docs/professor/metodo.md): o Protocolo de fim de bloco, a mesma ideia de 4 jeitos, a ficha dupla e o registro de entrevista (do metodo-de-estudo.md do vault), os exercícios N1 a N4 e o gabarito comentado (da arquitetura do livro Lógica e Máquina), os quadros das apostilas dele, a regra 20/80 e uma porta só (`just professor hoje`). A correção guarda os pontos fracos para a prática deliberada, e o `fechar` guarda o tempo real contra o estimado.

## Limites (ditos com franqueza)

- IA erra. Toda aula aponta a fonte oficial, e a prática no setup é a prova real: se o comando não funciona, a aula estava errada.
- O Professor não substitui revisão de gente mais experiente (PR em open source, mentor, comunidade) nem cliente de verdade. Ele prepara para isso.
- Quem estuda é você: o setup pode ensinar, cobrar e lembrar, mas não aprende por você.
