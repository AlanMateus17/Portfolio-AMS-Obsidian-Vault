---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Plano de Estudos — Do Básico ao Nível Sênior, Entrelaçado por Fase
### Ao final da Fase 6, o AuraPOS deve estar pronto E construído com prática de nível sênior — não "funcionando" e "sênior" como duas etapas separadas

> Este documento substitui o `plano-de-estudos-atualizado-portfolio-completo.md` como referência principal até o fim do AuraPOS. As Fases 7 em diante (Python, criptografia, IA) daquele documento continuam válidas sem alteração — a mudança está inteira nas Fases 0-6.

---

## Princípio desta versão

Profundidade sênior não é um bloco de conteúdo extra no fim — é o **como** você estuda cada fase, não um **o que** adicional depois. Cada fase abaixo tem uma seção "Nível padrão" (o suficiente pra funcionar) e uma seção "Aprofundamento sênior" (o que separa "funciona" de "profissional") — estudadas juntas, no mesmo momento, nunca em blocos separados no tempo.

---

## FASE 0 — Lógica de Programação (2–3 semanas)

Sem mudança — fundamento é fundamento, não tem versão "sênior" de `if/else`.

**Conteúdo completo a dominar:**
- Variável, tipo primitivo (inteiro, decimal, texto, booleano), constante
- Operador aritmético, relacional, lógico (`&&`, `||`, `!`) e precedência entre eles
- Entrada/saída de dado (console)
- `if/else if/else`, `switch/case`, tabela-verdade
- `for`, `while`, `do-while`, `break`, `continue`, como identificar e evitar loop infinito
- Array, lista, dicionário (key-value), noção de pilha (stack) e fila (queue)
- Função: parâmetro, retorno, escopo de variável, função pura vs. com efeito colateral
- Recursão (nível conceitual — fatorial, busca simples)
- Lógica booleana composta aplicada a regra de negócio (ex: `if (estoque > 0 && cliente.ativo && !pedido.cancelado)`)
- Noção de complexidade (por que loop dentro de loop fica lento com muito dado — sem Big O formal ainda)
- Leitura de mensagem de erro e uso de log/print pra depurar

**O que desenvolver enquanto estuda (sem banco, sem API — só lógica pura em console):**
- Simulação do cálculo de carrinho de compra com desconto (exercício-âncora da fase)
- Simulação simplificada da escada de inadimplência do `aura-licensing` (uma função que recebe "dias em atraso" e retorna o status: ativo → atraso → restrito → suspenso) — já pensando na regra de negócio real que você vai implementar de verdade depois
- Simulação do cálculo de rebalanceamento ARCA do AuraWealth em versão simplificada (uma função que recebe 4 valores de quadrante e retorna quanto falta pra cada um chegar a 25%) — puro `if`/aritmética, sem banco, só pra já se familiarizar com a regra de negócio antes de codificar de verdade na Fase 2

**✅ Critério de saída:** resolve os três exercícios acima sem travar.

---

## FASE 1 — Git, SQL e Docker (1–2 semanas)

### Nível padrão — conteúdo completo
- **Git:** `init`, `clone`, `add`, `commit`, `push`, `pull`, branch, `merge`, resolução de conflito, `.gitignore`, Pull Request
- **SQL/PostgreSQL:** `CREATE TABLE`, tipo de coluna, chave primária/estrangeira, `SELECT/INSERT/UPDATE/DELETE`, `WHERE`, `ORDER BY`, `GROUP BY`/`HAVING`, `JOIN` (INNER, LEFT), subquery, transação (`BEGIN/COMMIT/ROLLBACK`)
- **Docker:** imagem vs. container, `Dockerfile` básico, `docker-compose.yml`, volume, rede entre container

### Aprofundamento sênior
- **Plano de execução de query** — `EXPLAIN ANALYZE` no PostgreSQL, entender por que uma query é lenta antes de precisar otimizar de verdade
- **Estratégia de índice** — quando um índice ajuda, quando atrapalha (índice em coluna de baixa cardinalidade, por exemplo)
- **Git além do básico** — rebase interativo, squash, mensagem de commit que conta uma história, não só "fix"

