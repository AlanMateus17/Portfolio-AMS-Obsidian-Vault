---
tags: [estudo, mapa, indice, portfolio-ams]
tipo: indice-central
atualizado: 2026-11-17
---

# 🗺️ MAPA DE ESTUDO — tudo o que você vai estudar, num lugar só

> **O que é:** a lista completa de áreas, assuntos e conceitos de **todos** os seus planos (vault e dev-setup), com o nível que cada um precisa e quando entra. **Não é para ler de ponta a ponta.** O dia a dia continua sendo o [Cartão](../CARTAO-voce-esta-aqui.md) ou o `just professor hoje`. Abra este mapa só para achar um assunto ou ver onde ele se encaixa.
>
> **Quando** e **em que ordem**: [PLANO-PASSO-A-PASSO](PLANO-PASSO-A-PASSO.md) (fonte única). **Como estudar:** [metodo-de-estudo](metodo-de-estudo.md). Os arquivos `trilha-*` e o [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) viram material de referência: o que estava neles está aqui.

## Como ler cada linha

**Nível-alvo** (o que "dominar" quer dizer para aquele assunto):

| Nível | Nome | Quer dizer |
|---|---|---|
| N1 | Conhecer | Sabe o que é, para que serve e quando usar. Explica em 2 frases. |
| N2 | Usar | Faz funcionar com documentação aberta. |
| N3 | A fundo | Faz sem consulta, explica como funciona por dentro, resolve casos de borda e erros. |
| N4 | Dominar | Ensina (aula dada de verdade), decide trade-offs, revisa o trabalho dos outros e o da IA. É o nível sênior. |

**Quando:** `M1`…`M12` = mês do plano de 12 meses · `T1`…`T4` = trimestre · `H` = horizonte longo, ativo no roteiro sem mês fixo · `∞` = contínuo.
**Arquivo:** 📘 = arquivo do assunto já escrito (clique) · 📝 = será escrito na semana anterior ao estudo dele.
**★** = cobrado em vaga de dev júnior/pleno hoje.

Cada arquivo de assunto segue o [modelo](assuntos/_MODELO.md): o que é, por que existe, como funciona por baixo, conceitos, qualidades, defeitos, quando usar, erros comuns, no seu setup e no AM Gestão, o que o mercado cobra, exercícios N1–N4, fontes e critério de domínio.

---

## 00 · Aprender a aprender

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Método de estudo | Recuperação ativa, repetição espaçada (1/3/7/21/60/120 dias), intercalação, dificuldade desejável, Feynman, prática deliberada, 20/80 em 2 passadas | N4 | M1 · `b-aprender` | [metodo-de-estudo](metodo-de-estudo.md) |
| Estudar com TDAH | Uma porta só, blocos de 25 min, um objetivo por bloco, ambiente sem distração, rotina âncora | N3 | ∞ | 📝 |
| Ler documentação e fontes primárias | Documentação oficial, RFC, man pages, código-fonte, changelog; inglês técnico | N3 ★ | ∞ | 📝 |
| Debugging como método | Reproduzir, isolar, hipótese, medir, corrigir, teste que prova | N4 ★ | M1→∞ | 📝 |
| Escrita técnica | Nota, README, ADR, post, relatório; escrever para ensinar | N3 | ∞ | 📝 |

## 01 · Matemática

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Linguagem matemática e lógica | Proposição, conectivos, tabela-verdade, quantificadores, implicação, demonstração | N4 | M1 · `mat-linguagem` | 📝 |
| Teoria dos conjuntos | Pertinência, inclusão, união, interseção, diferença, complemento, produto cartesiano | N4 | M1 · `mat-conjuntos` | 📝 |
| Teoria dos números | Divisibilidade, primos, MDC/MMC, Euclides, aritmética modular, congruência (base do RSA) | N3 | T1–T2 | 📝 |
| Álgebra | Expressões, equações, inequações, funções, potências, logaritmos | N3 | T1–T2 · `mat-potencias-log` | 📝 |
| Porcentagem e juros | Porcentagem, juros simples e compostos | N4 ★ | T1 · `mat-porcentagem-juros` | 📝 |
| Estatística descritiva | Média, mediana, moda, variância, desvio-padrão, distribuição, gráficos | N3 | T2–T3 | 📝 |
| Espaço e geometria | Geometria plana e espacial, trigonometria, vetores | N2 | T2 (PostGIS) | 📝 |
| Contagem e probabilidade | Princípio fundamental, permutação, combinação, probabilidade, condicional, Bayes | N3 | T3 | 📝 |
| Números complexos | Forma algébrica e trigonométrica, plano de Argand | N2 | H | 📝 |
| Representações e símbolos | Bases numéricas, notação científica, leitura de símbolos | N3 | M1–M2 | 📝 |
| Matemática discreta | Indução, recursão, relações, grafos, combinatória | N3 | T3 | 📝 |
| Álgebra linear | Vetores, matrizes, multiplicação, determinante, autovalores (base de IA) | N3 | T3 | 📝 |
| Cálculo | Limite, derivada, integral, gradiente (base de IA e física) | N2 → N3 | H | 📝 |
| Matemática avançada | Análise real, álgebra abstrata, teoria da informação, teoria da computação | N1 → N2 | H | 📝 |

