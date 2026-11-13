---
tags: [estudo, engenharia-de-software, portfolio-ams]
tipo: trilha
status: ativo
atualizado: 2026-10-26
---

# 🏗️ Engenharia de Software — O Currículo Completo, Mapeado nos Passos

> **Em palavras simples:** engenharia de software é tudo o que faz um sistema funcionar bem por anos, e não só hoje: organização do código, testes, segurança, publicação e, no seu caso, fazer contas com dinheiro sem nunca errar um centavo.

> **O que este documento é:** o mapa do seu estudo autodidata de engenharia de software. A maior parte **já é a Trilha Principal** do [Sumário Único](PLANO-UNICO-AMtech.md) — aqui ela aparece organizada por área (como num currículo de faculdade), para você ver que nada ficou de fora e saber o que **acrescentar**.
>
> **Detalhe técnico completo de cada camada** (o que dominar, item por item, e o critério de sênior): [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md).
>
> **O que é novo aqui:** a área **Engenharia de sistemas financeiros**, que conecta esta trilha com a [Trilha de Finanças e Economia](trilha-financas-economia.md). É o seu diferencial: pouca gente sabe programar dinheiro direito.

---

## 🗺️ Áreas × onde cada uma é estudada

| Área | Onde já está | O que acrescentar |
|---|---|---|
| **Fundamentos** (lógica, estruturas de dados, algoritmos) | Passos 1, 3 · horizonte longo §Ciência da Computação | Big-O e estruturas de dados formalmente, junto da École 42 |
| **Requisitos e modelagem** | Seus documentos de projeto (RF/RNF, RNFT) em `02-sistemas-de-negocio` | Histórias de usuário e critérios de aceite (já usa no EPIC-01) |
| **Banco de dados** | Passos 2, 5, 9 | Transações e níveis de isolamento a fundo (ver §financeiro) |
| **Construção** (TypeScript, Next.js, Python) | Passos 3–5, 7 | — |
| **Qualidade e testes** | Passo 6 | Testes de propriedade para regra de dinheiro |
| **Design e arquitetura** (SOLID, padrões, Clean Architecture, DDD) | Passos 8, 12 | DDD estratégico (contextos delimitados entre os sistemas Aura) |
| **DevOps e produção** (CI/CD, Docker, deploy, observabilidade) | Passos 2, 6, 10, 11, 12 | — |
| **Sistemas distribuídos** (cache, mensageria, tempo real, consistência) | Passos 9, 13 · [perfil-senior-completo-auditoria](perfil-senior-completo-auditoria.md) | Mensageria (fila, outbox), consistência eventual |
| **Segurança de aplicação** | Passo 4 (OWASP) · [roadmap de segurança](roadmap-seguranca-ofensiva-completo.md) | — |
| **Processo e gestão** (Scrum, Kanban, RAD) | EPIC-01 · AM Taskoro | — |
| **Engenharia de sistemas financeiros** | Espalhado (RNFT-E01/E02) | 🆕 **Área própria — abaixo** |
| **Engenharia de sistemas de IA** | — | 🆕 [trilha-dados-ia](trilha-dados-ia.md) IA5–IA7 |

---

## 💰 Engenharia de sistemas financeiros *(área nova)*

Entra **dentro dos Passos** que já constroem o Kaixara e o Rendara — não é bloco separado.

| Tópico | O que significa | Passo |
|---|---|---|
| Dinheiro em `decimal`, nunca `float`/`double` | Erro de centavo vira prejuízo e processo | Passo 3 |
| Arredondamento (bancário × comercial) e onde arredondar | Regra explícita, testada | Passo 5 |
| **Ledger de partidas dobradas** | Todo movimento gera débito e crédito; saldo é derivado, nunca editado | Passo 7 (com F1 da Trilha de Finanças) |
| Idempotência de pagamento (RNFT-E02) | Cobrar duas vezes é o pior bug possível | Passo 7 |
| Concorrência otimista (RNFT-E01, `RowVersion`) | Estoque e saldo não ficam negativos sob carga | Passo 5 |
| Trilha de auditoria imutável | Ninguém apaga lançamento; corrige com estorno | Passo 7 · `aura-historico` |
| Conciliação | Comparar o que o sistema diz com o que o banco diz | Passo 14 (Rendara) |
| Pix, Open Finance, ISO 20022 | Integração com o sistema de pagamentos brasileiro | Passo 14 (com F5) |
| Fuso horário, data de competência × data de caixa | A mesma venda cai em meses diferentes conforme a regra | Passo 7 |

**✅ Pronto quando:** o Kaixara passa num teste que dispara o mesmo pagamento 100 vezes em paralelo e cobra uma vez só, e o ledger fecha em zero.

---

## 📚 Leituras de engenharia (uma por vez, no ritmo dos Passos)

| Livro | Autor | Quando |
|---|---|---|
| *Refactoring* | Martin Fowler | Passo 8 |
| *Patterns of Enterprise Application Architecture* | Martin Fowler | Passo 8 (tem padrões de dinheiro e de transação) |
| *Domain-Driven Design* | Eric Evans | Passo 12 |
| *Designing Data-Intensive Applications* | Martin Kleppmann | Passos 9–13 (o mais importante da lista) |
| *Release It!* | Michael Nygard | Passo 10 |
| *Software Engineering at Google* | Winters, Manshreck e Wright | Passo 12+ |

Hábitos que continuam: roadmap.sh como auditoria e Fábio Akita ([integracao-42-roadmap-akita](integracao-42-roadmap-akita.md)).

## 🌍 Sênior para o Brasil e para o exterior
Não haverá faculdade de engenharia de software: este documento é o currículo. Para ser contratado como sênior, principalmente fora do Brasil, somam-se:
- **Inglês fluente** (leitura, escrita técnica e entrevista falada) — o maior filtro para vaga no exterior. Meta: C1. Ver [ingles-espanhol-integrado](ingles-espanhol-integrado.md).
- **Algoritmos e estruturas de dados para entrevista** — exercícios no estilo das entrevistas técnicas internacionais, a partir do Passo 8.
- **System design** — explicar e desenhar a arquitetura de um sistema grande em 45 minutos; o Aura é o seu material de treino ([perfil-senior-completo-auditoria](perfil-senior-completo-auditoria.md)).
- **Portfólio público em inglês** — README, ADRs e estudos de caso dos sistemas em inglês (Inglês Fase C, Passo 9).
- **Diploma reconhecido lá fora** — por isso a faculdade para IA (Ciência da Computação ou IA) está em [formacao-academica](formacao-academica.md).

O conteúdo teórico de computação (compiladores, SO, teoria da computação — os livros de Sipser e Petzold que você já comprou) mora no [mapa-horizonte-longo-sistemas](mapa-horizonte-longo-sistemas.md).
