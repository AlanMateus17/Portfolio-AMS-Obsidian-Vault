---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-goals — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]].

---

## 1. Visão do produto

Serviço compartilhado de metas financeiras, consumido hoje pelo AuraWealth (meta individual/PJ) e pelo Momentos/Cupido (meta compartilhada de casal). Resolve o mesmo problema — acompanhamento de objetivo financeiro com aporte recorrente — em dois contextos de uso diferentes, sem duplicar lógica.

**Diferencial de inovação:** meta financeira compartilhada de casal, visível tanto no contexto afetivo (Momentos/Cupido) quanto no contexto financeiro (AuraWealth), com cada parceiro mantendo sua segregação individual intacta — nenhum concorrente de nenhum dos dois mercados (apps de casal, apps financeiros) resolve essa ponte hoje.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Meta individual
- Criação de meta com valor-alvo, prazo e sugestão de aporte mensal
- Acompanhamento de progresso

### 2.2 Meta compartilhada (casal)
- Meta com dois contribuintes, cada um com opção de privacidade sobre o valor individual aportado (só o total e o progresso são necessariamente visíveis a ambos)
- Vínculo exige confirmação mútua antes da meta existir como "compartilhada" — nenhum parceiro pode criar meta compartilhada unilateralmente

### 2.3 Integração com fonte de dado real
- Meta pode ser alimentada automaticamente pelo fluxo de caixa do AuraWealth (quando o usuário também usa esse sistema) ou lançada manualmente

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Criar meta individual com valor-alvo, prazo e sugestão de aporte | Formaliza objetivo financeiro com plano de ação, não só intenção |
| RF02 | Criar meta compartilhada, exigindo confirmação mútua dos dois parceiros | Impede que um parceiro crie vínculo financeiro compartilhado sem consentimento do outro |
| RF03 | Permitir privacidade do valor individual aportado dentro de uma meta compartilhada | Preserva autonomia financeira de cada parceiro mesmo dentro do objetivo comum |
| RF04 | Consumir dado de fluxo de caixa do AuraWealth quando disponível, com fallback manual | Automatiza o acompanhamento sem travar o usuário que não usa o AuraWealth |
| RF05 | Expor API consumível tanto pelo AuraWealth quanto pelo Momentos/Cupido | É a razão de existir como serviço compartilhado, não módulo duplicado em cada sistema |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Usuário do AuraWealth (meta individual ou PJ)
- **Cadastro:** herdado da conta AuraWealth
- **Uso:** cria e acompanha meta dentro do próprio dashboard do AuraWealth
- **Suporte:** canal do AuraWealth

### 4.2 Casal do Momentos/Cupido (meta compartilhada)
- **Cadastro:** herdado da conta Momentos/Cupido, com vínculo mútuo confirmado
- **Uso:** acompanha meta compartilhada dentro do contexto do Cupido
- **Suporte:** canal do Momentos/Cupido

### 4.3 Suporte técnico interno
- Mesma lacuna recorrente do portfólio — aqui a complexidade extra é que um problema de meta compartilhada pode envolver dois sistemas diferentes ao mesmo tempo (AuraWealth + Momentos/Cupido), exigindo visibilidade cruzada que nenhum painel de suporte individual de sistema teria sozinho

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-goals | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Meta compartilhada é dado financeiro de duas pessoas ao mesmo tempo | Cumpre obrigação legal para os dois titulares, não só um |
| RNFT07 (BOLA) | Acesso a meta compartilhada deve validar que o usuário é um dos dois parceiros vinculados | Impede terceiro (nem que seja outro usuário do Momentos/Cupido) ver meta de casal alheio |
| RNFT-S03/S04 (conexão entre sistemas) | Consumo pelo AuraWealth e Momentos/Cupido segue consentimento explícito e escopo mínimo | Nenhum dos dois sistemas deve herdar acesso amplo ao outro só por consumir o `aura-goals` |
| Consistência de privacidade | Valor individual marcado como privado nunca deve aparecer em nenhuma view, log ou relatório consumido pelo parceiro | É a garantia técnica que sustenta a promessa de privacidade opcional (RF03) |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-goals |
|---|---|
| Dados | Dado financeiro compartilhado entre duas pessoas exige cuidado redobrado de segregação — erro aqui expõe dado de duas pessoas ao mesmo tempo, não uma |
| Conexão entre sistemas | Já coberto pelo padrão RNFT-S03/S04 do portfólio, aplicado aqui a dois consumidores simultâneos |
| Auditoria externa | Prioridade média — não é SPOF nem processa pagamento diretamente, mas manipula dado financeiro sensível |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno, consumido via API pelos dois sistemas que o utilizam, sem instalador nem distribuição própria.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Sem necessidade de redundância especial (diferente do `aura-licensing`), já que uma indisponibilidade aqui degrada uma funcionalidade específica, não o portfólio inteiro.

---

## 9. Modelo de receita

Não gera receita direta — é um serviço de suporte a funcionalidade que agrega valor percebido tanto ao AuraWealth quanto ao Momentos/Cupido, mas nunca é cobrado separadamente. Diferente do `aura-licensing`, não há um ângulo claro de venda como produto B2B independente — meta compartilhada de casal é um problema de nicho específico demais para licenciar a terceiros fora do próprio ecossistema.

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Existe só como conceito de integração dentro dos PRDs do AuraWealth e do Momentos/Cupido — este é o primeiro documento a formalizar RF/RNF próprios.

---

## 11. Pendências e decisões em aberto

1. **Regra de visibilidade da meta compartilhada na interface** — já sinalizada como pendência no documento do AuraWealth, precisa ser validada com o usuário antes de formalizar comportamento padrão.
2. **O que acontece quando um casal do Momentos/Cupido termina o relacionamento** — a meta compartilhada precisa de um fluxo de encerramento/divisão, ainda não desenhado.
3. **Painel de suporte técnico interno com visibilidade cruzada** (seção 4.3) — ainda sem RF formal.
