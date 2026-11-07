# Soberania: serviços próprios

`compose.yaml` com um perfil por serviço; nada sobe sem o `--profile`. Tudo em 127.0.0.1.

| Perfil | Serviço | Papel no setup |
|---|---|---|
| forgejo | Forgejo | Espelho de todos os repositórios do GitHub (com Git LFS) |
| soft-serve | Soft Serve | Git por SSH no servidor da casa (firmware, placas) |
| headscale | Headscale | Reserva do Tailscale e redes de clientes |
| glitchtip | GlitchTip | Erros dos sistemas (principal; Sentry SaaS é a reserva) |
| bookstack | BookStack | Manuais dos clientes |
| actual | Actual Budget | Orçamento pessoal por envelopes |
| ghostfolio | Ghostfolio | Painel do patrimônio |
| firefly | Firefly III | Fluxo de caixa com importação de extrato (reserva) |
| akaunting | Akaunting | Contabilidade do CNPJ, quando abrir |

Os grandes têm instalador oficial e não entram aqui: SigNoz, Plane, Plausible CE, ERPNext (frappe_docker), Formbricks, HeyForm, Plunk, Coolify e Dokploy. Os comandos estão nos passos da fase Soberania do roteiro.
