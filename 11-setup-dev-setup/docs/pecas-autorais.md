<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Peças autorais

[← Índice da documentação](README.md)

Agentes, skills, hooks e ferramentas que fazem parte do setup e são construídos por mim.

| Peça | Tipo | Fase | O que faz |
|---|---|---|---|
| **Acervo AMtech** | Ferramenta Python | Agora | Converte todos os seus documentos para o Obsidian, separa pessoais, terceiros e escola, e sugere produtos. Já existe: tools/acervo/acervo.py. |
| **CLAUDE.md padrão do Aura** | Contexto do agente | Agora | Modelo copiado para cada repo: stack, camadas, nomes, a árvore apps/ e packages/ e como rodar testes. |
| **Subagente revisor-csharp** | Agente do Claude Code | Agora | Caça seus erros recorrentes: PascalCase, throw sem if, atribuição esquecida no construtor. |
| **Skill /commit** | Skill do Claude Code | Agora | Mensagens no padrão Conventional Commits a partir do diff. |
| **dotfiles + install.sh** | Repositório | Agora | Reconstrói o ambiente (WSL agora, Arch depois) com um comando. |
| **Skill /novo-sistema-aura** | Skill do Claude Code | Próximos 3 meses | Esqueleto de sistema AM: solução Clean Arch, Aspire, compose, testes, CLAUDE.md, Actions e Terraform. |
| **Módulos Terraform do Aura** | Infra como código | Próximos 3 meses | Um módulo reaproveitável (app + PostgreSQL + Key Vault) usado por todos os sistemas, primeiro no Azure. |
| **Hooks do Claude Code + Git** | Hooks | Próximos 3 meses | Pós-edição: dotnet format. pre-commit: gitleaks e testes. post-commit: sinal para o aura-status. |
| **aura-mcp** | Servidor MCP em C# | 3 a 12 meses | Expõe ao agente o catálogo dos 13 sistemas, ADRs e o vault. Projeto de portfólio de IA com sua stack. |
| **Subagente arquiteto-aura** | Agente do Claude Code | 3 a 12 meses | Confere Clean Arch/DDD e escreve o rascunho do ADR. |
| **aura-status** | Ferramenta C# | Próximos 3 meses | Painel de repos, backup, Dependabot e estudos. Depois, módulo da Waybar no Arch. |
| **Laboratório de segurança** | Repositório + VMs | 3 a 12 meses | Configuração das VMs e writeups das máquinas resolvidas. |
| **AMtech Dev Edition** | Scripts sobre o Omarchy | Depois de 12 meses | Sua edição do Arch com tema Aura e ambiente .NET. |
| **Pipeline de treino AMtech** | Repositório Python | 3 a 12 meses | Gera o dataset a partir das suas fontes, treina no Kaggle, avalia, registra no MLflow e publica o GGUF no Ollama. Um comando por etapa. |
| **Projeto dbt das métricas** | Repositório dbt | Próximos 3 meses | Modelos de vendas, gastos e publicações com testes; o painel de lucro passa a ler daqui. |
