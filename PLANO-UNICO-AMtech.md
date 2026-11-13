# PLANO ÚNICO — AMtech

Data: 2026-11-13 (atualizado para a nova realidade) · Alan Mateus

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

## 2. A stack (recomendação — confirmar)

Dois pilares, guiados por mercado, não stack fixa:

- **TypeScript + Next.js + PostgreSQL (Supabase)** — web, SaaS, sites, tudo que
  vira renda rápido. Uma linguagem no front e no back = menos troca de contexto
  (bom para TDAH e para construir sozinho com alto volume).
- **Python** — dados, IA e finanças. Motor de crescimento e diferencial.
- **SQL/PostgreSQL** por baixo dos dois. **Go** para ferramentas de linha de
  comando. **C/C++ e Rust** entram pela trilha de baixo nível (ver §3).

**Decisão pendente sua:** eu recomendo **tirar o .NET do centro** e usá-lo só
quando um emprego ou cliente pagar por ele — para construir e vender produto
rápido + IA, TS+Python abre mais portas. Como o ecossistema Aura foi desenhado em
.NET, essa troca tem custo; **confirme antes de eu marcar como definitivo.**

Por que isso protege da mudança de mercado: TS e Python são as duas apostas que o
mercado menos vai abandonar (Python lidera vagas e IA; JS/TS dominam a web).

---

## 3. As trilhas — o que é ativo e o que fica na fila

Decisões de 13/11: **mandarim removido**; **robótica mantida ativa**; **dominar
SO/Linux mantido ativo** (construir o AM-OS continua horizonte).

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
| **Linux/Arch + conceitos de SO (internals)** | **Ativo** | 🆕 Fundamento forte para dev/IA; Arch como máquina do dia a dia (estilo Akita) |
| Redes | Fila curta | Quando deploy/segurança pedir |
| Finanças F4–F8 (valuation, mercado, econometria) | Fila | Depois do T4 |
| Segurança / pentest + 1 certificação | Fila | Depois de redes/Linux |
| Baixo nível a fundo: C/C++, École 42 | Fila | Alimenta o SO e a robótica |
| **AM-OS / AM Linux (SO próprio como produto)** | Fila longa | Dominar SO é agora; *fabricar* o seu SO é depois |
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
| PDV / Caixa | AM Kaixara | Venda no balcão, ficha técnica, cardápio |
| Pedidos / Delivery | AM Rotara | Pedido online, entrega, geolocalização |
| Financeiro | AM Rendara | Caixa, contas, DRE, conciliação |
| Loja online (opcional) | AM Vendra | Venda online para além do restaurante |

Nome provisório: **AM Gestão** (um produto, vários módulos). **MVP = PDV +
Pedidos + Financeiro básico**, lançado primeiro para os restaurantes/vendedores
que já te procuram. A loja online entra como módulo depois que o MVP vender.

Isso é melhor que 23 sistemas por três motivos: você termina **um**, vende
**um**, e um cliente que usa PDV + pedidos + financeiro junto dificilmente troca
(fica preso ao valor). Os outros sistemas antigos viram, no máximo, módulos
futuros — não produtos separados.

---

## 5. Os 12 meses — a espinha

~2h/dia reais; 4h é bônus. Cada trimestre: avança o AM Gestão, estuda o que ele
pede, testa uma renda.

| Trim. | Construir (AM Gestão + web) | Estudar junto | Renda que testa | Repos |
|---|---|---|---|---|
| **1 · nov/26–jan/27** | Setup; fundamentos TS/Python + SQL; 1 site de cliente | Contabilidade básica; matemática VHSlins | 1 site pago; aulas particulares; planilha do financeiro à venda; 3 posts | dev-setup, github.io, catalogo-html, ensino-ti |
| **2 · fev–abr/27** | MVP do AM Gestão (PDV + Pedidos + Financeiro); deploy, testes, Docker | Matemática financeira | 10 planilhas vendidas; MVP rodando em 1 restaurante que já te procura | dev-setup, am-gestao (novo) |
| **3 · mai–jul/27** | Pix/Pix Automático, loja online (módulo Vendra), observabilidade; começa Python/dados | Tributos de empresa; conciliação | 5 clientes pagantes (restaurantes + vendas online) | am-gestao |
| **4 · ago–out/27** | IA no produto (ex.: previsão de caixa, classificação de itens); DDD, performance | Investimentos (sua metodologia no financeiro) | Renda rumo a R$ 7 mil líq./mês; 12 posts/ano | am-gestao, github.io |

Robótica e SO rodam **em paralelo leve**, com saída concreta: um protótipo para
casa/terreno por trimestre e o Arch como máquina do dia a dia — sem roubar o foco
do AM Gestão.

**Nunca pausa:** Licenciatura, inglês, validar antes de construir, regras de
segurança/alunos, dormir.

---

## 6. As fontes de renda — foco em 4 que compõem

De 47 para as 4 que saem do mesmo estudo e se reforçam:

1. **Aulas particulares** — caixa agora.
2. **Mini-curso de Lógica** — escala o que você ensina.
3. **Sites para empresas** — freela com a stack nova.
4. **AM Gestão (SaaS)** — o produto, começando pela planilha do financeiro.

O resto (infoprodutos, editora, serviços locais, robótica comercial) entra **uma
por vez, depois da primeira venda**, na ordem da pontuação. Negócios físicos
(padaria, delivery, sushi) saem do mapa ativo.

---

## 7. As empresas — uma, com linhas de produto

De 3 empresas para **uma com linhas**: a **Grupo AMtech** é o veículo; o
**Instituto AMS** é a linha de cursos (nasce das suas aulas); a **Editora** fica
pausada. Não abra 3 CNPJs — uma estrutura, vários produtos.

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

1. Você confirma: **(a)** a stack (tirar .NET do centro, sim/não) e **(b)** o
   nome e os módulos do AM Gestão.
2. Eu fecho a consolidação (este plano como fonte única + `repos.json` no
   dev-setup), você dá merge.
3. **Montamos a rotina** com seus horários reais.
4. Começamos o bloco 1 com o professor e o recrutador.

---

### Fontes de mercado
Linguagens: tekrevol, boundev.ai, devopscube (nov/2026). IA/ML: IEEE Spectrum
(BLS), 365datascience. Segurança: ISC2 via hakia, destcert, SANS.
