# 6 · Engenharia reversa, migração e construir x usar

[← Motor de decisão](README.md) · Regras de segurança já existentes: [docs/seguranca](../../seguranca/README.md)

## Objetivo definido pelo Alan

Entender a fundo como funciona cada ferramenta que usa, para extrair 100% da performance e decidir com números se compensa criar a própria. Meta de longo prazo: o setup ser feito por ele, com a ajuda do primeiro setup.

## O que a engenharia reversa NÃO garante

Não dá para substituir todas as ferramentas por clones idênticos:

- **Jurídico:** cópia idêntica (código, interface, marca) de software proprietário viola direito autoral; muitos termos de uso proíbem engenharia reversa. Sala limpa reimplementa comportamento, não copia. Para produto comercial, confirmar com advogado.
- **Serviço no servidor não se reverte:** de Claude, GitHub, Hostinger, Cloudflare e Stripe só se vê a API; o valor está na infraestrutura, nos dados e nos modelos.
- **Escala e manutenção:** kernel, PostgreSQL, Docker, navegadores e compiladores são décadas de trabalho; cada ferramenta recriada vira manutenção eterna, inclusive de segurança.
- **Paradoxo:** ferramenta madura tem menos bugs que uma versão nova.

Meta reformulada e atingível: **"100% controlado por mim"** (toda configuração declarada no repositório, todos os dados exportáveis, toda peça substituível por adaptador).

## As 3 camadas

1. **Feito pelo Alan (com o primeiro setup ajudando):** Núcleo AMtech, escada, roteador, catálogo, scripts promovidos, comandos `just`, painéis, integrações, sistemas AM. É o diferencial e o produto.
2. **Open source auto-hospedado:** NixOS/Linux, PostgreSQL, Ollama, LiteLLM, n8n, Home Assistant, Forgejo (se sair do GitHub), Syft, Trivy.
3. **Alugado e isolado por adaptador:** IA de ponta, GitHub, hospedagem, pagamentos, Hotmart.

## Dissecação em 4 níveis

Compreender 100% de tudo é impossível; o padrão sênior é dominar a camada usada e entender um nível abaixo. Open source dispensa engenharia reversa (código, testes e histórico abertos).

1. **Uso:** documentação inteira, todas as opções, flags e recursos (onde está a maior parte da performance desperdiçada).
2. **Arquitetura:** componentes, formato dos dados, protocolo, origem da lentidão.
3. **Comportamento medido:** benchmark no hardware real, RAM/CPU/GPU, limites, casos de borda, testes de caixa-preta (`perf`, `strace`, mitmproxy ou Wireshark só no próprio tráfego).
4. **Interno:** código crítico (abertas) ou Ghidra, no laboratório, só em software que se tem direito de analisar e quando os termos permitem.

Cada dissecação gera uma **ficha** no vault: o que faz, como funciona, configuração ótima, limites medidos, alternativas, custo de substituir. As fichas também viram material de aulas particulares e do Instituto.

Automatizável: nível 1 (IA lê a doc e extrai opções), nível 2 (resumo com IA local e embeddings), nível 3 (benchmarks por script). Do Alan: conduzir os experimentos, entender e decidir.

Começar por: LiteLLM, Ollama, n8n, Docker (abertos, nível 4 sem risco jurídico).

## Decisão construir x usar (da ficha, com números)

- Usa menos de 20% dos recursos e a parte é pequena → construir é candidato.
- **Custo de construir** = horas para fazer + 12 meses de manutenção, × R$ 45/h.
- **Custo de usar** = preço em 12 meses + custo da dor atual.
- É o produto ou a licença impede o uso → pesa a favor de construir.
- Constrói só se construir < usar, ou se for o diferencial.

## Técnicas de engenharia reversa legal

- **Sala limpa:** uma etapa estuda só o comportamento e escreve a especificação; outra implementa do zero (template `infra/templates/sala-limpa`).
- **Caixa-preta:** registrar entradas e saídas e transformar em testes de caracterização; seguro contra dependência de fornecedor.
- **Legado próprio:** extrair as regras do Caixa da Casa para especificação antes de reescrever no AM Rendara (.NET).
- **Laboratório:** falhas nas próprias cópias, como já planejado.

## Migração sem quebrar

- **Estrangulamento (strangler fig):** trocar o sistema velho por partes.
- **Adaptadores:** como as interfaces do Aura (`IFonteDeEstoque`, `IEmissorFiscal` etc.), aplicadas a toda ferramenta externa.
- **Modo sombra:** novo e velho em paralelo, resultados comparados, sem efeito real.
- **Migrações versionadas com desfazer.**

## Hugging Face

Usar: LLMs pequenos em GGUF (Ollama), embeddings, classificadores pequenos (tipo de tarefa, dado sensível), Whisper e Piper, OCR e leitura de documentos (NFC-e, contracheques, PDFs), Spaces para dissecar soluções de outros.

Escolher: model card (licença, tarefa, tamanho, data), versão quantizada, os 20 casos de teste próprios, VRAM e velocidade medidas no notebook. Só entra no catálogo o que passar.

Juntar partes:

| Forma | Possível? | Produtivo? |
|---|---|---|
| Encadear peças inteiras (Whisper → classificador → LLM pequeno → Piper) | Sim | Muito |
| Juntar bibliotecas maduras com licença conferida e adaptador | Sim | Sim |
| Recortar trechos de código de vários apps | Sim | Não (dependências escondidas, sem correções, licenças mistas); só para entender |
| Fundir modelos (merging) ou LoRA | Só entre modelos da mesma arquitetura | Raramente vence um bom prompt com contexto |
| Treinar do zero | Só modelos minúsculos para estudo | Não no hardware atual |

Regra: juntar no nível da arquitetura (peças inteiras por adaptadores), não no código ou nos pesos.
