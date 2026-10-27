# 12 Projetos da Formação — especificações

Sep 28, 2026 · @Alan Mateus

Doze projetos levam o aluno do primeiro programa a um sistema completo no ar, cada um inspirado num sistema real do portfólio Aura. O aluno recebe a especificação e o resultado esperado; o código ele escreve do zero.

## Como os projetos funcionam

O aluno recebe tudo o que precisa para construir, menos o código. Cada projeto traz o mesmo pacote, e a avaliação é a mesma em todos.

| O aluno recebe | O aluno não recebe |
| --- | --- |
| O problema do cliente, contado como história | Código-fonte, repositório pronto ou esqueleto do projeto |
| Requisitos numerados (RF) e regras de negócio (RN) | Passo a passo de código ("crie o arquivo X e escreva Y") |
| Casos de teste: a entrada e a saída esperada | A solução dos casos de teste |
| Critérios de aceite (o que precisa funcionar para passar) | Um site de demonstração navegável, porque o código do front-end ficaria visível no navegador |
| Vídeo e imagens do resultado esperado, feitos pelo professor |  |
| Marcos (o que deve funcionar em cada parada) e perguntas-guia |  |
| Links para os módulos da Documentação que o projeto usa |  |

**Entrega de todo projeto**

- Repositório no GitHub, com commits ao longo do trabalho (não um commit só no fim).
- README com o que o projeto faz, como rodar, as decisões tomadas e o que ficou de fora.
- Link publicado (projetos com front-end) ou coleção de requisições (APIs).
- Vídeo de até 2 minutos mostrando os critérios de aceite funcionando.

**Avaliação (a mesma rubrica nos 12)**

| Critério | Peso | Como se mede |
| --- | --- | --- |
| Funciona como pedido | 50% | Cada critério de aceite e cada caso de teste conferidos |
| Qualidade do código | 20% | Nomes claros, funções pequenas, sem repetição, sem código morto |
| Documentação | 15% | README completo e histórico de commits com mensagens que dizem o que mudou |
| Explicação | 15% | O aluno explica, em até 5 minutos, qualquer trecho que o professor apontar |

**IA nos projetos:** vale o guia "Usar IA do jeito certo". Pode explicar erros, conceitos e revisar o código pronto. Não pode gerar o projeto nem partes inteiras dele. A explicação oral é o que garante isso: quem não sabe explicar o próprio código não passa.

## Mapa dos 12 projetos

Um projeto por mês, na ordem das etapas do roteiro da Documentação. Cada um usa o que os anteriores ensinaram, e o 12 junta tudo.

| # | Projeto | Inspirado em | Etapa | Módulos | Tecnologias | Duração | Formato |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Caixa Rápido | AM Kaixara (PDV) | 1 | 1 | JavaScript puro | 2 a 3 semanas | Individual |
| 2 | Linha do Tempo | AM Vynla (histórias e linha do tempo) | 2 | 2 | HTML, CSS, GitHub Pages | 2 a 3 semanas | Individual |
| 3 | Portfólio pessoal | Seu site pessoal | 2 | 2, 3 | HTML, CSS, JavaScript | 3 a 4 semanas | Individual |
| 4 | Quadro Kanban | AM Taskoro (gestão de projetos) | 2 | 2 | JavaScript, DOM, localStorage | 3 a 4 semanas | Individual |
| 5 | Finanças em dupla | AM Rendara (finanças e rebalanceamento) | 3 | 3 | JavaScript, CSV, Git em equipe | 4 semanas | Dupla |
| 6 | Agenda com API | AM Horaria (agendamentos) | 3 | 4 | fetch, HTTP, API falsa (json-server) | 3 a 4 semanas | Individual |
| 7 | Loja virtual | AM Vendra (e-commerce) | 4 | 5, 6 | TypeScript, React, Next.js, Tailwind, Zustand | 5 a 6 semanas | Individual |
| 8 | Ordens de serviço | AM Consertta (assistência técnica) | 5 | 7, 8 | C#, POO, LINQ, JSON | 4 a 5 semanas | Individual |
| 9 | Banco do PDV | AM Kaixara (PDV) | 6 | 10 | SQL, PostgreSQL, Docker Compose | 4 semanas | Individual |
| 10 | API da clínica veterinária | AM Petara (veterinária) | 7 | 9, 10, 12 | ASP.NET Core, EF Core, JWT, PostgreSQL | 6 a 8 semanas | Individual |
| 11 | Reservas com TDD | AM Predara (condomínios) | 8 | 14 | xUnit, testes de integração, Playwright | 4 a 5 semanas | Individual |
| 12 | Sistema completo (1 de 3) | AM Kaixara, AM Rotara ou AM Mentor | 9 | Todos | A stack inteira, Docker, GitHub Actions, deploy | 8 a 12 semanas | Individual ou dupla |

Os projetos 1 a 6 fecham o nível aluno. Os projetos 7 a 12 formam o portfólio para a primeira vaga: um front-end moderno, um back-end em C#, um banco modelado, uma API com login, testes e um sistema completo no ar.

## Projeto 1 — Caixa Rápido

**Inspirado no AM Kaixara (PDV).** Etapa 1 · Módulo 1 (Lógica) · JavaScript puro · 2 a 3 semanas · individual.

**O problema:** a padaria do bairro fecha as vendas numa calculadora e erra o troco no fim do dia. O dono quer um programa que some a venda, aplique o desconto certo e diga exatamente quais cédulas e moedas devolver.

**Requisitos**

1. RF01 — Adicionar item: nome, preço unitário e quantidade.
2. RF02 — Remover item e alterar a quantidade.
3. RF03 — Mostrar subtotal, desconto e total a qualquer momento.
4. RF04 — Finalizar com dinheiro, Pix ou cartão.
5. RF05 — No dinheiro, mostrar o troco separado por cédulas e moedas.
6. RF06 — Emitir um recibo em texto com itens, totais e forma de pagamento.

**Regras de negócio**

- RN01 — Desconto de 5% no subtotal acima de R$ 100,00 e de 10% acima de R$ 200,00 (acima = maior que, não igual).
- RN02 — Todo valor é guardado em centavos, como número inteiro. Nenhuma conta usa número com vírgula.
- RN03 — Troco com o menor número de peças: R$ 100, 50, 20, 10, 5, 2, 1 e 0,50, 0,25, 0,10, 0,05, 0,01.
- RN04 — Cartão em até 3 vezes sem juros, só para total acima de R$ 60,00. Os centavos que sobram da divisão vão na primeira parcela.
- RN05 — Quantidade e preço precisam ser maiores que zero. Venda sem itens não finaliza.

**Resultado esperado: casos de teste**

| # | Entrada | Saída esperada |
| --- | --- | --- |
| 1 | 2 × R$ 12,50 e 1 × R$ 80,00; dinheiro R$ 100,00 | Subtotal R$ 105,00 · desconto R$ 5,25 · total R$ 99,75 · troco R$ 0,25 = 1 moeda de 0,25 |
| 2 | Itens somando R$ 250,00; dinheiro R$ 300,00 | Desconto R$ 25,00 · total R$ 225,00 · troco R$ 75,00 = 1 × 50 + 1 × 20 + 1 × 5 |
| 3 | Subtotal R$ 100,00; cartão em 3 vezes | Sem desconto · parcelas R$ 33,34 + R$ 33,33 + R$ 33,33 |
| 4 | Total R$ 45,90; cartão em 2 vezes | Recusado: "Parcelamento só acima de R$ 60,00" |
| 5 | Total R$ 99,75; dinheiro R$ 90,00 | Recusado: "Faltam R$ 9,75" |
| 6 | Nenhum item; finalizar | Recusado: "Adicione pelo menos um item" |
| 7 | Preço 0 ou quantidade -1 | Item não entra, com a mensagem do erro |

