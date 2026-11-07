<!-- Arquivo GERADO por tools/recursos/recursos.py a partir de data/recursos.json. Não edite à mão. -->

# Recursos: o melhor de cada ferramenta para cada tarefa

[← Índice da documentação](README.md)

Auditado em 2026-11-01. Refaça a cada 3 meses, junto com a auditoria de custos: os planos mudam rápido.

## Regras

- Cada tarefa vai para a ferramenta que faz melhor ou mais barato; nenhuma tarefa depende dos créditos de uma ferramenta só (sempre há uma primária e uma reserva).
- Todos os agentes seguem as mesmas regras: AGENTS.md é o padrão lido pela maioria (Codex, Copilot e outros); CLAUDE.md e GEMINI.md saem do mesmo arquivo (scripts/wsl/regras-ia.sh).
- Portão humano: nada vai para a internet, gasta dinheiro ou fala com cliente sem a sua aprovação. O agente prepara; você aprova o PR, a prévia ou a mensagem.
- Dado de aluno, finanças pessoais e senhas não entram em nenhum agente na nuvem nem no OpenClaw.
- Auditoria de recursos a cada 3 meses, junto com a de custos: os planos mudam rápido (o Gemini CLI saiu do ar para contas pessoais e o v0 cortou o crédito mensal em 2026).

## Qual ferramenta faz cada tarefa

Toda tarefa tem uma primária, uma reserva e um portão. Assim nenhuma depende dos créditos de uma ferramenta só.

| Tarefa | Primária | Reserva | Portão |
|---|---|---|---|
| Site novo (seu ou de cliente) | Copilot (agente na nuvem): issue com a ficha → PR | Claude Code; depois Codex | Você aprova a prévia e o PR |
| Revisar cada PR da esteira | Rotina do Claude Code disparada pelo PR | Revisão do Copilot | Merge só com o CI verde |
| Publicar e ligar domínio | Deploy por push na Hostinger + skills da Hostinger | Cloudflare Pages para site estático | Merge aprovado |
| Manter WordPress dos clientes | Skill maintain-wordpress pelo MCP da Hostinger | Painel da Hostinger | Você aprova antes de atualizar |
| Protótipo para validar ideia | Lovable grátis → GitHub | Copilot | Teste com público antes de construir |
| Software (sistemas AM) | Claude Code | Copilot CLI ou Codex | Testes e revisão sua |
| Tarefas noturnas do setup | Rotinas do Claude Code (5/dia) e n8n na VM | OpenClaw isolado (fase 3) | Relatório no Telegram; ação só com aprovação |
| Rascunho em volume | Gateway: gratis-cf, gratis, local | barato, reserva | Nada sensível |
| Pagamento em site ou sistema | Agente com o MCP do Mercado Pago (chave de teste) | Documentação manual | Troca para produção feita por você |
| Imagens, capas e posts | ChatGPT Go e Canva | FLUX local | Você aprova antes de publicar |

## Esteira de sites (você só confere)

1. Você preenche a ficha (a mesma do kit de sites) como issue no repositório do site, com o rótulo 'site'.
2. A issue é atribuída ao Copilot, que abre um PR com o site (modelo da stack, sem dependências novas sem motivo).
3. O CI roda links, acessibilidade e desempenho; a rotina do Claude revisa o PR contra o AGENTS.md.
4. Uma prévia sobe no Cloudflare Pages; você abre no celular e aprova ou pede ajuste no próprio PR.
5. Merge → deploy por push na Hostinger → o vigia semanal passa a monitorar o site.

## Ferramenta por ferramenta

### GitHub Copilot Pro (grátis para professor verificado)

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Agente na nuvem | Você atribui uma issue ao Copilot e ele abre um pull request com o código; dá para pedir ajustes no próprio PR | Incluído no Pro (1.500 créditos de IA por mês) | Motor principal da esteira de sites e de tarefas de código pequenas, sem gastar o limite do Claude | **usar grátis** |
| Agentes de terceiros | Escolher outro agente na mesma issue (prévia pública nos planos pagos) | Incluído no Pro, em prévia | Rodar a mesma issue em outro agente quando o primeiro errar | **usar grátis** |
| Copilot CLI e app | Agente no terminal, incluído em todos os planos | Créditos do plano | Reserva de código no terminal quando o Claude Code bater o limite | **usar grátis** |

