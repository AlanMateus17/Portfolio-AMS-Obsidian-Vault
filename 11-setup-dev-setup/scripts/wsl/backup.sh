#!/usr/bin/env bash
# Backup diário com o restic (agendado pelo agendar.sh). Sem pergunta: precisa da senha num arquivo só seu.
#   bash scripts/wsl/backup.sh             # faz o backup, limpa os antigos e confere
#   bash scripts/wsl/backup.sh --simular   # mostra o que faria
# Configuração em ~/.config/amtech/backup.env (modelo em infra/templates/backup.env.example):
#   RESTIC_REPOSITORY=/mnt/d/backup-restic
#   RESTIC_PASSWORD_FILE=$HOME/.config/amtech/restic.senha   (chmod 600; a mesma senha fica no KeePassXC)
#   BACKUP_PASTAS="$HOME/dev $HOME/AMtech $HOME/.config/amtech $HOME/financas"
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CONF="$HOME/.config/amtech/backup.env"
[[ -f "$CONF" ]] || { echo "Falta $CONF (copie infra/templates/backup.env.example)."; exit 1; }
# shellcheck source=/dev/null
source "$CONF"
export RESTIC_REPOSITORY RESTIC_PASSWORD_FILE
[[ -f "${RESTIC_PASSWORD_FILE:-}" ]] || { echo "Falta o arquivo de senha do restic."; exit 1; }
[[ "$(stat -c %a "$RESTIC_PASSWORD_FILE")" == "600" ]] || { echo "O arquivo de senha precisa de chmod 600."; exit 1; }
read -r -a PASTAS <<< "${BACKUP_PASTAS:?defina BACKUP_PASTAS}"
if [[ "${1:-}" == "--simular" ]]; then echo "restic backup ${PASTAS[*]}"; echo "restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune"; exit 0; fi
restic backup "${PASTAS[@]}" --exclude-caches --exclude node_modules --exclude bin --exclude obj --tag diario
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 12 --prune --tag diario
restic check --read-data-subset=2%
python3 "$RAIZ/tools/nucleo/nucleo.py" evento backup.concluido "$(restic snapshots --latest 1 --compact | tail -2 | head -1)" >/dev/null 2>&1 || true