**Critérios de aceite**

- [ ] Os 7 casos de teste dão exatamente a saída da tabela.
- [ ] Nenhuma conta de dinheiro usa números com vírgula (RN02).
- [ ] Cada regra está numa função própria, com nome que diz o que ela faz.
- [ ] O recibo mostra itens, subtotal, desconto, total, forma de pagamento e troco ou parcelas.

**Marcos**

1. As funções de cálculo funcionam no Console, chamadas à mão.
2. A venda guarda uma lista de itens e recalcula os totais a cada mudança.
3. As três formas de pagamento funcionam, com os erros tratados.
4. Uma página simples com formulário usa as mesmas funções e mostra o recibo.

**Perguntas-guia**

- Por que 0,1 + 0,2 não dá 0,3 no JavaScript, e como os centavos resolvem isso?
- O troco com o menor número de peças: qual peça você tenta primeiro, e até quando?
- Quais funções só calculam e quais mostram coisas na tela? Por que separar as duas?

**Desafio extra:** o caixa começa o dia com uma quantidade limitada de cada cédula e moeda. O troco passa a respeitar o que existe no caixa e avisa quando não há troco possível.

## Projeto 2 — Linha do Tempo

**Inspirado no AM Vynla (histórias e linha do tempo).** Etapa 2 · Módulo 2 (HTML e CSS) · HTML, CSS, GitHub Pages · 2 a 3 semanas · individual.

**O problema:** o museu da cidade quer contar a história de Barbacena (ou de uma família, de um time, de uma escola: o aluno escolhe) numa página que funcione bem no celular, porque é pelo celular que os visitantes vão abrir, lendo um QR Code na entrada.

**Requisitos**

1. RF01 — Pelo menos 10 acontecimentos, cada um com data, título, texto curto e foto.
2. RF02 — Um menu que leva a cada período (décadas ou fases) pela âncora.
3. RF03 — No celular, a linha do tempo é uma coluna com a linha à esquerda; no computador, os acontecimentos alternam de lado.
4. RF04 — Um acontecimento em destaque, visualmente diferente dos outros.
5. RF05 — Rodapé com as fontes de cada informação e de cada foto.
6. RF06 — Publicada no GitHub Pages, com o link e a imagem aparecendo certos ao compartilhar no WhatsApp.

**Regras de negócio**

- RN01 — Só HTML e CSS. Nenhuma linha de JavaScript.
- RN02 — HTML semântico: a linha do tempo é uma lista ordenada, cada acontecimento um artigo, cada data uma tag de data com o valor que as máquinas leem.
- RN03 — Cada foto com texto alternativo, largura e altura, e no máximo 300 KB.
- RN04 — Cores e espaços em variáveis CSS. Nenhuma cor repetida fora delas.

**Critérios de aceite (resultado esperado)**

- [ ] O validador do W3C não mostra nenhum erro.
- [ ] Lighthouse: Acessibilidade 90 ou mais e Desempenho 90 ou mais, no modo celular.
- [ ] Em 360 px de largura não existe rolagem para o lado; em 1280 px os itens alternam de lado.
- [ ] Navegando só com Tab, o foco aparece em todo link do menu.
- [ ] O Verificador do projeto não mostra nenhum item vermelho.
- [ ] O link compartilhado mostra título, descrição e imagem.

**Marcos**

1. O conteúdo inteiro escrito em HTML puro, sem CSS, lido de cima a baixo como um documento.
2. A versão de celular pronta (coluna única, linha à esquerda).
3. A versão de computador com `@media` (itens alternados).
4. Fotos otimizadas, metadados de compartilhamento e publicação.

**Perguntas-guia**

- Se o CSS não carregar, a página ainda faz sentido? O que isso diz sobre o seu HTML?
- A linha vertical é conteúdo ou decoração? Onde ela deve ser desenhada, no HTML ou no CSS?
- Qual seletor escolhe "um item sim, outro não" sem colocar uma classe em cada um?

**Desafio extra:** uma versão para impressão (`@media print`) em uma coluna, sem menu, com o endereço de cada fonte escrito ao lado do link.

## Projeto 3 — Portfólio pessoal

**Inspirado no seu site pessoal (alanmateus17.github.io).** Etapa 2 · Módulos 2 e 3 · HTML, CSS, JavaScript · 3 a 4 semanas · individual.

**O problema:** o aluno vai precisar mostrar o que sabe fazer. Um recrutador gasta menos de um minuto num portfólio: precisa ver quem é a pessoa, os projetos e como falar com ela, sem procurar.

**Requisitos**

1. RF01 — Seções: apresentação, projetos, habilidades, contato.
2. RF02 — Os cards de projeto são montados pelo JavaScript a partir de uma lista de objetos (nome, descrição, tecnologias, imagem, link do site, link do repositório).
3. RF03 — Filtro por tecnologia: clicar em "CSS" mostra só os projetos que usam CSS; dá para combinar dois filtros.
4. RF04 — Clicar num card abre uma janela com os detalhes do projeto.
5. RF05 — Formulário de contato com validação (nome, e-mail, mensagem de 20 a 500 caracteres) e mensagem de confirmação.
6. RF06 — Tema claro e escuro, lembrado na próxima visita.

**Regras de negócio**

- RN01 — Acrescentar um projeto novo = acrescentar um objeto na lista. Nenhum HTML muda.
- RN02 — Com dois filtros ligados, aparecem os projetos que têm as duas tecnologias.
- RN03 — A janela fecha com Esc, com o botão fechar e clicando fora dela; ao fechar, o foco volta ao card.
- RN04 — Nenhum filtro ligado = todos os projetos. Nenhum resultado = mensagem "Nenhum projeto com essas tecnologias".

**Resultado esperado: casos de teste**

| # | Ação | Resultado esperado |
| --- | --- | --- |
| 1 | Acrescentar um objeto na lista e recarregar | Um card novo aparece, com a imagem e os links |
| 2 | Ligar "CSS" e depois "JavaScript" | Só os projetos que têm as duas |
| 3 | Ligar um filtro que nenhum projeto tem | A mensagem de nenhum resultado |
| 4 | Abrir um card e apertar Esc | A janela fecha e o foco volta ao card |
| 5 | Enviar o formulário com e-mail "ana@" | O erro aparece junto do campo, e nada é enviado |
| 6 | Ligar o tema escuro e recarregar | Continua escuro |

**Critérios de aceite**

- [ ] Os 6 casos de teste funcionam.
- [ ] Tudo é usável só com o teclado.
- [ ] Lighthouse 90 ou mais em Acessibilidade e em Boas práticas.
- [ ] Publicado no endereço principal (`seu-usuario.github.io`).
- [ ] Os projetos 1 e 2 já estão no portfólio, com os links funcionando.

**Marcos**

1. Página estática com as seções e dois cards escritos à mão.
2. Cards gerados pela lista de objetos.
3. Filtros e janela de detalhes.
4. Formulário, tema, publicação.

**Perguntas-guia**

