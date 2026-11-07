# Hugging Face: o que usar no setup e o que comprar

[← Arquitetura de IA](README.md)

Pesquisa de nov/2026, com foco em três frentes: **TI** em primeiro lugar, **casa inteligente** e **agropecuária** (pecuária, lavoura e horta, e o negócio de agro), filtrada e pelo que cabe na sua máquina (Acer Nitro, 32 GB de RAM, GTX 1650 com 4 GB e **sem bfloat16**). Antes de baixar qualquer modelo, confira o tamanho:

```bash
python3 ~/dev/dev-setup/tools/ia/cabe.py --hf Qwen/Qwen3-VL-2B-Instruct
```

## Modelos e bibliotecas

### TI: código, documentos, RAG, agentes e segurança

| Projeto | Para quê | Na GTX 1650 | Atenção |
|---|---|---|---|
| `ibm-granite/granite-docling-258M` + Docling | NFC-e do Caixa da Casa, documentos da escola, verificador ABNT, acervo | Cabe | Apache 2.0; português não foi validado pela IBM: teste |
| `Qwen/Qwen2.5-Coder-1.5B-Instruct` (GGUF) | Autocompletar código no VS Code sem internet (Continue + Ollama), reserva do Copilot | Cabe inteiro | Apache 2.0; para tarefa grande, o Claude continua melhor |
| `BAAI/bge-m3` | Busca nas suas notas (RAG do setup) em português | Cabe | MIT |
| `Qwen/Qwen3-1.7B` e `Qwen3-4B` (GGUF) | Modelo local de reserva sem internet | 1.7B inteiro; 4B no limite | Apache 2.0 |
| `Polygl0t/Tucano2-*` | Modelos feitos para português, de 0,5B a 3,7B | Os pequenos cabem | Confira a licença no cartão |
| `meta-llama/Llama-Prompt-Guard-2-86M` | Filtro de injeção de prompt antes do Jarvis agir | Cabe | Licença Llama; teste com frases em português |
| `smolagents`, `tiny-agents`, Spaces com MCP | Agentes pequenos e Spaces do Hub como ferramentas do Claude | — | Apache 2.0; Space de terceiro é código de terceiro: rode no ai-jail |

### Voz do Jarvis

| Projeto no Hub | Para quê | Na GTX 1650 | Atenção |
|---|---|---|---|
| `openai/whisper-large-v3-turbo` (via faster-whisper) | Trocar o Whisper `small` por um bem mais preciso | Cabe em int8 | Licença MIT |
| `fsicoli/whisper-large-v3-pt-cv16`, `distil-whisper-large-v3-ptbr` | Whisper ajustado para português | Teste antes | O cartão do primeiro não publica a taxa de erro: meça com 20 frases suas |
| `rhasspy/piper-voices` (`pt_BR-faber-medium`) | Voz do Jarvis, já no setup | CPU basta | Licença varia por voz |
| `hexgrad/Kokoro-82M` | Voz mais natural que o Piper | Cabe | Tem vozes pt-BR para testar; Apache 2.0 |
| F5-TTS pt-BR, Chatterbox pt | Clonar a **sua** voz localmente | Teste | F5-TTS é não comercial (CC BY-NC); voz de outra pessoa, nunca |
| openWakeWord `hey_jarvis` | Palavra de ativação | CPU | Modelos prontos são CC BY-NC-SA: pessoal pode, produto à venda não |

### Câmeras e visão

| Projeto | Para quê | Na GTX 1650 | Atenção |
|---|---|---|---|
| `Qwen/Qwen3-VL-2B-Instruct` (GGUF, Ollama) | "O que tem na câmera do quintal?" respondido **local**, sem mandar imagem para a nuvem | Cabe em Q4 (~2 GB) | O 4B pede 6 GB: fica para a GPU nova |
| `HuggingFaceTB/SmolVLM2-*` | Visão ainda menor, até no servidor da casa | Cabe | Mais fraco em português |
| Detectores ONNX que o Frigate aceita (YOLO e outros; confira a lista na documentação dele) | Detecção de pessoa, carro e animal | GPU ou OpenVINO no N100 | Ultralytics YOLO é AGPL: uso pessoal sim, produto fechado não |

O Frigate também gera descrição dos eventos com um modelo local pelo Ollama: une as duas linhas acima sem nada sair de casa.

### Robótica (o maior achado)

| Projeto | Para quê | Atenção |
|---|---|---|
| **`lerobot`** (biblioteca) | Gravar demonstrações, treinar e rodar robôs que aprendem por imitação; integra SO-101, LeKiwi e outros | Apache 2.0; em português há guia na wiki da Seeed |
| `lerobot/smolvla_base` | Modelo visão-linguagem-ação de 0,5B: você fala a tarefa, o braço executa | Treino em bf16: vai para GPU alugada (L4, A10) |
| Política ACT | Política menor e mais simples para começar | Treina no Kaggle (T4) |
| Datasets do Hub (`lerobot/*`) | Ver como os outros gravaram antes de gravar o seu | Grave os seus sem rosto de aluno |

### Agropecuária

O Hub tem pontos de partida, não soluções prontas: todo modelo de campo precisa ser retreinado com fotos do lugar onde vai rodar (luz, raça, cultura e câmera mudam tudo).

**Pecuária**

