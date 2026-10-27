<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Decisões: o que entra de outro jeito e o que fica de fora

[← Índice da documentação](README.md)

Nada do planejamento foi retirado. Os quatro primeiros entram por outro caminho, com passo e data no [roteiro](implantacao/roteiro.md); os outros são decisões suas ou de segurança, e voltam se você mudar de ideia.

| Item | Decisão |
|---|---|
| Dual boot no SSD atual | Não no SSD do Windows, pelo risco de perder dados. O Arch entra do mesmo jeito: em pendrive agora e no 2º NVMe, com boot próprio, quando você comprar o disco (fase Linux nativo do roteiro). |
| Kali como sistema principal | Kali é caixa de ferramentas de pentest, não ambiente de dev. Ele entra em pendrive com persistência e em VM (fases Dados, IA e pendrives e Linux nativo). |
| Treinar um 8B na GTX 1650 | A placa tem 4 GB e o QLoRA de 8B pede 6 GB. O treino entra pelo Kaggle e por GPU alugada em 2027, e em casa quando a workstation com GPU chegar (fase Infraestrutura própria). |
| Mobile nativo (Kotlin, Swift, Flutter) | Abriria outra stack. O app mobile entra em 2028 com .NET MAUI, na mesma linguagem do Aura (fase Distribuído, plataforma e segunda nuvem). |
| OpenClaw | Histórico sério de instâncias expostas e execução de código não confiável. |
| Bun, Hono, Rust, Tauri, gRPC | Rejeitados por você para o Aura. |
| Postman, IDEs pagas, SaaS pagos | Você prefere open source; Bruno, DBeaver e VS Code cobrem. |
