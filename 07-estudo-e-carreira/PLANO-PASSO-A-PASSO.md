---
tags: [estudo, rotina, passo-a-passo, portfolio-ams]
tipo: plano
status: ativo
atualizado: 2026-11-17
fonte-unica: true
---

# 🧭 PLANO PASSO A PASSO + ROTINA — 12 meses

> **O que é:** o caminho exato, semana a semana e mês a mês, para você sair do lugar e virar o profissional mais completo possível em até 12 meses — alternando **todas** as trilhas (TS, Go, Python/dados/IA, SQL, matemática, finanças, inglês, física, robótica, sistema operacional, baixo nível) sem largar nenhuma.
>
> **Como ler:** o [[PLANO-UNICO-AMtech]] diz *o quê e por quê*; a [[stack-tecnologica]] diz *com o quê*; **este diz quando e como, dia a dia.** O detalhe profundo de cada área está nas trilhas (links no fim).
>
> **Fonte única do estudo (desde 17/11/2026):** este arquivo manda. O `docs/plano-eixo.md` e o currículo do Professor (`data/professor/curriculo.json`) no dev-setup seguem este plano ([ADR 0018](../11-setup-dev-setup/docs/adr/0018-plano-de-estudo-unico-no-vault.md)). Se os dois discordarem, vale este, e o outro é corrigido.
>
> **O que estudar, por área e nível:** repositório [mapa-de-estudo](https://github.com/AlanMateus17/mapa-de-estudo), com um arquivo por assunto.
>
> **A regra que rege tudo:** você nunca "só estuda". **Cada bloco entrega um ativo** (uma ferramenta, uma parte do AM Gestão, um site, um protótipo) que vira renda e portfólio. No máximo **1 ativo sendo construído + 1 sendo testado** por vez.

---

## PARTE 1 — A ROTINA SEMANAL (feita sobre os seus horários reais)

Base real: você acorda **6h todo dia**; **segunda não tem restaurante**; **quinta não tem escola**; restaurante à noite de ter–dom; manhãs quase todas livres; precisa **cuidar dos cães todo dia**; Licenciatura em paralelo.

A âncora é simples e à prova de TDAH: **toda manhã, 6h–8h, é estudo**, antes do mundo acordar. É o bloco que nunca falha. O resto são blocos extras nos buracos livres.

| Dia | Manhã (6h–) | Tarde | Noite |
|---|---|---|---|
| **Segunda** | 6–8h âncora técnica (foco do mês) | Escola | **Bloco profundo 20–22h** (AM Gestão — sem restaurante!) |
| **Terça** | 6–7h **base do Akita** (1 episódio + nota) | Escola | Restaurante (até 22h) |
| **Quarta** | 6–8h âncora técnica | Escola | Restaurante |
| **Quinta** | **6–11h bloco profundo** (AM Gestão + trilha par) — seu maior dia | Livre → cães / Licenciatura | Restaurante |
| **Sexta** | 6–11h matemática (VHSlins) + Licenciatura + revisão | Escola+restaurante (12:55–23h) | — |
| **Sábado** | **6–13h: ofício leve (Go a partir do Mês 2) + robótica/SO + física** | Restaurante (15–23h) | — |
| **Domingo** | **Folga.** Só a revisão do Anki (30 min) e a Licenciatura quando houver prazo | Restaurante (15–23h) | — |

**Blocos fixos da semana:**
- **Âncora 6h–8h** (seg, qua) → o foco técnico do mês. **Terça 6h–7h** → 1 episódio da base do Akita (Parte 4.2).
- **Inglês todo dia, 20–30 min** → nunca pausa. Documentação em inglês, 1 vídeo, Anki. Encaixe no café/deslocamento.
- **Cães** → logo após a âncora ou no meio-dia; parte fixa da rotina, não "tempo perdido".
- **Dois blocos profundos de semana:** segunda à noite + quinta de manhã (os dois maiores vazios que você tem).
- **Sábado de manhã** → o bloco pesado do fim de semana (Go, robótica/SO, física).
- **Domingo é folga** → um dia inteiro sem estudo por semana é parte do plano, não atraso. Com escola, restaurante e Licenciatura, sem folga o plano quebra em poucas semanas.
- **Entrevista (recrutador)** → 45 min uma vez por semana, dentro do bloco de quinta.
- **Licenciatura** → quinta à tarde; domingo só quando houver prazo.

**Conta de horas:** âncoras (seg, qua) + terça curta + 2 blocos profundos (seg noite, qui manhã) + sexta + sábado ≈ **18–20h/semana reais**. **O plano é calibrado nessas ~20h; as 4h/dia do plano antigo do setup viram bônus, nunca dívida.** Em semana corrida, só a âncora já mantém o ritmo.

---

## PARTE 2 — COMO ESTUDAR (o seu método completo, do Professor)

Detalhe inteiro em [metodo-de-estudo](metodo-de-estudo.md) e no `docs/professor/metodo.md` do dev-setup. Resumo fiel:

### 2.1 O 20/80 em DUAS passadas (o princípio que rege o plano todo)
Cada tecnologia e cada tema tem uma **profundidade calibrada** decidida antes:

- **1ª passada — "usar" (os 20% que resolvem 80%):** você aprende só o essencial que faz o ativo da semana funcionar. Não lê a documentação inteira. Vai largo e raso por tudo, rápido, construindo.
- **2ª passada — "a fundo" (os 80% que resolvem os 20% difíceis):** só nos temas que **voltam** (os que o produto ou a vaga realmente cobram) você aprofunda — internals, casos de borda, performance. O que nunca voltou, fica na profundidade "usar" mesmo.

Isso é o que te deixa **completo em 12 meses sem afogar:** primeiro a largura toda no nível "usar", depois a profundidade só onde paga. A espinha dos 12 meses (Parte 3) é a 1ª passada; a 2ª acontece dentro dela, nos meses 10–12 e sempre que um tema reaparece.

### 2.2 Intercalação (por que o plano alterna as trilhas)
Alternar assuntos no mesmo dia retém mais que estudar um em bloco (Rohrer & Taylor). É por isso que a rotina mistura ofício + setup + finanças/matemática no mesmo dia, e não "um mês só de X".

### 2.3 As técnicas que você adotou
- **Prática de recuperação:** feche o material e reconstrua de cabeça — vale mais que reler.
- **Repetição espaçada:** revisar pouco antes de esquecer, em **1, 3, 7, 21, 60 e 120 dias** (Anki).
- **Dificuldade desejável:** o que custa na hora (testar-se, espaçar) é o que fica. Prova < 80 → revisão volta amanhã.
- **Exemplos com retirada de apoio:** ver resolvido → resolver com lacunas → resolver sozinho.
- **Prática deliberada:** treinar o que ainda não domina, com retorno.
- **Feynman (ensinar):** explicar sem jargão mostra o buraco — e você é professor.
- **Velocidade calibrada:** estimativa é hipótese; o tempo medido corrige o plano (não vira dívida de atraso).
- **Motivação antes da definição:** todo tópico abre por "por que isso importa".

### 2.4 Blocos e protocolo de fim de bloco
- **Blocos de 25 min** (Pomodoro), um objetivo só por bloco. **Uma porta só** (TDAH): `just professor hoje` decide o que abrir — você não escolhe.
- **Ao fim de todo bloco:** (1) feche o material; (2) reconstrua de cabeça o que resolveu e por quê; (3) ensine em 3–5 frases sem jargão; (4) faça 1–3 cartões; (5) anote o tempo real; (6) só então avance.

### 2.5 Exercícios em 4 níveis (N1–N4)
N1 reconhecimento · N2 aplicação direta · N3 aplicação combinada e "encontre o erro" · N4 desafio / mini-projeto real. Gabarito sempre comentado.

### 2.6 Ficha dupla + registro de entrevista (o estudo vira dois ativos)
Todo estudo gera, de uma vez: **a ficha dupla** (ideia, código, por que importa) → vira material de aula; e **o registro de entrevista** (contexto, decisão + alternativa descartada, resultado com número) → vira resposta pronta para vaga. O nível 4 ("ensinou") só conta quando você dá a aula de verdade (escola, aula particular, vídeo ou post).

### 2.6b Registros no setup (leitura, erros, atritos e fichas)
Toda sessão de leitura (livro, documentação, post do Akita) é registrada no setup, para o Professor, o Recrutador, as fichas e o conteúdo poderem usar:
1. **Antes:** `just livros para ETAPA` diz o que ler para o assunto e se falta comprar algum livro (`just livros comprar` mostra a lista na ordem em que vai precisar).
2. **Depois de ler:** feche o livro e faça o protocolo de fim de bloco. Então registre: `just livros ler LIVRO --trecho "cap. 1-2" --min 50 --assunto 0.4 --nota "o que entendi, com as minhas palavras"`.
3. O registro fica no vault em `07-estudo-e-carreira/leituras.md`. **Só entram as suas palavras:** página de livro nunca vai para o registro, para o Git nem para a IA (nota longa demais é recusada).
4. `just livros lidos` mostra o que você já leu e os minutos por livro.
5. Livro comprado: `just livros marcar LIVRO tenho`.
6. **Errou num exercício ou na prova?** `just erro ETAPA "o erro" --certo "o certo"`. Vai para o caderno de erros (`07-estudo-e-carreira/caderno-de-erros.md`), que vira cartão e volta nas revisões. `just erros` lista.
7. **Algo do setup travou, foi lento ou manual?** `just atrito "o que aconteceu" --area X`. Vai para `06-execucao-e-desenvolvimento/atritos-do-setup.md`; `just atritos` mostra o que já apareceu 3 vezes e deve virar script.
8. **Ficha dupla e registro de entrevista:** o `just professor fechar ID MINUTOS` cria o arquivo; você preenche.
9. **Não crie** resumos de livro, notas soltas por aula nem cópias de explicação da IA. O código dos exercícios vai para o repositório (`logica-ts`), não para nota.

### 2.7 As fontes e o papel de cada uma
- **Alura** → primeira exposição em vídeo (assistir **antes** da aula).
- **Livros do VHSlins** → teoria e exercícios no papel (base de matemática).
- **Fabio Akita (posts/Akitando)** → visão de quem faz há 30 anos; o que conta são as regras e notas que saem, não o tempo assistindo.
- **Documentação oficial** → a verdade sobre cada ferramenta.
- **O Professor** → liga tudo ao seu setup, cobra, corrige e traz de volta.
- **Regra fixa:** conteúdo de curso pago e página de livro são para você ler/assistir — **nunca vão para a IA**.

---

## PARTE 3 — O PASSO A PASSO DE 12 MESES

**A ordem dos assuntos vem do [mapa-de-estudo](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/MAPA.md)** (etapas por pré-requisito: nada é usado antes de ter base). Cada mês abaixo diz quais etapas ele cobre e o que entrega.

Cada mês tem: **Foco · O que estudar (passo a passo) · Recursos · Exemplo/entregável.** As trilhas se alternam, mas as "nunca-pausam" (inglês, matemática, Licenciatura, física leve) correm por baixo o tempo todo.

### 🟢 TRIMESTRE 1 — Fundamentos viram o primeiro dinheiro (nov/26–jan/27)

> **Calendário real:** o estudo começou em **17/11/2026**. Cada mês abaixo anda ~2 semanas para frente (Mês 1 = 17/11 a 13/12, Mês 2 = 14/12 a ~10/01, e assim por diante). Os nomes dos meses ficam como referência.

#### Mês 1 (nov) — Setup + lógica + TypeScript do zero
- **Foco:** deixar a máquina pronta, **aprender a operar o setup** e começar a programar de verdade em TS.
- **Passo a passo (semana a semana; o dia a dia está no [Cartão](../CARTAO-voce-esta-aqui.md)):**
  - **Semana 1 (17–23/11) · Etapa 0:** como o computador funciona e representação de dados (0.4, 0.5) + lógica de programação no TS Playground com os 3 exercícios, **sem IA** (0.6) + Matemática Cap. 1, lógica (0.2).
  - **Semana 2 (24–30/11) · Etapas 0 → 1, setup instalado:** Matemática Cap. 2, conjuntos (0.3) + sistema operacional essencial e WSL2 (1.1, 1.2) + `s-terminal` (1.3) + Akita `b-aprender`.
  - **Semana 3 (01–07/12) · Etapa 1:** criptografia essencial (1.4) + `s-git` (1.5) + `s-segredos` (1.6) + `s-backup` (1.7) + Akita `b-computador`.
  - **Semana 4 (08–13/12) · Etapas 1 → 2:** `s-docker`, `s-just`, `s-nucleo`, `s-ia-segura` (1.8–1.10) + TypeScript de verdade no terminal com testes (2.1, 2.4) + refazer os 3 exercícios de cabeça, agora com testes (prova do mês).
- **Recursos:** [TS Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) · [SQLBolt](https://sqlbolt.com/) · [roadmap.sh/typescript](https://roadmap.sh/typescript).
- **Entregável:** ambiente reproduzível (`setup-dev.sh`) + repositório de exercícios de lógica em TS + começo de 1 site simples. **Renda:** primeiras aulas particulares.

#### Mês 2 (dez) — Web (Next.js) + SQL + **Go começa (ferramentas)**
- **Foco:** colocar um site no ar e fabricar sua primeira ferramenta. **Etapas 2 (fim) e 3.**
- **Passo a passo:**
  0. **Antes do site (Etapa 2 → 3):** funcional essencial, estruturas de dados básicas e Big-O, debugging, assincronia (2.2–2.6); depois **redes essenciais, HTTP/HTTPS e a jornada de uma requisição** (3.1–3.4), e só então HTML/CSS, JavaScript no navegador e React (3.5–3.7).
  1. **Next.js + Tailwind:** páginas, componentes, deploy na Vercel.
  2. **PostgreSQL via Supabase:** criar banco, tabela, consulta do app.
  3. **Go-1 e Go-2** ([trilha-go-ferramentas](trilha-go-ferramentas.md)): primeiro binário + organizador de arquivos.
  4. **Git fluente** + GitHub Actions básico (rodar teste a cada push).
  5. **Finanças F0 (leve):** contabilidade básica — débito/crédito.
  6. **Trilha R-1 (revisar código de IA):** o site do cliente sai pela esteira do setup (issue → agente → PR); você **revisa cada PR com o checklist** (Parte 4.1) antes do merge.
- **Recursos:** [Next.js Learn](https://nextjs.org/learn) · [Supabase Docs](https://supabase.com/docs) · [Tour of Go](https://go.dev/tour/).
- **Entregável:** **1 site de cliente no ar (pago)** + 1 CLI em Go que você usa no dia a dia.

#### Mês 3 (jan) — Backend TS + API + banco a fundo + segurança
- **Foco:** sair do "site" para "sistema" — API, banco sério, segurança. **Etapa 4.**
- **Passo a passo:**
  0. **Antes da API:** modelagem relacional e SQL (4.1, 4.2), **POO** e arquitetura em camadas essencial (4.4, 4.6), requisitos (4.5). NestJS só depois de POO.
  1. **API** em Next/NestJS: rotas, validação com Zod, status corretos.
  2. **ORM (Prisma/Drizzle):** migrations, relacionamentos, evitar N+1.
  3. **Segurança (Passo 4):** OWASP Top 10, autenticação, Row-Level Security do Supabase.
  4. **Testes (Vitest):** primeiro teste de unidade e de API. **Teste antes de pedir código ao agente** (Trilha R-2): você escreve o teste, o agente implementa, o teste decide.
  5. **IA em TypeScript (IA-T1):** chamar um modelo pela API (Vercel AI SDK), saída estruturada validada com Zod, custo por chamada medido. Exemplo: classificar despesas da planilha do financeiro. **Não precisa de Python.**
  6. **Robótica (paralelo, sábado):** primeiro protótipo — LED/sensor no Arduino/ESP32.
- **Recursos:** [OWASP Top 10](https://owasp.org/www-project-top-ten/) · [Prisma Docs](https://www.prisma.io/docs) · [Vitest](https://vitest.dev/guide/).
- **Entregável:** **planilha do financeiro à venda** + esqueleto do AM Gestão com teste no CI + protótipo 1. **Renda:** aulas + site + planilha.

### 🟡 TRIMESTRE 2 — O produto nasce e roda num cliente (fev–abr/27)

#### Mês 4 (fev) — AM Gestão: módulo **Caixa (PDV)** + Go no agente fiscal
- **Foco:** o coração do produto, com dinheiro correto. **Etapa 5 (5.1–5.10).**
- **Passo a passo:**
  0. **Antes do Caixa:** concorrência e paralelismo (5.2), depois transações a fundo (5.3).
  1. **Engenharia financeira (Passo 3/5):** dinheiro em `decimal` nunca `float`; arredondamento; idempotência de pagamento; concorrência otimista.
  2. **PDV offline:** SQLite local + sincronização quando a conexão volta.
  3. **Go-5 e Go-6:** servidor HTTP local + **agente fiscal** (impressora ESC/POS).
  4. **Matemática financeira:** juros, porcentagem aplicada ao PDV.
  5. **Trilha R-3:** um `CLAUDE.md` por projeto com as regras do AM Gestão (dinheiro, migrations, o que o agente nunca faz), incluindo as regras do Akita aprovadas (AK-0008, AK-0016, AK-0018).
- **Recursos:** [trilha-go-ferramentas](trilha-go-ferramentas.md) Go-5/Go-6 · [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) (camada banco/testes).
- **Entregável:** módulo **Caixa** funcionando com impressão real.

#### Mês 5 (mar) — AM Gestão: **Pedidos + Financeiro** + deploy
- **Etapa 5 (5.11–5.17).**
- **Passo a passo:**
  0. **Antes do servidor e da IA:** Linux administração e SSH (5.11, 5.12) antes do deploy em VPS; vetores essencial (5.15) antes do RAG.
  1. **Pedidos/Delivery:** PostGIS (geolocalização, rotas).
  2. **Financeiro:** ledger de partidas dobradas (todo movimento = débito+crédito).
  3. **Deploy + Docker + CI/CD:** subir o MVP num servidor.
  4. **SO (paralelo):** Arch como máquina do dia a dia (daily driver).
  5. **IA-T2 (RAG em TypeScript):** pgvector no próprio Postgres + embeddings; busca "como faço X?" na ajuda do AM Gestão. Primeira feature de IA que um cliente vê.
- **Recursos:** [PostGIS](https://postgis.net/documentation/) · [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md).
- **Entregável:** **MVP (Caixa+Pedidos+Financeiro) rodando em 1 restaurante** que já te procura.

#### Mês 6 (abr) — Produção de verdade: testes + observabilidade
- **Etapa 6.**
- **Passo a passo:**
  1. **Observabilidade (Passo 10):** logs estruturados, métricas, o que quebrou e por quê.
  2. **Testes de propriedade** para a regra de dinheiro (dispara 100 pagamentos, cobra 1).
  2b. **Trilha R-4 (avaliar IA):** um conjunto de 20 perguntas reais com resposta esperada para a busca do Mês 5; roda no CI e mostra se a IA piorou depois de cada mudança.
  3. **Go (ferramenta 3):** CLI de deploy/monitoramento.
  4. **Inglês Fase B:** documentação técnica só em inglês a partir daqui.
- **Entregável:** MVP estável + **10 planilhas vendidas** + começo da base de clientes.

### 🟠 TRIMESTRE 3 — Dados, Python e os primeiros clientes pagantes (mai–jul/27)

#### Mês 7 (mai) — **Python** começa + dados
- **Etapa 7 (meses 7–9).** Estatística (7.1) vem antes de pandas; probabilidade e álgebra linear (7.6, 7.7) antes de machine learning.
- **Passo a passo:**
  1. **Python do zero→confortável** (reusa a lógica que você já tem de TS): [trilha-dados-ia](trilha-dados-ia.md) IA0.
  2. **pandas:** analisar os dados reais do AM Gestão (vendas, caixa).
  3. **SQL avançado:** `GROUP BY`, window functions, índices.
  4. **Robótica:** protótipo 2 (algo útil para casa/terreno).
- **Recursos:** [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/) · [trilha-dados-ia](trilha-dados-ia.md).
- **Entregável:** **dashboard de dados do próprio produto** (o que vende mais, horário de pico).

#### Mês 8 (jun) — Python + **IA (início)** + tributos
- **Passo a passo:**
  1. **scikit-learn:** primeiro modelo simples (previsão de caixa / classificação de itens).
  2. **Pix / Pix Automático** no produto.
  3. **Finanças:** tributos de empresa, conciliação.
  4. **Trilha R-5 (custo de IA):** o roteador do setup decide código, IA local ou IA online por tarefa; medir tokens e custo de cada feature de IA do AM Gestão.
- **Recursos:** [scikit-learn](https://scikit-learn.org/stable/getting_started.html) · [Pix — Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/pix).
- **Entregável:** **5 clientes pagantes** + 1ª feature de dados no produto.

#### Mês 9 (jul) — **IA de verdade** (RAG/local) + SO internals
- **Passo a passo:**
  1. **Ollama + Python:** levar o RAG do Mês 5 para IA local (sem custo por chamada) e virar assistente dentro do AM Gestão.
  2. **PyTorch (noção):** entender o que há por baixo.
  3. **SO internals + C/C++ (leve):** processos, memória, arquivos.
- **Recursos:** [pgvector](https://github.com/pgvector/pgvector) · [Ollama](https://ollama.com/) · [trilha-dados-ia](trilha-dados-ia.md) IA5–IA7.
- **Entregável:** assistente/IA rodando no produto (seu diferencial de mercado).

### 🔵 TRIMESTRE 4 — Sênior, portfólio e lançamento (ago–out/27)

#### Mês 10 (ago) — Arquitetura + performance + DDD
- **Etapa 8 (meses 10–12).**
- **Passo a passo:**
  1. **SOLID, padrões, Clean Architecture, DDD** (Passos 8/12) — ler *Refactoring* e *DDD*.
  2. **Performance e escalabilidade.**
  3. **Go (ferramenta de performance).**
  4. **Investimentos:** sua metodologia aplicada ao módulo financeiro.
- **Entregável:** refactor do AM Gestão + **system design documentado** (material de entrevista).

#### Mês 11 (set) — Sistemas distribuídos + skills de sênior
- **Passo a passo:**
  1. **Cache, filas/outbox, consistência eventual** (ler *Designing Data-Intensive Applications*).
  2. **Algoritmos para entrevista** + **system design** (explicar um sistema grande em 45 min).
  3. **Portfólio público em inglês:** README, ADRs e estudos de caso dos seus sistemas.
  4. **Trilha R-6 (orquestrar agentes):** vários agentes em paralelo no setup (worktrees, revisão automática de PR que trata a descrição como não verificada, regra AK-0017), com você como revisor final.
- **Entregável:** **portfólio em inglês + registros de entrevista** (recrutador) — pronto para aplicar a vagas, inclusive fora.

#### Mês 12 (out) — AMtech OS + loja online + consolidação
- **Passo a passo:**
  1. **AMtech OS:** Linux com o dev-setup embutido — a trilha de SO culmina aqui.
  2. **Loja online (módulo Vendra)** no AM Gestão.
  3. **Revisão geral** + entrevistas simuladas (recrutador).
- **Entregável:** renda **rumo a R$ 7 mil líq./mês** + portfólio completo + **AMtech OS v1**.

---

## PARTE 4 — AS TRILHAS QUE NUNCA PAUSAM

Correm por baixo do mês inteiro, em blocos pequenos e fixos:

| Trilha | Quando | Como |
|---|---|---|
| **Inglês** | Todo dia, 20–30 min | Doc em inglês, 1 vídeo, Anki. Meta C1. [ingles-espanhol-integrado](ingles-espanhol-integrado.md) |
| **Matemática (VHSlins)** | Sexta de manhã | Integrada à programação e à Licenciatura. [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md) |
| **Licenciatura em Matemática** | Quinta tarde (domingo só com prazo) | Prazos reais da faculdade mandam |
| **Física (leve)** | Sábado | Ligada a hardware/robótica |
| **Base do Akita** | Terça, 6h–7h | 1 episódio por semana + nota de 5 frases. Ordem na Parte 4.2; o Professor entrega (trilha `base`) |
| **Revisar código de IA (Trilha R)** | Dentro do ofício, desde o Mês 2 | Checklist e etapas na Parte 4.1 |
| **Registro de leitura** | Depois de cada leitura | `just livros ler ...` (seção 2.6b) |
| **Revisão espaçada (Anki)** | 10 min/dia + 30 min no domingo | O que trava sem isso, você esquece |

### 4.1 Trilha R — trabalhar com agentes de IA (o que o mercado e o seu setup cobram)

O seu setup é feito para a IA escrever e você conferir. Isso só funciona se **você souber revisar melhor do que a IA escreve**. Regra fixa: **aprendizado novo é sem IA; produção é com IA e com revisão sua.**

| Etapa | Mês | O que treinar | Prova de que aprendeu |
|---|---|---|---|
| R-1 | 2 | Revisar PR do agente com checklist | Nenhum PR do site entra sem o checklist preenchido |
| R-2 | 3 | Teste antes do código: você escreve o teste, o agente implementa | 3 features do AM Gestão feitas assim |
| R-3 | 4 | Especificação e regras: `CLAUDE.md` por projeto, pedido sem ambiguidade | O agente erra menos na 2ª semana do que na 1ª (anote) |
| R-4 | 6 | Avaliar IA: conjunto de perguntas com resposta esperada no CI | A busca do AM Gestão tem nota e a nota não cai |
| R-5 | 8 | Custo: tokens, roteador local/online, cache | Custo por feature de IA medido e no painel |
| R-6 | 11 | Orquestrar vários agentes e revisar em lote | 1 semana com 3 agentes em paralelo sem quebrar a main |

**Checklist de revisão (R-1 em diante):** (1) eu sei explicar cada linha? (2) tem teste que falha sem a mudança? (3) dinheiro, data e fuso estão certos? (4) entrou segredo, dependência nova ou permissão a mais? (5) o que acontece se der erro no meio? (6) dá para reverter com um comando?

### 4.2 Base do Akita — os fundamentos de computação, em ordem

O que o Akita insiste que todo programador precisa entender por baixo da linguagem: como o computador funciona, sistema operacional, redes, concorrência, memória, criptografia, estruturas de dados e bancos. Cada módulo tem 2 episódios; o Professor entrega um por vez, na terça (`just professor hoje`). Os posts práticos (Git, Docker, backup, segredos, ai-jail) já vêm junto com os módulos de setup.

| Trimestre | Módulos (trilha `base` do Professor) |
|---|---|
| T1 | `b-aprender` (#76, #65) · `b-computador` (#80, #81) · `b-linux-wsl` (#60, #54) · `b-iniciante` (#38, #39) · `b-backend` (#40, #41) · `b-redes-1` (#121, #122) · `b-redes-2` (#123, #124) |
| T2 | `b-concorrencia` (#43, #44) · `b-memoria` (#45, #46) · `b-cripto` (#67, #68) · `b-hardware` (#97, #98) · `b-armazenamento` (#101, #117) · `b-devops` (#47, #48) · `b-containers` (#139, #113) |
| T3 | `b-redes-3` (#125, #126) · `b-testes-perf` (#130, #133) · `b-escala` (#110, #118) · `b-estruturas` (#95, #140) · `b-bancos` (#143, #49) · `b-ia` (#142, #148) |
| T4 | `b-linux-boot` (#127, #116) · `b-cripto-pratica` (#147, #145) · `b-linguagens` (#15, #16) · `b-oficio` (#23, #104) |

Lista completa e links: `docs/akita/trilha-estudo.md` no dev-setup. As regras que o setup extrai dos posts novos (`just akita pendentes`) são outra coisa: decidem como o setup trabalha, não o que você estuda.

---

## PARTE 5 — COMO SABER QUE ESTÁ DANDO CERTO (checkpoints)

- **Fim do T1:** 1 site pago, 1 CLI em Go, planilha à venda, ambiente redondo, 1ª chamada de IA em TS, 7 módulos da base do Akita, R-1 e R-2 em uso.
- **Fim do T2:** MVP do AM Gestão num restaurante real + 10 planilhas vendidas + busca com IA (RAG em TS) avaliada no CI.
- **Fim do T3:** 5 clientes pagantes + IA no produto + Python/dados sólidos.
- **Fim do T4:** portfólio sênior em inglês + AMtech OS + renda rumo a R$ 7k/mês.
- **Semanal:** `just progresso` no dev-setup + 1 registro de recrutador.

Se um mês atrasar, **não empilha**: termina o ativo em curso antes de começar o próximo. Um por vez é o que mais reduz atraso.

---

## 🔗 Trilhas com o detalhe profundo
- [trilha-engenharia-software](trilha-engenharia-software.md) · [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) · [trilha-go-ferramentas](trilha-go-ferramentas.md) · [trilha-dados-ia](trilha-dados-ia.md) · [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md) · [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md) · [trilha-financas-economia](trilha-financas-economia.md) · [ingles-espanhol-integrado](ingles-espanhol-integrado.md) · [metodo-de-estudo](metodo-de-estudo.md)
- Plano e stack: [PLANO-UNICO-AMtech](../PLANO-UNICO-AMtech.md) · [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md)