**Lacuna:** A verificação de professor no GitHub Education ainda está pendente; é ela que libera o Pro grátis. É a maior lacuna do setup hoje.

Fonte: <https://docs.github.com/en/copilot/concepts/billing/individual-plans>

### Claude Pro (app, Claude Code e rotinas)

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Rotinas do Claude Code | Tarefa salva que roda na nuvem da Anthropic por horário, por chamada de API ou por evento do GitHub (PR, issue), mesmo com o notebook desligado | Pro: 5 execuções por dia, à parte do limite normal | Revisar todo PR da esteira, resumo noturno dos repositórios, vigia de dependências | **usar já** |
| Conectores e skills da Hostinger | Skills prontas para publicar, ligar domínio, manter WordPress, auditar e consertar sites na Hostinger | Já pago; precisa conectar o MCP da Hostinger | Publicar e manter os sites de clientes pela conversa | **usar já** |

**Lacuna:** Cada rotina começa de um clone novo do repositório: o que ela precisa saber tem de estar em AGENTS.md ou em arquivo do repositório.

Fonte: <https://www.noqta.tn/en/blog/claude-code-routines-cloud-ai-automation-guide-2026>

### Codex (OpenAI)

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Codex no ChatGPT Go | Agente de código incluído no Go, com limite baixo e cota semanal | Grátis pelo Nubank (Go) | Segunda opinião e reserva em tarefas leves; lê o mesmo AGENTS.md | **usar grátis** |
| Sites (ChatGPT/Codex) | Cria e hospeda apps e páginas a partir da conversa | Só nos planos pagos acima do Go | Nenhum: proíbe comércio e pagamentos e publica direto em produção, sem prévia | **não usar** |

**Lacuna:** Não serve como agente principal no Go: a cota semanal acaba em poucas horas de uso pesado.

Fonte: <https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan>

### Google (AI Plus, Antigravity, Jules)

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Gemini CLI | Saiu do ar para contas pessoais sem licença paga em 18/06/2026; o substituto é o Antigravity CLI, de código fechado | — | Nenhum fluxo do setup deve depender dele | **não usar** |
| Antigravity | Ambiente de agentes do Google; o acesso ampliado aparece só no plano Pro, não no Plus | Limitado no Plus | Testar só se sobrar cota; não é motor da esteira | **adiar** |
| Deep Research e NotebookLM no AI Plus | Mais acesso que o grátis; o NotebookLM responde preso às suas fontes | AI Plus | Rascunho de aulas e pesquisa de mercado | **usar já** |

**Lacuna:** O armazenamento do AI Plus varia por país (a página internacional mostra 400 GB); confira o valor no Brasil antes de trocar o Google One.

Fonte: <https://www.shopifreaks.com/google-ends-free-gemini-cli-access-for-non-enterprise-users-on-june-18-replacing-it-with-closed-source-antigravity-cli/>

### Hostinger

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| MCP oficial (hostinger-api-mcp) | 146 ferramentas para IAs: sites, VPS, domínios e DNS, e-mail marketing, pagamentos, e-commerce e Horizons | Grátis com a conta | Claude, Codex ou o agente noturno publicam e conferem sites sem você abrir o painel | **usar já** |
| Deploy por push no GitHub | Cada push no repositório publica o site; apps Node.js são construídos a partir do código | Incluído na hospedagem web | Último passo da esteira: PR aprovado → merge → site no ar | **usar já** |
| Construtor com IA, Hostinger Agent e Reach | Criação de sites e campanhas por IA com créditos à parte (recarga a partir de 500 créditos, que vencem em 3 meses) | Plano de créditos de IA, pago à parte | Só quando um cliente do pacote Vendas pagar pela função | **adiar** |
| Kodee (VPS gerenciada por IA) | Agente que executa comandos na VPS da Hostinger | Só com VPS | Nenhum agora: a VM grátis da Oracle já faz o papel de servidor 24 h | **não usar** |

**Lacuna:** O MCP da Hostinger ainda não está conectado ao Claude; sem ele, as skills de publicar e manter sites não funcionam.

Fonte: <https://www.hostinger.com/support/?p=342>

