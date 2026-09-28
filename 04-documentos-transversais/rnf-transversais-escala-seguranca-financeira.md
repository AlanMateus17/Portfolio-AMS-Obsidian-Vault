---
tags: [transversal, portfolio-ams]
tipo: regra-transversal
status: completo
---

# RNF Transversais — Escala e Segurança Financeira
### Documento de referência única, aplicável a todos os sistemas do portfólio que vendem produto ou processam pagamento

Este documento não pertence a um sistema específico. Ele existe para ser **referenciado** pelo documento de RF/RNF de cada sistema (AM Kaixara, AM Consertta, AuraVet, Delivery, Loja Virtual, `aura-licensing`), em vez de repetir o mesmo requisito em cada um. Quando um requisito próprio de um sistema depender de um destes, ele deve citar o ID aqui definido em vez de redescrever.

---

## RNFT-E01 — Controle de concorrência em operações de estoque

**Requisito:** toda operação que decrementa quantidade em estoque deve usar controle de concorrência (otimista via token de versão, ou pessimista via lock de curta duração) que impeça duas operações simultâneas de venderem a mesma unidade.

**Critério de verificação:** disparar duas requisições de venda simultâneas para o último item em estoque deve resultar em uma venda confirmada e uma rejeitada com erro claro ("estoque insuficiente"), nunca em duas vendas confirmadas.

**Aplica-se a:** AM Kaixara, AM Consertta, AuraVet (módulo de loja), Loja Virtual, AM Rotara — qualquer sistema com estoque compartilhado entre mais de um canal de venda.

**Mecanismo recomendado:** coluna de versão (`xmin` do próprio PostgreSQL, ou coluna `RowVersion` explícita) na tabela de estoque, com a atualização feita como `UPDATE ... WHERE id = @id AND versao = @versao_lida` — se zero linhas forem afetadas, a aplicação trata como conflito de concorrência e recarrega o estado antes de tentar de novo.

---

## RNFT-E02 — Idempotência em eventos de pagamento

**Requisito:** todo processamento de evento de pagamento (webhook de gateway, confirmação de Pix, callback de cartão) deve ser idempotente — processar o mesmo evento mais de uma vez deve produzir exatamente o mesmo efeito de processar uma vez só.

**Critério de verificação:** reenviar manualmente o mesmo payload de webhook duas vezes não deve gerar cobrança duplicada, baixa de estoque duplicada, nem duplicar o registro da venda.

**Aplica-se a:** qualquer sistema que processa pagamento — AM Kaixara, AM Consertta, AuraVet (assinatura/plano), Loja Virtual, `aura-licensing` (cobrança recorrente).

**Mecanismo recomendado:** chave de idempotência única por evento (geralmente já fornecida pelo próprio gateway como ID da transação), registrada antes do processamento; qualquer evento com chave já registrada é descartado sem reprocessar.

---

## RNFT-E03 — Processamento assíncrono para picos de venda

**Requisito:** a confirmação da venda ao cliente não deve depender do sucesso síncrono de etapas não críticas para a confirmação (emissão fiscal, notificação, atualização de relatório) — essas etapas devem ser enfileiradas e processadas com re-tentativa automática em caso de falha.

**Critério de verificação:** uma falha temporária no serviço de emissão fiscal não deve impedir a confirmação da venda ao cliente; a emissão deve completar depois, via re-tentativa, sem intervenção manual.

**Aplica-se a:** todos os sistemas de venda, com prioridade nos que esperam maior volume simultâneo (AM Kaixara, AM Consertta, Loja Virtual).

**Mecanismo recomendado:** fila baseada em Redis Streams (já cogitado para o `aura-historico`, reaproveitável aqui) ou equivalente, separando "confirmar venda" (síncrono, rápido) de "processar consequências da venda" (assíncrono).

---

## RNFT-E04 — Estratégia de escala de banco de dados

**Requisito:** toda tabela particionável por tenant deve ter índice contendo `tenant_id` como parte da chave de busca mais comum; a decisão de réplica de leitura e connection pooling deve estar registrada mesmo que não implementada ainda.

**Critério de verificação:** consultas mais frequentes de cada sistema (listagem de produto, histórico de venda) devem usar índice que inclui `tenant_id`, verificável via `EXPLAIN ANALYZE`.

**Aplica-se a:** todos os sistemas com PostgreSQL multi-tenant.

**Mecanismo recomendado:** índice composto iniciando por `tenant_id` nas tabelas de maior volume; PgBouncer para connection pooling quando o número de conexões simultâneas justificar; réplica de leitura como item de roadmap, não bloqueante para o estágio atual.

---

## RNFT-E05 — Observabilidade e alerta

**Requisito:** todo sistema em produção deve emitir log estruturado das operações financeiras (venda, cobrança, estorno) e disparar alerta automático em caso de divergência detectável (ex: tentativa de decremento de estoque abaixo de zero, falha de idempotência detectada, erro recorrente no mesmo endpoint).

**Critério de verificação:** uma falha na categoria acima deve gerar notificação (e-mail, WhatsApp ou painel) em até alguns minutos, sem depender de reclamação de cliente para ser descoberta.

**Aplica-se a:** todos os sistemas em produção, com prioridade para os que processam pagamento diretamente.

**Mecanismo recomendado:** logging estruturado desde o início (não precisa de ferramenta cara — mesmo um log em arquivo/tabela com alerta simples via webhook do WhatsApp já cumpre o requisito no estágio atual).

---

## RNFT-E06 — Reconciliação financeira periódica

**Requisito:** deve existir uma rotina periódica (mínimo semanal) que compara o total recebido segundo o gateway de pagamento com o total registrado como recebido internamente, sinalizando qualquer divergência.

**Critério de verificação:** divergência entre os dois totais deve ser detectada e reportada automaticamente, não apenas descoberta manualmente em auditoria eventual.

**Aplica-se a:** `aura-licensing` (responsável central pela cobrança recorrente de todo o portfólio) como dono principal deste requisito; cada sistema que processa pagamento direto (AM Kaixara, AM Consertta, Loja Virtual) também precisa expor os dados necessários para essa reconciliação.

**Mecanismo recomendado:** job agendado (pode rodar via GitHub Actions em cron, sem necessidade de infraestrutura nova) comparando extratos.

---

## Tabela de aplicabilidade por sistema

| Sistema | E01 (estoque) | E02 (idempotência) | E03 (fila) | E04 (banco) | E05 (observabilidade) | E06 (reconciliação) |
|---|---|---|---|---|---|---|
| AM Kaixara | Sim — prioridade alta, já em código | Sim, quando integrar gateway online | Sim | Sim | Sim | Reporta dados, não é dono |
| AM Consertta | Sim — prioridade alta | Sim | Sim | Sim | Sim | Reporta dados, não é dono |
| AuraVet | Sim (módulo de loja) | Sim (assinatura/plano) | Sim | Sim | Sim | Reporta dados, não é dono |
| AM Rotara | Sim | Sim | Sim | Sim | Sim | Reporta dados, não é dono |
| Loja Virtual | Sim | Sim | Sim | Sim | Sim | Reporta dados, não é dono |
| Momentos/Cupido | Não se aplica (sem estoque físico) | Sim (assinatura) | Opcional | Sim | Sim | Reporta dados, não é dono |
| `aura-licensing` | Não se aplica | Sim — crítico, é o motor central | Opcional | Sim | Sim | **Dono do requisito** |