**O que desenvolver enquanto estuda:**
- Criar o schema real de tabelas do AuraPOS (produto, categoria, estoque, venda) direto no PostgreSQL, à mão, antes de qualquer EF Core — entender o banco antes de deixar o ORM gerar por você
- Modelar (só o schema, sem código ainda) as tabelas centrais do `aura-licensing` (tenant, módulo, assinatura) — é pequeno e simples, bom segundo exercício de modelagem multi-tenant desde já
- Subir Postgres + Redis via `docker-compose up` num comando só, ambiente de desenvolvimento do AuraPOS

**✅ Critério de saída:** além do JOIN/transação, você lê um `EXPLAIN ANALYZE` e identifica se uma query está fazendo full scan quando não deveria.

---

## FASE 2 — C# e .NET (4–6 semanas, a mais densa do plano)

### 2.1 — C# fundamentals

**Nível padrão — conteúdo completo:**
- Tipo de valor vs. tipo de referência, `struct` vs. `class`, `record`
- Classe: propriedade, método, construtor, `static` vs. instância
- Herança, interface, polimorfismo, classe abstrata
- Coleção: `List<T>`, `Dictionary<K,V>`, `HashSet<T>`, `IEnumerable<T>`
- LINQ: `Select`, `Where`, `OrderBy`, `GroupBy`, `Join`, `FirstOrDefault`, método de extensão
- Tratamento de exceção (`try/catch/finally`, exceção customizada)
- Nullable reference type (`string?` vs. `string`) — evita boa parte dos erros de referência nula
- Generic (`List<T>`, criar sua própria classe genérica)

**Aprofundamento sênior:**
- `async/await` de verdade — não só a sintaxe, entender o que o compilador faz por baixo (state machine), por que `async void` é perigoso, quando usar `Task` vs `ValueTask`
- Tempo de vida de injeção de dependência (`Singleton`, `Scoped`, `Transient`) — e o erro clássico de injetar `Scoped` dentro de `Singleton`

**O que desenvolver:** entidades de domínio do AuraPOS (`Product`, `Category`, `Sale`, `TenantId`/`FilialId`) já com nullable reference type habilitado desde o início — é mais barato nascer com isso do que adicionar depois. Em paralelo, as entidades do AuraTest (já em andamento) servem de segundo terreno de prática pros mesmos conceitos, sem pressão de ser "o produto real".

### 2.2 — ASP.NET Core Web API

**Nível padrão — conteúdo completo:**
- Roteamento, `[ApiController]`, model binding, `[FromBody]`/`[FromQuery]`/`[FromRoute]`
- DTO de entrada e saída (nunca expor a entidade de domínio direto na API)
- Validação de entrada (Data Annotations ou FluentValidation)
- Middleware pipeline — o que é, ordem de execução, como escrever um middleware customizado
- Autenticação JWT — geração de token, validação, `[Authorize]`, claim
- Documentação de API (OpenAPI/Swagger)

**Aprofundamento sênior:**
- **Design de API maduro** — versionamento (`/v1/`), paginação consistente, código de status HTTP correto (não tudo 200)
- **OWASP Top 10 aplicado, não teórico** — direto em cima do próprio endpoint de login: injeção, quebra de autenticação, exposição de dado sensível, controle de acesso quebrado (BOLA)
- **Rate limiting** — implementação real, não só conceito

**O que desenvolver:** `AuthController` (login/JWT — já em andamento, esta fase é o momento de blindar o que existe contra o OWASP Top 10), `ProductsController`, `CategoriesController`, `SalesController` do AuraPOS. **Ponto de reaproveitamento real:** a lógica de emissão/validação de JWT que você escrever aqui é literalmente o núcleo do futuro `aura-identity` — construir com cuidado agora economiza reescrever depois quando ele virar serviço central.

### 2.3 — Entity Framework Core

**Nível padrão — conteúdo completo:**
- `DbContext`, `DbSet<T>`, Fluent API de configuração de entidade
- Migration: criar, aplicar, reverter
- Relacionamento 1:N e N:N no EF Core
- Consulta com `Where`, `Include`, `Select` (projeção)

**Aprofundamento sênior:**
- Ligar o `EXPLAIN ANALYZE` da Fase 1 ao SQL que o EF Core gera
- `AsNoTracking()` e quando usar, `Include()` vs. projeção com `Select()`, problema de N+1 e como evitar

