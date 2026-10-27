#!/usr/bin/env bash
# Laboratório de dados e de IA no Ubuntu do WSL2: um projeto uv em ~/dev/lab-ia.
# Seguro para rodar várias vezes: o que já está instalado é pulado.
#
#   bash scripts/wsl/lab-ia.sh --simular    # mostra o que faria
#   bash scripts/wsl/lab-ia.sh              # dados + IA (PyTorch com CUDA, cerca de 6 GB)
#   bash scripts/wsl/lab-ia.sh --so-dados   # só a parte de engenharia de dados
#
# Dados: Polars, pandas (<3, pelo PySpark), PyArrow, DuckDB, JupyterLab, dbt (Postgres e DuckDB), PySpark (+ Java 17), MLflow.
# IA:    PyTorch, Transformers, PEFT, TRL, Datasets, Accelerate, bitsandbytes e gguf.
# O fine-tuning de modelos 8B roda no Kaggle ou numa GPU alugada: a GTX 1650 tem 4 GB e o QLoRA de 8B pede 6 GB ou mais.
set -euo pipefail

SIMULAR=0; SO_DADOS=0; PASTA="$HOME/dev/lab-ia"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --simular) SIMULAR=1 ;;
    --so-dados) SO_DADOS=1 ;;
    --pasta) PASTA="${2:?informe a pasta}"; shift ;;
    -h|--help) sed -n '2,11p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done

SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
APT="DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
mkdir -p "$HOME/.local/state"
LOG="$HOME/.local/state/lab-ia-$(date +%Y%m%d-%H%M).log"
ERROS=0
export PATH="$HOME/.local/bin:$PATH"

DADOS=(polars "pandas<3" pyarrow duckdb jupyterlab ipykernel dbt-core dbt-postgres dbt-duckdb pyspark mlflow)
IA=(torch transformers peft trl datasets accelerate bitsandbytes gguf)

linha() { printf '%-9s %-28s %-11s %s\n' "$1" "$2" "$3" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "INSTALARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "INSTALADO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}
faltando() {  # pacotes da lista que ainda não estão no projeto
  local out=()
  for p in "$@"; do
    local nome="${p%%[<>=]*}"  # "pandas<3" -> pandas
    if [[ ! -f "$PASTA/pyproject.toml" ]] || ! grep -qiE "\"$nome([<>=~! \[]|\")" "$PASTA/pyproject.toml"; then out+=("$p"); fi
  done
  echo "${out[@]:-}"
}

echo "Registro em: $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

if ! tem uv; then linha base uv "FALTA" "rode antes o bootstrap.sh"; exit 1; fi

# Java 17 para o PySpark
if tem java; then linha base "Java (PySpark)" "JA TEM" "$(java -version 2>&1 | grep -i version | head -1)"
else rodar base "Java 17 (PySpark)" bash -c "$SUDO apt-get update -y && $SUDO env $APT install openjdk-17-jre-headless"; fi

# Projeto uv
if [[ -f "$PASTA/pyproject.toml" ]]; then linha projeto "$PASTA" "JA TEM"
else rodar projeto "$PASTA" bash -c "mkdir -p '$PASTA' && cd '$PASTA' && uv init --bare --python 3.12 --name lab-ia"; fi

read -r -a F_DADOS <<< "$(faltando "${DADOS[@]}")"
if [[ ${#F_DADOS[@]} -eq 0 ]]; then linha dados "pacotes de dados (${#DADOS[@]})" "JA TEM"
else rodar dados "pacotes de dados (${#F_DADOS[@]})" bash -c "cd '$PASTA' && uv add $(printf "'%s' " "${F_DADOS[@]}")"; fi

if [[ $SO_DADOS -eq 0 ]]; then
  read -r -a F_IA <<< "$(faltando "${IA[@]}")"
  if [[ ${#F_IA[@]} -eq 0 ]]; then linha ia "pacotes de IA (${#IA[@]})" "JA TEM"
  else rodar ia "pacotes de IA (${#F_IA[@]})" bash -c "cd '$PASTA' && uv add ${F_IA[*]}"; fi
fi

# Kernel do Jupyter apontando para o projeto
if [[ $SIMULAR -eq 0 && -d "$PASTA/.venv" ]]; then
  (cd "$PASTA" && uv run python -m ipykernel install --user --name lab-ia --display-name "lab-ia" >>"$LOG" 2>&1) \
    && linha projeto "kernel do Jupyter" "OK" "lab-ia" || linha projeto "kernel do Jupyter" "AVISO" "veja $LOG"
fi

# GPU
if tem nvidia-smi && nvidia-smi >/dev/null 2>&1; then
  linha gpu "driver NVIDIA no WSL" "OK" "$(nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null | head -1)"
else
  linha gpu "driver NVIDIA no WSL" "AVISO" "atualize o driver NVIDIA no Windows; o WSL2 usa o driver de lá"
fi
if [[ $SO_DADOS -eq 0 && $SIMULAR -eq 0 && -d "$PASTA/.venv" ]]; then
  if r="$(cd "$PASTA" && uv run python -c 'import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else "")' 2>>"$LOG")"; then
    case "$r" in *True*) linha gpu "PyTorch e a GPU" "OK" "$r" ;; *) linha gpu "PyTorch e a GPU" "AVISO" "$r (roda na CPU)" ;; esac
  else linha gpu "PyTorch" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
fi

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $ERROS -gt 0 ]]; then echo "$ERROS item(ns) com problema. Veja $LOG"; exit 1
else echo "Pronto. Abra com: cd $PASTA && uv run jupyter lab"; fi
