<!-- Escrito à mão. Como o "Contexto mestre unificado: setup e engenharia da empresa solo" entrou no dev-setup. -->

# Empresa solo: o contexto mestre dentro do setup

[← Índice da documentação](README.md)

O contexto mestre (soberania técnica, anti-Frankenstein, economia de tokens, as 88 ferramentas, `just architect` e `just triage`, Kamal, ARCA, ciclo comercial, estrutura legal, o cronograma de 14 dias e os 5 módulos complementares) está **inteiro** no setup. Cada ferramenta tem uma função, um passo no [roteiro](implantacao/roteiro.md) e uma data ou gatilho.

O que evita o Frankenstein não é deixar ferramenta de fora: é **cada função ter uma principal e, quando faz sentido, uma reserva** ([ADR 0008](adr/0008-trocas-de-ferramenta-principal.md)). A reserva não roda o tempo todo; ela sobe quando a principal falhar ou quando o papel dela aparecer. Nenhuma linguagem é proibida: a triagem escolhe a melhor para cada trabalho ([ADR 0007](adr/0007-poliglota-por-funcao.md)).

## Decisões

| Tema | Decisão |
|---|---|
| Linguagens | Aura em .NET 10 + Next.js; Astro para sites, SvelteKit + PocketBase para MVP, Go para CLIs, Rust para firmware, Python para dados e IA (ADR 0007) |
| Repositórios | Um por sistema AM, todos com `apps/web`, `apps/api`, `packages/core`, `packages/db` e `config/deploy.yml` |
| Deploy | Kamal; VM grátis da Oracle primeiro; EC2 (sa-east-1) ou Azure B2s (Brazil South) quando um cliente pagar (ADR 0005) |
| Segredos | Só no KeePassXC. age cifra arquivos que saem da máquina; sops cifra configuração de VM fora do Git |
| Itens pagos | Configurados e prontos; ligam quando uma renda pagar (VM paga, VPS de cliente, SES do Plunk, SLU) |
| Cronograma de 14 dias | Fase própria: Sprint de 14 dias, no recesso escolar de jan/2027 |

## Todas as ferramentas e o papel de cada uma

**P** = principal da função. **R** = reserva. **+** = papel próprio, ao lado da principal.

| Grupo | Ferramentas |
|---|---|
| Terminal e ergonomia | Windows Terminal (P no Windows) · Ghostty (P no Arch) · Zellij (P) · tmux (R, servidores) · Starship · Neovim com lazy.nvim e snacks.nvim |
| Runtimes e coreutils | mise (P: Node, Go, Rust e CLIs) · fnm (R) · uv (P de Python) · zoxide · eza · ripgrep · fd · fzf |
| Arquivos, Git e containers | yazi · lazygit · lazydocker · Docker Desktop (P) · Podman (+ rootless no lab e em VPS) |
| APIs, bancos e backends | Bruno (P) · posting (R, terminal e SSH) · DBeaver (P) · harlequin (R, terminal) · PocketBase (+ MVP) |
| Automação e métricas | just (porta única) · gum (`just menu`) · btop · hyperfine · bubbletea (CLIs em Go) |
| Dotfiles e segredos | chezmoi (P, lê o KeePassXC) · gitleaks · age e sops (arquivos cifrados) · KeePassXC (P de segredos) |
| Rede, túneis e backup | Tailscale (P) · Headscale (R e redes de clientes) · cloudflared (P de webhooks) · bore (+ TCP próprio) · restic · Litestream (+ SQLite do PocketBase) |
| Deploy | Kamal (P dos sistemas AM) · Coolify (+ VPS de cliente) · Dokploy (R do Coolify) |
| Custódia de código | GitHub (P) · Forgejo (espelho com LFS) · Soft Serve (servidor da casa) · Git LFS · gocryptfs (alvos cifrados) |
| Contexto de IA | Repomix (`just contexto-ia`) · tree-sitter (no Neovim, no Repomix e no repo map do Aider) |
| IA | Claude Code (P) · Aider + Ollama (nível R$ 0) · llm (pipes) · Ollama · ai-jail · ai-memory · MCP |
| Monetização e release | Hotmart e Kiwify (P no Brasil) · Polar (+ venda internacional) · Stripe CLI · GoReleaser · cargo-dist · act |
| Observabilidade | SigNoz (P dos apps) · Loki + Tempo (R) · Grafana (P do painel de lucro) · GlitchTip (P de erros) · Sentry (R) · Uptime Kuma · OpenTelemetry |
| Diagnóstico | strace · bpftrace · Wireshark/tshark · tcpdump · k6 (P) · vegeta (+ taxa constante) · Trivy |
| Projetos e desenho | GitHub Projects (P do código) · Plane (+ clientes e negócios) · Mermaid (P na documentação) · D2 (+ arquitetura) · Penpot |
| Engenharia reversa | Ghidra (P) · radare2 (+ triagem) · sala limpa (alvos → specs → src) |
| Hardware e firmware | KiCad · InteractiveHtmlBom · FreeCAD · tio · sigrok/PulseView · analisador lógico · probe-rs |
| Qualidade e testes | Zod (front) · Biome · Vitest · Playwright · xUnit |
| Finanças e ARCA | financeiro.py e Caixa da Casa (P) · Beancount + Fava (P do livro contábil) · hledger (R) · Portfolio Performance (P da rentabilidade) · Ghostfolio (painel) · Actual Budget (+ envelopes) · Firefly III (R) · ERPNext (+ negócios físicos) · Akaunting (+ CNPJ) |
| Comercial e atendimento | Invoice Ninja · Cal.com · HeyForm (P da qualificação) · Twenty · Chatwoot · Documenso · Formbricks (P do NPS) · BookStack (+ manuais) · Klaro! |
| Sites, e-mail e analytics | Astro (P dos sites de conteúdo) · SvelteKit (+ apps pequenos) · Next.js (P dos sistemas) · Resend (P) · Plunk (R próprio) · React Email · Umami (P) · Plausible (R) · n8n |
| Notas | Obsidian (P) · Logseq (+ diário e runbooks) |

