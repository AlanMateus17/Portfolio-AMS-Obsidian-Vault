---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-historico — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]].

---

## 1. Visão do produto

Serviço de registro imutável de eventos, construído em Clojure + Datomic — única peça do portfólio fora do stack fixo .NET, decisão consciente por causa da vantagem estrutural real do Datomic em histórico consultável no tempo. Consumido por qualquer sistema que precise de auditoria robusta ou simulação especulativa (o "e se" do AM Rendara).

**Diferencial de inovação:** a maioria dos sistemas guarda histórico como log de mudança (before/after num campo). Aqui, cada fato é imutável e consultável em qualquer ponto do tempo (`as-of`), e permite transação especulativa (`d/with`) sem afetar o dado real — isso é o que viabiliza o simulador "e se" de rebalanceamento do AM Rendara sem duplicar a carteira do cliente num ambiente de teste separado.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Ingestão de evento
- Consumidor de evento genérico via Redis Streams, recebendo evento de qualquer sistema do portfólio
- Gravação imutável de fato, com schema genérico o suficiente para registrar produto, pedido, carteira, fluxo de caixa, ou qualquer outro tipo de fato futuro

### 2.2 Consulta temporal
- API de consulta `as-of` (estado em um ponto específico do tempo) e `history` (linha do tempo completa de um fato)

### 2.3 Simulação especulativa
- Transação especulativa via `d/with`, usada hoje exclusivamente pelo simulador "e se" do AM Rendara — permite simular sem persistir

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Consumir evento de qualquer sistema do portfólio via Redis Streams | Desacopla o sistema de origem do registro histórico — origem não espera confirmação síncrona |
| RF02 | Gravar fato de forma imutável, nunca sobrescrever ou deletar | É a garantia central do serviço — sem isso, "histórico" vira só mais um log mutável comum |
| RF03 | Responder consulta `as-of` para qualquer ponto do tempo | Permite reconstruir "como estava" em qualquer momento passado, sem snapshot manual |
| RF04 | Responder consulta `history` com linha do tempo completa de um fato | Sustenta auditoria e investigação de disputa |
| RF05 | Suportar transação especulativa (`d/with`) sem persistir | Viabiliza simulação sem duplicar dado real em ambiente de teste |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Sistema consumidor (AM Rendara, e futuramente outros)
- **Uso:** publica evento, consulta histórico/simulação via API
- Não tem usuário humano direto — é consumido máquina a máquina

### 4.2 Você (auditoria/investigação)
- **Uso:** consulta pontual em caso de disputa ou investigação de bug, via ferramenta técnica direta (não um painel polido, dado o estágio inicial)
- **Lacuna:** não existe interface amigável para essa consulta hoje — só acesso técnico direto ao Datomic

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-historico | Para que serve |
|---|---|---|
| RNFT02 (isolamento de falha, série original) | Indisponibilidade do `aura-historico` não pode bloquear operação crítica do sistema de origem | Histórico é valor agregado, não deve ser dependência bloqueante de venda/operação |
| RNFT06 (LGPD) | Imutabilidade entra em tensão direta com direito de exclusão do titular — precisa de estratégia de anonimização/tombstone, não exclusão física | Sem isso, o próprio diferencial do serviço (imutabilidade) vira risco de não conformidade |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-historico |
|---|---|
| Dados | Se registra fato financeiro (fluxo de caixa do AM Rendara), herda a mesma sensibilidade do sistema de origem |
| Auditoria externa | Prioridade baixa por ora — uso interno, sem exposição direta a cliente final; sobe de prioridade só se virar produto vendável (seção 9) |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno, sem instalador nem distribuição direta.

---

## 8. Deploy e CI/CD

Diferente do restante do stack, este serviço roda em Clojure/Datomic, não em .NET — exige pipeline próprio (não reaproveita diretamente o Dockerfile .NET padrão), ainda a ser definido.

---

## 9. Modelo de receita — incluindo forma de venda nova

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — sustenta auditoria e simulação do AM Rendara |
| **"Trilha de auditoria como serviço" para terceiros** | Empresas de outros setores (fintech, healthtech) que precisam de histórico imutável robusto e não querem montar infraestrutura Clojure/Datomic própria — cobrança por volume de evento registrado |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Descrito em arquitetura híbrida (outbox pattern, idempotência de integração com o núcleo .NET), mas este é o primeiro documento com RF/RNF formal.

---

## 11. Pendências e decisões em aberto

1. **Estratégia de anonimização/tombstone para conformidade com LGPD** — tensão direta com o princípio de imutabilidade, precisa de solução antes de registrar qualquer dado pessoal real.
2. **Pipeline de deploy próprio** (Clojure/Datomic, fora do padrão .NET) — ainda não definido.
3. **Avaliar se "trilha de auditoria como serviço" vale a pena como produto B2B** — mercado nichado, mas com pouco concorrente direto no Brasil.
4. **Interface de consulta para você** (seção 4.2) — hoje só acesso técnico direto, sem painel.
