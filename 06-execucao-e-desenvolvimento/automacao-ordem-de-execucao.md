---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: completo
atualizado: 2026-10-02
---

# Automação — Ordem de Construção e Sequência de Execução
### Irmão do [automacao-o-que-e-por-que](automacao-o-que-e-por-que.md) — aquele é "o quê/como/por quê", este é "quando"

## 1. Ordem de construção — amarrada ao Passo do [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md)
| Quando (Passo) | O que construir | Por que aqui |
|---|---|---|
| Passo 1 | Nenhuma — exercícios como arquivo solto | Git só no Passo 2 |
| Passo 2 | Pre-commit (Gitleaks) + Dependabot | 1º repositório real |
| Passo 2 | Backup agendado do `C:\dev\` | já há conteúdo real |
| Passo 4-5 | Nenhuma nova | CI só com teste pra rodar |
| Passo 6 | CI (build+teste a cada push) | Passo já é sobre teste |
| Passo 6 | SAST (CodeQL) | já há código e CI |
| Passo 10 | CD + Uptime Kuma + log estruturado | "Produção real" |
| Passo 10 | Backup do banco + 1º teste de restauração | dado real de cliente |
| Passo 11 | Teste de carga (k6) | Passo é sobre performance |
| Passo 12 | IaC (Terraform) + CI/CD reutilizável + MkDocs | Passo extrai o que repete |
| Passo 13-14+ | Notificação, CODEOWNERS, DAST | mais de um sistema |
| 2-3 sistemas cobrando | Automação financeira (dry run) | há o que conciliar |
| Volume justificar | Bot de atendimento 1º nível | antes, manual é mais rápido |
| Nuvem paga ativa | Alerta de custo (FinOps) | há custo a monitorar |

**Regra de bolso:** entra no Passo onde o problema passa a existir — nunca "por precaução".

## 2. Sequência de execução (o que dispara quando)
| Momento | Dispara sozinho | Onde conferir |
|---|---|---|
| `git commit` | formata, Gitleaks, commitlint | terminal |
| GitHub recebe push/PR | build, testes, SAST | aba Actions |
| Merge na `main` | CD (imagem + deploy) | Actions + site/API |
| Produção contínua | Uptime Kuma + log | dashboard/log |
| Toda noite | backup `C:\dev\`+banco | log do script |
| 1x/semana | Dependabot | aba Pull Requests |
| 1x/mês (lembrete) | teste de restauração | você, isolado |
| Renovação | Certbot (SSL) | log/site abre |

"Está rodando agora?" Se não houve commit/push/merge recente e não é hora do agendamento, **nada está rodando**.

## 3. Rotina de checagem
Segunda (5min): backup rodou? PR do Dependabot? · Início de mês (15min): teste de restauração · Início de mês (5min): custo crescendo? · Após deploy: smoke test + Uptime verde · A cada 3 meses: limites de alerta ainda fazem sentido?

## 🔗 Relacionados
- [automacao-o-que-e-por-que](automacao-o-que-e-por-que.md) · [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md)
