---
tags: [ferramenta-pessoal, portfolio-ams, aprendizado]
tipo: ferramenta-pessoal
status: completo
---

# aura-queue — Documento de Projeto Final
### Fila de mensagem mínima — uso 100% interno, sem modelo de receita (razão explicada na seção 9)

---

## 1. Visão do produto

Fila de mensagem mínima, em memória ou sobre o Redis já usado no stack Aura, com `Publish(evento)` e `Subscribe(tipo)`. Ensina o mecanismo central de comunicação assíncrona entre sistemas — quem publica não sabe quem consome — sem a escala de bilhões de mensagens/segundo, replicação e particionamento do Kafka real.

**Público:** exclusivamente interno — os próprios sistemas do portfólio Aura, quando dois ou mais precisarem se avisar de algo sem chamar API um do outro diretamente.

---

## 2. Funcionalidades completas

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Publicação de evento | `Publish<T>(evento)` grava o evento na fila | Novo |
| Assinatura de evento | `Subscribe<T>(handler)` registra consumidor por tipo | Novo |
| Timeout de processamento | Handler que não responde em tempo configurável é descartado, sem travar o publicador | Novo |
| Log de falha | Evento que nenhum handler conseguiu processar fica registrado, não desaparece silenciosamente | Novo |

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | `Publish<T>(evento)` grava o evento numa fila em memória/Redis | Núcleo do desacoplamento — quem publica não sabe quem consome |
| RF02 | `Subscribe<T>(handler)` registra múltiplos consumidores por tipo de evento | Permite mais de um sistema reagir ao mesmo evento |
| RF03 | Timeout por handler, sem travar o restante da fila | Um consumidor lento nunca bloqueia os outros |
| RF04 | Log de evento não processado por nenhum handler | Evita perda silenciosa de evento importante |

---

## 4. Sistemas e interfaces paralelas

| Sistema Aura | Papel | Evento típico |
|---|---|---|
| AM Kaixara | Publica | "Venda concluída" |
| AM Rendara | Consome | Reage à venda pra registrar receita |
| AuraNotifications | Consome | Dispara notificação relacionada ao evento |

Não há interface de usuário final — é infraestrutura interna, consumida só por código de outros sistemas Aura.

---

## 5. Requisitos Não Funcionais (RNF)

| ID | Aplicação no aura-queue | Para que serve |
|---|---|---|
| Desempenho | Publicação não bloqueia o sistema publicador — sempre assíncrona | Sistema que publica não trava esperando consumidor processar |
| Confiabilidade | Evento não processado fica registrado em log, nunca descartado silenciosamente | Rastreabilidade mínima sem a complexidade de garantia de entrega distribuída do Kafka |

---

## 6. Segurança de nível profissional

Uso exclusivamente interno, sem exposição de rede externa por padrão — roda dentro do mesmo ambiente de produção dos sistemas Aura, protegido pela mesma rede/VLAN já definida em [[infraestrutura-fisica-10-anos]]. Se algum dia precisar de acesso externo, exigiria autenticação própria — não planejado hoje.

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Biblioteca/serviço interno do portfólio Aura, nunca distribuído ou instalado por terceiros — não é produto.

---

## 8. Deploy e CI/CD

Parte do pipeline padrão de cada sistema Aura que o consome — sem pipeline de deploy próprio e separado.

---

## 9. Modelo de receita

**Nenhum, por decisão deliberada.** Quem precisa de fila de mensagem de verdade já usa RabbitMQ ou Kafka gratuitos e maduros — uma versão "simples" feita por um dev solo não tem diferenciação possível nessa categoria. Detalhe completo da análise em [[veredito-clonar-ou-nao-ferramenta-paga]].

---

## 10. Status atual de desenvolvimento

Não iniciado — só entra quando 2+ sistemas Aura precisarem se comunicar de fato, ver [[automacao-ordem-de-execucao]].

---

## 11. Pendências e decisões em aberto

1. Decidir entre implementação em memória (mais simples) ou sobre Redis (sobrevive a reinício do processo) — só decidir quando o primeiro caso de uso real aparecer
2. Nenhuma outra pendência — escopo deliberadamente mínimo

---

## 🔗 Documentos relacionados
- [[painel-central-arquitetura-todas-fases]] — a arquitetura de fonte plugável que este documento complementa
- [[aura-status-documento-projeto-final]] — a única das 4 ferramentas com modelo de receita real
- [[veredito-clonar-ou-nao-ferramenta-paga]] — por que não clonar Kafka
- [[template-documento-projeto-final]] — o padrão que este documento segue, igual aos 23 sistemas de negócio
