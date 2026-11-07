# Voz

[← Jarvis](README.md)

## O caminho de um pedido falado

| Etapa | Peça | Onde roda | Observação |
|---|---|---|---|
| Acordar | microWakeWord (no satélite) ou openWakeWord com `hey_jarvis` | Satélite ESP32-S3 ou `infra/jarvis` | Comece com limiar 0,5 e suba para 0,7 no cômodo com TV, se acordar sozinho |
| Ouvir | faster-whisper, modelo `small` em pt | GPU do notebook (`infra/jarvis`); reserva na CPU do servidor | O `medium` é mais preciso e fica no limite dos 4 GB da GTX 1650 |
| Entender | Frases locais do Assist; o que não casar vai para o Claude | Servidor da casa | Ligue "preferir comandos locais": o simples nem passa pela IA |
| Decidir | Política do Jarvis | Servidor da casa | `tools/jarvis/politica.py` |
| Falar | Piper, voz `pt_BR-faber-medium` | `infra/jarvis` | Tropeça em valores, telefones e endereços; escreva respostas curtas |

Tudo isso se fala pelo protocolo Wyoming. No Home Assistant: Configurações > Dispositivos e serviços > Wyoming Protocol, um para cada porta (10300, 10200, 10400), e depois Configurações > Assistentes de voz > novo assistente com idioma Português (Brasil).

## Satélites (um por cômodo)

- **ESP32-S3** com microfone e alto-falante, gravado pelo ESPHome no navegador. A palavra de ativação roda no próprio chip.
- **Home Assistant Voice Preview Edition**: o pronto, que funciona de primeira. Confira preço e importação antes.
- **O ESP32 comum (sem S3) que você já tem** não dá conta da palavra de ativação; use-o para sensores e robôs.
- **Celular**: o app do Home Assistant já é um satélite (atalho de voz na tela inicial) e é o primeiro a testar, sem comprar nada.

## Respostas faladas no PC

O Claude Code ouve pelo `/voice`. Para ele responder em voz, o hook `tools/jarvis/falar.py` lê a última resposta, tira código, tabelas e links, corta no tamanho de uma fala e toca pelo Piper. Configuração em [PC e código](04-pc.md).

## Voz clonada?

A voz clonada da ElevenLabs (bloco `voz`) é para os vídeos e cursos, e é paga por caractere. O assistente fala com a voz local do Piper: grátis, sem internet, e ninguém confunde o Jarvis com você numa gravação.
