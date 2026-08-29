---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Passo a Passo Mestre — Do Dia 1 até o Portfólio em Aceleração
### Sequência única, cronológica, unindo estudo + desenvolvimento + matemática + reaproveitamento

> ℹ️ **Para o dia a dia, use [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]]** — este documento continua aqui como referência de detalhe (texto mais longo por Passo), mas não precisa mais ser aberto pra saber "o que vem agora".

> Este documento é o **guia de sequência**. Os detalhes de conteúdo completo de cada fase continuam nos documentos originais ([[plano-estudos-basico-avancado-entrelacado]], [[matematica-e-desenvolvimento-integrado]], [[estrategia-reaproveitamento-ordem-construcao]], [[ordem-construcao-rf-telas-reaproveitaveis]], [[EPIC-01-backlog-passo1-fundamentos]], [[ingles-espanhol-integrado]], [[metodo-correto-estudo-idiomas]], [[perfil-senior-completo-auditoria]], [[metodo-estudo-producao-didatica-simultanea]], [[github-estrutura-profissional-autoridade]], [[aurapos-frontend-documento-unico]], [[rnf-transversais-design-tema]]) — aqui você só olha "onde estou, o que vem agora".

---

## PASSO 1 — Lógica + Matemática (Parte I) + Inglês (início) (2-3 semanas)
**Estudar:** Fase 0 do plano de desenvolvimento (variável, condicional, laço, função, coleção) **junto com** a Parte I completa do livro de Matemática (Capítulo 1 — Linguagem Matemática, Capítulo 2 — Teoria Ingênua dos Conjuntos) — na mesma semana, reforçando o mesmo raciocínio dos dois lados. Em paralelo, iniciar a Fase A de Inglês (nivelamento + atenção ao vocabulário técnico que já aparece no código).
**Desenvolver:** exercícios de lógica pura em console — cálculo de carrinho com desconto, simulação da escada de inadimplência, simulação simplificada do rebalanceamento ARCA (sem banco, sem API).
**✅ Sinal de conclusão:** resolve os três exercícios sem travar. Ver detalhamento completo em [[EPIC-01-backlog-passo1-fundamentos]].

---

## PASSO 2 — Git, SQL, Docker (1-2 semanas)
**Estudar:** Fase 1 completa (Git, SQL/PostgreSQL com `EXPLAIN ANALYZE`, Docker). A Matemática pausa a leitura nova aqui — a Parte II do livro (Naturais/Inteiros/Aritmética Modular/Racionais/Aplicações Aritméticas/Sequências/Reais) é densa demais pra caber "de raspão"; ela começa de fato no Passo 3, junto com C#.
**Desenvolver:** o schema real de tabelas do AuraPOS (produto, categoria, estoque, venda) direto no PostgreSQL, à mão. Em seguida, o schema simples do `aura-licensing` (tenant, módulo, assinatura) como segundo exercício de modelagem.
**✅ Sinal de conclusão:** lê um `EXPLAIN ANALYZE` e identifica full scan desnecessário; ambiente sobe com `docker-compose up`.

---

## PASSO 3 — C# Fundamentals + Matemática (Parte II, início) (1-2 semanas)
**Estudar:** Fase 2.1 (tipo, classe, coleção, LINQ, nullable reference type, `async/await` real, tempo de vida de DI) + início da **Parte II do livro** (Capítulo 3 — Naturais e Inteiros: indução, divisibilidade, MDC/MMC, **Algoritmo de Euclides**). *Nota: "Cálculo I" (limite/derivada) não está neste livro — é um livro futuro, separado, só relevante bem mais adiante; o que sustenta noção de complexidade de algoritmo por enquanto é a própria lógica do Capítulo 1, já vista no Passo 1.*
**Desenvolver:** entidades de domínio do AuraPOS (`Product`, `Category`, `Sale`) já com nullable reference type habilitado desde o início. Ao chegar em recursão (Fase 2.1 aprofundada), implementar o Algoritmo de Euclides em código — matemática e programação convergindo no mesmo conceito, não analogia.
**✅ Sinal de conclusão:** entidades compilando, sem warning de referência nula; Algoritmo de Euclides implementado e testado.

---

