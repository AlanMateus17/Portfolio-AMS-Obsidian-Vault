---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-copilot — Documento de Projeto Final

Segue a estrutura fixa do [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md). Este é o serviço mais em estágio de ideia de todo o portfólio — o documento reflete isso com mais pendências que os demais, de propósito, em vez de fingir certeza que não existe.

---

## 1. Visão do produto

Assistente de IA embutido em AM Kaixara, Loja Virtual e AM Rendara, usando **function-calling contra dado ao vivo do sistema**, não RAG (busca em documento estático) — decisão já tomada anteriormente e que vale manter como princípio central.

**Diferencial de inovação:** a maioria dos "assistentes de IA" embutidos em SaaS de varejo/finanças hoje é RAG sobre manual de ajuda — responde pergunta sobre "como usar o sistema", não sobre o dado real do negócio. Aqui a proposta é o oposto: o assistente consulta o dado ao vivo (estoque, venda, carteira) e responde/age sobre ele — "quanto vendi essa semana comparado à anterior", "sugere um rebalanceamento", em vez de só "como faço para cadastrar produto".

---

## 2. Funcionalidades completas (estado final — ainda o mais especulativo do portfólio)

### 2.1 No AM Kaixara
- Consulta em linguagem natural sobre venda, estoque, faturamento ("como estão minhas vendas essa semana")
- Ação assistida (ex: sugerir reposição de estoque, com confirmação do usuário antes de executar)

### 2.2 Na Loja Virtual
- Assistente de compra para o cliente final (ex: recomendação de produto), papel diferente do assistente administrativo do AM Kaixara

### 2.3 No AM Rendara
- Explicação de sugestão de rebalanceamento em linguagem natural, apoiando (não substituindo) o motor determinístico já existente

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Responder pergunta em linguagem natural consultando dado ao vivo via function-calling, nunca RAG sobre documento estático | É o diferencial central do produto — sem isso, é só mais um chatbot de ajuda genérico |
| RF02 | Toda ação sugerida que altere dado (ex: ajustar estoque) exige confirmação explícita do usuário antes de executar | Impede que uma alucinação do modelo cause dano real ao negócio do cliente |
| RF03 | No AM Rendara, o copilot explica a sugestão do motor determinístico, nunca substitui o cálculo dele | Preserva a garantia de motor auditável e determinístico já estabelecida como requisito central do AM Rendara |
| RF04 | Escopo de dado consultável pelo copilot deve respeitar o mesmo isolamento por `tenant_id` do sistema hospedeiro | Um copilot mal implementado é o tipo de superfície que mais facilmente vaza dado entre tenant, se não for tratado com o mesmo rigor do resto do sistema |
| RF05 | Na Loja Virtual, o copilot atua como assistente de compra para o cliente final (recomendação de produto), papel distinto do assistente administrativo do AM Kaixara/AM Rendara | Sem essa distinção formal, o comportamento esperado do copilot fica ambíguo entre "ajudar o lojista" e "ajudar o comprador" |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Usuário administrativo (AM Kaixara, AM Rendara)
- **Uso:** chat/consulta embutido na interface já existente do sistema hospedeiro
- **Não tem cadastro próprio** — herda a sessão autenticada do sistema hospedeiro

### 4.2 Cliente final (Loja Virtual)
- **Uso:** assistente de compra, papel de vendedor assistido
- Diferente do 4.1 — aqui o "usuário" é o consumidor, não o dono do negócio

### 4.3 Você (avaliação de qualidade/custo)
- **Lacuna:** não existe hoje nenhum processo definido de avaliação de qualidade de resposta nem de controle de custo de API de modelo de linguagem — ambos são riscos reais de um produto de IA em produção, e nenhum dos dois foi endereçado ainda

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-copilot | Para que serve |
|---|---|---|
| RNFT07 (BOLA) | Function-calling não pode consultar dado fora do escopo do tenant autenticado | Mesmo risco de vazamento entre tenant, agravado pela superfície nova que é o modelo de linguagem |
| Confirmação de ação (RF02, elevado a RNF) | Nenhuma ação que altere dado deve executar sem confirmação humana | Requisito de segurança tão importante que merece ser tratado como não-negociável, não só funcional |
| Controle de custo (próprio) | Deve existir limite configurável de uso por tenant, evitando custo de API de modelo de linguagem crescer sem controle | Sem isso, o custo do serviço pode crescer mais rápido que a receita que ele gera |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-copilot |
|---|---|
| Isolamento de dado | Maior risco novo do portfólio: prompt injection ou erro de escopo pode vazar dado entre tenant de um jeito que nenhum outro sistema do portfólio está exposto |
| Confirmação de ação | Toda ação que altera dado precisa de confirmação explícita — nunca autonomia total |
| Auditoria externa (RNFT-S06) | Deveria ter prioridade alta apesar do estágio inicial, precisamente porque é a superfície de risco mais nova e menos testada de todo o portfólio |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço embutido nos sistemas hospedeiros, sem instalador nem distribuição própria.

---

## 8. Deploy e CI/CD

Ainda não definido — depende da escolha de provedor de modelo de linguagem (API externa vs. modelo auto-hospedado), decisão que não foi tomada.

---

## 9. Modelo de receita

Não gera receita direta hoje — é um diferencial embutido nos sistemas que o hospedam, possivelmente cobrado como módulo adicional via `aura-licensing` no futuro, uma vez que o custo de API de modelo de linguagem for previsível o suficiente para precificar.

---

## 10. Status atual de desenvolvimento

**Apenas proposto.** Nenhum RF/RNF existia antes deste documento, nenhuma decisão de provedor de modelo foi tomada, nenhum protótipo existe. É o serviço em estágio mais inicial de todo o portfólio.

---

## 11. Pendências e decisões em aberto

1. **Provedor de modelo de linguagem** — API externa (Anthropic, OpenAI) vs. modelo auto-hospedado — decisão que afeta custo, latência e privacidade de dado.
2. **Processo de avaliação de qualidade de resposta** — inexistente hoje.
3. **Controle de custo de uso por tenant** — inexistente hoje, risco financeiro real se não resolvido antes do lançamento.
4. **Precificação como módulo do `aura-licensing`** — só faz sentido depois do custo unitário ficar previsível.
5. **Este documento deveria ser tratado como o de menor prioridade de implementação de todo o portfólio** — não porque a ideia seja ruim, mas porque tudo aqui depende de decisões (provedor de modelo, controle de custo) que ainda nem começaram a ser tomadas, diferente dos outros 5 serviços compartilhados.
