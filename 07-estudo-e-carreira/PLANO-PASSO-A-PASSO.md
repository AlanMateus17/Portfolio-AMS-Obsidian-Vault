---
tags: [estudo, rotina, passo-a-passo, portfolio-ams]
tipo: plano
status: ativo
atualizado: 2026-11-13
---

# 🧭 PLANO PASSO A PASSO + ROTINA — 12 meses

> **O que é:** o caminho exato, semana a semana e mês a mês, para você sair do lugar e virar o profissional mais completo possível em até 12 meses — alternando **todas** as trilhas (TS, Go, Python/dados/IA, SQL, matemática, finanças, inglês, física, robótica, sistema operacional, baixo nível) sem largar nenhuma.
>
> **Como ler:** o [[PLANO-UNICO-AMtech]] diz *o quê e por quê*; a [[stack-tecnologica]] diz *com o quê*; **este diz quando e como, dia a dia.** O detalhe profundo de cada área está nas trilhas (links no fim).
>
> **A regra que rege tudo:** você nunca "só estuda". **Cada bloco entrega um ativo** (uma ferramenta, uma parte do AM Gestão, um site, um protótipo) que vira renda e portfólio. No máximo **1 ativo sendo construído + 1 sendo testado** por vez.

---

## PARTE 1 — A ROTINA SEMANAL (feita sobre os seus horários reais)

Base real: você acorda **6h todo dia**; **segunda não tem restaurante**; **quinta não tem escola**; restaurante à noite de ter–dom; manhãs quase todas livres; precisa **cuidar dos cães todo dia**; Licenciatura em paralelo.

A âncora é simples e à prova de TDAH: **toda manhã, 6h–8h, é estudo**, antes do mundo acordar. É o bloco que nunca falha. O resto são blocos extras nos buracos livres.

| Dia | Manhã (6h–) | Tarde | Noite |
|---|---|---|---|
| **Segunda** | 6–8h âncora técnica (foco do mês) | Escola | **Bloco profundo 20–22h** (AM Gestão — sem restaurante!) |
| **Terça** | 6–7h leitura/inglês (escola de manhã) | Escola | Restaurante (até 22h) |
| **Quarta** | 6–8h âncora técnica | Escola | Restaurante |
| **Quinta** | **6–11h bloco profundo** (AM Gestão + trilha par) — seu maior dia | Livre → cães / Licenciatura | Restaurante |
| **Sexta** | 6–11h matemática (VHSlins) + Licenciatura + revisão | Escola+restaurante (12:55–23h) | — |
| **Sábado** | **6–13h: Go (ferramentas) + robótica/SO + física (leve)** | Restaurante (15–23h) | — |
| **Domingo** | **6–13h: Python/dados/IA + revisão espaçada + portfólio/recrutador** | Restaurante (15–23h) | — |

**Blocos fixos da semana:**
- **Âncora diária 6h–8h** (seg, qua) e 6h–7h (ter) → o foco técnico do mês.
- **Inglês todo dia, 20–30 min** → nunca pausa. Documentação em inglês, 1 vídeo, Anki. Encaixe no café/deslocamento.
- **Cães** → logo após a âncora ou no meio-dia; parte fixa da rotina, não "tempo perdido".
- **Dois blocos profundos de semana:** segunda à noite + quinta de manhã (os dois maiores vazios que você tem).
- **Fim de semana de manhã** → os blocos pesados (Go, Python/dados, robótica/SO, revisão).
- **Licenciatura** → quinta à tarde + domingo; ajuste aos prazos reais da faculdade.

**Conta de horas:** ~2h/dia na âncora + 2 blocos profundos (seg noite, qui manhã) + 3 manhãs de fim de semana ≈ **18–22h/semana reais**, com margem. Em semana corrida, só a âncora já mantém o ritmo.

---

## PARTE 2 — COMO ESTUDAR (método, não força de vontade)

Direto do seu "professor" do dev-setup, pensado pra TDAH:

1. **Blocos de 25 min** (Pomodoro), 5 de pausa. Dois ou três por sessão.
2. **20/80:** aprenda os 20% que resolvem 80%. Não leia a doc inteira — leia o que o ativo da semana pede.
3. **Ciclo de 4 passos por tópico:** (a) ver o conceito → (b) **você tenta sem olhar** → (c) prova sem consulta → (d) revisão espaçada (Anki no dia 1, 3, 7, 15).
4. **Sempre aplicado:** todo conceito novo vira linha de código num ativo real no mesmo dia.
5. **Recrutador:** cada semana vira um registro (o que aprendi, o que provei) + um item de portfólio em inglês. É assim que o estudo vira vaga.