## PASSO 4 — API e Autenticação, na ordem certa de reaproveitamento (2-3 semanas)
**Estudar:** Fase 2.2 completa (rota, DTO, validação, JWT, design de API maduro, OWASP Top 10 aplicado, rate limiting) + continuação da Parte II (Capítulo 4 — Aritmética Modular, incluindo a aplicação a **RSA** citada no próprio livro — conexão direta com segurança/autenticação que você está construindo nesta mesma fase). Inglês: Fase B (trocar fonte de documentação técnica pra inglês) começa aqui.
**Desenvolver, nesta ordem exata (Grupo 1 do documento de ordem de construção):**
1. Convenção `tenant_id` + Row-Level Security no `DbContext`
2. `AuthController` — login com JWT + BCrypt (AuraPOS RF01) — já pensando que isso vira o protótipo do `aura-identity` depois
3. Controle de acesso por papel (RF02)
4. Blindar o login contra o OWASP Top 10 estudado nesta mesma fase

**Tela a construir em paralelo, seguindo agora o `aurapos-frontend-documento-unico` (11 etapas), não mais genérico:**
1. Etapa 3 (Design System) — implementar os tokens exatos como CSS custom properties (cor, sombra, z-index, animação, ícone — valores hex reais, não "azul petróleo" solto)
2. Etapa 4.3 — Tela de login e shell do painel administrativo, aplicando os tokens acima
3. **Pendência real, não fictícia:** a Etapa 1 (Discovery) do documento de frontend ainda depende de 3-5 conversas reais com dono/operador de pequeno comércio pra validar a persona — vale fazer isso em paralelo a este Passo, não depois

**✅ Sinal de conclusão:** login funcional, protegido, com tela real consumindo a API, usando os tokens de cor exatos definidos no Etapa 3.

---

## PASSO 5 — EF Core + o CRUD que vira molde de tudo (1-2 semanas)
**Estudar:** Fase 2.3 (migration, relacionamento, `AsNoTracking`, N+1, leitura do SQL gerado) + fechamento da Parte II (Capítulo 5 — Racionais; Capítulo 6 — Aplicações Aritméticas: **aqui sim entram razão, proporção, regra de três, porcentagem e juros**, com aplicação direta no cálculo de desconto que você já simulou no Passo 1; Capítulo 7 — Sequências, ligando recorrência matemática a recursão em código; Capítulo 8 — Reais).
**Desenvolver, nesta ordem (Grupo 2):**
1. CRUD de produto/categoria (RF03) — este é o "molde" que todo sistema futuro copia
2. **RNFT-E01 imediatamente** — coluna `RowVersion`, atualização condicional no `ProductRepository`. Não adie isso: é o item que sozinho destrava reaproveitamento em 8 sistemas futuros
3. Reserva de estoque (RF11 — `ReservedQuantity`/`ReservedUntil`)

**Telas em paralelo, seguindo `aurapos-frontend-documento-unico`:**
3. Etapa 6.1 — Configurar TanStack Query (estado de servidor) + Zustand (estado local do carrinho) desde o início do CRUD, não depois
4. Etapa 4 — Tabela genérica com busca/filtro/paginação (item 3), já com estado de skeleton loading (`--skeleton-base`/`--skeleton-shimmer`)
5. Formulário genérico de cadastro/edição (item 4), com anel de foco (`--foco-anel`) aplicado desde a primeira versão, não retrofit depois

**✅ Sinal de conclusão:** CRUD de produto funcionando, com teste de concorrência passando (duas requisições simultâneas, uma aceita, uma rejeitada corretamente).

---

## PASSO 6 — Teste como disciplina (1-2 semanas)
**Estudar:** Fase 2.4 (pirâmide de teste, `Moq`, teste de integração, ciclo TDD) + Etapa 8 do `aurapos-frontend-documento-unico` (Testing Library, Playwright).
**Desenvolver:** teste unitário e de integração do fluxo de venda (o trecho mais sensível à concorrência) no backend; teste de componente do carrinho + primeiro E2E com Playwright (login → busca → adicionar → confirmar → recibo) no frontend, os dois no mesmo Passo, não em momentos separados. Praticar TDD puro no `aura-goals` (regra pequena e isolada, bom terreno de treino).
**✅ Sinal de conclusão:** cobertura de teste real no fluxo de venda, no backend e no frontend, não só nos casos fáceis.

---

## PASSO 7 — Fechar o resto do AuraPOS: pagamento e cobrança (2-3 semanas)
**Estudar:** continuação da Fase 2/3, sem tópico novo de estudo formal — é fase de aplicação.
**Desenvolver, nesta ordem (Grupo 3):**
1. Carrinho com múltiplos meios de pagamento (RF04)
2. **RNFT-E02** — idempotência de pagamento (chave de idempotência em webhook)
3. Abertura/fechamento de caixa (RF05), cancelamento com restauração de estoque (RF06)

