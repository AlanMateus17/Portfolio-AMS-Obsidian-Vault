---
tags: [planejamento, portfolio-ams]
tipo: planejamento
status: completo
---

# Template — Documento de Projeto Final de Sistema
### Estrutura fixa, usada em todo sistema do portfólio a partir de agora

Todo "Documento de Projeto Final" segue exatamente estas seções, nesta ordem. Se uma seção não se aplica ao sistema em questão (ex: hardware num sistema sem componente físico), ela **permanece no documento com a justificativa explícita do porquê não se aplica** — nunca é omitida silenciosamente, porque omissão silenciosa foi exatamente o problema identificado no documento do AM Rotara.

1. **Visão do produto** — o que é, e o diferencial de inovação em relação ao que já existe no mercado
2. **Funcionalidades completas (estado final)** — por módulo, cobrindo tudo que o sistema terá quando pronto, não só o MVP
3. **Requisitos Funcionais (RF)** — lista formal com ID (RF01, RF02...), descrição do requisito, e uma coluna explícita de **"para que serve"** — nunca só a descrição técnica sem o porquê. Cada funcionalidade da seção 2 deve ter pelo menos um RF correspondente; se não tem, ou a funcionalidade está mal definida, ou o RF está faltando.
4. **Sistemas e interfaces paralelas por perfil de usuário** — todo sistema com mais de um tipo de usuário precisa mapear, para cada perfil, a interface/app/fluxo que ele usa — e garantir que nenhum perfil fica sem caminho de uso completo (cadastro → uso → suporte). Isso inclui perfis "internos" (operação/suporte do próprio Alan), não só os perfis pagantes.
5. **Requisitos Não Funcionais (RNF) — próprios + transversais** — mesmo padrão do RF: ID, descrição, e "para que serve", referenciando os documentos RNFT aplicáveis (série original RNFT01-10, série de escala RNFT-E01-E06, série de segurança RNFT-S01-S06) mas sempre explicando a aplicação específica a este sistema, não só citando o ID
6. **Segurança de nível profissional** — aplicação concreta do checklist do documento de Distribuição/Segurança a este sistema especificamente, não só uma referência genérica
7. **Hardware, instalador e distribuição** — se aplicável, detalhado; se não aplicável, a seção permanece com a justificativa (ex: "SaaS puro, sem componente físico, distribuição via pacote comercial padrão")
8. **Deploy e CI/CD** — pipeline, ambiente de produção, decisões de infraestrutura
9. **Modelo de receita** — todas as fontes, incluindo pacotes comerciais aplicáveis
10. **Status atual de desenvolvimento** — o que já existe em código vs. o que é só planejamento; se nada foi codificado ainda, a seção diz isso explicitamente
11. **Pendências e decisões em aberto** — tudo que ainda depende de uma escolha sua antes do documento ser considerado fechado

Esse é o padrão. Auditoria de conformidade (data desta atualização): **nenhum dos 5 documentos completos até agora (AM Kaixara, AM Rotara, AuraVet, AM Consertta, AM Rendara) estava 100% aderente** — AM Kaixara/Delivery/AM Rendara não tinham RF formal nenhum, e AuraVet/AM Consertta tinham RF sem coluna de propósito. Todos os 5 precisam de correção, aplicada em sequência.
