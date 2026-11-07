# 0008 · Trocas de ferramenta principal e o papel de cada reserva

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O Alan pediu todas as ferramentas do contexto mestre no setup, configuradas, e que cada ferramenta que já existia fosse comparada com a sugestão nova: se a nova for melhor, troca. O setup já usa o modelo principal, reserva e portão por tarefa (docs/recursos.md).

## Trocas (a nova vira principal)

| Função | Antes | Agora (principal) | Reserva | Por quê |
|---|---|---|---|---|
| Runtimes | fnm (Node) | mise (Node, Go, Rust e as CLIs) | fnm | Um gerenciador para tudo; com várias linguagens, o fnm não cobre |
| Multiplexador | tmux | Zellij | tmux (servidores) | Atalhos visíveis na tela, layouts e sessões que voltam |
| Dotfiles | repositório com cópia manual | chezmoi | — | Modelos por máquina e segredos lidos do KeePassXC |
| Erros dos sistemas | Sentry (SaaS) | GlitchTip (próprio) | Sentry | Mesmo SDK, dado seu, sem cota |
| Logs, traces e métricas dos apps | Loki + Tempo + Prometheus | SigNoz | Loki + Tempo | Uma tela só, nativo de OpenTelemetry; o Grafana fica para o painel de lucro |
| Sites de conteúdo | Jekyll | Astro | Hostinger IA (clientes) | Rápido, estático, componentes; o site pessoal migra para ele |
| Formulário de qualificação | perguntas do Cal.com | HeyForm | Cal.com | Formulário de conversa com lógica, antes de abrir a agenda |
| Pesquisas e NPS | manual | Formbricks | — | Pesquisa no produto e por link, com histórico |
| Contabilidade em partidas dobradas | — | Beancount + Fava | hledger | Texto puro versionável, com balanço e DRE |
| Rentabilidade da carteira | — | Portfolio Performance | Ghostfolio (painel) | TTWROR e IRR; o investimentos.py segue escolhendo os ativos |

## Mantidas (a atual continua melhor) e o papel da sugestão

| Função | Principal (mantida) | A sugestão entra como | Por quê |
|---|---|---|---|
| Deploy dos sistemas AM | Kamal | Coolify (apps de um clique em VPS de cliente), Dokploy (reserva leve) | Kamal é código no repositório e rollback por versão |
| Containers | Docker Desktop + WSL | Podman (rootless no lab de alvo e em VPS) | A integração com o WSL já funciona |
| Rede privada | Tailscale | Headscale (redes de clientes e reserva) | Grátis, sem servidor para manter |
| Hospedagem de código | GitHub | Forgejo (espelho com LFS), Soft Serve (servidor da casa) | Actions, Copilot e Education ficam no GitHub |
| Agente de código | Claude Code | Aider com Ollama (nível R$ 0), llm (pipes no terminal) | O Claude Code é o mais capaz; o Aider custa zero |
| Teste de API | Bruno | posting (no terminal e por SSH) | Coleções em arquivo para cliente |
| SQL | DBeaver | harlequin (no terminal, DuckDB e Postgres) | Janela para o dia a dia |
| Carga | k6 | vegeta (taxa constante, achar o teto) | Cenários e limites no k6 |
| Diagramas na documentação | Mermaid | D2 (arquitetura de sistema e de cliente) | O GitHub desenha o Mermaid sozinho |
| Tarefas | GitHub Projects | Plane (projetos de cliente e dos negócios fora do código) | Ligado aos repositórios |
| Documentação | MkDocs | BookStack (manuais dos clientes) | Dev escreve em Markdown no repositório |
| Notas | Obsidian | Logseq (diário e runbooks em tópicos, mesma pasta) | O vault já existe com Git |
| Analytics | Umami | Plausible (reserva, painéis de cliente) | Mais leve na VM |
| E-mail transacional | Resend | Plunk (próprio, sobre o SES, quando o volume pedir) | Plano grátis basta agora |
| Engenharia reversa | Ghidra | radare2 (triagem rápida e scripts) | Descompilador melhor |
| Finanças pessoais | financeiro.py + Caixa da Casa | Actual (envelopes), Firefly III (reserva) | As suas regras já estão no código |
| ERP | sistemas AM | ERPNext (negócios físicos até o Aura cobrir; referência de mercado), Akaunting (CNPJ) | O Aura é o produto |
| Terminal no Windows | Windows Terminal | Ghostty (no Arch nativo) | O Ghostty não tem versão para Windows |

## Consequências

- Nenhuma ferramenta do contexto mestre ficou de fora; cada uma tem função, passo e data.
- Reserva não roda o tempo todo: sobe quando a principal falhar ou quando o papel dela aparecer.
- Itens pagos (VM na AWS ou Azure, VPS do Forgejo, SES do Plunk, SLU) ficam prontos e ligam quando uma renda pagar.