Livro-base: VHSlins, *Matemática Básica* (10 partes). Mapa capítulo a capítulo: [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md).

## 02 · Física

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Grandezas e medidas | SI, unidades, conversão, ordem de grandeza, notação científica | N3 | T1 · `fis-grandezas` | 📝 |
| Eletricidade básica | Carga, tensão, corrente, resistência, lei de Ohm, potência, circuitos série/paralelo | N3 | T1 · `fis-eletricidade` | 📝 |
| Eletromagnetismo aplicado | Indutância, capacitância, motores, sinais | N2 | T3 (robótica) | 📝 |
| Mecânica | Cinemática, dinâmica, energia (robótica, construção) | N2 | H | 📝 |
| Termodinâmica | Calor, energia, entropia (meta longa do plano de matemática) | N1 → N2 | H | 📝 |

## 03 · Engenharia da computação (hardware, eletrônica e máquina)

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Representação de dados | Binário, hexadecimal, complemento de dois, ponto flutuante IEEE 754, caracteres (ASCII, Unicode, UTF-8) | N4 ★ | M1–M2 · `b-computador` | 📝 |
| Eletrônica digital | Portas lógicas, álgebra booleana, circuitos combinacionais e sequenciais, flip-flop, multiplexador | N3 | T2 | 📝 |
| Arquitetura de computadores | CPU, ULA, registradores, ciclo de instrução, pipeline, cache L1/L2/L3, barramentos, memória, I/O | N4 | T2 · `b-hardware` | 📝 |
| Organização e desempenho | Hierarquia de memória, localidade, interrupções, DMA, multicore | N3 | T2–T3 | 📝 |
| Armazenamento | HD, SSD, NVMe, sistemas de arquivos, RAID | N3 | T2 · `b-armazenamento` | 📝 |
| Montagem e manutenção | Componentes, diagnóstico, BIOS/UEFI, POST (base das suas aulas e da assistência técnica) | N4 | ∞ | 📝 |
| Sistemas embarcados | Microcontrolador, GPIO, PWM, ADC, I2C, SPI, UART, firmware | N3 | T3 → H | 📝 |
| Assembly | x86-64 e ARM64, registradores, chamadas de função, stack frame | N2 → N3 | H | 📝 |

## 04 · Ciência da computação

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Lógica de programação | Variável, tipo, condição, laço, função, coleção, recursão | N4 ★ | M1 | 📘 [logica-de-programacao](assuntos/04-ciencia-da-computacao/logica-de-programacao.md) |
| Complexidade de algoritmos | Big-O de tempo e espaço, melhor/pior/médio caso, amortizado | N4 ★ | T2–T3 | 📝 |
| Estruturas de dados | Array, lista ligada, pilha, fila, deque, hash table, árvores (BST, balanceada, heap, trie), grafos | N4 ★ | T2–T3 · `b-estruturas` | 📝 |
| Algoritmos clássicos | Ordenação, busca binária, BFS/DFS, Dijkstra, topológica, programação dinâmica, guloso, backtracking, dois ponteiros, janela deslizante | N4 ★ | T3–T4 | 📝 |
| Paradigmas de programação | Imperativo, procedural, orientado a objetos, funcional, lógico, concorrente | N3 | T1–T2 · `b-linguagens` | 📝 |
| Programação orientada a objetos | Classe, objeto, encapsulamento, herança, polimorfismo, abstração, composição, interfaces, SOLID | N4 ★ | T1 (classes) · T4 (design) | 📘 [poo](assuntos/04-ciencia-da-computacao/poo.md) |
| Programação funcional | Função pura, imutabilidade, função de ordem superior, closure, composição, map/filter/reduce | N3 ★ | M1–M2 | 📝 |
| Compiladores e interpretadores | Léxico, sintaxe, AST, compilação, interpretação, JIT, bytecode, gramáticas (BNF) | N2 | T2 · `b-armazenamento` → H | 📝 |
| Teoria da computação | Autômatos, linguagens formais, máquina de Turing, computabilidade (Sipser) | N2 | H | 📝 |
| Teoria da informação | Entropia, compressão, códigos de correção de erro (Shannon) | N2 | H · `b-linux-boot` | 📝 |