- Que forma de dado guarda "um projeto" com todas as informações dele? E "todos os projetos"?
- Filtrar é esconder cards que já existem ou montar a lista de novo? Quais são as vantagens de cada jeito?
- Qual elemento do HTML já é uma janela e já fecha com Esc?

**Desafio extra:** a lista de projetos sai de um arquivo `projetos.json` lido com `fetch`, e o portfólio mostra quantos commits cada repositório tem, pela API pública do GitHub.

## Projeto 4 — Quadro Kanban

**Inspirado no AM Taskoro** · Etapa 2 · Módulo 2 · HTML, CSS, JavaScript (DOM, eventos, localStorage) · 3 a 4 semanas · individual

### O problema

Uma pequena equipe controla as tarefas em um grupo de mensagens e perde o que foi combinado. Ela precisa de um quadro simples, que funcione no navegador, sem login, onde cada pessoa veja o que está parado, o que está andando e o que terminou.

### Requisitos funcionais

1. RF1 — Três colunas fixas: **A fazer**, **Fazendo** e **Feito**.
2. RF2 — Criar cartão com título (obrigatório), descrição, prioridade (baixa, média, alta) e data de entrega (opcional).
3. RF3 — Editar e excluir cartão. Excluir pede confirmação.
4. RF4 — Mover cartão entre colunas arrastando com o mouse **e** por botões ou teclado (quem não usa mouse também precisa conseguir).
5. RF5 — Cada coluna mostra quantos cartões tem.
6. RF6 — Cartão com data de entrega vencida e fora de Feito aparece destacado.
7. RF7 — Filtro por prioridade e busca por texto no título.
8. RF8 — Tudo continua lá depois de fechar e abrir o navegador.
9. RF9 — Exportar o quadro para um arquivo .json e importar de volta.

### Regras de negócio

- RN1 — A coluna Fazendo aceita no máximo **3 cartões** (limite de trabalho em andamento). O 4º é recusado com um aviso, e o cartão volta para onde estava.
- RN2 — Título vazio ou só com espaços não cria cartão.
- RN3 — Cartão em Feito nunca aparece como atrasado.
- RN4 — Dentro da coluna, a ordem é: prioridade alta primeiro, depois a data de entrega mais próxima.
- RN5 — Importar um arquivo inválido não apaga o quadro atual; mostra o erro.

### Resultado esperado: casos de teste

| Situação | Ação | Resultado esperado |
| --- | --- | --- |
| Fazendo tem 3 cartões | Arrastar um 4º para Fazendo | Aviso "Limite de 3 cartões em Fazendo"; o cartão continua na coluna de origem |
| Título "   " | Clicar em Criar | Nenhum cartão criado; mensagem no campo |
| Hoje é 10/05; cartão em A fazer com entrega 09/05 | Abrir o quadro | Cartão destacado como atrasado |
| Mesmo cartão movido para Feito | — | Destaque some |
| 5 cartões criados | Fechar e reabrir o navegador | Os 5 cartões, nas mesmas colunas e na mesma ordem |
| Arquivo .json com texto qualquer | Importar | Mensagem de erro; quadro atual intacto |
| Cartões: média 12/05, alta 20/05, alta 15/05 | Ver a coluna | Ordem: alta 15/05, alta 20/05, média 12/05 |

### Critérios de aceite

- [ ] Todos os casos de teste acima passam.
- [ ] Dá para usar o quadro inteiro só com o teclado (Tab, Enter, setas ou botões).
- [ ] Funciona no celular sem rolagem horizontal.
- [ ] Nenhum erro no Console (F12).
- [ ] Código separado em HTML, CSS e JS; nada de onclick no HTML.
- [ ] Publicado no GitHub Pages, com README que explica como usar.

### Marcos

1. Colunas e formulário estáticos, com dados de exemplo escritos no JS.
2. Criar, editar, excluir e salvar no localStorage.
3. Mover (arrastar e teclado), limite de 3 e ordenação.
4. Atrasados, filtros, exportar e importar, responsivo e publicação.

### Perguntas-guia

- Onde fica a "verdade" do quadro: no HTML da tela ou num array de objetos no JS? O que acontece se forem duas verdades diferentes?
- Depois de mudar o array, como a tela fica igual a ele? Vale redesenhar tudo ou só o cartão que mudou?
- O localStorage só guarda texto. Como guardar um array de objetos?
- Como comparar a data de entrega com hoje sem errar por causa do horário?

### Desafio extra

Histórico de cada cartão ("criado em", "movido para Fazendo em") e um botão Desfazer para a última ação.

## Projeto 5 — Finanças em dupla

**Inspirado no AM Rendara** · Etapa 3 · Módulo 3 · HTML, CSS, JavaScript, Git em equipe (branches, pull requests, revisão) · 4 semanas · **em dupla**

### O problema

Uma pessoa quer saber para onde vai o dinheiro do mês e como dividir o que sobra entre as suas reservas (emergência, viagem, investimentos) sem fazer contas na mão. O projeto é feito em dupla porque, no trabalho, ninguém programa sozinho: o foco aqui é tanto o sistema quanto o jeito de trabalhar junto.

### Regra de trabalho da dupla

- Ninguém faz commit direto na main. Toda mudança entra por uma branch e um pull request.
- Todo pull request é revisado e aprovado pela outra pessoa, com pelo menos um comentário real.
- As tarefas ficam nas Issues do GitHub, cada uma com dono.
- Pelo menos um conflito de merge resolvido e registrado no README (o que conflitou e como resolveram).

### Requisitos funcionais

1. RF1 — Lançar receita ou despesa: descrição, valor, categoria, data.
2. RF2 — Listar os lançamentos do mês escolhido, com editar e excluir.
3. RF3 — Saldo do mês (receitas menos despesas) e total por categoria.
4. RF4 — Gráfico de despesas por categoria.
5. RF5 — Orçamento por categoria, com aviso em 80% e em 100%.
6. RF6 — Importar extrato em CSV (data;descrição;valor), mostrando o que será importado antes de confirmar.
7. RF7 — Carteiras (reservas) com saldo atual e meta em porcentagem.
8. RF8 — Botão "Distribuir aporte": informa um valor e o sistema diz quanto vai para cada carteira.
9. RF9 — Dados salvos no navegador.

### Regras de negócio

- RN1 — Valor zero ou negativo no formulário é recusado (o tipo, receita ou despesa, é que define o sinal).
- RN2 — Aviso de orçamento: amarelo ao atingir 80%, vermelho ao atingir 100%.
- RN3 — No CSV, valor negativo é despesa e positivo é receita. Linhas com data ou valor inválidos são ignoradas e listadas no fim.
- RN4 — Distribuir aporte: o total depois do aporte é dividido pelas metas. Cada carteira recebe a diferença entre o que deveria ter e o que tem, só se estiver abaixo da meta. Se a soma das diferenças passar do aporte, reparte-se o aporte na proporção das diferenças.
- RN5 — As metas das carteiras precisam somar 100%.
- RN6 — Dinheiro com duas casas decimais; a soma do que foi distribuído é exatamente igual ao aporte.

### Resultado esperado: casos de teste

