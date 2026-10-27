---
tags: [estudo, senior, engenharia-de-software, stack, portfolio-ams]
tipo: curriculo
status: ativo
atualizado: 2026-10-26
---

# 🧭 Currículo Completo do Desenvolvedor Sênior — Todas as Camadas e Etapas

> **Em palavras simples:** esta é a lista **completa** do que um programador sênior sabe, dividida em 15 áreas. Ela é grande de propósito: serve para conferir que nada ficou de fora, não para estudar de uma vez. A ordem de estudo é a do [Sumário Único](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md); cada linha diz em qual Passo entra. Termos: [Glossário](../00-GLOSSARIO.md).

> **O que este documento é:** a lista completa do que você precisa dominar tecnicamente para ser **desenvolvedor sênior** na sua stack (C#/.NET 10 + TypeScript/Next.js + PostgreSQL/Redis + Docker, com Python em paralelo), no Brasil e no exterior. Cobre **todas as camadas** (fundamentos, backend, frontend, dados, arquitetura, infraestrutura, segurança, qualidade, produção) e **todas as etapas** (requisitos → design → código → teste → deploy → operação → evolução).
>
> **Como usar:** você **não** estuda este documento de cima para baixo. A ordem continua sendo a do [Sumário Único](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md). Cada item aqui diz **em qual Passo** entra (coluna "Onde"). Use este documento para três coisas:
> 1. **Auditoria:** no início de cada Passo, abra a camada correspondente e veja se nada ficou de fora.
> 2. **Critério de sênior:** cada camada termina com "**Sênior quando…**" — é o teste de que você domina, não de que estudou.
> 3. **Preparação de entrevista:** a seção 15 lista o que é cobrado em vaga sênior, inclusive no exterior.
>
> **Legenda da coluna "Onde":** `P1`–`P14` = Passos do Sumário · `Py` = bloco paralelo de Python · `IA` = [trilha-dados-ia](trilha-dados-ia.md) · `42` = [École 42](trilha-42-circles-oficial-verificado.md) · `Lx` = [trilha Linux](trilha-linux-arch-profissional.md) · `Red` = [trilha de redes](trilha-de-redes.md) · `Seg` = [roadmap de segurança](roadmap-seguranca-ofensiva-completo.md) · `Fin` = [trilha de finanças](trilha-financas-economia.md) · `HL` = [horizonte longo](mapa-horizonte-longo-sistemas.md) · `Sr` = fase sênior (depois do P12)

---

## Índice das camadas

| # | Camada | Etapa do ciclo |
|---|---|---|
| 1 | Fundamentos de computação | Base de tudo |
| 2 | Linguagens: C#, TypeScript, Python, SQL, shell | Construção |
| 3 | Backend .NET e ASP.NET Core | Construção |
| 4 | Frontend: HTML, CSS, JavaScript, TypeScript, React, Next.js | Construção |
| 5 | Banco de dados e dados | Construção e operação |
| 6 | Design e arquitetura de software | Design |
| 7 | Sistemas distribuídos, mensageria e integração | Design e construção |
| 8 | Qualidade e testes | Verificação |
| 9 | Segurança de aplicação | Todas |
| 10 | Infraestrutura, DevOps e cloud | Entrega |
| 11 | Observabilidade e operação em produção | Operação |
| 12 | Performance e escalabilidade | Operação e evolução |
| 13 | Software de desktop e dispositivo (agente local do Kaixara) | Construção |
| 14 | Processo, requisitos e colaboração | Todas |
| 15 | Competências de sênior e carreira internacional | Todas |

---

## 1. Fundamentos de computação

| Tópico | O que dominar | Onde |
|---|---|---|
| Lógica e algoritmos | Variável, condicional, laço, função, recursão; pensamento algorítmico | P1 |
| Complexidade | Big-O de tempo e espaço; melhor/pior/médio caso; amortizado | P3 · 42 |
| Estruturas de dados | Array, lista ligada, pilha, fila, deque, hash table (colisão, load factor), árvore binária de busca, árvore balanceada (noção de AVL/rubro-negra), heap, trie, grafo (lista e matriz de adjacência) | P3 · 42 |
| Algoritmos clássicos | Ordenação (merge, quick, heap, counting), busca binária, BFS/DFS, Dijkstra, ordenação topológica, programação dinâmica, guloso, backtracking, dois ponteiros, janela deslizante | P3–P8 · 42 |
| Matemática para computação | Lógica, conjuntos, indução, teoria dos números (Euclides, aritmética modular, RSA), combinatória, probabilidade, álgebra linear | P1–P13 (livro do Lins) |
| Como o computador funciona | CPU, registradores, cache L1/L2/L3, memória, stack × heap, representação binária, ponto flutuante IEEE 754 (por que `0.1 + 0.2 != 0.3`) | P3 · 42 · HL |
| Sistemas operacionais | Processo, thread, escalonamento, memória virtual, sistema de arquivos, syscalls, I/O bloqueante × não bloqueante | Lx · HL |
| Concorrência | Condição de corrida, deadlock, mutex, semáforo, atomicidade, memória compartilhada × troca de mensagens | P5 · P9 |
| Redes | Modelo TCP/IP, IP, TCP × UDP, DNS, HTTP/1.1, HTTP/2, HTTP/3, TLS, portas, NAT, proxy, balanceador | Red · P10 |
| Compiladores e runtimes (noção) | Compilação × interpretação × JIT, bytecode/IL, garbage collector | P11 · HL |

**Sênior quando…** escolhe a estrutura de dados certa sem pensar, explica o custo de cada operação e resolve problemas de entrevista de nível médio em 30–40 minutos falando em voz alta.

---

## 2. Linguagens

### 2.1 C# (linguagem principal)
| Tópico | O que dominar | Onde |
|---|---|---|
| Base | Tipos de valor × referência, `struct` × `class` × `record`, nullable reference types, pattern matching, switch expressions | P3 |
| Coleções e LINQ | `List`, `Dictionary`, `HashSet`, `IEnumerable` × `IQueryable`, execução adiada, custo de cada operador | P3 · P5 |
| Orientação a objetos | Encapsulamento, herança × composição, interfaces, classes abstratas, polimorfismo | P3 · P8 |
| Genéricos | Restrições (`where`), covariância e contravariância | P3 · P8 |
| Assíncrono | `Task`, `async/await`, `ValueTask`, `CancellationToken`, `ConfigureAwait`, armadilhas (`async void`, `.Result`, deadlock), `IAsyncEnumerable`, `Channel<T>` | P3 · P9 |
| Memória | `Span<T>`, `Memory<T>`, `stackalloc`, alocação e pressão no GC, `IDisposable` e `using` | P11 |
| Recursos modernos | `required`, `init`, primary constructors, collection expressions, records imutáveis | P3 |
| Exceções | Quando lançar, quando retornar resultado (`Result`), filtros de exceção | P4 |
| Reflection e geração de código | Atributos, reflection (custo), source generators (noção) | P12 |
| Runtime .NET | CLR, IL, JIT e tiered compilation, AOT nativo (noção), GC geracional e modos server/workstation | P11 |

### 2.2 TypeScript e JavaScript
| Tópico | O que dominar | Onde |
|---|---|---|
| JavaScript base | Escopo, closures, `this`, protótipos, módulos ES, desestruturação, spread | P3 |
| Assíncrono em JS | Event loop, microtask × macrotask, Promises, `async/await`, `fetch`, `AbortController` | P3 · P4 |
| TypeScript | Tipos, interfaces × type aliases, união e interseção, narrowing, genéricos, utility types (`Partial`, `Pick`, `Omit`, `Record`), `unknown` × `any`, modo `strict` | P3 |
| TypeScript avançado | Tipos condicionais, mapped types, template literal types, inferência; tipar respostas da API a partir do contrato OpenAPI | P5 · P12 |
| Ferramentas | Node.js, npm/pnpm, `tsconfig`, ESLint, Prettier, bundlers (noção de como o Next empacota) | P4 |

### 2.3 Python (bloco paralelo desde o Passo 3)
| Tópico | O que dominar | Onde |
|---|---|---|
| Base | Tipos, coleções, compreensões, funções, módulos, ambiente virtual (`venv`/`uv`), `pip` | Py |
| Idiomático | Iteradores, geradores, context managers, decorators, dataclasses, type hints com `mypy` | Py |
| Testes | `pytest`, fixtures, parametrização | Py |
| Assíncrono | `asyncio`, quando usar | Py |
| Web | **FastAPI** (único Python da stack: `aura-analytics`), Pydantic | Py · IA0 |
| Dados e IA | NumPy, Pandas, statsmodels, Prophet, OR-Tools, PyTorch | IA · P13 |
| Automação | Scripts para o seu setup, raspagem, relatórios | Py |

**Método do bloco Python:** a cada Passo, refaça em Python os exercícios do Passo (mesma lógica, outra linguagem) — o mesmo método de duas linguagens da 42. 1–2 h/semana. Assim a trilha de IA começa com Python pronto.

### 2.4 SQL
Ver camada 5. É linguagem de primeira classe, não "detalhe do ORM".

### 2.5 Shell
| Tópico | O que dominar | Onde |
|---|---|---|
| Bash | Navegação, pipes, redirecionamento, `grep`, `sed`, `awk`, `find`, `xargs`, scripts com variáveis, condicionais e laços, `set -euo pipefail` | Lx · P2 |
| PowerShell | Objetos no pipeline, scripts de automação no Windows (o seu ambiente de trabalho) | P2 |

### 2.6 C e C++
Pela [École 42](trilha-42-circles-oficial-verificado.md): ponteiros, memória manual, Makefile, structs, alocação, depuração com `gdb`/`valgrind`. Dá o entendimento de baixo nível que diferencia o sênior.

### 2.7 Clojure (decisão pendente)
Só entra se o `aura-historico` continuar em Clojure + Datomic: programação funcional, imutabilidade, REPL, Datomic. **Gatilho:** Passo 14, quando o Rendara precisar do histórico. Se você decidir por Event Sourcing com Marten em .NET, este item sai e entra Marten na camada 7.

**Sênior quando…** lê código desconhecido de qualquer uma das três linguagens principais e aponta o problema de desempenho ou de concorrência; escreve código idiomático em cada uma, não "C# escrito em Python".

---

## 3. Backend .NET e ASP.NET Core

| Tópico | O que dominar | Onde |
|---|---|---|
| Pipeline HTTP | Kestrel, middleware (ordem importa), roteamento, filtros | P4 |
| **Controllers** (escolha fixa da stack) | Atributos de rota, model binding, `ActionResult<T>`, `ProblemDetails` (RFC 9457) para erros | P4 |
| Injeção de dependência | Ciclos de vida (`Singleton`, `Scoped`, `Transient`) e o erro de capturar `Scoped` dentro de `Singleton`; registro por convenção | P3 · P4 |
| Configuração | `appsettings` por ambiente, variáveis de ambiente, Options pattern (`IOptions`, `IOptionsSnapshot`), validação de configuração | P4 |
| Validação | Data annotations × FluentValidation; validação de entrada × regra de domínio | P4 |
| Autenticação e autorização | JWT, refresh token, cookies, **OAuth 2.0 e OpenID Connect** (fluxos authorization code + PKCE, client credentials), políticas e claims, autorização por recurso, multi-tenant com `tenant_id` + RLS | P4 · P12 |
| Design de API REST | Recursos, verbos e status corretos, paginação (offset × cursor), filtros, ordenação, versionamento, idempotência com `Idempotency-Key`, ETag e concorrência otimista, HATEOAS (noção) | P4 · P7 |
| Documentação de API | OpenAPI, geração de cliente TypeScript a partir do contrato | P4 · P5 |
| GraphQL | HotChocolate, schema, resolvers, problema N+1 com DataLoader (AM Taskoro) | P14 |
| Tempo real | SignalR (hubs, grupos, escala com backplane Redis) | P9 |
| Tarefas em segundo plano | `BackgroundService`, `IHostedService`, filas, agendamento | P9 · P12 |
| Logging | `ILogger`, logs estruturados, níveis, correlação por requisição | P4 · P10 |
| Resiliência | Retry, timeout, circuit breaker com Polly / `Microsoft.Extensions.Http.Resilience`, `HttpClientFactory` | P9 |
| Caching | `IMemoryCache`, `IDistributedCache` com Redis, output caching, invalidação | P9 |
| Rate limiting | Middleware de rate limiting por IP, usuário e tenant | P4 |
| Health checks | Liveness × readiness | P10 |
| Arquivos | Upload em streaming, armazenamento em objeto (R2/S3), URL assinada | P9 |
| E-mail, PDF e relatórios | Geração de PDF, templates, envio assíncrono | P12 |
| Multi-tenancy | Isolamento por `tenant_id`, RLS no PostgreSQL, configuração por tenant | P4 · P12 |
| Dinheiro e fiscal | `decimal`, arredondamento, ledger de partidas dobradas, emissão fiscal | P3 · P7 · Fin |

**Sênior quando…** desenha uma API que outro time consome sem perguntar nada, e explica por que cada status, cada campo e cada regra de autorização está ali.

---

## 4. Frontend

### 4.1 Fundamentos da web
| Tópico | O que dominar | Onde |
|---|---|---|
| HTML semântico | Estrutura, landmarks, formulários corretos, metadados, SEO básico | P4 (você já ensina) |
| Acessibilidade | WCAG 2.2 nível AA, navegação por teclado, foco, ARIA só quando o HTML não resolve, contraste, leitores de tela | P4 · P12 |
| CSS | Cascata e especificidade, box model, Flexbox, Grid, posicionamento, unidades relativas, responsividade e mobile-first, variáveis CSS, temas claro/escuro | P4 |
| Tailwind | Utilitários, tokens do Aura Design System em `tailwind.config`, componentes sem repetir classes | P4 |
| Navegador | Como a página é renderizada (DOM, CSSOM, layout, paint), cookies, `localStorage`, CORS, Service Worker | P4 · P9 |

### 4.2 React
| Tópico | O que dominar | Onde |
|---|---|---|
| Modelo mental | Componentes, props, estado, renderização e reconciliação, keys em listas | P4 |
| Hooks | `useState`, `useEffect` (e quando **não** usar), `useMemo`, `useCallback`, `useRef`, `useReducer`, hooks próprios | P4 · P5 |
| Estado | Estado local × global × de servidor; **TanStack Query** para dados da API (cache, revalidação, mutações otimistas); **Zustand** para estado de cliente | P5 |
| Formulários | React Hook Form + validação com Zod usando o mesmo contrato da API | P5 |
| Componentes reutilizáveis | Composição, tabela genérica, formulário genérico, component library com **Storybook** | P5 · P12 |
| Performance | Re-render desnecessário, memoização, virtualização de listas longas, code splitting, React DevTools Profiler | P11 |

### 4.3 Next.js
| Tópico | O que dominar | Onde |
|---|---|---|
| App Router | Layouts, rotas aninhadas, loading e error boundaries | P4 |
| Renderização | Server Components × Client Components, SSR, SSG, ISR, streaming; quando cada um faz sentido | P4 · P9 |
| Dados | Buscar no servidor, cache do Next, revalidação, Server Actions (e quando preferir chamar a API .NET) | P5 |
| Autenticação no front | Sessão, middleware de rota, proteção de páginas | P4 |
| Exportação estática | Sites dos clientes de freela na Hostinger | P4 |
| Internacionalização | Português, inglês e espanhol (produtos para fora do Brasil) | Sr |

### 4.4 Qualidade no frontend
| Tópico | O que dominar | Onde |
|---|---|---|
| Testes | Vitest + Testing Library (componente), **Playwright** (E2E) | P6 |
| Performance web | Core Web Vitals (LCP, INP, CLS), Lighthouse, imagens otimizadas, fontes | P11 |
| PWA | Manifesto, service worker, offline (apps do Rotara e AuraVet) | P9 |
| Segurança no front | XSS, CSP, armazenamento seguro de token, dependências | P12 |

**Sênior quando…** constrói uma tela complexa acessível, rápida e testada, e decide com argumento entre renderizar no servidor ou no cliente.

---

## 5. Banco de dados e dados

| Tópico | O que dominar | Onde |
|---|---|---|
| Modelagem | Entidade-relacionamento, normalização (1FN–3FN) e quando desnormalizar, chaves naturais × substitutas, UUID × sequencial | P2 |
| SQL completo | `JOIN`s (base no produto cartesiano do Lins), agregação, `GROUP BY`/`HAVING`, subconsultas, **CTE** e CTE recursiva, **window functions**, `UPSERT` (`ON CONFLICT`) | P2 · P5 |
| Índices | B-tree, índice composto e ordem das colunas, índice parcial, de cobertura, GIN/GiST (JSONB, texto, PostGIS); quando um índice atrapalha a escrita | P2 · P11 |
| Plano de execução | `EXPLAIN ANALYZE`, seq scan × index scan, estatísticas, `VACUUM` e autovacuum | P2 · P11 |
| Transações | ACID, **níveis de isolamento** (read committed, repeatable read, serializable) e as anomalias de cada um, locks, deadlock, `SELECT … FOR UPDATE`, concorrência otimista × pessimista | P5 · P7 |
| PostgreSQL específico | JSONB, enums, constraints e `CHECK`, **Row-Level Security**, extensões (PostGIS, pgvector), funções e triggers (com moderação) | P4 · P9 · IA5 |
| EF Core a fundo | Migrations, relacionamentos, tracking × `AsNoTracking`, N+1 e `Include`, consultas compiladas, SQL bruto, `RowVersion`; quando usar **Dapper** | P5 · P11 |
| Migrações sem parar o sistema | Expandir e contrair (adicionar coluna, migrar dado, remover depois), migração em produção com rollback | P10 |
| Operação | Backup e **teste de restauração**, point-in-time recovery, réplica de leitura, connection pooling (PgBouncer), particionamento de tabela | P10 · Sr |
| Redis | Tipos (string, hash, list, set, sorted set, stream), TTL, padrões de cache (cache-aside, write-through), invalidação, locks distribuídos e seus riscos, Redis Streams como fila | P9 |
| Geoespacial | PostGIS: geometria × geografia, índice espacial, distância e área (AM Rotara) | P9 · P13 |
| Busca | Full-text search no PostgreSQL; quando um motor dedicado seria necessário | Sr |
| SQLite | Banco local do agente offline do Kaixara, sincronização | P7 |
| Dados analíticos | OLTP × OLAP, modelagem dimensional (noção), ETL | IA2 |

**Sênior quando…** olha uma consulta lenta em produção, lê o plano, cria o índice certo e explica o custo que ele adiciona na escrita.

---

## 6. Design e arquitetura de software

| Tópico | O que dominar | Onde |
|---|---|---|
| Código limpo | Nomes, funções pequenas, coesão, acoplamento, duplicação × abstração errada | P3 · P8 |
| SOLID | Os cinco princípios com exemplo real do Kaixara | P8 |
| Design patterns | Criação (Factory, Builder), estrutura (Adapter, Decorator, Facade, Proxy), comportamento (Strategy, Observer, Command, Template Method, Chain of Responsibility), padrões de dinheiro do Fowler | P8 |
| Refatoração | Catálogo do Fowler, refatorar com testes cobrindo | P8 |
| Clean Architecture e hexagonal | Camadas, regra de dependência, portas e adaptadores (`IFonteDeEstoque`, `IEmissorFiscal`) | P8 |
| **DDD tático** | Entidade, objeto de valor, agregado e sua fronteira de consistência, repositório, serviço de domínio, eventos de domínio | P8 |
| **DDD estratégico** | Contextos delimitados, linguagem ubíqua, mapa de contexto entre os sistemas Aura | P12 |
| CQRS | Separar leitura e escrita; quando vale a complexidade | P12 |
| Event Sourcing | Estado como sequência de eventos; base do `aura-historico` (Datomic ou Marten) | P14 |
| Monolito modular × microsserviços | Por que começar modular; custo real de distribuir | P12 |
| Decisões registradas | ADRs (você já usa) | P12 |
| Modelagem e diagramas | Modelo C4 (contexto, contêiner, componente), diagramas de sequência | P8 · P12 |

**Sênior quando…** defende uma arquitetura falando de trade-offs (custo, prazo, time, risco) e sabe dizer quando um padrão **não** deve ser usado.

---

## 7. Sistemas distribuídos, mensageria e integração

| Tópico | O que dominar | Onde |
|---|---|---|
| Teoria | Falácias da computação distribuída, CAP e PACELC, consistência forte × eventual, relógios e ordenação | P9 · Sr |
| Mensageria | Fila × pub/sub, garantias (at-most-once, at-least-once, exactly-once na prática), mensagens duplicadas e consumidor idempotente, dead letter queue, ordem de mensagens | P9 · P12 |
| Ferramentas | Redis Streams (da stack); conceitos de RabbitMQ e Kafka para entrevista e para quando a escala pedir | P9 · Sr |
| Padrões de consistência | **Outbox** transacional, **Saga** (orquestração × coreografia), compensação | P12 · P14 |
| Integração com terceiros | Webhooks (assinatura, reentrega, idempotência), APIs de pagamento, Pix e Open Finance, cobrança recorrente | P7 · P14 · Fin |
| Resiliência | Timeouts, retry com backoff e jitter, circuit breaker, bulkhead, degradação controlada | P9 |
| Consenso (noção) | Raft e líder; base para entender bancos e o ByteSDCoin (PoA) | HL |
| gRPC | Saber o que é e quando se usa (entrevista). **Fora do portfólio** por decisão sua | — |

**Sênior quando…** projeta um fluxo de pagamento entre dois sistemas que continua correto se qualquer mensagem chegar duas vezes, atrasada ou nunca.

---

## 8. Qualidade e testes

| Tópico | O que dominar | Onde |
|---|---|---|
| Estratégia | Pirâmide e "troféu" de testes, o que testar em cada camada, cobertura como sinal e não meta | P6 |
| Unitário | **xUnit**, AAA, test doubles (mock, stub, fake) com Moq, testes legíveis | P6 |
| Integração | `WebApplicationFactory`, **Testcontainers** com PostgreSQL e Redis reais | P6 |
| Contrato | Teste de contrato da API (consumidor × provedor) | P12 |
| E2E | **Playwright**, testes estáveis (sem `sleep`), dados de teste | P6 |
| TDD | Ciclo vermelho-verde-refatorar, quando ajuda e quando atrapalha | P6 |
| Testes de propriedade | Gerar entradas aleatórias para regras de dinheiro (FsCheck) | P7 |
| Mutação | Medir a qualidade dos testes (Stryker.NET) | Sr |
| Carga | **k6**: carga, estresse, pico, duração | P11 |
| Análise estática | Analyzers do .NET, ESLint, CodeQL, SonarQube (noção) | P6 |
| Revisão de código | O que olhar num PR: correção, legibilidade, segurança, teste | P6 · Sr |

**Sênior quando…** uma refatoração grande passa em produção sem susto porque os testes certos existiam — e o time confia na suíte.

---

## 9. Segurança de aplicação

| Tópico | O que dominar | Onde |
|---|---|---|
| OWASP Top 10 | Injeção, quebra de controle de acesso, falhas criptográficas, SSRF, configuração insegura, componentes vulneráveis etc. — e como cada um aparece no seu código | P4 |
| OWASP API Security Top 10 | Autorização por objeto (BOLA), exposição excessiva de dados, rate limiting | P4 |
| Autenticação | Hash de senha (BCrypt/Argon2), 2FA, sessão, recuperação de conta, OAuth/OIDC | P4 |
| Criptografia aplicada | Simétrica × assimétrica, hash × HMAC × assinatura, TLS, gestão de chaves (KMS), criptografia de campo (`aura-vault`) | P4 · P12 |
| Modelagem de ameaças | STRIDE aplicado a cada sistema novo | P8 |
| Segredos | Nunca no repositório (Gitleaks), cofre de segredos (`aura-secrets`) | P2 · P10 |
| Cadeia de suprimentos | Dependabot, lock files, verificação de pacotes | P2 |
| Testes de segurança | SAST (CodeQL), DAST (OWASP ZAP), pentest do próprio Aura | P6 · Seg |
| Privacidade | LGPD (e GDPR para clientes de fora), minimização de dados, retenção, direito de exclusão | P4 · P12 |

**Sênior quando…** encontra a falha de autorização no PR de outra pessoa antes de ela chegar em produção.

---

## 10. Infraestrutura, DevOps e cloud

| Tópico | O que dominar | Onde |
|---|---|---|
| Linux para dev | Terminal, permissões, processos, systemd, logs, SSH, firewall | Lx · P10 |
| Git avançado | Branches, rebase × merge, `cherry-pick`, `bisect`, `reflog`, conventional commits, trunk-based × git flow | P2 |
| Docker | Imagem × contêiner, camadas e cache, **multi-stage**, imagem mínima e sem root, volumes, redes, Docker Compose | P2 · P10 |
| CI/CD | **GitHub Actions**: build, teste, análise, publicação de imagem, deploy; pipelines reutilizáveis | P6 · P10 · P12 |
| Estratégias de deploy | Rolling, blue-green, canary, feature flags, rollback | P10 · Sr |
| Infraestrutura como código | **Terraform**: estado, módulos, ambientes | P12 |
| Cloud | Conceitos comuns às nuvens: computação, rede (VPC), armazenamento de objeto, banco gerenciado, IAM, custos; VPS + Vercel do seu setup | P10 · Sr |
| Kubernetes (noção sólida) | Pod, deployment, service, ingress, config e secrets, escalonamento — cobrado em vaga sênior mesmo quando você não usa | Sr |
| CDN e DNS | Cache na borda, certificados, domínio dos clientes | P10 |
| Ambientes | Desenvolvimento, homologação e produção; paridade entre eles | P10 |

**Sênior quando…** um commit vai sozinho até produção com teste, análise e possibilidade de voltar atrás em minutos.

---

## 11. Observabilidade e operação em produção

| Tópico | O que dominar | Onde |
|---|---|---|
| Os três sinais | Logs estruturados, métricas, **tracing distribuído** com **OpenTelemetry** | P10 |
| Ferramentas | Serilog/OTel no .NET, Grafana/Prometheus (ou equivalente), Uptime Kuma (já planejado) | P10 |
| SLI, SLO e orçamento de erro | Definir o que é "funcionando" para cada sistema | Sr |
| Alertas | Alertar no sintoma do usuário, não em cada métrica; evitar fadiga de alerta (`aura-oncall`) | P10 |
| Incidentes | Resposta a incidente, comunicação, **postmortem sem culpa** | Sr |
| Runbooks | Passo a passo para os problemas conhecidos | P10 |
| Capacidade e custo | Prever crescimento, custo por tenant | Sr |

**Sênior quando…** descobre a causa de um problema em produção pelos traces e logs, sem precisar reproduzir na máquina.

---

## 12. Performance e escalabilidade

| Tópico | O que dominar | Onde |
|---|---|---|
| Medir antes | Profiling (dotnet-trace, dotnet-counters, PerfView), **BenchmarkDotNet**, flame graphs | P11 |
| Memória no .NET | Alocações, GC, pooling (`ArrayPool`), `Span<T>` | P11 |
| Banco | Índices, consultas, pool de conexões, réplica de leitura | P11 · Sr |
| Cache | Onde cachear (navegador, CDN, aplicação, banco), invalidação | P9 · P11 |
| Escala | Vertical × horizontal, aplicação sem estado, filas para picos | P12 · Sr |
| Frontend | Core Web Vitals, bundle menor, renderização no servidor | P11 |
| Carga | k6 com cenários reais, encontrar o gargalo | P11 |

**Sênior quando…** mostra "antes e depois" com números reais e explica por que a otimização valeu o custo de manutenção.

---

## 13. Software de desktop e dispositivo — agente local do AM Kaixara

| Tópico | O que dominar | Onde |
|---|---|---|
| Windows Service em .NET | `BackgroundService` como serviço do Windows, instalação, logs no Event Viewer | P7 |
| Offline-first | SQLite local, fila de sincronização, resolução de conflito quando a internet volta | P7 |
| Periféricos | Impressora fiscal/térmica (ESC/POS), gaveta de dinheiro, balança, TEF — atrás de interfaces (`IImpressoraFiscal`, `IGavetaDinheiro`, `IBalanca`, `ITefService`) | P7 |
| Comunicação | Porta serial e USB, comunicação local com o navegador | P7 |
| Distribuição | Instalador MSIX ou WiX, **assinatura de código**, atualização automática | P10 · P12 |

**Sênior quando…** o caixa continua vendendo sem internet e nenhuma venda se perde nem duplica quando a conexão volta.

---

## 14. Processo, requisitos e colaboração

| Tópico | O que dominar | Onde |
|---|---|---|
| Requisitos | Entrevista com usuário, requisitos funcionais e não funcionais (seus documentos RF/RNF), histórias de usuário, critérios de aceite | P1 (EPIC-01) |
| Fatiar trabalho | Dividir em entregas pequenas que já geram valor | P1 · P7 |
| Estimativa | Estimar com faixa e risco, não com número único | Sr |
| Métodos ágeis | Scrum, Kanban, RAD (os três do AM Taskoro), retrospectiva | P12 |
| Revisão de código | Dar e receber revisão com respeito e objetividade | P6 · Sr |
| Documentação | README, ADR, guia de contribuição, documentação de API, runbook — em português e inglês | P9 · P12 |
| Comunicação técnica | Explicar trade-offs para quem não é técnico (cliente, sócia, gestor) | Sr |

---

## 15. Competências de sênior e carreira internacional

### O que separa o sênior do pleno
- **Autonomia:** recebe um problema vago e entrega uma solução completa, perguntando só o necessário.
- **Escopo:** pensa no sistema inteiro (dados, segurança, operação, custo), não só no código da tarefa.
- **Julgamento:** escolhe a solução mais simples que resolve; sabe quando não construir.
- **Multiplicador:** faz o time render mais com revisão, mentoria, documentação e ferramentas. A sua experiência como professor é um diferencial real aqui.
- **Responsabilidade por produção:** o que ele entrega funciona às 3 da manhã.

### Entrevistas (Brasil e exterior)
| Etapa da entrevista | Preparação | Onde |
|---|---|---|
| Algoritmos e estruturas de dados | Problemas de nível médio, falando em voz alta, em inglês | P8+ |
| **System design** | Desenhar em 45 minutos: encurtador de URL, sistema de pagamentos, feed, chat, sistema de entregas (use o Aura); requisitos, estimativa de escala, API, dados, gargalos | Sr |
| Projeto prático | Entregar código limpo, testado e documentado em prazo curto | P10+ |
| Comportamental | Método **STAR** com histórias reais (incidentes, conflitos, decisões) | Sr |
| Inglês | Conversação técnica fluente — meta C1 | contínuo |

### Exterior — além do técnico
- Portfólio e GitHub **em inglês**, LinkedIn em inglês.
- Diploma reconhecido: por isso a [faculdade para IA](formacao-academica.md) (Ciência da Computação ou IA).
- Trabalho remoto para fora: contrato como pessoa jurídica, câmbio e impostos — conecta com a [trilha de finanças](trilha-financas-economia.md) F3.
- Fusos horários e comunicação assíncrona por escrito.

---

## 📚 Leituras de referência (por camada)

| Camada | Livro |
|---|---|
| Fundamentos | *Grokking Algorithms* (Bhargava) · *Introduction to Algorithms* (Cormen et al., consulta) |
| C# e .NET | *C# in Depth* (Jon Skeet) · documentação oficial do .NET (Microsoft Learn) |
| Arquitetura | *Clean Architecture* (Robert Martin) · *Domain-Driven Design* (Eric Evans) · *Patterns of Enterprise Application Architecture* (Fowler) · *Refactoring* (Fowler) |
| Dados e distribuídos | *Designing Data-Intensive Applications* (Kleppmann) — o mais importante desta lista |
| Produção | *Release It!* (Nygard) · *Site Reliability Engineering* (Google, gratuito online) |
| Processo | *Software Engineering at Google* (Winters, Manshreck e Wright) · *The Pragmatic Programmer* (Hunt e Thomas) |
| Entrevista | *System Design Interview* (Alex Xu) |

Auditoria cruzada contínua: [roadmap.sh](https://roadmap.sh/roadmaps) — Backend, Frontend, ASP.NET Core, React, PostgreSQL, Docker, System Design e Software Architect ([integracao-42-roadmap-akita](integracao-42-roadmap-akita.md)).

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Currículo — Alan Mateus](../12-artefatos/documentos/curriculo-alan-mateus.md)
- [Portfólio AMtech](../12-artefatos/paginas/portfolio-amtech-mbj1/index.html) · página interativa · [sobre](../12-artefatos/paginas/portfolio-amtech-mbj1/LEIA-ME.md)
- [12 Projetos da Formação — especificações](../12-artefatos/documentos/12-projetos-da-formacao-especificacoes.md)
- [Guia de Terminal: Git, GitHub, PowerShell e Git Bash](../12-artefatos/documentos/guia-de-terminal-git-github-powershell-e-git-bash.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