## 05 · Sistemas operacionais

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Terminal Linux e shell | Navegar, ler, procurar, pipes, redirecionamento, variáveis, scripts | N4 ★ | M1 · `s-terminal` | 📘 [terminal-linux](assuntos/05-sistemas-operacionais/terminal-linux.md) |
| Conceitos de SO | Processo, thread, escalonamento, memória virtual, sistema de arquivos, syscalls, I/O bloqueante e não bloqueante | N4 ★ | T1–T2 · `b-backend`, `b-memoria` | 📝 |
| Concorrência e paralelismo | Condição de corrida, deadlock, mutex, semáforo, atomicidade, async × paralelismo, event loop | N4 ★ | T2 · `b-concorrencia` | 📝 |
| Gerenciamento de memória | Stack × heap, alocação, coletor de lixo, vazamento, ponteiros | N3 ★ | T2 · `b-memoria` | 📝 |
| Linux administração | Usuários, permissões, systemd, pacotes, logs, cron/timers, SSH | N3 ★ | T1–T2 | 📝 |
| WSL2 e virtualização | Hypervisor, VM, WSL2, containers × VMs | N3 | M1 · `b-linux-wsl` | 📝 |
| Arch Linux | Instalação manual, pacman/AUR, Wayland/Hyprland, Omarchy | N3 | T2 | [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md) |
| Boot e sistemas de arquivos | BIOS/UEFI, bootloader, kernel, init, ext4, BTRFS, snapshots | N3 | T4 · `b-linux-boot` | 📝 |
| Linux internals | Kernel, VFS, drivers, módulos, LFS/BLFS | N2 → N3 | H | 📝 |
| Windows internals | Arquitetura NT, Win32/NT API, registro, NTFS, ACL/SID/tokens, UAC, PowerShell | N2 → N3 | H | 📝 |
| macOS e iOS internals | Darwin/XNU, launchd, APFS, SIP, Gatekeeper, Secure Enclave, Mach-O | N1 → N2 | H | 📝 |
| SO próprio | AMtech OS (camada sobre Ubuntu), AM Linux, AM-OS | N3 | T4 → H | 📝 |

## 06 · Redes de computadores

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Camadas e pacotes | Modelo OSI e TCP/IP, encapsulamento, quadro, pacote, segmento | N4 ★ | T1 · `b-redes-1` | 📝 |
| Sinais e erros | Transmissão digital, modulação, paridade, checksum, CRC | N2 | T1 · `b-redes-1` | 📝 |
| Endereçamento | IPv4, IPv6, máscara, sub-redes (CIDR), portas, MAC, ARP | N4 ★ | T1 | 📝 |
| Protocolos principais | TCP × UDP, handshake, DNS, DHCP, HTTP/1.1, HTTP/2, HTTP/3, TLS, ICMP | N4 ★ | T1 · `b-redes-2` | 📝 |
| Sockets e cliente-servidor | Socket TCP/UDP, porta, bind/listen/accept, WebSocket | N3 ★ | T1 · `b-redes-2` | 📝 |
| A jornada de uma requisição | Do navegador ao servidor e de volta: DNS, TCP, TLS, HTTP, proxy, balanceador | N4 ★ | T1 | 📝 |
| Infraestrutura de rede | Switch, roteador, VLAN, NAT, firewall, proxy, balanceador de carga, CDN | N3 | T2 | 📝 |
| Roteamento | Tabela de rotas, gateway, roteamento estático e dinâmico (OSPF, BGP noção) | N2 → N3 | T3 → H (CCNA) | 📝 |
| SSH, VPN e rede segura | Túnel SSH, chaves, VPN (WireGuard), Tailscale, NAS | N3 | T3 · `b-redes-3` | 📝 |
| Wi-Fi | Padrões 802.11, canais, WPA2/WPA3 | N2 | H | 📝 |
| Diagnóstico de rede | ping, traceroute, dig, curl, ss, tcpdump, Wireshark | N3 ★ | T1 → ∞ | 📝 |
| Rede da casa e do setup | Servidor da casa, Zigbee, MQTT, Tailscale, rede isolada do laboratório | N3 | T2–T3 | [trilha-de-redes](trilha-de-redes.md) |

Certificações ligadas: CompTIA Network+ (T2–T3), CCNA (opcional, H).

