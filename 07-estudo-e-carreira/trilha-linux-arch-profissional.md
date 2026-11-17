---
tags: [estudo, linux, arch, infraestrutura, portfolio-ams]
tipo: trilha
status: novo
data: 2026-09-28
---

# 🐧 Trilha Linux/Arch Profissional

> Base de infraestrutura para dev, segurança e servidores. Cada fase termina com evidência pública (commit, README, post). O que não vira evidência não entra no currículo. Ponto de entrada do dia a dia continua sendo [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../PLANO-UNICO-AMtech.md).

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

## Fase 4 — Ambiente de desenvolvimento (stack nova)
Rodar o AM Gestão inteiro no Arch, sem Windows.

- [ ] Node + TypeScript via Mise; `node --version`
- [ ] Python via Mise (dados/IA); ambiente virtual por projeto
- [ ] IDE: VS Code ou LazyVim; registrar o motivo
- [ ] Docker nativo via systemd, usuário no grupo `docker`, sem Docker Desktop
- [ ] `docker compose` com PostgreSQL (ou Supabase local)
- [ ] Mise para Node, Python e versões por projeto
- [ ] Subir o AM Gestão do zero: frontend Next.js + API TS + Python + banco
- [ ] (Opcional) SDK do Go para o agente fiscal / ferramentas CLI
- [ ] ZSH: aliases, Starship, Atuin
- [ ] TUIs: LazyGit, LazyDocker
- [ ] **Evidência:** `setup-dev.sh` que reconstrói o ambiente num Arch limpo com um comando

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