**O que desenvolver:** migration real do AuraPOS já rodada — este é o momento certo pra resolver a pendência que ficou registrada no documento final do AuraPOS (seção 6.2): adicionar a coluna de controle de concorrência (`RowVersion`) ao `Product` e ajustar o `ProductRepository` pra atualização condicional (RNFT-E01). Não é exercício teórico — é literalmente o próximo passo real do seu sistema em produção.

### 2.4 — Teste além do básico

**Conteúdo completo:**
- Estrutura Arrange-Act-Assert
- `Moq` (ou biblioteca equivalente) pra mock de dependência
- **Pirâmide de teste** — muito unitário, menos integração, poucos end-to-end, e por quê
- Teste de integração com banco real (banco de teste dedicado ou Testcontainers)
- Ciclo TDD (red-green-refactor) como disciplina, não teoria

**O que desenvolver:** teste unitário e de integração do fluxo de venda do AuraPOS (é o trecho mais sensível a bug de concorrência, já identificado). Em paralelo, o `aura-goals` é um bom segundo alvo de prática de TDD puro — regra de negócio pequena e isolada (meta, contribuição, confirmação mútua), ótima pra treinar escrever teste antes da implementação sem a complexidade do AuraPOS em volta.

**Projeto prático (toda a Fase 2):** API do AuraPOS completa — produto, estoque, venda, autenticação — construída já com os pontos acima aplicados, não retrabalhada depois.

**✅ Critério de saída:** API funcional, com cobertura de teste unitário e de integração, JWT seguro contra os erros mais comuns do OWASP Top 10, e você consegue explicar por que cada decisão de design da API foi tomada.

---

## FASE 3 — Frontend (3–5 semanas, paralelo à Fase 2)

> **Atualização:** esta fase estava genérica ("TypeScript, Next.js, Tailwind") desde antes do frontend do AuraPOS ter sido planejado com rigor completo (11 etapas, em `[[aurapos-frontend-documento-unico]]`). Agora ela reflete o conteúdo real.

**Conteúdo completo a dominar:**
- **TypeScript:** tipo primitivo, interface, `type`, generic básico, union type, `unknown` vs. `any`
- **Next.js (App Router):** estrutura de pasta/rota, Server Component vs. Client Component, `fetch` no servidor, formulário e `Server Action`, layout compartilhado
- **Tailwind CSS + tokens exatos:** classe utilitária, responsividade (`sm:`/`md:`/`lg:`), variável CSS customizada — agora com **valor hexadecimal real** definido em `[[rnf-transversais-design-tema]]` (`--aura-primaria: #0E3A45`, etc.), não mais descrição de cor solta
- **TanStack Query (React Query):** cache de estado de servidor, revalidação
- **Zustand:** estado de UI local (carrinho em edição) — nunca usado pra tudo, só o que precisa ser global
- **Acessibilidade (RNFT-D04/D07 do portfólio):** contraste mínimo WCAG AA, navegação por teclado, atributo `alt`/`aria-label`, anel de foco (`--foco-anel`)
- Teste de componente (Testing Library) + primeiro E2E (Playwright)

**O que desenvolver, seguindo as 11 etapas de `[[aurapos-frontend-documento-unico]]`:**
1. Etapa 1 (Discovery) — já formalizada retroativamente, com a pendência real de validação de persona (3-5 conversas com dono/operador de comércio) ainda em aberto
2. Etapa 3 (Design System) — implementar os tokens exatos como CSS custom properties: cor, sombra, z-index, duração de animação, escala de ícone, **e a paleta de estado dinâmico** (badge de status, indicador online/offline, skeleton, paleta de gráfico `--viz-1` a `--viz-5`)
3. Etapa 4 — tela de PDV do AuraPOS consumindo a API real da Fase 2, já com o diferencial central implementado: **operável 100% por teclado**, com painel de atalhos (`?`) descobrível
4. Construir uma vez aqui, no primeiro sistema, significa que AuraVet, AuraCondo, AuraObra e todo o resto reaproveitam sem reconstruir nada, só trocando o valor do token — inclusive a paleta de estado dinâmico, que já nasce transversal a todo sistema com dashboard

