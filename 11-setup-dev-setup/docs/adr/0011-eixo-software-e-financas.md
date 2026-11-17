# 0011 · Eixo profundo: software para finanças, dentro do Grupo AMtech Digital

> **Revisto em parte pelo [ADR 0015](0015-nada-pausado.md) (11/11/2026):** o item 5 (pausas com gatilho) foi retirado. O eixo continua; os temas da lista estão ativos.

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O Alan quer chegar a sênior. Ser sênior em todas as áreas de interesse dele não cabe numa vida: cada uma leva de 5 a 10 anos de prática, e ele tem cerca de 4 horas por dia, além da escola e do restaurante. Ele escolheu o eixo: **desenvolvimento de software e finanças, com o Grupo AMtech Digital como veículo.**

## Decisão

1. **Um T só.** Software é o ofício e finanças é o domínio: o Alan é um dev sênior que constrói sistemas financeiros para pequenas empresas e pessoas (AM Rendara, Caixa da Casa, cobrança e conciliação para os clientes da AMtech Software). As duas coisas são um eixo, não duas trilhas.
2. **O ofício:** .NET 10 + Next.js + PostgreSQL, levados até a produção com cliente pagante, testes, deploy de um comando, backup restaurado, observabilidade e relato de incidente.
3. **O domínio:** contabilidade básica e fluxo de caixa, matemática financeira, tributos do dia a dia (carnê-leão, Simples, Fator R, NFS-e), pagamentos (Pix, Pix Automático, boleto) e, no fim do ano, investimentos e análise de balanço.
4. **Validar antes de construir:** cada sistema financeiro começa como planilha vendida; o sistema só nasce depois de 10 vendas.
5. **Pausado com gatilho:** C/C++ da 42, AM-OS e AM Linux, trilha de pentest (eJPT e OSCP), treino de IA do zero e fine-tuning, robótica pessoal, agro, construção civil, espanhol e mandarim, e a escolha da segunda faculdade. Nada é apagado: tudo volta quando o gatilho do plano chegar (fim do trimestre 4 com a meta de renda batida). Segurança fica no que todo dev sênior precisa (OWASP, segredos, revisão de PR), e IA no uso diário, não no treino de modelos.
6. **Continua:** a Licenciatura em Matemática (já em curso, e serve de base para a matemática financeira), inglês todo dia e a escola até a saída planejada para 2027.
7. **Setup congelado em amplitude:** nenhuma área ou ferramenta nova no setup até a primeira venda da AMtech Software e o primeiro sistema em produção. Consertar e usar pode; expandir, não.

## Consequências

- O plano de 12 meses fica em docs/plano-eixo.md e na fase "Eixo de 12 meses" do roteiro, com um critério de pronto por trimestre (`just agora`).
- Certificações financeiras (ANBIMA, CFP, CNPI) entram depois do ano 1. Elas não tornam ninguém sênior; servem para recomendar investimentos, um objetivo de longo prazo do Alan.
- Toda revisão trimestral é uma decisão do Alan: seguir, ajustar ou mudar o eixo, sempre com o motivo anotado.
