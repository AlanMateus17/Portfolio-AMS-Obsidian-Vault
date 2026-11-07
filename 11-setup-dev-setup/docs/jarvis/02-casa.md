# Casa

[← Jarvis](README.md)

## Escolha de aparelhos

| Preferir | Por quê | Evitar |
|---|---|---|
| **Zigbee** (pelo Zigbee2MQTT) | Local, barato, bateria dura, não depende da nuvem da marca | Aparelho que só funciona com o app e a nuvem do fabricante |
| **Matter** | Padrão novo, local, entra no Home Assistant direto | Wi-Fi "genérico" sem integração local (acaba virando nuvem) |
| **ESPHome** (seus ESP32) | Você programa e controla tudo | Placa "pronta" com firmware fechado |
| **Câmera com RTSP** | Frigate grava local | Câmera que só manda para a nuvem do fabricante |

Antes de comprar qualquer aparelho, procure o modelo exato na lista de dispositivos suportados do Zigbee2MQTT ou nas integrações do Home Assistant.

## Energia

- **Tomadas com medição** (Zigbee) na geladeira, no chuveiro elétrico (só com modelo próprio para a corrente dele), no computador e na máquina de lavar: consumo por aparelho.
- **Medidor no quadro** (pinça de corrente, tipo Shelly EM ou similar): consumo da casa inteira. **Instalação no quadro só por eletricista**, com o disjuntor desligado.
- No Home Assistant, o **painel de energia** junta tudo: kWh por dia, por aparelho e o custo pela tarifa da concessionária.
- Perguntas que o Jarvis responde: "quanto gastei hoje?", "o que mais gastou esta semana?", "a geladeira está consumindo mais que o normal?" (sinal de borracha da porta ou degelo).

## Água

- **AI-on-the-edge-device**: uma ESP32-CAM presa em frente ao hidrômetro fotografa os números e lê no próprio chip, mandando o valor pelo MQTT.
- O hidrômetro é da concessionária: o leitor só fotografa, sem abrir, furar ou mexer no lacre.
- Com a leitura: consumo por dia no painel de energia (o Home Assistant tem a parte de água) e alerta de vazamento ("consumo contínuo de madrugada").

## Câmeras

- **Frigate** grava e detecta pessoas, carros e animais localmente; o Home Assistant recebe o evento e manda o aviso com a foto para o seu celular.
- "Hey jarvis, mostra o quintal" abre a imagem no celular ou no painel, nunca numa IA na nuvem.
- **Privacidade e LGPD:** câmeras só na sua casa. Nada apontado para rua, calçada ou casa de vizinho. Avise quem mora e quem visita; cômodo íntimo, nunca.
- A política proíbe desligar câmera e apagar gravação por voz.

## Portas, janelas, portão e cortinas

| Pedido | Nível | Motivo |
|---|---|---|
| Trancar a porta, fechar janela e cortina | livre | Sentido seguro |
| Abrir a cortina | livre | Sem risco |
| Destrancar a porta, abrir janela, porta ou portão | **celular** (toque no aviso) | Voz pode ser imitada, gravada ou gritada de fora |
| "Ficou alguma janela aberta?" | livre | Sensor de abertura |

Para isso funcionar é preciso hardware: **fechadura eletrônica** com integração local (Zigbee ou Matter), **motor de portão** com módulo, **motor de janela ou cortina**. Janela comum não tem motor: é obra, com serralheiro e eletricista, e só vale onde fizer sentido (cortina da sala, basculante do banheiro). Sensores de porta e janela custam pouco e entregam a maior parte do valor (aviso de "ficou aberta").

## Geladeira e outros eletrodomésticos

- **Ligar** qualquer coisa: livre.
- **Desligar a geladeira:** só com o ok no celular, e a política gera a automação que **religa sozinha** depois do tempo combinado (30 min no modelo) e avisa. Comida estragada é o erro mais caro desta lista.
- **Desligar outras tomadas:** confirmação falada ("tem certeza?").
- Ar, TV e controle remoto: emissor infravermelho por ESPHome ou Zigbee.
- Robô aspirador: integração do fabricante ou o seu projeto (ver [Robótica](03-robotica.md)).

## Gerar a política e as automações de segurança

```bash
mkdir -p ~/.config/amtech && cp -n ~/dev/dev-setup/tools/jarvis/politica.example.toml ~/.config/amtech/jarvis.toml
python3 ~/dev/dev-setup/tools/jarvis/politica.py validar ~/.config/amtech/jarvis.toml
python3 ~/dev/dev-setup/tools/jarvis/politica.py expor   ~/.config/amtech/jarvis.toml     # o que marcar como exposto
python3 ~/dev/dev-setup/tools/jarvis/politica.py ha-yaml ~/.config/amtech/jarvis.toml > automations_jarvis.yaml
```

Os níveis "voz" e "celular" viram, no Home Assistant, scripts com confirmação: o Jarvis chama o script, e o script pede o ok (pergunta falada ou notificação com botão no app) antes de executar.