---

## PARTE 3 — O PASSO A PASSO DE 12 MESES

Cada mês tem: **Foco · O que estudar (passo a passo) · Recursos · Exemplo/entregável.** As trilhas se alternam, mas as "nunca-pausam" (inglês, matemática, Licenciatura, física leve) correm por baixo o tempo todo.

### 🟢 TRIMESTRE 1 — Fundamentos viram o primeiro dinheiro (nov/26–jan/27)

#### Mês 1 (nov) — Setup + lógica + TypeScript do zero
- **Foco:** deixar a máquina pronta e começar a programar de verdade em TS.
- **Passo a passo:**
  1. **SO (leve):** montar o ambiente — WSL2/Arch, Git, Node, Python, Go, Docker, VS Code. Isso já é a trilha de SO começando.
  2. **Lógica (Passo 1):** refazer os 3 exercícios de lógica **em TypeScript**, sem IA.
  3. **TS:** tipos, arrays, `map/filter/reduce`, funções, `async/await`.
  4. **SQL básico:** `SELECT`, `WHERE`, `JOIN` num PostgreSQL local.
  5. **Matemática (VHSlins):** bloco 1, integrada.
- **Recursos:** [TS Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) · [SQLBolt](https://sqlbolt.com/) · [roadmap.sh/typescript](https://roadmap.sh/typescript).
- **Entregável:** ambiente reproduzível (`setup-dev.sh`) + repositório de exercícios de lógica em TS + começo de 1 site simples. **Renda:** primeiras aulas particulares.

#### Mês 2 (dez) — Web (Next.js) + SQL + **Go começa (ferramentas)**
- **Foco:** colocar um site no ar e fabricar sua primeira ferramenta.
- **Passo a passo:**
  1. **Next.js + Tailwind:** páginas, componentes, deploy na Vercel.
  2. **PostgreSQL via Supabase:** criar banco, tabela, consulta do app.
  3. **Go-1 e Go-2** ([trilha-go-ferramentas](trilha-go-ferramentas.md)): primeiro binário + organizador de arquivos.
  4. **Git fluente** + GitHub Actions básico (rodar teste a cada push).
  5. **Finanças F0 (leve):** contabilidade básica — débito/crédito.
- **Recursos:** [Next.js Learn](https://nextjs.org/learn) · [Supabase Docs](https://supabase.com/docs) · [Tour of Go](https://go.dev/tour/).
- **Entregável:** **1 site de cliente no ar (pago)** + 1 CLI em Go que você usa no dia a dia.

#### Mês 3 (jan) — Backend TS + API + banco a fundo + segurança
- **Foco:** sair do "site" para "sistema" — API, banco sério, segurança.
- **Passo a passo:**
  1. **API** em Next/NestJS: rotas, validação com Zod, status corretos.
  2. **ORM (Prisma/Drizzle):** migrations, relacionamentos, evitar N+1.
  3. **Segurança (Passo 4):** OWASP Top 10, autenticação, Row-Level Security do Supabase.
  4. **Testes (Vitest):** primeiro teste de unidade e de API.
  5. **Robótica (paralelo, sábado):** primeiro protótipo — LED/sensor no Arduino/ESP32.
- **Recursos:** [OWASP Top 10](https://owasp.org/www-project-top-ten/) · [Prisma Docs](https://www.prisma.io/docs) · [Vitest](https://vitest.dev/guide/).
- **Entregável:** **planilha do financeiro à venda** + esqueleto do AM Gestão com teste no CI + protótipo 1. **Renda:** aulas + site + planilha.

### 🟡 TRIMESTRE 2 — O produto nasce e roda num cliente (fev–abr/27)

#### Mês 4 (fev) — AM Gestão: módulo **Caixa (PDV)** + Go no agente fiscal
- **Foco:** o coração do produto, com dinheiro correto.
- **Passo a passo:**
  1. **Engenharia financeira (Passo 3/5):** dinheiro em `decimal` nunca `float`; arredondamento; idempotência de pagamento; concorrência otimista.
  2. **PDV offline:** SQLite local + sincronização quando a conexão volta.
  3. **Go-5 e Go-6:** servidor HTTP local + **agente fiscal** (impressora ESC/POS).
  4. **Matemática financeira:** juros, porcentagem aplicada ao PDV.
- **Recursos:** [trilha-go-ferramentas](trilha-go-ferramentas.md) Go-5/Go-6 · [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) (camada banco/testes).
- **Entregável:** módulo **Caixa** funcionando com impressão real.

#### Mês 5 (mar) — AM Gestão: **Pedidos + Financeiro** + deploy
- **Passo a passo:**
  1. **Pedidos/Delivery:** PostGIS (geolocalização, rotas).
  2. **Financeiro:** ledger de partidas dobradas (todo movimento = débito+crédito).
  3. **Deploy + Docker + CI/CD:** subir o MVP num servidor.
  4. **SO (paralelo):** Arch como máquina do dia a dia (daily driver).
- **Recursos:** [PostGIS](https://postgis.net/documentation/) · [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md).
- **Entregável:** **MVP (Caixa+Pedidos+Financeiro) rodando em 1 restaurante** que já te procura.

#### Mês 6 (abr) — Produção de verdade: testes + observabilidade
- **Passo a passo:**
  1. **Observabilidade (Passo 10):** logs estruturados, métricas, o que quebrou e por quê.
  2. **Testes de propriedade** para a regra de dinheiro (dispara 100 pagamentos, cobra 1).
  3. **Go (ferramenta 3):** CLI de deploy/monitoramento.
  4. **Inglês Fase B:** documentação técnica só em inglês a partir daqui.
- **Entregável:** MVP estável + **10 planilhas vendidas** + começo da base de clientes.

### 🟠 TRIMESTRE 3 — Dados, Python e os primeiros clientes pagantes (mai–jul/27)

#### Mês 7 (mai) — **Python** começa + dados
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
- **Recursos:** [scikit-learn](https://scikit-learn.org/stable/getting_started.html) · [Pix — Banco Central](https://www.bcb.gov.br/estabilidadefinanceira/pix).
- **Entregável:** **5 clientes pagantes** + 1ª feature de dados no produto.

#### Mês 9 (jul) — **IA de verdade** (RAG/local) + SO internals
- **Passo a passo:**
  1. **pgvector + Ollama:** busca semântica / assistente dentro do AM Gestão.
  2. **PyTorch (noção):** entender o que há por baixo.
  3. **SO internals + C/C++ (leve):** processos, memória, arquivos.
- **Recursos:** [pgvector](https://github.com/pgvector/pgvector) · [Ollama](https://ollama.com/) · [trilha-dados-ia](trilha-dados-ia.md) IA5–IA7.
- **Entregável:** assistente/IA rodando no produto (seu diferencial de mercado).

### 🔵 TRIMESTRE 4 — Sênior, portfólio e lançamento (ago–out/27)

#### Mês 10 (ago) — Arquitetura + performance + DDD
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
| **Licenciatura em Matemática** | Quinta tarde + domingo | Prazos reais da faculdade mandam |
| **Física (leve)** | Sábado | Ligada a hardware/robótica |
| **Revisão espaçada (Anki)** | Domingo + 10 min/dia | O que trava sem isso, você esquece |

---

## PARTE 5 — COMO SABER QUE ESTÁ DANDO CERTO (checkpoints)

- **Fim do T1:** 1 site pago, 1 CLI em Go, planilha à venda, ambiente redondo.
- **Fim do T2:** MVP do AM Gestão num restaurante real + 10 planilhas vendidas.
- **Fim do T3:** 5 clientes pagantes + IA no produto + Python/dados sólidos.
- **Fim do T4:** portfólio sênior em inglês + AMtech OS + renda rumo a R$ 7k/mês.
- **Semanal:** `just progresso` no dev-setup + 1 registro de recrutador.

Se um mês atrasar, **não empilha**: termina o ativo em curso antes de começar o próximo. Um por vez é o que mais reduz atraso.

---

## 🔗 Trilhas com o detalhe profundo
- [trilha-engenharia-software](trilha-engenharia-software.md) · [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) · [trilha-go-ferramentas](trilha-go-ferramentas.md) · [trilha-dados-ia](trilha-dados-ia.md) · [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md) · [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md) · [trilha-financas-economia](trilha-financas-economia.md) · [ingles-espanhol-integrado](ingles-espanhol-integrado.md) · [metodo-de-estudo](metodo-de-estudo.md)
- Plano e stack: [PLANO-UNICO-AMtech](../PLANO-UNICO-AMtech.md) · [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md)