| Entrada | Resultado esperado |
| --- | --- |
| Carteiras A=1000, B=500, C=500, D=0; metas 25% cada; aporte 1000 | A 0, B 200, C 200, D 600 (novo total 3000; meta de cada 750) |
| Carteiras A=0, B=0; metas 50% e 50%; aporte 100 | A 50, B 50 |
| Metas 50%, 30%, 10% | Erro: "As metas somam 90%; precisam somar 100%" |
| Orçamento Mercado 500; despesas 400 | Aviso amarelo (80%) |
| Orçamento Mercado 500; despesas 520 | Aviso vermelho (104%) |
| CSV com 10 linhas, 2 com data "32/13/2024" | 8 importadas; as 2 aparecem como ignoradas |
| Receitas 3000; despesas 2150,75 | Saldo 849,25 |

### Critérios de aceite

- [ ] Todos os casos de teste passam.
- [ ] Histórico do GitHub mostra os pull requests revisados pelas duas pessoas, e nenhum commit direto na main.
- [ ] Issues fechadas pelos pull requests ("Closes #3").
- [ ] Valores exibidos no formato brasileiro (R$ 1.234,56).
- [ ] Publicado no GitHub Pages; README com o que cada pessoa fez.

### Marcos

1. Repositório, proteção da main, Issues divididas; lançamentos e saldo.
2. Categorias, orçamento e avisos; gráfico.
3. Importação de CSV.
4. Carteiras e distribuição de aporte; revisão final e publicação.

### Perguntas-guia

- Por que 0,1 + 0,2 não dá 0,3 no JavaScript? Como guardar dinheiro sem esse problema (dica: centavos inteiros)?
- Na distribuição, se cada parte for arredondada, a soma pode dar 999,99. Para quem vai o centavo que sobrou?
- Como dividir o trabalho para que as duas pessoas não editem o mesmo arquivo ao mesmo tempo?
- O que um bom comentário de revisão diz, além de "ok"?

### Desafio extra

Meta de economia com previsão de quando será atingida, e exportar o mês em CSV.

## Projeto 6 — Agenda com API

**Inspirado no AM Horaria** · Etapa 3 · Módulo 4 · JavaScript assíncrono (fetch, async/await, Promise), API falsa com json-server · 3 a 4 semanas · individual

### O problema

Um salão com três profissionais marca horários por telefone e vive tendo dois clientes no mesmo horário. Ele quer uma página onde o cliente escolhe o serviço, o profissional e um horário livre. Os dados ficam numa API (aqui, uma API falsa que roda no seu computador), e a página conversa com ela pela rede, como um sistema de verdade.

### A API

O aluno cria o arquivo db.json e sobe a API com o json-server. Recursos obrigatórios:

- /servicos — nome, duração em minutos (30, 60 ou 90), preço.
- /profissionais — nome e lista de serviços que faz.
- /agendamentos — cliente, telefone, serviço, profissional, data e hora de início, status (marcado, cancelado).

### Requisitos funcionais

1. RF1 — Escolher serviço; a lista de profissionais mostra só quem faz aquele serviço.
2. RF2 — Escolher data e ver os horários livres do profissional naquele dia.
3. RF3 — Marcar: nome e telefone obrigatórios; grava na API com POST.
4. RF4 — "Meus agendamentos": busca pelo telefone e lista os futuros.
5. RF5 — Cancelar agendamento (PATCH do status, sem apagar o registro).
6. RF6 — Tela de estado em toda chamada: carregando, erro (com botão Tentar de novo) e lista vazia.
7. RF7 — Visão do dia para o salão: todos os agendamentos por profissional.

### Regras de negócio

- RN1 — Expediente das 9h às 18h, horários de início a cada 30 minutos. Almoço das 12h às 13h. Fecha aos domingos.
- RN2 — O serviço inteiro precisa caber no expediente: não pode invadir o almoço nem passar das 18h.
- RN3 — Sem conflito: um profissional não atende dois agendamentos que se sobrepõem (considerando a duração).
- RN4 — Não marca no passado e exige antecedência mínima de 2 horas.
- RN5 — Cancelamento só até 24 horas antes do horário.
- RN6 — Agendamento cancelado libera o horário.

### Resultado esperado: casos de teste

| Situação | Resultado esperado |
| --- | --- |
| Serviço de 60 min às 11h30 | Horário não aparece (terminaria 12h30, dentro do almoço) |
| Serviço de 60 min às 11h | Aparece (termina 12h) |
| Serviço de 90 min às 17h | Não aparece (terminaria 18h30) |
| Profissional com agendamento 14h–15h; novo serviço de 30 min | 14h e 14h30 não aparecem; 13h30 e 15h aparecem |
| Mesma situação; serviço de 60 min | 13h30 não aparece (13h30–14h30 bate com 14h) |
| Agora são 10h10 do mesmo dia | Primeiro horário oferecido: 13h (o mínimo seria 12h10, e 12h30 cai no almoço) |
| Agendamento amanhã às 9h; agora são 10h de hoje | Cancelar recusado (faltam 23h) |
| Um domingo | Mensagem "Fechado aos domingos"; nenhum horário |
| API desligada | Mensagem de erro e botão Tentar de novo; a página não quebra |

### Critérios de aceite

- [ ] Todos os casos de teste passam.
- [ ] Toda chamada à API usa async/await com try/catch.
- [ ] A regra de conflito também é conferida logo antes do POST (outra pessoa pode ter marcado enquanto a tela estava aberta).
- [ ] As funções de cálculo de horário ficam separadas das funções que mexem na tela.
- [ ] README explica como subir a API (npx json-server db.json) e abrir a página.

### Marcos

1. db.json com dados de exemplo; listar serviços e profissionais pela API.
2. Cálculo dos horários livres (sem tela, testado no console).
3. Marcar, listar e cancelar, com os estados de carregando e erro.
4. Visão do dia, responsivo e README.

### Perguntas-guia

- Como transformar "11:30" em um número que dá para somar e comparar?
- Dois intervalos \[início, fim) se sobrepõem quando? Escreva a condição antes de programar.
- O que o usuário vê enquanto o fetch não respondeu? E se ele clicar em Marcar duas vezes?
- Por que a regra do conflito não pode ficar só na tela?

### Desafio extra

Folga e férias por profissional, e lembrete gerado como texto pronto para mandar por WhatsApp.

## Projeto 7 — Loja virtual

**Inspirado no AM Vendra** · Etapa 4 · Módulos 5 e 6 · React, Next.js, TypeScript, Tailwind CSS, Zustand, deploy na Vercel · 5 a 6 semanas · individual

### O problema

Uma loja pequena vende pelo Instagram e anota os pedidos no caderno. Ela quer um catálogo com carrinho que calcule frete e cupom sozinho e gere o resumo do pedido. O pagamento real fica fora do escopo: o pedido termina numa tela de confirmação.

### Requisitos funcionais

1. RF1 — Catálogo com pelo menos 20 produtos (JSON local ou API falsa): foto, nome, preço, categoria, estoque.
2. RF2 — Página de cada produto em rota dinâmica (/produto/\[id\]), com título e descrição próprios para o Google.
3. RF3 — Busca por nome e filtros por categoria e faixa de preço, refletidos na URL (dá para mandar o link do filtro).
4. RF4 — Carrinho: adicionar, mudar quantidade, remover; continua lá ao recarregar a página.
5. RF5 — Frete pelo CEP, a partir de uma tabela de faixas.
6. RF6 — Cupom de desconto.
7. RF7 — Checkout com formulário validado e tela de confirmação com o resumo.
8. RF8 — Página 404 e estado de carregando.

### Regras de negócio

