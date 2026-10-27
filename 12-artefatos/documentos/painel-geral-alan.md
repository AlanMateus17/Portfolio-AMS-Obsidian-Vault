# Painel Geral — Alan

Sep 27, 2026 · @Alan Mateus

Índice único dos planos: estudos, produtos, sites e cursos. Não substitui os documentos detalhados; aponta para eles.

## Como usar este painel

Este é o seu ponto único de partida. Quando bater a sensação de "não sei o que estudar", abra aqui primeiro.

- **É um índice, não um plano novo.** Cada bloco resume e aponta para o documento detalhado. Os planos completos vivem nos outros documentos.
- **Sua aposta dos próximos 12 meses:** vaga de dev + renda própria (infoprodutos, freela, aulas). O resto é apoio para isso.
- **A regra que você mesmo definiu:** fazer tudo com qualidade, sem tocar muitas frentes ao mesmo tempo. Este painel existe para respeitar isso, e não para justificar abrir tudo de uma vez.
- **Regra de foco:** escolha UMA coisa por vez em cada bloco. O painel mostra o todo para você se orientar, não para executar o todo simultaneamente.

## A rotina de estudos

Você tem três trilhas técnicas que se entrelaçam, mais o plano-mestre (matemática, inglês, C/C++, etc.). A ordem entre as trilhas técnicas:

1. **Linux Fase 1 + Segurança S1** (juntas) — fundamentos + Bandit
2. **Redes** — faça cedo; destrava quase todo o resto
3. **Linux Fase 2** → abre **Segurança S2** (redes para pentest)
4. **Linux Fases 3–4** → abre **Segurança S3** (testar o próprio Aura) ← maior retorno imediato
5. **Linux Fases 5–6** → abre **Segurança S4** (escalada de privilégio)
6. **Linux Fase 8** → abre **Segurança S5** (laboratório Kali)
7. **Segurança S6** (Windows/AD) → **S7** (baixo nível) → **S8** (relatório e currículo)

**Regra de ouro:** nunca abrir uma fase de segurança sem o gate da trilha Linux correspondente fechado.

**Seu primeiro passo já definido (2–3 semanas):** Lógica de Programação (variável, condicional, laço, função, coleção) + Matemática cap. 1–2 + Inglês Fase A em paralelo. Pronto quando resolver os 3 exercícios de lógica sem travar. Some a isso o Bandit, que cabe nas horas livres.

**Seu tempo:** cerca de 4h/dia. Não distribua entre tudo; concentre em 1 ou 2 frentes por vez.

## Bloco 1 — Estudos

**Trilhas técnicas (criadas hoje, cada uma com fases e evidências):**

- **Trilha Linux/Arch Profissional** — base de tudo; 10 fases, do fundamento ao currículo, incluindo o projeto aura-status na Waybar
- **Trilha de Redes** — 6 fases; pré-requisito de segurança e homelab
- **Trilha de Cibersegurança e Pentest** — mentalidade dos atacantes + 8 fases com gates

**Plano-mestre (já existente, mais amplo):**

- Programação, C#/.NET, frontend, arquitetura, cloud, performance
- Matemática pelo livro do V.H.S. Lins, rumo a cálculo
- C/C++ pelo Common Core da École 42 (implementar na sua stack, depois portar)
- Inglês e espanhol (futuramente mandarim); leituras em inglês já compradas
- roadmap.sh e o canal/blog do Fabio Akita como referência
- Vault Obsidian com o plano detalhado

**Pendência:** reorganizar o repositório de estudos (você vai me passar o endereço depois).

## Bloco 2 — Produtos a vender

**Meta:** renda com infoprodutos, mirando entre R$ 10 mil/mês em vendas.

**Regra que vale para todos (a sua):** validar antes de construir. Lança a versão mínima barata primeiro (ex.: a planilha antes do sistema AM Rendara) e só constrói o grande se o pequeno vender.

**Três nichos, em paralelo:**

- TI / programação
- Matemática
- Finanças (conteúdo próprio a partir do que estudou, não revenda)

**Tipos de produto:** mini-cursos, frontends prontos, código-fonte, templates.

**Primeiro lançamento já escolhido:** mini-curso de **Lógica de Programação** — e ele nasce do seu próprio primeiro passo de estudo, fechando o ciclo estudar → ensinar → vender.

**Público:** alunos de ensino médio/técnico, concurseiros de TI, professores, iniciantes. Você já tem audiência.

**Canal:** Instagram monetizado para cursos, vídeos e o livro.

*(Detalhes no documento de infoprodutos.)*

## Bloco 3 — Sites a desenvolver

Quatro sites, que precisam conversar entre si sem repetir informação à toa e com navegação agradável:

- **Site pessoal / portfólio** — hoje em Jekyll (alanmateus17.github.io), migrando para a sua stack própria
- **Blog** — tech/dev, crítica de educação e sociedade; também recebe os write-ups das trilhas
- **Instituto AMS** — plataforma de cursos, inspirada no modelo do VHSlins
- **Institucional da Grupo AMtech Digital** — o 4º site, da sua empresa

**Ligação com o resto:** o portfólio é onde os projetos das trilhas (dotfiles, aura-status, homelab) viram vitrine; o Instituto AMS é onde os infoprodutos são vendidos; o blog alimenta os dois com conteúdo.

*(Detalhes no plano de presença web.)*

## Bloco 4 — Cursos e fontes

**Plataformas que você tem:** Alura, Rocketseat, Finclass, DIO, Udemy, cursos avulsos, e a faculdade de ADS. (Alura cobre \~80–85% da sua stack; lacunas em SignalR e PostGIS.)

**Trajetória acadêmica decidida:** concluir ADS e Licenciatura em Matemática → Ciência da Computação → duas pós, nesta ordem: **Cibersegurança primeiro, depois Arquitetura de Software**.

**Ordem das certificações:** CompTIA A+/Network+ → Security+ → CCNA (opcional) → eJPT → OSCP. Confira preço e formato atuais de cada uma antes.

**Outros aprendizados que você quer:** desenho, violão, idiomas. Estes ficam como lazer/longo prazo, fora da aposta principal dos 12 meses.

*(Detalhes no plano-mestre de estudos.)*

## O que fazer nesta semana

Nada do painel inteiro. Só isto, para sair da paralisia:

- [ ] **Estudo:** o Passo 1 já definido — Lógica de Programação + Matemática cap. 1–2 + Inglês Fase A
- [ ] **Hacker:** começar o OverTheWire Bandit (gratuito, sem instalar nada)
- [ ] **Produto:** esboçar o índice do mini-curso de Lógica de Programação — só o índice, aproveitando o que você estudar no Passo 1
- [ ] **Base:** criar o repositório `AlanMateus17/dotfiles` vazio, para receber as evidências das trilhas
- [ ] **Pendência:** me mandar o endereço do repositório de estudos para reorganizar

Uma coisa de cada vez. Quando terminar, volte ao painel e pegue o próximo recorte.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🧭 Plano Mestre — tudo em um só passo a passo](../../00-PLANO-MESTRE-PASSO-A-PASSO.md)
- [🎯 Plano Unificado AMS — O Mapa de Tudo](../../00-PLANO-UNIFICADO.md)
- [Plano Mestre — Frentes de Estudo, Negócio e Renda](../../01-planejamento-geral/plano-mestre-frentes-alan.md)
- [Status de Planejamento do Portfólio — o que já existe, o que falta, e o que se reaproveita de onde](../../01-planejamento-geral/status-planejamento-portfolio.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
