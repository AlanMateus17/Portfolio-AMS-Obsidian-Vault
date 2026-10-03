---
tags: [planejamento, portfolio-ams]
tipo: planejamento
status: completo
---

# O que fazer agora — Ação imediata no portfólio
### Revisado — os itens de "consolidar Documento de Projeto Final" da versão anterior já foram todos concluídos

Este documento responde a uma pergunta prática: **dado tudo que já foi planejado até hoje, o que efetivamente precisa da sua atenção agora?** Não repete o conteúdo de nenhum outro documento — só aponta pra eles e diz a ordem.

---

## 1. Ação imediata (agora)

### 1.1 AM Kaixara — revisar código já escrito contra RNFT-E01 e RNFT-E02
Continua sendo o único sistema com código em produção-alvo já rodando (Sprint 3-4). Antes de empilhar funcionalidade nova, confirme se a lógica atual de baixa de estoque tem proteção de concorrência — ver [kaixara-documento-projeto-final](../02-sistemas-de-negocio/kaixara-documento-projeto-final.md).

### 1.2 Decidir o modelo de seguro/responsabilidade em trânsito do AM Consertta
Continua pendente — decisão de negócio, não técnica, sinalizada no próprio documento do AM Consertta. Precisa ser fechada antes de qualquer código no fluxo de envio.

### 1.3 Decidir `aura-historico`: manter Clojure/Datomic ou revisar pra Marten (.NET)
Mesma pergunta que já foi resolvida pro AM Taskoro (GraphQL híbrido), ainda em aberto aqui — ver [stack-tecnologica](../05-stack-tecnologica/stack-tecnologica.md). Não bloqueia nada tecnicamente, mas vale decidir antes de chegar no bloco de estudo correspondente, não durante.

---

## 2. O que a versão anterior deste documento listava, e já está resolvido

- ~~Formalizar RF/RNF do `aura-licensing`~~ — feito, documento completo em [aura-licensing-documento-projeto-final](../03-servicos-compartilhados/aura-licensing-documento-projeto-final.md)
- ~~Consolidar Documento de Projeto Final de cada sistema~~ — feito, 23 de 23 sistemas/serviços completos
- ~~Loja Virtual sair do estágio de incerteza~~ — feito, RF/RNF formal completo
- ~~Formalizar o Módulo de Ordem de Serviço~~ — feito, absorvido pelo Documento de Projeto Final do AM Consertta
- ~~`aura-goals`, `aura-copilot` sem RF/RNF~~ — feito, ambos completos

---

## 3. Ação de médio prazo (sem mudança da versão anterior)

- Avaliar a certificação CEA/CFP pra destravar a camada de consultoria do AM Rendara — ver [plano-mestre-frentes-alan](plano-mestre-frentes-alan.md)
- Revisitar a vertical de Reprodução & Biotecnologia do AuraVet, condicionada à sua decisão sobre atuar nessa área

---

## 4. O que NÃO fazer agora

- Não iniciar código novo em nenhum sistema além do AM Kaixara antes de chegar nele na sequência de estudo — ver [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md)
- Não tratar `aura-historico`, `aura-analytics` como urgentes — não bloqueiam nenhum sistema comercial de sair do papel

---

## 🔗 Documentos relacionados
- [status-planejamento-portfolio](status-planejamento-portfolio.md) — o inventário completo, revisado
- [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md) — a ordem de estudo/desenvolvimento
