# 0014 · Motor de decisão: a IA propõe, o código decide e verifica

- **Status:** aceita
- **Data:** 2026-11-11
- **Detalhes:** [docs/ia/motor](../ia/motor/README.md)

## Contexto

O Alan quer escrever do jeito dele e ter resultado de engenheiro sênior, gastando o mínimo de tokens, créditos e dinheiro, rodando localmente quando possível e sem depender de uma ferramenta só. Também quer entender a fundo cada ferramenta e decidir com números se cria a própria.

## Decisão

1. **Escada de 5 degraus** para todo pedido: pronto → código → automação → IA (local, depois assinatura, API só com renda) → Alan. Estende o `just triagem`.
2. **Determinístico onde houver regra:** dinheiro, segurança, aprovações, infraestrutura, checagens de aulas e o próprio roteador são código testado. A IA só onde há ambiguidade, e sempre verificada.
3. **Porta única de IA (LiteLLM)** com teto que bloqueia, cache e registro de cada chamada.
4. **Regra de três:** tarefa aprovada 3 vezes vira cache, template ou script, gerado com testes, aprovado em PR e rodado em modo sombra antes de assumir.
5. **Chat e Claude Code como principais** enquanto não há renda; API só para automação e produto.
6. **"100% controlado", não "100% recriado":** núcleo próprio, infraestrutura open source auto-hospedada, serviços alugados atrás de adaptadores. Construir só quando a ficha de dissecação mostrar que compensa.
7. **Segurança no CI:** classificação de dados, separação entre agente que lê e agente que age, Syft, ScanCode, Trivy/OSV-Scanner, Semgrep e gitleaks bloqueando o merge.
8. **Nuvem só para o que fica ligado 24 h** (Oracle Always Free na fase 0, Hostinger KVM 2 quando uma renda pagar).

## Consequências

- Versão 0.1: escada, catálogo e registro. O resto depende dos três.
- Nada fica congelado (decisão do Alan, 11/11/2026): o motor entra agora; a ordem de execução segue o roteiro e o limite de 3 frentes "agora".

## Alternativas descartadas

- **Chamar todos os modelos em toda pergunta:** o jeito mais caro de trabalhar.
- **Clonar todas as ferramentas por engenharia reversa:** risco jurídico, impossível para serviços em servidor e manutenção maior que as 7 h semanais.
- **Usar a assinatura do chat como motor de automação:** não é permitido para produto nem automação de terceiros.
