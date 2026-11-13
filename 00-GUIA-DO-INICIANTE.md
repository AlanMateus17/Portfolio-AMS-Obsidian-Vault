---
tags: [ponto-de-entrada, guia, passo-a-passo, portfolio-ams]
tipo: guia
status: ativo
atualizado: 2026-10-26
---

# 🧭 Guia do Iniciante — Tudo o Que Você Vai Fazer, em Ordem e em Palavras Simples

> **Desde 06/11/2026 a porta do dia mudou** ([ADR 0013](11-setup-dev-setup/docs/adr/0013-um-vault-e-o-plano-mestre.md)). No Ubuntu do WSL:
> - **O que estudar hoje:** `cd ~/dev/dev-setup && just professor hoje` · método: [Professor](11-setup-dev-setup/docs/professor/metodo.md) · plano: [Eixo de 12 meses](11-setup-dev-setup/docs/plano-eixo.md) (software + finanças; AM Rendara no 2º trimestre)
> - **O que fazer hoje no setup:** `just agora` · roteiro completo na [pasta 11](11-setup-dev-setup/00-INDICE-DO-SETUP.md), espelho automático do dev-setup
> Este arquivo continua aqui como referência; nada foi apagado.


> **Para quem é este documento:** para você, lendo como se não soubesse nada do plano. Ele junta **estudo, setup, rendas, finanças, faculdades e certificações** num caminho só, com etapas numeradas. Cada palavra técnica tem explicação no [Glossário](00-GLOSSARIO.md).
>
> **Lista completa de itens:** este guia é o resumo. Todos os 391 itens (os 253 passos do setup, os 14 Passos de estudo, as trilhas, as rendas, as finanças, a faculdade e as certificações), cada um com código, “pronto quando” e ligações, estão no [Plano Mestre passo a passo](PLANO-UNICO-AMtech.md).
>
> **Como usar:** abra só este guia e o [Cartão "Você está aqui"](CARTAO-voce-esta-aqui.md). Faça a etapa atual, marque `[x]`, passe para a próxima. Os outros 100 arquivos do vault são **material de consulta**: você só abre quando uma etapa manda abrir.

---

## 1. O plano inteiro em 10 frases

1. **Onde você quer chegar:** ser **programador sênior** (Brasil e exterior), especialista em **IA** e em **software para empresas e finanças**, dono das próprias empresas e com **certificações para atuar no mercado de investimentos**.
2. **O dinheiro de hoje:** R$ 4.900/mês (escola + restaurante). Em 2027, se sair da escola, fica só o restaurante: R$ 2.200.
3. **A meta:** R$ 7.000 líquidos por mês, com renda feita em casa, até o fim de 2027.
4. **As rendas que vêm primeiro:** aulas particulares, manutenção de computador, sites com mensalidade e o mini-curso de Lógica. Depois, uma oferta nova por vez. Lista completa: [fontes de renda](01-planejamento-geral/fontes-de-renda-completas.md).
5. **O setup** (notebook, programas, automações) é a máquina que produz aula, conteúdo e venda: [setup completo](01-planejamento-geral/setup-completo-dev-setup.md); os documentos, fluxogramas e scripts estão na [pasta do setup](11-setup-dev-setup/00-INDICE-DO-SETUP.md).
6. **O estudo** segue 14 Passos, um de cada vez: [Sumário Único](PLANO-UNICO-AMtech.md). Tudo o que um sênior precisa saber está no [currículo](07-estudo-e-carreira/curriculo-dev-senior-completo.md).
7. **As faculdades:** Licenciatura em Matemática (agora), depois Economia e uma faculdade para IA, uma de cada vez: [formação](07-estudo-e-carreira/formacao-academica.md).
8. **As certificações de investimento:** CPA → CNPI → CGA → CFA, na ordem: [formação](07-estudo-e-carreira/formacao-academica.md).
9. **A regra de ouro:** **uma coisa em construção e uma em teste por vez.** O resto espera na fila, anotado.
10. **A regra de segurança:** **só sair da escola quando a renda extra passar de R$ 1.500/mês por 2 meses seguidos.**

---

## 2. A sua semana (base para tudo)

