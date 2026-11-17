# 0018 · Um plano de estudo só: o PLANO-PASSO-A-PASSO do vault

- **Status:** aceita
- **Data:** 2026-11-17
- **Substitui em parte:** o item 3 do [ADR 0013](0013-um-vault-e-o-plano-mestre.md) (o plano do eixo como plano mestre).

## Contexto

Em 17/11/2026 havia dois planos de 12 meses que não batiam:

1. **O vault** (`07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md`, 13/11): AM Gestão como produto, Python no mês 7, Go ativo, rotina montada sobre os horários reais (escola, restaurante, cães, Licenciatura).
2. **O setup** (`docs/plano-eixo.md`): AM Rendara no trimestre 2, Python no trimestre 1, 4 h por dia, semana do Professor diferente da rotina real.

Além disso, as mudanças de 13/11 (ADR 0017, stack TypeScript + Python) foram feitas só no espelho da pasta 11 do vault e nunca chegaram a este repositório. O `just professor hoje` continuava ensinando C#/.NET.

## Decisão

1. **A fonte do estudo é o `PLANO-PASSO-A-PASSO.md` do vault.** O `docs/plano-eixo.md` vira um resumo que aponta para ele. Se discordarem, vale o vault e este repositório é corrigido.
2. **A semana do Professor segue a rotina real do vault:** segunda e quarta ofício e setup; terça a base do Akita; quinta o bloco profundo (ofício, setup, finanças); sexta matemática; sábado ofício leve e física; domingo folga.
3. **Calibrado em ~20 h por semana.** As 4 h por dia viram bônus, nunca dívida (resolve a divergência da seção 8 do método do Professor).
4. **Trilha nova `base` no currículo:** 24 módulos com os episódios de fundamentos do Akita (computador, Linux, back-end, redes, concorrência, memória, criptografia, hardware, devops, estruturas de dados, bancos, IA), um por semana.
5. **IA entra em TypeScript no trimestre 1** (chamada de API com saída validada) e RAG em TypeScript no trimestre 2. Python continua no trimestre 3, para dados e IA local.
6. **Trilha R (revisar código de IA)** a partir do mês 2, porque o setup é feito para a IA escrever e o Alan conferir.
7. **A pasta 11 do vault não se edita à mão** (regra do ADR 0013 reforçada): mudança no setup é feita aqui e espelhada.

## Consequências

- O roteiro do eixo e o recrutador continuam valendo; os marcos de trimestre falam em AM Gestão (ADR 0017), não em AM Rendara.
- O calendário real começou em 17/11/2026; cada mês do plano anda ~2 semanas.
