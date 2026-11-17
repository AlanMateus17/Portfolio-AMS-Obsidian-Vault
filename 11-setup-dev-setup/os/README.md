# AMtech OS

[← Índice da documentação](../docs/README.md) · Decisão: [ADR 0016](../docs/adr/0016-amtech-os.md)

O AMtech OS é o dev-setup virando sistema operacional: **Ubuntu LTS como base, a sua camada por cima**. É o mesmo caminho do Omarchy, que é uma camada do DHH sobre o Arch: instala-se a base oficial e depois roda-se um script.

```
AMtech OS
├── Sua camada: este repositório (perfis, tema, comando amtech, segurança, dev-setup)
└── Base: Ubuntu 24.04 ou mais novo + kernel Linux
```

Versão atual: **0.1** (camada instalável). A ISO própria vem na 0.2.

## Testar numa VM (comece por aqui)

Na VM não há risco nenhum para o Windows nem para os seus arquivos.

1. **Baixe o Ubuntu Desktop LTS** em ubuntu.com/download/desktop (26.04 LTS; 24.04 também serve).
2. **Crie a VM no VirtualBox:** Linux / Ubuntu (64-bit), 4 CPUs, 8 GB de memória, disco de 60 GB, **EFI ligado** (Sistema → Placa-mãe), vídeo VMSVGA com 128 MB.
3. **Instale o Ubuntu na VM.** Para testar os snapshots, escolha a instalação manual e formate a partição `/` como **Btrfs** (com uma partição EFI de 1 GB em FAT32). Com o padrão (ext4) tudo funciona, menos os snapshots.
4. **No terminal da VM**, traga o dev-setup (o repositório é privado, então o login no GitHub vem antes):
   ```
   sudo apt install -y git gh
   gh auth login
   gh repo clone AlanMateus17/dev-setup ~/dev/dev-setup
   cd ~/dev/dev-setup
   ```
5. **Veja o que ele faria**, sem mudar nada:
   ```
   bash os/instalar.sh --simular
   ```
6. **Instale de verdade:**
   ```
   bash os/instalar.sh --perfil dev --nome "Alan Mateus" --email SEU_EMAIL
   ```
7. **Saia e entre de novo na sessão** e rode `amtech`.

Anote no vault o que faltou ou incomodou durante uma semana de uso. É isso que vira a 0.2.

## Perfis

| Perfil | Para quem | Traz |
|---|---|---|
| `dev` (padrão) | Você e quem programa | Base + Docker, Podman, KVM, Neovim e o preparador do dev-setup (.NET, Node, Python, Claude Code, ai-jail...) |
| `escola` | Laboratório de informática | Base + LibreOffice, Thonny, Okular |
| `empresa` | Pequenos negócios | Base + LibreOffice, backup (Déjà Dup), acesso remoto (Remmina) |
| `seguranca` | Estudo de pentest | Base + nmap, Wireshark, Lynis, rkhunter, USBGuard (desligado), KVM e o dev-setup |
| `criador` | Conteúdo | Base + OBS, Kdenlive, Audacity, Krita, Inkscape, ffmpeg |

A base de todo perfil: Git, GitHub CLI, KeePassXC, Syncthing, Flameshot, Zathura, firewall, atualização de segurança diária, SMART e sensores. As listas estão em [`perfis/`](perfis/): um pacote por linha.

## O que o instalador faz

1. Confere se é Ubuntu 24.04 ou mais novo, e recusa o WSL (lá vale o `scripts/wsl/bootstrap.sh`).
2. Instala os pacotes do perfil, pulando com aviso o que não existir na versão.
3. Driver da NVIDIA, só com `--com-nvidia` e só em máquina de verdade.
4. Firewall (bloqueia entrada, libera saída) e atualização de segurança diária.
5. Seu usuário no grupo `docker`.
6. Snapshots com o snapper, se a raiz for Btrfs, e o primeiro ponto de volta.
7. Identidade: `/etc/amtech-release`, papel de parede, padrões do GNOME (tema escuro, Fira Code, 4 áreas de trabalho, privacidade), mensagem no terminal e o comando `amtech`.
8. Nos perfis `dev` e `seguranca`, roda o preparador do dev-setup.

Não mexe em disco nem em partição. Os padrões do GNOME são só padrões: o que você mudar nas Configurações vale por cima.

## O comando `amtech`

| Comando | O que faz |
|---|---|
| `amtech` | Estado: versão, disco, memória, snapshots, firewall, Docker, GPU, atualizações, dev-setup |
| `amtech saude` | SMART dos discos, temperatura e capacidade da bateria |
| `amtech atualizar` | Snapshot antes (se Btrfs), atualiza o sistema e puxa o dev-setup |
| `amtech snapshots` | Lista os pontos de volta |
| `amtech sobre` | Versão, perfil e base |

## Voltar atrás

Com a raiz em Btrfs, cada `amtech atualizar` cria um snapshot antes. Para desfazer as mudanças de arquivos feitas depois do snapshot N:

```
sudo snapper -c root list
sudo snapper -c root undochange N..0
```

Bootar direto num snapshot pelo menu do GRUB fica para a 0.2.

## No notebook de verdade (depois da VM)

- **Só no 2º NVMe.** O Windows fica intocado no SSD atual, como o ADR 0001 exige. Na instalação, confira duas vezes o disco escolhido.
- **Secure Boot pode ficar ligado:** o Ubuntu dá boot com ele. O driver da NVIDIA pede para cadastrar uma chave (MOK) no próximo boot: anote a senha que ele pedir.
- **Criptografia ou snapshots:** se o instalador não oferecer Btrfs e criptografia juntos, num notebook escolha a **criptografia**. Notebook roubado com disco aberto é pior que ficar sem snapshot. A 0.2 junta os dois.
- **USBGuard** (perfil `seguranca`) vem desligado. Ligar sem cadastrar teclado e mouse trava a máquina. Para ligar, com tudo o que você usa já conectado:
  ```
  sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf' && sudo chmod 0600 /etc/usbguard/rules.conf
  sudo systemctl enable --now usbguard
  ```

## Próximas versões

| Versão | O que entra |
|---|---|
| 0.2 | ISO própria com o instalador; Btrfs com criptografia; boot em snapshot pelo GRUB; tela de boot e de login com a marca |
| 0.3 | Sentinela: saúde do hardware com histórico, Lynis, AIDE, OpenSnitch, relatório semanal |
| 0.4 | Central AMtech (painel gráfico) e assistente de primeiro boot |
| 1.0 | Edição Community pública, sem nada pessoal |
