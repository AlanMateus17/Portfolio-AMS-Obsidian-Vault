# 3 · A escada de decisão e o roteador local

[← Motor de decisão](README.md)

## A escada (do mais barato e confiável ao mais caro e incerto)

Todo pedido desce os degraus e para no primeiro "sim":

1. **Já existe pronto?** (setup, open source, ferramenta já paga) → reutilizar.
2. **A regra cabe em código?** (conferível e repetível) → script ou algoritmo, sempre com teste.
3. **Dispara por evento ou horário?** (webhook, agenda, fila) → automação (n8n, cron, GitHub Actions).
4. **Precisa entender linguagem?** (texto livre, rascunho, ideia) → IA local primeiro; se falhar no critério, assinatura online; API paga só quando uma renda pagar.
5. **Julgamento ou mundo real?** (decidir, aprovar, testar) → o Alan.

Os degraus 2 e 3 costumam andar juntos (script disparado por agenda). A escada estende o `just triagem` atual.

## O que é determinístico (código, nunca IA)

Regra: se dá para escrever a regra, vira código. Se só dá para descrever o que se quer, entra a IA, e logo depois um teste confere.

- **Roteador:** tabela de regras decide primeiro; o modelo local só quando nenhuma regra casar. Teto de gasto é contador que bloqueia. Escopo cruza com `portfolio.json` e o limite de 3 frentes. Contexto por lista fixa de arquivos por tipo de tarefa e ripgrep.
- **Camada de IA:** prompts versionados no git, saída em JSON validado por schema, temperatura 0 em classificação e extração, cache de respostas, conjunto fixo de testes a cada mudança.
- **Dinheiro:** nenhuma conta por IA (Caixa da Casa, rateio, imposto, metodologias, R$ 45/h, VEH, métricas).
- **Segurança e aprovação:** KeePassXC, sops/age, tokens mínimos, guarda de escopo de pentest, política do Jarvis, portões de publicar, pagar e falar com cliente.
- **Infraestrutura:** instalação declarativa (NixOS no AMtech OS), scripts idempotentes, versões fixadas, backup 3-2-1, git hooks e tags.
- **Aulas:** templates, numeração, PDF, checagens (quantidade, "100% teóricas", enunciado completo, ABNT), filtro de dados de alunos.
- **Rotina:** prazos, lembretes, horas semanais, aviso quando a execução passar de 3 frentes "agora".

Continua com a IA (e é verificado por código): interpretar o texto do Alan, redigir, gerar código (só passa com teste e CI), propor ideias e design.

## O roteador local (custo zero)

- **Ferramentas comuns primeiro:** ripgrep, JSON do setup, `just`, git hooks, testes no CI.
- **Ollama** com modelo pequeno escolhido no [catálogo do Hugging Face](../hugging-face.md): preenche o formulário, classifica, resume, extrai, confere contra o critério de pronto.
- **Embeddings locais** para achar trechos do repositório.
- **LiteLLM** (`infra/ia/litellm.yaml`) como porta única.
- **n8n** auto-hospedado para fluxos sem IA.
- **Fora, sem custo extra:** Claude Code (assinatura) para código e arquitetura com o Alan acompanhando; Copilot Pro (GitHub Education) na esteira de sites; Gemini e camadas grátis para rascunho sem dado sensível; API paga do Claude desligada até uma renda pagar.

Fluxo: texto do Alan → modelo local monta o formulário e puxa o contexto → 3 linhas para confirmar → roteador escolhe o destino → resultado volta → modelo local confere → Alan.

Limites aceitos: o modelo local é lento e erra mais (serve para rotear, não para criar); assinaturas têm limite (o roteador espera ou cai para opção mais fraca); assinatura é uso pessoal (produto para cliente exige API); "grátis" custa energia, desgaste e tempo de configuração. Hardware: Acer Nitro, GTX 1650 4 GB, 32 GB RAM, modelos de 3 a 8B.

## Papel de cada ferramenta do dia a dia

| Ferramenta | Papel no motor |
|---|---|
| Claude (chat) | Pensar, planejar, aulas; skill `arquiteto-de-prompt`; fichas de dissecação |
| Claude Code | Construir escada, catálogo, registro e scripts promovidos; revisar PRs |
| Copilot Pro | Esteira de sites e código repetitivo no editor |
| Codex, OpenClaw | Reserva de agente de código |
| Gemini, ChatGPT Go | Rascunho e pesquisa de baixo risco, nunca dado sensível |
| Ollama | Degrau 4 local |
| LiteLLM | Porta única: roteamento, teto, cache, registro |
| n8n | Degrau 3 |
| GitHub Actions | Checagens que bloqueiam o merge |
| Docker, WSL2 | Laboratório isolado (garimpo e dissecação) |
| `just` | Interface de tudo |
| KeePassXC, sops/age | Segredos que nenhuma IA vê |
| Obsidian | ADRs, lições, fichas, runbooks |
| ActivityWatch | Horas reais para o retorno de cada automação |
| Hostinger | Hospedagem e deploy, isolado por adaptador |
