# Arquitetura de IA: modelos grandes sem comprar um computador maior

[← Índice da documentação](../README.md)

**A verdade primeiro:** treinar do zero um modelo com centenas de bilhões de parâmetros custa milhões de reais em GPU. Isso não cabe em nenhum setup pessoal. O que cabe, e é o que os profissionais fazem, são estas sete estratégias.

| # | Estratégia | O que você ganha | Onde roda | Custo |
|---|---|---|---|---|
| 1 | **Quantização (GGUF 4 a 5 bits)** | Um modelo de 14B a 32B no seu notebook | llama.cpp/Ollama, GPU 4 GB + RAM 32 GB | Grátis |
| 2 | **Modelos MoE** (mistura de especialistas) | Muitos parâmetros no total, poucos ativos por token: rodam bem com RAM | Seu notebook, com offload | Grátis |
| 3 | **Cluster na sua rede** (llama.cpp RPC, exo) | Um modelo maior dividido entre os seus computadores | Notebook + outros PCs pela rede da casa ou Tailscale | Grátis com o que você tem |
| 4 | **Fine-tuning QLoRA** | Um modelo de 8B a 70B treinado no SEU conteúdo, sem treinar do zero | Kaggle/Colab (T4 grátis) até ~14B; GPU alugada por hora para 32B a 70B | Grátis a dezenas de reais por treino |
| 5 | **GPU por hora + vLLM** | Servir um modelo grande só nas horas em que precisa | RunPod e afins, ligado ao gateway | Por hora, com teto de gasto |
| 6 | **Destilação** | Um modelo pequeno que imita um grande na SUA tarefa | Gera os exemplos com o modelo grande, treina o pequeno no Kaggle | Baixo |
| 7 | **Modelos de fronteira por API** | O máximo de qualidade para o que é difícil | Gateway LiteLLM com nomes "rapido", "forte", "local" | Por uso, com limite mensal |

**Regra de arquitetura:** os agentes nunca chamam um modelo pelo nome. Eles pedem `local`, `rapido`, `forte` ou `gpu-alugada` ao gateway ([infra/ia](../../infra/ia/compose.yaml)). Trocar o modelo por trás é mudar uma linha, sem tocar em agente nenhum.

**RAG antes de treino:** para "o modelo saber das minhas coisas", busca nas suas notas (RAG) resolve 80% e não precisa de GPU. Treine só quando o *jeito* de responder precisa mudar.

**Catálogo do Hugging Face:** modelos e kits que servem ao setup, filtrados pela sua GPU, em [hugging-face.md](hugging-face.md).

**Economia de tokens:** produzir mais gastando menos no Claude, com o exemplo da planta baixa, em [tokens.md](tokens.md).

**Motor de decisão (nov/2026):** a escada que decide entre ferramenta pronta, código, automação, IA local, IA online ou você, com regra de três, qualidade, segurança e nuvem barata, em [motor/](motor/README.md) ([ADR 0014](../adr/0014-motor-de-decisao-e-custo-minimo.md)).

## Quanto cabe na sua máquina

```bash
python3 ~/dev/dev-setup/tools/ia/cabe.py 32        # um modelo de 32B
python3 ~/dev/dev-setup/tools/ia/cabe.py 30 --ativos 3   # MoE de 30B com 3B ativos
python3 ~/dev/dev-setup/tools/ia/cabe.py 70        # mostra que 70B vai para GPU alugada ou cluster
python3 ~/dev/dev-setup/tools/ia/cabe.py --hf Qwen/Qwen3-VL-2B-Instruct   # lê o tamanho direto do Hugging Face
```

## Qualidade medida, não achada

- **Evals:** cada agente tem casos de teste ([promptfoo](../../infra/ia/evals/promptfooconfig.yaml)). Mudou o prompt ou o modelo, roda os testes antes de pôr em produção.
- **Custo e rastro:** o gateway registra quanto cada agente gastou e corta quando passa do limite.
- **Revisor:** um agente revisor confere cada entrega contra o padrão de qualidade da oferta antes de chegar ao cliente.
- **Dados:** dado de aluno, senha e dado financeiro pessoal nunca entram em prompt, dataset ou treino.

## Para aprender de verdade

Construir um GPT pequeno do zero (tokenizador, atenção, treino) no Kaggle ensina mais arquitetura do que qualquer curso. Está no roteiro como passo da trilha de IA.
