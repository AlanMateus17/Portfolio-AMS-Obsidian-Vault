> **Recuperado em 06/11/2026.** Estes arquivos moravam em `11-setup-dev-setup/tools/plano_mestre` e `11-setup-dev-setup/ferramentas` e foram feitos só no vault (nunca existiram no repositório dev-setup). Quando a pasta 11 virou espelho automático do dev-setup, eles foram apagados por engano e voltaram para cá, numa pasta que o espelho não toca. As três páginas estão em [../../paginas](../../paginas).
>
> **Atenção, está desatualizado:** o `montar.py` liga as fases do roteiro do setup pela posição (`FASE_ETAPA`), e o roteiro ganhou fases novas depois de 27/10 (empresa, eixo, Professor, Escola Akita). Rodar hoje gera um Plano Mestre com etapas trocadas. Desde o ADR 0013, a porta do dia é `just professor hoje` e `just agora`; este gerador fica como referência.
>
> Para rodar mesmo assim, no Ubuntu do WSL: `python3 ~/dev/notas/10-ferramentas-pessoais/plano-mestre/tools/montar.py ~/dev/dev-setup ~/dev/notas /tmp/plano-mestre.json`

# Plano Mestre (setup + estudo num só passo a passo)

Junta `data/implantacao.json` e `data/portfolio.json` deste repositório com o Sumário do vault de estudos.

```bash
python tools/plano_mestre/montar.py . ../Portfolio-AMS-Obsidian-Vault plano-mestre.json
python tools/plano_mestre/gerar_md.py plano-mestre.json ../Portfolio-AMS-Obsidian-Vault/00-PLANO-MESTRE-PASSO-A-PASSO.md
```

`fluxogramas.py docs/ saida.html` junta os 68 diagramas Mermaid dos documentos numa página só.

Rode de novo sempre que mudar uma fase do setup ou um Passo do estudo. O script para com erro se algum código se repetir, e avisa se alguma ligação apontar para um item que não existe ou se um pré-requisito cair numa etapa posterior.
