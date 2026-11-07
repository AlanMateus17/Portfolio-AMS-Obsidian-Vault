# 0013 · Um vault só, o setup espelhado nele, e o plano do eixo como plano mestre

- **Status:** aceita
- **Data:** 2026-11-06
- **Substitui em parte:** a decisão de out/2026 de pôr o dev-setup inteiro dentro do vault.

## Contexto

O estudo e o setup estavam separados em três lugares:

1. **O vault do Alan** (Portfolio-AMS-Obsidian-Vault, privado), com o Sumário Único (14 Passos), o Cartão "Você está aqui", o Plano Mestre e uma cópia do dev-setup na pasta 11, parada em 27/10.
2. **O dev-setup**, 21 versões à frente dessa cópia.
3. **Um segundo cofre**, que o `vault.sh` criaria em ~/dev/notas, onde o Professor e a Escola Akita gravavam.

Além disso, os dois planos de estudo divergiam. O Sumário punha o AM Kaixara como 1º sistema (jan a mar/2027). O plano do eixo (ADR 0011) põe o AM Rendara no 2º trimestre e software com finanças como eixo.

## Decisão (escolhas do Alan)

1. **Um vault só, o dele.** O `vault.sh` clona o Portfolio-AMS-Obsidian-Vault em ~/dev/notas, ou só completa as pastas se ele já estiver lá. O Professor grava em `07-estudo-e-carreira/professor`, as fichas duplas vão para `09-material-producao-simultanea/fichas-duplas` e as notas da Escola Akita para `07-estudo-e-carreira/akita`.
2. **O dev-setup continua repositório próprio** (CI, testes, geradores) e é **espelhado** na pasta 11 do vault por `tools/vault/espelho.py`. O espelho roda no `just docs`, no `just vault-espelho` e na manutenção de domingo. É uma cópia exata: o que sai do setup sai do vault, e a pasta 11 não se edita no Obsidian.
3. **O plano mestre é o plano do eixo com o Professor.** A porta do dia passa a ser `just professor hoje` (estudo) e `just agora` (setup). O Sumário Único, o Cartão e o Plano Mestre do vault ganham um aviso apontando para eles. O conteúdo dos 14 Passos fica como fonte do currículo, e nada é apagado.

## Por que não juntar os repositórios de fato

As notas do vault se salvam sozinhas a cada 10 minutos (Obsidian Git). Isso dispararia o CI do setup o tempo todo, e todos os caminhos `~/dev/dev-setup` mudariam. O espelho entrega o mesmo resultado para quem lê (tudo no Obsidian) sem esses custos.
