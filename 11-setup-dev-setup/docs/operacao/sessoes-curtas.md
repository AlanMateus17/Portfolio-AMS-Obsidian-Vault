# Conversas curtas: gastar o mínimo de limite

[← Operação do grupo](README.md)

**Por que o limite acaba:** a cada mensagem, a IA relê a conversa inteira. Uma conversa de 100 mensagens custa muito mais que 10 conversas de 10. O remédio é estrutural, não força de vontade.

## O protocolo

1. **Uma conversa = uma tarefa** (um passo do roteiro, uma aula, um cliente).
2. **Comece com o pacote de contexto** (poucas centenas de tokens), nunca colando tudo:
   ```bash
   python3 ~/dev/dev-setup/tools/sessao/contexto.py --passo ia-mcp | clip.exe
   ```
   Cole na conversa nova. Para o estado geral: `--resumo`.
3. **Termine pedindo 5 linhas para o `ESTADO.md`** e faça commit. A próxima conversa começa dali.
4. **Rascunho barato, revisão cara:** rascunhe no NotebookLM/Gemini, ChatGPT Go, DeepSeek ou modelo local; revise no Claude.
5. **No Claude Code:** `/clear` entre tarefas, `/compact` quando a sessão crescer, CLAUDE.md curto (as regras únicas têm menos de 30 linhas).
6. **Memória automática:** o ai-memory 2.0 (do Akita) dá um briefing do projeto no começo de cada sessão do Claude Code, sem você colar nada.
7. **Veja o limite antes de começar:** o ai-usagebar (do Akita) mostra o uso de Claude, Codex, Z.AI e OpenRouter no terminal.
8. **Resultado em arquivo, não em texto longo no chat:** peça para gravar no repositório.
9. **Modelo certo:** o mais leve para tarefas simples; o mais forte só para planejar e revisar.

## Sinais de que é hora de abrir conversa nova

- A conversa passou de ~30 mensagens ou mudou de assunto.
- A IA começa a esquecer decisões do começo.
- Você precisou colar o mesmo contexto duas vezes.
