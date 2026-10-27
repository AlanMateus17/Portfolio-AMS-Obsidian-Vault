# 0001 · WSL2 em vez de dual boot no disco atual

- **Status:** aceita
- **Data:** 2026-10-19

## Contexto

O notebook tem um único SSD de 1 TB com Windows 11 Home. O plano original previa dual boot com Linux e uma partição NTFS compartilhada. O disco já foi perdido uma vez (agosto de 2026), e o WSL2 com Ubuntu e Docker já funciona.

## Decisão

Todo o desenvolvimento roda no Ubuntu do WSL2, com o código em `~/dev` (ext4). O Windows fica só com apps gráficos, drivers e segurança. O Arch Linux entra depois, num segundo NVMe com boot próprio, sem tocar no disco do Windows. Kali, Ubuntu Server e Windows Server rodam em máquinas virtuais.

## Consequências

- Git, Docker e .NET rodam no sistema de arquivos nativo do Linux, sem a lentidão e os problemas de permissão do NTFS.
- Nenhum reparticionamento: risco zero de perder o Windows de novo.
- O Arch fica para quando houver o segundo disco; até lá, é treinado em VM.
- VMs no Windows Home usam a plataforma de hipervisor do Windows e ficam um pouco mais lentas com o WSL2 ligado.