**✅ Critério de saída:** tela de PDV funcional, consumindo API real, com o sistema de tokens de design completo implementado (cor exata, estado dinâmico, animação, z-index — nada solto no código), navegável 100% por teclado.

---

## FASE 4 — Arquitetura de Verdade (contínua, paralela às Fases 2 e 3)

### Nível padrão — conteúdo completo
- **SOLID:** cada uma das 5 letras com exemplo real, não só definição
- **Design Patterns relevantes:** Repository, Factory, Strategy, Decorator — os que aparecem de verdade em Clean Architecture aplicada a sistema de negócio, não o catálogo inteiro do GoF
- **Clean Architecture:** as 4 camadas (Domain/Application/Infrastructure/Api), regra de dependência (camada de fora depende de dentro, nunca o contrário)
- **DDD tático:** Entity, Value Object, Aggregate, Domain Event, Repository como abstração de domínio

### Aprofundamento sênior
- Ligar o tempo de vida de DI (Fase 2.1) diretamente à arquitetura — por que repositório costuma ser `Scoped`, por que isso importa em Clean Architecture especificamente
- Revisão de código deliberada — pegar uma classe já escrita e refatorar aplicando SOLID de propósito, comparando antes/depois

**O que desenvolver:** refatorar o AuraPOS existente aplicando cada padrão estudado nele mesmo — nunca em projeto de exemplo descartável. As interfaces trocáveis já formalizadas no portfólio (`IFonteDeEstoque`, `IEmissorFiscal`, `IFonteDeMovimentacaoBancaria`, `IFonteDeReceita`) são o exemplo real de Strategy Pattern aplicado — implementá-las aqui é aprender o padrão E avançar o produto ao mesmo tempo.

**Regra mantida:** aplicar sempre refatorando o AuraPOS real, nunca em teoria solta.

---

## FASE 5 — Ponte para Delivery e Multi-sistema (após MVP do AuraPOS)

**Conteúdo completo a dominar:**
- **PostGIS:** tipo `geography`/`geometry`, `ST_Distance`, `ST_DWithin`, índice espacial (`GIST`)
- **Redis:** tipo de dado (string, hash, sorted set), cache de leitura, fila simples
- **SignalR:** Hub, conexão, grupo, envio de evento do servidor pro cliente sem refresh
- **Mobile:** diferença PWA vs. nativo, manifest e service worker básico de um PWA

**O que desenvolver:**
- Cache de consulta de produto/estoque do AuraPOS via Redis (reduz carga direta no banco)
- **Aura Delivery — Bloco 1 do MVP** (pedido + geolocalização), o próximo sistema real da fila, usando PostGIS pra calcular distância de entrega — não é exercício isolado, é o início de fato do segundo sistema do portfólio
- SignalR aplicado a dois lugares ao mesmo tempo: dashboard do AuraPOS atualizando em tempo real, e status de pedido do Aura Delivery — mesmo Hub, dois casos de uso, reforçando o padrão

**✅ Critério de saída:** protótipo calcula distância de entrega, atualiza status em tempo real.

---

## FASE 6 — Cloud e Produção

### Nível padrão — conteúdo completo
- `Dockerfile` multi-stage, `docker-compose.yml` de produção separado do de desenvolvimento
- Deploy em serviço gerenciado (AWS ECS/Elastic Beanstalk ou Azure App Service — escolher um)
- Banco gerenciado (RDS ou Azure Database for PostgreSQL)
- Pipeline GitHub Actions: sintaxe de workflow, `build → test → deploy` automático no push
- Gestão de segredo (variável de ambiente/secret, nunca senha commitada)

### Aprofundamento sênior — **observabilidade deixa de ser "depois" e entra aqui, agora**
- **Logging estruturado** (não `Console.WriteLine`) — já é requisito formal do seu portfólio (RNFT-E05)
- **Health check** — endpoint que diz se a API está saudável
- **Métrica básica** — quantidade de requisição, tempo de resposta, taxa de erro
- **`dotnet-trace`/profiling introdutório** — o suficiente pra diagnosticar API lenta em produção

**Deixar pra depois (mantido):** Infrastructure as Code, multi-região, APM completo/tracing distribuído de nível enterprise.

