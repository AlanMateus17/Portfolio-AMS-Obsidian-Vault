# Trilha Linux/Arch Profissional

Sep 27, 2026 · @Alan Mateus

## Como usar esta trilha

O objetivo é sair de "uso Arch" para "administro e automatizo Linux e provo isso publicamente". São 10 fases; cada uma termina com algo que um recrutador consegue abrir e verificar.

- **Regra da evidência:** uma tarefa só está feita quando deixou um rastro público (commit, README, post, script). O que não tem link não entra no currículo.
- **Ordem:** faça as fases em sequência. As fases 1 e 2 acontecem em máquina virtual, sem arriscar o notebook.
- **Ritmo realista:** algo entre 3 e 5 meses no seu tempo livre. Uma fase por vez; não abra a próxima antes de fechar a anterior.
- **Fonte principal:** [ArchWiki](https://wiki.archlinux.org/title/Main_page) e as páginas `man`. Vídeos servem de apoio, não de base.
- **Repositório único desde o dia 1:** crie `AlanMateus17/dotfiles` agora. Ele vai recebendo configs, scripts e anotações de todas as fases.

## Fase 1: Fundamentos de Linux

Antes de instalar qualquer coisa, domine o terreno. Dá para fazer tudo no WSL2 que você já tem.

- [ ] Hierarquia de diretórios (FHS): saber o que vive em `/etc`, `/var`, `/usr`, `/home`, `/boot`, `/proc`, `/dev`
- [ ] Navegação e arquivos: `ls`, `cd`, `cp`, `mv`, `rm`, `find`, `ln` (link simbólico e hard link)
- [ ] Texto no terminal: `cat`, `less`, `grep`, `sed`, `awk`, `cut`, `sort`, `uniq`, `wc`, pipes e redirecionamento (`|`, `>`, `>>`, `2>&1`)
- [ ] Permissões: `chmod` (octal e simbólico), `chown`, UID/GID, `sudo`, grupos, setuid
- [ ] Processos: `ps`, `top`/`htop`, `kill`, sinais, jobs em primeiro e segundo plano
- [ ] Editor no terminal: completar o `vimtutor` inteiro
- [ ] Variáveis de ambiente e `PATH`; diferença entre `.bashrc`, `.zshrc` e `.profile`
- [ ] Git no terminal sem IDE: branch, merge, rebase, resolver conflito
- [ ] **Evidência:** `notas/01-fundamentos.md` no repo de dotfiles, com os comandos que você mais usou e um exemplo real de cada

## Fase 2: Instalação manual do Arch em VM

É o exercício que o Akita deixa para iniciantes: instalar pelo [guia oficial](https://wiki.archlinux.org/title/Installation_guide), sem archinstall. Faça em VirtualBox ou QEMU, quantas vezes precisar.

- [ ] Criar a VM em modo UEFI e dar boot na ISO oficial
- [ ] Particionar na mão com `fdisk` ou `cfdisk`: partição EFI + raiz
- [ ] Formatar a raiz em BTRFS e criar os subvolumes `@` e `@home`
- [ ] `pacstrap`, `genfstab`, `arch-chroot`: entender o que cada um faz
- [ ] Configurar fuso, locale, hostname, usuário com `sudo` e NetworkManager
- [ ] Instalar e configurar um bootloader (GRUB ou systemd-boot) e dar boot sozinho
- [ ] Quebrar de propósito (apagar o `fstab`, errar o bootloader) e recuperar pela ISO com `arch-chroot`
- [ ] Repetir a instalação até conseguir fazer sem consultar o guia a cada passo
- [ ] Depois, instalar uma vez com `archinstall` e comparar o resultado
- [ ] **Evidência:** `notas/02-instalacao-manual.md` com o passo a passo nas suas palavras, os erros que você cometeu e como resolveu

## Fase 3: Setup real com Omarchy no notebook

Agora sim no Acer Nitro. O ponto de maior risco é a GPU híbrida (AMD integrada + NVIDIA), então teste antes de apagar qualquer coisa.

- [ ] Backup completo do que existe hoje (arquivos, chaves SSH, lista de programas)
- [ ] Pendrive com Ventoy; dar boot na ISO do Omarchy em modo live e testar Wi-Fi, áudio, brilho, suspensão e segundo monitor
- [ ] Decidir: Linux só ou dual boot com Windows (se ainda depender do Visual Studio). Registrar a decisão e o motivo
- [ ] Instalar pela ISO do Omarchy (LUKS + Limine + Snapper)
- [ ] Configurar a NVIDIA: GPU integrada no desktop, dedicada sob demanda; verificar com `nvidia-smi`
- [ ] Criar subvolumes separados para `/var/lib/docker` (fora dos snapshots)
- [ ] Testar o rollback: instalar algo, criar snapshot, quebrar e voltar pelo menu de boot
- [ ] Ler o manual do Omarchy e decorar os atalhos principais
- [ ] Configurar monitores e workspaces em `~/.config/hypr/` para o seu uso
- [ ] Dominar o gerenciamento de pacotes: `pacman`, `yay`, AUR, remover órfãos, ler um `PKGBUILD` antes de instalar
- [ ] **Evidência:** `~/.config/hypr/` versionado no repo de dotfiles + `notas/03-setup-notebook.md` com hardware, decisões e problemas resolvidos

## Fase 4: Ambiente de desenvolvimento .NET/Aura

O objetivo é rodar um sistema do Aura inteiro no Arch, sem Windows no caminho.

- [ ] Instalar o .NET 10 SDK (pacote oficial ou via Mise) e rodar `dotnet --info`
- [ ] Escolher a IDE (Rider, VS Code com C# Dev Kit ou LazyVim com o extra de C#) e registrar o motivo
- [ ] Docker nativo: serviço via systemd, usuário no grupo `docker`, sem Docker Desktop
- [ ] `docker compose` com PostgreSQL e Redis para desenvolvimento
- [ ] Mise para Node, Python e demais versões por projeto
- [ ] Subir o AM Kaixara (ou outro projeto do Aura) do zero: API + banco + frontend Next.js
- [ ] ZSH configurado: aliases, Starship, Atuin
- [ ] TUIs no dia a dia: LazyGit, LazyDocker
- [ ] **Evidência:** script `setup-aura-dev.sh` no repo que reconstrói esse ambiente num Arch limpo com um comando. Testar na VM da Fase 2

## Fase 5: Administração e automação

É aqui que "uso Linux" vira "administro Linux". É a fase que mais pesa numa entrevista.

- [ ] systemd: `systemctl` (start, enable, status), escrever um serviço próprio em `/etc/systemd/system/`
- [ ] systemd timers no lugar de cron: agendar uma tarefa real
- [ ] Logs com `journalctl`: filtrar por serviço, por boot, por prioridade
- [ ] Diagnóstico: `df`, `du`, `free`, `lsblk`, `ss`, `ip`, `dmesg`
- [ ] Bash de verdade: `set -euo pipefail`, funções, argumentos, tratamento de erro; passar os scripts no `shellcheck`
- [ ] Backup: script com `rsync` para disco externo + timer semanal; testar a restauração
- [ ] Manutenção de BTRFS: `btrfs scrub`, `balance`, uso real de espaço
- [ ] Rede: DNS, `/etc/hosts`, NetworkManager pela linha de comando (`nmcli`)
- [ ] **Evidência:** pasta `scripts/` e `systemd/` no repo, cada script com comentário de uso e um teste de restauração documentado

## Fase 6: Segurança

- [ ] Chaves SSH ED25519 com senha; `ssh-agent`; arquivo `~/.ssh/config` para seus hosts
- [ ] Servidor SSH na VM: desativar login por senha e login como root
- [ ] Firewall com `ufw` ou `nftables`: liberar só o necessário
- [ ] Entender o LUKS que o Omarchy configurou: onde fica, como trocar a senha, header de backup
- [ ] Reinstalar o KeePassXC e organizar o cofre
- [ ] Assinar commits no Git com a chave SSH
- [ ] Rotina de atualização: ler as notícias do [archlinux.org](https://archlinux.org/) antes de atualizar
- [ ] **Regra para o repo público:** nenhuma chave de API, senha ou IP interno. Segredos ficam num arquivo fora do Git (ex.: `~/.secrets`, carregado pelo `.zshrc`)
- [ ] **Evidência:** `notas/06-seguranca.md` com o que foi endurecido e por quê

## Fase 7: Projeto autoral — aura-status na Waybar

O aura-status ganha um modo `--waybar` que imprime uma linha de JSON. A Waybar executa o programa, mostra o resumo na barra e, ao clicar, abre a TUI completa no terminal. Nenhuma interface gráfica precisa ser desenvolvida.

### Como funciona

1. A Waybar roda `aura-status --waybar` a cada 5 minutos (ou quando recebe um sinal).
2. O aura-status consulta as fontes que já existem via `IFonteDeStatus` (git, backup, catálogo de estudos, Dependabot).
3. Ele calcula a pior severidade entre as fontes e devolve o JSON.
4. A Waybar pinta o módulo pela `class` (ok, aviso, crítico) e mostra os detalhes no `tooltip`.
5. Clique: abre `aura-status` em modo TUI no terminal.

### Contrato de saída (uma linha, JSON)

```json
{"text": " 3   ok", "tooltip": "am-kaixara: 2 commits sem push\nam-rotara: 1 PR do Dependabot\nBackup: há 20 h", "class": "aviso", "alt": "aviso"}
```

### No C#

```csharp
public enum Severidade { Ok, Aviso, Critico }

public sealed record ResultadoStatus(string Fonte, Severidade Severidade, string Resumo, IReadOnlyList<string> Detalhes);

public static class WaybarFormatter
{
    public static string Formatar(IReadOnlyList<ResultadoStatus> resultados)
    {
        var pior = resultados.Max(r => r.Severidade);
        var saida = new
        {
            text = string.Join("  ", resultados.Select(r => r.Resumo)),
            tooltip = string.Join("\n", resultados.SelectMany(r => r.Detalhes)),
            @class = pior.ToString().ToLowerInvariant(),
            alt = pior.ToString().ToLowerInvariant()
        };
        return JsonSerializer.Serialize(saida);
    }
}
```

No `Program.cs`, se `args` contiver `--waybar`, chama o formatter e sai; sem argumento, abre a TUI (Spectre.Console é a opção mais simples). Publique como binário único com `dotnet publish -c Release -r linux-x64 --self-contained -p:PublishSingleFile=true` e copie para `~/.local/bin/`.

### Na Waybar (`~/.config/waybar/config.jsonc`)

```jsonc
"modules-right": ["custom/aura-status", "..."],

"custom/aura-status": {
  "exec": "~/.local/bin/aura-status --waybar",
  "return-type": "json",
  "interval": 300,
  "signal": 8,
  "on-click": "alacritty -e ~/.local/bin/aura-status",
  "tooltip": true
}
```

Troque `alacritty` pelo terminal que o seu Omarchy usar. O `signal: 8` permite atualizar na hora com `pkill -RTMIN+8 waybar`, por exemplo num hook `post-commit` do Git.

### No estilo (`~/.config/waybar/style.css`)

```css
#custom-aura-status.ok      { color: #7fb77e; }
#custom-aura-status.aviso   { color: #C08A3E; }
#custom-aura-status.critico { color: #e06c75; }
```

### Tarefas

- [ ] Implementar `Severidade`, `ResultadoStatus` e `WaybarFormatter` com testes unitários
- [ ] Modo `--waybar` com tempo de resposta abaixo de 1 segundo (usar cache se a fonte for lenta, como a API do GitHub)
- [ ] Publicar binário único e configurar o módulo na Waybar
- [ ] TUI com Spectre.Console ao clicar
- [ ] Hook do Git que envia o sinal de atualização
- [ ] Pacote no AUR (`PKGBUILD`) para instalar com `yay` — opcional, mas é o diferencial mais forte da trilha
- [ ] **Evidência:** repositório próprio com README, GIF da barra funcionando e instruções de instalação

## Fase 8: Homelab e infraestrutura

Dá para começar sem o NAS: um PC velho, um Raspberry Pi ou uma VM sempre ligada servem de servidor.

- [ ] Servidor Linux sem interface gráfica, acessado só por SSH
- [ ] Gitea self-hosted com Docker Compose, espelhando alguns repositórios do GitHub
- [ ] Compartilhamento NFS ou Samba montado no notebook via `fstab` com automount
- [ ] Backup do notebook para o servidor, agendado por timer, com teste de restauração
- [ ] Acesso externo seguro (VPN como WireGuard ou túnel), nunca porta aberta direto no roteador
- [ ] Monitoramento simples: saber quando o disco enche ou um container cai
- [ ] Levar o banco de dados de desenvolvimento do Aura para o servidor
- [ ] **Evidência:** repositório `homelab` com os `docker-compose.yml` (sem segredos), um diagrama da rede e um README explicando cada serviço

## Fase 9: Documentação pública, portfólio e ensino

Saber e não mostrar não conta para recrutador. Esta fase transforma o trabalho das fases anteriores em vitrine.

- [ ] README do repo de dotfiles: screenshot do desktop, o que cada pasta faz, como instalar, decisões técnicas (por que BTRFS, por que subvolumes, por que Omarchy)
- [ ] Fixar no perfil do GitHub os 3 repositórios mais fortes: dotfiles, aura-status e homelab
- [ ] Série no blog, um post por fase: instalação manual, setup do notebook, ambiente .NET no Linux, o módulo da Waybar
- [ ] Laboratório de Sistemas Operacionais para as turmas: instalação do Arch em VM com roteiro, checkpoints e critério de avaliação
- [ ] Levar o roteiro para o repositório ensino-ti e marcar como capítulo candidato do livro
- [ ] Contribuir com algo pequeno para um projeto aberto (correção no ArchWiki, issue bem escrita, PR de tema no Omarchy)
- [ ] **Evidência:** links públicos de cada item acima

## Fase 10: Currículo, LinkedIn e entrevista

Recrutador não se impressiona com "uso Arch". Impressiona-se com problema resolvido, resultado mensurável e link para conferir. Cada linha abaixo só entra quando a fase correspondente estiver fechada.

### Linhas para o currículo

- **Administração Linux:** mantenho Arch Linux como ambiente principal, com BTRFS (subvolumes e snapshots com rollback), systemd, LUKS e automação em Bash versionada em \[github.com/AlanMateus17/dotfiles\].
- **Automação de ambiente:** script que reconstrói o ambiente .NET 10 + PostgreSQL + Redis + Docker num sistema limpo em um comando.
- **Ferramenta autoral:** aura-status, CLI/TUI em C# com arquitetura de plugins, integrada à barra do sistema (Waybar) \[e publicada no AUR\].
- **Infraestrutura:** homelab com Gitea, Docker Compose, NFS, VPN e backup automatizado com restauração testada.
- **Ensino:** criei laboratório prático de instalação e administração Linux para a disciplina de Sistemas Operacionais do curso técnico.

### Tarefas

- [ ] Seção de competências só com o que você defende sem consulta: Linux (Arch), Bash, systemd, BTRFS, Docker, Git, SSH, Neovim
- [ ] Atualizar o LinkedIn: título, seção de projetos com os 3 repositórios e os posts do blog
- [ ] Ensaiar em voz alta as respostas para as perguntas da seção seguinte
- [ ] Opcional: certificação de entrada como LPI Linux Essentials ou LPIC-1 (confira preço e formato atuais no site da LPI). Ajuda a passar por filtro de RH, mas pesa menos que os repositórios

### Perguntas que você precisa responder bem

- O que acontece desde apertar o botão de ligar até aparecer a tela de login?
- O sistema não dá boot depois de uma atualização. O que você faz?
- O disco encheu. Como descobre o culpado?
- Um serviço caiu. Onde você olha primeiro?
- Qual a diferença entre snapshot e backup?
- Por que Docker direto no Linux é diferente do Docker Desktop no Windows?
- Conte um problema difícil que você resolveu no seu setup.

## Critério final de domínio

Você domina o assunto com profissionalismo quando consegue fazer tudo abaixo sem tutorial aberto:

- [ ] Instalar o Arch do zero pelo método manual em menos de 1 hora
- [ ] Recuperar um sistema que não dá boot, tanto por snapshot quanto por `arch-chroot`
- [ ] Reconstruir o notebook inteiro (sistema + ambiente .NET + configs) a partir do seu repositório em uma tarde
- [ ] Restaurar um arquivo apagado a partir do backup, não só do snapshot
- [ ] Explicar cada linha do seu `fstab`, do `hyprland.conf` e dos seus scripts
- [ ] Ensinar o laboratório de instalação para uma turma e resolver os erros dos alunos na hora
- [ ] Ter 3 repositórios públicos, documentados e com commits recentes que provam tudo isso

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🎯 Sumário Único de Estudo — O Único Arquivo Que Você Abre](../PLANO-UNICO-AMtech.md)
- [Método de Estudo — Documento Único](../../07-estudo-e-carreira/metodo-de-estudo.md)
- [🐧 Trilha Linux/Arch Profissional](../../07-estudo-e-carreira/trilha-linux-arch-profissional.md)
- [🌌 Mapa de Horizonte Longo — Sistemas, Baixo Nível e SO Próprio](../../07-estudo-e-carreira/mapa-horizonte-longo-sistemas.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
