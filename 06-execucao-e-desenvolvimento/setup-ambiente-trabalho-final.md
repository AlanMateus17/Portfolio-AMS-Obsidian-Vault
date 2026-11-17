---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Setup do Ambiente de Trabalho — Versão Final Consolidada
### Acer Nitro AN515-45 — reconstruído após reinstalação do Windows, atualizado para a stack nova (AM Gestão)

> **Contexto real:** o Windows foi reinstalado (corrupção) e o ambiente está sendo remontado do zero. Este documento consolida o que já foi confirmado instalado, o que falta do checklist, e o que o ambiente precisa agora com a stack nova (TS + Python + SQL; Go e C# como reserva), além de Trilha 42 e Segurança.

---

## 🚨 Dois alertas reais, resolver antes de continuar o resto

### 1. Núcleo da stack nova — garantir antes de prosseguir
O núcleo agora é **TypeScript + Python + SQL** (ver [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md)). **Ação:** confirmar Node LTS + pnpm e Python 3.13 funcionando (`node -v`, `pnpm -v`, `python --version`). O .NET deixou de ser base — só instale o SDK quando for mexer na carta de reserva (vaga .NET ou agente fiscal, onde Go também serve).

### 2. Senha da chave SSH em papel — resolver com prioridade máxima
A senha da chave SSH está anotada fisicamente, aguardando o KeePassXC terminar de instalar. **Ação imediata:** assim que o KeePassXC estiver pronto, mover essa senha pra lá e destruir o papel — é o primeiro item a fechar, antes de qualquer outra coisa deste documento, porque é o único risco de segurança real e ativo agora.

---

## ✅ Já confirmado funcionando (não precisa reinstalar)

- Node.js 24.19 LTS, Git 2.55, VS Code, Docker Desktop 4.88 (testado com `docker run hello-world`)
- Python 3.13
- WSL2 + Ubuntu, usuário `alanmateus`
- Chave SSH ED25519 gerada e autenticada no GitHub
- Identidade Git configurada (nome + e-mail)
- Repositórios confirmados intactos no GitHub: Aura, AM Kaixara, AMtech
- Visual Studio 2026 instalando com workload **C++ Desktop** já incluído — bom, isso já cobre parte do que a Trilha 42 vai precisar

---

## 📋 Checklist completo, na ordem certa — o que falta

### Camada 1 — Fundamento do núcleo (TypeScript + Python)
- [ ] Node LTS + **pnpm** (via nvm-windows ou Mise)
- [ ] Python 3.13 + ambiente virtual por projeto; `pip`/`uv`
- [ ] Extensões VS Code: ESLint, Prettier, Python, Pylance
- [ ] (Só se for mexer na reserva) .NET SDK ou Go
- [ ] **Gitleaks** (binário + hook de pre-commit) — segredo vazado em commit, especialmente importante usando Claude Code (ver [seguranca-e-ferramentas-todas-as-frentes](../01-planejamento-geral/seguranca-e-ferramentas-todas-as-frentes.md))
- [ ] `git lfs install` — mesmo sem uso imediato, deixa configurado antes de precisar
- [ ] Claude Code (`npm install -g @anthropic-ai/claude-code` ou instalador nativo — requer Node.js 18+, já confirmado instalado)

### Camada 2 — Frontend (Next.js)
- [ ] `nvm-windows` + `pnpm` (gerenciador de versão Node + pacote mais rápido que npm) — necessário pro Next.js do Design System compartilhado, usado por todo o portfólio, não só um sistema
- [ ] Extensões VS Code: ESLint, Prettier, Tailwind CSS IntelliSense

### Camada 3 — Banco de dado e API local
- [ ] DBeaver (cliente visual de Postgres)
- [ ] Bruno (cliente de API, alternativa gratuita ao Postman)
- [ ] `docker-compose.yml` do AM Gestão rodando Postgres local (ou Supabase local via CLI)

### Camada 4 — Trilha 42 (C/C++)
- [ ] Toolchain C/C++ dentro do WSL2: `build-essential`, `make`, `cmake`, `gdb`, `valgrind`
- [ ] MiniLibX (biblioteca gráfica da 42, pros projetos `so_long`/`miniRT`)
- [ ] Norminette (`pip install norminette` dentro do WSL2 — verificador de estilo de código oficial da 42)

### Camada 5 — Segurança Ofensiva
- [ ] VirtualBox + Kali Linux (pode continuar como "depois", não bloqueia o resto)
- [ ] Burp Suite Community, Nmap, Wireshark (dentro da VM Kali ou do WSL2)

### Camada 6 — Segurança Defensiva (novo — nunca listado antes)
- [ ] Wazuh ou Security Onion (SIEM open source, pra prática de Blue Team — ver `plano-estudos-basico-avancado-entrelacado`, Fase 12B)
- [ ] Sysmon (Windows, já parcialmente coberto pelo Sysinternals da Camada 8) — logging avançado de evento do sistema

### Camada 7 — Senha e organização
- [ ] Finalizar instalação do KeePassXC, restaurar banco de senha, mover a senha SSH do papel pra lá (Alerta 2)
- [ ] Obsidian — restaurar o vault (59 arquivos, `Portfolio-AMS-Obsidian-Vault.zip`, já existe pronto pra importar)

### Camada 8 — Produtividade geral
- [ ] PowerToys, Everything (busca), 7-Zip, ShareX (captura de tela), Sysinternals Suite

### Camada 9 — Frentes de renda paralelas
- [ ] Python + Poppler + Pillow + ReportLab (pipeline de material didático, já em uso de produção)
- [ ] Local by Flywheel ou XAMPP + FileZilla (freelance WordPress/Hostinger)

### Camada 10 — Cloud (decisão pendente)
- [ ] CLI da cloud escolhida (AWS ou Azure) — **decisão ainda não tomada**, mesma pendência transversal já registrada em vários documentos do portfólio; não instalar CLI de nenhuma das duas até decidir

### Camada 11 — Backup e continuidade (a lição real desta reconstrução)
- [ ] NAS com RAID 1, ou pelo menos backup automático do `C:\dev\` e do vault do Obsidian em nuvem — **esta reconstrução inteira aconteceu porque não havia backup local automático**; vale resolver isso antes de qualquer coisa da Camada 9-10, não depois

---

## 🔗 Documentos relacionados
- [infraestrutura-fisica-10-anos](../01-planejamento-geral/infraestrutura-fisica-10-anos.md) — este documento é a fatia de software da Camada 4 dessa arquitetura maior
- [seguranca-e-ferramentas-todas-as-frentes](../01-planejamento-geral/seguranca-e-ferramentas-todas-as-frentes.md) — Gitleaks, Git LFS e Claude Code, detalhados
- [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md) — Fase 12 (Segurança Ofensiva) e Fase 12B (Segurança Defensiva, nova)
- [trilha-42-circles-oficial-verificado](../07-estudo-e-carreira/trilha-42-circles-oficial-verificado.md) — o que a Camada 4 deste setup sustenta
- [Next.js/Design System](../04-documentos-transversais/rnf-transversais-design-tema.md) — o que a Camada 2 deste setup sustenta
- [sequencia-mestra-completa-desde-o-inicio](../99-arquivo/sequencia-mestra-completa-desde-o-inicio.md) — onde cada camada entra na ordem real de estudo

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Fluxogramas do Setup](../12-artefatos/paginas/fluxogramas-do-setup-vbdz/index.html) · página interativa · [sobre](../12-artefatos/paginas/fluxogramas-do-setup-vbdz/LEIA-ME.md)
- [Mapa do Setup AMtech](../12-artefatos/paginas/mapa-do-setup-amtech-btuy/index.html) · página interativa · [sobre](../12-artefatos/paginas/mapa-do-setup-amtech-btuy/LEIA-ME.md)
- [Implantação AMtech](../12-artefatos/paginas/implantacao-amtech-cj27/index.html) · página interativa · [sobre](../12-artefatos/paginas/implantacao-amtech-cj27/LEIA-ME.md)
- [Repositório dev-setup (versão de 23/10)](../12-artefatos/paginas/repositorio-dev-setup-k9wt/index.html) · página interativa · [sobre](../12-artefatos/paginas/repositorio-dev-setup-k9wt/LEIA-ME.md)
- [Repositório dev-setup (versão de 21/10)](../12-artefatos/paginas/repositorio-dev-setup-ria4/index.html) · página interativa · [sobre](../12-artefatos/paginas/repositorio-dev-setup-ria4/LEIA-ME.md)
- [Casa Inteligente e Setup Automatizado](../12-artefatos/documentos/casa-inteligente-e-setup-automatizado.md)
- [Guia de Terminal: Git, GitHub, PowerShell e Git Bash](../12-artefatos/documentos/guia-de-terminal-git-github-powershell-e-git-bash.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