- RN1 — Quantidade no carrinho nunca passa do estoque.
- RN2 — Frete por faixa de CEP: 30000-000 a 39999-999 = R$ 15; 01000-000 a 19999-999 = R$ 25; demais = R$ 40. CEP inválido não calcula.
- RN3 — Frete grátis quando o subtotal, já com desconto, for R$ 300 ou mais.
- RN4 — Cupom pode ser porcentagem ou valor fixo, tem validade e valor mínimo de compra. Só um cupom por pedido. O desconto incide só sobre os produtos, não sobre o frete, e nunca deixa o total negativo.
- RN5 — Cupons do teste: DEZ (10%, mínimo R$ 100, válido), MENOS20 (R$ 20 fixo, sem mínimo, válido), VELHO (10%, vencido).

### Resultado esperado: casos de teste

| Carrinho | Ação | Resultado esperado |
| --- | --- | --- |
| Subtotal R$ 90 | Cupom DEZ | Recusado: "Compra mínima de R$ 100,00" |
| Subtotal R$ 150 | Cupom DEZ | Desconto R$ 15; produtos R$ 135 |
| Subtotal R$ 15 | Cupom MENOS20 | Desconto R$ 15 (nunca negativo); produtos R$ 0 |
| Qualquer | Cupom VELHO | Recusado: "Cupom vencido" |
| Subtotal R$ 150, CEP 30140-071 | Calcular frete | Frete R$ 15; total R$ 165 |
| Subtotal R$ 320, cupom DEZ, CEP 01310-100 | — | Produtos R$ 288 (abaixo de 300); frete R$ 25; total R$ 313 |
| Subtotal R$ 340, cupom DEZ, CEP 69900-000 | — | Produtos R$ 306; frete grátis; total R$ 306 |
| Produto com estoque 2 | Tentar quantidade 3 | Bloqueado em 2, com aviso |
| /produto/9999 | Abrir | Página 404 da loja |

### Critérios de aceite

- [ ] Todos os casos de teste passam.
- [ ] TypeScript em modo strict, sem any e sem erros no build.
- [ ] Regras de frete e cupom em funções puras, fora dos componentes.
- [ ] Lighthouse no celular: Acessibilidade 90 ou mais, Desempenho 80 ou mais.
- [ ] No ar na Vercel, com link no README.

### Marcos

1. Projeto Next.js com TypeScript e Tailwind; catálogo e página do produto.
2. Busca e filtros na URL.
3. Carrinho com Zustand e persistência; frete e cupom.
4. Checkout, 404, Lighthouse, deploy.

### Perguntas-guia

- Quais dados precisam de estado global (carrinho) e quais podem ficar no componente (campo de busca)?
- Qual é o tipo de um cupom? Escreva o type antes do código que o usa.
- Onde a página do produto deve ser montada: no servidor ou no navegador? O que muda para o Google?
- Na ordem de cálculo, o desconto vem antes ou depois de decidir o frete grátis? (A RN3 responde.)

### Desafio extra

Painel simples de administração para cadastrar produtos e cupons, protegido por senha.

## Projeto 8 — Ordens de serviço

**Inspirado no AM Consertta** · Etapa 5 · Módulos 7 e 8 · C#, .NET, programação orientada a objetos, LINQ, System.Text.Json, aplicação de console · 4 a 5 semanas · individual

### O problema

Uma assistência técnica de celulares e notebooks perde o controle de quais aparelhos estão na bancada, quais esperam aprovação do cliente e quais já podem ser retirados. Antes de ter tela e banco de dados, o sistema nasce como um programa de console: é aqui que o aluno aprende a modelar regras com classes, e não com if espalhado.

### Requisitos funcionais

1. RF1 — Cadastrar cliente (nome, telefone), equipamento (tipo, marca, modelo, número de série) e técnico (nome, valor da hora).
2. RF2 — Abrir ordem de serviço com cliente, equipamento e defeito relatado.
3. RF3 — Registrar diagnóstico, peças (descrição, valor) e horas previstas.
4. RF4 — Gerar orçamento e registrar aprovação ou recusa do cliente.
5. RF5 — Avançar o status da ordem, guardando data e hora de cada mudança.
6. RF6 — Consultar garantia de uma ordem entregue.
7. RF7 — Relatórios: ordens por status, faturamento do mês, técnico com mais ordens entregues, tempo médio entre abertura e entrega.
8. RF8 — Salvar e carregar tudo em um arquivo JSON ao sair e ao abrir o programa.
9. RF9 — Menu de console com opções numeradas; entrada inválida não derruba o programa.

### Regras de negócio

- RN1 — Fluxo de status: **Aberta → Em diagnóstico → Aguardando aprovação → Em reparo → Pronta → Entregue**. Qualquer status antes de Entregue pode ir para **Cancelada**. Orçamento recusado leva de Aguardando aprovação para Pronta (devolução sem reparo, só com a taxa de diagnóstico).
- RN2 — Qualquer outra transição lança exceção com a mensagem "Transição inválida: \<de> → \<para>".
- RN3 — Orçamento = soma das peças + horas × valor da hora do técnico.
- RN4 — Taxa de diagnóstico de R$ 50, cobrada só quando o orçamento é recusado.
- RN5 — Garantia de 90 dias corridos a partir da data de entrega, só para ordens reparadas.
- RN6 — Uma ordem Entregue ou Cancelada não muda mais.
- RN7 — O status só muda por um método da classe OrdemDeServico; de fora, ninguém altera a propriedade diretamente.

### Resultado esperado: casos de teste

| Situação | Resultado esperado |
| --- | --- |
| Ordem Em reparo; mudar para Entregue | Exceção: "Transição inválida: Em reparo → Entregue" |
| Ordem Aberta; mudar para Em diagnóstico | Aceito; histórico com 2 registros |
| Peças R$ 120 + R$ 60; 2,5 h; técnico a R$ 80/h | Orçamento R$ 380,00 |
| Orçamento recusado | Status Pronta; valor a cobrar R$ 50,00 |
| Entregue em 10/01/2025; consulta em 10/04/2025 | Na garantia (último dia) |
| Mesma ordem; consulta em 11/04/2025 | Fora da garantia |
| Ordem Entregue; tentar Cancelada | Exceção de transição inválida |
| Digitar "abc" no menu | Mensagem "Opção inválida"; o menu volta |
| Fechar e abrir o programa | Todas as ordens e históricos de volta |

### Critérios de aceite

- [ ] Todos os casos de teste passam.
- [ ] Compila sem nenhum aviso, com Nullable habilitado.
- [ ] Status é um enum; as transições permitidas ficam num só lugar do código.
- [ ] Relatórios feitos com LINQ, sem laços manuais de soma.
- [ ] Valores em decimal (nunca double para dinheiro).
- [ ] README com o diagrama das classes e o fluxo de status.

### Marcos

1. Classes e enum; diagrama no papel antes do código.
2. Fluxo de status com exceções e histórico; orçamento.
3. Menu de console e persistência em JSON.
4. Garantia, relatórios com LINQ e README.

### Perguntas-guia

- Por que a propriedade Status deve ter set privado?
- Como representar "de Em reparo só pode ir para Pronta ou Cancelada" como dado, e não como uma cadeia de if?
- 90 dias é o mesmo que 3 meses? Qual método de DateTime usar?
- O que acontece com os dados se o programa fechar no meio da gravação do arquivo?

### Desafio extra

Testes automatizados com xUnit para o fluxo de status e o cálculo do orçamento (é o que o Projeto 11 vai exigir).

## Projeto 9 — Banco de dados do PDV

