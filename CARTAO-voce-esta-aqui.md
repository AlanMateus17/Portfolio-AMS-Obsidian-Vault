---
tags: [hoje, portfolio-ams]
tipo: dashboard-diario
atualizado: 2026-11-21
---

# 📍 Você Está Aqui

> **Uma porta só.** Quando o setup estiver instalado, quem manda é o `just professor hoje`. Ele segue o mesmo plano e a mesma semana deste cartão. **Até lá, quem manda é este cartão.**
> Plano completo (só para consulta): [PLANO-PASSO-A-PASSO](07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md) · tudo o que você vai estudar: [mapa-de-estudo](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/MAPA.md)

**Fase atual:** Trimestre 1 → Mês 1 → **Etapa 0: a base de tudo** → agora: **0.1 e 0.2**
**Ativo que este mês entrega:** repositório `logica-ts` com os 3 exercícios resolvidos em TypeScript, sem IA

> O Mês 1 começa de fato em 23/11 e vai até 27/12 (5 semanas: o 0.1 e o 0.2 ganharam uma semana só deles). O resto do plano anda junto. Isso não é atraso: estimativa é hipótese, e o tempo medido corrige o plano.

---

## ✅ Todo dia (nunca pausa)
- [ ] **Inglês 20–30 min** (Anki + 1 vídeo ou 1 página de documentação em inglês)
- [ ] **Leu algo? Registre:** `just livros ler LIVRO --trecho ... --min ... --assunto ... --nota "com as suas palavras"`
- [ ] **Errou?** `just erro ETAPA "o erro" --certo "o certo"` · **O setup travou?** `just atrito "..." --area ...`
- [ ] **Começou um assunto?** Diagnóstico primeiro: `just diag ETAPA c3 x2 c1` · **Terminou?** `just ficha ETAPA` e `just colher ETAPA`

## 🛒 Comprar agora
- [ ] **Código**, Charles Petzold, 2ª edição (Bookman, 2023), ISBN 9788582606315: livro do 0.4 e 0.5. Até chegar, use o arquivo do assunto, o Akita #80 e #81 e o site grátis do livro (codehiddenlanguage.com). Quando chegar: `just livros marcar petzold-codigo tenho`.

## 🗓️ Semana 1 — 23 a 29/11 · Etapa 0: primeiro o 0.1 e o 0.2, até o fim

> **Remarcada em 21/11:** a semana de 17 a 23/11 não aconteceu (o setup ainda estava sendo instalado). Não é atraso: o plano anda pelo tempo medido.
> **Regra desta semana:** só os dois assuntos que já estão escritos e conferidos. O próximo só entra quando estiver pronto. O `just professor hoje` (v2.40) segue esta mesma ordem: o 0.2 só libera depois que o 0.1 passar na prova.
> **Comandos `just`:** rodam no Ubuntu, em `~/dev/dev-setup`. Se o setup ainda não estiver de pé, escreva o comando no caderno e rode depois.
> **Hoje e amanhã (sáb 21 e dom 22):** livres. Se quiser adiantar, faça só o diagnóstico do 0.1 (seção 0 do arquivo).

| Dia | Bloco | O que fazer | Feito |
|---|---|---|---|
| Seg 23 | 6–8h | **Setup de pé:** na cópia do Windows, `git pull`; no Ubuntu, `just verificar`, clonar o mapa em `~/dev/mapa-de-estudo` e conferir `just professor hoje`. O que travar: `just atrito`. | [ ] |
| Ter 24 | 6–7h | **Akita `b-aprender`** (#76 e #65) + nota de 5 frases, de cabeça. | [ ] |
| Qua 25 | 6–8h | **[0.1 Aprender a aprender](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/assuntos/00-aprender-a-aprender/aprender-a-aprender.md), blocos 1 a 4.** Comece pelo diagnóstico, nos 7 passos da seção 0: `just diag 0.1 ...`. | [ ] |
| Qui 26 | 6–9h | **0.1, blocos 5 e 6:** exemplos, Anki com FSRS ligado, exercícios N1 a N3. **Fechar o 0.1:** `just ficha 0.1` sem abrir o arquivo, corrigir pelo gabarito e registrar: `just professor nota b-aprender NOTA`. | [ ] |
| Sex 27 | 6–11h | **[0.2 Linguagem matemática e lógica](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/assuntos/01-matematica/linguagem-matematica-e-logica.md), blocos 1 a 6**, com o VHSlins Cap. 1 no papel. Confira no livro a precedência de → e ↔. | [ ] |
| Sáb 28 | 6–10h | **0.2, blocos 7 a 10** (N3, N4 em TypeScript, resumo e cartões). | [ ] |
| Sáb 28 | 10–12h | **Fechar o 0.2:** `just ficha 0.2`, gabarito e `just professor nota mat-linguagem NOTA`. Depois `just colher 0.1` e `just colher 0.2`: os planos de aula vão para o `ensino-ti` e os exercícios para o Anki. | [ ] |
| Dom 29 | — | **Folga.** Só 30 min de Anki. | [ ] |
| Seg 30 | 6–8h | **Revisão espaçada:** exercícios N3 do 0.1 e do 0.2 de cabeça, com o material fechado; o que errar vai para `just erro`. | [ ] |

## 🗓️ Semana 2 — 30/11 a 06/12
- [ ] **0.3 Teoria dos conjuntos** (VHSlins Cap. 2), **0.4 e 0.5 Como o computador funciona e representação de dados** (Petzold, *Código*), **um de cada vez e só quando o arquivo estiver escrito e conferido**.
- [ ] Se nenhum estiver pronto: revisão espaçada do 0.1 e do 0.2, inglês e o livro do Petzold no papel (registre com `just livros ler ...`).

**Semanas 3 a 5 (07 a 27/12):** 0.6 lógica de programação (os 3 exercícios no TS Playground, sem IA), 0.7, sistema operacional, WSL2 e terminal (1.1 a 1.3); criptografia essencial, Git (aí sim nasce o repo `logica-ts`), segredos e backup (1.4 a 1.7); Docker, `just`, Núcleo e segurança de agentes (1.8 a 1.10) e TypeScript no terminal com testes (2.1, 2.4). A semana do Natal é curta. O detalhe dia a dia entra aqui quando a semana anterior fechar.

> Os arquivos dos assuntos de cada semana são escritos e conferidos antes dela, pelo protocolo do [MAPA](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/MAPA.md#como-cada-arquivo-é-escrito).

---

## 🎯 Critério de pronto do Mês 1
- [ ] Resolvo os 3 exercícios de lógica em TS **sem travar e sem IA**
- [ ] Consigo explicar cada um em 3–5 frases sem jargão
- [ ] Repositório `logica-ts` público no GitHub
- [ ] Sei rodar `just professor hoje`, fazer commit/branch/PR e restaurar um backup

## 🔁 Em todo bloco de 25 min
Feche o material → reconstrua de cabeça → explique em 3–5 frases → faça 1–3 cartões no Anki → rode o comando da coluna "Ao terminar, registre" do roteiro.

---

## 🚫 Não pense nisso agora: está guardado, não perdido
AM Gestão, Go, Python, IA, pentest, AMtech OS, os outros negócios. Tudo isso tem mês marcado no plano. **Agora é só a linha da tabela de hoje.**

## 🧭 Se perder o fio
Releia só este cartão e faça a próxima linha sem `[x]`. Não abra os outros arquivos para "se situar".