## 07 · Linguagens de programação

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| TypeScript e JavaScript | Tipos, inferência, union, generics, funções de ordem superior, closures, classes, módulos, erros, event loop, async/await | N4 ★ | M1 → T4 · `o-csharp` | 📘 [typescript-fundamentos](assuntos/07-linguagens/typescript-fundamentos.md) |
| SQL | SELECT, JOIN, GROUP BY, subconsulta, window functions, DDL, transações | N4 ★ | M1 → T3 · `o-sql` | 📝 |
| Python | Sintaxe, tipos, coleções, funções, classes, módulos, ambientes virtuais, typing | N3 ★ | T3 (M7) | 📝 |
| Go | Tipos, structs, interfaces, goroutines, channels, erros como valor, módulos, binário único | N3 | T1 (M2) → T4 | [trilha-go-ferramentas](trilha-go-ferramentas.md) |
| Shell (Bash) | Script, variáveis, condições, laços, funções, set -euo pipefail, ShellCheck | N3 ★ | M1 → T2 | 📝 |
| C | Ponteiros, memória manual, structs, compilação, Makefile, depuração (gdb, valgrind) | N3 | H (École 42) | [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md) |
| C++ | RAII, classes, templates, STL, smart pointers | N3 | H (École 42) | idem |
| Rust | Ownership, borrowing, lifetimes, traits (firmware e SO) | N2 | H | 📝 |
| C# / .NET | Carta de reserva: vaga corporativa ou agente fiscal | N2 | só se puxar a carta | [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) §2.1 |

## 08 · Engenharia de software

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Git e controle de versão | Commit, branch, merge, rebase, PR, conflitos, desfazer, histórico limpo, tags | N4 ★ | M1 · `s-git` | 📘 [git](assuntos/08-engenharia-de-software/git.md) |
| Requisitos | Requisito funcional e não funcional, história de usuário, critério de aceite, escopo | N3 ★ | T1–T2 | 📝 |
| Modelagem | UML essencial (classes, sequência, casos de uso), diagrama ER, C4 | N3 | T2 | 📝 |
| Processos ágeis | Scrum, Kanban, RAD, backlog, sprint, retrospectiva, métricas de fluxo | N3 ★ | T1 → ∞ | 📝 |
| Código limpo | Nomes, funções pequenas, coesão, acoplamento, comentários úteis | N4 ★ | T1 → T4 | 📝 |
| Princípios SOLID | SRP, OCP, LSP, ISP, DIP | N4 ★ | T4 (M10) | 📝 |
| Padrões de projeto | Strategy, Factory, Adapter, Observer, Repository, Decorator, Dependency Injection | N3 ★ | T4 (M10) | 📝 |
| Refatoração | Code smells, refatorar com teste, passos pequenos (Fowler) | N4 ★ | T4 (M10) | 📝 |
| Testes | Unidade, integração, cenário/E2E, propriedade, mocks, cobertura, TDD, teste que reproduz o bug | N4 ★ | T1 (M3) → T2 · `o-dotnet` | 📝 |
| Arquitetura de software | Camadas, hexagonal (ports & adapters), Clean Architecture, monólito modular × microsserviços | N4 ★ | T4 (M10) | 📝 |
| Domain-Driven Design | Linguagem ubíqua, entidades, objetos de valor, agregados, contextos delimitados | N3 | T4 (M10) | 📝 |
| Decisões e documentação | ADR, README, documentação de API (OpenAPI), changelog, versionamento semântico | N4 ★ | T1 → ∞ | 📝 |
| Revisão de código | Revisar PR humano e de IA, checklist, comentários úteis | N4 ★ | T1 (M2, Trilha R) | 📝 |
| Estimativa e planejamento | Estimativa como hipótese, fatiamento, entrega incremental | N3 | ∞ | 📝 |

## 09 · Desenvolvimento web

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| HTML e CSS | Semântica, formulários, box model, flexbox, grid, responsivo | N4 ★ | T1 (M2) | 📝 (base: seu Catálogo do HTML) |
| JavaScript no navegador | DOM, eventos, fetch, armazenamento, módulos | N3 ★ | T1 (M2) | 📝 |
| HTTP para devs | Métodos, status, cabeçalhos, cookies, cache, CORS | N4 ★ | T1 · `b-redes-2` | 📝 |
| React | Componentes, props, estado, hooks, renderização | N3 ★ | T1 (M2) | 📝 |
| Next.js | Rotas, server e client components, server actions, cache, deploy | N3 ★ | T1 (M2) → T2 | 📝 |
| Tailwind e design de interface | Utilitários, design system, acessibilidade básica | N3 | T1 (M2) | 📝 |
| APIs | REST, GraphQL (noção), OpenAPI, versionamento, paginação, idempotência | N4 ★ | T1 (M3) | 📝 |
| Validação e contratos | Zod, validar na borda, tipos compartilhados | N3 ★ | T1 (M3) | 📝 |
| Autenticação e autorização | Sessão, cookie, JWT, OAuth2/OIDC, RBAC, Row-Level Security | N4 ★ | T1 (M3) | 📝 |
| Back-end em TypeScript | NestJS, injeção de dependência, middlewares, filas | N3 ★ | T1 (M3) → T2 | 📝 |
| Back-end em Python | FastAPI, Pydantic, async | N3 | T3 | 📝 |
| Performance web | Core Web Vitals, cache, compressão, lazy loading | N3 | T3 · `b-testes-perf` | 📝 |
| Acessibilidade | WCAG, semântica, teclado, leitor de tela | N2 | T2 | 📝 |