**Inspirado no AM Kaixara** · Etapa 6 · Módulo 10 · PostgreSQL, SQL, modelagem, Docker Compose · 4 semanas · individual

### O problema

Um mercadinho vai trocar o caderno por um sistema de ponto de venda (PDV). Antes de qualquer tela, precisa de um banco de dados que não aceite dado errado e responda rápido às perguntas do dono. O entregável são arquivos .sql, não um sistema: este banco é reaproveitado na opção A do Projeto 12.

### Requisitos funcionais

1. RF1 — Diagrama entidade-relacionamento com: categoria, produto, cliente (opcional na venda), venda, item\_venda, pagamento e movimentacao\_estoque.
2. RF2 — Arquivo 01-estrutura.sql com as tabelas, chaves, restrições e índices.
3. RF3 — Arquivo 02-dados.sql que gera dados de teste: 50 produtos, 200 clientes e 10.000 vendas espalhadas por 90 dias (use generate\_series).
4. RF4 — Arquivo 03-consultas.sql com as 10 consultas abaixo, cada uma com um comentário da pergunta que responde.
5. RF5 — Arquivo 04-desempenho.sql com EXPLAIN ANALYZE de uma consulta lenta antes e depois de criar um índice, e o tempo anotado.
6. RF6 — docker-compose.yml que sobe o PostgreSQL e roda os arquivos na ordem.

**As 10 consultas:** (1) ranking de produtos por faturamento no período; (2) ticket médio por dia; (3) produtos abaixo do estoque mínimo; (4) vendas por forma de pagamento; (5) curva ABC dos produtos; (6) faturamento por categoria e mês; (7) os 10 melhores clientes; (8) horário de pico (vendas por hora do dia); (9) produtos sem venda nos últimos 30 dias; (10) estoque atual de cada produto calculado pelas movimentações.

### Regras de negócio

- RN1 — Preço maior que zero; quantidade vendida maior que zero; código de barras único.
- RN2 — O item guarda o preço do momento da venda (se o preço do produto mudar amanhã, a venda de hoje não muda).
- RN3 — Forma de pagamento só entre: dinheiro, pix, débito, crédito.
- RN4 — Produto com vendas não pode ser apagado (só desativado).
- RN5 — Curva ABC: A até 80% do faturamento acumulado, B de 80% a 95%, C o restante.
- RN6 — Dinheiro em numeric(10,2), nunca em float.

### Resultado esperado: casos de teste

**Inserts que o banco precisa recusar** (cada um deve dar erro):

| Tentativa | Deve falhar por |
| --- | --- |
| Produto com preço -5 | CHECK |
| Item de venda com quantidade 0 | CHECK |
| Item apontando para a venda 999999, que não existe | Chave estrangeira |
| Dois produtos com o mesmo código de barras | UNIQUE |
| Pagamento com forma "cheque" | CHECK |
| DELETE de um produto que tem vendas | Chave estrangeira (RESTRICT) |

**Base de conferência** (rode antes do 02-dados.sql): produtos Café R$ 10, Leite R$ 5, Pão R$ 1. Dia 1: venda A = 2 cafés + 10 pães; venda B = 1 leite. Dia 2: venda C = 3 cafés; venda D = 4 leites + 5 pães.

| Consulta | Resultado esperado |
| --- | --- |
| Ranking por faturamento | Café R$ 50,00 · Leite R$ 25,00 · Pão R$ 15,00 |
| Ticket médio por dia | Dia 1: R$ 17,50 · Dia 2: R$ 27,50 |
| Curva ABC | Café A (55,6% acumulado) · Leite B (83,3%) · Pão C (100%) |

### Critérios de aceite

- [ ] docker compose up sobe o banco com tudo criado, sem passo manual.
- [ ] Os 6 inserts inválidos falham; a base de conferência dá exatamente os resultados acima.
- [ ] As 10 consultas rodam nos dados de teste em menos de 1 segundo cada.
- [ ] O EXPLAIN ANALYZE mostra a troca de Seq Scan por Index Scan (ou explica por que não trocou).
- [ ] README com o diagrama e a explicação de cada índice criado.

### Marcos

1. Diagrama e estrutura; testar os inserts inválidos.
2. Base de conferência e as consultas 1, 2 e 5 conferidas.
3. Geração dos 10.000 registros e as outras consultas.
4. Índices, EXPLAIN ANALYZE, Docker Compose e README.

### Perguntas-guia

- Por que o preço fica copiado no item\_venda se já está no produto?
- Estoque deve ser uma coluna do produto ou a soma das movimentações? Quais são as vantagens de cada escolha?
- Na curva ABC, como calcular o "acumulado" sem laço? (Pesquise funções de janela.)
- Um índice deixa tudo mais rápido? O que ele piora?

### Desafio extra

Uma view para o relatório de fechamento de caixa e uma função que registra a venda e baixa o estoque numa só transação.

## Projeto 10 — API da clínica veterinária

**Inspirado no AM Petara** · Etapa 7 · Módulos 9, 10 e 12 · ASP.NET Core Web API (Controllers), Entity Framework Core, PostgreSQL, JWT, Swagger, Docker Compose · 6 a 8 semanas · individual

### O problema

Uma clínica veterinária quer um sistema que a recepção, os veterinários e o dono usem ao mesmo tempo, cada um vendo só o que pode. Este projeto é só a API (o back-end); qualquer tela pode ser ligada nela depois. É o primeiro projeto com login, permissões e banco de verdade.

### Requisitos funcionais

1. RF1 — CRUD de tutores (donos), pets, veterinários e vacinas.
2. RF2 — Agendar, remarcar, cancelar e concluir consultas.
3. RF3 — Prontuário: anotações do veterinário em cada consulta concluída.
4. RF4 — Carteira de vacinação do pet, com a data da próxima dose e as atrasadas.
5. RF5 — Login que devolve um token JWT; usuários com papel Recepção, Veterinário ou Admin.
6. RF6 — Listagens paginadas (page, pageSize) e com filtro (pets por nome, consultas por data e por veterinário).
7. RF7 — Swagger com todos os endpoints documentados e botão de autorização.
8. RF8 — Erros no formato ProblemDetails.
9. RF9 — docker compose up sobe a API e o banco, com migrations aplicadas.

### Regras de negócio

- RN1 — A API recebe e devolve DTOs, nunca as entidades do banco.
- RN2 — Consulta dura 30 minutos; um veterinário não tem duas consultas que se sobrepõem.
- RN3 — Não se agenda no passado; o pet precisa existir e estar ativo.
- RN4 — Próxima dose = data da aplicação + intervalo em dias da vacina. Passou da data sem nova aplicação = atrasada.
- RN5 — Permissões: Recepção cadastra tutores, pets e agenda consultas, mas não lê prontuário. Veterinário lê e escreve prontuário e aplica vacinas. Admin cadastra veterinários e usuários.
- RN6 — Senhas guardadas com hash, nunca em texto.
- RN7 — Pet com consultas não é apagado, é desativado.

### Resultado esperado: casos de teste

