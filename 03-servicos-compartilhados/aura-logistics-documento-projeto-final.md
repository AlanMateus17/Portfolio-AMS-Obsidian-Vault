---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-logistics — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Último dos 4 serviços compartilhados pendentes — já havia sido sinalizado dentro do próprio AuraFix, agora formalizado como sistema próprio.

---

## 1. Visão do produto

Serviço central de frete, etiqueta e rastreio, consumido por qualquer sistema do portfólio que precise enviar algo fisicamente: aparelho em conserto e devolução (AuraFix), produto de loja (Loja Virtual, AuraVet), cartão NFC físico (Momentos/Cupido). Elimina a necessidade de cada sistema implementar sua própria integração com Correios/transportadora.

**Diferencial de inovação:** nenhum outro sistema do portfólio precisa disso sozinho o suficiente para justificar construir uma integração de frete robusta — mas a soma de todos eles justifica plenamente. É o exemplo mais claro de "nenhum dos 4 sistemas de origem pediria isso individualmente, mas o portfólio inteiro precisa".

---

## 2. Funcionalidades completas (estado final)

### 2.1 Cálculo de frete
- Cálculo por CEP de origem/destino, com múltiplas transportadoras cotadas ao mesmo tempo quando aplicável

### 2.2 Geração de etiqueta e rastreio
- Etiqueta de postagem gerada automaticamente, código de rastreio vinculado ao sistema e ao pedido/OS de origem

### 2.3 Webhook de status de envio
- Recebe atualização de status da transportadora (postado, em trânsito, entregue), repassa ao sistema de origem via evento — que então aciona o `aura-notifications` para avisar o cliente

### 2.4 Conferência de recebimento remoto
- Reaproveita o conceito já formalizado no AuraFix (checklist + foto) — generaliza para qualquer sistema que precise confirmar recebimento de item enviado

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Calcular frete por CEP, cotando mais de uma transportadora quando disponível | Evita que cada sistema implemente sua própria integração de cálculo de frete |
| RF02 | Gerar etiqueta de postagem e código de rastreio, vinculado ao sistema/pedido de origem | Centraliza a geração, mantendo rastreabilidade de qual sistema originou o envio |
| RF03 | Receber webhook de atualização de status da transportadora e repassar ao sistema de origem | Desacopla o sistema consumidor de lidar diretamente com a API de cada transportadora |
| RF04 | Disparar evento para o `aura-notifications` a cada mudança relevante de status | Reaproveita o motor de notificação central em vez de duplicar lógica de aviso |
| RF05 | Suportar checklist de conferência de recebimento remoto (fotos + validação) | Generaliza o padrão já usado no AuraFix para qualquer sistema que precise |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Sistema consumidor (AuraFix, Loja Virtual, AuraVet, Momentos/Cupido)
- **Uso:** solicita cálculo de frete, gera etiqueta, consulta status — máquina a máquina
- Não tem usuário humano direto neste papel

### 4.2 Cliente final (remetente ou destinatário do envio)
- **Uso:** recebe etiqueta/instrução de postagem (quando aplicável, ex: cliente envia aparelho pro AuraFix), acompanha rastreio via notificação
- **Suporte:** canal do sistema de origem, não deste serviço

### 4.3 Você (monitoramento de entrega/disputa)
- **Uso:** acompanhar envio extraviado ou atrasado, acionar transportadora em caso de disputa
- **Lacuna:** sem painel formal ainda — mas o `aura-support` (documento anterior) é o candidato natural a incorporar essa visão, em vez de este serviço construir o próprio painel

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-logistics | Para que serve |
|---|---|---|
| RNFT02 (isolamento de falha, série original) | Indisponibilidade não pode bloquear a venda/abertura de OS no sistema consumidor — cálculo de frete pode falhar graciosamente com valor estimado, sem travar o checkout | Frete é etapa auxiliar, nunca deveria ser dependência bloqueante de uma venda |
| RNFT-E03 (fila) | Processamento de webhook de status de transportadora deve ser assíncrono | Evita que instabilidade momentânea da transportadora afete o sistema consumidor |
| Confiabilidade de rastreio (já formalizado no AuraFix, herdado aqui como origem) | Rastreio precisa ser confiável o bastante para substituir a confiança do contato presencial | Cliente remoto não tem contato visual — esse requisito nasceu no AuraFix e se generaliza pra todo consumidor deste serviço |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-logistics |
|---|---|
| Dados | Endereço de entrega é dado pessoal — minimizar exposição além do necessário para as partes envolvidas na transação específica |
| Rede/API | Credencial de integração com transportadora protegida, nunca exposta a nenhum sistema consumidor diretamente — só o `aura-logistics` fala com a API externa |
| Auditoria externa | Prioridade baixa-média — não processa pagamento nem dado altamente sensível, mas concentra endereço de cliente de múltiplos sistemas |

---

## 7. Hardware, instalador e distribuição

**Não aplicável no sentido de instalador.** É o único serviço compartilhado com dependência física indireta real — o produto sendo enviado é físico, mesmo que o serviço em si seja puramente API.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Como depende de integração externa (Correios/transportadora), mesmo cuidado já registrado no documento do AuraFix: teste de contrato dessa integração no pipeline, não só teste unitário interno.

---

## 9. Modelo de receita — incluindo forma de venda nova

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — reduz custo de integração duplicada entre os sistemas consumidores |
| **API de frete/rastreio para terceiros** | Pequeno e-commerce ou negócio local fora do ecossistema Aura que só quer o cálculo de frete e geração de etiqueta, sem comprar sistema completo — cobrança por envio processado, mesmo ângulo já aplicado ao `aura-analytics` |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Já havia sido mencionado como candidato dentro do documento do AuraFix; esta é a primeira formalização como sistema próprio, com RF/RNF completos.

---

## 11. Pendências e decisões em aberto

1. **Provedor de transportadora** (Correios, transportadora privada, ou ambos) — mesma pendência já registrada no AuraFix, agora centralizada aqui.
2. **Painel de monitoramento de disputa/extravio** (seção 4.3) — decisão de incorporar ao `aura-support` em vez de construir painel próprio, a confirmar.
3. **Avaliar API de frete como produto B2B** (seção 9) — mercado potencialmente amplo (qualquer pequeno e-commerce brasileiro), vale dimensionar antes de priorizar.
