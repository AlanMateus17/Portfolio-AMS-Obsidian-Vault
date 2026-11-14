---
tags: [estudo, portfolio-ams, ponto-de-entrada]
tipo: estudo
status: ativo
atualizado: 2026-10-26
---

# 🎯 Sumário Único de Estudo — O Único Arquivo Que Você Abre

> **Desde 06/11/2026 a porta do dia mudou** ([ADR 0013](11-setup-dev-setup/docs/adr/0013-um-vault-e-o-plano-mestre.md)). No Ubuntu do WSL:
> - **O que estudar hoje:** `cd ~/dev/dev-setup && just professor hoje` · método: [Professor](11-setup-dev-setup/docs/professor/metodo.md) · plano: [Eixo de 12 meses](11-setup-dev-setup/docs/plano-eixo.md) (software + finanças; AM Rendara no 2º trimestre)
> - **O que fazer hoje no setup:** `just agora` · roteiro completo na [pasta 11](11-setup-dev-setup/00-INDICE-DO-SETUP.md), espelho automático do dev-setup
> Este arquivo continua aqui como referência; nada foi apagado.


> **Em palavras simples:** esta é a lista do que **estudar**, em ordem. São 14 Passos; cada um junta programação, matemática e inglês, e termina com um projeto real (o AM Kaixara é o primeiro). Você nunca escolhe o que estudar: é sempre o próximo Passo sem `[x]`. Palavras difíceis: [Glossário](00-GLOSSARIO.md). O caminho completo (estudo + setup + rendas): [Guia do Iniciante](00-GUIA-DO-INICIANTE.md). Cada Passo aparece no [Plano Mestre](00-PLANO-MESTRE-PASSO-A-PASSO.md) com o código `E-P1` a `E-P14`, ligado aos passos do setup que ele destrava.

## 🗺️ Roadmap por fases (execução dos projetos)

A sequência de *execução* das frentes principais, uma por vez. A trilha de *estudo* (Passos, abaixo) roda dentro dela.

| Fase | Quando | Principal | Secundário |
| --- | --- | --- | --- |
| 1 | Out–Dez 2026 | ByteSDCoin em sala + revisão de fim de ano | Mini-curso de Lógica + Instagram |
| 2 | Jan–Mar 2027 | MVP do AM Kaixara (blocos de frontend reusáveis) | 2º infoproduto |
| 3 | Abr–Jun 2027 | AM Rendara + backend am-mentor | Migração do portfólio |
| 4 | Jul–Dez 2027 | AM Rotara + AM Taskoro + site Grupo AMtech | Início do freelance |
| Fila 2028+ | — | Demais sistemas, Instituto AMS completo, certificações de segurança | — |

**Regra de foco:** no máximo 1 principal + 1 secundário por fase. O resto fica em fila, pausado de propósito.

> **Renda extra roda por fora desta tabela, desde já:** aulas particulares, manutenção de PC e sites com manutenção mensal (definidos em out/2026). Elas pagam as contas enquanto as fases andam — ver [00-PLANO-UNIFICADO](00-PLANO-UNIFICADO.md) Eixo 2.

### 🎓 Formação acadêmica (roda por fora da Trilha Principal)
ADS ✅ → **Licenciatura em Matemática** (em curso) → **Ciências Econômicas** 🆕 e **faculdade para IA** (Ciência da Computação ou bacharelado em IA), em ordem a decidir. Sem pós-graduação e sem faculdade de engenharia de software (autodidata). Certificações do setor de investimentos (CPA, CNPI, CGA, CFA) e o que fica só no autodidata: [formacao-academica](07-estudo-e-carreira/formacao-academica.md).

**Removidos do estudo em out/2026:** concurso PF/PRF (e o direito ligado a ele) · desenho · violão · pós em Cybersecurity e em Arquitetura de Software.

### 🔒 Gate de segurança ↔ Linux
A parte de segurança ([roadmap-seguranca-ofensiva-completo](07-estudo-e-carreira/roadmap-seguranca-ofensiva-completo.md)) só avança com a fase da [trilha-linux-arch-profissional](07-estudo-e-carreira/trilha-linux-arch-profissional.md) concluída:
- Linux F1 + Segurança S1 (juntas) → Bandit · faça [trilha-de-redes](07-estudo-e-carreira/trilha-de-redes.md) cedo
- Linux F2 → S2 (redes p/ pentest) · F3–4 → S3 (testar o próprio Aura) · F5–6 → S4 (escalada) · F8 → S5 (lab Kali) → Windows/AD → baixo nível
- **Regra de ouro:** nunca abrir uma fase de segurança sem o gate de Linux fechado.