| Requisição | Resposta esperada |
| --- | --- |
| GET /api/pets sem token | 401 |
| Recepção: GET /api/consultas/{id}/prontuario | 403 |
| POST consulta do Dr. Ana às 14h10, já existindo uma às 14h | 409, ProblemDetails dizendo o conflito |
| POST consulta do Dr. Ana às 14h30, já existindo uma às 14h | 201 com Location |
| POST pet sem nome | 400 com o erro no campo "nome" |
| GET /api/pets/9999 | 404 |
| Vacina com intervalo de 365 dias aplicada em 15/03/2025 | Próxima dose 15/03/2026 |
| Mesma vacina; consulta da carteira em 20/03/2026 sem nova aplicação | Dose aparece como atrasada |
| GET /api/pets?page=2&pageSize=10 com 25 pets | 10 itens; total 25; 3 páginas |
| DELETE de pet com consultas | 204, e o pet some das listagens mas continua no banco como inativo |

### Critérios de aceite

- [ ] Todos os casos de teste passam, conferidos por uma coleção de requisições (arquivo .http ou coleção do Postman/Insomnia) entregue no repositório.
- [ ] Regras de negócio fora dos controllers (em serviços).
- [ ] Segredos (chave do JWT, senha do banco) fora do código, em variáveis de ambiente.
- [ ] Migrations versionadas no Git.
- [ ] README com o diagrama das entidades, como rodar e usuários de teste de cada papel.

### Marcos

1. Projeto, entidades, DbContext, migrations e CRUD de tutores e pets.
2. Consultas com a regra de conflito, validação e ProblemDetails.
3. Autenticação JWT e permissões por papel; prontuário.
4. Vacinas, paginação, Swagger, Docker Compose e README.

### Perguntas-guia

- Qual é a diferença entre 401 e 403? E entre 400 e 409?
- Por que devolver a entidade do EF Core direto pode vazar dados ou causar laço infinito no JSON?
- A regra de conflito fica no controller, no serviço ou no banco? E se duas requisições chegarem no mesmo milissegundo?
- O que vai dentro de um token JWT? Por que não se coloca a senha nele?

### Desafio extra

Envio de lembrete de vacina (simulado com log) por um serviço em segundo plano que roda uma vez por dia.

## Projeto 11 — Reservas do condomínio com TDD

**Inspirado no AM Predara** · Etapa 8 · Módulo 14 · ASP.NET Core, xUnit, testes de integração com WebApplicationFactory, Playwright, cobertura de testes · 4 a 5 semanas · individual

### O problema

Um condomínio com 120 apartamentos briga toda semana pelo salão de festas e pela churrasqueira. As regras estão no regimento, mas ninguém confere. Aqui a novidade não é a tecnologia: é o método. **Cada regra nasce primeiro como um teste que falha**, e só depois vira código. O histórico de commits precisa mostrar isso.

### Requisitos funcionais

1. RF1 — Áreas comuns com nome, capacidade e taxa de uso (salão: 80 pessoas, R$ 150; churrasqueira: 30 pessoas, R$ 80).
2. RF2 — Reservar uma área para uma data, informando a unidade e o número de convidados.
3. RF3 — Cancelar reserva, com cálculo de multa quando houver.
4. RF4 — Lista de espera por área e data.
5. RF5 — Marcar unidade como inadimplente ou em dia.
6. RF6 — Endpoints da API para tudo acima, e uma tela simples de reserva (pode ser Razor Pages ou uma página HTML que chama a API).

### Regras de negócio

- RN1 — Cada unidade tem no máximo 1 reserva por área por semana (segunda a domingo).
- RN2 — Antecedência mínima de 48 horas e máxima de 60 dias. Cada reserva ocupa o dia inteiro.
- RN3 — Unidade inadimplente não reserva.
- RN4 — Convidados não passam da capacidade da área.
- RN5 — Cancelamento grátis até 72 horas antes; depois disso, multa de 20% da taxa.
- RN6 — Quando uma reserva é cancelada, a primeira unidade da lista de espera (que ainda cumpra as regras) recebe a reserva automaticamente.
- RN7 — O relógio é injetado (uma interface de "agora"), para que os testes controlem a data.

### Resultado esperado: casos de teste

Agora = segunda-feira, 02/06/2025, 10h. Todos os casos devem virar testes automatizados.

| Cenário | Resultado esperado |
| --- | --- |
| Unidade 101 reserva o salão para 04/06 (quarta) | Recusado: faltam 38 h (mínimo 48 h) |
| Unidade 101 reserva o salão para 05/06 (quinta) | Aceito |
| Unidade 101 reserva o salão para 02/08/2025 | Recusado: mais de 60 dias |
| Unidade 101 já tem o salão em 05/06; pede o salão em 07/06 | Recusado: já tem reserva do salão nesta semana |
| Mesma unidade pede a churrasqueira em 07/06 | Aceito (área diferente) |
| Unidade 305 inadimplente pede qualquer área | Recusado: unidade inadimplente |
| Salão com 90 convidados | Recusado: capacidade 80 |
| Reserva do salão em 10/06; cancelada em 06/06 às 10h (86 h antes) | Cancelada sem multa |
| Mesma reserva cancelada em 08/06 às 10h (38 h antes) | Cancelada com multa de R$ 30,00 |
| 101 tem o salão em 12/06; 202 entra na lista de espera; 101 cancela | Reserva passa para a 202 automaticamente |
| Mesmo cenário, mas a 202 ficou inadimplente | Pula a 202; vai para a próxima da lista, ou a data fica livre |

### Critérios de aceite

- [ ] Todos os cenários acima existem como testes de unidade, com nomes que dizem a regra (ex.: Reserva\_com\_menos\_de\_48h\_e\_recusada).
- [ ] Pelo menos 5 testes de integração chamando a API de verdade (WebApplicationFactory).
- [ ] 1 teste de ponta a ponta com Playwright: abrir a tela, reservar, ver a confirmação.
- [ ] Cobertura de 80% ou mais no projeto de domínio (as regras).
- [ ] Histórico do Git com commits "teste falhando" antes de "regra implementada" em pelo menos 5 regras.
- [ ] Nenhum teste depende da data real do computador.

### Marcos

1. Projeto de domínio e de testes; relógio injetável; RN2 e RN4 por TDD.
2. RN1, RN3 e RN5 por TDD.
3. Lista de espera (RN6) e a API com testes de integração.
4. Tela, teste com Playwright, relatório de cobertura e README.

### Perguntas-guia

- Por que um teste que usa DateTime.Now pode passar hoje e falhar amanhã?
- Qual é o menor código que faz o teste passar? Por que começar por ele?
- Qual é a diferença entre um teste de unidade e um de integração? Qual quebra mais fácil, e por quê?
- 80% de cobertura garante que o sistema funciona? O que ela não mede?

### Desafio extra

GitHub Actions rodando todos os testes a cada push, com o selo de "passando" no README.

## Projeto 12 — Sistema completo (escolha 1 de 3)

**Inspirado no AM Kaixara, AM Rotara ou AM Mentor** · Etapa 9 · Todos os módulos · tudo o que veio antes, mais Docker, CI/CD, deploy e observabilidade · 8 a 12 semanas · individual ou em dupla

### O problema

Este é o projeto que vai para o topo do portfólio e para a conversa da entrevista. Ele junta front-end, API, banco, testes e deploy num sistema que alguém de fora consegue abrir e usar. O aluno escolhe **uma** das três opções; todas têm o mesmo tamanho e os mesmos requisitos comuns.

### Requisitos comuns (valem para as três opções)