## Correções que valem para sempre

1. **`.claudeignore` não existe no Claude Code.** O que funciona é `permissions.deny` no `.claude/settings.json`. O `.aiderignore` é do Aider e também está no repo-padrão.
2. **"Claude 3.5 Sonnet" está obsoleto.** A versão de modelo fica no gateway LiteLLM e em [custos.md](custos.md), nunca em documento.
3. **Zod é TypeScript.** O contrato do backend .NET é o OpenAPI (ADR 0006).
4. **age cifra, não assina.** Assinatura de firmware é o Secure Boot do chip (ESP32 ou STM32).
5. **Fator R:** os 6% do Anexo III valem só na 1ª faixa (até R$ 180 mil em 12 meses) e o pró-labore de 28% paga INSS de 11% e IR.
6. **`just architect` não pesquisa sozinho.** `just arquiteto` monta o pacote (stack, regras, o que existe, link do grep.app) e o Claude responde a partir dele.

## O cronograma de 14 dias

Fase **Sprint de 14 dias (Estratégia do Halter)**, no recesso escolar de jan/2027, com o gatilho de uma das 3 rendas de agora já ter passado no portão:

| Dias | O quê |
|---|---|
| 1 | VM, Uptime Kuma e Kamal conferidos |
| 2 | Chatwoot com e-mail pelo Resend |
| 3 | 5 empresas de Barbacena abordadas (lista aprovada por você) |
| 4 | Demonstração, proposta e contrato no Documenso (R$ 1.800 + R$ 350/mês, mais o custo da API do WhatsApp) |
| 5 e 6 | WhatsApp oficial do cliente, atendentes e a primeira fatura |
| 7 | Treinamento e NPS |
| 8 e 9 | MVP do ARCA em PocketBase e SvelteKit |
| 10 | Lógica dos 4 quadrantes e do aporte, com Zod e Vitest |
| 11 e 12 | Pix do Asaas e landing page em Astro |
| 13 e 14 | Playwright, deploy pelo Kamal com réplica no R2 e 50 testadores no TabNews |

## Ordem de montagem

```bash
cd ~/dev/dev-setup && git pull
bash scripts/wsl/bootstrap.sh --simular && bash scripts/wsl/bootstrap.sh   # just, terminal moderno, mise
bash scripts/wsl/extras.sh --simular && bash scripts/wsl/extras.sh         # CLIs do mise, uv, Podman, Git LFS
chezmoi init && cp -rn infra/dotfiles/. ~/.local/share/chezmoi/ && chezmoi init && chezmoi apply
just check                                                                  # antes de todo commit
just menu                                                                   # todas as receitas
```

Os serviços próprios (Forgejo, GlitchTip, BookStack, Headscale, Actual, Ghostfolio, Firefly III, Akaunting, Soft Serve) sobem por perfil: `just servico forgejo`. Os grandes (SigNoz, Plane, ERPNext, Formbricks, HeyForm, Plausible, Plunk, Coolify, Dokploy) têm o instalador oficial no passo de cada um.
