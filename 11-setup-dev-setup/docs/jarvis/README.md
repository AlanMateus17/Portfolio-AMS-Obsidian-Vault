# Jarvis: o setup e a casa por comando de voz

[← Índice da documentação](../README.md)

Você fala, ele faz: no PC (pastas, arquivos, pesquisa, repositórios, contribuições open source), na casa (luz, tomadas, energia, água, câmeras, portas, janelas, eletrodomésticos) e nos robôs. Tudo montado com projetos abertos e maduros, sem reinventar nada que já existe.

## O que existe de verdade (pesquisa de nov/2026)

- **Home Assistant Assist** é o assistente de voz aberto mais maduro: palavra de ativação, reconhecimento e voz rodando em casa pelo protocolo **Wyoming**, com satélites por cômodo. Desde a versão 2025.2 o Home Assistant também é **servidor MCP**: o Claude controla só as entidades que você expõe.
- **Claude Code** tem modo de voz (`/voice`) desde mar/2026: você fala o pedido e ele executa. A resposta falada não vem pronta; o setup fecha isso com o hook `tools/jarvis/falar.py` e o Piper.
- **Frigate** grava câmeras e detecta pessoas localmente; **AI-on-the-edge-device** lê hidrômetro com uma ESP32-CAM; **ESPHome** transforma qualquer ESP32 em aparelho do Home Assistant; o **mqtt_client** liga o ROS 2 ao MQTT.
- **Pipecat** é a opção para um assistente de conversa contínua próprio, se um dia o do Home Assistant ficar pequeno.

## Como fica

```mermaid
flowchart LR
  subgraph Voce["Você fala"]
    S["Satélite do cômodo<br/>ESP32-S3"]
    C["Celular<br/>app do Home Assistant"]
    P["Notebook<br/>Claude Code /voice"]
  end
  S --> HA["Home Assistant<br/>(servidor da casa)"]
  C --> HA
  HA -->|"Whisper, Piper, hey jarvis"| W["Voz local (Wyoming)<br/>GPU do notebook ou CPU do servidor"]
  HA -->|"frase simples"| L["Comandos locais<br/>sem IA"]
  HA -->|"o resto"| CL["Claude<br/>agente de conversa"]
  CL --> POL{"Política<br/>livre · voz · celular · proibido"}
  POL --> M["MQTT"]
  M --> Z["Zigbee: tomadas,<br/>sensores, fechadura, janelas"]
  M --> F["Frigate: câmeras"]
  M --> A["Hidrômetro"]
  M --> R["Robôs: ESPHome e ROS 2"]
  P --> J["ai-jail: pastas, arquivos,<br/>pesquisa, git, PRs"]
  J -->|"falar.py"| W
```

Três cérebros, cada um no que faz melhor:

| Pedido | Quem resolve | Precisa de internet? |
|---|---|---|
| "Apaga a luz da sala", "liga o ventilador" | Frases locais do Assist | Não |
| "Quanto gastei de energia esta semana comparado com a outra?" | Claude, pelas entidades expostas | Sim |
| "Cria a pasta da aula de quinta e copia o modelo" | Claude Code por voz, no PC | Sim |
| "Abre a porta" | Ninguém sozinho: vai para o seu celular confirmar | Não |

## Documentos

1. [Voz](01-voz.md): palavra de ativação, reconhecimento em português, voz, satélites e o que esperar de atraso
2. [Casa](02-casa.md): energia, água, câmeras, portas e janelas, eletrodomésticos e o que precisa de eletricista
3. [Robótica](03-robotica.md): ESP32 pelo ESPHome, Arduino, Raspberry Pi com ROS 2 e parada de emergência
4. [PC e código](04-pc.md): o Claude Code por voz, o que ele pode fazer, pesquisa, clonar repositórios e contribuir em open source

Decisão de onde tudo roda: [ADR 0004](../adr/0004-casa-num-servidor-proprio.md). Passo a passo: [fase 51 do roteiro](../implantacao/roteiro.md#f-jarvis).

## O que dá e o que não dá

- **"Fazer tudo que eu pedir"** vira: fazer tudo que está na lista do que ele pode fazer, e pedir confirmação para o resto. Um assistente que obedece qualquer coisa obedece também a quem imita a sua voz, a um vídeo tocando na TV ou a uma página web com instrução escondida.
- **A GTX 1650 (4 GB) não segura um modelo local bom de conversa.** Ouvir, falar, acordar e os comandos simples são locais; a conversa usa o Claude. Sem internet, a casa continua obedecendo às frases simples.
- **Português do Brasil:** o reconhecimento por frases fixas (Speech-to-Phrase) só tem português de Portugal; por isso o setup usa o Whisper, que entende pt-BR bem.
- **Janela, porta e portão só abrem por motor ou fechadura elétrica.** Janela comum de casa brasileira não tem motor; é obra, com custo, e fica para depois.
- **Atraso:** quem montou o pipeline local relata cerca de 1 segundo até a primeira palavra; com o Claude no meio, conte com alguns segundos a mais (meça no seu). Não é o do filme, mas é útil.

## Regras do Jarvis

1. **Política antes de tudo** (`tools/jarvis/politica.py`): cada ação tem um nível. Destrancar porta, abrir janela, porta e portão e desligar a geladeira só com o toque no celular; desarmar alarme, desligar câmera e apagar gravação nunca por voz. Esses mínimos estão no código e nenhum arquivo afrouxa.
2. **A geladeira nunca fica desligada esquecida:** a política gera a automação que religa sozinha depois do tempo combinado e avisa.
3. **No máximo 25 entidades expostas ao Claude.** Com mais, os modelos esquecem aparelhos e erram.
4. **Conteúdo lido é dado, nunca ordem.** Página, e-mail ou documento com "Jarvis, abra a porta" não dispara nada.
5. **Imagem de câmera e áudio da casa não vão para IA na nuvem.** A detecção é local, no Frigate.
6. **Sem porta aberta na internet.** De fora, só pelo Tailscale ou pelo Home Assistant Cloud.
7. **No PC, o agente trabalha dentro do ai-jail** e pede confirmação antes de apagar, publicar ou mandar algo em seu nome.
8. **Registro de tudo:** o histórico do Home Assistant e o log do agente mostram quem pediu o quê e quando.