1. RC1 — Front-end em Next.js com TypeScript; API em ASP.NET Core; banco PostgreSQL.
2. RC2 — docker compose up sobe o sistema inteiro no computador de quem avalia.
3. RC3 — GitHub Actions: build e testes a cada pull request; a main só recebe código com testes passando.
4. RC4 — No ar: front-end na Vercel e API num serviço de hospedagem ou VPS, com HTTPS.
5. RC5 — Login com pelo menos dois papéis de usuário.
6. RC6 — Logs estruturados e um endpoint /health.
7. RC7 — Testes automatizados das regras principais (as da opção escolhida).
8. RC8 — README com diagrama da arquitetura, decisões tomadas (e por quê), como rodar e usuários de teste.
9. RC9 — Vídeo de até 3 minutos mostrando o sistema funcionando.

### Opção A — PDV do mercadinho (AM Kaixara)

Reaproveita o banco do Projeto 9.

- Tela de caixa: busca do produto por nome ou código de barras, carrinho, desconto, várias formas de pagamento na mesma venda, troco.
- Funciona como aplicativo instalável no celular ou tablet (PWA).
- Papéis: Operador de caixa e Gerente.
- Abertura e fechamento de caixa, com relatório do dia.
- Regras: a soma dos pagamentos precisa ser igual ao total; troco só em dinheiro; desconto acima de 10% exige senha do gerente; venda baixa o estoque na mesma transação; fechamento compara o dinheiro contado com o esperado.

| Caso | Resultado esperado |
| --- | --- |
| Total R$ 87,50; pix R$ 50 + dinheiro R$ 50 | Venda concluída; troco R$ 12,50 |
| Total R$ 87,50; pix R$ 50 + débito R$ 40 | Recusado: troco só em dinheiro |
| Desconto de 15% feito pelo operador | Pede senha do gerente |
| Caixa aberto com R$ 100; vendas em dinheiro R$ 430; contado R$ 525 | Fechamento com falta de R$ 5,00 |

### Opção B — Pedidos com entrega em tempo real (AM Rotara)

- Cliente faz o pedido; restaurante aceita e muda o status; entregador atualiza a posição.
- O cliente acompanha o status e o entregador no mapa sem recarregar a página (SignalR).
- Mapa com Leaflet e OpenStreetMap; a posição do entregador pode ser simulada.
- Papéis: Cliente, Restaurante e Entregador.
- Regras: entrega só dentro do raio de 5 km do restaurante (cálculo no banco com PostGIS); taxa de entrega R$ 5 + R$ 1,50 por km, arredondando o km para cima; pedido só pode ser cancelado pelo cliente antes de o restaurante aceitar.

| Caso | Resultado esperado |
| --- | --- |
| Endereço a 3,2 km | Aceito; taxa R$ 11,00 (4 km) |
| Endereço a 6 km | Recusado: fora da área de entrega |
| Restaurante muda para "Saiu para entrega" | Tela do cliente muda em até 2 segundos, sem recarregar |
| Cliente cancela após o restaurante aceitar | Recusado |

### Opção C — Plataforma de exercícios (AM Mentor)

- Trilhas com módulos e exercícios (múltipla escolha e resposta curta), corrigidos automaticamente.
- Progresso do aluno por trilha; certificado em PDF com código que qualquer pessoa confere numa página pública.
- Papéis: Aluno e Professor (que cria trilhas e exercícios).
- Regras: o gabarito comentado só aparece depois de 3 tentativas ou do acerto; o módulo seguinte só libera com 70% de acertos no anterior; certificado só com a trilha 100% concluída.

| Caso | Resultado esperado |
| --- | --- |
| Aluno erra 2 vezes | Gabarito ainda escondido |
| Aluno erra a 3ª vez | Gabarito comentado aparece |
| Módulo 1 com 6 de 10 acertos | Módulo 2 continua bloqueado |
| Trilha completa; pedir certificado | PDF com código; a página de conferência mostra nome, trilha e data |
| Código inventado na página de conferência | "Certificado não encontrado" |

### Critérios de aceite

- [ ] Todos os requisitos comuns cumpridos e os casos da opção escolhida passando.
- [ ] Link público funcionando; usuários de teste de cada papel no README.
- [ ] Pipeline do GitHub Actions verde, com pelo menos um pull request barrado por teste falhando no histórico.
- [ ] Nenhum segredo no repositório.
- [ ] Vídeo de até 3 minutos no README.

### Marcos

1. Escolha da opção, diagrama da arquitetura, modelo do banco e lista de Issues.
2. API com as regras e os testes.
3. Front-end ligado à API, com login e papéis.
4. Docker Compose e GitHub Actions.
5. Deploy, logs, /health.
6. README, vídeo e ensaio da apresentação de 5 minutos para entrevista.

### Perguntas-guia

- Se o avaliador tiver 5 minutos, o que ele precisa ver primeiro?
- Qual decisão de arquitetura você tomou que um júnior normalmente não toma? Como explicar o porquê?
- O que acontece se a API cair enquanto alguém usa o front-end?
- Como saber que o sistema no ar está funcionando sem abrir a página?

### Desafio extra

Monitoramento com alerta (por exemplo, um serviço gratuito que chama o /health a cada 5 minutos e avisa por e-mail).

## Como produzir o "resultado esperado" sem entregar o código

O aluno recebe o enunciado acima e vê o sistema pronto funcionando, mas nunca o código. Para isso:

1. **Você constrói cada projeto primeiro.** Cada um corresponde a uma etapa do seu próprio plano de estudos, então fazer os 12 é estudar e produzir material ao mesmo tempo. Guarde os repositórios como privados.
2. **Grave um vídeo de 1 a 2 minutos** por projeto, mostrando cada caso de teste acontecendo na tela, na ordem da tabela. Sem mostrar o editor de código.
3. **Tire capturas de tela** no computador e no celular das telas principais. Elas servem de referência visual, não de molde a copiar pixel por pixel.
4. **Não publique demonstração ao vivo dos projetos de front-end (1 a 7).** Uma página publicada entrega o HTML, o CSS e o JavaScript para qualquer um que aperte F12. Vídeo e capturas bastam.
5. **Nas APIs (6, 10, 11 e 12), entregue a coleção de requisições** (arquivo .http) com a resposta esperada de cada uma. O aluno roda a coleção contra a própria API e compara.
6. **Opcional, e muito valioso: testes de aceite prontos.** Para os projetos com regras fechadas (1, 5, 8, 9 e 11), você pode entregar um arquivo de testes que o aluno liga no código dele. Os testes dizem se passou ou falhou, mas não mostram como resolver. Para isso, o enunciado precisa fixar o nome das funções ou endpoints que serão testados.
7. **Mantenha os números das tabelas exatos.** Eles são o contrato: se o vídeo mostrar R$ 313,00 e a tabela disser R$ 313,00, o aluno tem como saber sozinho se acertou.

### O que o aluno recebe em cada projeto

| Recebe | Não recebe |
| --- | --- |
| Enunciado com requisitos, regras e casos de teste | Código-fonte da solução |
| Vídeo e capturas do resultado final | Estrutura de pastas pronta ou código inicial |
| Coleção de requisições (projetos com API) | Link ao vivo dos projetos de front-end |
| Testes de aceite (quando houver) | Respostas das perguntas-guia |
| Indicação dos módulos do site que ensinam o necessário |  |

### Por que isso é suficiente para fazer do zero

Cada projeto só usa o que os módulos anteriores ensinaram, os marcos dizem por onde começar e em que ordem seguir, as perguntas-guia apontam as armadilhas antes de o aluno cair nelas, e os casos de teste dizem exatamente quando terminou. O que falta é justamente o que ele precisa aprender a fazer: transformar um enunciado em código.
