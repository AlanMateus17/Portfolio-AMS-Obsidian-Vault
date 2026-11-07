# Rede própria entre os seus computadores

[← Índice da documentação](../README.md)

Objetivo: notebook, celular e os próximos computadores (servidor caseiro, workstation) conversando com segurança, de casa ou de fora, sem abrir porta no roteador.

| Camada | Ferramenta | Para quê |
|---|---|---|
| Rede privada | **Tailscale** (WireGuard por baixo) | Todos os seus aparelhos numa rede só, criptografada, com nomes (MagicDNS) e regras de quem acessa o quê (ACL) |
| Acesso | **SSH com chave** (do KeePassXC) | Entrar em qualquer máquina sem senha digitada |
| Arquivos | **Syncthing** | Pastas sincronizadas direto entre os aparelhos, sem nuvem |
| DNS | **AdGuard Home** ([compose](../../infra/rede/compose.yaml)) | Bloqueio de anúncios e rastreadores para a casa toda |
| IA | **llama.cpp RPC / exo** | Dividir um modelo grande entre os computadores da rede ([arquitetura de IA](../ia/README.md)) |
| Laboratório | **Packet Tracer / containerlab** | Treinar redes, VLANs e roteamento para Network+ e CCNA sem comprar equipamento |
| Aprender por baixo | **WireGuard na mão** | Montar um túnel entre duas máquinas sem o Tailscale, para entender o que ele faz |

## Regras de segurança

1. Nada exposto para a internet: serviços escutam em `127.0.0.1` ou só no Tailscale.
2. ACL do Tailscale: celular acessa só o que precisa; servidor não inicia conexão para o notebook.
3. Chave SSH por máquina, nunca senha; login de root desligado.
4. Pastas do Syncthing com dados pessoais só entre aparelhos seus, nunca compartilhadas.
5. Toda máquina nova entra no backup 3-2-1 e no monitoramento.
