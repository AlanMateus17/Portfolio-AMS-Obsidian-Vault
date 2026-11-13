# 1 · Modelos Claude, chat x API e economia de tokens

[← Motor de decisão](README.md)

## Claude Fable 5.2 (lançado em 09/11/2026)

- O modelo mais capaz disponível ao público. Feito para trabalho técnico longo: migrações grandes de código, agentes rodando por horas ou dias, pesquisa e design de engenharia.
- Contexto de 1 milhão de tokens, saída de até 128 mil. Até 30% mais rápido que o 5.1.
- Pode ser "conselheiro" de modelos menores (ferramenta advisor), o que barateia a execução.
- No FrontierCode 2.0: 49,1% contra 45,5% do Opus 5.5. Melhor, mas não muda tarefa simples.
- Preço na API: US$ 8 por milhão de tokens de entrada. Caro para uso contínuo.
- **Limite que afeta o Alan:** o Fable tem travas de cibersegurança. O Mythos 5.2 (o mesmo modelo, sem as travas) só é liberado para organizações verificadas. Pentest e engenharia reversa no Fable vão esbarrar em recusas; as ferramentas determinísticas (Ghidra, Trivy, Semgrep) não recusam.

Fontes: [Anthropic](https://www.anthropic.com/news/claude-fable-and-mythos-5-2), [DataCamp](https://www.datacamp.com/blog/claude-fable-5-2-and-mythos-5-2), [UnificAlly](https://unifically.com/models/claude-fable-5.2), [SQ Magazine](https://sqmagazine.co.uk/anthropic-launches-claude-fable-mythos-5-2.md).

## Divisão por modelo

| Modelo | Uso |
|---|---|
| Fable 5.2 | Arquitetura grande, migrações, AMtech OS, planejar a orquestração do Núcleo. De preferência só planeja; menores executam |
| Opus | Revisão delicada, raciocínio difícil |
| Sonnet | Execução do dia a dia, código, conteúdo |
| Haiku | Classificar, extrair, formatar, tarefas repetitivas e automáticas |

Esforço baixo ou médio por padrão. Alto só quando o resultado falhar.

## Chat x API

- **Chat e Claude Code (assinatura):** principal enquanto o setup não gera renda. Custo fixo, com busca, arquivos, artifacts, memória e conectores prontos. Para pensar, planejar, estudar, preparar aulas e programar junto.
- **API (paga por token):** só para o que roda sozinho ou fica dentro de um produto (roteador do Núcleo, automações agendadas, aura-copilot). Tem cache, batch e registro exato do gasto.
- **Proibido:** usar a assinatura do chat como motor de automação ou de produto para clientes. Isso exige API.
- Quando um produto vender, o custo da API dele entra no preço cobrado.

## O que mais gasta (em ordem)

1. Contexto repetido (repositório ou histórico inteiro a cada chamada).
2. Modelo grande em tarefa pequena.
3. Esforço alto sem motivo (raciocínio também é cobrado).
4. Saída sem limite.

## Técnicas de economia (nível sênior)

- **Roteamento por complexidade** (Haiku → Sonnet → Opus → Fable).
- **Prompt caching:** parte fixa (regras, CLAUDE.md, docs dos sistemas AM) no início e sempre igual; leitura em cache custa cerca de 10% do normal.
- **Batch API:** tarefas sem pressa custam cerca de metade.
- **Contexto mínimo:** só os arquivos relevantes, achados por busca. No Claude Code, `/clear` entre tarefas e CLAUDE.md curto.
- **Saída estruturada:** JSON com campos definidos e `max_tokens` baixo.
- **Skills em vez de prompt gigante:** a instrução só carrega quando é usada.
- **Medir:** gravar o campo `usage` de cada chamada; manter de 10 a 20 perguntas reais como teste fixo e comparar custo e qualidade a cada mudança.
