# Robótica

[← Jarvis](README.md)

O Jarvis não fala com cada robô do jeito de cada um: todo robô vira entidade do Home Assistant ou tópico do MQTT. Assim, "manda o robô para a sala" e "apaga a luz" seguem o mesmo caminho e a mesma política.

## Três caminhos, conforme a placa

| Placa | Caminho | Quando usar |
|---|---|---|
| **ESP32** | ESPHome (arquivo YAML), entra no Home Assistant sozinho | Sensores, relés, robô simples, carrinho, braço com servos |
| **Arduino** (Uno, Leonardo) | Ligado por serial a um ESP32 ou a um Raspberry Pi, que faz a ponte | Projetos das aulas que já estão em Arduino |
| **Raspberry Pi** | ROS 2 no Pi + `mqtt_client` (ponte ROS 2 ↔ MQTT) | Robô com mapa, navegação, câmera: aspirador e carro autônomo |

O ESP32 também pode rodar **micro-ROS** e conversar com o ROS 2 direto, quando o projeto crescer.

## Exemplo: robô aspirador próprio

1. O Pi roda o ROS 2 (navegação e mapa) e publica estado e bateria.
2. O `mqtt_client` leva `/robo/estado` e `/robo/comando` para o MQTT.
3. No Home Assistant, as entidades do robô aparecem pelo MQTT; o Jarvis expõe só "iniciar", "voltar para a base" e "ir para o cômodo".
4. "Hey jarvis, limpa a sala" → Assist → política (livre) → MQTT → ROS 2.

## Segurança com coisas que se mexem

- **Parada de emergência física** (botão que corta o motor) em todo robô com motor, independente de software.
- Robô com motor forte, corte ou calor (impressora 3D, ferramenta) nunca liga por voz sem você no cômodo: nível "celular" na política.
- Limite de velocidade e área no próprio firmware, não só no Home Assistant.
- Nada disso vai para a sala de aula sem o mesmo cuidado: a versão dos alunos usa motores pequenos e o botão de parada.

## Ligação com as aulas

O mesmo caminho serve ao projeto de robótica com o agro e às aulas de Noções de Robótica: um sensor de umidade em ESPHome que aparece num painel é uma aula completa de ponta a ponta (sensor → rede → servidor → painel).
