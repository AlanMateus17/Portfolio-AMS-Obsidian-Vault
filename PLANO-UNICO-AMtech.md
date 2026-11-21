# PLANO ÚNICO — AMtech

Data: 2026-11-13 (nova realidade) · revisado em 2026-11-20 (rendas, empresas e suítes) · Alan Mateus

> **Este é o único planejamento.** Substitui o Plano Unificado, o Sumário Único,
> o Plano Mestre passo a passo e os rascunhos. Todos viraram referência em
> `99-arquivo/`. Se dois documentos divergirem, **este vence.** A rotina diária
> (horários) é o próximo passo, feita a partir daqui.

---

## 1. O Norte e a regra única

**Norte:** ser desenvolvedor sênior capaz de criar IA e entender de dinheiro,
tendo a Grupo AMtech como veículo — no Brasil e no exterior, com várias fontes de
renda próprias.

**A regra única:** você nunca "só estuda". **Todo estudo constrói um ativo que
gera renda e vira portfólio.** Aprende → constrói → vende → o ativo prova
competência e abre vagas. Ensinar entra no meio (é renda e é o teste de domínio).

**A regra de foco:** no máximo **um ativo sendo construído + um sendo testado**
por vez. O resto fica na fila, anotado, sem ocupar a cabeça.

---

## 2. A stack (definitiva — 13/11)

Núcleo **TypeScript + Python + SQL**, stack por problema, não stack fixa. Detalhe
completo em [stack-tecnologica](05-stack-tecnologica/stack-tecnologica.md).

- **TypeScript + Next.js + PostgreSQL (Supabase)** — web, SaaS, sites, tudo que
  vira renda rápido. Uma linguagem no front e no back = menos troca de contexto
  (bom para TDAH e para construir sozinho com alto volume).
- **Python** — dados, IA e finanças. Motor de crescimento e diferencial.
- **SQL/PostgreSQL** por baixo dos dois. **Go** para ferramentas de linha de
  comando e o agente fiscal do PDV. **C/C++ e Rust** entram pela trilha de baixo
  nível e robótica (ver §3).