---
### Ponto de entrada único. Uma trilha, uma numeração, sem bifurcação.

> **Por que este documento existe:** você tinha 3 documentos tentando ser "a sequência oficial" ([mapa-mestre-prioridade-total](99-arquivo/mapa-mestre-prioridade-total.md), [sequencia-mestra-completa-desde-o-inicio](99-arquivo/sequencia-mestra-completa-desde-o-inicio.md), [passo-a-passo-mestre-desde-o-inicio](99-arquivo/passo-a-passo-mestre-desde-o-inicio.md)), com duas numerações diferentes ("Bloco" e "Passo") que não se encaixavam 1-pra-1. Este arquivo resolve isso: junta a clareza de prioridade do mapa-mestre com o detalhe acionável do passo-a-passo-mestre, numa numeração só (**Passo**), sem repetir o mesmo conteúdo em três lugares.
>
> Os três documentos originais continuam existindo no vault — não foram apagados nem alterados — mas a partir de agora você só precisa abrir **este arquivo** no dia a dia. Eles ficam como referência de detalhe profundo, não como algo que você precisa consultar pra saber "o que vem agora".

---

## ➕ Como adicionar conteúdo novo a este sumário

Quando surgir um assunto novo pra estudar (tecnologia nova, livro novo, trilha que não existia):

1. Me diga o assunto e, se souber, onde ele parece se encaixar (ex: "isso é matemática, entra depois do Passo 9" ou "é uma trilha nova, tipo um 4º item de Trilha Paralela").
2. Decidimos juntos o tipo de encaixe:
   - **Cabe dentro de um Passo existente** → vira uma linha a mais em "Estudar" ou "Desenvolver" daquele Passo, sem criar Passo novo.
   - **É grande o bastante pra merecer bloco próprio** → vira um novo Passo, deslocando a numeração dos seguintes.
   - **É longo e contínuo, sem travar a Trilha Principal** → vira uma nova linha na tabela de Trilhas Paralelas, mesmo tratamento da Trilha 42/Pentest.
3. **Só este arquivo muda.** Os documentos-fonte antigos ([sequencia-mestra-completa-desde-o-inicio](99-arquivo/sequencia-mestra-completa-desde-o-inicio.md), [mapa-mestre-prioridade-total](99-arquivo/mapa-mestre-prioridade-total.md), [passo-a-passo-mestre-desde-o-inicio](99-arquivo/passo-a-passo-mestre-desde-o-inicio.md)) não são mais tocados no dia a dia — se o assunto novo precisar de detalhe profundo, criamos um documento novo só pra ele e linkamos aqui, sem inflar este sumário.
4. Você não precisa reorganizar nada sozinho — só avisar o assunto novo.

---

## 🔀 Como alternar de assunto dentro de um mesmo Passo (pra não misturar tudo de uma vez)

Cada Passo lista mais de um assunto (Portfólio + Matemática + Idioma, às vezes Física) porque intercalar assuntos é comprovadamente melhor pra reter — mas intercalar não é misturar no mesmo bloco de tempo. Dentro de cada sessão de estudo, siga sempre esta ordem fixa:

1. **Comece pelo item de Portfólio/Desenvolvimento** do Passo atual — é o que exige mais memória de trabalho ativa; faça com a cabeça mais fresca.
2. **PARE** ao fechar o "Desenvolver" do dia (não precisa terminar o Passo inteiro numa sessão só). Feche o editor de código **antes** de abrir o livro de matemática — nunca os dois ao mesmo tempo.
3. **Troque para Matemática** (ou Física, quando entrar) — o capítulo já está indicado no mesmo Passo.
4. **PARE** ao fechar o capítulo/exercício do dia.
5. **Troque para Inglês/Espanhol** (Anki + fonte técnica em inglês, se já estiver na fase B) — é o item mais leve, funciona bem como o último bloco da sessão.
6. Só depois de passar pelos assuntos que aquele Passo tiver (nem todos têm os 3), aplique o **Protocolo de Fim de Bloco** abaixo — uma vez, sobre a sessão inteira, não um por assunto.

Isso não é regra rígida de tempo — é a ordem de troca, sempre a mesma, pra você nunca precisar decidir "e agora o quê" no meio da sessão.

