# Contexto para a outra conta do Claude Code (porta de entrada)

> **Primeira mensagem na outra conta**, dentro do Claude Code aberto na pasta do dev-setup:
> *"Leia docs/implantacao/CONTEXTO-OUTRA-CONTA.md e docs/implantacao/INSTALACAO-AUTONOMA.md, nessa ordem, e siga os dois. Minha ficha está abaixo."* Cole a ficha da seção 0.1 do INSTALACAO-AUTONOMA.md logo depois.
> Se o repositório ainda não estiver no notebook, cole este arquivo e o INSTALACAO-AUTONOMA.md inteiros.
> Escrito em 11/11/2026, a partir da conversa "dev-setup: celular e instalação autônoma" da conta principal.

Este arquivo tem duas coisas:

- **(A)** o que foi decidido e construído na conversa da conta principal, que você não enxerga;
- **(B)** tudo o que precisa estar conectado, instalado e ligado para o setup funcionar, separado entre o que é preciso **para instalar** e o que vem **depois**.

O passo a passo da instalação está no INSTALACAO-AUTONOMA.md.

---

## A. O que a conversa da conta principal fez e decidiu

### A.1 O pedido do Alan

- Ver nas conversas anteriores o que falta e **pôr o setup para funcionar logo**, ao menos em partes, com **um comando**.
- **Criar coisas pelo celular** conectado ao setup local.
- Quando os créditos do Claude acabarem, as tarefas possíveis **continuam sem ele**.
- Ter o setup técnico **completo no notebook em 2 semanas** (até 25/11/2026), feito de forma autônoma por outra conta, para ele conferir o resultado depois.
- **Ele não vai ter acesso físico ao notebook** por enquanto. Tudo pelo celular, quando possível.

### A.2 O que foi construído (v2.28, PR #4 em `AlanMateus17/dev-setup`, ramo `v2.28-celular`)

| Peça | Onde | O que faz |
|---|---|---|
| `just ligar` | `scripts/wsl/ligar-tudo.sh` | Confere systemd e linger e instala o que falta (Claude Code, Ollama com `qwen2.5-coder:7b` e `qwen2.5:7b`, aider). Sobe o LiteLLM se houver Docker. Grava e liga os serviços `amtech-fila`, `amtech-remoto` (Claude Code Remote Control, modo servidor, worktree por sessão) e `amtech-bot`. Chama o `manter-ligado.ps1`. Também: `--simular`, `just ligado`, `just desligar`. |
| `manter-ligado.ps1` | `scripts/windows/` | Cria a tarefa "AMtech WSL" no login (liga o Ubuntu escondido), põe `vmIdleTimeout=-1` no `.wslconfig` e, só na tomada, tira o sono e faz a tampa fechada não suspender. Opções `-SemEnergia` e `-Desfazer`. Pede administrador por conta própria. |
| Fila de pedidos | `tools/remoto/fila.py` | `/pedir` e `/fila` no Telegram, e `just pedir` e `just fila` no terminal. O motor de decisão filtra primeiro. Cada pedido ganha uma worktree `~/dev/.fila/ID` no ramo `fila/ID`. Os motores, em ordem: Claude Code (`claude -p`) → aider com a cota grátis (LiteLLM ou Gemini direto) → aider com o Ollama local. Pedido sensível vai **só para o local**. Quando o Claude bate no limite, fica **5 h de pausa**. Depois: commit, PR em rascunho (se o `gh` estiver logado) e aviso no Telegram. **Nunca faz merge.** |
| LiteLLM | `infra/ia/litellm.yaml` | Modelo `local-codigo` e reserva `gratis → gratis-cf → reserva → local`. |
| Roteiro | `data/implantacao.json`, fase `f-remoto` | O passo `re-servico` virou `just ligar`. Passos novos: `re-remoto`, `re-gemini` e `re-teste`. |
| Permissões | `.claude/settings.json` | Libera os comandos do setup e bloqueia ler segredos, apagar em massa, push forçado ou na `main` e merge. |
| Documentos | `docs/operacao/celular.md`, `docs/implantacao/INSTALACAO-AUTONOMA.md`, este arquivo | Uso do celular, instalação autônoma e o contexto. |

Os testes passam: `just check` verde, 14 testes em `tools/remoto`, simulação do `just ligar` num HOME limpo, e a fila testada de ponta a ponta com motores falsos (o Claude bate no limite e a cota grátis faz o commit no ramo). A parte que **não foi testada** é a máquina real: WSL com systemd, GPU e `claude remote-control`. É você quem vai provar isso.

### A.3 Decisões que valem para você

