# Operação 24 horas: o que roda onde

[← Operação do grupo](README.md)

**A verdade primeiro:** o que roda no seu notebook para quando ele desliga ou dorme. Para trabalhar 24 horas sem pagar, o setup usa três lugares.

| Onde | Custo | Fica ligado? | O que roda |
|---|---|---|---|
| **Seu notebook** (Windows + WSL) | Já tem | Só quando ligado | Estudo, desenvolvimento, modelos locais, ActivityWatch, rotinas do cron |
| **GitHub Actions** | Grátis (cota mensal) | Sim, por horário | Vigia semanal (sites dos clientes e segredos), CI de todos os repositórios, Dependabot |
| **VM da Oracle (Always Free)** | Grátis (2 núcleos, 12 GB desde jun/2026) | 24 horas | n8n, bot do Telegram, Uptime Kuma, gateway de modelos, avisos |
| **Tarefas agendadas do Claude** | Gastam o limite do Claude | Por horário | No máximo 2, que paguem o próprio gasto (ex.: analista semanal) |

## O que o setup faz sozinho, o tempo todo

| Frente | Automático | Você |
|---|---|---|
| **Segurança** | CI com segredos e vulnerabilidades, vigia semanal, Dependabot, monitoramento | Corrigir o que for apontado |
| **Clientes** | Prospector monta a lista e o rascunho | Aprovar cada contato (nada de disparo em massa) |
| **Renda** | Checkout, entrega, cobrança recorrente, funil de e-mails, publicação agendada com aprovação | Criar o produto uma vez, aprovar posts |
| **Otimização** | Lucro por ferramenta e por renda, retorno por hora, evals dos agentes | Cortar o que der prejuízo por 2 meses |
| **"Treino"** | Notas reindexadas e evals mensais | Fine-tuning só por trimestre e com ganho medido |

## Limites honestos

- "Treinar o tempo todo" não melhora um modelo e gasta dinheiro: o que melhora é dado novo + avaliação. Por isso é mensal.
- Prospecção agressiva automática (mensagens em massa) bloqueia o seu número e fere a LGPD. Agressivo aqui é **volume com aprovação**: lista toda semana, contato um a um.
- "Procurar buracos" só nos sites e sistemas seus ou de clientes com contrato. Em sistema de terceiros sem autorização é crime.
