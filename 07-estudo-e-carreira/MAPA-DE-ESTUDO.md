---
tags: [estudo, mapa, indice, portfolio-ams]
tipo: indice-central
atualizado: 2026-11-17
---

# 🗺️ MAPA DE ESTUDO — tudo o que você vai estudar, na ordem certa

> **O que é:** a lista completa do que você vai estudar em **todos** os seus planos (vault e dev-setup), **em ordem de dependência**: cada assunto só aparece depois de tudo o que ele precisa. Seguindo de cima para baixo, você nunca precisa parar para voltar em algo que devia ter estudado antes.
>
> **Não é para ler de ponta a ponta.** O dia a dia continua sendo o [Cartão](../CARTAO-voce-esta-aqui.md) ou o `just professor hoje`. Este mapa diz **o quê e em que ordem**; o [PLANO-PASSO-A-PASSO](PLANO-PASSO-A-PASSO.md) diz **quando** (calendário, rotina e entregáveis). Os dois seguem a mesma sequência de etapas.

## As 4 regras da ordem

1. **Pré-requisito antes, sempre.** Se B usa A, A vem antes, nem que seja no nível N1.
2. **Duas passadas.** Na 1ª passada você aprende o suficiente para usar (N1–N2) **logo antes** de precisar. A 2ª passada (↻) aprofunda (N3–N4) quando o assunto volta com mais peso. Isso evita estudar tudo a fundo antes de começar, e evita também usar algo sem base.
3. **Fundamento antes de ferramenta.** Como o computador, a rede e o banco funcionam vem antes do framework que os esconde.
4. **Cada etapa termina num ativo.** Não se passa de etapa sem o entregável dela (critério no plano).

## Como ler cada linha

| Nível | Nome | Quer dizer |
|---|---|---|
| N1 | Conhecer | Sabe o que é, para que serve e quando usar. Explica em 2 frases. |
| N2 | Usar | Faz funcionar com documentação aberta. |
| N3 | A fundo | Faz sem consulta, explica como funciona por dentro, resolve casos de borda. |
| N4 | Dominar | Ensina, decide trade-offs, revisa o trabalho dos outros e o da IA. Nível sênior. |

