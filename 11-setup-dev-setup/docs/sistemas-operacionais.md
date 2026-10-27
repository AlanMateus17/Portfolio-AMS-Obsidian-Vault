<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Sistemas operacionais

[← Índice da documentação](README.md)

Arch e Kali entram, mas sem dual boot no disco atual: Arch no segundo NVMe, o resto em VMs.

| Sistema | Origem | Fase | Onde roda | Por quê |
|---|---|---|---|---|
| **Windows 11 Home** | Já instalado | Instalado | SSD atual (NVMe 1) | Host do dia a dia: apps com janela, GPU, drivers. Também é o que a maioria das empresas usa no notebook do dev .NET. |
| **Ubuntu no WSL2** | Já instalado | Instalado | Dentro do Windows | Onde o código roda. Ubuntu é o Linux mais comum em servidores e containers, então é o que mais aparece em vaga. |
| **Arch Linux + Omarchy** | Seu plano (estilo Akita) | 3 a 12 meses | Pendrive ou SSD USB agora; segundo NVMe depois | Primeiro a instalação manual pelo ArchWiki num pendrive ou SSD USB, portátil e sem tocar no Windows; depois no segundo NVMe com boot próprio. Ensina Linux por dentro e vira destaque no currículo. |
| **Kali Linux** | Trilha de segurança | 3 a 12 meses | Pendrive com persistência e VM (VirtualBox) | Caixa de ferramentas de pentest, não sistema do dia a dia. No pendrive você leva o Kali para qualquer máquina sua; na VM você monta laboratório com alvos (Metasploitable, Juice Shop). Sempre só contra alvos seus ou autorizados. Entra com Security+ e eJPT. |
| **Secure Boot e BitLocker** | Antes de dar boot num pendrive | Decisão sua | Firmware do Nitro (tecla F2) e menu de boot (F12) | Kali e a ISO oficial do Arch não dão boot com o Secure Boot ligado. Desligar o Secure Boot muda o que o TPM mede, e o Windows pede a chave de recuperação do BitLocker. Antes: suspenda o BitLocker (manage-bde -protectors -disable C:) e tenha a chave no KeePassXC. Depois: religue o Secure Boot e reative (manage-bde -protectors -enable C:). |
| **Ubuntu Server / Debian** | Homelab | Próximos 3 meses | VM agora, NAS ou PC velho depois | Servidor sem interface, só SSH. É onde você treina deploy de verdade, proxy reverso, firewall e backup. |
| **Windows Server (avaliação)** | Sugestão | Depois de 12 meses | VM | Active Directory está em quase toda empresa grande e é o alvo principal em pentest corporativo (OSCP cobra AD). A versão de avaliação é gratuita por tempo limitado. |
| **RHEL / Rocky Linux** | Sugestão | Depois de 12 meses | VM | Linux corporativo de banco, governo e indústria. Vale conhecer o básico (dnf, SELinux, systemd) depois de dominar Ubuntu. |
