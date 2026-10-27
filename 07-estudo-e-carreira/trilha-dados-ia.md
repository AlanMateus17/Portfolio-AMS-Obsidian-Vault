---
tags: [estudo, ia, dados, python, portfolio-ams]
tipo: trilha
status: novo
atualizado: 2026-10-26
---

# 🤖 Trilha de Dados e Inteligência Artificial — Do Python ao Treino dos Próprios Modelos

> **Objetivo:** desenvolver IA de verdade, não só consumir API: dados, ML clássico, deep learning, LLMs e fine-tuning de modelos 8B treinados com o seu próprio material, dentro do ecossistema Aura.
>
> **Por que ela se encaixa tão bem no seu plano:** IA, econometria e finanças quantitativas usam **a mesma base** — Python, estatística, álgebra linear e cálculo. A Licenciatura, a faculdade de Economia e esta trilha se reforçam; você não está abrindo três frentes, está abrindo uma com três aplicações.
>
> **Gatilho:** Trilha Paralela, começa **depois do Passo 8** (mesmo gatilho da 42 e do Pentest). Antes disso, nada aqui — o Passo 8 é o que garante que você sabe engenharia de software antes de pôr modelo em produção.

---

## 🗺️ Módulos

| Módulo | Tema | Pré-requisito | Aplicação no Aura |
|---|---|---|---|
| **IA0** | Python para quem já sabe C# | Passo 8 | Scripts, aura-analytics |
| **IA1** | Matemática para IA | Lins Partes III, IV, VII + Cálculo | — |
| **IA2** | Dados e engenharia de dados | IA0 + SQL dos Passos 2/5 | Pipelines do aura-analytics |
| **IA3** | Machine learning clássico | IA1 + IA2 | Previsão de fluxo de caixa (Rendara) |
| **IA4** | Deep learning | IA3 | Classificação de notas fiscais (Caixa da Casa) |
| **IA5** | LLMs aplicados | IA0 (pode correr junto de IA3) | aura-copilot · tutor do AM Mentor |
| **IA6** | Treino e fine-tuning | IA4 + IA5 | Modelo próprio 8B com suas apostilas |
| **IA7** | MLOps | IA6 + Passo 10 | Modelos em produção, monitorados |

---

## IA0 — Python *(2–4 semanas)*
- [ ] Sintaxe, tipos, coleções, compreensões, módulos, ambiente virtual, `pytest`
- [ ] FastAPI (é o único Python da stack: `aura-analytics`)
- **Desenvolver:** endpoint FastAPI que recebe uma série e devolve média/desvio — o esqueleto do aura-analytics.
- **✅ Pronto quando:** reescreve em Python um exercício do Passo 1 e testa com pytest.

> O Passo 13 (Python + OR-Tools no AM Rotara) fica mais rápido: o Python já estará pronto.

## IA1 — Matemática para IA *(contínua, puxada pelos livros)*
- [ ] Estatística descritiva e probabilidade (Lins Partes III e VII)
- [ ] Álgebra linear: vetores, matrizes, produto, transformações (Lins Cap. 13 + material de Álgebra Linear)
- [ ] Cálculo: derivada, gradiente, regra da cadeia (base do backpropagation) — suas notas de Cálculo no `ensino-ti`
- [ ] Estatística inferencial e regressão (cruza com a econometria da faculdade de Economia)

## IA2 — Dados e engenharia de dados
- [ ] NumPy, Pandas, visualização (Matplotlib)
- [ ] Limpeza, junção, agregação; formatos (CSV, Parquet)
- [ ] Pipelines ETL, agendamento, qualidade de dado
- **Desenvolver:** pipeline que puxa dados do BCB/IBGE (módulo F6 da [Trilha de Finanças](trilha-financas-economia.md)) e grava no PostgreSQL.
- **Leituras:** *Python for Data Analysis* (Wes McKinney) · *Fundamentals of Data Engineering* (Joe Reis e Matt Housley)

## IA3 — Machine learning clássico
- [ ] Regressão linear/logística, árvores, random forest, gradient boosting
- [ ] Validação cruzada, overfitting, métricas
- [ ] Séries temporais (Prophet, statsmodels — já previstos no aura-analytics)
- **Desenvolver:** previsão de fluxo de caixa no Rendara, comparada contra uma média simples (se não ganhar da média, não vai para produção).
- **Leitura:** *Hands-On Machine Learning* (Aurélien Géron)

## IA4 — Deep learning do zero
- [ ] Implementar **sem biblioteca**: neurônio, rede de várias camadas, **autograd** (derivada automática) e backpropagation, só com Python e NumPy
- [ ] Depois, o mesmo em PyTorch
- [ ] CNN, RNN e **transformers** (a arquitetura dos LLMs)
- **Desenvolver:** classificador de itens de NFC-e em categorias de gasto para o Caixa da Casa.
- **Recursos:** *Neural Networks: Zero to Hero* (Andrej Karpathy, gratuito no YouTube) · curso Practical Deep Learning (fast.ai, gratuito)

## IA5 — LLMs aplicados
- [ ] APIs de modelos, function calling (é o coração do `aura-copilot`)
- [ ] RAG: embeddings, banco vetorial (pgvector no seu PostgreSQL), recuperação
- [ ] Avaliação de respostas, custo, latência
- [ ] Governança: as regras RNFT-IA01–04 que você já escreveu · segurança (prompt injection — [roadmap de segurança](roadmap-seguranca-ofensiva-completo.md) §6.1)
- **Desenvolver:** tutor do AM Mentor que responde com base nos seus próprios capítulos do *Lógica e Máquina* (RAG), citando a seção de onde tirou a resposta.

## IA6 — Treinar do zero e fine-tuning
- [ ] **Tokenizer próprio** (BPE) e **transformer escrito do zero**
- [ ] **Pré-treinar um modelo pequeno do zero** (dezenas de milhões de parâmetros) com seus textos, numa GPU alugada
- [ ] Como os grandes modelos são treinados (pré-treino em escala, ajuste fino, alinhamento) — treinar um modelo do tamanho dos maiores do mercado exige computação de milhões de dólares; o alcance realista é o modelo pequeno do zero mais o ajuste fino de modelo aberto
- [ ] LoRA/QLoRA em modelo aberto de ~8B, no notebook ou em GPU na nuvem
- [ ] Montar dataset próprio (suas apostilas, exercícios, fichas duplas) com licença e sem dado de aluno
- **Desenvolver:** modelo 8B ajustado ao seu estilo didático, comparado contra o modelo base num conjunto de perguntas fixo.
- **Leitura:** *Build a Large Language Model (From Scratch)* (Sebastian Raschka)

## IA7 — MLOps
- [ ] Servir modelo (API), versionar modelo e dado, monitorar desvio
- **Desenvolver:** o modelo do IA3 ou IA6 rodando atrás do aura-analytics com observabilidade do Passo 10.

---

## ⚖️ Limites que valem para toda IA do ecossistema
- **IA que sugere investimento** é recomendação perante a CVM — passa pela sócia certificada ([formacao-academica](formacao-academica.md)).
- **Dado de aluno e dado financeiro** nunca entram em dataset de treino sem anonimização e base legal (LGPD).

## 🔗 Ligações
- Finanças e econometria: [trilha-financas-economia](trilha-financas-economia.md)
- Engenharia por trás de modelo em produção: [trilha-engenharia-software](trilha-engenharia-software.md)
- Matemática: [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md)
