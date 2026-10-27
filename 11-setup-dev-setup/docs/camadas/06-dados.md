<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 06 · Dados e treino de IA

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Os seus dados viram tabelas limpas e datasets; o treino pesado roda numa GPU da nuvem e o modelo volta para o Ollama do notebook.

**13 blocos** · 2 precisam de conta · 0 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_dados["Dados e treino de IA"]
    n_pyds["Python de dados (Polars, Jupyter)"]
    n_duck["DuckDB + Parquet"]
    n_dbt["dbt Core"]
    n_orq["Airflow (orquestração)"]
    n_spark["Spark (PySpark)"]
    n_dset["Seus datasets (só conteúdo seu)"]
    n_torch["PyTorch + CUDA (WSL2)"]
    n_hf["Hugging Face (modelos e Hub)"]
    n_unsl["Unsloth (QLoRA)"]
    n_kgl["Kaggle · Colab (GPU grátis)"]
    n_mlflow["MLflow (experimentos)"]
    n_evals["Avaliação dos modelos"]
    n_gguf["llama.cpp (GGUF)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_acv["Acervo (seus documentos)"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_metrics["Banco de métricas (PostgreSQL)"]
    n_painel["Painel de lucro (Grafana)"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_exyaml["Exercícios em YAML"]
    n_fonte["Fonte única (Markdown + Pandoc)"]
  end
  subgraph L_est["Estudo e carreira"]
    n_dez["Zoomcamp de dados + cursos de IA"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_whis["Whisper (local)"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gpuh["GPU por hora (RunPod e afins)"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
    n_kafka["Kafka"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_oll["Ollama"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_rt[".NET 10 · Node · Python"]
    n_wsl["Ubuntu (WSL2)"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_hw["Hardware"]
    n_nb["Acer Nitro (32 GB, GTX 1650)"]
  end
  n_pyds -->|"consulta Parquet"| n_duck
  n_rt -->|"Python + uv"| n_pyds
  n_orq -->|"extrações agendadas"| n_pyds
  n_dez -->|"projetos dos módulos"| n_pyds
  n_dbt -->|"modelos locais"| n_duck
  n_spark -->|"mesmos Parquet"| n_duck
  n_dbt -->|"modelos limpos"| n_painel
  n_metrics -->|"tabelas brutas"| n_dbt
  n_orq -->|"roda todo dia"| n_dbt
  n_docker -->|"container"| n_orq
  n_kafka -->|"streaming"| n_spark
  n_dset -->|"treina com"| n_unsl
  n_dset -->|"dataset privado"| n_hf
  n_obsd -->|"suas notas"| n_dset
  n_exyaml -->|"exercícios com gabarito"| n_dset
  n_whis -->|"transcrições das suas aulas"| n_dset
  n_fonte -->|"texto do livro"| n_dset
  n_acv -->|"só o que é seu"| n_dset
  n_torch -->|"base do treino"| n_unsl
  n_wsl -->|"CUDA no WSL2"| n_torch
  n_nb -->|"GTX 1650 (4 GB)"| n_torch
  n_dez -->|"exercícios de redes neurais"| n_torch
  n_hf -->|"modelos base; guarda o adaptador"| n_unsl
  n_unsl -->|"registra o treino"| n_mlflow
  n_unsl -->|"modelo treinado"| n_evals
  n_kgl -->|"GPU grátis (T4 16 GB)"| n_unsl
  n_gpuh -->|"GPU de 24 GB"| n_unsl
  n_evals -->|"aprovado"| n_gguf
  n_gguf -->|"importa o modelo"| n_oll
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_pyds,n_duck,n_dbt,n_orq,n_spark,n_dset,n_torch,n_hf,n_unsl,n_kgl,n_mlflow,n_evals,n_gguf desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Python de dados (Polars, Jupyter)](#pyds) | Local | Polars, pandas e JupyterLab num projeto uv em ~/dev/lab-ia. A base de toda a trilha de dados e de IA. | passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [DuckDB + Parquet](#duck) | Local | Banco analítico que roda dentro do Python e lê Parquet direto. Faz no notebook o que muita empresa faz num data warehouse. | passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [dbt Core](#dbt) | Local | Transforma as tabelas brutas (vendas, gastos, publicações) em modelos limpos e testados, com SQL versionado no Git. | passo 21.7 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Airflow (orquestração)](#orq) | Local | Agenda e acompanha as rotinas de dados: extrair das plataformas, rodar o dbt, avisar se falhar. É o orquestrador mais pedido em vaga. Roda em Docker. | passo 21.8 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Spark (PySpark)](#spark) | Local | Processamento distribuído. No notebook roda em modo local, o suficiente para aprender a API que as empresas usam com volumes grandes. | passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Seus datasets (só conteúdo seu)](#dset) | Local | Pares de pergunta e resposta tirados das suas notas, exercícios, livro e aulas que você gravou. Nada de aulas da Udemy, DIO, Alura ou de terceiros; dados de alunos só com consentimento, e de menores só com autorização dos responsáveis. | passo 21.10 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [PyTorch + CUDA (WSL2)](#torch) | Local | Base do treino de redes neurais. A GTX 1650 (Turing, 4 GB) tem suporte no CUDA do WSL2: serve para aprender, treinar modelos pequenos e testar código antes de pagar GPU. | passo 21.3 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Hugging Face (modelos e Hub)](#hf) | Remoto · precisa de conta | Transformers, PEFT, TRL e Datasets; no Hub ficam os modelos base e, em repositórios privados, os seus datasets e adaptadores. | passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Unsloth (QLoRA)](#unsl) | Local | Fine-tuning com pouca memória. Um 8B em QLoRA pede no mínimo 6 GB de VRAM: não cabe nos 4 GB da GTX 1650, então o treino do 8B roda no Kaggle ou numa GPU alugada. | passo 21.11 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Kaggle · Colab (GPU grátis)](#kgl) | Remoto · precisa de conta | Notebooks com GPU T4 de 16 GB sem pagar: o Kaggle dá 30 horas por semana, com sessões de até 9 horas. Suficiente para o primeiro fine-tuning de um 8B. | passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.11 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [MLflow (experimentos)](#mlflow) | Local | Registra cada treino: dados usados, parâmetros, métricas e o modelo gerado. Sem isso você não sabe qual versão ficou melhor. | passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Avaliação dos modelos](#evals) | Local | Um conjunto de perguntas com respostas certas, separado do treino. O modelo novo só substitui o anterior se ganhar nele. | passo 21.10 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.12 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [llama.cpp (GGUF)](#gguf) | Local | Converte e quantiza o modelo treinado para GGUF, o formato que o Ollama carrega no notebook. | passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.12 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |

<a id="pyds"></a>

### Python de dados (Polars, Jupyter)

*Local*

Polars, pandas e JupyterLab num projeto uv em ~/dev/lab-ia. A base de toda a trilha de dados e de IA.

**Quando entra:** passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DuckDB + Parquet](06-dados.md#duck) | Dados e treino de IA | consulta Parquet |
| ← recebe de | [.NET 10 · Node · Python](04-lin.md#rt) | Linux (Ubuntu no WSL2, Arch no 2º disco) | Python + uv |
| ← recebe de | [Airflow (orquestração)](06-dados.md#orq) | Dados e treino de IA | extrações agendadas |
| ← recebe de | [Zoomcamp de dados + cursos de IA](14-est.md#dez) | Estudo e carreira | projetos dos módulos |

<a id="duck"></a>

### DuckDB + Parquet

*Local*

Banco analítico que roda dentro do Python e lê Parquet direto. Faz no notebook o que muita empresa faz num data warehouse.

**Quando entra:** passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Python de dados (Polars, Jupyter)](06-dados.md#pyds) | Dados e treino de IA | consulta Parquet |
| ← recebe de | [dbt Core](06-dados.md#dbt) | Dados e treino de IA | modelos locais |
| ← recebe de | [Spark (PySpark)](06-dados.md#spark) | Dados e treino de IA | mesmos Parquet |

<a id="dbt"></a>

### dbt Core

*Local*

Transforma as tabelas brutas (vendas, gastos, publicações) em modelos limpos e testados, com SQL versionado no Git.

**Quando entra:** passo 21.7 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DuckDB + Parquet](06-dados.md#duck) | Dados e treino de IA | modelos locais |
| → envia para | [Painel de lucro (Grafana)](21-mkt.md#painel) | Marketing, automação e medição | modelos limpos |
| ← recebe de | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | tabelas brutas |
| ← recebe de | [Airflow (orquestração)](06-dados.md#orq) | Dados e treino de IA | roda todo dia |

<a id="orq"></a>

### Airflow (orquestração)

*Local*

Agenda e acompanha as rotinas de dados: extrair das plataformas, rodar o dbt, avisar se falhar. É o orquestrador mais pedido em vaga. Roda em Docker.

**Quando entra:** passo 21.8 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [dbt Core](06-dados.md#dbt) | Dados e treino de IA | roda todo dia |
| → envia para | [Python de dados (Polars, Jupyter)](06-dados.md#pyds) | Dados e treino de IA | extrações agendadas |
| ← recebe de | [Docker + Compose](09-cnt.md#docker) | Containers, Kubernetes e infra como código | container |

<a id="spark"></a>

### Spark (PySpark)

*Local*

Processamento distribuído. No notebook roda em modo local, o suficiente para aprender a API que as empresas usam com volumes grandes.

**Quando entra:** passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DuckDB + Parquet](06-dados.md#duck) | Dados e treino de IA | mesmos Parquet |
| ← recebe de | [Kafka](09-cnt.md#kafka) | Containers, Kubernetes e infra como código | streaming |

<a id="dset"></a>

### Seus datasets (só conteúdo seu)

*Local*

Pares de pergunta e resposta tirados das suas notas, exercícios, livro e aulas que você gravou. Nada de aulas da Udemy, DIO, Alura ou de terceiros; dados de alunos só com consentimento, e de menores só com autorização dos responsáveis.

**Quando entra:** passo 21.10 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | treina com |
| → envia para | [Hugging Face (modelos e Hub)](06-dados.md#hf) | Dados e treino de IA | dataset privado |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | suas notas |
| ← recebe de | [Exercícios em YAML](15-editora.md#exyaml) | Editora AMS Silva (produção de livros) | exercícios com gabarito |
| ← recebe de | [Whisper (local)](13-cont.md#whis) | Produção de conteúdo | transcrições das suas aulas |
| ← recebe de | [Fonte única (Markdown + Pandoc)](15-editora.md#fonte) | Editora AMS Silva (produção de livros) | texto do livro |
| ← recebe de | [Acervo (seus documentos)](23-oper.md#acv) | Operação do grupo (esteira, marca, qualidade) | só o que é seu |

<a id="torch"></a>

### PyTorch + CUDA (WSL2)

*Local*

Base do treino de redes neurais. A GTX 1650 (Turing, 4 GB) tem suporte no CUDA do WSL2: serve para aprender, treinar modelos pequenos e testar código antes de pagar GPU.

**Quando entra:** passo 21.3 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | base do treino |
| ← recebe de | [Ubuntu (WSL2)](04-lin.md#wsl) | Linux (Ubuntu no WSL2, Arch no 2º disco) | CUDA no WSL2 |
| ← recebe de | [Acer Nitro (32 GB, GTX 1650)](01-hw.md#nb) | Hardware | GTX 1650 (4 GB) |
| ← recebe de | [Zoomcamp de dados + cursos de IA](14-est.md#dez) | Estudo e carreira | exercícios de redes neurais |

<a id="hf"></a>

### Hugging Face (modelos e Hub)

*Remoto · precisa de conta*

Transformers, PEFT, TRL e Datasets; no Hub ficam os modelos base e, em repositórios privados, os seus datasets e adaptadores.

**Quando entra:** passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | modelos base; guarda o adaptador |
| ← recebe de | [Seus datasets (só conteúdo seu)](06-dados.md#dset) | Dados e treino de IA | dataset privado |

<a id="unsl"></a>

### Unsloth (QLoRA)

*Local*

Fine-tuning com pouca memória. Um 8B em QLoRA pede no mínimo 6 GB de VRAM: não cabe nos 4 GB da GTX 1650, então o treino do 8B roda no Kaggle ou numa GPU alugada.

**Quando entra:** passo 21.11 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MLflow (experimentos)](06-dados.md#mlflow) | Dados e treino de IA | registra o treino |
| → envia para | [Avaliação dos modelos](06-dados.md#evals) | Dados e treino de IA | modelo treinado |
| ← recebe de | [PyTorch + CUDA (WSL2)](06-dados.md#torch) | Dados e treino de IA | base do treino |
| ← recebe de | [Hugging Face (modelos e Hub)](06-dados.md#hf) | Dados e treino de IA | modelos base; guarda o adaptador |
| ← recebe de | [Seus datasets (só conteúdo seu)](06-dados.md#dset) | Dados e treino de IA | treina com |
| ← recebe de | [Kaggle · Colab (GPU grátis)](06-dados.md#kgl) | Dados e treino de IA | GPU grátis (T4 16 GB) |
| ← recebe de | [GPU por hora (RunPod e afins)](12-nuvem.md#gpuh) | Nuvem, código e entrega | GPU de 24 GB |

<a id="kgl"></a>

### Kaggle · Colab (GPU grátis)

*Remoto · precisa de conta*

Notebooks com GPU T4 de 16 GB sem pagar: o Kaggle dá 30 horas por semana, com sessões de até 9 horas. Suficiente para o primeiro fine-tuning de um 8B.

**Quando entra:** passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.11 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | GPU grátis (T4 16 GB) |

<a id="mlflow"></a>

### MLflow (experimentos)

*Local*

Registra cada treino: dados usados, parâmetros, métricas e o modelo gerado. Sem isso você não sabe qual versão ficou melhor.

**Quando entra:** passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | registra o treino |

<a id="evals"></a>

### Avaliação dos modelos

*Local*

Um conjunto de perguntas com respostas certas, separado do treino. O modelo novo só substitui o anterior se ganhar nele.

**Quando entra:** passo 21.10 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.12 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [llama.cpp (GGUF)](06-dados.md#gguf) | Dados e treino de IA | aprovado |
| ← recebe de | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | modelo treinado |

<a id="gguf"></a>

### llama.cpp (GGUF)

*Local*

Converte e quantiza o modelo treinado para GGUF, o formato que o Ollama carrega no notebook.

**Quando entra:** passo 21.4 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029); passo 21.12 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Ollama](05-ia.md#oll) | Agentes de IA e sandbox | importa o modelo |
| ← recebe de | [Avaliação dos modelos](06-dados.md#evals) | Dados e treino de IA | aprovado |

---

[↑ Camada 07 · Assistentes de IA (chat, pesquisa e estudo)](07-chat.md) · [↓ Camada 05 · Agentes de IA e sandbox](05-ia.md)