**Telas:**
5. Dashboard com card de indicador (item 5)
6. Checkout/carrinho (item 6) — reaproveitado depois por Loja Virtual, AuraFix, AuraVet, AuraEdu

**✅ Sinal de conclusão:** AuraPOS com fluxo de venda ponta a ponta, pagamento idempotente.

---

## PASSO 8 — Arquitetura de verdade (contínuo, mas consolida aqui)
**Estudar:** Fase 4 (SOLID, Design Patterns, Clean Architecture, DI ligada à arquitetura).
**Desenvolver:** refatorar o AuraPOS já existente aplicando cada padrão nele mesmo. Implementar as interfaces trocáveis (`IFonteDeEstoque`, `IEmissorFiscal`) — é Strategy Pattern aplicado, aprendido e avançando o produto ao mesmo tempo.
**✅ Sinal de conclusão:** você refatora uma classe e explica por que cada mudança segue SOLID.

---

## PASSO 8B — Trilha 42 (bloco de 7-9 meses, roda em paralelo aos Passos 9 em diante)
**Não trava nenhum passo seguinte** — é trilha longa e paralela, mesma posição do Pentest (Fase 12) e do Python (Fase 7).
**✅ Sinal de conclusão:** os 24 entregáveis completos, cada um com a versão C#/TypeScript e a versão C/C++ funcionando.

---

## PASSO 9 — Ponte técnica pro próximo sistema (após MVP do AuraPOS)
**Estudar:** Fase 5 (PostGIS, Redis, SignalR, PWA vs. nativo) + Capítulo 13 (Estruturas Lineares — sistema linear, vetor, matriz) e Capítulo 17 (Geometria Analítica — distância e ponto médio, vetores no plano) do livro. **Esses dois capítulos já cobrem o que seria "Álgebra Linear I" separada — não precisa comprar outro livro pra PostGIS.** Inglês entra na Fase C aqui (ADR e README em inglês, já que Fase 6D se aproxima).
**Desenvolver:** cache de produto/estoque via Redis no próprio AuraPOS; SignalR no dashboard do AuraPOS (prepara o terreno técnico pro status de pedido do Delivery depois).
**✅ Sinal de conclusão:** dashboard atualiza em tempo real sem refresh.

---

## PASSO 10 — Produção real (2-3 semanas)
**Estudar:** Fase 6 completa (Docker multi-stage, deploy gerenciado, pipeline GitHub Actions, **observabilidade — log estruturado, health check, métrica básica**, `dotnet-trace` introdutório).
**Desenvolver:** deploy real do AuraPOS — primeiro marco de verdade do portfólio inteiro.
**✅ Sinal de conclusão:** sistema no ar, observável, com deploy automático a cada push.

---

## PASSO 11 — Performance com dado real (após meses em produção)
**Estudar:** Fase 6C (`Span<T>`, Garbage Collector, `BenchmarkDotNet`) + Capítulo 9 (Estatística Descritiva — média, mediana, dispersão, interpretação gráfica) do livro, agora com aplicação real: interpretar os números do próprio benchmark.
**Desenvolver:** medir e otimizar o endpoint mais usado do AuraPOS com número real, não achismo.
**✅ Sinal de conclusão:** você tem "antes e depois" medido de uma otimização real.

---

## PASSO 12 — Extração da plataforma interna (Fase 6D, 2-3 semanas) — o ponto de virada do cronograma inteiro
**Estudar:** template `dotnet new` customizado, pacote NuGet privado/GitHub Packages, decisão monorepo vs. polyrepo. Início do Espanhol (Fase A) — o Inglês já deve estar em B1-B2 nesse ponto. Nomear formalmente a metodologia ágil que você já pratica no `EPIC-01` (leitura curta, 1-2h). Começar a estruturar o repositório no GitHub seguindo `[[github-estrutura-profissional-autoridade]]`.
**Desenvolver, extraindo do AuraPOS pronto:**
1. Template de projeto com Clean Architecture + `tenant_id` já configurados
2. `aura-identity` de verdade, a partir do JWT já construído no Passo 4
3. Biblioteca de multi-tenancy reutilizável
4. Pipeline de CI/CD reutilizável (composite action)
5. Component library de frontend com o sistema de tokens de design (RNFT-D01-D07, valores exatos definidos) — extraída das telas dos Passos 4-7, publicada como **Storybook** (Etapa 8 do documento de frontend) via GitHub Pages
6. `aura-notifications` (Grupo 4 — barato de fazer, altíssimo reaproveitamento)
7. `aura-support` (resolve a lacuna repetida em 9 documentos, de uma vez)
8. Publicar a primeira leva de fichas duplas (`[[metodo-estudo-producao-didatica-simultanea]]`) acumuladas desde o Passo 1 — já dá pra montar a primeira apostila piloto
9. Etapas 10-11 do `aurapos-frontend-documento-unico` (Segurança de Frontend — CSP, sanitização, token em cookie `httpOnly`; Lançamento — CDN, invalidação de cache, instrumentação das métricas definidas na Etapa 1.8)

