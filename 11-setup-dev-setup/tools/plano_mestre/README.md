# Plano Mestre (setup + estudo num só passo a passo)

Junta `data/implantacao.json` e `data/portfolio.json` deste repositório com o Sumário do vault de estudos.

```bash
python tools/plano_mestre/montar.py . ../Portfolio-AMS-Obsidian-Vault plano-mestre.json
python tools/plano_mestre/gerar_md.py plano-mestre.json ../Portfolio-AMS-Obsidian-Vault/00-PLANO-MESTRE-PASSO-A-PASSO.md
```

`fluxogramas.py docs/ saida.html` junta os 68 diagramas Mermaid dos documentos numa página só.

Rode de novo sempre que mudar uma fase do setup ou um Passo do estudo. O script para com erro se algum código se repetir, e avisa se alguma ligação apontar para um item que não existe ou se um pré-requisito cair numa etapa posterior.