## 10 · Banco de dados e dados

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Modelagem relacional | Entidades, relacionamentos, chaves, normalização (1FN–3FN), quando desnormalizar | N4 ★ | T1 | 📝 |
| PostgreSQL | Tipos, constraints, índices, EXPLAIN, extensões, backup | N4 ★ | T1 → T3 | 📝 |
| Transações | ACID, níveis de isolamento, locks, concorrência otimista, deadlock | N4 ★ | T2 (M4) | 📝 |
| Índices e desempenho | B-tree, índice composto, cobertura, plano de execução, N+1 | N4 ★ | T2 → T3 · `b-escala` | 📝 |
| ORM e migrations | Prisma/Drizzle, migrations versionadas, expand-contract | N3 ★ | T1 (M3) | 📝 |
| SQLite e offline | SQLite local, sincronização, conflito | N3 | T2 (M4) | 📝 |
| PostGIS | Geometria, SRID, consultas espaciais | N2 | T2 (M5) | 📝 |
| pgvector | Embeddings, busca por similaridade, índices vetoriais | N3 | T2 (M5) | 📝 |
| Redis e cache | Chave-valor, TTL, invalidação, filas | N2 | T4 | 📝 |
| NoSQL | Documento, coluna, grafo; quando usar | N2 | T3 · `b-bancos` | 📝 |
| Engenharia de dados | ETL/ELT, pipelines, data warehouse, qualidade de dados | N2 → N3 | T3 → H | [trilha-dados-ia](trilha-dados-ia.md) IA2 |

## 11 · Sistemas distribuídos e escalabilidade

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Escalabilidade | Vertical × horizontal, gargalo, stateless, balanceamento | N3 ★ | T3 · `b-escala` → T4 | 📝 |
| Cache | Onde cachear, invalidação, cache-aside, CDN | N3 ★ | T4 (M11) | 📝 |
| Mensageria | Filas, pub/sub, outbox, idempotência do consumidor, retry, dead letter | N3 | T4 (M11) | 📝 |
| Consistência | Consistência eventual, CAP/PACELC, relógios, conflitos | N2 → N3 | T4 (M11) | 📝 |
| Tempo real | WebSocket, SSE, SignalR (noção) | N2 | T2 (pedidos) | 📝 |
| System design | Requisitos, estimativa de carga, desenho, trade-offs em 45 min | N4 ★ | T4 (M10–M11) | 📝 |

## 12 · DevOps, nuvem e infraestrutura

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Containers | Imagem, container, Dockerfile, Compose, volumes, rede, namespaces e cgroups | N4 ★ | M1 · `s-docker`, `b-containers` | 📝 |
| CI/CD | GitHub Actions, pipeline, portão (`just check`), cache, artefatos | N4 ★ | T1 · `s-ci` | 📝 |
| Deploy | Vercel, VPS, Kamal, Hostinger por push, rollback de um comando, staging, feature flag | N3 ★ | T1 → T2 · `s-deploy` | 📝 |
| Os 12 fatores | Configuração no ambiente, processos stateless, logs como fluxo | N3 ★ | T2 · `b-containers` | 📝 |
| Observabilidade | Logs estruturados, métricas, traces, alertas, Uptime Kuma | N3 ★ | T2 (M6) | 📝 |
| Backup e recuperação | restic, retenção, restauração ensaiada, snapshots | N4 | M1 · `s-backup` | 📝 |
| Segredos | KeePassXC, sops/age, variáveis de ambiente, nunca no Git | N4 ★ | M1 · `s-segredos` | 📝 |
| Infraestrutura como código | Terraform, Ansible, receitas idempotentes | N2 → N3 | T4 → H | 📝 |
| Kubernetes | Pod, deployment, service, ingress (noção para vaga) | N1 → N2 | H | 📝 |
| Nuvem | Azure (AZ-900, AI-200), AWS (Cloud Practitioner), custos | N2 → N3 | T3 → H | 📝 |
| Homelab | Servidor da casa, VMs, rede isolada, monitoramento | N3 | T2 → H | 📝 |

