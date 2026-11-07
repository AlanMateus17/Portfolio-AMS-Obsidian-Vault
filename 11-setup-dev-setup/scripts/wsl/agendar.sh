#!/usr/bin/env bash
# Agenda as rotinas no cron do Ubuntu (idempotente: rodar de novo não duplica).
#   bash scripts/wsl/agendar.sh            # mostra o que vai agendar
#   bash scripts/wsl/agendar.sh --aplicar  # grava no crontab
#   bash scripts/wsl/agendar.sh --remover  # tira as linhas do setup
# Resumo da manhã às 6h10 no Telegram; manutenção no domingo às 9h (aplica o que não pede sudo, simula o apt);
# backup diário às 22h30, com aviso no Telegram se falhar. O WSL precisa estar aberto (na VM, roda sempre).
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MARCA="# amtech-setup"
LINHAS="10 6 * * * bash $RAIZ/scripts/wsl/resumo-manha.sh --telegram >/dev/null 2>&1 $MARCA
0 9 * * 0 bash $RAIZ/scripts/wsl/manutencao-semanal.sh --usuario > \$HOME/manutencao-ultima.log 2>&1; python3 $RAIZ/tools/remoto/bot.py --avisar 'Manutenção de domingo feita (apt só simulado): veja ~/manutencao-ultima.log' $MARCA
30 22 * * * bash $RAIZ/scripts/wsl/backup.sh > \$HOME/backup-ultimo.log 2>&1 || python3 $RAIZ/tools/remoto/bot.py --avisar 'Backup FALHOU: veja ~/backup-ultimo.log' $MARCA"
atual="$(crontab -l 2>/dev/null | grep -v "$MARCA" || true)"
case "${1:-}" in
  --aplicar) printf '%s\n%s\n' "$atual" "$LINHAS" | sed '/^$/d' | crontab - ; echo "Agendado:"; crontab -l | grep "$MARCA" ;;
  --remover) printf '%s\n' "$atual" | sed '/^$/d' | crontab - ; echo "Linhas do setup removidas." ;;
  *) echo "Vai agendar (use --aplicar):"; echo "$LINHAS" ;;
esac