**O que desenvolver:** deploy real do AuraPOS em produção — o primeiro marco de verdade do portfólio inteiro. Ao mesmo tempo, formalizar o **template de pipeline GitHub Actions reaproveitável**: como o padrão de CI/CD é praticamente idêntico entre os 21 sistemas (build → teste → deploy, mesmo Dockerfile multi-stage), vale extrair aqui um modelo genérico que só muda o nome do projeto — economia real de tempo em todos os próximos 20 sistemas, não só um detalhe deste.

**✅ Critério de saída:** sistema em produção, com log estruturado, health check e métrica básica — não só "no ar", mas **observável**.

---

## FASE 6B — Fundamentos para entrevista técnica (contínua, a partir da Fase 4)

Sem mudança — estrutura de dado/algoritmo nível entrevista, comunicação de solução técnica, paralela a qualquer fase seguinte.

---

## FASE 6C — Performance de memória profunda (nova, após a Fase 6, com AuraPOS já em produção)

**Por que agora, e não antes:** estudar Garbage Collector e `Span<T>` em profundidade sem um sistema real gerando carga é estudar em abstrato — você não sente o problema que a técnica resolve. Só faz sentido depois que o AuraPOS estiver em produção (Fase 6) e você tiver dado real de uso pra analisar.

**Conteúdo:**
- `Span<T>` e `Memory<T>` — quando evitam alocação desnecessária, e por que isso importa
- Garbage Collector do .NET em detalhe — gerações (Gen 0/1/2), quando uma alocação vira pressão de GC perceptível
- `BenchmarkDotNet` — medir antes e depois de uma otimização, nunca otimizar por intuição
- `dotnet-trace` e `dotnet-counters` aprofundado (a Fase 6 já introduziu o básico) — diagnosticar lentidão real em produção, não simulada

**Projeto prático:** pegar o endpoint mais usado do AuraPOS em produção, medir com `BenchmarkDotNet`, aplicar uma otimização real, medir de novo — sentir a diferença com número, não achismo.

**O que desenvolver:** além do endpoint do AuraPOS, este é o momento certo de revisitar o `aura-vault` (se já estiver em desenvolvimento) com atenção de performance — operação de criptografia/decriptografia de campo é candidata natural a gargalo se mal implementada, e medir isso cedo evita descobrir o problema só quando o volume de dado real crescer.

**✅ Critério de saída:** você sabe diferenciar "esse código parece lento" de "esse código é lento, aqui está o número que prova, e aqui está o que melhorou depois da mudança".

---

## FASE 12 — Segurança Ofensiva e Trilha para Empresa de Pentest (nova, trilha própria e mais longa)

> A versão aprofundada desta fase (6 níveis, todas as ferramentas, certificações e labs) está em [[roadmap-seguranca-ofensiva-completo]] e seu companion [[recursos-links-seguranca-ofensiva]].

**Diferença importante em relação a tudo que veio antes:** as fases anteriores entrelaçam segurança *defensiva* aplicada dentro do desenvolvimento do AuraPOS (OWASP Top 10 na Fase 2.2, RNFT-S01-S06 já formalizados no portfólio). Isso é necessário, mas é **insuficiente** pra cobrar de terceiro como serviço de pentest — segurança ofensiva é uma especialização à parte, com profundidade e responsabilidade legal diferentes. Por isso vira fase própria, não mais um item entrelaçado.

### 12.0 — Quando começar
**Depois da Fase 4 (Clean Architecture) consolidada, rodando em paralelo à Fase 5 em diante — nunca antes.** Você precisa entender como um sistema é construído corretamente antes de conseguir avaliar de forma útil como ele quebra. Pentest feito por quem nunca construiu nada de verdade tende a ser superficial — checklist sem entendimento do que está por trás.

