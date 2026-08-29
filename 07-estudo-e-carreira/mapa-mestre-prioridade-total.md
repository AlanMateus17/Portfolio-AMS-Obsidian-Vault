---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Mapa Mestre de Prioridade Total
### Tudo que você vai estudar — dev, matemática, idiomas, 42, roadmap.sh, Akita, pentest, perfil sênior — numa única sequência, sem gap

> ℹ️ **Para o dia a dia, use [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]]** — este documento continua aqui como referência de detalhe, mas não precisa mais ser aberto pra saber "o que vem agora".


---

## Como ler este mapa

Cada linha é um bloco de conteúdo, com: **prioridade** (P0 = bloqueia tudo o resto / P1 = trilha longa paralela / P2 = hábito contínuo, sem prazo), **quando começa**, e **link pro documento de detalhe**. Você nunca precisa adivinhar "o que vem agora" — é só seguir a ordem de prioridade de cima pra baixo, checando o que já está em andamento.

---

## P0 — Sequência principal, bloqueia todo o resto (nunca pule)

| Ordem | Bloco | Quando | Detalhe completo |
|---|---|---|---|
| 1 | Passo 1-8: Lógica → C# → API → EF Core → Teste → Frontend → Arquitetura | Agora, sequencial | [[passo-a-passo-mestre-desde-o-inicio]] |
| 2 | Matemática — Parte I e II do livro (Lógica, Teoria dos Números) | Junto aos Passos 1-5 | [[matematica-e-desenvolvimento-integrado]] |
| 3 | Inglês — Fase A/B (nivelamento + troca de fonte técnica) | Desde o Passo 1 | [[ingles-espanhol-integrado]], [[metodo-correto-estudo-idiomas]] |
| 4 | Passo 9-14: Deploy → Performance → Extração de plataforma → Aura Delivery e demais sistemas | Depois do Passo 8 | [[passo-a-passo-mestre-desde-o-inicio]] |

**Critério de avanço:** só passa pro próximo item de P0 quando o critério de saída do Passo atual (já definido em cada Passo) estiver cumprido.

---

## P1 — Trilhas longas, rodam em paralelo a partir do ponto certo (nunca bloqueiam P0, nunca são esquecidas)

