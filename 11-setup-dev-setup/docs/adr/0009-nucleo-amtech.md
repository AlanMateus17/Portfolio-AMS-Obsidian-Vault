# 0009 · Núcleo AMtech: um cérebro que conecta todas as ferramentas, sem reescrevê-las

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O Alan quer o setup 100% conectado e agindo sozinho em tudo o que for possível, com mineração de código em repositórios públicos, para ter o máximo de renda trabalhando menos e para abrir a empresa de TI e as demais empresas do grupo. Ele perguntou se seria melhor fazer engenharia reversa em todas as ferramentas e criar um sistema único.

## Decisão

1. **Não reescrever as ferramentas.** Quase todas são de código aberto (o código já está publicado e elas conversam por API, webhook e banco), reescrevê-las levaria anos, e várias são AGPL: copiar o código delas num produto vendido como serviço obriga a publicar o código do produto. Engenharia reversa de ferramenta fechada costuma violar os termos de uso.
2. **O sistema único é o Núcleo AMtech (`aura-nucleo`)**, mais um serviço compartilhado do Aura:
   - **Banco central** (PostgreSQL + pgvector na VM; SQLite local no notebook com o mesmo esquema): eventos, conhecimento, tarefas e auditoria.
   - **Adaptadores** por ferramenta (n8n para os simples, código para os complexos): traduzem tudo em eventos e executam ações.
   - **Orquestrador de agentes** (Claude Agent SDK) 24 horas na VM, com os agentes que o setup já tem.
   - **Política de autonomia** para toda ação: automático, avisa, pede ok (toque no celular), proibido. Botão de parar tudo.
   - **MCP do núcleo**: Claude Code, Aider e Jarvis consultam a mesma base antes de agir.
   - **Teste do sistema inteiro** toda noite (simulação de ponta a ponta com dados falsos) e testes de contrato a cada push.
3. **Credenciais dos agentes:** tokens de permissão mínima, só leitura onde der, cifrados com sops + age na VM. Exceção aceita à regra "segredo só no KeePassXC", que continua o cofre principal. Nunca senha de banco, corretora ou gov.br na VM.
4. **Teto de gasto com IA dos agentes:** US$ 20 por mês no gateway LiteLLM (cerca de R$ 110), além do Claude Pro. Passou, recusa. Tarefa simples vai para o modelo local.
5. **Ordem:** fundação → banco central → **garimpo** (adiantado, é o que o Alan mais quer usar) → política e auditoria → arquiteto e ganchos → adaptadores de dev → adaptadores de negócio → orquestrador 24 h → teste do sistema.
6. **Renda primeiro:** cada fase entrega algo que uma renda usa. O próprio núcleo, com os adaptadores de negócio, vira o produto de automação que a empresa de TI vende para pequenos negócios (oferta `automacaoia`) e a base de operação das outras empresas do grupo.

## Consequências

- O valor está no que é seu (orquestração, garimpo, base de conhecimento, regras); as ferramentas são peças trocáveis.
- Mais uma peça crítica para manter: o núcleo ganha backup, monitoramento e testes como qualquer sistema AM.
- Autonomia de verdade depende da VM ligada 24 horas; o notebook entra como reforço (GPU e modelos locais).
- Com o teto de 7 horas extras por semana, o plano completo leva de 4 a 6 meses.