| Projeto | Para quê | Atenção |
|---|---|---|
| `nsagatov1/cattle-detection-yolov8`, `rmayormartins/yolov5-farm-cattle` | Contar e detectar gado na câmera do curral ou do bebedouro, pelo Frigate | Base Ultralytics (AGPL); retreine com fotos do rebanho |
| Qwen3-VL 2B local | "Tem animal deitado fora do normal no piquete?" em foto, sem internet | Confirmação humana sempre: é aviso, não diagnóstico |
| ESPHome: ultrassom no bebedouro e no cocho, célula de carga (HX711) na balança | Nível de água e ração e pesagem no Home Assistant | Hardware barato; sem IA |

**Lavoura e horta**

| Projeto | Para quê | Atenção |
|---|---|---|
| ESPHome + sensor de umidade capacitivo + válvula solenoide | Irrigação por umidade do solo e por horário, com a política do Jarvis | Sensor capacitivo dura; o resistivo oxida em semanas |
| Estação meteorológica (ESPHome) + previsão da Open-Meteo no Home Assistant | Não irrigar quando vai chover | — |
| `Francesco/weed-crop-aerial`, CropAndWeed | Datasets para detectar erva daninha em foto (drone ou câmera fixa) | Ponto de partida para um modelo seu, treinado no Kaggle |
| ESP32 com rádio LoRa (SX1276/SX1262) | Sensores a centenas de metros da casa, onde o Wi-Fi não chega | Ponto a ponto primeiro; LoRaWAN com ChirpStack só com muitos sensores |

**Negócio de agro (AMtech Campo)**

O que der certo na horta e no curral vira produto para sítios e produtores da região: o "Automação rural (irrigação, caixa d'água, sensores)" de [docs/negocios](../negocios/03-produtos-proprios.md), agora com painel no Home Assistant, avisos no celular e contagem por câmera. Produto com rádio vendido no Brasil precisa de homologação da Anatel: comece instalando placas já homologadas e vendendo o serviço e o painel.

## Compras, em ordem do que destravam

Preços em dólar das fontes oficiais; com frete e impostos de importação, conte bem mais que isso. Compare com revendedor no Brasil antes.

| # | O que | Preço de referência | Destrava | Quando |
|---|---|---|---|---|
| 1 | Servidor da casa (N100 ou Pi 5) | — | Toda a casa e a voz (ADR 0004) | Primeiro |
| 2 | **Par de braços SO-101** (líder + seguidor) + 2 câmeras USB | Peças e motores US$ 230 (o par); as peças impressas à parte | LeRobot, aula de robótica por imitação, SmolVLA, conteúdo "build in public" | Primeira compra de robótica |
| 3 | **Reachy Mini Wireless** | US$ 499 (Lite, US$ 399) no lançamento | Um corpo para o Jarvis na mesa: 4 microfones, câmera, alto-falante, cabeça que se mexe; apps do Hub; aulas | Depois do SO-101 |
| 4 | LeKiwi (base móvel para o SO-101) | Confira na Seeed | Robô que anda e pega coisas: base do aspirador e do carro autônomo | Depois de treinar o SO-101 |
| 5 | Câmeras IP com RTSP | — | Frigate e a câmera que descreve | Com o servidor da casa |
| 6 | Kit de campo: ESP32 com LoRa, sensores de umidade capacitivos, válvula solenoide, ultrassom e célula de carga | Barato (componentes nacionais) | Irrigação da horta, bebedouro, cocho e balança; o primeiro produto da AMtech Campo | Junto do servidor da casa |
| 7 | GPU de 12 GB ou mais | — | Modelos de visão e voz maiores e treino local | Só quando uma renda passar no portão; antes, GPU por hora com teto |

Sobre o Reachy Mini: a própria Hugging Face diz que ele está no começo do desenvolvimento, vem como kit para montar e tinha cerca de 90 dias de entrega no lançamento.

## Fontes

- [LeRobot no Hugging Face](https://huggingface.co/lerobot) · [SmolVLA base](https://huggingface.co/lerobot/smolvla_base) · [Custo e peças do SO-101](https://physicalailab.io/en/so-101-robot-arm-kit-cost-buy-setup/) · [LeKiwi na wiki da Seeed (pt-BR)](https://wiki.seeedstudio.com/pt-br/lerobot_lekiwi/)
- [Reachy Mini (blog da Hugging Face)](https://huggingface.co/blog/reachy-mini)
- [Qwen3-VL 4B GGUF](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct-GGUF) · [Memória do Qwen3-VL 2B, 4B e 8B](https://codersera.com/blog/qwen3-vl-4b-vs-qwen3-vl-8b-benchmarks-vram-guide/amp/)
- [Granite-Docling (IBM)](https://ibm.com/new/announcements/granite-docling-end-to-end-document-conversion) · [Whisper Large v3 Portuguese](https://huggingface.co/fsicoli/whisper-large-v3-pt-cv16) · [Tucano](https://huggingface.co/TucanoBR/Tucano-160m)
- [Bibliotecas de agentes do Hub](https://huggingface.co/docs/hub/agents-libraries)
- [Detecção de gado YOLOv8](https://huggingface.co/nsagatov1/cattle-detection-yolov8) · [YOLOv5 farm cattle](https://huggingface.co/rmayormartins/yolov5-farm-cattle) · [weed-crop-aerial](https://huggingface.co/datasets/Francesco/weed-crop-aerial) · [CropAndWeed](https://docs.voxel51.com/dataset_zoo/datasets_hf/cropandweed.html) · [Nó LoRa com ESP32 para o Home Assistant](https://esp32.co.uk/esp32-lora-remote-sensor-node-for-home-assistant-sx1276/)
