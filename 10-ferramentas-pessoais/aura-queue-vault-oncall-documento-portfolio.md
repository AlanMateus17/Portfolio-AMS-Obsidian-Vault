---
tags: [ferramenta-pessoal, portfolio-ams, aprendizado]
tipo: ferramenta-pessoal
status: completo
---

# aura-queue, aura-vault-simples, aura-oncall — Documento de Portfólio
### Diferente do aura-status: estas 3 são documentadas como peça de portfólio e aprendizado, não como produto de venda — a razão está explicada em cada uma, não é recusa sem justificativa

> **Por que não recebem o modelo de receita dos outros 23 sistemas:** as três competem contra ferramenta madura, testada por milhões de usuários, geralmente com camada gratuita real (Kafka/RabbitMQ, HashiCorp Vault open source, PagerDuty free tier). Um cliente pagando por uma versão "simples" feita por um dev solo, numa categoria onde confiança e histórico importam tanto (principalmente segurança), não é um plano de negócio real — é o tipo de honestidade que vale mais que forçar um modelo de receita que não existe de verdade.

---

## aura-queue

### 1. Visão
Fila de mensagem mínima em memória (ou sobre o Redis já no stack), com `Publish(evento)` e `Subscribe(tipo)` — ensina o mecanismo central de comunicação assíncrona entre sistemas, sem a escala de bilhões de mensagens/segundo do Kafka real.

### 2. Funcionalidades
Publicar evento tipado; múltiplos assinantes por tipo de evento; sem replicação, sem particionamento, sem garantia de entrega distribuída.

### 3. RF
| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | `Publish<T>(evento)` grava o evento numa fila em memória/Redis | Núcleo do desacoplamento — quem publica não sabe quem consome |
| RF02 | `Subscribe<T>(handler)` registra um consumidor por tipo de evento | Permite múltiplos sistemas reagirem ao mesmo evento |

### 4-8. Sistemas paralelos, RNF, segurança, distribuição, deploy
Não aplicável em profundidade — uso interno, entre sistemas Aura, nunca exposto a cliente externo.

### 9. Modelo de receita
**Nenhum.** Uso 100% interno — resolve comunicação entre AuraPOS/AuraWealth/etc quando precisarem se avisar de algo sem chamar API um do outro diretamente. Não é vendável: quem precisa de fila de mensagem de verdade já usa RabbitMQ ou Kafka gratuitos, maduros.

### 10-11. Status e pendências
Não iniciado — só entra quando 2+ sistemas precisarem conversar entre si (ver [[ordem-e-sequencia-de-execucao-automacoes]]).

---

## aura-vault-simples

### 1. Visão
Cofre de segredo mínimo — API pequena, autenticada, que guarda segredo criptografado e devolve só pra quem tem permissão. Ensina por que segredo não deveria nunca ficar em arquivo de configuração, e como um serviço central de segredo funciona.

### 2. Funcionalidades
Guardar segredo criptografado; devolver segredo mediante autenticação; sem política granular de acesso, sem rotação automática distribuída (o que o Vault real tem).

### 3. RF
| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Armazenar segredo criptografado no banco, associado a um sistema/serviço | Nunca guarda segredo em texto puro |
| RF02 | Devolver segredo mediante requisição autenticada | Só quem tem permissão explícita recebe o valor |

### 4-8. Sistemas paralelos, RNF, segurança, distribuição, deploy
Uso 100% interno, entre os próprios sistemas Aura em produção. **Nunca exposto como produto** — um cofre de segredo malfeito é pior que nenhum cofre; o risco reputacional de vender "segurança" sem o rigor de anos que o Vault real tem é real demais pra valer a pena.

### 9. Modelo de receita
**Nenhum, por decisão deliberada de segurança, não só de mercado.** Mesmo que houvesse demanda, vender gerenciamento de segredo malfeito é o tipo de risco que pode custar reputação profissional inteira se der errado — o oposto do que este documento inteiro (e o `seguranca-e-ferramentas-todas-as-frentes`) defende.

### 10-11. Status e pendências
Não iniciado — só entra no Passo 10 (primeira produção real).

---

## aura-oncall

### 1. Visão
Escalonamento de incidente mínimo — extensão do `aura-notifications` que você já tem, não projeto novo do zero. Ensina como alerta vira ação: se ninguém confirma em X minutos, escala pra outro canal/pessoa.

### 2. Funcionalidades
Recebe alerta; aguarda confirmação; reenvia/escala se não confirmado no prazo.

### 3. RF
| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Reenviar alerta não confirmado após tempo configurável | Garante que alerta crítico não fica sem resposta |

### 4-8. Sistemas paralelos, RNF, segurança, distribuição, deploy
Extensão de `aura-notifications` — herda toda a infraestrutura que já existe, sem sistema novo.

### 9. Modelo de receita
**Nenhum.** Só relevante com mais de uma pessoa respondendo incidente — sozinho, alerta direto no celular via Uptime Kuma já resolve, sem escalonamento. PagerDuty/Opsgenie já têm camada gratuita que cobre esse uso de sobra pra quem realmente precisa comprar isso pronto.

### 10-11. Status e pendências
Não iniciado — só relevante se/quando houver equipe.

---

## Resumo — por que a assimetria com aura-status é intencional, não inconsistência

O `aura-status` tem um ângulo que os outros três não têm: **ninguém mais construiu especificamente pra TDAH, com esse desenho de baixa carga cognitiva** — é diferenciação real. Fila de mensagem, cofre de segredo e escalonamento de incidente **já são resolvidos**, de graça, por ferramentas com anos de maturidade — não existe diferenciação possível numa versão "simples" feita por uma pessoa só. Documentar os três com o mesmo rigor técnico dos 23 sistemas (o que fizemos aqui) sem forçar um modelo de receita que não existe é mais útil do que fingir que os quatro são igualmente promissores.

---

## 🔗 Documentos relacionados
- [[aura-status-documento-projeto-final]] — a única das 4 com modelo de receita real
- [[painel-central-arquitetura-todas-fases]] — a arquitetura de fonte plugável que conecta os 4
- [[veredito-clonar-ou-nao-ferramenta-paga]] — a análise original de por que construir versão pequena, não clone completo
