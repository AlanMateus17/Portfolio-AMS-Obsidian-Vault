#!/usr/bin/env bash
# Preenche as senhas vazias do .env com valores aleatórios e mostra onde guardá-las.
# Não troca senhas que já existem.
set -euo pipefail
cd "$(dirname "$0")"
[[ -f .env ]] || cp .env.example .env
chmod 600 .env
aleatoria() { head -c 32 /dev/urandom | base64 | tr -dc 'A-Za-z0-9' | head -c "$1"; }
for chave in METRICAS_SENHA GRAFANA_DB_SENHA GRAFANA_SENHA N8N_CHAVE; do
  if grep -qE "^${chave}=$" .env; then
    sed -i "s|^${chave}=$|${chave}=$(aleatoria 32)|" .env
    echo "Gerada: ${chave}"
  else
    echo "Mantida: ${chave}"
  fi
done
if grep -q 'SEU_USUARIO' .env; then
  sed -i "s|/home/SEU_USUARIO/AMtech|${HOME}/AMtech|" .env
  echo "AMTECH_DIR=${HOME}/AMtech"
fi
echo
echo "Guarde no KeePassXC: GRAFANA_SENHA (login 'admin' em http://localhost:3001) e N8N_CHAVE (sem ela, as credenciais do n8n não abrem)."