### 12.1 — Fundamentos de rede e sistema (pré-requisito, ~4-6 semanas)
- TCP/IP, modelo OSI, DNS, HTTP/HTTPS em profundidade (não o nível de "sei fazer requisição", o nível de "sei o que acontece em cada handshake")
- Linux — linha de comando com fluência real, não só comando básico
- **Recurso:** este é um dos poucos pontos de todo o plano onde vale considerar certificação formal cedo — CompTIA Network+ ou equivalente gratuito (Professor Messer, em inglês, referência forte e gratuita)
- **Trilha de certificação completa (correção: encontrada em conversa separada, nunca formalizada aqui):** `CompTIA A+/Network+ → CompTIA Security+ → CCNA (opcional, reforço de rede) → eJPT → OSCP`. Se os fundamentos de rede já estiverem sólidos (via `NetPractice` da Trilha 42), dá pra pular direto pro eJPT sem passar pelas certificações CompTIA/CCNA — elas existem pra quem começa do zero em rede, não é seu caso
- **Conceito fundamental a garantir antes de avançar:** CIA Triad (Confidencialidade/Integridade/Disponibilidade), Blue Team vs. Red Team vs. Purple Team, Zero Trust, Defense in Depth — vocabulário que aparece direto nas provas eJPT/OSCP, não só na prática

### 12.1B — Frameworks conceituais e ferramentas de reconhecimento (novo, encontrado em conversa separada)
- **Frameworks a dominar o vocabulário:** MITRE ATT&CK, Cyber Kill Chain, Diamond Model — usados pra estruturar e comunicar um teste de intrusão de forma profissional, não é forma de ataque em si
- **Ferramentas de varredura/enumeração além do Nmap:** `netstat`, `arp`, `tcpdump`, Wireshark (análise de protocolo)
- **Ferramentas de forense (relevante pra entender o outro lado — resposta a incidente):** FTK Imager, Autopsy, memdump, WinHex
- **Sandbox de análise de malware:** VirusTotal, Joe Sandbox, any.run, urlscan
- **Distro:** Kali Linux ou ParrotOS como ambiente de prática padrão
- **Tipos de ataque a conhecer, com nome formal:** MITM, DNS Poisoning, Pass the Hash, Directory Traversal — e técnicas de **bypass** (evasão de antivírus, contorno de WAF) que entram no nível OSCP de pós-exploração, não no eJPT inicial

### 12.2 — Metodologia de teste de segurança web (~6-8 semanas)
- OWASP Testing Guide — a versão completa, não só o Top 10 (que você já aplicou defensivamente na Fase 2.2, aqui é a mesma base olhada pelo lado ofensivo)
- Metodologia de reconhecimento, enumeração, exploração, pós-exploração, relatório — pentest de verdade é processo estruturado, não "tentar quebrar coisa aleatoriamente"
- **Prática:** plataformas de treino legal — PortSwigger Web Security Academy (gratuita, referência da indústria), TryHackMe, HackTheBox

### 12.3 — Ferramental (~4 semanas, em paralelo à 12.2)
- Burp Suite (interceptação e manipulação de requisição) — ferramenta padrão de mercado
- OWASP ZAP (alternativa open source)
- Nmap (varredura de rede/porta)
- Scripting de automação — **aqui o Python que você já vai estudar na Fase 7 (para o `aura-analytics`) se reaproveita diretamente**, evitando estudar a linguagem duas vezes