| Trilha | Começa em | Duração | Detalhe completo |
|---|---|---|---|
| **Trilha 42** (29 entregáveis, C#→C/C++) | Depois do Passo 8 | ~10-12 meses | [[trilha-42-circles-oficial-verificado]] |
| **Matemática avançada** (Partes III-VIII do livro: Estatística, Álgebra, Espaço, Complexos, Contagem) | Distribuída conforme a Trilha 42 e a Fase 7 exigirem (cada capítulo já tem gatilho próprio) | Contínua | [[matematica-e-desenvolvimento-integrado]] |
| **Python + OR-Tools** (Fase 7) | Quando o Aura Delivery chegar no bloco de roteirização | 5-7 semanas | [[passo-a-passo-mestre-desde-o-inicio]] |
| **Pentest/OSCP** (Fase 12) | Depois do Passo 8 (mesmo ponto de entrada da Trilha 42 — rodam em paralelo uma à outra) | 1-2 anos | [[roadmap-seguranca-ofensiva-completo]], [[recursos-links-seguranca-ofensiva]] |
| **Espanhol** | Depois do Inglês atingir B1-B2 (por volta do Passo 12) | Mais rápido que o inglês | [[ingles-espanhol-integrado]] |
| **Perfil sênior — itens técnicos** (System Design, Infrastructure as Code) | Depois da Fase 6D (Passo 12) | Pontual, não bloco longo | [[perfil-senior-completo-auditoria]] |
| **AgileFlow** (GraphQL híbrido via HotChocolate — dentro do .NET, 22º sistema) | Bloco 21B da sequência mestra, depois da Trilha 42 | 2-3 meses | [[agileflow-documento-projeto-final]], [[sequencia-mestra-completa-desde-o-inicio]] |

**Como as trilhas P1 convivem entre si:** Trilha 42 e Pentest começam no mesmo ponto (Passo 8) — não precisam ser simultâneas o tempo todo; alterne semana a semana ou bloco a bloco entre elas, conforme o que estiver mais engajante ou com prazo mais apertado no momento.

---

## P2 — Hábito contínuo, sem prazo, sem "fase que termina" (começam já e nunca param)

| Hábito | Frequência sugerida | Detalhe completo |
|---|---|---|
| **roadmap.sh — auditoria cruzada** | No início de cada bloco grande (Passo 3, 8, 8B, 10) — 2 minutos comparando contra o que já está planejado | [[integracao-42-roadmap-akita]] |
| **Fábio Akita** (blog/YouTube/podcast) | 1 vídeo ou post por semana | [[integracao-42-roadmap-akita]] |
| **Produção didática simultânea** (ficha dupla pra alunos) | A cada tópico novo de matemática+código | [[metodo-estudo-producao-didatica-simultanea]] |
| **Anki** (repetição espaçada — inglês, espanhol, vocabulário técnico) | Diário, 10-20 min | [[metodo-correto-estudo-idiomas]] |

---

## P3 — Só perto da hora de usar, nunca adiantado (evita sofisticação prematura)

| Item | Só ativa quando | Detalhe completo |
|---|---|---|
| Apresentação de portfólio, entrevista comportamental (STAR) | Perto de aplicar pra vaga de verdade | [[perfil-senior-completo-auditoria]], [[passo-a-passo-portfolio-vaga-junior]] |
| Certificação formal de inglês (TOEFL/IELTS) | Só se for aplicar pra vaga internacional formalmente | [[ingles-espanhol-integrado]] |
| GitHub — organização, ADR, GitHub Pages | A partir da Fase 6D | [[github-estrutura-profissional-autoridade]] |

---

## Visão consolidada — o que está rodando em cada grande fase do tempo

```
AGORA (Passos 1-8)
├── P0: Lógica → C# → API → EF Core → Teste → Frontend → Arquitetura
├── P0: Matemática Parte I-II
├── P0: Inglês Fase A/B
└── P2: roadmap.sh (auditoria cruzada), Anki

DEPOIS DO PASSO 8 (Passos 9-14 + trilhas longas)
├── P0: Deploy → Extração de plataforma → Aura Delivery → demais sistemas
├── P1: Trilha 42 (29 entregáveis) — 10-12 meses
├── P1: Pentest/OSCP — 1-2 anos
├── P1: Espanhol (após Inglês B1-B2)
├── P1: Python/OR-Tools (quando o Delivery pedir)
├── P1: Matemática avançada (Partes III-VIII, gatilho por capítulo)
├── P2: roadmap.sh (auditoria cruzada), Fábio Akita, fichas didáticas
└── P3: GitHub profissional, ADR

PERTO DE APLICAR PRA VAGA
└── P3: Apresentação de portfólio, STAR, certificação de idioma (se aplicável)
```

---

## A regra de ouro deste mapa, pra nunca ter gap

1. **P0 nunca para.** Se você não sabe o que fazer agora, é sempre o próximo item de P0.
2. **P1 nunca é esquecida, mas também nunca é urgente.** Reserve um bloco de tempo fixo por semana pra ela (ex: 2 das suas 9h), sem deixar o P0 comer esse espaço.
3. **P2 é hábito, não tarefa** — não tem "terminar", só "manter".
4. **P3 fica parada até o gatilho certo.** Não adianta, mesmo que pareça produtivo adiantar.

---

## 🔗 Documentos relacionados
- [[biblioteca-recursos-por-passo]] — recurso específico (doc oficial, guia, ferramenta) pra cada passo listado acima
- [[sequencia-mestra-completa-desde-o-inicio]] — a mesma prioridade, agora com os 29 projetos da 42 intercalados bloco a bloco com o desenvolvimento do portfólio