**Depende de:** os números dos assuntos que precisam vir antes. **Arquivo:** 📘 escrito (clique) · 📝 será escrito pelo [protocolo de escrita](#como-cada-arquivo-é-escrito) antes de você chegar nele. **↻** = 2ª passada de um assunto que já apareceu. **★** = cobrado em vaga de dev júnior/pleno.

**Nunca pausam** (correm por baixo de todas as etapas): inglês (todo dia) · matemática do VHSlins (sexta, na ordem da etapa) · Licenciatura · revisão espaçada (Anki) · base do Akita (terça, na ordem desta página).

---

## ETAPA 0 · A base de tudo · Mês 1, semanas 1–2

> O que tudo depende: saber estudar, pensar com precisão e entender o que é um computador. Sem isso, cada assunto seguinte vira decoreba.

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 0.1 | Aprender a aprender | 00 | Recuperação ativa, repetição espaçada, intercalação, Feynman, prática deliberada, 20/80, estudar com TDAH | N3 | — | [metodo-de-estudo](metodo-de-estudo.md) |
| 0.2 | Linguagem matemática e lógica | 01 | Proposição, conectivos, tabela-verdade, quantificadores, implicação | N3 | 0.1 | 📝 |
| 0.3 | Teoria dos conjuntos | 01 | Pertinência, inclusão, união, interseção, diferença, produto cartesiano | N3 | 0.2 | 📝 |
| 0.4 | Como o computador funciona | 03 | Bit, byte, binário, hexadecimal, CPU, memória, programa como sequência de instruções, o que é um sistema operacional | N2 ★ | 0.1 | 📝 |
| 0.5 | Representação de dados | 03 | Inteiros, complemento de dois, ponto flutuante IEEE 754 (por que `0.1 + 0.2 ≠ 0.3`), texto (ASCII, Unicode, UTF-8) | N2 ★ | 0.4 | 📝 |
| 0.6 | Lógica de programação | 04 | Variável, tipo, operadores, condição, laço, função, coleção, recursão, teste de mesa | N3 ★ | 0.2, 0.4 | 📘 [logica-de-programacao](assuntos/04-ciencia-da-computacao/logica-de-programacao.md) |
| 0.7 | Ler documentação e inglês técnico | 00 | Documentação oficial, man pages, mensagens de erro, vocabulário técnico | N2 ★ | — | 📝 |

**Ativo da etapa:** os 3 exercícios de lógica resolvidos no papel e no TS Playground.

## ETAPA 1 · A máquina e as ferramentas · Mês 1, semanas 2–4

> Antes de programar de verdade, você precisa operar a máquina onde o código vive: sistema operacional, terminal, controle de versão e o seu setup.

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 1.1 | Sistema operacional: o essencial | 05 | Kernel, processo, arquivo, sistema de arquivos, usuário, permissão, memória (visão geral) | N2 ★ | 0.4 | 📝 |
| 1.2 | WSL2 e virtualização | 05 | Hypervisor, máquina virtual, WSL2, onde ficam os arquivos | N2 | 1.1 | 📝 |
| 1.3 | Terminal Linux e shell | 05 | Navegar, ler, procurar, pipes, redirecionamento, permissões, processos, variáveis de ambiente, script básico | N3 ★ | 1.1, 1.2 | 📘 [terminal-linux](assuntos/05-sistemas-operacionais/terminal-linux.md) |
| 1.4 | Criptografia: o essencial | 13 | Hash, sal, chave simétrica e assimétrica, par de chaves, assinatura (o que cada um garante) | N1 ★ | 0.5 | 📝 |
| 1.5 | Git e controle de versão | 08 | Commit, branch, merge, PR, conflitos, desfazer, hash do commit | N3 ★ | 1.3, 1.4 | 📘 [git](assuntos/08-engenharia-de-software/git.md) |
| 1.6 | Segredos | 12 | KeePassXC, sops/age, variáveis de ambiente, nunca no Git | N3 ★ | 1.4, 1.5 | 📝 |
| 1.7 | Backup e recuperação | 12 | restic, retenção, restaurar de verdade, snapshots | N3 | 1.3 | 📝 |
| 1.8 | Containers e Docker | 12 | Imagem, container, Dockerfile, Compose, volume, porta; container × VM | N2 ★ | 1.1, 1.2, 1.3 | 📝 |
| 1.9 | `just` e o Núcleo | 12 | Porta única de comandos, banco central, agenda, auditoria | N2 | 1.3 | 📝 |
| 1.10 | Segurança de agentes de IA | 16 | ai-jail, sem credencial de produção, ler o comando antes de aprovar, revisar o que a IA fez | N3 | 1.3, 1.5 | 📝 |

**Ativo da etapa:** setup instalado e operado por você; repositório `logica-ts` no GitHub com histórico limpo; um backup restaurado.

## ETAPA 2 · Programar de verdade · Mês 1 (fim) → Mês 2

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 2.1 | TypeScript: fundamentos | 07 | Tipos, inferência, union, funções, objetos, `type`/`interface`, arrays, `map/filter/reduce`, módulos | N2 ★ | 0.5, 0.6, 1.3 | 📘 [typescript-fundamentos](assuntos/07-linguagens/typescript-fundamentos.md) |
| 2.2 | Programação funcional: o essencial | 04 | Função pura, imutabilidade, função de ordem superior, closure, composição | N2 ★ | 2.1 | 📝 |
| 2.3 | Estruturas de dados básicas e Big-O | 04 | Array, lista, pilha, fila, hash map, set; noção de O(1), O(n), O(n²) | N2 ★ | 0.6, 2.1 | 📝 |
| 2.4 | Testes automatizados: o essencial | 08 | Teste de unidade, asserção, caso-limite, Vitest, rodar no terminal | N2 ★ | 2.1 | 📝 |
| 2.5 | Debugging como método | 00 | Reproduzir, isolar, hipótese, depurador, teste que prova | N2 ★ | 2.1, 2.4 | 📝 |
| 2.6 | Erros e assincronia: o essencial | 07 | `try/catch`, `Promise`, `async/await`, o que é I/O | N2 ★ | 1.1, 2.1 | 📝 |
| 2.7 | Porcentagem e juros | 01 | Porcentagem, aumento e desconto, juros simples e compostos | N3 ★ | 0.2 | 📝 |
| 2.8 | Representações e potências | 01 | Bases numéricas, potências, notação científica, logaritmos (base do Big-O) | N2 | 0.5 | 📝 |

**Ativo da etapa:** `logica-ts` com testes passando no terminal; um script TypeScript que lê CSV e gera relatório.

## ETAPA 3 · Como a web funciona · Mês 2

> Antes do primeiro site no ar: o que acontece entre digitar um endereço e a página aparecer.

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 3.1 | Redes: o essencial | 06 | Camadas TCP/IP, IP, porta, cliente-servidor, TCP × UDP, DNS | N2 ★ | 1.1, 1.3 | 📝 |
| 3.2 | HTTP e HTTPS | 06 | Métodos, status, cabeçalhos, cookies, cache, CORS, TLS (usa 1.4) | N2 ★ | 3.1, 1.4 | 📝 |
| 3.3 | A jornada de uma requisição | 06 | DNS → TCP → TLS → HTTP → servidor → resposta; proxy, CDN | N2 ★ | 3.1, 3.2 | 📝 |
| 3.4 | Diagnóstico de rede | 06 | ping, dig, curl, ss, ferramentas do navegador | N2 ★ | 3.1 | 📝 |
| 3.5 | HTML e CSS | 09 | Semântica, formulários, box model, flexbox, grid, responsivo | N3 ★ | 3.2 | 📝 |
| 3.6 | JavaScript no navegador | 09 | DOM, eventos, `fetch`, armazenamento | N2 ★ | 2.1, 2.6, 3.5 | 📝 |
| 3.7 | React | 09 | Componentes, props, estado, hooks, renderização | N2 ★ | 3.6 | 📝 |
| 3.8 | Next.js e Tailwind | 09 | Rotas, server e client components, estilos utilitários | N2 ★ | 3.7 | 📝 |
| 3.9 | CI/CD: o essencial | 12 | GitHub Actions, testes a cada push, `just check` como portão | N2 ★ | 1.5, 2.4 | 📝 |
| 3.10 | Deploy de site | 12 | Vercel, Hostinger por push, domínio e DNS (usa 3.1) | N2 ★ | 3.8, 3.9 | 📝 |
| 3.11 | Revisar código de IA (R-1) | 16 | Checklist de PR, ler diff, explicar cada linha | N2 ★ | 1.5, 2.4 | 📝 |
| 3.12 | Go: ferramentas (Go-1, Go-2) | 07 | Tipos, structs, funções, erros como valor, binário, arquivos | N2 | 1.3, 2.1 | [trilha-go-ferramentas](trilha-go-ferramentas.md) |
| 3.13 | Contabilidade: o essencial | 18 | Débito e crédito, regime de caixa e competência, fluxo de caixa | N2 | 2.7 | 📝 |
| 3.14 | Preço de serviço | 18 | Hora mínima, custo, margem, proposta | N2 | 2.7, 3.13 | 📝 |

**Ativo da etapa:** 1 site de cliente no ar pela esteira, com PRs revisados; 1 CLI em Go que você usa.

## ETAPA 4 · Dados e back-end · Mês 3

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 4.1 | Modelagem relacional | 10 | Entidade, relacionamento, chave primária e estrangeira, normalização | N2 ★ | 0.3, 2.3 | 📝 |
| 4.2 | SQL | 07 | SELECT, WHERE, JOIN, GROUP BY, subconsulta, INSERT/UPDATE/DELETE, DDL (álgebra de conjuntos aplicada) | N3 ★ | 0.3, 4.1 | 📝 |
| 4.3 | PostgreSQL: o essencial | 10 | Tipos, constraints, índices (noção de B-tree), transação e ACID (noção) | N2 ★ | 4.2, 1.8 | 📝 |
| 4.4 | POO | 04 | Classe, objeto, encapsulamento, interface, polimorfismo, composição, injeção de dependência | N2 ★ | 2.1, 2.2 | 📘 [poo](assuntos/04-ciencia-da-computacao/poo.md) |
| 4.5 | Requisitos e histórias | 08 | Requisito funcional e não funcional, história de usuário, critério de aceite | N2 ★ | — | 📝 |
| 4.6 | Arquitetura em camadas: o essencial | 08 | Domínio separado de infraestrutura, repository, por que a regra não conhece o banco | N2 ★ | 4.4 | 📝 |
| 4.7 | APIs REST e contratos | 09 | Recursos, rotas, status corretos, OpenAPI, paginação, validação com Zod | N2 ★ | 3.2, 2.1 | 📝 |
| 4.8 | Back-end com NestJS | 09 | Módulos, controllers, providers, injeção de dependência | N2 ★ | 4.4, 4.6, 4.7 | 📝 |
| 4.9 | ORM e migrations | 10 | Prisma/Drizzle, migration versionada, relacionamentos, N+1 | N2 ★ | 4.3, 4.8 | 📝 |
| 4.10 | Autenticação e autorização | 09 | Senha com hash (usa 1.4), sessão, cookie, JWT, OAuth (noção), RBAC, Row-Level Security | N2 ★ | 1.4, 3.2, 4.8 | 📝 |
| 4.11 | OWASP Top 10 | 13 | Injeção, controle de acesso quebrado, XSS, SSRF, configuração insegura | N2 ★ | 3.2, 4.2, 4.10 | 📝 |
| 4.12 | Testes de integração e teste antes do código (R-2) | 08 | Teste de API, banco de teste, escrever o teste e deixar o agente implementar | N2 ★ | 2.4, 4.8 | 📝 |
| 4.13 | Como a IA funciona: o essencial | 15 | Token, contexto, modelo, prompt, alucinação, custo | N1 ★ | 0.4 | 📝 |
| 4.14 | IA em TypeScript (IA-T1) | 15 | Chamar modelo pela API, saída estruturada validada com Zod, custo por chamada | N2 ★ | 4.7, 4.13 | 📝 |
| 4.15 | Arduino: primeiro protótipo | 19 | Entradas, saídas, sensor, LED (usa a eletricidade da física) | N2 | 0.6, física T1 | [trilha-robotica-iot](trilha-robotica-iot.md) |

**Ativo da etapa:** esqueleto do AM Gestão com API, banco, autenticação e teste no CI; planilha do financeiro à venda; 1ª chamada de IA no produto.

## ETAPA 5 · O produto com dinheiro de verdade · Meses 4–5

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 5.1 | Dinheiro no código | 17 | Centavos inteiros, decimal × float (usa 0.5), arredondamento, moeda | N3 ★ | 0.5, 2.1 | 📝 |
| 5.2 | Concorrência e paralelismo | 05 | Processo × thread, condição de corrida, deadlock, mutex, event loop por dentro | N2 ★ | 1.1, 2.6 | 📝 |
| 5.3 | ↻ Transações a fundo | 10 | Níveis de isolamento, locks, concorrência otimista, deadlock no banco | N3 ★ | 4.3, 5.2 | 📝 |
| 5.4 | Idempotência e pagamentos | 17 | Chave de idempotência, retry seguro, efeito externo irreversível | N3 | 4.7, 5.3 | 📝 |
| 5.5 | Matemática financeira | 18 | Juros compostos, VPL, TIR, SAC, Price | N3 | 2.7 | 📝 |
| 5.6 | Ledger de partidas dobradas | 17 | Lançamento, débito/crédito (usa 3.13), saldo derivado, imutabilidade | N3 | 3.13, 5.1, 5.3 | 📝 |
| 5.7 | SQLite e offline | 10 | Banco local, sincronização, conflito | N2 | 4.3, 5.3 | 📝 |
| 5.8 | Go: HTTP e agente fiscal (Go-3 a Go-6) | 07 | CSV/JSON, automação, servidor HTTP, impressora ESC/POS | N2 | 3.12, 3.2 | [trilha-go-ferramentas](trilha-go-ferramentas.md) |
| 5.9 | Fiscal | 17 | NFC-e, NFS-e, o papel do agente local | N2 | 5.8 | 📝 |
| 5.10 | Especificação para agentes (R-3) | 16 | CLAUDE.md por projeto, pedido sem ambiguidade, regras do produto | N3 | 3.11, 4.12 | 📝 |
| 5.11 | Linux: administração | 05 | Usuários, systemd, pacotes, logs, timers | N2 ★ | 1.3 | 📝 |
| 5.12 | SSH e acesso remoto | 06 | Chaves (usa 1.4), túnel, servidor remoto | N2 ★ | 1.4, 3.1 | 📝 |
| 5.13 | Deploy em servidor e os 12 fatores | 12 | VPS, Docker em produção, Kamal, configuração no ambiente, rollback de um comando | N2 ★ | 1.8, 3.10, 5.11, 5.12 | 📝 |
| 5.14 | Geometria e PostGIS | 01 · 10 | Coordenadas, distância, SRID, consulta espacial | N2 | 4.3 | 📝 |
| 5.15 | Vetores: o essencial | 01 | Vetor, comprimento, produto escalar, similaridade de cosseno | N2 | 2.8 | 📝 |
| 5.16 | RAG e embeddings (IA-T2) | 15 | Embedding (usa 5.15), chunking, pgvector, busca por similaridade, citação | N2 ★ | 4.14, 5.15, 4.3 | 📝 |
| 5.17 | Tempo real | 11 | WebSocket, SSE (pedidos em tempo real) | N1 | 3.2 | 📝 |

**Ativo da etapa:** módulo Caixa com impressão real; MVP (Caixa + Pedidos + Financeiro) rodando num restaurante; busca com IA no produto.

## ETAPA 6 · Produção de verdade · Mês 6

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 6.1 | Observabilidade | 12 | Logs estruturados, métricas, traces, alertas | N2 ★ | 5.13 | 📝 |
| 6.2 | ↻ Testes a fundo | 08 | Testes de propriedade, cenário/E2E, mocks, cobertura | N3 ★ | 4.12, 5.4 | 📝 |
| 6.3 | Avaliar IA (R-4) | 15 · 16 | Conjunto de perguntas com resposta esperada, nota no CI | N2 | 5.16, 3.9 | 📝 |
| 6.4 | Modelagem de ameaças | 13 | STRIDE, ativos, superfície de ataque | N2 | 4.11 | 📝 |
| 6.5 | LGPD e privacidade | 13 | Dados pessoais, bases legais, incidente | N2 ★ | 4.10 | 📝 |
| 6.6 | Segurança do Linux e da rede | 13 | Hardening, firewall, SSH seguro, mínimo privilégio | N2 | 5.11, 5.12 | 📝 |
| 6.7 | DevSecOps | 13 | CodeQL, Trivy, Dependabot, gitleaks, revisão automática de PR | N2 ★ | 3.9, 4.11 | 📝 |
| 6.8 | Relato de incidente | 13 | Linha do tempo, causa, correção, prevenção | N2 | 6.1 | 📝 |

**Ativo da etapa:** MVP estável com alertas, backup restaurado, rollback testado; 10 planilhas vendidas.

## ETAPA 7 · Dados, Python e IA · Meses 7–9

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 7.1 | Estatística descritiva | 01 | Média, mediana, variância, desvio-padrão, distribuições, gráficos | N3 | 2.7 | 📝 |
| 7.2 | Python | 07 | Sintaxe, tipos, coleções, funções, classes, módulos, ambientes virtuais | N3 ★ | 2.1, 4.4 | 📝 |
| 7.3 | Python para dados | 15 | NumPy, pandas, visualização, notebooks | N2 ★ | 7.1, 7.2 | 📝 |
| 7.4 | ↻ SQL avançado e índices | 10 | Window functions, CTE, EXPLAIN, índice composto, plano de execução | N3 ★ | 4.2, 2.3 | 📝 |
| 7.5 | ↻ Estruturas de dados: árvores e grafos | 04 | Árvore de busca, balanceada, heap, trie, grafo (base dos índices B-tree) | N3 ★ | 2.3 | 📝 |
| 7.6 | Contagem e probabilidade | 01 | Combinação, permutação, probabilidade condicional, Bayes | N3 | 0.3, 7.1 | 📝 |
| 7.7 | Álgebra linear | 01 | Matrizes, multiplicação, transformações, autovalores (noção) | N2 → N3 | 5.15 | 📝 |
| 7.8 | Machine learning clássico | 15 | Regressão, classificação, validação, overfitting, scikit-learn | N2 | 7.3, 7.6, 7.7 | 📝 |
| 7.9 | Back-end em Python | 09 | FastAPI, Pydantic, async | N2 | 7.2, 4.7 | 📝 |
| 7.10 | Tributação brasileira | 18 | Simples Nacional, Fator R, NFS-e, carnê-leão, conciliação | N2 | 3.13 | 📝 |
| 7.11 | Pix e Pix Automático | 17 | API do Pix, QR Code, webhooks, devolução (usa 5.4) | N2 | 5.4 | 📝 |
| 7.12 | Custo e roteamento de IA (R-5) | 15 · 16 | Tokens, cache de prompt, IA local × online, modelo certo por tarefa | N3 | 4.14, 6.3 | 📝 |
| 7.13 | Gerenciamento de memória | 05 | Stack × heap, coletor de lixo, vazamento, ponteiros (noção) | N2 ★ | 5.2 | 📝 |
| 7.14 | Arquitetura de computadores | 03 | CPU por dentro, cache, hierarquia de memória, GPU, memória de vídeo (por que um modelo de 8B pesa) | N2 | 0.4, 7.13 | 📝 |
| 7.15 | Deep learning: o essencial | 15 | Rede neural, gradiente, treino, transformer (noção), PyTorch | N1 → N2 | 7.7, 7.8 | 📝 |
| 7.16 | IA local | 15 | Ollama, quantização, memória de GPU, Hugging Face | N2 | 7.14, 5.16 | 📝 |
| 7.17 | ↻ Conceitos de SO | 05 | Escalonamento, memória virtual, syscalls, I/O bloqueante × não bloqueante | N3 ★ | 5.2, 7.13 | 📝 |
| 7.18 | ESP32 e Raspberry Pi | 19 | Wi-Fi, MQTT, GPIO, Linux embarcado | N2 | 4.15, 5.11 | 📝 |

**Ativo da etapa:** dashboard de dados do produto; 5 clientes pagantes; assistente com IA local no AM Gestão.

## ETAPA 8 · Senioridade · Meses 10–12

| # | Assunto | Área | Conceitos | Nível | Depende de | Arquivo |
|---|---|---|---|---|---|---|
| 8.1 | ↻ POO e princípios SOLID | 04 · 08 | SRP, OCP, LSP, ISP, DIP; composição × herança com argumento | N4 ★ | 4.4, 4.6 | 📘 [poo](assuntos/04-ciencia-da-computacao/poo.md) |
| 8.2 | Padrões de projeto | 08 | Strategy, Factory, Adapter, Observer, Repository, Decorator | N3 ★ | 8.1 | 📝 |
| 8.3 | Código limpo e refatoração | 08 | Code smells, refatorar com teste, passos pequenos | N4 ★ | 6.2, 8.1 | 📝 |
| 8.4 | ↻ Arquitetura de software | 08 | Hexagonal, Clean Architecture, monólito modular × microsserviços, ADR | N4 ★ | 4.6, 8.1 | 📝 |
| 8.5 | Domain-Driven Design | 08 | Linguagem ubíqua, entidade, objeto de valor, agregado, contexto delimitado | N3 | 8.4 | 📝 |
| 8.6 | Modelagem e documentação | 08 | UML essencial, C4, OpenAPI, README e ADR públicos | N3 | 8.4 | 📝 |
| 8.7 | Performance e escalabilidade | 11 | Medir antes, gargalo, stateless, balanceamento | N3 ★ | 6.1, 7.4 | 📝 |
| 8.8 | Cache | 11 | Onde cachear, invalidação, Redis, CDN | N3 ★ | 8.7 | 📝 |
| 8.9 | Mensageria | 11 | Filas, pub/sub, outbox, idempotência do consumidor (usa 5.4) | N3 | 5.4, 8.7 | 📝 |
| 8.10 | Consistência em sistemas distribuídos | 11 | Consistência eventual, CAP/PACELC, conflitos | N2 → N3 | 5.3, 8.9 | 📝 |
| 8.11 | ↻ Algoritmos clássicos e complexidade | 04 | Ordenação, busca binária, BFS/DFS, Dijkstra, programação dinâmica, guloso, backtracking, Big-O formal | N4 ★ | 7.5, 2.8 | 📝 |
| 8.12 | System design | 11 | Requisitos, estimativa de carga, desenho, trade-offs em 45 min | N4 ★ | 8.4, 8.7–8.10 | 📝 |
| 8.13 | Orquestrar agentes (R-6) | 16 | Worktrees, agentes em paralelo, revisão automática de PR | N3 | 5.10, 7.12 | 📝 |
| 8.14 | Entrevista técnica | 24 | Algoritmos em voz alta, system design, comportamental (STAR) | N4 ★ | 8.11, 8.12 | 📝 |
| 8.15 | Portfólio e GitHub em inglês | 24 | Estudos de caso, ADRs, contribuição open source | N3 ★ | 8.6 | 📝 |
| 8.16 | Finanças corporativas e valuation | 18 | Fluxo de caixa descontado, múltiplos, análise de balanço (usa 5.5) | N2 | 5.5 | 📝 |
| 8.17 | Boot, sistemas de arquivos e o AMtech OS | 05 | BIOS/UEFI, bootloader, init, BTRFS, snapshots, camada sobre Ubuntu | N3 | 7.17, 5.11 | 📝 |

**Ativo da etapa:** AM Gestão refatorado com system design documentado; portfólio em inglês; AMtech OS v1; renda rumo a R$ 7 mil/mês.

---

## HORIZONTE · Depois dos 12 meses, ativo no roteiro

> Mesma regra: cada linha só depois das que ela cita. As trilhas do horizonte andam uma pesada por vez.

### H1 · Ciência da computação e baixo nível

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H1.1 | Eletrônica digital | Portas lógicas, álgebra booleana (usa 0.2), circuitos combinacionais e sequenciais | N3 | 0.2, 7.14 |
| H1.2 | C | Ponteiros, memória manual, structs, Makefile, gdb, valgrind (École 42, Circles 00–02) | N3 | 7.13, 1.3 |
| H1.3 | Assembly | x86-64 e ARM64, registradores, stack frame | N2 → N3 | H1.1, H1.2 |
| H1.4 | C++ | RAII, classes, templates, STL (École 42, Circles 03–06) | N3 | H1.2, 8.1 |
| H1.5 | Compiladores e interpretadores | Léxico, AST, gramática (BNF), JIT, bytecode | N2 → N3 | H1.2, 7.5 |
| H1.6 | Teoria da computação | Autômatos, linguagens formais, máquina de Turing (Sipser) | N2 | 0.2, 7.6 |
| H1.7 | Teoria da informação | Entropia, compressão, códigos de erro (Shannon) | N2 | 7.6 |
| H1.8 | Sistemas embarcados | Microcontrolador, GPIO, PWM, I2C, SPI, UART, firmware | N3 | H1.1, H1.2, 7.18 |
| H1.9 | Rust | Ownership, borrowing, lifetimes, traits | N2 | H1.2 |
| H1.10 | Linux internals | Kernel, VFS, drivers, módulos, LFS/BLFS | N3 | 7.17, H1.2 |
| H1.11 | Windows internals | Arquitetura NT, Win32/NT API, registro, NTFS, tokens, UAC | N3 | 7.17 |
| H1.12 | macOS e iOS internals | Darwin/XNU, launchd, APFS, SIP, Secure Enclave, Mach-O | N2 | 7.17 |
| H1.13 | AM Linux e AM-OS | Distribuição própria e sistema operacional próprio | N3 | H1.10, H1.3, 8.17 |

### H2 · Redes a fundo

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H2.1 | ↻ Endereçamento e sub-redes | IPv4, IPv6, CIDR, MAC, ARP | N4 | 3.1 |
| H2.2 | Sinais e correção de erros | Transmissão digital, paridade, checksum, CRC | N2 | 3.1, H1.7 |
| H2.3 | Infraestrutura de rede | Switch, roteador, VLAN, NAT, firewall, proxy, balanceador, CDN | N3 | H2.1 |
| H2.4 | Roteamento | Tabelas, gateway, OSPF e BGP (noção) | N3 | H2.3 |
| H2.5 | VPN e rede segura | WireGuard, Tailscale, NAS, rede isolada do laboratório | N3 | 5.12, H2.3 |
| H2.6 | Wi-Fi | 802.11, canais, WPA2/WPA3 | N2 | H2.3 |
| H2.7 | ↻ Diagnóstico avançado | tcpdump, Wireshark | N3 | 3.4, H2.3 |

Certificações: CompTIA Network+ → CCNA (opcional).

### H3 · Segurança ofensiva

> Só em laboratório próprio ou com autorização por escrito. Trilha completa: [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md).

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H3.1 | ↻ Criptografia a fundo | AES, RSA (usa H6.1), curvas elípticas, certificados, PKI | N3 | 1.4, H6.1 |
| H3.2 | Metodologia e lei | PTES, OWASP Testing Guide, escopo, autorização, Lei 12.737, Marco Civil | N4 | 6.4 |
| H3.3 | Reconhecimento | OSINT, DNS, varredura de portas (nmap), fingerprinting | N3 | H2.3, H3.2 |
| H3.4 | Web hacking | SQLi, XSS, CSRF, SSRF, IDOR, upload, desserialização, Burp Suite | N4 | 4.11, H3.3 |
| H3.5 | Bypass e evasão | WAF evasion, burlar proxy e firewall (túneis), bypass de autenticação e de controles do cliente, evasão de antivírus/EDR, bypass de UAC/AMSI | N3 | H3.4, H2.5, H1.11 |
| H3.6 | Escalada de privilégios | Linux (SUID, sudo, cron, kernel) e Windows (serviços, tokens, registro) | N3 | H1.10, H1.11 |
| H3.7 | Active Directory | Kerberos, NTLM, enumeração, kerberoasting, movimento lateral | N3 | H1.11, H3.6 |
| H3.8 | Pivoting e tunneling | Port forwarding, SOCKS, chisel, ligolo | N3 | H2.5, H3.6 |
| H3.9 | Wireless | Ataques a WPA2/WPA3 | N2 | H2.6 |
| H3.10 | Engenharia reversa | Ghidra, depurador, análise estática e dinâmica | N3 | H1.3 |
| H3.11 | Desenvolvimento de exploit | Buffer overflow, ROP, shellcode, ASLR, DEP | N3 | H1.3, H3.10 |
| H3.12 | Análise de malware | Sandbox, comportamento, indicadores | N2 | H3.10 |
| H3.13 | C2 e OPSEC | Comando e controle, OPSEC, deception | N2 | H3.5, H3.8 |
| H3.14 | Engenharia social | Só em exercício autorizado; conscientização | N2 | H3.2 |
| H3.15 | Cloud e mobile security | IAM, buckets, Android e iOS básicos | N2 | H5.3, H1.12 |
| H3.16 | Relatório de pentest | CVSS, evidência, recomendação, sumário executivo | N4 | H3.4 |
| H3.17 | Blue team e forense | Detecção, SIEM (noção), linha do tempo, análise de memória e disco | N2 → N3 | 6.8, H3.12 |

Certificações: CompTIA A+ e Network+ → Security+ → eJPT → BSCP → OSCP → OSWE e OSEP.

### H4 · IA a fundo

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H4.1 | Cálculo | Limite, derivada, integral, gradiente | N3 | H6.2, 7.7 |
| H4.2 | ↻ Deep learning | Backpropagation, CNN, transformer por dentro | N3 | H4.1, 7.15 |
| H4.3 | Engenharia de dados | ETL/ELT, pipelines, qualidade de dados, data warehouse | N3 | 7.3, 7.4 |
| H4.4 | Agentes e MCP | Loop de ferramentas, MCP, orquestração, limites | N3 | 8.13, 7.12 |
| H4.5 | Treinar e ajustar modelos | Treino pequeno do zero, fine-tuning, LoRA/QLoRA, modelo de 8B | N3 | H4.2, 7.16 |
| H4.6 | MLOps | Versionar dados e modelos, servir, monitorar | N2 | H4.5, 6.1 |
| H4.7 | Voz e visão | Whisper, Piper, Frigate (Jarvis e casa) | N2 | 7.16 |

### H5 · Infraestrutura e nuvem a fundo

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H5.1 | Infraestrutura como código | Terraform, Ansible, receitas idempotentes | N3 | 5.13 |
| H5.2 | Kubernetes | Pod, deployment, service, ingress | N2 | 1.8, H2.3 |
| H5.3 | Nuvem | Azure (AZ-900, AI-200), AWS (Cloud Practitioner), custos | N3 | 5.13 |
| H5.4 | Homelab | Servidor da casa, VMs, rede isolada, monitoramento | N3 | H2.5, 6.1 |
| H5.5 | Arch Linux e Omarchy | Instalação manual, pacman/AUR, Wayland/Hyprland | N3 | 5.11, 8.17 |

### H6 · Matemática, física e economia a fundo

| # | Assunto | Conceitos | Nível | Depende de |
|---|---|---|---|---|
| H6.1 | Teoria dos números | Divisibilidade, primos, Euclides, aritmética modular | N3 | 0.2 |
| H6.2 | Álgebra e funções | Equações, inequações, funções (VHSlins) | N3 | 0.2 |
| H6.3 | Matemática discreta | Indução, relações, grafos, combinatória | N3 | 0.3, 7.6 |
| H6.4 | Números complexos | Forma algébrica e trigonométrica | N2 | H6.2 |
| H6.5 | Matemática avançada | Análise real, álgebra abstrata, topologia, EDO | N1 → N2 | H4.1 |
| H6.6 | Física: mecânica, eletromagnetismo, termodinâmica | Cinemática, dinâmica, energia, indutância, calor, entropia | N2 | H4.1 |
| H6.7 | Mercado financeiro e regulação | CVM, ANBIMA, B3, fundos, regras de recomendação | N3 | 8.16 |
| H6.8 | Economia | Micro, macro, inflação, juros, câmbio, econometria (faculdade) | N3 | 7.1, 8.16 |
| H6.9 | Finanças quantitativas | Séries temporais, risco, otimização de carteira | N2 | H6.8, 7.8 |

O livro do VHSlins anda às sextas na ordem das etapas (a parte de cada etapa está no [mapa capítulo a capítulo](matematica-e-desenvolvimento-integrado.md)); H6.1 e H6.2 podem começar antes, pelo livro, sem esperar o fim dos 12 meses. Física: grandezas e eletricidade no T1 (sábado), antes de 4.15. Certificações de finanças: CNPI → consultor CVM → CGA/CGE → CFP → CFA.

### H7 · Outras frentes

| # | Assunto | Conceitos | Depende de |
|---|---|---|---|
| H7.1 | Casa inteligente e Jarvis | Home Assistant, Zigbee, automações, voz | 7.18, H4.7 |
| H7.2 | Robótica móvel e agro | Motores, PID, visão, sensores de solo | 7.18, H6.6 |
| H7.3 | Blockchain | Hash e assinatura (usa 1.4), consenso, Ethereum, contratos | H3.1, 8.10 |
| H7.4 | Construção civil pela TI | BIM/IFC, SINAPI | 7.2 |
| H7.5 | Empreendedorismo, marketing e vendas | Validar antes de construir, funil, tráfego pago, proposta, infoprodutos, consultoria | contínuo desde a Etapa 3 |
| H7.6 | Didática e produção de conteúdo | Planejar aula, avaliar, post técnico mensal, curso | contínuo |
| H7.7 | Espanhol | Depois do B1 em inglês | inglês B1 |
| H7.8 | Formação formal | Licenciatura (em curso), ENEM 2027, Ciências Econômicas, CC ou IA | [formacao-academica](formacao-academica.md) |

---

## Como cada arquivo é escrito

Para não estudar conteúdo raso, desatualizado ou com erro, cada 📝 só vira 📘 depois destes passos:

1. **Fonte primária primeiro:** documentação oficial, especificação ou livro de referência, na **versão atual** (anotada no arquivo).
2. **Pesquisa do momento:** o que mudou recentemente e o que o mercado cobra hoje, com fonte e data.
3. **Akita:** só episódios e posts que tratam do assunto de verdade, conferidos antes de citar.
4. **Todo código do arquivo é executado** antes de entrar (TypeScript, Python, shell), com a versão usada anotada.
5. **Conferência dos fatos:** datas, nomes e números checados contra a fonte; o que não deu para confirmar sai do arquivo.
6. **Cabeçalho de validade:** `verificado-em`, versões e fontes. Se a versão mudar muito, o arquivo volta para revisão.
7. **Profundidade de verdade:** cada arquivo segue o [modelo](assuntos/_MODELO.md) inteiro, com o "como funciona por baixo" e exercícios N1–N4; nada de resumo de uma tela.

Os 5 arquivos 📘 escritos antes desta ordem (lógica, terminal, Git, TypeScript e POO) **passam por esse protocolo de novo** antes de serem estudados.