**Não duplicar — overlap já identificado com outras trilhas do plano:**
- Rede/Linux: `NetPractice` e `Born2beroot` da [[trilha-42-circles-oficial-verificado]] já cobrem boa parte
- Criptografia básica: já no plano via [[integracao-42-roadmap-akita]] (episódios #67/#131/#147 do Akitando)
- OWASP Top 10 (lado defensivo): já aplicado na Fase 2.2 — aqui (12.2) é a mesma base, olhada pelo lado ofensivo

### 12.4 — Certificação como âncora de credibilidade (~6-12 meses de preparo, a mais longa do plano inteiro)
- **eJPT** (entry-level, acessível, bom primeiro objetivo mensurável)
- **OSCP** (Offensive Security Certified Professional) — é o padrão-ouro reconhecido de mercado pra credibilidade de empresa de pentest; extremamente prático (exame é uma invasão real cronometrada, não múltipla escolha); caro e difícil, mas é o que separa "estudei sozinho" de "o mercado reconhece"

### 12.5 — O que a certificação técnica NÃO cobre — parte legal e de negócio, obrigatória pra empresa de verdade
Isso é tão importante quanto a técnica, e frequentemente ignorado por quem só estuda o lado ofensivo:
- **Autorização por escrito antes de qualquer teste** — sem contrato formal de escopo assinado, pentest é crime (Lei 12.737/2012, invasão de dispositivo informático) mesmo com boa intenção
- **Contrato de escopo bem definido** — o que pode e o que não pode ser testado, janela de tempo, responsabilidade sobre dano acidental
- **LGPD aplicada ao próprio trabalho de pentest** — você vai acessar dado sensível do cliente do seu cliente durante o teste; isso exige cuidado formal, não intuição
- **Seguro de responsabilidade civil profissional** — praticamente obrigatório pra operar com segurança jurídica real
- Recomendo, aqui sim, validação com advogado especializado em direito digital antes de fechar o primeiro contrato de pentest — mesmo padrão de cautela já aplicado ao AuraObra e ao AuraAgenda

**✅ Critério de saída da Fase 12:** você tem certificação reconhecida (mínimo eJPT, ideal OSCP), já praticou em plataforma legal o suficiente pra ter metodologia própria, e entende a parte contratual/legal o bastante pra não expor você ou o cliente a risco jurídico no primeiro trabalho.

### 12.6 — Credencial acadêmica formal (encontrado em conversa separada, nunca antes formalizado aqui)
Além da certificação técnica (eJPT/OSCP), existe decisão já tomada de trajetória acadêmica: depois de ADS + Licenciatura em Matemática, cursar **Ciência da Computação** (preferida sobre Engenharia de Software pela profundidade teórica — Compiladores, Sistemas Distribuídos, Grafos, Complexidade), seguida de **duas pós-graduações, nesta ordem: Cibersegurança primeiro, Arquitetura de Software depois**. Isso não substitui a Fase 12 nem a certificação — é credencial formal complementar, relevante principalmente se a trajetória incluir CLT em empresa estruturada, onde credencial formal pesa na progressão de carreira mais do que em ambiente de portfólio próprio.

### O que desenvolver/praticar — e um aviso importante
Toda prática técnica da Fase 12 (12.2 e 12.3) deve acontecer em **plataforma de treino legal isolada** (PortSwigger, TryHackMe, HackTheBox, ou aplicação deliberadamente vulnerável como OWASP Juice Shop/DVWA) — **nunca contra o AuraPOS ou qualquer sistema seu em produção com dado real de cliente**, mesmo sendo seu próprio sistema. Só depois de certificado e com metodologia madura, o primeiro teste contra um sistema real do seu portfólio deveria acontecer numa **cópia de homologação isolada**, com autorização formal por escrito de você mesmo enquanto responsável pelo produto (mesmo processo formal que você exigiria de um cliente) — é assim que se treina o hábito de nunca pular a etapa de autorização, mesmo quando parece desnecessário "porque é seu".

---

## FASE 12B — Segurança Defensiva (Blue Team, novo — nunca existia antes, complementa a Fase 12)

**Por que é fase própria, não item dentro da 12:** ofensiva (Red Team) e defensiva (Blue Team) são disciplinas com ferramental, mentalidade e certificação diferentes — quem ataca pensa em encontrar uma falha; quem defende pensa em detectar e conter, com volume de ruído muito maior pra filtrar. Empresa de segurança séria, ou profissional Purple Team, domina as duas, não só uma.

### 12B.1 — Quando começar
Depois da Fase 12.1-12.2 (fundamento de rede e metodologia ofensiva) — entender como o ataque funciona é pré-requisito real pra saber o que defender e por quê, mesma lógica já aplicada à Fase 12 inteira em relação ao desenvolvimento.

### 12B.2 — Fundamento de operação de defesa
- **SOC (Security Operations Center):** o que é, como opera, os três turnos de monitoramento contínuo
- **SIEM (Security Information and Event Management):** correlação de log de múltiplas fonte pra detectar padrão de ataque — ferramenta prática: **Wazuh** ou **Security Onion** (ambos gratuitos e open source, instaláveis em VM local)
- **DFIR (Digital Forensics and Incident Response):** o que fazer depois que um incidente já aconteceu — cadeia de custódia de evidência, contenção, erradicação, recuperação

### 12B.3 — Threat Hunting e análise de log
- Análise de log do Windows (Event Viewer, Sysmon) e do Linux (`journalctl`, `/var/log`)
- Hipótese de caça a ameaça: procurar atividade maliciosa que passou despercebida pelo alerta automático, não só reagir a alarme
- Reaproveita direto o MITRE ATT&CK já estudado na Fase 12 — mesmo framework, agora usado pra saber **o que procurar**, não **o que explorar**

### 12B.4 — Certificação de defesa (paralela ao eJPT/OSCP da Fase 12)
- **CompTIA CySA+** (Cybersecurity Analyst) — equivalente defensivo ao Security+/eJPT, bom primeiro objetivo mensurável
- **BTL1** (Blue Team Level 1, da Security Blue Team) — alternativa mais prática e mais barata que CySA+, bem avaliada pela comunidade
- **GCIH** (GIAC Certified Incident Handler) — padrão-ouro de resposta a incidente, equivalente defensivo ao OSCP em prestígio, mas mais caro

### 12B.5 — Aplicação direta no seu próprio portfólio
Diferente da Fase 12 (nunca testar sistema próprio antes de certificado), a Fase 12B **pode e deve** ser aplicada desde já nos seus próprios sistemas em produção — monitorar, não atacar, não tem o mesmo risco. Configurar log estruturado (já exigido pelo RNFT-E05) alimentando um SIEM simples é prática real de Blue Team, direto no AuraPOS.

**✅ Critério de saída da Fase 12B:** você consegue configurar um SIEM básico, interpretar alerta gerado por ele, e tem pelo menos uma certificação defensiva (mínimo CySA+ ou BTL1).

---

| Fase | Adição de profundidade sênior | Duração adicional estimada |
|---|---|---|
| 1 | Plano de execução de query, Git avançado | +2-3 dias |
| 2.1 | async/await real, tempo de vida de DI | +1 semana |
| 2.2 | Design de API maduro, OWASP aplicado, rate limiting | +1-2 semanas |
| 2.3 | Leitura de SQL gerado, `AsNoTracking`/projeção | +3-5 dias |
| 2.4 (nova) | Pirâmide de teste, integração, TDD | +1-2 semanas |
| 4 | DI ligada à arquitetura, refatoração deliberada | Sem tempo extra — aplicado dentro da Fase 4 já existente |
| 6 | Observabilidade movida de "depois" pra "agora" | +1 semana |
| 6C (nova) | Performance de memória (`Span<T>`, GC, benchmark) | +2-3 semanas, após produção |
| 12 (nova) | Segurança ofensiva completa até certificação (eJPT→OSCP) | +1-2 anos, trilha própria em paralelo |

**Tempo total revisado até MVP do AuraPOS com prática sênior:** ~16–21 semanas de estudo direto (vs. 12–16 do plano anterior), mais o tempo real de aplicação — o que, com 9h/semana e sua vida cheia de compromissos, continua sendo trabalho de mais de um ano em calendário corrido, não semanas.

---

## O que ainda não entra aqui, de propósito

Depois de adicionar as Fases 6C e 12, sobra pouco fora do escopo — mas vale registrar:
- **Pentest de infraestrutura/rede corporativa complexa, hardware hacking, engenharia social formal** — subespecialidades dentro do próprio universo ofensivo, que só fazem sentido depois da Fase 12 estar consolidada e a empresa já validada com pentest web, que é o ponto de entrada mais direto dado o resto do seu portfólio

---

## Honestidade sobre a escala real disso tudo junto

Você pediu pra não esconder nada — então não vou. Somando os dois grandes blocos:

- **Fases 0-6C** (desenvolvimento sênior do AuraPOS): ~17-22 semanas de estudo direto
- **Fase 12** (trilha de pentest até OSCP): isoladamente, **1 a 2 anos** de dedicação séria — é reconhecida no mercado de segurança como uma das certificações mais exigentes que existem, mesmo para quem já tem base forte de desenvolvimento

Rodando as duas coisas em paralelo (Fase 12 começa depois da Fase 4, sobrepondo Fases 5, 6, 6C), com 9h/semana dividido entre isso, os outros 20 sistemas do portfólio, duas graduações, escola e restaurante: **isso não é um plano de 1 ano, é um plano de 3 a 5 anos bem executado**, com o AuraPOS e a base de segurança ofensiva como os dois marcos mais importantes desse período, não como itens de checklist rápido.

Não digo isso pra desanimar — digo porque um plano que finge que isso cabe em meses seria um plano ruim, e você merece um real.
