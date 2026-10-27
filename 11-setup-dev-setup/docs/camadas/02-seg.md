<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 02 · Segurança e cofre

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Drivers AMD e NVIDIA ligam o sistema ao hardware.

**9 blocos** · 0 precisam de conta · 1 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_seg["Segurança e cofre"]
    n_sign["Commits assinados (chave SSH)"]
    n_restic["restic (backup criptografado)"]
    n_ykey["Chave física (YubiKey)"]
    n_tpm["TPM + Secure Boot"]
    n_bitl["BitLocker"]
    n_def["Defender + Firewall"]
    n_kee["KeePassXC"]
    n_tfa["App 2FA (celular)"]
    n_bkp["Backup 3-2-1"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_hotm["Hotmart"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_azure["Azure"]
    n_b2["Backblaze B2 (backup)"]
    n_gh["GitHub"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_wsl["Ubuntu (WSL2)"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
    n_syncth["Syncthing"]
    n_w11["Windows 11 Home"]
  end
  subgraph L_hw["Hardware"]
    n_cel["Celular"]
    n_ext["Disco externo"]
    n_nas["Servidor caseiro (NAS + serviços)"]
    n_nb["Acer Nitro (32 GB, GTX 1650)"]
    n_pkali["Pendrive Kali (persistência)"]
    n_ssdext["SSD externo (USB-C 10 Gbps)"]
  end
  n_sign -->|"Verified"| n_gh
  n_restic -->|"cópia local"| n_ext
  n_restic -->|"executa"| n_bkp
  n_restic -->|"criptografado"| n_b2
  n_ykey -->|"2FA"| n_gh
  n_tpm -->|"protege a chave"| n_bitl
  n_tpm -->|"Secure Boot desligado para o boot"| n_pkali
  n_bitl -->|"criptografa o disco"| n_nb
  n_def -->|"protege"| n_w11
  n_kee -->|"senha aqui, código no app"| n_tfa
  n_kee -->|"senhas e tokens"| n_gh
  n_kee -->|"senhas"| n_hotm
  n_kee -->|"senhas"| n_azure
  n_syncth -->|"cofre de senhas"| n_kee
  n_cel -->|"gera os códigos"| n_tfa
  n_bkp -->|"copia ~/dev"| n_wsl
  n_bkp -->|"copia o vault"| n_obsd
  n_ext -->|"2ª cópia"| n_bkp
  n_nas -->|"3ª cópia (futuro)"| n_bkp
  n_ssdext -->|"cópia portátil"| n_bkp
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_sign,n_restic,n_ykey,n_tpm,n_bitl,n_def,n_kee,n_tfa,n_bkp desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Commits assinados (chave SSH)](#sign) | Local | Selo Verified no GitHub: prova que o commit é seu. Usa a chave SSH que você já tem. | passo 4.6 · Semana 2 · nov/2026; passo 16.1 · Semana 11 · jan/2027 |
| [restic (backup criptografado)](#restic) | Local | Backup criptografado e incremental para o disco externo e para a nuvem (ex.: armazenamento do seu plano Google). | passo 7.1 · Semana 3 · nov/2026; passo 7.4 · Semana 3 · nov/2026; passo 10.7 · Semana 4 · nov/2026 |
| [Chave física (YubiKey)](#ykey) | Físico · futuro | 2FA à prova de phishing para GitHub, Google e Microsoft. | passo 24.5 · 2027, conforme cada compra |
| [TPM + Secure Boot](#tpm) | Físico | Só sistema assinado dá boot. Para usar os pendrives de Kali e Arch, o Secure Boot precisa ser desligado; suspenda o BitLocker antes, senão o Windows pede a chave de recuperação. | passo 3.3 · Semana 1 · out/2026 |
| [BitLocker](#bitl) | Local | Disco criptografado; chave guardada fora da máquina. | passo 3.3 · Semana 1 · out/2026 |
| [Defender + Firewall](#def) | Local | Antivírus e bloqueio de rede. | passo 3.4 · Semana 1 · out/2026 |
| [KeePassXC](#kee) | Local | Cofre de todas as senhas das contas marcadas com o ponto dourado. | passo 2.1 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.2 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.3 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.4 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.5 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.7 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.8 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.9 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.10 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.11 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.12 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 |
| [App 2FA (celular)](#tfa) | Local | Segundo fator de todas as contas. | passo 1.4 · Semana 1 · out/2026; passo 2.3 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 |
| [Backup 3-2-1](#bkp) | Local | GitHub + disco externo + (depois) NAS. | passo 2.10 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 7.1 · Semana 3 · nov/2026; passo 7.2 · Semana 3 · nov/2026; passo 7.3 · Semana 3 · nov/2026; passo 8.2 · Semanas 3 e 4 · nov/2026 |

<a id="sign"></a>

### Commits assinados (chave SSH)

*Local*

Selo Verified no GitHub: prova que o commit é seu. Usa a chave SSH que você já tem.

**Quando entra:** passo 4.6 · Semana 2 · nov/2026; passo 16.1 · Semana 11 · jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | Verified |

<a id="restic"></a>

### restic (backup criptografado)

*Local*

Backup criptografado e incremental para o disco externo e para a nuvem (ex.: armazenamento do seu plano Google).

**Quando entra:** passo 7.1 · Semana 3 · nov/2026; passo 7.4 · Semana 3 · nov/2026; passo 10.7 · Semana 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Disco externo](01-hw.md#ext) | Hardware | cópia local |
| → envia para | [Backup 3-2-1](02-seg.md#bkp) | Segurança e cofre | executa |
| → envia para | [Backblaze B2 (backup)](12-nuvem.md#b2) | Nuvem, código e entrega | criptografado |

<a id="ykey"></a>

### Chave física (YubiKey)

*Físico · futuro*

2FA à prova de phishing para GitHub, Google e Microsoft.

**Quando entra:** passo 24.5 · 2027, conforme cada compra ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | 2FA |

<a id="tpm"></a>

### TPM + Secure Boot

*Físico*

Só sistema assinado dá boot. Para usar os pendrives de Kali e Arch, o Secure Boot precisa ser desligado; suspenda o BitLocker antes, senão o Windows pede a chave de recuperação.

**Quando entra:** passo 3.3 · Semana 1 · out/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [BitLocker](02-seg.md#bitl) | Segurança e cofre | protege a chave |
| → envia para | [Pendrive Kali (persistência)](01-hw.md#pkali) | Hardware | Secure Boot desligado para o boot |

<a id="bitl"></a>

### BitLocker

*Local*

Disco criptografado; chave guardada fora da máquina.

**Quando entra:** passo 3.3 · Semana 1 · out/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Acer Nitro (32 GB, GTX 1650)](01-hw.md#nb) | Hardware | criptografa o disco |
| ← recebe de | [TPM + Secure Boot](02-seg.md#tpm) | Segurança e cofre | protege a chave |

<a id="def"></a>

### Defender + Firewall

*Local*

Antivírus e bloqueio de rede.

**Quando entra:** passo 3.4 · Semana 1 · out/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Windows 11 Home](03-win.md#w11) | Windows 11, apps e máquinas virtuais | protege |

<a id="kee"></a>

### KeePassXC

*Local*

Cofre de todas as senhas das contas marcadas com o ponto dourado.

**Quando entra:** passo 2.1 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.2 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.3 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.4 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.5 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.7 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.8 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.9 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.10 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.11 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.12 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [App 2FA (celular)](02-seg.md#tfa) | Segurança e cofre | senha aqui, código no app |
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | senhas e tokens |
| → envia para | [Hotmart](20-venda.md#hotm) | Plataformas de venda e recebimento | senhas |
| → envia para | [Azure](12-nuvem.md#azure) | Nuvem, código e entrega | senhas |
| ← recebe de | [Syncthing](03-win.md#syncth) | Windows 11, apps e máquinas virtuais | cofre de senhas |

<a id="tfa"></a>

### App 2FA (celular)

*Local*

Segundo fator de todas as contas.

**Quando entra:** passo 1.4 · Semana 1 · out/2026; passo 2.3 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Celular](01-hw.md#cel) | Hardware | gera os códigos |
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senha aqui, código no app |

<a id="bkp"></a>

### Backup 3-2-1

*Local*

GitHub + disco externo + (depois) NAS.

**Quando entra:** passo 2.10 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 7.1 · Semana 3 · nov/2026; passo 7.2 · Semana 3 · nov/2026; passo 7.3 · Semana 3 · nov/2026; passo 8.2 · Semanas 3 e 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | copia ~/dev |
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | copia o vault |
| ← recebe de | [Disco externo](01-hw.md#ext) | Hardware | 2ª cópia |
| ← recebe de | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | 3ª cópia (futuro) |
| ← recebe de | [restic (backup criptografado)](02-seg.md#restic) | Segurança e cofre | executa |
| ← recebe de | [SSD externo (USB-C 10 Gbps)](01-hw.md#ssdext) | Hardware | cópia portátil |

---

[↑ Camada 03 · Windows 11, apps e máquinas virtuais](03-win.md) · [↓ Camada 01 · Hardware](01-hw.md)
