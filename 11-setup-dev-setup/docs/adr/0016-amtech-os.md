# 0016 · AMtech OS: o setup como sistema operacional, sobre o Ubuntu

- **Status:** proposta (o Alan aceita ou ajusta ao revisar o PR)
- **Data:** 2026-11-10
- **Substitui em parte:** [ADR 0001](0001-wsl2-em-vez-de-dual-boot.md), quando o 2º NVMe chegar.

## Contexto

Hoje o código roda no Ubuntu do WSL2, dentro do Windows (ADR 0001). O Arch + Omarchy estava reservado para o 2º NVMe. O Alan quer que o dev-setup vire um sistema operacional próprio, rápido, seguro e controlado por ele, e que dê para vender: quem comprar não deveria passar pelo mesmo trabalho de configuração.

Avaliação feita nas 485 peças do ecossistema (planilha "AMtech OS: as 485 peças do setup"):

- 1 fica no Windows: Revit, Civil 3D e Robot (Autodesk educacional).
- 10 entram com atenção: NitroSense, DaVinci, ActivityWatch no Wayland, Cocos, uso do computador do Claude, app do Codex, React Native, modelos .docx da escola, voz do Claude Code e o app do Claude.
- 13 trocam de ferramenta (ShareX, Rufus, SumatraPDF, PowerToys, BitLocker, Defender, scripts .ps1...).
- 23 ficam melhores (Docker, Podman, CUDA, Ollama, Whisper, KVM, bpftrace, rotinas pelo systemd...).
- O resto é igual: roda nativo no Linux ou é web.
- Nenhuma oferta do portfólio acaba (eram 108 na avaliação; o AMtech OS é a 109ª). Assistência técnica, revenda de celulares e notebooks e automação BIM continuam precisando da partição Windows.

## Decisão

1. **Base Ubuntu LTS, não Arch e não NixOS.** O app oficial do Claude para Linux é só para Ubuntu e Debian. O `bootstrap.sh` já é Ubuntu, e a VM de produção também. O chezmoi e o mise já dão a reprodutibilidade que o NixOS daria, e duplicar isso iria contra o ADR 0008.
2. **O AMtech OS é uma camada, não um sistema escrito do zero.** Mesmo modelo do Omarchy e do Pop!_OS: a pasta `os/` deste repositório transforma um Ubuntu recém-instalado no AMtech OS (perfis, tema, segurança base, comando `amtech`, snapshots e o preparador do dev-setup).
3. **No notebook: AMtech OS no 2º NVMe, Windows intocado no SSD atual.** O ADR 0001 continua valendo no que importa: nada de reparticionar o disco do Windows. O Arch + Omarchy segue como trilha de estudo do Akita, em pendrive e VM.
4. **Testar primeiro numa VM** (os/README.md). O notebook só depois de uma semana de uso sem problema e da compra do disco.
5. **Perfis** (`dev`, `escola`, `empresa`, `seguranca`, `criador`) sobre a mesma base. São a forma de vender o mesmo sistema para públicos diferentes.
6. **Nada pessoal na camada.** Senhas no KeePassXC, finanças em `~/financas`, vault e documentos no backup. É isso que permite publicar uma edição Community.

## Consequências

- O WSL2 sai de cena quando o AMtech OS virar o sistema do dia a dia. Os scripts de `scripts/wsl` passam a valer nos dois lugares (o bootstrap já reconhece o Linux nativo).
- O Windows fica para o que só roda nele, um de cada vez no boot.
- A 0.1 não tem ISO própria: instala-se o Ubuntu oficial e roda-se `os/instalar.sh`. A ISO, o Btrfs com criptografia e o boot em snapshot vêm na 0.2.
- Venda: oferta `amtechos` no portfólio, derivada do `setuppro`. Na fila até o Alan usar o sistema por alguns meses.
- Cuidados para vender: não usar o nome nem o logo do Ubuntu ("baseado em Ubuntu" pode); publicar o código GPL que for alterado e distribuído; registrar a marca no INPI.
