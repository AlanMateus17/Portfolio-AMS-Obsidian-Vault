---
tags: [estudo, linux, arch, infraestrutura, portfolio-ams]
tipo: trilha
status: novo
data: 2026-09-28
---

# 🐧 Trilha Linux/Arch Profissional

> Base de infraestrutura para dev, segurança e servidores. Cada fase termina com evidência pública (commit, README, post). O que não vira evidência não entra no currículo. Ponto de entrada do dia a dia continua sendo [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]].

**Regra de foco:** uma fase por vez. Repositório único desde o dia 1: `AlanMateus17/dotfiles`, que recebe configs, scripts e notas de todas as fases.

---

## Fase 1 — Fundamentos de Linux
Dá para fazer tudo no WSL2 que já existe no notebook.

- [ ] Hierarquia de diretórios (FHS): `/etc`, `/var`, `/usr`, `/home`, `/boot`, `/proc`, `/dev`
- [ ] Navegação e arquivos: `ls`, `cd`, `cp`, `mv`, `rm`, `find`, `ln`
- [ ] Texto: `cat`, `less`, `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, pipes e redirecionamento
- [ ] Permissões: `chmod` (octal e simbólico), `chown`, UID/GID, `sudo`, grupos, setuid
- [ ] Processos: `ps`, `htop`, `kill`, sinais, jobs
- [ ] `vimtutor` inteiro
- [ ] Variáveis de ambiente e `PATH`; `.bashrc` vs `.zshrc` vs `.profile`
- [ ] Git no terminal sem IDE: branch, merge, rebase, conflito
- [ ] **Evidência:** `notas/01-fundamentos.md` no dotfiles

## Fase 2 — Instalação manual do Arch em VM
Pelo guia oficial do ArchWiki, sem archinstall. Em VirtualBox ou QEMU.

- [ ] VM em modo UEFI, boot na ISO oficial
- [ ] Particionar na mão (`fdisk`/`cfdisk`): EFI + raiz
- [ ] Formatar raiz em BTRFS, subvolumes `@` e `@home`
- [ ] `pacstrap`, `genfstab`, `arch-chroot`
- [ ] Fuso, locale, hostname, usuário com `sudo`, NetworkManager
- [ ] Bootloader (GRUB ou systemd-boot) e boot sozinho
- [ ] Quebrar de propósito e recuperar via `arch-chroot`
- [ ] Repetir até fazer sem consultar o guia a cada passo
- [ ] Depois, instalar uma vez com `archinstall` e comparar
- [ ] **Evidência:** `notas/02-instalacao-manual.md`

## Fase 3 — Setup real com Omarchy no notebook
Acer Nitro. Ponto de maior risco: GPU híbrida (AMD integrada + NVIDIA). Testar antes de apagar.

- [ ] Backup completo (arquivos, chaves SSH, lista de programas)
- [ ] Pendrive com Ventoy; ISO do Omarchy em live; testar Wi-Fi, áudio, brilho, suspensão, 2º monitor
- [ ] Decidir: Linux só ou dual boot com Windows (se ainda depender do Visual Studio). Registrar o motivo
- [ ] Instalar pela ISO do Omarchy (LUKS + Limine + Snapper)
- [ ] NVIDIA: integrada no desktop, dedicada sob demanda; verificar `nvidia-smi`
- [ ] Subvolumes separados para `/var/lib/docker` (fora dos snapshots)
- [ ] Testar rollback: instalar, snapshot, quebrar, voltar pelo boot
- [ ] Ler o manual do Omarchy; decorar atalhos
- [ ] Configurar monitores/workspaces em `~/.config/hypr/`
- [ ] Pacotes: `pacman`, `yay`, AUR, remover órfãos, ler `PKGBUILD`
- [ ] **Evidência:** `~/.config/hypr/` versionado + `notas/03-setup-notebook.md`

## Fase 4 — Ambiente de desenvolvimento .NET/Aura
Rodar um sistema do Aura inteiro no Arch, sem Windows.

- [ ] .NET 10 SDK (pacote ou Mise); `dotnet --info`
- [ ] IDE: Rider, VS Code (C# Dev Kit) ou LazyVim (extra de C#); registrar o motivo
- [ ] Docker nativo via systemd, usuário no grupo `docker`, sem Docker Desktop
- [ ] `docker compose` com PostgreSQL e Redis
- [ ] Mise para Node, Python e versões por projeto
- [ ] Subir o AM Kaixara do zero: API + banco + frontend Next.js
- [ ] ZSH: aliases, Starship, Atuin
- [ ] TUIs: LazyGit, LazyDocker
- [ ] **Evidência:** `setup-aura-dev.sh` que reconstrói o ambiente num Arch limpo com um comando

## Fase 5 — Administração e automação
"Uso Linux" vira "administro Linux". A fase que mais pesa em entrevista.

- [ ] systemd: `systemctl`, escrever um serviço em `/etc/systemd/system/`
- [ ] systemd timers no lugar de cron
- [ ] Logs: `journalctl` (por serviço, por boot, por prioridade)
- [ ] Diagnóstico: `df`, `du`, `free`, `lsblk`, `ss`, `ip`, `dmesg`
- [ ] Bash: `set -euo pipefail`, funções, argumentos, erro; passar no `shellcheck`
- [ ] Backup: `rsync` + timer semanal; testar restauração
- [ ] BTRFS: `scrub`, `balance`, uso real de espaço
- [ ] Rede: DNS, `/etc/hosts`, `nmcli`
- [ ] **Evidência:** pastas `scripts/` e `systemd/` no dotfiles, com teste de restauração

## Fase 6 — Segurança
- [ ] Chaves SSH ED25519 com senha; `ssh-agent`; `~/.ssh/config`
- [ ] Servidor SSH na VM: sem login por senha nem root
- [ ] Firewall com `ufw` ou `nftables`
- [ ] Entender o LUKS do Omarchy; backup do header
- [ ] Reinstalar KeePassXC
- [ ] Assinar commits no Git
- [ ] Rotina de atualização: ler avisos do archlinux.org antes
- [ ] **Regra do repo público:** nenhuma chave/senha/IP interno; segredos fora do Git
- [ ] **Evidência:** `notas/06-seguranca.md`

## Fase 7 — Projeto autoral: aura-status na Waybar
Ver documento próprio: [[aura-status-documento-projeto-final]]. O aura-status ganha modo `--waybar` que imprime uma linha JSON; a Waybar mostra o resumo e abre a TUI ao clicar.

- [ ] `Severidade`, `ResultadoStatus`, `WaybarFormatter` com testes
- [ ] Modo `--waybar` abaixo de 1s (cache para fontes lentas como a API do GitHub)
- [ ] Publicar binário único e configurar o módulo na Waybar
- [ ] TUI com Spectre.Console ao clicar
- [ ] Hook do Git que envia sinal de atualização
- [ ] `PKGBUILD` no AUR (opcional, diferencial forte)
- [ ] **Evidência:** repositório com README e GIF da barra

## Fase 8 — Homelab e infraestrutura
Dá para começar sem o NAS: PC velho, Raspberry Pi ou VM sempre ligada.

- [ ] Servidor Linux sem interface, só SSH
- [ ] Gitea self-hosted com Docker Compose
- [ ] NFS ou Samba montado no notebook via `fstab` com automount
- [ ] Backup do notebook para o servidor, por timer, com teste de restauração
- [ ] Acesso externo seguro (WireGuard ou túnel), nunca porta aberta no roteador
- [ ] Monitoramento simples (disco cheio, container caído)
- [ ] Levar o banco de dev do Aura para o servidor
- [ ] **Evidência:** repo `homelab` com `docker-compose.yml` (sem segredos), diagrama e README

## Fases 9–10 — Documentação e currículo
- [ ] README do dotfiles com screenshot e decisões (por que BTRFS, subvolumes, Omarchy)
- [ ] Fixar no GitHub: dotfiles, aura-status, homelab
- [ ] Série no blog, um post por fase
- [ ] Contribuir com algo pequeno em projeto aberto
- [ ] Linhas de currículo (com link): administração Linux, automação de ambiente, ferramenta autoral, infraestrutura
- [ ] Competências só o que defende sem consulta: Linux (Arch), Bash, systemd, BTRFS, Docker, Git, SSH, Neovim

## Critério final de domínio
- [ ] Instalar Arch manual em < 1h
- [ ] Recuperar sistema que não dá boot (snapshot e `arch-chroot`)
- [ ] Reconstruir o notebook inteiro pelo repositório numa tarde
- [ ] Restaurar arquivo do backup (não só do snapshot)
- [ ] Explicar cada linha do `fstab`, do `hyprland.conf` e dos scripts
- [ ] 3 repositórios públicos, documentados, com commits recentes
