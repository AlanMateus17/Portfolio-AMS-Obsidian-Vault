<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 04 · Linux (Ubuntu no WSL2, Arch no 2º disco)

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O código fica no ext4 do Linux; o Windows enxerga pela ponte do WSL2.

**9 blocos** · 0 precisam de conta · 2 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_nvim["Neovim"]
    n_netw["nmap · dig · curl"]
    n_wsl["Ubuntu (WSL2)"]
    n_git["Git + SSH + gh"]
    n_rt[".NET 10 · Node · Python"]
    n_tex["TeX Live"]
    n_sec["gitleaks · Trivy"]
    n_dot["dotfiles"]
    n_arch["Arch + Omarchy (2º NVMe)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_overif["Verificadores"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bci["Pipeline do livro (CI)"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gh["GitHub"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_api["API ASP.NET Core"]
    n_status["aura-status"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
  end
  subgraph L_dados["Dados e treino de IA"]
    n_pyds["Python de dados (Polars, Jupyter)"]
    n_torch["PyTorch + CUDA (WSL2)"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_cc["Claude Code"]
    n_jail["ai-jail"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_boot["Gerenciador de boot"]
    n_vms["VMs: Kali · Arch · Servidores"]
    n_vsc["VS Code"]
    n_w11["Windows 11 Home"]
    n_wslcfg[".wslconfig + localhost"]
    n_wterm["Terminal · PowerShell · winget"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_bkp["Backup 3-2-1"]
  end
  subgraph L_hw["Hardware"]
    n_nvme["2º NVMe (1–4 TB)"]
    n_parch["Pendrive Arch (instalação portátil)"]
  end
  n_nvim -->|"editor"| n_wsl
  n_netw -->|"diagnóstico"| n_vms
  n_wsl -->|"terminal"| n_git
  n_wsl -->|"executa"| n_rt
  n_wsl -->|"socket da engine"| n_docker
  n_wsl -->|"CUDA no WSL2"| n_torch
  n_bkp -->|"copia ~/dev"| n_wsl
  n_w11 -->|"WSL2"| n_wsl
  n_vsc -->|"Remote – WSL"| n_wsl
  n_jail -->|"só ~/dev/#lt;projeto#gt;"| n_wsl
  n_wslcfg -->|"limite de RAM"| n_wsl
  n_wterm -->|"abre o Ubuntu"| n_wsl
  n_overif -->|"confere"| n_wsl
  n_git -->|"push via SSH"| n_gh
  n_sec -->|"pre-commit"| n_git
  n_status -->|"git status"| n_git
  n_cc -->|"commit com sua revisão"| n_git
  n_rt -->|"compila e roda"| n_api
  n_rt -->|"Python + uv"| n_pyds
  n_tex -->|"compila o PDF"| n_bci
  n_dot -->|"versionado"| n_gh
  n_dot -->|"mesmos dotfiles"| n_parch
  n_arch -->|"mesmos dotfiles"| n_dot
  n_nvme -->|"disco próprio"| n_arch
  n_boot -->|"boot"| n_arch
  n_parch -->|"treino antes do 2º NVMe"| n_arch
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_nvim,n_netw,n_wsl,n_git,n_rt,n_tex,n_sec,n_dot,n_arch desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Neovim](#nvim) | Local · futuro | Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo. | passo 24.2 · 2027, conforme cada compra |
| [nmap · dig · curl](#netw) | Local | Diagnóstico de rede no Ubuntu: portas, DNS e requisições HTTP. Instalados pelo bootstrap.sh. | passo 4.4 · Semana 2 · nov/2026 |
| [Ubuntu (WSL2)](#wsl) | Local | Onde o código vive e roda. | passo 4.1 · Semana 2 · nov/2026; passo 4.5 · Semana 2 · nov/2026 |
| [Git + SSH + gh](#git) | Local | Versionamento e acesso ao GitHub. | passo 4.4 · Semana 2 · nov/2026; passo 4.6 · Semana 2 · nov/2026 |
| [.NET 10 · Node · Python](#rt) | Local | Runtimes das APIs, do front e dos scripts. | passo 4.4 · Semana 2 · nov/2026 |
| [TeX Live](#tex) | Local | Compila o livro e as apostilas. | passo 4.4 · Semana 2 · nov/2026 |
| [gitleaks · Trivy](#sec) | Local | Barra senha no commit e acha vulnerabilidades em imagens. | passo 4.4 · Semana 2 · nov/2026 |
| [dotfiles](#dot) | Local | Configuração versionada do ambiente. | passo 4.7 · Semana 2 · nov/2026 |
| [Arch + Omarchy (2º NVMe)](#arch) | Local · futuro | Linux nativo com boot próprio, sem tocar no Windows. Antes dele, o Arch portátil em pendrive ou SSD USB. | passo 24.1 · 2027, conforme cada compra |

<a id="nvim"></a>

### Neovim

*Local · futuro*

Editor de terminal da trilha Arch e Akita. Aprender aos poucos; não substitui o VS Code no começo.

**Quando entra:** passo 24.2 · 2027, conforme cada compra ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |

<a id="netw"></a>

### nmap · dig · curl

*Local*

Diagnóstico de rede no Ubuntu: portas, DNS e requisições HTTP. Instalados pelo bootstrap.sh.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [VMs: Kali · Arch · Servidores](03-win.md#vms) | Windows 11, apps e máquinas virtuais | diagnóstico |

<a id="wsl"></a>

### Ubuntu (WSL2)

*Local*

Onde o código vive e roda.

**Quando entra:** passo 4.1 · Semana 2 · nov/2026; passo 4.5 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| → envia para | [.NET 10 · Node · Python](04-lin.md#rt) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |
| → envia para | [Docker + Compose](09-cnt.md#docker) | Containers, Kubernetes e infra como código | socket da engine |
| → envia para | [PyTorch + CUDA (WSL2)](06-dados.md#torch) | Dados e treino de IA | CUDA no WSL2 |
| ← recebe de | [Backup 3-2-1](02-seg.md#bkp) | Segurança e cofre | copia ~/dev |
| ← recebe de | [Windows 11 Home](03-win.md#w11) | Windows 11, apps e máquinas virtuais | WSL2 |
| ← recebe de | [VS Code](03-win.md#vsc) | Windows 11, apps e máquinas virtuais | Remote – WSL |
| ← recebe de | [ai-jail](05-ia.md#jail) | Agentes de IA e sandbox | só ~/dev/<projeto> |
| ← recebe de | [Neovim](04-lin.md#nvim) | Linux (Ubuntu no WSL2, Arch no 2º disco) | editor |
| ← recebe de | [.wslconfig + localhost](03-win.md#wslcfg) | Windows 11, apps e máquinas virtuais | limite de RAM |
| ← recebe de | [Terminal · PowerShell · winget](03-win.md#wterm) | Windows 11, apps e máquinas virtuais | abre o Ubuntu |
| ← recebe de | [Verificadores](23-oper.md#overif) | Operação do grupo (esteira, marca, qualidade) | confere |

<a id="git"></a>

### Git + SSH + gh

*Local*

Versionamento e acesso ao GitHub.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026; passo 4.6 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | push via SSH |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | terminal |
| ← recebe de | [gitleaks · Trivy](04-lin.md#sec) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |
| ← recebe de | [aura-status](11-app.md#status) | Aplicação: sistemas AM (Aura) | git status |
| ← recebe de | [Claude Code](05-ia.md#cc) | Agentes de IA e sandbox | commit com sua revisão |

<a id="rt"></a>

### .NET 10 · Node · Python

*Local*

Runtimes das APIs, do front e dos scripts.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](11-app.md#api) | Aplicação: sistemas AM (Aura) | compila e roda |
| → envia para | [Python de dados (Polars, Jupyter)](06-dados.md#pyds) | Dados e treino de IA | Python + uv |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | executa |

<a id="tex"></a>

### TeX Live

*Local*

Compila o livro e as apostilas.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Pipeline do livro (CI)](15-editora.md#bci) | Editora AMS Silva (produção de livros) | compila o PDF |

<a id="sec"></a>

### gitleaks · Trivy

*Local*

Barra senha no commit e acha vulnerabilidades em imagens.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | pre-commit |

<a id="dot"></a>

### dotfiles

*Local*

Configuração versionada do ambiente.

**Quando entra:** passo 4.7 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | versionado |
| → envia para | [Pendrive Arch (instalação portátil)](01-hw.md#parch) | Hardware | mesmos dotfiles |
| ← recebe de | [Arch + Omarchy (2º NVMe)](04-lin.md#arch) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |

<a id="arch"></a>

### Arch + Omarchy (2º NVMe)

*Local · futuro*

Linux nativo com boot próprio, sem tocar no Windows. Antes dele, o Arch portátil em pendrive ou SSD USB.

**Quando entra:** passo 24.1 · 2027, conforme cada compra ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [dotfiles](04-lin.md#dot) | Linux (Ubuntu no WSL2, Arch no 2º disco) | mesmos dotfiles |
| ← recebe de | [2º NVMe (1–4 TB)](01-hw.md#nvme) | Hardware | disco próprio |
| ← recebe de | [Gerenciador de boot](03-win.md#boot) | Windows 11, apps e máquinas virtuais | boot |
| ← recebe de | [Pendrive Arch (instalação portátil)](01-hw.md#parch) | Hardware | treino antes do 2º NVMe |

---

[↑ Camada 05 · Agentes de IA e sandbox](05-ia.md) · [↓ Camada 03 · Windows 11, apps e máquinas virtuais](03-win.md)
