#!/usr/bin/env bash
# Roda um comando com um segredo vindo direto do KeePassXC, sem .env em texto puro.
#   bash scripts/wsl/segredos.sh "Automacao/N8N_CHAVE" N8N_CHAVE -- docker compose up -d
# Pede a senha do cofre (digite à mão). O segredo existe só no ambiente daquele comando.
# Cofre: variável COFRE ou o padrão abaixo. Precisa do keepassxc-cli (sudo apt install keepassxc).
set -euo pipefail
COFRE="${COFRE:-/mnt/c/Users/${USER}/cofre senhas.kdbx}"
[[ $# -ge 4 && "$3" == "--" ]] || { sed -n '2,5p' "$0"; exit 1; }
ENTRADA="$1"; VAR="$2"; shift 3
command -v keepassxc-cli >/dev/null 2>&1 || { echo "Instale: sudo apt install keepassxc"; exit 1; }
[[ -f "$COFRE" ]] || { echo "Cofre não encontrado: $COFRE (defina COFRE=...)"; exit 1; }
valor="$(keepassxc-cli show -q -s -a Password "$COFRE" "$ENTRADA")"
export "$VAR=$valor"
unset valor
exec "$@"
