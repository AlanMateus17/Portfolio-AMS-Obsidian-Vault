---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: completo
atualizado: 2026-10-02
---

# Automação — O Que É, Como Fazer e Por Quê

> **Consolida três documentos antigos** (`plano-automacao-completo`, `automacao-total-ambiente-trabalho`, `por-que-automatizar-riscos-e-testes`) em seis seções. A sequência (quando construir) fica em [[automacao-ordem-de-execucao]]. Os três originais foram para `99-arquivo/`.

> **Regra que governa tudo:** automatize o determinístico e verificável. **Nunca** 100% automático o que envolve dinheiro saindo, mensagem ao cliente sem revisão, ou decisão de arquitetura/negócio — o script prepara, você aprova.
> **Honesto:** automação não é grátis — cada ferramenta é mais uma que pode quebrar e dar falsa segurança.

Prioridade: 🟢 já, mesmo sozinho · 🟡 só com produção real · 🔴 só time grande.

## A. Catálogo — adotar vs. construir
**A.1 Adotar (grátis):** `dotnet format` · Gitleaks · GitHub Actions · Dependabot · CodeQL (SAST) · GitHub Actions+script (CD) · Terraform (IaC) · Uptime Kuma (monitor) · Grafana Loki (log) · Swagger (doc API) · MkDocs (site doc) · semantic-release (changelog) · k6 (carga) · Claude Code Action (revisão PR) · GitHub Projects (≈Jira) · GitHub Container Registry · RabbitMQ (≈Kafka). A coluna "enterprise" (Jenkins, Snyk, Datadog, Splunk, PagerDuty, HashiCorp Vault, Kafka...) é só pra reconhecer o nome.
**A.2 Construir (é seu):** `aura-status` — console C#, agrega Git de todos os repos, pasta órfã, backup, catálogo, PRs do Dependabot, timer do Protocolo, Anki, zip-gabaritos. (arquitetura em [[painel-central-arquitetura-todas-fases]])
**A.3 Setup conectado:** backup no Task Scheduler, `aura-status` semanal em log, Certbot semanal, Uptime Kuma via Docker `--restart=always`.

## B. Como fazer (comando real)
- **Commit 🟢:** `dotnet format`; `gitleaks protect --staged -v`; `pre-commit install`; commitlint.
- **CI 🟢:** `.github/workflows/ci.yml` (checkout → setup-dotnet 10 → restore → build → test). Dependabot: Settings→Security, 2 cliques.
- **CD 🟡:** `.github/workflows/deploy.yml` com `appleboy/ssh-action` → `git pull && docker compose up -d --build`; migração `dotnet ef database update`.
- **IaC 🟡:** Terraform (`init` → `plan` SEMPRE antes → `apply`); `certbot renew --quiet`.
- **Observabilidade 🟡:** Uptime Kuma via Docker; `_logger.LogInformation("Venda {VendaId} {Valor}", ...)`.
- **Segurança 🟡:** CodeQL no CI; `trivy image`; `zap-baseline` (DAST); anonimizar CPF no ambiente de teste (LGPD).
- **Doc 🟢:** `AddSwaggerGen()`; `mkdocs gh-deploy`; `npx semantic-release`.
- **Ambiente 🟢:** Dev Container / `setup.ps1` (winget + dotnet restore).
- **Backup 🟢:** `backup.ps1` (Compress-Archive + robocopy pro NAS) agendado + teste de restauração mensal.
- **Negócio/IA 🟡🔴:** nota fiscal via API (dry run), conciliação, notificação Discord, `actions/stale`, CODEOWNERS, k6, FinOps, `claude-code-action` (revisão, nunca decisão final).

## C. Por quê / risco (resumo)
Você é 1 pessoa com 23 sistemas e TDAH → o risco é **esquecer a tarefa chata**; automação é a prótese pra isso. Riscos por categoria: pipeline (flaky, precisa rollback testado) · IaC (`apply` sem `plan` apaga produção) · observabilidade (fadiga de alerta) · segurança (falso positivo; rotacionar segredo) · doc (técnica demais → ficha dupla continua) · **backup não testado não é backup** · financeiro (dinheiro real → dry run) · bot (caminho pra humano) · IA (vaza segredo ~2x, GitGuardian mar/2026; 2ª opinião, não decisão).

## D. Testes (pirâmide)
Unitário (xUnit) · Integração (Testcontainers) · Contrato (Pact — crítico com 22 sistemas) · E2E (Playwright) · Smoke · Regressão · Carga (k6) · Segurança (CodeQL/ZAP) · Acessibilidade (Lighthouse) · Exploratório manual · **Restauração de backup (1x/mês, o mais esquecido)**.

## E. Onde usar IA
✅ esqueleto de teste, 1ª revisão PR, explicar erro, msg de commit, triagem de log, doc técnica. 🟡 resposta a cliente (com escape), correção de vuln, anomalia financeira (só alerta). 🔴 código de auth, LGPD, mover dinheiro, aprovar o próprio PR. Régua: perto de dinheiro/dado/jurídico, menos automático.

## F. Práticas indispensáveis
1. Nunca commit sem Gitleaks · 2. Nunca `apply` sem `plan` · 3. Nunca deploy sem rollback testado · 4. Nunca backup sem teste mensal · 5. Nunca financeiro 100% sem revisão · 6. Nunca IA aprovando o próprio código · 7. Sempre log estruturado · 8. Sempre limite de profundidade GraphQL (AM Taskoro).
**Começar agora (🟢):** pre-commit (feito) · Dependabot · CI básico · backup do `C:\dev\` · setup em um comando.

## 🔗 Relacionados
- [[automacao-ordem-de-execucao]] · [[painel-central-arquitetura-todas-fases]] · [[mapa-automacao-por-contexto-profissional]] · [[seguranca-e-ferramentas-todas-as-frentes]] · [[infraestrutura-fisica-10-anos]] · [[setup-ambiente-trabalho-final]]
