# Celular ligado ao setup (v2.28)

Um comando liga tudo: `just ligar`. Seguro para rodar de novo; o que já está pronto é pulado.

## Os dois caminhos do celular

| Caminho | Quando usar | Precisa de crédito do Claude? |
|---|---|---|
| **App do Claude → aba Code → "Setup AMtech"** (Remote Control) | Conversar e criar em tempo real, vendo o que o agente faz no seu notebook | Sim (plano Pro ou Max) |
| **Telegram → `/pedir TEXTO`** (fila) | Mandar um pedido e receber o resultado depois, num ramo ou PR em rascunho | Não: usa o Claude enquanto houver; depois a cota grátis do Gemini; depois o modelo local |

Os dois rodam **no seu notebook**: arquivos, ferramentas e conectores do setup. Nada vai para a nuvem além do que cada IA precisa ler.

## Como a fila decide

1. O **motor de decisão** desce a escada. Pedido de aprovar, pagar ou publicar volta para você; o que já existe no setup é respondido com o que já está pronto.
2. Abre uma **worktree** separada (`~/dev/.fila/ID`, ramo `fila/ID`). A sua pasta de trabalho não é tocada.
3. Tenta os motores em ordem: **Claude Code** (`claude -p`) → **aider + Gemini grátis** (pelo LiteLLM, ou direto se o Docker estiver desligado) → **aider + Ollama** (`qwen2.5-coder:7b`, sem internet).
   Dado sensível vai direto para o local. Quando o Claude avisa que o limite acabou, ele sai da fila por 5 h.
4. Faz commit, abre **PR em rascunho** se o `gh` estiver logado e avisa no Telegram. **Nunca faz merge.**

Outro repositório: comece com `@nome-da-pasta`, por exemplo `/pedir @catalogo-html corrigir o menu no celular`.

## Primeira vez (uma vez só)

1. `cd ~/dev/dev-setup && just ligar --simular` e depois `just ligar`.
   Se avisar do systemd: no PowerShell, `wsl --shutdown`, abra o Ubuntu e rode `just ligar` de novo.
   O Windows pede administrador uma vez: cria a tarefa que liga o Ubuntu no login e, **só na tomada**, deixa o notebook sem dormir e com a tampa fechada sem suspender. Para desfazer: `scripts/windows/manter-ligado.ps1 -Desfazer`.
2. **Remote Control:** `claude remote-control` na pasta do dev-setup → `y`, `y`, `2` (worktree) → leia o QR com o celular → `Ctrl+C` → `touch ~/.config/amtech/remoto-aceito && just ligar`.
3. **Telegram:** passos `re-bot`, `re-env` e `re-id` do roteiro (`just agora`). Depois `just ligar` liga o bot sozinho.
4. **Cota grátis:** chave do Google AI Studio em `infra/ia/.env` (`GEMINI_API_KEY=`), cópia no KeePassXC.
5. **Teste:** `/pedir adicionar uma linha de teste no FILA-TESTE.md` e confira o aviso.

## Dia a dia

- `just ligado`: o que está no ar.
- `just pedir "texto"` / `just fila`: o mesmo do Telegram, pelo terminal.
- `just desligar`: para os serviços.
- Logs: `journalctl --user -u amtech-fila -f` (ou `amtech-remoto`, `amtech-bot`).

## Limites honestos

- O notebook precisa estar **ligado, na tomada e com internet**. Desligado, nada responde (a VM da fase Soberania resolve isso depois).
- O modelo local (7B na GTX 1650 de 4 GB) é lento e erra mais: bom para mudanças pequenas e bem descritas, fraco para arquitetura. Para o pesado, espere o Claude voltar.
- O Remote Control em modo servidor desiste depois de ~10 min sem rede; o serviço reinicia em 30 s quando a rede volta.
- Toda mudança chega como ramo ou PR em rascunho: **você revisa antes de entrar**.
