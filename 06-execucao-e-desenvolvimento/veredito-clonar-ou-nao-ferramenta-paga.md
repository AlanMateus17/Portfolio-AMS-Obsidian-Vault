---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: novo
---

# Ferramenta Paga: Clonar, Adotar Grátis, ou Já Está Coberto?
### Cada item do `plano-automacao-completo`, com veredito — pra você nunca ficar em dúvida se vale construir

> **A regra que decide cada linha:** só vale construir versão própria quando (1) não existe equivalente gratuito maduro **e** (2) o esforço de aprender construindo é realista sozinho, em paralelo com o resto do seu portfólio. Onde as duas condições não batem, a resposta é "adote o gratuito" ou "já está coberto" — nunca "construa do zero mesmo assim".

---

## ✅ Já coberto — você já está construindo isso, só não sabia que era "isso"

| Ferramenta paga | Por que já está resolvido |
|---|---|
| **Jira** (gestão de tarefa/sprint) | **É o AgileFlow.** Kanban + Scrum + RAD, exatamente o que Jira faz — você já tem o Documento de Projeto Final completo dele. Não precisa de um segundo projeto pra isso |
| **Confluence** (documentação de time) | MkDocs + GitHub Pages, já no seu plano — mesma função, publicado automaticamente |

---

## 🟢 Não clone — adote o gratuito, já é maduro e resolve

| Ferramenta paga | Equivalente gratuito que você já vai usar |
|---|---|
| Jenkins, CircleCI, Azure DevOps | GitHub Actions |
| Snyk, Mend | Dependabot |
| Checkmarx, Veracode | CodeQL |
| Docker Hub, AWS ECR | GitHub Container Registry |
| GitGuardian, TruffleHog | Gitleaks |
| Datadog, New Relic, Splunk | Uptime Kuma + Grafana Loki |
| Terraform Enterprise, Pulumi | Terraform (núcleo open source) |
| Spinnaker, ArgoCD, Harness | GitHub Actions + script de deploy |
| k6 Cloud, Gatling, JMeter (Enterprise) | k6 (núcleo open source) |

**Por que não vale clonar nenhuma dessas:** o valor delas está em **anos de refinamento de UI, integração e escala** — não em conceito novo pra aprender. Construir uma versão própria de "CI engine" ou "scanner de vulnerabilidade" ensina muito menos do que construir um sistema de negócio real (que é o que os 23 sistemas Aura já fazem). Aqui, aprender é usar bem, não reconstruir.

---

## 🟡 Vale construir uma versão de aprendizado — pequena, não "exatamente igual"

Só três itens passam nas duas condições (conceito valioso de aprender **e** escopo realista sozinho). Para os três: o objetivo é entender o mecanismo central, não replicar o produto inteiro.

### `aura-queue` — versão mínima de fila de mensagem (conceito do Kafka)

**O que ensina de verdade:** como sistema desacopla comunicação — um sistema publica um evento, outro consome, sem esperar resposta direta. É o mecanismo, não a escala de bilhões de mensagens/segundo do Kafka real.

**Escopo realista:** uma fila em memória (ou usando o Redis que você já tem no stack) com `Publish(evento)` e `Subscribe(tipo)` — sem replicação, sem partição, sem garantia de entrega distribuída. Isso já ensina o conceito e ainda resolve um problema real seu: quando dois sistemas Aura precisarem se avisar de algo (ex: AuraPOS avisa AuraWealth de uma venda) sem chamar a API um do outro diretamente.

**Onde entra:** depois que 2-3 sistemas já estiverem em produção e precisarem conversar entre si — não antes, não é urgente agora.

### `aura-secrets` — versão mínima de cofre de segredo (conceito do HashiCorp Vault)

**O que ensina de verdade:** por que segredo não deveria nunca ficar em arquivo de configuração, e como um serviço central de segredo funciona (pedido autenticado → segredo devolvido → nunca fica gravado em texto puro).

**Escopo realista:** uma API pequena, autenticada, que guarda segredo criptografado no banco e devolve só pra quem tem permissão — sem o sistema de política granular do Vault real, sem rotação automática distribuída.

**Onde entra:** quando o primeiro sistema for pra produção (Passo 10) — nesse momento, já existe segredo real de produção que precisa de um lugar melhor que variável de ambiente solta.

### `aura-oncall` — versão mínima de escalonamento de incidente (conceito do PagerDuty)

**O que ensina de verdade:** como alerta vira ação — não só "avisar", mas "se ninguém confirmar em X minutos, escala pra outra pessoa/canal".

**Escopo realista:** reaproveita o `aura-notifications` que você já tem — só adiciona a lógica de escalonamento por tempo. Não é projeto novo do zero, é extensão de um serviço que já existe no seu portfólio.

**Onde entra:** só relevante quando você tiver mais de uma pessoa respondendo incidente — sozinho, alerta direto pro seu celular (que o Uptime Kuma já faz) resolve sem precisar de escalonamento.

---

## Resumindo pra não ficar confuso

- **2 itens:** você já está construindo, nem precisa pensar de novo (Jira → AgileFlow, Confluence → MkDocs)
- **9 itens:** adote a versão gratuita, nunca construa a sua — o aprendizado não compensa o tempo
- **3 itens:** valem uma versão pequena, de aprendizado, no momento certo do seu portfólio (não agora) — e nem são projetos novos soltos, dois deles (`aura-queue`, `aura-secrets`) só nascem quando o problema real que resolvem já existir, e o terceiro é extensão de algo que você já tem

Isso significa **zero projeto novo agora** — os três só entram quando o Passo correspondente chegar, do jeito que todo o resto do portfólio já funciona.

---

## 🔗 Documentos relacionados
- [[plano-automacao-completo]] — a tabela original de onde cada item desta lista veio
- [[agileflow-documento-projeto-final]] — o "Jira" que você já está construindo
- [[ordem-e-sequencia-de-execucao-automacoes]] — onde os três itens 🟡 entrariam, quando chegar a hora
