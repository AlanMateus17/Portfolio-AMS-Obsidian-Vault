---
tags: [transversal, portfolio-ams]
tipo: regra-transversal
status: completo
---

# RNFT-IA01 a IA04 — Governança de Geração por IA
### Série transversal nova, originada no AuraArquiteto, reaproveitável por qualquer sistema futuro do portfólio que gere conteúdo por IA voltado ao cliente final

---

## Por que existe

Diferente de RNFT-E (escala), RNFT-S (segurança/distribuição) e RNFT-D (design), esta série resolve um risco específico: **conteúdo gerado por IA, entregue direto ao cliente final, sem revisão humana em tempo real**. Isso já existe no AuraArquiteto (relatório de arquitetura) e potencialmente reaparece em qualquer sistema futuro que use `aura-copilot` pra saída voltada ao cliente, não só uso interno.

---

## RNFT-IA01 — Validação estrutural obrigatória (golden file)

Toda saída gerada por IA passa por teste automatizado (`xUnit`, padrão "golden file") comparando a estrutura contra um schema esperado, antes de chegar ao cliente. Não é validação de conteúdo (isso é IA02), é validação de **forma** — a saída tem todos os campos esperados, no formato esperado.

## RNFT-IA02 — QA automático de coerência antes da entrega

Validação de coerência de conteúdo (orçamento dentro do informado, produto disponível de verdade, recomendação coerente com a região do cliente) — automática, roda antes de qualquer entrega, não depois.

## RNFT-IA03 — Amostragem manual periódica

Mesmo com IA01/IA02 automatizados, uma fração da saída gerada passa por revisão humana periódica (amostragem, não 100%) — detecta erro sistemático que a validação automática não capturaria sozinha.

## RNFT-IA04 — Acompanhamento pós-entrega estruturado

Follow-up automatizado em pontos fixos (7/30/90 dias) verificando se o cliente realmente executou/usou o que foi gerado — fecha o ciclo de qualidade além do momento da entrega.

---

## Onde já se aplica

- **AuraArquiteto** — origem da série, relatório de arquitetura gerado por IA
- Qualquer sistema futuro que usar `aura-copilot` pra saída direta ao cliente final, sem revisão humana no caminho crítico

## Onde não se aplica

Uso interno de IA (ex: sugestão de código, resumo administrativo) não precisa desta série — ela é específica pra saída que o cliente final recebe como produto, não ferramenta de produtividade interna.

---

## 🔗 Documentos relacionados
- [[auraarquiteto-documento-projeto-final]] — o sistema que originou esta série
- [[aura-copilot-documento-projeto-final]] — o serviço compartilhado que esta série governa
- [[rnf-transversais-escala-seguranca-financeira]], [[rnf-transversais-design-tema]], [[distribuicao-licenciamento-seguranca]] — as demais séries transversais do portfólio
