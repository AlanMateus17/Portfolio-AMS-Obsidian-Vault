---
tags: [hoje, portfolio-ams]
tipo: dashboard-diario
atualizado: 2026-11-17
---

# 📍 Você Está Aqui

> **Uma porta só.** Quando o setup estiver instalado, quem manda é o `just professor hoje`. Ele segue o mesmo plano e a mesma semana deste cartão. **Até lá, quem manda é este cartão.**
> Plano completo (só para consulta): [PLANO-PASSO-A-PASSO](07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md) · tudo o que você vai estudar: [mapa-de-estudo](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/MAPA.md)

**Fase atual:** Trimestre 1 → Mês 1 → **Etapa 0: a base de tudo** → agora: **0.1 e 0.2**
**Ativo que este mês entrega:** repositório `logica-ts` com os 3 exercícios resolvidos em TypeScript, sem IA

> O Mês 1 começou na metade de novembro, então o plano inteiro anda ~2 semanas para frente. Isso não é atraso: estimativa é hipótese, e o tempo medido corrige o plano.

---

## ✅ Todo dia (nunca pausa)
- [ ] **Inglês 20–30 min** (Anki + 1 vídeo ou 1 página de documentação em inglês)
- [ ] **Leu algo? Registre:** `just livros ler LIVRO --trecho ... --min ... --assunto ... --nota "com as suas palavras"`
- [ ] **Errou?** `just erro ETAPA "o erro" --certo "o certo"` · **O setup travou?** `just atrito "..." --area ...`
- [ ] **Começou um assunto?** Diagnóstico primeiro: `just diag ETAPA c3 x2 c1` · **Terminou?** `just ficha ETAPA` e `just colher ETAPA`

## 🛒 Comprar agora
- [ ] **Código**, Charles Petzold, 2ª edição (Bookman, 2023), ISBN 9788582606315: livro do 0.4 e 0.5. Até chegar, use o arquivo do assunto, o Akita #80 e #81 e o site grátis do livro (codehiddenlanguage.com). Quando chegar: `just livros marcar petzold-codigo tenho`.

## 🗓️ Semana 1 — 17 a 23/11 · Etapa 0: primeiro o 0.1 e o 0.2, até o fim

> **Regra desta semana:** só os dois assuntos que já estão escritos e conferidos. O próximo só entra quando estiver pronto.
> **Comandos `just`:** só funcionam com o setup instalado. Até lá, escreva o comando exato no caderno (por exemplo, `just diag 0.1 c3 x2 c1 --min 3`) e rode quando o setup estiver de pé.

| Dia | Bloco | O que fazer | Feito |
|---|---|---|---|
| Ter 17 | — | Só o inglês. | [ ] |
| Qua 18 | 6–8h | **[0.1 Aprender a aprender](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/assuntos/00-aprender-a-aprender/aprender-a-aprender.md), blocos 1 a 4.** Comece pelo diagnóstico, nos 7 passos da seção 0. | [ ] |
| Qui 19 | 6–9h | **0.1, blocos 5 e 6:** exemplos, Anki com FSRS ligado, exercícios N1 a N3. Depois, **fechar o 0.1:** `just ficha 0.1`, preencher sem abrir o arquivo. | [ ] |
| Qui 19 | 9–11h | **Setup de pé:** conferir a instalação e rodar os registros anotados no caderno (`just diag`, `just erro`, `just professor fechar`). O que travar: `just atrito`. | [ ] |
| Sex 20 | 6–11h | **[0.2 Linguagem matemática e lógica](https://github.com/AlanMateus17/mapa-de-estudo/blob/main/assuntos/01-matematica/linguagem-matematica-e-logica.md), blocos 1 a 6**, com o VHSlins Cap. 1 no papel. Confira no livro a precedência de → e ↔. | [ ] |
| Sáb 21 | 6–10h | **0.2, blocos 7 a 10** (N3, N4 em TypeScript, resumo e cartões). | [ ] |
| Sáb 21 | 10–12h | **Fechar o 0.2:** `just ficha 0.2`. Depois `just colher 0.1` e `just colher 0.2`: os planos de aula vão para o `ensino-ti` e os exercícios para o Anki. | [ ] |
| Dom 22 | — | **Folga.** Só 30 min de Anki. | [ ] |
| Seg 23 | 6–8h | **Revisão espaçada:** exercícios N3 do 0.1 e do 0.2 de cabeça, com o material fechado; o que errar vai para `just erro`. | [ ] |
| Seg 23 | 20–22h | **Aulas:** revisar os planos de aula gerados no `ensino-ti` e fazer o commit. | [ ] |

## 🗓️ Semana 2 — 24 a 30/11
- [ ] **Ter 24, 6–7h:** 0.1 bloco 7, Akita `b-aprender` (#76 e #65) + nota de 5 frases
- [ ] Os próximos assuntos da Etapa 0 (0.3 conjuntos, 0.4 e 0.5 como o computador funciona, 0.6 lógica de programação) entram aqui **quando estiverem escritos e conferidos**, um de cada vez.

**Semanas 3 e 4 (01–13/12):** criptografia essencial, Git (aí sim nasce o repo `logica-ts`), segredos, backup, Docker, `just`, Núcleo, segurança de agentes; e TypeScript no terminal com testes. O detalhe dia a dia entra aqui quando a Semana 2 fechar.

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
