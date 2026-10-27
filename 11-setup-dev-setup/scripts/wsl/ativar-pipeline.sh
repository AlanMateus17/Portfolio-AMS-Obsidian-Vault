#!/usr/bin/env bash
# Liga o pipeline de conteúdo: um timer do systemd roda tools/conteudo/processar.py a cada 15 minutos.
#   bash scripts/wsl/ativar-pipeline.sh            # liga
#   bash scripts/wsl/ativar-pipeline.sh --desligar # desliga
set -euo pipefail
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
UNID="$HOME/.config/systemd/user"
CFG="$HOME/.config/amtech/conteudo.env"

if [[ "${1:-}" == "--desligar" ]]; then
  systemctl --user disable --now amtech-conteudo.timer 2>/dev/null || true
  echo "Pipeline desligado."
  exit 0
fi

[[ "$(ps -p 1 -o comm=)" == "systemd" ]] || { echo "O systemd não está ativo. Rode scripts/wsl/bootstrap.sh e depois 'wsl --shutdown' no PowerShell."; exit 1; }
if [[ ! -f "$CFG" ]]; then
  mkdir -p "$(dirname "$CFG")"
  cp "$REPO/tools/conteudo/conteudo.env.example" "$CFG"
  chmod 600 "$CFG"
  echo "Criei $CFG. Preencha a ANTHROPIC_API_KEY (e o Telegram, se quiser) e rode este script de novo."
  exit 1
fi
grep -qE '^ANTHROPIC_API_KEY=.+' "$CFG" || { echo "Falta a ANTHROPIC_API_KEY em $CFG."; exit 1; }

mkdir -p "$UNID"
cat > "$UNID/amtech-conteudo.service" <<EOF
[Unit]
Description=Pipeline de conteúdo AMtech (entrada -> fila de aprovação)

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 $REPO/tools/conteudo/processar.py --uma-vez
Environment=PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin
EOF
cat > "$UNID/amtech-conteudo.timer" <<EOF
[Unit]
Description=Roda o pipeline de conteúdo AMtech a cada 15 minutos

[Timer]
OnBootSec=2min
OnUnitActiveSec=15min
Persistent=true

[Install]
WantedBy=timers.target
EOF
systemctl --user daemon-reload
systemctl --user enable --now amtech-conteudo.timer
echo "Pipeline ligado. Próxima execução:"
systemctl --user list-timers amtech-conteudo.timer --no-pager | sed -n '1,2p'
echo "Para ver o que ele fez: journalctl --user -u amtech-conteudo.service -n 50"
