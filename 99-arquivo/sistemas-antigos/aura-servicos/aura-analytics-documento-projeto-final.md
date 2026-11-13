---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-analytics — Documento de Projeto Final

Segue a estrutura fixa do [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md).

---

## 1. Visão do produto

Serviço de análise estatística e otimização, construído em Python + FastAPI — segunda peça do portfólio fora do stack .NET puro, por vantagem estrutural real do ecossistema Python em dado/ML. Consumido por AM Kaixara (previsão de demanda), AM Rotara (otimização de rota) e AM Rendara (projeção patrimonial).

**Diferencial de inovação:** um único serviço resolvendo três problemas de naturezas diferentes (previsão de série temporal, otimização combinatória, projeção estatística) para três sistemas diferentes, evitando que cada sistema monte sua própria stack de dado — a mesma lógica de reaproveitamento que rege todo o portfólio, aplicada a inteligência analítica.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Previsão de demanda (AM Kaixara)
- Endpoint de previsão via Prophet/statsmodels, consumido pelo dashboard do AM Kaixara

### 2.2 Otimização de rota (AM Rotara)
- Endpoint de roteirização via Google OR-Tools, resolvendo como problema de roteirização de veículos (VRP) — é o motor técnico por trás do diferencial competitivo do Delivery

### 2.3 Projeção patrimonial (AM Rendara)
- Endpoint de projeção de crescimento de longo prazo, simulação estatística de aportes recorrentes

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Expor endpoint de previsão de demanda por produto/período, consumindo histórico de venda do AM Kaixara | Permite sugestão de reposição de estoque antes da ruptura |
| RF02 | Expor endpoint de roteirização otimizada de múltiplas entregas (VRP) | É o motor técnico do diferencial competitivo do AM Rotara — sem isso, a promessa de "roteirização real" não existe |
| RF03 | Expor endpoint de projeção de crescimento patrimonial com simulação de aporte recorrente | Ajuda o usuário do AM Rendara a visualizar efeito composto de longo prazo |
| RF04 | Cada endpoint deve funcionar de forma independente dos outros dois | Um sistema consumidor não deve ser afetado por instabilidade de um endpoint que ele não usa |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Sistema consumidor (AM Kaixara, Delivery, AM Rendara)
- **Uso:** consulta endpoint via API, sem usuário humano direto — máquina a máquina, resultado exibido dentro da interface do sistema de origem

### 4.2 Você (ajuste de modelo/parâmetro)
- **Uso:** acompanhar qualidade da previsão/otimização ao longo do tempo, retreinar modelo quando necessário
- **Lacuna:** não existe painel de monitoramento de qualidade de modelo hoje — decisão de ajustar é manual e não instrumentada

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-analytics | Para que serve |
|---|---|---|
| RNFT02 (isolamento de falha, série original) | Indisponibilidade não pode bloquear operação crítica do sistema de origem — AM Kaixara deve vender mesmo sem previsão de demanda disponível | Analytics é valor agregado, nunca dependência bloqueante |
| RNFT-E04 (escala de banco/consulta) | Consulta de histórico para treinar/gerar previsão deve ser eficiente mesmo com grande volume acumulado | Evita que o próprio serviço de analytics vire gargalo de performance |
| Qualidade de modelo (próprio) | Previsão/otimização deve ter métrica de acurácia monitorada ao longo do tempo, não só implementada uma vez | Modelo que nunca é reavaliado degrada silenciosamente com o tempo |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-analytics |
|---|---|
| Dados | Consome dado de venda/financeiro de múltiplos tenants para treinar modelo — precisa garantir que previsão de um tenant nunca vaza informação de outro (ex: modelo treinado por tenant, não modelo único misturando dado de todos) |
| Auditoria externa | Prioridade baixa por ora — uso interno, sobe de prioridade se virar produto vendável (seção 9) |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno, sem instalador nem distribuição direta.

---

## 8. Deploy e CI/CD

Roda em Python/FastAPI, fora do padrão .NET — pipeline próprio a definir, semelhante à mesma pendência do `aura-historico`.

---

## 9. Modelo de receita — incluindo forma de venda nova

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — sustenta diferencial competitivo do AM Kaixara, Delivery e AM Rendara |
| **API de previsão/otimização para terceiros** | Pequeno varejo ou operação de entrega fora do ecossistema Aura que só quer o endpoint de previsão de demanda ou roteirização, sem comprar o sistema inteiro — cobrança por chamada ou por volume |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Descrito em arquitetura (três endpoints mapeados aos três sistemas consumidores), mas este é o primeiro documento com RF/RNF formal.

---

## 11. Pendências e decisões em aberto

1. **Modelo treinado por tenant vs. modelo único** — decisão técnica que impacta diretamente isolamento de dado (seção 6).
2. **Painel de monitoramento de qualidade de modelo** (seção 4.2) — ainda não especificado.
3. **Pipeline de deploy próprio** (Python, fora do padrão .NET) — mesma pendência do `aura-historico`.
4. **Avaliar API de previsão/otimização como produto B2B** — mercado potencialmente maior que o `aura-historico`, dado que previsão de demanda é dor comum a qualquer varejo.