| Dia | Manhã | Tarde | Noite |
|---|---|---|---|
| Segunda | Estudo | Escola | Livre: prospecção e planejamento da semana |
| Terça | Escola | Escola | Restaurante (até 22h) |
| Quarta | Estudo | Escola | Restaurante |
| **Quinta** | **Bloco de construção** (setup, produto, conteúdo) | **Bloco de construção** | Restaurante |
| Sexta | Bloco de construção | Escola (a partir de 12h55) | Restaurante |
| Sábado | Estudo / aulas particulares | Restaurante (15h) | Restaurante |
| Domingo | Descanso / estudo leve | Restaurante (15h) | Restaurante |

- Acordar às 6h, cuidar dos cães todos os dias.
- **Tempo real de estudo hoje: cerca de 16 h por semana.** Não 4 h por dia. Em 2027, se sair da escola, as tardes de segunda a quarta ficam livres.
- Confira e ajuste no Caixa da Casa (aba Rotina).

---

## 3. O caminho, etapa por etapa

> As datas são uma proposta. Onde houver **gatilho**, a etapa espera o gatilho, não a data.

### Etapa 0 — Esta semana: arrumar a base
- [ ] **Setup — Diagnóstico:** rodar o `RODAR-DIAGNOSTICO.cmd` (só lê o notebook). *Pronto quando:* você tem o relatório `diagnostico.md`.
- [ ] **Setup — Senhas:** instalar o KeePassXC e começar a passar as contas para ele, 5 por semana. *Pronto quando:* e-mail principal e banco estão no cofre, com 2FA.
- [ ] **Finanças:** lançar no Caixa da Casa os gastos fixos (R$ 2.045) e as parcelas do cartão. *Pronto quando:* você sabe quanto sobra por mês.
- [ ] **Estudo:** abrir o [EPIC-01](07-estudo-e-carreira/EPIC-01-backlog-passo1-fundamentos.md) e fazer a primeira User Story do **Passo 1** (lógica + matemática).
- [ ] **Renda:** mandar mensagem para contatos e pais de alunos oferecendo **aulas particulares** e **manutenção de computador** (formatação, limpeza, troca por SSD). *Pronto quando:* a mensagem saiu.

### Etapa 1 — Novembro e dezembro de 2026: primeiros clientes
- [ ] **Setup:** fases 1 a 12 (Windows, Linux, GitHub, backup, acervo, automação, pipeline de conteúdo, contas e canais). Umas 5 h por semana, quinta e sexta.
- [ ] **Estudo:** terminar o **Passo 1** e o **Passo 2** (Git, SQL, Docker).
- [ ] **Renda:** primeiros **alunos** de aula particular; primeiro **cliente de manutenção**; montar **1 site modelo** (restaurante) para mostrar.
- [ ] **Finanças:** **zerar o cartão**; começar a reserva (3 meses de gastos fixos).
- [ ] **Conteúdo:** 3 posts por semana tirados das próprias aulas.
- *Pronto quando:* existe pelo menos 1 real de renda extra entrando e o cartão está sob controle.