**Decisão tomada: o .NET sai do centro.** Vira carta de reserva — só quando um
emprego ou cliente pagar por ele, ou para o agente fiscal (onde Go também serve).
TS+Python abre mais portas para construir/vender produto + IA. O que foi
aposentado (C# base, ASP.NET, Clojure/Datomic, SignalR, EF Core, GraphQL) está
listado no `stack-tecnologica`.

Por que isso protege da mudança de mercado: TS e Python são as duas apostas que o
mercado menos vai abandonar (Python lidera vagas e IA; JS/TS dominam a web).

---

## 3. As trilhas — o que é ativo e o que fica na fila

Decisões de 13/11: **mandarim removido**; **robótica mantida ativa**; **sistema
operacional mantido por inteiro** — é parte de concluir o seu setup.

| Trilha | Horizonte | Observação |
|---|---|---|
| Fundamentos + Engenharia de software | **Ativo** | Base de tudo |
| Web (TS/Next.js) | **Ativo** | O que mais vira renda |
| Python + dados + IA | **Ativo** (entra no T3–T4) | Analista, big data, eng. de IA saem daqui |
| Finanças F0–F3 (investir, contabilidade, mat. financeira, tributos) | **Ativo** (leve) | Dentro dos sistemas |
| Matemática (VHSlins) | **Ativo** | Liga à Licenciatura e à IA |
| Física | **Ativo** (leve) | Sábado, ligada a hardware/robótica |
| Inglês | **Ativo** | Nunca pausa |
| **Robótica / IoT + IA embarcada** | **Ativo** | 🆕 Vaga na área + protótipos para casa e terreno + conteúdo de aula. Escopo: um protótipo útil por vez, não "dominar toda a robótica" |
| **Sistema operacional — Linux/Arch, internals e AMtech OS** | **Ativo** | Mantido por inteiro: parte de concluir o setup. Arch no dia a dia (estilo Akita), internals, e o AMtech OS = Linux com o dev-setup embutido |
| **Go — ferramentas, CLIs, automação, agente fiscal** | **Ativo** | 🆕 A linguagem das suas ferramentas. Entra no mês 2 e volta sempre que você precisar de um binário útil. Passo a passo em [trilha-go-ferramentas](07-estudo-e-carreira/trilha-go-ferramentas.md) |
| Baixo nível: C/C++, École 42 | **Ativo** (leve) | Alimenta o SO e a robótica |
| Redes | Fila curta | Quando deploy/segurança pedir |
| Finanças F4–F8 (valuation, mercado, econometria) | Fila | Depois do T4 |
| Segurança / pentest + 1 certificação | Fila | Depois de redes/Linux |
| Economia (faculdade), espanhol | Fila longa | Depois da Licenciatura |
| Agro, construção civil | Fila longa | Só depois do Norte andar |

Cargos (dev, analista, big data, eng. de IA, eng. de software) saem da mesma
base. Robótica + IA embarcada é um cruzamento extra que o mercado paga.

---

## 4. O produto único — um sistema completo, não 23

Decisão de 13/11: **acabou o império de 23 sistemas.** Em vez disso, **um sistema
só**, juntando o que faz sentido para o seu público real (restaurantes e quem
vende online — onde você já tem procura).

**Composição proposta (confirmar nome e módulos):**

| Módulo | Vem de | Faz |
|---|---|---|
| PDV / Caixa | o antigo Kaixara | Venda no balcão, ficha técnica, cardápio |
| Pedidos / Delivery | o antigo Rotara | Pedido online, entrega, geolocalização |
| Financeiro | o antigo Rendara | Caixa, contas, DRE, conciliação |
| Loja online (opcional) | o antigo Vendra | Venda online para além do restaurante |

Nome provisório: **AM Gestão** (um produto, vários módulos). **MVP = PDV +
Pedidos + Financeiro básico**, lançado primeiro para os restaurantes/vendedores
que já te procuram. A loja online entra como módulo depois que o MVP vender.

Isso é melhor que 23 sistemas por três motivos: você termina **um**, vende
**um**, e um cliente que usa PDV + pedidos + financeiro junto dificilmente troca
(fica preso ao valor). Com o MVP pronto, o AM Gestão é vendido em **pacotes**
(Caixa · Caixa + Financeiro · Integrado · Integrado + Loja · Pedidos com a sua
marca). Os outros sistemas antigos seguem o mesmo raciocínio (decisão de 20/11):
viram **suítes** de 3 ou mais sistemas, vendidas em pacotes, uma por vez e só
depois da anterior vender — AM Serviços (agenda, assistência, veterinária),
AM Escola (gestão escolar, AM Mentor, plataforma de cursos, documentos) e
AM Projetos (Kanban, obras, diagnóstico por IA).

---

## 5. Os 12 meses — a espinha

~2h/dia reais; 4h é bônus. Cada trimestre: avança o AM Gestão, estuda o que ele
pede, testa uma renda. **O passo a passo mês a mês, com rotina semanal real,
recursos e exemplos, está em [PLANO-PASSO-A-PASSO](07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md).**

| Trim. | Construir (AM Gestão + web) | Estudar junto | Renda que testa | Repos |
|---|---|---|---|---|
| **1 · nov/26–jan/27** | Setup; fundamentos TS/Python + SQL; mini-curso de Lógica | Contabilidade básica; matemática VHSlins | Mini-curso no ar; planilha do financeiro à venda; primeiros vídeos do Primer Code | dev-setup, github.io, catalogo-html, ensino-ti |
| **2 · fev–abr/27** | MVP do AM Gestão (PDV + Pedidos + Financeiro); deploy, testes, Docker | Matemática financeira | 10 planilhas vendidas; MVP rodando em 1 restaurante que já te procura; Anki e AM Mentor; Bancada Dev | dev-setup, am-gestao (novo) |
| **3 · mai–jul/27** | Pix/Pix Automático, loja online (módulo Vendra), observabilidade; começa Python/dados | Tributos de empresa; conciliação | 5 clientes pagantes nos pacotes do AM Gestão; Udemy; canal de finanças | am-gestao |
| **4 · ago–out/27** | IA no produto (ex.: previsão de caixa, classificação de itens); DDD, performance | Investimentos (sua metodologia no financeiro) | Renda rumo a R$ 7 mil líq./mês; AM Serviços e Maker Digital começam | am-gestao, github.io |

Robótica e SO rodam **em paralelo leve**, com saída concreta: um protótipo para
casa/terreno por trimestre e o Arch como máquina do dia a dia — sem roubar o foco
do AM Gestão.

**Nunca pausa:** Licenciatura, inglês, validar antes de construir, regras de
segurança/alunos, dormir.

---

## 6. As fontes de renda — só passivas, em ondas (decisão de 18/11)

Só **rendas passivas** entram no plano, em ondas. A onda seguinte só começa quando
uma da atual passar no portão (3 meses se pagando). Lista completa, com tipo e
onda de cada oferta, no dev-setup: `docs/operacao/portfolio.md` e `docs/empresas.md`.

- **Onda 0 — agora (no máximo 4):** mini-curso de Lógica · canais sem rosto ·
  planilha do AM Gestão (financeiro) · catálogo do HTML.
- **Os 3 canais sem rosto:** **Primer Code** (lógica e programação), **Bancada Dev**
  (setup e ferramentas) e um canal de finanças com **nome a definir** (Bolso Exato
  está ocupado).
- **Onda 1:** Anki · templates · modelos financeiros · calculadoras · Udemy · afiliados.
- **Onda 2:** monetização das plataformas · newsletter · AM Mentor · simulados ·
  aulas prontas para professores · fábrica de documentos para professores ·
  dublagem · templates em inglês · UI kits · canal em público.
- **Onda 3:** AM Gestão SaaS (Kaixara e Rotara) · formação técnica · comunidade ·
  livro · camisetas · dividendos.
- **Rendas ativas, fora das ondas:** sites, aulas particulares, sistemas sob
  encomenda e laudo de segurança de sites — só o que chegar, sem prospectar.
- **Saíram do plano:** avaliação de IA (18/11); restaurantes próprios, mercadinho,
  máquina de lanches, revenda de veículos e revendas de usados (20/11).

---

## 7. As empresas — 6 marcas, CNPJ só quando faturar (decisão de 20/11)

Uma empresa por área, para nada ficar confuso; o **Grupo AMtech Digital** é o
nome-mãe. CNPJ próprio só quando cada uma faturar (confirmar com contador).
Detalhe, produtos e pacotes de cada uma em `docs/empresas.md` do dev-setup.

| Empresa | Estado | Produtos principais |
|---|---|---|
| **AMtech Software** | ativa | AM Gestão e as suítes; Kit Dev; sites sob demanda |
| **Instituto AMS Silva** | ativa | Trilha Lógica; formações; para professores; catálogo do HTML |
| **AMtech Mídia** | ativa | Primer Code, Bancada Dev, canal de finanças; Kit Finanças |
| **AMtech Maker** | software primeiro | Maker Digital → kits, serviços de campo e loja (fase 2) |
| **AM Logística** | software primeiro | Pedidos do AM Gestão → entregas e delivery (fase 2) |
| **Editora AMS Silva** | pausada | Coleção *Lógica e Máquina* (6 volumes, escrita a partir das suas notas) |

**Sequência:** 1) mini-curso, planilha do AM Gestão e Primer Code · 2) MVP do AM
Gestão em 1 restaurante, Anki e AM Mentor, Bancada Dev · 3) pacotes do AM Gestão,
Udemy, canal de finanças · 4) AM Serviços e Maker Digital · depois Editora e as
fases físicas, só no gatilho. Patrimônio é finança pessoal, não empresa.