## 13 · Segurança defensiva (AppSec, blue team)

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Criptografia | Hash, sal, simétrica (AES), assimétrica (RSA, curvas elípticas), assinatura, certificados, TLS, PKI | N3 ★ | T2 · `b-cripto` → T4 · `b-cripto-pratica` | 📝 |
| OWASP Top 10 | Injeção, quebra de controle de acesso, falhas criptográficas, SSRF, XSS, configuração insegura | N4 ★ | T1 (M3) | 📝 |
| OWASP API Top 10 | BOLA, autenticação quebrada, exposição excessiva, rate limit | N3 ★ | T1 (M3) → T2 | 📝 |
| Modelagem de ameaças | STRIDE, ativos, superfícies de ataque, mitigação | N3 | T2 | 📝 |
| DevSecOps | Análise estática (CodeQL), dependências (Trivy, Dependabot), segredos (gitleaks), revisão automática | N3 ★ | T1 → T3 | 📝 |
| LGPD e privacidade | Dados pessoais, bases legais, minimização, incidente | N3 ★ | T2 | 📝 |
| Segurança do Linux e da rede | Hardening, firewall, SSH seguro, atualizações, mínimo privilégio | N3 | T2 | 📝 |
| Segurança de agentes de IA | Sandbox (ai-jail), sem credencial de produção, injeção de prompt, revisão de PR | N4 | M1 · `s-ia-segura` | 📝 |
| Blue team e resposta a incidente | Logs, detecção, SIEM (noção), relato de incidente | N2 → N3 | T3 → H | 📝 |
| Forense digital | Coleta de evidência, linha do tempo, análise de memória e disco | N2 | H | 📝 |

## 14 · Segurança ofensiva (pentest e red team)

> Tudo aqui só em laboratório próprio ou com autorização por escrito (`escopo.py`). Trilha completa: [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md).

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Metodologia e lei | PTES, OWASP Testing Guide, escopo, autorização, Lei 12.737, Marco Civil, LGPD | N4 | H (antes de tudo) | 📝 |
| Reconhecimento | OSINT, enumeração de DNS e subdomínios, varredura de portas (nmap), fingerprinting | N3 | H | 📝 |
| Web hacking | Injeção SQL, XSS, CSRF, SSRF, IDOR, upload, desserialização, Burp Suite | N4 | H (eJPT, BSCP) | 📝 |
| Bypass e evasão | WAF evasion, burlar proxy e firewall (túneis, `b-redes-3`), bypass de autenticação e de controles do cliente, evasão de antivírus/EDR, bypass de UAC/AMSI (noção) | N3 | H (BSCP → OSEP) | 📝 |
| Escalada de privilégios | Linux (SUID, sudo, cron, kernel) e Windows (serviços, tokens, registro) | N3 | H (OSCP) | 📝 |
| Active Directory | Kerberos, NTLM, enumeração, kerberoasting, movimento lateral, kill chain | N3 | H (OSCP) | 📝 |
| Pivoting e tunneling | Port forwarding, SOCKS, chisel, ligolo | N3 | H (OSCP) | 📝 |
| Wireless | WPA2/WPA3, handshake, ataques de rede sem fio | N2 | H | 📝 |
| Desenvolvimento de exploit | Buffer overflow, ROP, shellcode, mitigações (ASLR, DEP, canário) | N3 | H (OSED) | 📝 |
| Engenharia reversa | Ghidra, depurador, assembly, análise estática e dinâmica, binários .NET/Java | N3 | H | 📝 |
| Análise de malware | Sandbox, comportamento, indicadores de comprometimento | N2 | H | 📝 |
| C2 e OPSEC | Frameworks de comando e controle, OPSEC, deception | N2 | H (OSEP) | 📝 |
| Engenharia social | Phishing (só em exercício autorizado), pretexto, conscientização | N2 | H | 📝 |
| Cloud e mobile security | IAM mal configurado, buckets, Android/iOS básico | N2 | H | 📝 |
| Relatório de pentest | CVSS, evidência, recomendação, sumário executivo | N4 | H | 📝 |

Certificações: CompTIA A+/Network+ → Security+ → eJPT → BSCP → OSCP → OSWE/OSEP.