## Fase 7 — Projeto autoral: um status na Waybar
Pequena ferramenta de status (Go ou Python) que agrega git/backup/estudo numa linha. Modo `--waybar` imprime uma linha JSON; a Waybar mostra o resumo e abre a TUI ao clicar. (Substitui o antigo `aura-status` em C#, arquivado.)

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
- [ ] Fixar no GitHub: dotfiles, ferramenta de status, homelab
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

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Trilha Linux/Arch Profissional](../12-artefatos/documentos/trilha-linux-arch-profissional.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->


---

## Horizonte longo — sistemas, baixo nível e SO próprio (estacionado)

> **Camada D do [00-PLANO-UNIFICADO](../PLANO-UNICO-AMtech.md).** Tudo aqui está **estacionado de propósito**: é o arco de ~10 anos, da base de sistemas até criar seu próprio SO e sua própria distro. Nenhum bloco compete pelas horas de 2026-2027. Ver tudo documentado aqui é o que te deixa tranquilo pra **não** tocar nisso agora.
>
> A parte ofensiva (reverse, exploit, kernel exploitation) é só **nomeada** aqui — o detalhe vive em [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md), não é duplicado.

---

## 🧭 Ordem de dependência (cada nível precisa do anterior)

```
MATEMÁTICA  (já corre na licenciatura + livro do Lins)
   ▼
LÓGICA · ALGORITMOS · ESTRUTURAS DE DADOS        → já no núcleo (Camada A)
   ▼
TypeScript · Python · SQL · C/C++ · Rust         → C/C++ e Rust vêm pela trilha de SO/robótica
   ▼
LINUX + WINDOWS (internals)                      → Linux já começa na Camada C
   ▼
REDES → SERVIDORES → WEB/APIs/DATABASES          → núcleo + Trilha de Redes
   ▼
CYBERSECURITY (web + Active Directory)           → trilha de segurança
   ▼
REVERSE ENGINEERING → ASSEMBLY → EXPLOIT DEV     → ponta avançada da segurança
   ▼
KERNEL (Linux · Windows NT · XNU/Apple)
   ▼
OS RESEARCH → AM-OS (SO próprio) · AM Linux (distro própria)
```

> macOS/iOS e Windows **não precisam esperar** terminar todo o Linux: depois dos fundamentos de redes, programação e SO, podem entrar em paralelo. Só o conteúdo realmente avançado (kernel, reverse profundo, pesquisa de vulnerabilidade) é que espera.

---

## 📚 Blocos por área (nível de currículo — o QUE estudar, não o passo a passo)

### Fundamentos de estudo
Terminal Linux/Windows · Git/GitHub · Markdown · leitura de RFC/manual/código-fonte · debugging · método científico · laboratório (virtualização, snapshots, redes isoladas) · escrita técnica · inglês técnico. → já coberto por [metodo-de-estudo](metodo-de-estudo.md).

### Matemática (profunda)
Básica → Álgebra → Geometria/Trigonometria → Discreta → Teoria dos Números → Cálculo → Álgebra Linear → Probabilidade/Estatística → (depois) Análise Real, Álgebra Abstrata, Topologia, Análise Complexa, EDO, Teoria da Informação, Teoria da Computação. → [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md).

### Ciência da Computação
Algoritmos, complexidade (Big-O), recursão, concorrência/paralelismo · estruturas de dados (array, lista, pilha, fila, árvore, heap, hash, grafo, trie) · algoritmos (ordenação, busca, DP, greedy, backtracking, grafos, caminho mínimo, árvore geradora, fluxo).

### Programação (baixo nível)
C, C++, Rust, Assembly x86-64/ARM64 · memória, ponteiros, stack/heap, gerência de memória, threads/processos, IPC, sockets, concorrência, async, generics, metaprogramação, FFI. → C/C++ pela [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md).

### Linux (profundo)
Fundamentos (FHS, terminal, permissões, processos, shell, Vim) → Arch manual → desktop (Wayland/Hyprland) → server → internals (kernel, syscalls, VFS, memória virtual, drivers) → LFS/BLFS → kernel development. → base prática em [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md).

### Windows / macOS / iOS
Windows: arquitetura NT, Win32/NT API, registro, NTFS, ACL/SID/tokens, UAC, PowerShell/WMI · Windows Internals · Active Directory.
macOS: Darwin/XNU/Mach/BSD, launchd, APFS, Keychain, SIP, Gatekeeper, TCC, sandbox, code signing.
iOS: iBoot, Secure Enclave, entitlements, provisioning, Data Protection, Mach-O, dyld, XPC.

### Segurança (web · redes · AD · ofensiva)
Escopo e trilha completos em [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md) e [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md). Áreas: segurança web (OWASP), pentest, wireless, AD security, reverse engineering, exploit development, kernel exploitation, malware analysis, forense digital, blue team, cloud security, segurança de containers/k8s, criptografia aplicada, segurança de hardware, IoT/embedded. **Regra permanente:** só em ambientes próprios ou autorizados.

### Sistemas Operacionais (juntar tudo)
boot/bootloader · kernel · memória virtual · processos/scheduling · interrupts · syscalls · IPC · filesystems · drivers · networking · segurança · userland. Comparar **Linux × Windows NT × XNU**.

---

## 🏗️ Projetos de coroação
- **AM-OS** — SO próprio: boot → GDT/IDT/interrupts → memória/paging → processos/scheduler → syscalls/user mode → filesystem/VFS → networking → shell → modelo de segurança.
- **AM Linux** — distro própria, depois do LFS: kernel + bootloader + glibc + systemd + coreutils + stack de rede + gerenciador de pacotes + instalador + ISO.
- **Homelab físico** — laboratório permanente (Linux/Windows/Apple, AD, Docker, monitoramento), expandindo com Raspberry Pi, mini-PC, switch, NAS, WireGuard. → [infraestrutura-fisica-10-anos](../01-planejamento-geral/infraestrutura-fisica-10-anos.md).

Progressão de identidade: **usuário Linux → administrador → desenvolvedor de sistemas → kernel developer → criador de distribuição.**

---

## 🔓 Gatilhos de ativação

| Bloco | Só ativa quando… |
|---|---|
| Linux internals, LFS/BLFS, Arch avançado | empregado como dev **E** Trilha Linux básica fechada |
| Windows internals, AD, macOS/iOS internals | a trilha de segurança (Camada C) chegar lá naturalmente |
| Reverse, exploit dev, kernel exploitation | pós-OSCP — ponta avançada da segurança |
| Criptografia avançada, hardware, IoT/embedded | quando um projeto real seu pedir |
| Linux kernel development | depois de C/C++ nativo (42) + Linux internals |
| **AM-OS** e **AM Linux** | só com kernel + C + Linux internals dominados |
| Homelab físico | quando houver renda extra pra hardware |

> **Padrão de toda a Camada D:** cada bloco termina em **laboratório + projeto + documentação + evidência**, igual aos sistemas Aura — nunca em "assisti a um curso".

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Trilha Linux/Arch Profissional](../12-artefatos/documentos/trilha-linux-arch-profissional.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