- **A IA propõe e o código decide.** Mudança no repositório só por ramo e PR. O merge é sempre do Alan.
- **Dois caminhos pelo celular**, depois de instalado:
  1. **App do Claude → aba Code → sessão "Setup AMtech"** (Remote Control, plano Pro ou Max, na conta logada no Claude Code do notebook).
  2. **Telegram `/pedir`**, que continua funcionando sem crédito do Claude.
- **Sem crédito, o setup continua.** A cota grátis do Gemini e o modelo local seguram tarefas pequenas. Arquitetura e trabalho pesado esperam o Claude voltar. O local é um 7B na GTX 1650 de 4 GB: lento e erra mais.
- **Limites que o Alan já ouviu e aceitou:**
  - o notebook precisa estar ligado, na tomada e com internet;
  - senha, 2FA, sudo, administrador e reinício são dele;
  - as sessões 4, 5 e 7 da trilha (negócio, domínio, banco, contador, clientes) não são instalação.
- **Sem acesso físico:** antes de tudo, alguém em casa passa uns 10 minutos no notebook e instala o **Chrome Remote Desktop** (remotedesktop.google.com/access, conta Google do Alan, com PIN). A partir daí o Alan aprova permissões e digita senhas pelo celular.

### A.4 Estado em 11/11/2026, 20h46

- **PR #4 aberto, sem conflito e com os testes passando, esperando o merge do Alan.** Se ainda não estiver na `main`, peça a ele (pode ser pelo app do GitHub). Não faça o merge você.
- O que já está feito no notebook **não está confirmado**. Por um registro de 06/11, as fases 0, 3, 4 e 5 estavam feitas, além do backup inicial, do Windows Update, do 2FA no GitHub e do KeePassXC instalado. Confira tudo pelo diagnóstico e pela ficha.

---

## B. O que precisa estar conectado

Regra: **para instalar, quase nada.** Conectores e plugins servem para as fases de **depois** (sites, marketing, finanças). Não ligue o que não for usar agora: cada conector age na conta do Alan.

### B.1 Obrigatório para a instalação (sem isso não começa)

| Item | Como | Quem faz |
|---|---|---|
| Conta Pro ou Max nesta conta do Claude | O plano grátis não tem Claude Code | Alan |
| Claude Code no Windows | PowerShell normal: `irm https://claude.ai/install.ps1 \| iex`, depois `claude` e `/login` | Alan (ou quem estiver no notebook) |
| Git e o repositório | `winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements` e `git clone https://github.com/AlanMateus17/dev-setup.git "$HOME\dev-setup"`. O login do GitHub abre no navegador | Alan |
| Acesso remoto, se o Alan estiver longe | Chrome Remote Desktop com a conta Google dele e PIN | Alguém no notebook, 10 min |
| Notebook acordado | Na tomada e sem dormir. O `manter-ligado.ps1` resolve depois, mas até ele rodar, ajuste à mão: Configurações → Energia → "Nunca" na tomada | Alan |

### B.2 Aparece durante a instalação (já está no roteiro, na ordem)

| Item | Passo | Observação |
|---|---|---|
| GitHub CLI no Ubuntu com chave SSH | `gh-login`: `gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing` | O login é do Alan, pelo navegador. A fila usa o `gh` para abrir PR em rascunho |
| Claude Code também dentro do Ubuntu | `claude-login` (o bootstrap instala). Depois, `claude` e `/login` | Use a **mesma conta** que vai cuidar do Remote Control |
| Remote Control | `re-remoto`: `cd ~/dev/dev-setup && claude remote-control` → `y`, `y`, `2` → QR no celular → `Ctrl+C` → `touch ~/.config/amtech/remoto-aceito && just ligar` | A sessão "Setup AMtech" aparece no app do Claude da conta logada |
| Ollama e modelos | `just ligar` instala | ~9 GB. A GPU funciona se o driver NVIDIA do Windows estiver em dia |
| Chave grátis do Gemini | `re-gemini`: `GEMINI_API_KEY=` em `infra/ia/.env` (aistudio.google.com) | O Alan cria e cola. Cópia no KeePassXC |
| Bot do Telegram | `re-bot`, `re-env`, `re-id` | O Alan cria no @BotFather. O token vai para `~/.config/amtech/telegram.env` (permissão 600) |
| Docker Desktop no WSL | `docker-wsl` | Opcional para a fila. Necessário para o LiteLLM e o resto da infra |

### B.3 Servidores MCP do Claude Code (depois da instalação, passos do roteiro)

Rode no Ubuntu, na pasta do repositório. Conferir com `/mcp` dentro do Claude Code.