## 15 · IA, dados e machine learning

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| LLMs na prática | Token, contexto, temperatura, prompt, saída estruturada, chamada de ferramenta | N4 ★ | T1 (M3) · `b-ia` | 📝 |
| IA em TypeScript | Vercel AI SDK, Zod para saída, custo por chamada, streaming | N3 ★ | T1 (M3) | 📝 |
| RAG e embeddings | Embedding, chunking, busca vetorial, reranking, citação de fonte | N4 ★ | T2 (M5) | 📝 |
| Avaliação de IA (evals) | Conjunto de teste, métrica, regressão, LLM como juiz | N3 ★ | T2 (M6) | 📝 |
| Agentes e MCP | Loop de ferramenta, MCP, orquestração, limites e custos | N3 ★ | T2 → T4 | 📝 |
| Otimização de uso de modelos | Tokens, cache de prompt, roteamento local/online, modelo certo por tarefa | N4 | T3 (M8) | 📝 |
| Python para dados | NumPy, pandas, visualização, notebooks | N3 ★ | T3 (M7) | 📝 |
| Machine learning clássico | Regressão, classificação, árvores, validação, overfitting, scikit-learn | N3 | T3 (M8) | 📝 |
| Deep learning | Redes neurais, backpropagation, PyTorch, CNN, transformer | N2 → N3 | T3 (M9) → H | 📝 |
| IA local | Ollama, quantização, memória de GPU, modelos do Hugging Face | N3 | T3 (M9) | 📝 |
| Treinar e ajustar modelos | Treinar do zero (pequeno), fine-tuning, LoRA/QLoRA, modelo de 8B | N2 → N3 | H | [trilha-dados-ia](trilha-dados-ia.md) IA6 |
| MLOps | Versionar dados e modelos, servir, monitorar | N2 | H | idem IA7 |
| Voz e visão | Whisper, Piper, Frigate (Jarvis e casa) | N2 | H | 📝 |

## 16 · Trabalhar com agentes de IA (Trilha R)

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Revisar código de IA | Checklist de PR, ler diff, explicar cada linha | N4 ★ | T1 (M2) · R-1 | 📝 |
| Teste antes do código | Especificar pelo teste, o agente implementa, o teste decide | N4 ★ | T1 (M3) · R-2 | 📝 |
| Especificação e regras | CLAUDE.md, pedido sem ambiguidade, contexto mínimo suficiente | N4 | T2 (M4) · R-3 | 📝 |
| Avaliar a IA | Evals no CI | N3 | T2 (M6) · R-4 | 📝 |
| Custo e roteamento | Medir tokens, decidir código/local/online | N4 | T3 (M8) · R-5 | 📝 |
| Orquestrar agentes | Worktrees, agentes em paralelo, revisão automática de PR | N3 | T4 (M11) · R-6 | 📝 |

## 17 · Engenharia de sistemas financeiros

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Dinheiro no código | Decimal × float, centavos inteiros, arredondamento bancário, moeda | N4 ★ | T2 (M4) | 📝 |
| Idempotência e pagamentos | Chave de idempotência, retry seguro, efeitos externos irreversíveis | N4 | T2 (M4) | 📝 |
| Ledger de partidas dobradas | Lançamento, débito e crédito, saldo derivado, imutabilidade | N4 | T2 (M5) | 📝 |
| Conciliação | Extrato × sistema, divergências, fechamento | N3 | T3 (M8) | 📝 |
| Pix e Pix Automático | API do Pix, QR Code, webhooks, devolução | N3 | T3 (M8) | 📝 |
| Fiscal | NFC-e/NFS-e, impressora ESC/POS, agente fiscal local | N3 | T2 (M4) | 📝 |

## 18 · Finanças e economia

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Finanças pessoais e investimentos | Orçamento, reserva, renda fixa, ações, FIIs, ARCA, aporte e rebalanceamento | N4 | ∞ (F0) | [trilha-financas-economia](trilha-financas-economia.md) |
| Contabilidade | Regime de caixa e competência, débito/crédito, balanço, DRE, fluxo de caixa | N3 | T1 (F1) · `f-*` | 📝 |
| Matemática financeira | Juros compostos, VPL, TIR, SAC, Price, valor do dinheiro no tempo | N4 | T2 (F2) | 📝 |
| Tributação brasileira | Simples Nacional, Fator R, NFS-e, carnê-leão, MEI × ME | N3 | T3 (F3) | 📝 |
| Preço de serviço | Hora mínima, custo, margem, proposta | N3 | T1 · `f-preco` | 📝 |
| Finanças corporativas e valuation | Fluxo de caixa descontado, múltiplos, análise de balanço | N3 | T4 (F4) | 📝 |
| Mercado financeiro e regulação | CVM, ANBIMA, B3, fundos, regras de recomendação | N3 | H (F5) | 📝 |
| Economia | Micro, macro, inflação, juros, câmbio, econometria | N2 → N3 | H (F6, faculdade) | 📝 |
| Finanças quantitativas | Séries temporais, risco, otimização de carteira | N2 | H (F8) | 📝 |

