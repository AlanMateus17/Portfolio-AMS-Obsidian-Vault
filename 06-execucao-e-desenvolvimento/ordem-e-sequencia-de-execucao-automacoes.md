---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: novo
---

# Ordem de Construção e Sequência de Execução das Automações
### O terceiro documento do trio — os outros dois explicam "como" e "por quê", este explica "quando"

> Duas perguntas diferentes, respondidas juntas aqui: **(1) em que ordem eu construo cada automação** (não dá pra automatizar teste antes de ter código, nem CD antes de ter algo pra rodar em produção) e **(2) durante o dia a dia, quando cada automação já construída realmente dispara**, e onde você olha pra confirmar que rodou certo.

---

## 1. Ordem de construção — amarrada ao Passo real do [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]]

Nada aqui é uma linha do tempo nova e separada — é a mesma sequência de sempre, com a automação encaixada no ponto exato onde ela passa a fazer sentido (não antes, por pré-requisito real; não depois, por já ter o que a justifica).

| Quando (Passo) | O que construir | Por que exatamente aqui, não antes |
|---|---|---|
| **Passo 1** — Lógica + Matemática + Inglês | Nenhuma automação ainda — os 3 exercícios de lógica (carrinho com desconto, escada de inadimplência, ARCA) ficam como arquivo solto, sem Git | Git só é ensinado formalmente no Passo 2 — forçar Git antes disso seria pedir pra usar uma ferramenta que ainda não foi estudada. Os arquivos deste Passo entram no repositório retroativamente, junto com o primeiro commit do Passo 2 |
| **Passo 2** — Git, SQL, Docker | Pre-commit hook (Gitleaks) + Dependabot ligado no repositório | É o primeiro momento em que existe um repositório Git de verdade — ativar os dois agora custa 10 minutos e já protege tudo que vem depois, **incluindo os arquivos do Passo 1 que entram junto no primeiro commit** |
| **Passo 2**, mesmo momento | Script de backup agendado do `C:\dev\` | `C:\dev\` já existe com conteúdo real (os exercícios do Passo 1 inclusive) a partir daqui — não faz sentido esperar |
| **Passo 4-5** — API/Auth, EF Core | Nenhuma automação nova ainda — só escrevendo o primeiro código de verdade | CI só faz sentido quando existe teste pra rodar (próximo item) |
| **Passo 6** — Teste como disciplina | CI completo: build + teste automático a cada push | O próprio Passo já é sobre pirâmide de teste — é o encaixe natural, não um adendo |
| **Passo 6**, mesmo momento | SAST (CodeQL) no pipeline | Já tem código e já tem CI rodando — adicionar o scanner de segurança é o próximo passo natural, não uma etapa separada |
| **Passo 10** — Produção real | CD (deploy automático) + Uptime Kuma + log estruturado | É literalmente o Passo "Produção real" — antes disso não existe onde fazer deploy nem o que monitorar |
| **Passo 10**, mesmo momento | Backup do banco de produção + primeiro teste de restauração | Existe dado real de cliente a partir daqui pela primeira vez |
| **Passo 11** — Performance | Teste de carga (k6) | O próprio Passo já é sobre medir e otimizar — mesmo encaixe do CI no Passo 6 |
| **Passo 12** — Extração da plataforma | Infraestrutura como código (Terraform) + pipeline de CI/CD reutilizável + MkDocs publicado | É o Passo que já existe pra extrair tudo que se repete entre sistemas — a automação reutilizável nasce junto, não depois |
| **Passo 13-14+** — Segundo/terceiro sistema em diante | Notificação automática (Discord/Slack), CODEOWNERS, DAST | Só faz sentido com mais de um sistema rodando, tempo suficiente decorrido pra Pull Request "esquecido" virar problema real |
| **Quando 2-3 sistemas cobrarem de verdade** | Automação financeira (nota fiscal, conciliação) — sempre em modo "dry run" no início | Só existe o que conciliar quando existe cobrança real acontecendo |
| **Quando o volume de atendimento justificar** | Bot de atendimento de primeiro nível | Antes disso, responder manualmente é mais rápido que calibrar um bot |
| **Só quando tiver conta de nuvem paga ativa** | Alerta de custo (FinOps) | Não existe custo de nuvem pra monitorar antes disso |

**Regra de bolso pra qualquer automação nova que não está nesta tabela:** ela entra no Passo onde o problema que ela resolve passa a existir de verdade — nunca antes, "por precaução".

---

## 2. Sequência de execução — o que dispara quando, durante o trabalho real

Isso é sobre o dia a dia **depois** que cada automação da tabela acima já foi construída — a pergunta "está rodando agora, ou não?".

| Momento | O que acontece sozinho | Onde você confere se funcionou |
|---|---|---|
| **Enquanto você escreve código** | Nada automático dispara ainda (a não ser um linter do próprio editor, se configurado) | — |
| **`git commit`** | Pre-commit hook roda: formata código, Gitleaks escaneia por segredo, commitlint valida a mensagem | Direto no terminal — se algo bloquear, o commit não acontece e a mensagem de erro aparece na hora |
| **`git push`** | Nada dispara localmente — o push só envia; o gatilho real é o GitHub recebendo | — |
| **GitHub recebe o push / abre um Pull Request** | GitHub Actions dispara: build, todos os testes automáticos, SAST (CodeQL) | Aba **Actions** do repositório — ✅ ou ❌ ao lado do commit, com o log completo se falhar |
| **Merge na branch `main`** | CD dispara: build da imagem Docker, deploy pro servidor | Aba Actions de novo (job separado, geralmente chamado `deploy`) + acessar o site/API pra confirmar que a versão nova está no ar |
| **Sistema rodando em produção — contínuo, o tempo todo** | Uptime Kuma checando se está no ar a cada poucos minutos; cada requisição gera uma linha de log estruturado | Dashboard do Uptime Kuma (fica aberto num navegador ou celular); arquivo/serviço de log quando precisar investigar algo específico |
| **Toda noite, agendado** | Backup do `C:\dev\` e do banco de produção | Log do próprio script de backup (linha "sucesso" ou "erro" com data) |
| **Uma vez por semana, agendado** | Dependabot escaneia dependência vulnerável | Aba **Pull Requests** do repositório — ele mesmo abre o PR de correção, sozinho |
| **Uma vez por mês, agendado por você (não é automático sozinho — é um lembrete pra você rodar)** | Teste de restauração do backup mais recente | Você mesmo confirma se o backup restaurado abre e tem dado íntegro |
| **A cada renovação de certificado necessária** | Certbot renova o SSL sozinho | Log do Certbot, ou só confirmando que o site continua abrindo sem aviso de certificado expirado |

**A pergunta "está rodando agora, ou não?" tem uma resposta simples, sempre:** se você não fez `commit`/`push`/`merge` nos últimos minutos, e não é hora do agendamento noturno/semanal, **nada está rodando** — automação não é um processo constante consumindo atenção, é um conjunto de gatilhos que só disparam em momentos específicos e previsíveis.

---

## 3. Rotina periódica de checagem — pra você nunca perder de vista o que está rodando

Sem isso, "automação" vira "coisa que eu configurei uma vez e não sei mais se está funcionando". Uma rotina curta, fixa:

| Frequência | O que checar | Onde |
|---|---|---|
| **Toda segunda-feira** (5 min) | Log do backup da semana rodou todos os dias? Algum PR do Dependabot esperando aprovação? | Log do script de backup + aba Pull Requests |
| **Todo início de mês** (15 min) | Teste de restauração de backup — restaurou e abriu de verdade? | Você mesmo, restaurando manualmente num lugar isolado |
| **Todo início de mês** (5 min) | Algum custo de ferramenta/nuvem crescendo sem explicação? | Fatura do provedor |
| **Depois de qualquer deploy grande** (imediato) | Smoke test — as rotas principais ainda respondem? Uptime Kuma continua verde? | Dashboard do Uptime Kuma |
| **A cada 3 meses** | Revisar se os limites de alerta ainda fazem sentido (muito alerta = fadiga; pouco = risco de não avisar) | Configuração do Uptime Kuma/observabilidade |

Essa tabela pode virar um checklist recorrente dentro do seu `00-catalogo-progresso` ou de um novo item semanal fixo — não precisa decorar, só consultar toda segunda.

---

## 🔗 Documentos relacionados
- [[automacao-total-ambiente-trabalho]] — o "como" de cada automação desta ordem
- [[por-que-automatizar-riscos-e-testes]] — o "por quê" e os riscos de cada uma
- [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] — a sequência de Passos que esta ordem de construção segue