**✅ Sinal de conclusão:** você consegue gerar a estrutura de um sistema novo com um comando, autenticado, com tema aplicado, sem escrever nada disso do zero.

---

## PASSO 13 — Segundo sistema: Aura Delivery (bem mais rápido que o primeiro)
**Estudar:** finalizar Fase 5 (o que não tiver sido consolidado ainda) + reforço de Geometria Analítica/Estruturas Lineares aplicada (Capítulos 13 e 17). Quando chegar no Bloco 3 (roteirização), inicia a Fase 7 (Python + Google OR-Tools) junto com o Capítulo 19 (Análise Combinatória) e Capítulo 20 (Probabilidade, incluindo Bayes) — a conexão mais forte de todo o livro com o portfólio.
**Desenvolver:** Aura Delivery Bloco 1 (pedido + geolocalização via PostGIS), já herdando login, tema, multi-tenancy e CI/CD do Passo 12 — o tempo aqui deveria ser sensivelmente menor que o AuraPOS, porque a fundação já existe.
**✅ Sinal de conclusão:** segundo sistema em produção, medindo quanto tempo real foi economizado versus o primeiro.

---

## PASSO 14 em diante — Terceiro sistema e além, na ordem de prioridade já definida no portfólio
Cada sistema novo segue reaproveitando mais que o anterior. A ordem de prioridade do portfólio (AuraWealth, AuraVet, AuraFix, Momentos/Cupido...) continua valendo — o que muda é que cada um agora começa com a plataforma interna já pronta, não do zero. Vocabulário formal de System Design (estimativa "back-of-envelope", CAP theorem) e preparação de entrevista comportamental (método STAR) entram aqui, perto da hora real de aplicar pra vaga — ver `[[perfil-senior-completo-auditoria]]`.

---

## As trilhas paralelas de longo prazo, que rodam por baixo de tudo isso sem travar nenhum passo acima

- **Fase 7 (Python/OR-Tools) + Capítulos 19-20 do livro (Combinatória/Probabilidade):** só entra quando o Aura Delivery (Passo 13) chegar no bloco de roteirização — não antes, não trava nenhum passo anterior
- **Fase 12 (Pentest/OSCP):** começa depois do Passo 8 (arquitetura consolidada), rodando em paralelo aos passos seguintes, no seu próprio ritmo, sempre em plataforma de treino isolada — nunca contra sistema seu em produção
- **Inglês:** integrado desde o Passo 1 (Fase A), sem bloco de tempo dedicado além do inicial — ver [[ingles-espanhol-integrado]] e [[metodo-correto-estudo-idiomas]]
- **Espanhol:** começa no Passo 12, só depois do Inglês estar em B1-B2
- **Produção didática simultânea:** entrelaçada em toda User Story do `EPIC-01` em diante, acumulando material que vira apostila real no Passo 12 — ver [[metodo-estudo-producao-didatica-simultanea]]
- **Perfil sênior completo (System Design, IaC, code review, entrevista comportamental):** maior parte já coberta pelos passos acima; o que sobra de genuinamente novo entra perto da hora de aplicar pra vaga — ver [[perfil-senior-completo-auditoria]]

---

## Uma frase pra fixar a lógica inteira deste documento

**Cada passo constrói exatamente o que o passo seguinte precisa, na ordem que gera mais reaproveitamento primeiro** — você nunca está "só estudando" nem "só codando", está sempre fazendo as duas coisas na mesma peça de trabalho, e cada peça paga dividendo nos sistemas que vêm depois.


---

## 🔗 Documentos relacionados
- [[biblioteca-recursos-por-passo]] — leitura/vídeo específico pra cada passo, sem precisar procurar sozinho
- [[CARTAO-voce-esta-aqui]] — a versão resumida de "o que fazer hoje"
- [[inventario-portfolio-atualizado]] — o status de cada sistema mencionado nos passos acima
- [[EPIC-01-backlog-passo1-fundamentos]] — o detalhamento em tarefas do Passo 1
