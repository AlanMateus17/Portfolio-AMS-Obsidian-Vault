---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Setup do Ambiente de Trabalho — Versão Final Consolidada
### Acer Nitro AN515-45 — reconstruído após reinstalação do Windows, atualizado com tudo decidido no portfólio de 23 sistemas

> **Contexto real:** o Windows foi reinstalado (corrupção) e o ambiente está sendo remontado do zero. Este documento consolida o que já foi confirmado instalado, o que falta do checklist original, e o que precisa ser **adicionado** agora que o portfólio cresceu (AM Taskoro, Trilha 42, Segurança Ofensiva **e** Defensiva).

---

## 🚨 Dois alertas reais, resolver antes de continuar o resto

### 1. Versão do .NET — verificar antes de prosseguir
Confirmado instalado: **.NET SDK 9.0.317**. Mas todo o portfólio (RNF, RF, os 23 sistemas) foi decidido em **C#/.NET 10**. Duas possibilidades: (a) você instalou a 9 de propósito porque a 10 ainda não estava disponível/estável via `winget` no momento, ou (b) foi instalada por engano durante a reconstrução rápida. **Ação:** rodar `dotnet --list-sdks`, confirmar se o SDK 10 já está disponível pra instalar, e se estiver, instalar ele também (podem coexistir) — não precisa desinstalar a 9, mas o projeto real deve mirar a 10.

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

### Camada 1 — Fundamento do stack fixo (C#/.NET)
- [ ] Confirmar/instalar .NET SDK 10 (ver alerta 1 acima)
- [ ] `dotnet-ef` (global tool, pra migration do EF Core)
- [ ] Extensão C# Dev Kit no VS Code (se for usar VS Code em vez do Visual Studio pra parte do trabalho)
- [ ] **Gitleaks** (binário + hook de pre-commit) — segredo vazado em commit, especialmente importante usando Claude Code (ver [seguranca-e-ferramentas-todas-as-frentes](../01-planejamento-geral/seguranca-e-ferramentas-todas-as-frentes.md))
- [ ] `git lfs install` — mesmo sem uso imediato, deixa configurado antes de precisar
- [ ] Claude Code (`npm install -g @anthropic-ai/claude-code` ou instalador nativo — requer Node.js 18+, já confirmado instalado)

### Camada 2 — Frontend (Next.js)
- [ ] `nvm-windows` + `pnpm` (gerenciador de versão Node + pacote mais rápido que npm) — necessário pro Next.js do Design System compartilhado, usado por todo o portfólio, não só um sistema
- [ ] Extensões VS Code: ESLint, Prettier, Tailwind CSS IntelliSense

### Camada 3 — Banco de dado e API local
- [ ] DBeaver (cliente visual de Postgres/Redis)
- [ ] Bruno (cliente de API, alternativa gratuita ao Postman)
- [ ] `docker-compose.yml` padrão do AM Kaixara rodando Postgres + Redis local

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
- [Next.js/Design System](../04-documentos-transversais/rnf-transversais-design-tema.md) — o que a Camada 2 deste setup sustenta (não mais o AM Taskoro, que agora é .NET)
- [sequencia-mestra-completa-desde-o-inicio](../99-arquivo/sequencia-mestra-completa-desde-o-inicio.md) — onde cada camada entra na ordem real de estudo