---

## 🧭 A única regra que importa

**Se você não sabe o que fazer agora, é sempre o próximo Passo não marcado da Trilha Principal, mais abaixo.** Nunca precisa adivinhar, nunca precisa abrir um segundo arquivo pra confirmar. Marque `[x]` conforme for terminando cada um.

---

## 📍 Onde você está agora

- [ ] **Passo 1** — em andamento (Sprint 1 do [EPIC-01-backlog-passo1-fundamentos](07-estudo-e-carreira/EPIC-01-backlog-passo1-fundamentos.md), User Story atual)

*(atualize esta linha manualmente conforme for avançando — é o seu "você está aqui" permanente)*

---

## 🧠 Antes de CADA Passo: o mesmo protocolo de 15-30min, sem exceção

Isso vale pra todo Passo da Trilha Principal e todo bloco de qualquer Trilha Paralela. Não é opcional — é o que transforma "eu vi isso uma vez" em "eu sei isso" (detalhe completo e a ciência por trás: [metodo-de-estudo](07-estudo-e-carreira/metodo-de-estudo.md)).

```
1. FECHE o material (código, vídeo, livro) — não olhe mais
2. RECONSTRUA de cabeça: o que esse Passo resolveu, e por quê daquele jeito
3. ENSINE em 3-5 frases simples, sem jargão — vira Ficha Dupla (curso) e Registro
   de Entrevista (vaga), os dois no [00-catalogo-progresso](09-material-producao-simultanea/00-catalogo-progresso.md) — não é opcional,
   é o mesmo raciocínio do passo 2, só formatado duas vezes
4. ANKI: 1-3 cartões do que valeu a pena fixar
5. REGISTRE quanto tempo o Passo realmente levou, vs. a estimativa abaixo
6. SÓ ENTÃO marque [x] e avance pro próximo
```

*(Antes de abrir o editor pra codar o "Desenvolver" de um Passo novo, registre a pasta/repositório no [00-catalogo-progresso](09-material-producao-simultanea/00-catalogo-progresso.md) — é o que mantém o código sempre rastreável até o Passo que o gerou, sem precisar procurar depois.)*

*(detalhe completo dos dois formatos de artefato: [metodo-de-estudo](07-estudo-e-carreira/metodo-de-estudo.md))*

---

## 🛤️ TRILHA PRINCIPAL — sempre o próximo item aqui, nunca pule

> **Tudo o que um desenvolvedor sênior domina, em todas as camadas, está no [Currículo Completo do Desenvolvedor Sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md).** Cada Passo abaixo tem uma linha **🧱 Stack completa** apontando para a parte do currículo que entra nele.

Cada Passo já junta estudo + desenvolvimento + matemática + idioma no mesmo bloco de tempo — você nunca "só estuda" ou "só codifica" separadamente.

- [ ] **Passo 1 — Lógica + Matemática Parte I + Inglês (início)** *(2-3 semanas)*
  Lógica de programação (variável, condicional, laço, função, coleção) junto com Matemática Cap. 1-2 (Linguagem Matemática, Teoria dos Conjuntos). Inglês Fase A começa em paralelo.
  **Desenvolver:** 3 exercícios de lógica pura (carrinho com desconto, escada de inadimplência, rebalanceamento ARCA simplificado).
  **✅ Pronto quando:** resolve os três exercícios sem travar.

