# 4 · Regra de três: tarefa repetida vira algoritmo

[← Motor de decisão](README.md)

Vale para 100% das chamadas que **passam pelo roteador**. O que o Alan faz direto no app do Claude, no Copilot do editor ou no Gemini não passa pelo setup, então não é contado.

## Fluxo

1. **Uma porta só:** toda IA do setup (agentes, n8n, scripts) chama pelo LiteLLM + escada.
2. **Registro padronizado:** tipo de tarefa, parâmetros, resposta, custo, se passou na verificação.
3. **Cache exato:** mesma entrada → resposta salva, custo zero.
4. **Detector de padrão:** mesmo tipo de tarefa 3 vezes, estrutura parecida, aprovada nas 3 → candidata.
5. **Geração:** a IA escreve o script e os testes, com os 3 casos reais como testes, mais casos de borda.
6. **Aprovação do Alan em PR.** Nada é promovido sozinho.
7. **Catálogo:** o script entra e a escada passa a achá-lo nos degraus 1 e 2.
8. **Proteção:** entrada fora do formato ou verificação falhou → volta para a IA e registra; falhas repetidas marcam o script para revisão.

Antes de assumir, o script roda em **modo sombra** ao lado da IA e os resultados são comparados.

## Três níveis de promoção

| Nível | Quando | Exemplo |
|---|---|---|
| Resposta fixa (cache) | Mesma pergunta, mesma resposta | Consultas repetidas |
| Template | Formato fixo, conteúdo muda; a IA só preenche | Estrutura de aula, proposta |
| Script completo | A regra inteira cabe em código | Converter, calcular, organizar, validar |

## Limites

- Reconhecer "a mesma tarefa" funciona bem com tarefas padronizadas por tipo; com texto livre, o detector erra às vezes.
- Tarefa criativa não vira script; no máximo template.
- Script gerado por IA pode ter erro: testes e aprovação são obrigatórios.
- Script desatualiza quando a entrada muda: o passo 8 existe para isso.

Medida: quantas chamadas de IA cada script evitou e quanto valeriam. Depende da escada, do catálogo e do registro (sem registro não há como contar as 3 repetições).