| MCP | Passo | Comando ou forma |
|---|---|---|
| GitHub (só o necessário) e banco de métricas (só leitura) | `mcp` (fase 6) | `claude "Passo mcp do roteiro: ..."`. Tokens no KeePassXC e em variável de ambiente, nunca no repositório |
| Hostinger | `ag-hostinger-mcp` | `bash ~/dev/dev-setup/scripts/wsl/segredos.sh "Hostinger/API_TOKEN" HOSTINGER_API_TOKEN -- claude mcp add -s user --env HOSTINGER_API_TOKEN="$HOSTINGER_API_TOKEN" hostinger-api-mcp -- npx -y hostinger-api-mcp`. Token criado pelo Alan no painel |
| Cloudflare (API nova) | `ag-cf-mcp` | `claude mcp add --transport http cloudflare https://mcp.cloudflare.com/mcp`, depois `/mcp` → autenticar. O conector antigo "Cloudflare Developer Platform" está **descontinuado** |
| Mercado Pago | fase de vendas | `claude mcp add --transport http mercadopago https://mcp.mercadopago.com/mcp`, depois `/mcp` → autenticar, região Brasil. **Só credenciais de teste** |
| MCP próprio (portfólio, softwares, roteiro) | `ia-mcp` | Construído pelo setup. Só leitura |
| Futuros | `sg-ghidramcp`, `co-mcp`, MCP do Home Assistant | Só nas fases deles |

### B.4 Plugins do Claude Code

- O marketplace oficial `claude-plugins-official` já vem no Claude Code. Veja e instale pelo `/plugin` → aba **Discover**.
- Os plugins de trabalho do Alan vêm do marketplace `anthropics/knowledge-work-plugins`: `/plugin marketplace add anthropics/knowledge-work-plugins`. Depois, pelo `/plugin`, instale **só estes**: small-business, marketing, engineering, design e finance.
- Os plugins de parceiro (**Hostinger, Adobe e Cloudinary**) você procura pelo nome no `/plugin` → Discover. O catálogo muda; se não aparecerem, anote no relatório e siga. Fiscal.ai é opcional, para estudos de investimento.
- Plugins adicionados pelo diretório do claude.ai chegam ao Claude Code pela sincronização da conta.
- **Não instale** maven-bio, Qt, conversor de CAD nem marketplaces de terceiros sem o Alan revisar: um plugin roda código na máquina dele.
- **Nenhum plugin é necessário para a instalação.** Ligue depois da sessão 3 da trilha.

### B.5 Conectores do claude.ai (nesta conta nova, todos começam desligados)

Os conectores são **por conta**: o que o Alan ligou na conta principal não existe aqui. Ele liga em claude.ai → Configurações → Conectores, conforme a fase pedir. A instalação não precisa de nenhum.

| Ligar quando a fase pedir | Para quê |
|---|---|
| Google (Gmail, Agenda, Drive) | Rotina, agenda e documentos |
| Canva, Figma, Adobe | Artes e sites |
| MailerLite | Lista de e-mail (atenção ao limite grátis) |
| Microsoft Learn | Estudo de .NET e Azure |
| Supabase, Lovable | Validar MVP antes de construir |
| Cloudflare (o novo, `https://mcp.cloudflare.com/mcp`) | DNS e Pages dos sites que vendem |
| Upwork | Freelas (depois do inglês B1) |
| vidIQ | Fase de conteúdo |
| Vercel | **Só projeto pessoal**: o plano Hobby não permite uso comercial |

**Não ligar:** Notion, monday, GitBook, Stripe, Shopify, WordPress.com e Spotify. Eles repetem ferramentas que já estão no setup (Obsidian, GitHub Projects, MkDocs, Hotmart) ou não entram no plano. **Hotmart nunca entra como conector**: só por webhook no n8n.

### B.6 O que NÃO precisa conectar

O GitHub da conta do Claude não é o que dá acesso ao repositório: o acesso vem do login do Alan no `git` e no `gh` do notebook. Não precisa de API paga do Claude: a fila usa a assinatura. Não precisa de nenhuma senha do Alan em lugar nenhum: tudo o que é segredo passa por ele e pelo KeePassXC.

---

## C. Ao terminar cada dia de trabalho

1. Atualize `~/dev/RELATORIO-INSTALACAO.md`: o que ficou feito, com a prova, a lista do Alan, uma linha por item, e os problemas.
2. Acrescente até 5 linhas ao `ESTADO.md`, num ramo, por PR.
3. Diga ao Alan, em até 5 linhas: o que ficou pronto, o que é dele (com o comando e onde rodar) e qual é o próximo passo.
