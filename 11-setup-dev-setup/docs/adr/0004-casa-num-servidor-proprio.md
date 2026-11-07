# 0004 · A casa roda num servidor próprio, ligado o tempo todo; o notebook só empresta a GPU para a voz

- **Status:** aceita
- **Data:** 2026-11-02

## Contexto

Hoje o Home Assistant está em `infra/casa`, no Docker do WSL do notebook, preso em 127.0.0.1. Para o Jarvis controlar a casa por voz isso não serve:

- O notebook sai de casa (escola) e desliga; a casa pararia junto, inclusive as automações de segurança (religar a geladeira, avisos de porta aberta).
- O WSL2 fica atrás de uma rede própria (NAT): a descoberta de aparelhos na rede de casa (mDNS) e o acesso a pendrive USB (coordenador Zigbee) ficam difíceis.
- A VM grátis da Oracle está na nuvem: não alcança a rede de casa sem túnel e não deve receber o controle da porta de casa.

A voz tem o problema contrário: reconhecer fala com Whisper é pesado para a CPU de um Raspberry Pi, e a GTX 1650 do notebook faz isso rápido.

## Decisão

1. **Servidor da casa:** um mini PC Intel N100 (preferido) ou um Raspberry Pi 5, ligado no nobreak, com **Home Assistant OS**. Nele ficam os complementos (add-ons): Mosquitto (MQTT), Zigbee2MQTT, ESPHome, Frigate (câmeras, pelo repositório de add-ons do próprio Frigate) e um Whisper pequeno na CPU como reserva, além das integrações Model Context Protocol Server e Anthropic (o Claude como agente de conversa).
2. **Notebook:** quando está em casa, oferece pelo protocolo Wyoming o Whisper na GPU, o Piper e o openWakeWord (`infra/jarvis/compose.yaml`). O assistente de voz do Home Assistant usa o do notebook e, se ele estiver fora, cai para o da CPU do servidor.
3. **O que decide tudo:** comando simples de casa ("apaga a luz") é resolvido pelas frases locais do Home Assistant, sem IA. O resto vai para o Claude, que vê só as entidades expostas e passa pela política do Jarvis (`tools/jarvis/politica.py`).
4. **Sem porta aberta para a internet.** Acesso de fora só pelo Tailscale (já no setup) ou pelo Home Assistant Cloud; nunca redirecionamento de porta no roteador.
5. O `infra/casa` continua no notebook para o Paperless e o Grocy; o Home Assistant dele vira o de testes.

## Consequências

- A casa funciona com o notebook desligado; só a voz fica um pouco mais lenta.
- Uma compra a mais (o servidor) e mais um aparelho para manter atualizado, com backup automático do Home Assistant para o restic.
- O modelo de IA local que caberia na GTX 1650 (4 GB) é fraco para conversa; por isso o cérebro da conversa é o Claude, e o que é local é ouvir, falar, acordar e os comandos simples. Sem internet, a casa continua obedecendo aos comandos simples.