- [ ] **Passo 2 — Git, SQL, Docker** *(1-2 semanas)*
  Git, SQL/PostgreSQL (`EXPLAIN ANALYZE`), Docker.
  **🧱 Stack completa:** Git avançado (rebase, `bisect`, conventional commits), modelagem e normalização, `JOIN`s, CTE, window functions, Docker Compose, Bash e PowerShell básicos — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §2.5, §5, §10.
  **Desenvolver:** schema real do AM Kaixara (produto, categoria, estoque, venda) + schema do `aura-licensing`.
  **✅ Pronto quando:** lê um `EXPLAIN ANALYZE` e identifica full scan; ambiente sobe com `docker-compose up`.
  **🤖 Automação que entra aqui:** pre-commit hook (Gitleaks) + Dependabot + backup agendado de `C:\dev\` — ver [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md).

- [ ] **Passo 3 — C# Fundamentals + TypeScript + Matemática Parte II (início)** *(2-3 semanas)*
  Tipo, classe, coleção, LINQ, nullable reference type, `async/await`, DI + Matemática Cap. 3 (Naturais/Inteiros, Algoritmo de Euclides).
  **🧱 Stack completa:** `record`, pattern matching, genéricos, `CancellationToken`; **JavaScript moderno e TypeScript** (closures, event loop, Promises, tipos, narrowing, genéricos, `strict`); estruturas de dados e Big-O. **🐍 Começa o bloco paralelo de Python** (1–2 h/semana, refazendo os exercícios do Passo em Python) — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §1, §2.1–2.3.
  **Desenvolver:** entidades `Product`/`Category`/`Sale` + Algoritmo de Euclides implementado. Todo valor em dinheiro como `decimal`, nunca `double` ([engenharia de sistemas financeiros](07-estudo-e-carreira/trilha-engenharia-software.md)).
  **✅ Pronto quando:** entidades compilam sem warning de nulo; Euclides testado.

- [ ] **Passo 4 — API, Autenticação e Frontend base** *(3-4 semanas)*
  Rota, DTO, validação, JWT, OWASP Top 10, rate limiting + Matemática Cap. 4 (Aritmética Modular/RSA). Inglês Fase B começa.
  **🧱 Stack completa — backend:** pipeline e middleware do ASP.NET Core, **Controllers** (escolha fixa, não Minimal API), DI e ciclos de vida, Options pattern, validação, `ProblemDetails`, OpenAPI, design REST (status, paginação, versionamento), rate limiting. **Frontend:** HTML semântico e acessibilidade (WCAG AA), CSS (Flexbox, Grid, responsivo), **Tailwind** com os tokens do Aura, **React** (componentes, props, estado, hooks) e **Next.js App Router** (layouts, Server × Client Components) — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §3, §4.1–4.3.
  **Desenvolver:** `tenant_id`+RLS → login JWT/BCrypt (AM Kaixara RF01) → controle de acesso por papel (RF02) → blindagem OWASP. Frontend: Design System (tokens reais) + tela de login.
  **✅ Pronto quando:** login funcional, protegido, com tela real usando os tokens corretos.

- [ ] **Passo 5 — EF Core + CRUD molde** *(1-2 semanas)*
  Migration, relacionamento, `AsNoTracking`, N+1 + Matemática Cap. 5-8 (Racionais, Aplicações Aritméticas, Sequências, Reais).
  **🧱 Stack completa:** EF Core a fundo (tracking, `Include` e N+1, consultas compiladas, quando usar Dapper), níveis de isolamento e locks; React Hook Form + Zod com o mesmo contrato da API; cliente TypeScript gerado do OpenAPI — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §4.2, §5.
  **Desenvolver:** CRUD de produto/categoria (RF03, o "molde") → `RowVersion`/RNFT-E01 (não adiar) → reserva de estoque (RF11). Frontend: TanStack Query + Zustand, tabela genérica, formulário genérico.
  **💹 Finanças (leve):** começa F1 Contabilidade (partidas dobradas, caixa × competência) e F2 Matemática financeira junto do Cap. 6 do Lins — [trilha-financas-economia](07-estudo-e-carreira/trilha-financas-economia.md).
  **✅ Pronto quando:** CRUD funciona com teste de concorrência passando.

- [ ] **Passo 6 — Teste como disciplina** *(1-2 semanas)*
  Pirâmide de teste, `Moq`, teste de integração, TDD + Testing Library/Playwright.
  **🧱 Stack completa:** **xUnit**, Moq, `WebApplicationFactory` + **Testcontainers** (PostgreSQL e Redis reais), Vitest + Testing Library, **Playwright**, pytest no bloco Python, CodeQL — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §8.
  **Desenvolver:** teste do fluxo de venda (unitário + integração) + teste de componente do carrinho + E2E completo. TDD puro no `aura-goals`.
  **✅ Pronto quando:** cobertura real no fluxo de venda, backend e frontend.
  **🤖 Automação que entra aqui:** CI completo (build + teste a cada push) + CodeQL — ver [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md).

- [ ] **Passo 7 — Fechar o AM Kaixara: pagamento e cobrança** *(2-3 semanas)*
  Aplicação do que já foi estudado, sem tópico novo formal.
  **🧱 Stack completa — agente local do Kaixara:** Windows Service em .NET, **SQLite offline** com fila de sincronização, periféricos atrás de interfaces (impressora ESC/POS, gaveta, balança, TEF), testes de propriedade nas regras de dinheiro — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §13.
  **Desenvolver:** múltiplos meios de pagamento (RF04) → idempotência/RNFT-E02 → abertura/fechamento de caixa (RF05) → cancelamento com restauração (RF06). Frontend: dashboard + checkout.
  **💹 Finanças:** fechamento de caixa gera lançamentos em **partidas dobradas** + DRE simples por consulta SQL (F1). Começa F3 Tributação (o que NFC-e/NF-e exigem, para o `IEmissorFiscal`).
  **✅ Pronto quando:** AM Kaixara com fluxo de venda ponta a ponta, pagamento idempotente, ledger fechando em zero.

- [ ] **Passo 8 — Arquitetura de verdade** *(contínuo, consolida aqui)*
  SOLID, Design Patterns, Clean Architecture, DI ligada à arquitetura.
  **🧱 Stack completa:** design patterns por categoria, refatoração (Fowler), **DDD tático** (entidade, objeto de valor, agregado, evento de domínio), diagramas C4, modelagem de ameaças STRIDE; começa a prática de algoritmos de entrevista — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §6, §9, §15.
  **Desenvolver:** refatorar o AM Kaixara aplicando cada padrão nele mesmo (`IFonteDeEstoque`, `IEmissorFiscal`).
  **✅ Pronto quando:** você refatora uma classe e explica por que segue SOLID.

  > 🔓 **A partir daqui destravam as Trilhas Paralelas** (Finanças F4+, Dados & IA, Trilha 42, Pentest/OSCP) — ver seção abaixo. Elas rodam por baixo dos Passos 9+ sem bloquear nada, **uma de cada vez**.

- [ ] **Passo 9 — Ponte técnica pro próximo sistema** *(após MVP do AM Kaixara)*
  PostGIS, Redis, SignalR, PWA vs. nativo + Matemática Cap. 13 e 17 (Estruturas Lineares, Geometria Analítica — cobre o que seria "Álgebra Linear I"). Inglês Fase C (ADR/README em inglês).
  **🧱 Stack completa:** padrões de cache e invalidação, **Redis Streams** como fila, consumidor idempotente, resiliência (Polly: retry, timeout, circuit breaker), `BackgroundService`, SignalR com backplane Redis, PWA e offline — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §3, §5, §7.
  **Desenvolver:** cache Redis no AM Kaixara + SignalR no dashboard.
  **✅ Pronto quando:** dashboard atualiza em tempo real sem refresh.

- [ ] **Passo 10 — Produção real** *(2-3 semanas)*
  Docker multi-stage, deploy gerenciado, pipeline GitHub Actions, observabilidade.
  **🧱 Stack completa:** Docker multi-stage sem root, Linux de servidor, **OpenTelemetry** (logs, métricas, traces), health checks, migração de banco sem parar o sistema (expandir e contrair), estratégias de deploy e rollback, backup com teste de restauração, instalador assinado do agente local — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §10, §11.
  **Desenvolver:** deploy real do AM Kaixara — primeiro marco de verdade do portfólio.
  **✅ Pronto quando:** sistema no ar, observável, deploy automático a cada push.
  **🤖 Automação que entra aqui:** CD completo, Uptime Kuma, backup de banco de produção com teste de restauração, [aura-secrets](10-ferramentas-pessoais/aura-secrets-documento-projeto-final.md) — ver [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md).

- [ ] **Passo 11 — Performance com dado real** *(após meses em produção)*
  `Span<T>`, Garbage Collector, `BenchmarkDotNet` + Matemática Cap. 9 (Estatística Descritiva).
  **🧱 Stack completa:** dotnet-trace/counters, flame graphs, `ArrayPool`, plano de execução e índices, Core Web Vitals e React Profiler no frontend — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §12.
  **Desenvolver:** medir e otimizar o endpoint mais usado, com número real.
  **✅ Pronto quando:** tem "antes e depois" medido de uma otimização real.
  **🤖 Automação que entra aqui:** teste de carga (k6) — ver [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md).

- [ ] **Passo 12 — Extração da plataforma interna** *(2-3 semanas — ponto de virada do cronograma)*
  Template `dotnet new`, NuGet privado, monorepo vs. polyrepo. Espanhol Fase A começa (Inglês já em B1-B2). Nomear a metodologia ágil já praticada.
  **Desenvolver, extraindo do AM Kaixara pronto:** template Clean Architecture+`tenant_id` → `aura-identity` real → lib de multi-tenancy → CI/CD reutilizável → component library (Storybook) → `aura-notifications` → `aura-support` → primeira apostila piloto (fichas duplas acumuladas) → segurança de frontend + lançamento (CDN, cache, métricas).
  **🧱 Stack completa:** **DDD estratégico** (contextos delimitados entre os sistemas Aura), CQRS, **outbox** e saga, **OAuth 2.0/OIDC** no `aura-identity`, Storybook, teste de contrato, TypeScript avançado — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §3, §6, §7, §8.
  **✅ Pronto quando:** gera a estrutura de um sistema novo com um comando, autenticado, com tema, sem escrever do zero.
  **🤖 Automação que entra aqui:** Infraestrutura como código (Terraform) + pipeline CI/CD reutilizável + MkDocs publicado — ver [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md).

- [ ] **Passo 13 — Segundo sistema: AM Rotara** *(bem mais rápido que o primeiro)*
  Reforço de Geometria Analítica/Estruturas Lineares. No bloco de roteirização: Python + OR-Tools + Matemática Cap. 19-20 (Combinatória, Probabilidade/Bayes). Se a Trilha de Dados & IA já passou do IA0, o Python já está pronto.
  **Desenvolver:** AM Rotara Bloco 1 (pedido + geolocalização via PostGIS), já herdando login/tema/multi-tenancy/CI-CD do Passo 12.
  **✅ Pronto quando:** segundo sistema em produção — meça quanto tempo real foi economizado vs. o primeiro.

- [ ] **Passo 14 em diante — Terceiro sistema e além**
  Ordem de prioridade do portfólio (AM Rendara — puxa F4/F5 da Trilha de Finanças, conciliação e Pix —, AuraVet, AM Consertta, Momentos/Cupido, Loja Virtual, AM Predara, AM Canteira, AM Saberia, AM Horaria, AM Projeta...). Cada sistema novo reaproveita mais que o anterior — a fundação já existe. System Design formal e preparação de entrevista (STAR) entram perto da hora real de aplicar pra vaga.
  **🎯 Fase sênior (roda junto do Passo 14+):** system design de entrevista, SLI/SLO e postmortem, Kubernetes (noção sólida), conceitos de RabbitMQ/Kafka, réplica de leitura e particionamento, mutation testing, inglês técnico C1 e entrevista em inglês — [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §7, §10, §11, §15.
  **Clojure/Datomic** (`aura-historico`): só entra aqui, quando o Rendara precisar do histórico — ou sai, se você trocar por Event Sourcing com Marten em .NET (pendência abaixo).
  **✅ Critério de entrada do AM Taskoro** *(22º sistema, GraphQL híbrido via HotChocolate — .NET, não stack separada)*: quando 2-3 sistemas principais já estiverem em produção e a Trilha 42 estiver avançada — ver Trilhas Paralelas abaixo.

---

## 🧵 TRILHAS PARALELAS — começam num gatilho, nunca bloqueiam a Principal, nunca são esquecidas

Reserve um bloco fixo por semana pra elas (ex: 2 das suas 9h) sem deixar a Trilha Principal comer esse espaço.

**Regra nova (out/2026): uma Trilha Paralela pesada ativa por vez.** Com quatro trilhas destravando no mesmo gatilho (Passo 8), rodar todas juntas dilui cada uma até nenhuma andar. Ordem sugerida, alinhada ao objetivo de sistemas financeiros: **Finanças F4–F5 → Dados & IA (IA0–IA3) → Trilha 42 → Pentest/OSCP**. Os módulos leves (Finanças F0–F3, Robótica R1, Espanhol, Física) não contam nesse limite. A ordem é decisão sua — mude aqui se preferir outra.

| Trilha | Começa em | Duração estimada | Documento de detalhe |
|---|---|---|---|
| **💹 Finanças e Economia** — F0–F3 leves agora; F4+ paralela pesada | F0 já · F1–F2 no Passo 5 · F3 no Passo 7 · F4+ depois do Passo 8 | Contínua (F4–F5: ~4-6 meses) | [trilha-financas-economia](07-estudo-e-carreira/trilha-financas-economia.md) |
| **🤖 Dados e IA** — Python → ML → deep learning → LLMs → fine-tuning 8B | Depois do Passo 8 | IA0–IA3: ~6-9 meses · IA4–IA7: +1 ano | [trilha-dados-ia](07-estudo-e-carreira/trilha-dados-ia.md) |
| **🐍 Python em paralelo** — base, idiomático, pytest, FastAPI; refaz em Python os exercícios de cada Passo | Passo 3 | Contínuo, 1–2 h/semana | [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) §2.3 |
| **🏗️ Engenharia de Software** — não é trilha nova: é o mapa da Trilha Principal por área + engenharia de sistemas financeiros. O detalhe técnico completo de cada camada está no [currículo sênior](07-estudo-e-carreira/curriculo-dev-senior-completo.md) | Já (é a própria Trilha Principal) | — | [trilha-engenharia-software](07-estudo-e-carreira/trilha-engenharia-software.md) |
| **🔧 Robótica e IoT** — R1 ativo pelo projeto agro da escola | R1 já · resto com gatilho | — | [trilha-robotica-iot](07-estudo-e-carreira/trilha-robotica-iot.md) |
| **Trilha 42** — Circles 00-06, sua stack primeiro depois nativo C/C++ | Depois do Passo 8 | ~7-12 meses ⚠️ | [trilha-42-circles-oficial-verificado](07-estudo-e-carreira/trilha-42-circles-oficial-verificado.md) (é a versão corrigida — use esta, não a contagem citada em outros arquivos) |
| **Pentest/OSCP** | Depois do Passo 8 (mesmo gatilho da Trilha 42) | 1-2 anos | [roadmap-seguranca-ofensiva-completo](07-estudo-e-carreira/roadmap-seguranca-ofensiva-completo.md), [recursos-links-seguranca-ofensiva](07-estudo-e-carreira/roadmap-seguranca-ofensiva-completo.md) |
| **Espanhol** | Passo 12 (Inglês já em B1-B2) | Mais rápido que o Inglês | [ingles-espanhol-integrado](07-estudo-e-carreira/ingles-espanhol-integrado.md) |
| **Python + OR-Tools** | Passo 13, no bloco de roteirização | 5-7 semanas | detalhe dentro do próprio Passo 13 acima |
| **Perfil sênior** (System Design, IaC) | Depois do Passo 12 | Pontual, não bloco longo | [perfil-senior-completo-auditoria](07-estudo-e-carreira/perfil-senior-completo-auditoria.md) |
| **AM Taskoro** (GraphQL/HotChocolate híbrido — .NET, 22º sistema) | Passo 14+, quando 2-3 sistemas em produção e Trilha 42 avançada | 2-3 meses (mais rápido que antes — sem stack nova pra aprender) | [taskoro-documento-projeto-final](02-sistemas-de-negocio/taskoro-documento-projeto-final.md) |
| **Física básica** | Desde o Passo 1, em paralelo | — | ⚠️ estrutura provisória — trilha só fecha de verdade quando você comprar o livro e eu vir o sumário real |

---

## 🔁 HÁBITOS CONTÍNUOS — sem prazo, só manter (começam já, nunca terminam)

| Hábito | Frequência | Detalhe |
|---|---|---|
| **roadmap.sh** — auditoria cruzada | Início de cada Passo grande (3, 8, 9, 10) | [integracao-42-roadmap-akita](07-estudo-e-carreira/trilha-42-circles-oficial-verificado.md) |
| **Fábio Akita** (blog/YouTube/podcast) | 1 conteúdo/semana | [integracao-42-roadmap-akita](07-estudo-e-carreira/trilha-42-circles-oficial-verificado.md) |
| **Produção didática simultânea** (ficha dupla) | A cada tópico novo de matemática+código | [metodo-de-estudo](07-estudo-e-carreira/metodo-de-estudo.md) |
| **`aura-status`** — rodar o painel central | Toda segunda-feira (ou depois de qualquer deploy) | [aura-status-documento-projeto-final](10-ferramentas-pessoais/aura-status-documento-projeto-final.md), rotina completa em [automacao-ordem-de-execucao](06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md) |
| **Anki** (repetição espaçada) | Diário, 10-20 min | [metodo-correto-estudo-idiomas](07-estudo-e-carreira/ingles-espanhol-integrado.md) |
| **Finanças pessoais e investimentos (F0)** — Finclass + revisão da carteira pelos métodos ARCA/Barsi/Bazin/Graham/Buffett | 1 bloco/semana + revisão mensal no Caixa da Casa | [trilha-financas-economia](07-estudo-e-carreira/trilha-financas-economia.md) §F0 |
| **Administração e negócios (F7)** — precificação, vendas, funil | Doses pequenas, puxadas pela renda extra | [trilha-financas-economia](07-estudo-e-carreira/trilha-financas-economia.md) §F7 |

---

## 💤 SÓ QUANDO CHEGAR A HORA — não adiante, mesmo parecendo produtivo

| Item | Só ativa quando |
|---|---|
| Apresentação de portfólio, entrevista STAR | Perto de aplicar pra vaga de verdade |
| Certificação formal de inglês (TOEFL/IELTS) | Só se for aplicar pra vaga internacional |
| GitHub — organização, ADR, GitHub Pages | A partir do Passo 12 |

---

## ⚠️ Pendências reais que este sumário não esconde

- **Quando matricular na Economia:** duas graduações EAD juntas consomem todo o tempo de estudo de hoje. Opções e recomendação em [formacao-academica](07-estudo-e-carreira/formacao-academica.md).
- **Ordem das Trilhas Paralelas** (Finanças → IA → 42 → Pentest): sugestão, não decisão — confirme ou troque.

- **Física:** sem sumário real do livro ainda — quando comprar, me mostre o índice e eu reconstruo essa trilha com precisão.
- **Contagem de projetos da 42 inconsistente entre documentos-fonte** (você vai ver "29", "25 entregáveis + 5 Exam Rank" e "24" em arquivos diferentes do vault) — [trilha-42-circles-oficial-verificado](07-estudo-e-carreira/trilha-42-circles-oficial-verificado.md) é o mais recente e corrigido; use ele como fonte de verdade até os outros arquivos serem atualizados.
- **`aura-historico` (Clojure/Datomic)** — mesma pergunta que revisou o AM Taskoro ainda em aberto aqui: Event Sourcing com Marten (.NET/PostgreSQL) resolveria o mesmo problema sem sair da stack. Diferente do AM Taskoro, o motivo original parece ser diversificação de paradigma (funcional/imutável), não só resolver o problema — decisão seguinte, sua, não corrigida automaticamente.

---

## 🔗 Onde cada coisa mora, se você precisar do detalhe fundo (não pro dia a dia)

- [00-catalogo-progresso](09-material-producao-simultanea/00-catalogo-progresso.md) — onde o código de cada Passo/sistema mora de verdade, local e no GitHub
- [metodo-de-estudo](07-estudo-e-carreira/metodo-de-estudo.md) — a ciência completa por trás do protocolo acima
- [passo-a-passo-mestre-desde-o-inicio](99-arquivo/passo-a-passo-mestre-desde-o-inicio.md) — mesma trilha principal, com texto mais longo por Passo
- [mapa-mestre-prioridade-total](99-arquivo/mapa-mestre-prioridade-total.md) — mesma priorização, no formato original P0/P1/P2/P3
- [sequencia-mestra-completa-desde-o-inicio](99-arquivo/sequencia-mestra-completa-desde-o-inicio.md) — mesma trilha, com a Trilha 42 intercalada bloco a bloco dentro da numeração
- [EPIC-01-backlog-passo1-fundamentos](07-estudo-e-carreira/EPIC-01-backlog-passo1-fundamentos.md) — as tarefas reais do Passo 1, em User Stories
- [automacao-o-que-e-por-que](06-execucao-e-desenvolvimento/automacao-o-que-e-por-que.md) — o que automatizar em cada Passo, documento único de referência

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Revisão do Vault de Estudos](12-artefatos/paginas/revisao-do-vault-de-estudos-udq7/index.html) · página interativa · [sobre](12-artefatos/paginas/revisao-do-vault-de-estudos-udq7/LEIA-ME.md)
- [Plano de Estudos de Inglês — 6º ano ao 3º EM](12-artefatos/documentos/plano-de-estudos-de-ingles-6o-ano-ao-3o-em.md)
- [Plano de Estudos de Espanhol — A1 ao C2](12-artefatos/documentos/plano-de-estudos-de-espanhol-a1-ao-c2.md)
- [Trilha de Redes](12-artefatos/documentos/trilha-de-redes.md)
- [Trilha Linux/Arch Profissional](12-artefatos/documentos/trilha-linux-arch-profissional.md)
- [Trilha de Cibersegurança e Pentest](12-artefatos/documentos/trilha-de-ciberseguranca-e-pentest.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