### OpenClaw

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Agente pessoal 24/7 | Agente auto-hospedado que executa tarefas agendadas e por mensagem, com skills e acesso a ferramentas | Grátis (código aberto) + o modelo que ele usar pelo gateway | Tarefas noturnas que as rotinas e o n8n não cobrem: triagem, relatórios, rascunhos de prospecção | **testar isolado** |

**Lacuna:** Histórico de segurança ruim em 2026: 341 skills maliciosas na loja oficial, mais de 135 mil instâncias expostas e falhas de nota 8,8 a 9,9. Só roda na VM isolada, atrás do Tailscale, sem suas contas pessoais, sem skills de terceiros não revisadas e com chave do gateway de teto baixo.

Fonte: <https://www.orcarouter.ai/blog/openclaw-exposed-instances-agent-identity>

### Cloudflare

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Workers AI | Modelos abertos rodando na rede da Cloudflare, com 10.000 neurônios grátis por dia | Grátis até a cota diária | Modelo 'gratis-cf' no gateway, para rascunho em volume | **usar grátis** |
| Cloudflare API MCP | Substitui o conector antigo, que avisa que está descontinuado | Grátis | DNS, Pages e Workers pela conversa | **trocar** |

**Lacuna:** O conector conectado hoje é o descontinuado.

Fonte: <https://costbench.com/software/llm-api-providers/cloudflare-workers-ai/free-plan/>

### Lovable

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| Plano grátis | 5 créditos por dia (máximo de 30 por mês), até 5 projetos em lovable.app, sem domínio próprio | Grátis | Protótipo de landing para validar uma ideia antes de construir | **usar grátis** |
| Sincronização com o GitHub | Disponível em todos os planos, inclusive o grátis | Grátis | Levar o protótipo aprovado para o repositório e publicar na Hostinger pela esteira | **usar grátis** |

**Lacuna:** Domínio próprio só no pago: o site final sai pela esteira, não pelo Lovable.

Fonte: <https://eesel.ai/blog/lovable-pricing>

### Vercel (v0)

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| v0 | Gerador de interfaces; o plano grátis virou crédito único de US$ 5 só para contas novas (out/2026) | Pago para uso contínuo | Nenhum: Lovable grátis e o Copilot cobrem | **não usar** |

**Lacuna:** Nenhum fluxo deve contar com crédito mensal grátis do v0.

Fonte: <https://www.usagepricing.com/blueprint/activity/v0-2026-10-05-free-credits-one-time>

### Mercado Pago

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| MCP oficial (Recursos para IA) | Servidor MCP do Mercado Pago para agentes consultarem a documentação e montarem a integração do checkout | Grátis | Integrar pagamento nos sites e sistemas com o agente lendo a documentação oficial | **usar já** |

**Lacuna:** Chave de produção nunca vai para agente: só a de teste, e a troca para produção passa pelo portão.

Fonte: <https://www.mercadopago.com.br/developers/pt/docs/checkout-pro/additional-content/mcp-server>

### Hotmart

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| MCPs de terceiros | Não há MCP oficial; os que existem são de terceiros | — | Nenhum com credencial de venda; use os webhooks oficiais pelo n8n | **não usar** |

**Lacuna:** Vendas da Hotmart chegam ao setup só por webhook oficial.

Fonte: <https://github.com/thaleslaray/hotmart-mcp>

### Canva

| Recurso | O que faz | Custo | Uso no setup | Decisão |
|---|---|---|---|---|
| IA no plano grátis | Até 20 usos premium de IA por mês (o Canva Code entra nessa cota) | Grátis | Capas e posts pontuais | **usar grátis** |
| Canva para Educação | Plano grátis para professores elegíveis, com recursos do Pro | Grátis se aprovado | Material de aula e posts sem pagar o Pro | **usar grátis** |

**Lacuna:** Pedir a verificação de professor no Canva para Educação (confira a elegibilidade).

Fonte: <https://www.eesel.ai/en/blog/canva-ai-pricing>

## Resumo das decisões

| Decisão | Recursos |
|---|---:|
| usar já | 6 |
| usar grátis | 9 |
| trocar | 1 |
| testar isolado | 1 |
| adiar | 2 |
| não usar | 5 |

Ferramentas locais e de código aberto (Git, Neovim, Docker etc.) ficam fora desta auditoria: não escondem recursos pagos nem mudam de plano.