Certificações: CNPI → registro de consultor CVM → CGA/CGE → CFP → CFA.

## 19 · Robótica, IoT e automação

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Arduino | Sketch, entradas e saídas, sensores, atuadores | N3 | T1 (M3) | [trilha-robotica-iot](trilha-robotica-iot.md) |
| ESP32 e IoT | Wi-Fi, MQTT, deep sleep, OTA | N3 | T3 | 📝 |
| Raspberry Pi | Linux embarcado, GPIO, câmera | N3 | T3 | 📝 |
| Casa inteligente | Home Assistant, Zigbee, automações, Jarvis por voz | N3 | T3 → H | 📝 |
| Robótica móvel | Motores, controle PID, visão, ROS (noção) | N2 | H | 📝 |
| Agro | Sensores de solo, irrigação, projeto escolar | N3 | H | 📝 |

## 20 · Blockchain

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Fundamentos de blockchain | Hash, assinatura, consenso, generais bizantinos, carteira | N3 | H | 📝 |
| Ethereum e contratos | EVM, Solidity, tokens, rede de teste (ByteSDCoin, AMtech OS) | N2 → N3 | H | 📝 |

## 21 · Empreendedorismo, marketing e vendas

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Validar antes de construir | Problema, cliente, MVP, beta, portão de venda | N4 | ∞ | 📝 |
| Empreendedorismo | Modelo de negócio, custos, formalização (CPF, MEI, ME), contrato | N3 | ∞ | 📝 |
| Marketing digital | Posicionamento, conteúdo, funil, SEO, tráfego pago | N3 | T2 → ∞ | 📝 |
| Vendas | Proposta, negociação, objeções, pós-venda | N3 | T1 → ∞ | 📝 |
| Infoprodutos | Curso, template, lançamento, plataforma (Hotmart) | N3 | T2 → ∞ | 📝 |
| Consultoria | Diagnóstico, escopo, entrega, preço | N3 | H | 📝 |

## 22 · Construção civil pela TI

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| BIM e IFC | Bonsai/FreeCAD, IFC, quantitativos | N2 | H | 📝 |
| Orçamento de obra | SINAPI, composição de custos | N2 | H | 📝 |

## 23 · Idiomas

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Inglês | Vocabulário técnico, leitura de documentação, escuta, fala, escrita, entrevista (meta C1) | N4 ★ | ∞ | [ingles-espanhol-integrado](ingles-espanhol-integrado.md) |
| Espanhol | Falsos cognatos, pronúncia, verbos irregulares (meta B2) | N3 | depois do B1 em inglês | idem |

## 24 · Carreira, comunicação e ensino

| Assunto | Conceitos | Nível | Quando | Arquivo |
|---|---|---|---|---|
| Entrevista técnica | Algoritmos em voz alta, system design, comportamental (STAR), registros do recrutador | N4 ★ | T4 (M11) → ∞ | 📝 |
| Portfólio e GitHub | READMEs, estudos de caso, ADRs públicos, contribuição open source | N3 ★ | T1 → T4 | 📝 |
| Didática | Planejar aula, avaliar, motivação antes da definição (Licenciatura e EMTI) | N4 | ∞ | 📝 |
| Produção de conteúdo | Post técnico mensal, vídeo, curso | N3 | ∞ | 📝 |

## 25 · Formação formal

| Formação | O que cobra | Quando |
|---|---|---|
| Licenciatura em Matemática | Disciplinas do curso | em curso |
| ENEM 2027 | Linguagens, humanas, natureza, matemática e redação | 2027 |
| Ciências Econômicas | Micro, macro, econometria, contabilidade | depois da Licenciatura |
| Ciência da Computação ou graduação em IA | Fundamentos formais de computação e IA | escolha pendente |

Detalhe: [formacao-academica](formacao-academica.md).

---

## Como um 📝 vira 📘

Na semana anterior ao estudo de um assunto, o arquivo dele é escrito a partir do [modelo](assuntos/_MODELO.md) e salvo em `assuntos/<área>/<assunto>.md`. A linha aqui troca de 📝 para 📘 com o link. Escrever todos de uma vez geraria arquivos rasos e desatualizados; escrever na véspera deixa cada um com o que você já sabe e com o mercado do momento.