---

## 8. Como fazer com o mínimo de erro

1. **Um ativo por vez** (a regra que mais reduz atraso).
2. **Validar antes de construir** (planilha antes do sistema).
3. **Professor** (como estudar): blocos de 25 min, 20/80, exemplo → você tenta →
   prova sem consulta, revisão espaçada.
4. **Recrutador** (provar no mercado): cada estudo vira registro de entrevista +
   item de portfólio.
5. **Confiabilidade:** backup 3-2-1, tudo no Git, segredos no KeePassXC, testes,
   esteira de segurança (`pentest/security.yml`), Docker.
6. **Medir, não achar:** `just progresso` e o "pronto quando" de cada trimestre.

---

## 9. O que este documento substitui

Em `99-arquivo/`: Plano Unificado, Sumário Único, Plano Mestre passo a passo e os
rascunhos. O `plano-eixo.md` do dev-setup é absorvido por este e continua sendo o
que o professor lê.

---

## 10. Próximo passo

1. ✅ Stack definida (.NET fora do centro). Falta você confirmar o **nome e os
   módulos do AM Gestão**.
2. Eu fecho a consolidação (este plano como fonte única + `repos.json` no
   dev-setup), você dá merge.
3. **Montamos a rotina** com seus horários reais.
4. Começamos o bloco 1 com o professor e o recrutador.

---

### Fontes de mercado
Linguagens: tekrevol, boundev.ai, devopscube (nov/2026). IA/ML: IEEE Spectrum
(BLS), 365datascience. Segurança: ISC2 via hakia, destcert, SANS.
