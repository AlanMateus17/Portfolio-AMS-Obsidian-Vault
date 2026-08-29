---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# Loja Virtual — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Este era o documento mais imaturo do portfólio — a própria Claude sinalizou incerteza elevada na conversa em que ele foi criado. Esta versão aplica o mesmo rigor de aprofundamento antes de fechar o documento, em vez de reproduzir a versão rasa anterior.

---

## 1. Visão do produto

Módulo de e-commerce **dependente do AuraPOS** — nunca um produto autônomo. O AuraPOS é a fonte única de verdade de produto, preço e estoque; a Loja Virtual nunca mantém cópia própria divergente. Um pedido pago na Loja Virtual gera automaticamente uma venda no AuraPOS, com o mesmo débito de estoque de uma venda de balcão.

**Por que dependente, e não autônomo — decisão de modelo de negócio, não só técnica:** isso reforça a venda do AuraPOS como base do portfólio, e a Loja Virtual como upsell natural. Se o lojista não usa o AuraPOS, a Loja Virtual não funciona sozinha.

**Diferencial de inovação:** diferente de plataforma de e-commerce genérica (Nuvemshop, Loja Integrada), aqui não existe risco de estoque divergir entre canal físico e online — é o mesmo problema estrutural que o Aura Delivery resolve, aplicado a e-commerce puro em vez de logística de entrega.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Catálogo e checkout
- Catálogo público conectado ao AuraPOS (leitura de produto/estoque em tempo real)
- Checkout com pagamento online

### 2.2 Integração com o AuraPOS
- Pedido pago gera venda automática no AuraPOS, com o mesmo débito de estoque de uma venda de balcão
- Painel de gestão de pedido para o lojista

### 2.3 Rastreamento
- Rastreamento de entrega em tempo real — reaproveitando a mesma infraestrutura de geolocalização/notificação do Aura Delivery quando o lojista também usa esse sistema; para lojista sem Delivery, rastreamento fica limitado a status simples (postado/entregue), sem geolocalização ao vivo

### 2.4 Reaproveitamento por outros sistemas
- É a base de "loja online" reaproveitada pelo AuraFix (seção 1.3 daquele documento) e candidata a reaproveitamento futuro pelo AuraVet (loja de produtos veterinários)

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Catálogo público deve refletir produto/estoque do AuraPOS em tempo real, sem cópia própria divergente | É o requisito central que evita o problema mais comum de e-commerce integrado a PDV: dessincronia |
| RF02 | Pedido pago deve gerar venda automática no AuraPOS, com débito de estoque idêntico ao de balcão | Garante que o estoque nunca diverge entre canal, sem exigir sincronização manual |
| RF03 | Painel de gestão de pedido para o lojista (aceitar, preparar, marcar como enviado) | Dá controle operacional sem depender de você como intermediário |
| RF04 | Rastreamento de entrega — completo se o lojista também usa o Aura Delivery, básico (status simples) caso contrário | Não trava o lojista sem Delivery, mas oferece experiência superior a quem tem os dois produtos |
| RF05 | Sistema deve recusar operar sem uma conta AuraPOS ativa vinculada | Reforça a decisão de modelo de negócio de dependência — Loja Virtual nunca deve funcionar isolada |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Cliente final (comprador)
- **Cadastro:** self-service ou checkout como convidado (mesma decisão pendente já registrada no Aura Delivery — vale decidir uma vez, aplicada aos dois)
- **Uso:** navega catálogo, compra, acompanha pedido
- **Suporte:** canal do lojista, não do Grupo AMtech diretamente — mesma lógica do operador de caixa do AuraPOS

### 4.2 Lojista (já usuário do AuraPOS)
- **Cadastro:** não tem cadastro próprio — é uma extensão da conta AuraPOS existente, ativada via `aura-licensing`
- **Uso:** painel de gestão de pedido (RF03)
- **Suporte:** canal com o Grupo AMtech Digital, mesma lacuna do AuraPOS (seção 3.2 daquele documento)

### 4.3 Suporte técnico interno
- Mesma lacuna recorrente do portfólio inteiro.

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação na Loja Virtual | Para que serve |
|---|---|---|
| RNFT-E01 (concorrência de estoque) | Direto — pedido na Loja Virtual decrementa o mesmo estoque do AuraPOS, mesmo risco multicanal já mapeado em todo o portfólio | Impede vender o mesmo item por dois canais ao mesmo tempo |
| RNFT-E02 (idempotência de pagamento) | Processa pagamento online | Evita cobrança duplicada em reenvio de webhook |
| RNFT-E03 (fila para picos) | Relevante em campanha promocional do lojista | Evita que checkout trave inteiro por lentidão em etapa não crítica |
| RNFT06 (LGPD) | Dado de cliente comprador, endereço de entrega | Cumpre obrigação legal |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica na Loja Virtual |
|---|---|
| Consistência de estoque | Mesmo cuidado já aplicado no AuraPOS/AuraFix/Delivery — reforçado aqui porque é o quarto canal disputando o mesmo estoque |
| Dados | Dado de pagamento nunca armazenado diretamente — sempre via gateway, mesmo padrão do restante do portfólio |
| Auditoria externa | Prioridade equivalente ao AuraPOS, dado que processa pagamento e depende do mesmo estoque crítico |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** SaaS puro (módulo web), sem componente físico. Ativado como módulo adicional dentro do pacote comercial do AuraPOS via `aura-licensing`, nunca vendido isoladamente (reforça RF05).

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Por ser módulo dependente, o deploy deveria estar versionado em conjunto com o do AuraPOS, evitando incompatibilidade de versão entre os dois.

---

## 9. Modelo de receita

| Fonte | Modelo |
|---|---|
| Comissão por pedido online | Percentual sobre cada venda feita pela Loja Virtual |
| Taxa de entrega | Repassada ou compartilhada entre lojista e entregador, quando integrado ao Aura Delivery |
| Módulo dentro do plano "Integrado" do AuraPOS | Não é vendido isoladamente — é upsell natural de quem já usa o AuraPOS, ativado via `aura-licensing` |

Diferente de quase todo o resto do portfólio, este documento **não lista forma de venda B2B fora do ecossistema** — a decisão de dependência do AuraPOS (seção 1) torna isso estruturalmente incoerente com o modelo de negócio já definido.

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** O documento de visão anterior tinha incerteza elevada; esta versão reduz essa incerteza formalizando RF/RNF, mas ainda depende de decisões de negócio (seção 11) antes de entrar em desenvolvimento.

---

## 11. Pendências e decisões em aberto

1. **Checkout como convidado vs. conta obrigatória** — mesma decisão do Aura Delivery, recomendo decidir uma vez para os dois.
2. **Comportamento de rastreamento para lojista sem Aura Delivery** (RF04) — o "status simples" precisa ser especificado com mais detalhe.
3. **Versionamento conjunto com o AuraPOS** (seção 8) — decisão de processo de deploy ainda não formalizada.
4. **Reaproveitamento futuro pelo AuraVet** (seção 2.4) — mencionado como candidato, não decidido.
5. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado como serviço compartilhado.
