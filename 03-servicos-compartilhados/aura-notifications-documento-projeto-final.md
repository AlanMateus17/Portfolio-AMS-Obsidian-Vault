---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-notifications — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Segundo dos 4 serviços compartilhados pendentes.

---

## 1. Visão do produto

Serviço central de notificação (WhatsApp Business API, push, e-mail, SMS), consumido por todos os sistemas que precisam avisar o cliente de algo — status de pedido, lembrete de consulta, boleto, aviso de assembleia. Hoje implementado separadamente em pelo menos 5 sistemas, cada um pagando e configurando sua própria integração.

**Diferencial de inovação:** além de eliminar duplicação, um serviço central de notificação abre uma possibilidade que nenhum sistema isolado tem — throttling e priorização inteligente por cliente (evitar que um mesmo morador do AM Predara receba 5 notificações separadas de 5 sistemas diferentes no mesmo minuto, se algum dia ele for cliente de mais de um produto Aura).

---

## 2. Funcionalidades completas (estado final)

### 2.1 Canais suportados
- WhatsApp Business API (canal principal, já mencionado em quase todo sistema do portfólio)
- Push notification (app/PWA)
- E-mail transacional
- SMS (fallback, quando os outros canais falharem ou não forem aplicáveis)

### 2.2 Template de mensagem por tipo de evento
- Cada sistema consumidor registra seus próprios templates (status de OS, lembrete de consulta, boleto gerado, aviso de assembleia), mas todos passam pelo mesmo motor de envio

### 2.3 Fila e re-tentativa
- Envio assíncrono via fila (mesmo padrão RNFT-E03 já formalizado), com re-tentativa automática em falha de canal

### 2.4 Preferência de canal por cliente
- Cliente final pode escolher canal preferido (ex: só WhatsApp, nunca e-mail) quando o sistema consumidor expuser essa opção

### 2.5 Throttling entre sistemas (diferencial da seção 1)
- Se o mesmo destinatário for cliente de mais de um produto Aura, o serviço evita rajada de notificação simultânea de sistemas diferentes — agrupa ou espaça envios não urgentes

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Expor API única de envio, com canal (WhatsApp/push/e-mail/SMS) e template parametrizado | Elimina a duplicação de integração hoje presente em pelo menos 5 sistemas |
| RF02 | Processar envio de forma assíncrona via fila, com re-tentativa automática | Evita que uma falha pontual de canal derrube uma notificação importante silenciosamente |
| RF03 | Permitir fallback automático de canal (ex: WhatsApp falhou, tenta SMS) para notificação crítica | Aumenta a chance real de entrega de aviso importante (ex: status de OS, boleto vencendo) |
| RF04 | Registrar preferência de canal por cliente, quando exposta pelo sistema consumidor | Respeita a escolha do usuário final, reduzindo cancelamento de opt-in por excesso de canal |
| RF05 | Aplicar throttling entre sistemas para o mesmo destinatário | Evita experiência ruim de cliente que usa mais de um produto Aura recebendo notificação duplicada/excessiva |
| RF06 | Registrar log de entrega por notificação (enviado, entregue, falhou) | Permite auditoria de "o cliente realmente recebeu o aviso" em caso de disputa |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Sistema consumidor (todos os do portfólio)
- **Uso:** registra template, dispara envio via API, consulta status de entrega
- Não tem usuário humano direto — máquina a máquina

### 4.2 Cliente final (destinatário)
- **Uso:** recebe notificação pelo canal escolhido; se exposto pelo sistema consumidor, pode configurar preferência de canal
- **Suporte:** canal do sistema de origem, não deste serviço

### 4.3 Você (monitoramento de entregabilidade)
- **Uso:** acompanhar taxa de entrega/falha por canal, decidir se algum provedor precisa ser trocado
- **Lacuna:** sem painel formal ainda, mesma recorrência do portfólio

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-notifications | Para que serve |
|---|---|---|
| RNFT-E03 (fila para picos) | Central aqui, não só relevante — todo envio já nasce assíncrono por design (RF02) | Evita que pico de notificação (ex: fim de mês, cobrança de condomínio) sobrecarregue qualquer sistema consumidor |
| RNFT02 (isolamento de falha, série original) | Indisponibilidade do serviço não pode bloquear a operação principal do sistema consumidor (ex: PDV continua vendendo mesmo sem conseguir notificar) | Notificação é valor agregado, nunca dependência bloqueante de operação crítica |
| RNFT06 (LGPD) | Número de telefone, e-mail e preferência de contato são dado pessoal | Cumpre obrigação legal sobre dado de contato |
| Confiabilidade de entrega crítica (próprio) | Notificação classificada como crítica (ex: status de OS, boleto) deve ter fallback de canal (RF03); notificação não crítica não precisa | Evita gastar o mesmo esforço de garantia de entrega em toda notificação, priorizando o que realmente importa |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-notifications |
|---|---|
| Dados | Concentra número de telefone e e-mail de clientes de todo o portfólio — superfície de valor para spam/phishing se comprometido |
| Rede/API | Mesmo padrão de credencial própria por sistema consumidor, nunca compartilhada |
| Auditoria externa | Prioridade média — não é SPOF de acesso (diferente do `aura-identity`), mas concentra dado de contato de todos os clientes |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno, consumido via API, sem instalador nem distribuição direta.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Não exige a mesma redundância crítica do `aura-identity`/`aura-licensing` (uma indisponibilidade aqui atrasa notificação, não impede operação principal de nenhum sistema, dado o RNFT02 já aplicado).

---

## 9. Modelo de receita

Não gera receita direta — é infraestrutura de suporte a experiência, com custo (API de WhatsApp/SMS) repassado indiretamente no preço de assinatura de cada sistema consumidor. Diferente do `aura-identity` e do `aura-licensing`, não há ângulo claro de venda B2B externa — notificação transacional é *commodity* de mercado (Twilio, Zenvia e afins já dominam esse espaço), sem diferencial suficiente pra competir como produto à parte.

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização deste serviço.

---

## 11. Pendências e decisões em aberto

1. **Provedor de WhatsApp Business API** — decisão ainda não tomada (oficial Meta vs. BSP terceirizado).
2. **Provedor de SMS/e-mail transacional** — mesma pendência.
3. **Regra de throttling entre sistemas** (RF05) — critério exato de "o que conta como rajada" ainda não definido.
4. **Painel de monitoramento de entregabilidade** (seção 4.3) — ainda sem RF formal.
