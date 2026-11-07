# Esteira de sites (modelo de repositório)

Copie esta pasta para o repositório do site e rode `bash ~/dev/dev-setup/scripts/wsl/regras-ia.sh <pasta>` para criar o AGENTS.md.

1. Abra uma issue com a ficha (.github/ISSUE_TEMPLATE/site.yml).
2. Atribua a issue ao Copilot (agente na nuvem). Ele abre um PR. Se errar, peça o ajuste no próprio PR ou troque de agente.
3. O workflow `qualidade` confere HTML, links, acessibilidade e a nota do Lighthouse (desempenho 80+, acessibilidade e SEO 90+; ajuste em .lighthouserc.json). O relatório fica nos artefatos da execução: mande para o cliente como prova de qualidade. A rotina do Claude revisa contra o AGENTS.md.
4. A prévia sobe no Cloudflare Pages (ligue o repositório ao Pages uma vez). Abra no celular.
5. Você aprova o PR. O merge publica na Hostinger pelo deploy por push (ligue uma vez no painel ou com a skill deploy-to-hosting).

Regras para os agentes neste repositório (acrescente ao AGENTS.md):
- Uma issue, um PR, uma mudança.
- Sem dependência nova sem dizer o motivo no PR.
- Sem dado pessoal de cliente final, sem chave ou senha no código.
- Imagens só as anexadas na issue ou geradas por você com licença de uso.
