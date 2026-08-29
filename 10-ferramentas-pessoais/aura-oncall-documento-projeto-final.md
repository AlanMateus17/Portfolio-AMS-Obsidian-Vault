---
tags: [ferramenta-pessoal, portfolio-ams, aprendizado]
tipo: ferramenta-pessoal
status: completo
---

# aura-oncall — Documento de Projeto Final
### Escalonamento de incidente mínimo — extensão do aura-notifications, uso 100% interno, sem modelo de receita (razão explicada na seção 9)

---

## 1. Visão do produto

Escalonamento de incidente mínimo — extensão do `aura-notifications` já existente no portfólio, não projeto novo do zero. Ensina como alerta vira ação: se ninguém confirma em X minutos, escala pra outro canal/pessoa, em vez de ficar sem resposta.

**Público:** exclusivamente interno — só relevante quando houver mais de uma pessoa respondendo incidente. Sozinho, alerta direto no celular via Uptime Kuma já resolve, sem escalonamento.

---

## 2. Funcionalidades completas

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Recebimento de alerta | Recebe alerta vindo do Uptime Kuma ou de outro sistema de monitoramento | Reaproveitado — `aura-notifications` |
| Aguardo de confirmação | Espera confirmação por tempo configurável | Novo |
| Escalonamento | Reenvia/escala pra outro canal ou pessoa se não confirmado no prazo | Novo |

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Reenviar alerta não confirmado após tempo configurável | Garante que alerta crítico não fica sem resposta |
| RF02 | Escalar pra canal/pessoa diferente após N reenvios sem confirmação | Cobre o cenário de a primeira pessoa não conseguir responder |

---

## 4. Sistemas e interfaces paralelas

| Perfil | Interface |
|---|---|
| Você, hoje | Notificação direta (celular), sem escalonamento — suficiente sozinho |
| Time futuro (se houver) | Escalonamento entre pessoas, via canal já configurado no `aura-notifications` |

---

## 5. Requisitos Não Funcionais (RNF)

| ID | Aplicação no aura-oncall | Para que serve |
|---|---|---|
| Confiabilidade | Alerta crítico nunca fica "preso" esperando uma pessoa só | Reduz risco de incidente real ficar sem resposta |
| Simplicidade | Reaproveita 100% da infraestrutura do `aura-notifications`, sem canal novo a manter | Menor superfície de manutenção |

---

## 6. Segurança de nível profissional

Nenhum requisito adicional além do que `aura-notifications` já cobre — este documento só adiciona lógica de temporização e escalonamento, sem tocar em dado sensível novo.

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Extensão de serviço interno já existente, nunca distribuído a terceiros.

---

## 8. Deploy e CI/CD

Nenhum deploy separado — faz parte do deploy do `aura-notifications`.

---

## 9. Modelo de receita

**Nenhum.** Só relevante com mais de uma pessoa respondendo incidente — sozinho, alerta direto no celular via Uptime Kuma já resolve sem escalonamento. PagerDuty e Opsgenie já têm camada gratuita que cobre esse uso de sobra pra quem realmente precisa comprar isso pronto, ver [[veredito-clonar-ou-nao-ferramenta-paga]].

---

## 10. Status atual de desenvolvimento

Não iniciado — só relevante se/quando houver equipe respondendo incidente junto com você.

---

## 11. Pendências e decisões em aberto

1. Nenhuma pendência técnica real — a única condição de entrada é ter uma segunda pessoa no time, o que hoje não está no horizonte

---

## 🔗 Documentos relacionados
- [[painel-central-arquitetura-todas-fases]] — a arquitetura de fonte plugável que este documento complementa
- [[aura-status-documento-projeto-final]] — a única das 4 ferramentas com modelo de receita real
- [[veredito-clonar-ou-nao-ferramenta-paga]] — por que não clonar PagerDuty/Opsgenie
- [[aura-notifications-documento-projeto-final]] — o serviço que este documento estende
- [[template-documento-projeto-final]] — o padrão que este documento segue, igual aos 23 sistemas de negócio