### Etapa 2 — Janeiro e fevereiro de 2027: primeira venda de produto
- [ ] **Setup:** fases 13 a 15 (agenda com Pix, carnê-leão, Hotmart/Kiwify, painel de vendas).
- [ ] **Renda:** **fase 16 — lançar o mini-curso de Lógica** (gravar 5 aulas, página, isca grátis, pré-venda, primeira venda real).
- [ ] **Estudo:** **Passo 3** (C# + TypeScript) e começar o **bloco de Python** (1–2 h/semana).
- [ ] **Decisão:** sair da escola? **Só se** a renda extra passou de R$ 1.500/mês por 2 meses. Se não, adiar.
- *Pronto quando:* a primeira venda do curso aconteceu e foi lançada no carnê-leão.

### Etapa 3 — Março a junho de 2027: rendas crescendo, base técnica firme
- [ ] **Estudo:** **Passos 4, 5 e 6** (API, login, frontend com React/Next.js, banco de dados, testes).
- [ ] **Estudo — finanças leves:** começar **contabilidade** e **matemática financeira** (módulos F1 e F2).
- [ ] **Renda:** fase 21 — **uma oferta nova por vez**, pela pontuação: kit de aulas para professores → planilha do Caixa da Casa (testa o AM Rendara) → automação com IA para pequenos negócios.
- [ ] **Renda:** sites com manutenção mensal: meta de **3 a 4 clientes**.
- [ ] **Setup:** fases 17 e 18 (base dos sistemas AM, nuvem).
- *Pronto quando:* o Kaixara tem login e CRUD testados e existem pelo menos 2 rendas extras recorrentes.

### Etapa 4 — Julho a dezembro de 2027: bater os R$ 7 mil
- [ ] **Estudo:** **Passo 7** (Kaixara completo: pagamento, caixa contábil, agente offline) e **Passo 8** (arquitetura).
- [ ] **Carreira:** currículo, LinkedIn e GitHub em português e inglês; **primeiras candidaturas** a vagas de dev.
- [ ] **Renda:** **7 clientes de manutenção de site** (paga o restaurante); aulas: 8 alunos individuais + 2 turmas online.
- [ ] **Finanças:** reserva de 6 meses; investimentos pelo ARCA (próximo foco: ações por Barsi e Bazin).
- [ ] **Formação:** decidir a matrícula na **Economia** ou na **faculdade para IA**, pela regra do [documento de formação](07-estudo-e-carreira/formacao-academica.md).
- [ ] **Trilha paralela:** destrava depois do Passo 8 — começar **Finanças F4–F5** (valuation e mercado). Prova **CPA** no fim.
- *Pronto quando:* R$ 7.000 líquidos por mês, por 3 meses seguidos.

### Etapa 5 — 2028: virar sênior e empresa
- [ ] **Estudo:** **Passos 9 a 12** (tempo real, produção, performance, plataforma interna).
- [ ] **Trilha paralela:** **Dados e IA** (Python → machine learning → deep learning do zero).
- [ ] **Renda:** sistemas AM à venda; **CNPJ** quando a renda justificar; agentes do grupo.
- [ ] **Certificação:** **CNPI** (destrava consultoria e relatórios de análise).
- [ ] **Setup:** fases 22 a 30 (marketing pago, Linux nativo, IA nos sistemas, segunda nuvem, infraestrutura própria).
- *Pronto quando:* um sistema AM tem cliente pagante e você está empregado como dev ou com renda própria acima de R$ 7 mil.

### Etapa 6 — 2029 em diante: especialização e expansão
- [ ] **Estudo:** **Passos 13 e 14** (Rotara, Rendara, demais sistemas) + **fase sênior** (system design, entrevista em inglês).
- [ ] **Trilhas:** École 42 (C/C++), segurança ofensiva (eJPT → OSCP), IA treinada do zero (modelo pequeno + ajuste fino de 8B).
- [ ] **Certificações:** **CGA** (gestão de fundos) e **CFA** (exterior).
- [ ] **Empresas:** negócios de Barbacena, um por vez, **só passando nos 5 portões** (onda A tecnologia → B logística → C alimentação).
- [ ] **Horizonte longo:** Linux internals, sistema operacional próprio (AM-OS), distribuição própria (AM Linux).

---

## 4. O que fica sempre rodando (hábitos)

| Hábito | Quando |
|---|---|
| Anki (revisão) | Todo dia, 10–20 min |
| Protocolo de fim de bloco (reconstruir de cabeça, ensinar em 3 frases) | Ao terminar cada sessão de estudo |
| Estuda → ensina → grava | Cada tópico novo vira aula paga e conteúdo |
| Revisão do Caixa da Casa | Uma vez por mês |
| `aura-status` (painel de tudo) | Toda segunda-feira |
| 1 conteúdo do Fábio Akita | Uma vez por semana |

---

## 5. O que saiu do plano (para você não procurar)

Concurso PF/PRF · desenho · violão · pós-graduações (Cybersecurity e Arquitetura) · faculdade de Engenharia de Software (vira autodidata) · certificação CEA (extinta em jan/2026).

---

## 6. Como conferir se está tudo no plano

Use a página **Auditoria do Plano** (publicada junto com esta revisão). Ela lista cada coisa que você já planejou nas conversas, na memória e nos repositórios, e mostra em qual arquivo do vault ela está. O que aparecer como "falta" é o que ainda precisa entrar.

🔗 [Glossário](00-GLOSSARIO.md) · [Sumário Único](PLANO-UNICO-AMtech.md) · [Plano Unificado](PLANO-UNICO-AMtech.md) · [Fontes de renda](01-planejamento-geral/fontes-de-renda-completas.md) · [Setup](01-planejamento-geral/setup-completo-dev-setup.md)
