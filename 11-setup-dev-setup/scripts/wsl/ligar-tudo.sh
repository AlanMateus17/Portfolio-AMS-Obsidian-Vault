#!/usr/bin/env bash
# Liga o setup para o celular (v2.28). Seguro para rodar de novo: o que já está ligado é pulado.
#   bash scripts/wsl/ligar-tudo.sh --simular   # mostra o que faria
#   bash scripts/wsl/ligar-tudo.sh             # instala o que falta e liga os serviços
#   bash scripts/wsl/ligar-tudo.sh --status    # só mostra o que está no ar
#   bash scripts/wsl/ligar-tudo.sh --desligar  # para os serviços (não desinstala nada)
#
# Depois de ligado, do celular:
#   · App do Claude → Code: a sessão "Setup AMtech" roda no seu notebook (Remote Control, plano Pro ou Max).
#   · Telegram: /pedir TEXTO manda para a fila, que usa Claude → cota grátis → modelo local, nessa ordem.
# Serviços (systemd do usuário): amtech-remoto, amtech-fila, amtech-bot (se o Telegram estiver configurado), ollama.
set -uo pipefail
USER="${USER:-$(id -un)}"
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODO="${1:-}"
UNIDADES="$HOME/.config/systemd/user"
CFG="$HOME/.config/amtech"
MODELOS=(qwen2.5-coder:7b qwen2.5:7b)
falhas=0; pendentes=()
tem() { command -v "$1" >/dev/null 2>&1; }
ok() { printf '  [ok]   %s\n' "$*"; }
faz() { printf '  [faz]  %s\n' "$*"; }
falta() { printf '  [você] %s\n' "$*"; pendentes+=("$*"); }
erro() { printf '  [erro] %s\n' "$*"; falhas=$((falhas + 1)); }
etapa() { echo; echo "== $*"; }
sim() { [[ "$MODO" == "--simular" ]]; }
export PATH="$HOME/.local/bin:$PATH"

status() {
  etapa "Status"
  for u in amtech-remoto amtech-fila amtech-bot ollama; do
    if systemctl --user is-active --quiet "$u" 2>/dev/null || systemctl is-active --quiet "$u" 2>/dev/null; then ok "$u no ar"
    else printf '  [--]   %s parado\n' "$u"; fi
  done
  curl -fsS -m 3 http://localhost:11434/api/tags >/dev/null 2>&1 && ok "Ollama responde" || printf '  [--]   Ollama não responde\n'
  curl -fsS -m 3 http://localhost:4000/health/liveliness >/dev/null 2>&1 && ok "LiteLLM responde" || printf '  [--]   LiteLLM fora do ar (a fila usa Gemini direto ou o local)\n'
  python3 "$RAIZ/tools/remoto/fila.py" listar 2>/dev/null | tail -4
}

case "$MODO" in
  --status) status; exit 0 ;;
  --desligar)
    systemctl --user stop amtech-remoto amtech-fila amtech-bot 2>/dev/null
    (cd "$RAIZ/infra/ia" && docker compose down 2>/dev/null)
    echo "Serviços parados. Para ligar de novo: just ligar"; exit 0 ;;
esac

etapa "1/7 Ambiente (systemd no WSL)"
if [[ "$(ps -p 1 -o comm= 2>/dev/null)" == "systemd" ]]; then ok "systemd ativo"
else
  sim && faz "gravaria /etc/wsl.conf com systemd=true" || { printf '[boot]\nsystemd=true\n' | sudo tee /etc/wsl.conf >/dev/null; }
  falta "No PowerShell: wsl --shutdown. Abra o Ubuntu de novo e rode just ligar outra vez."
  sim || { echo; echo "Pare aqui: sem systemd os serviços não sobem."; exit 1; }
fi
if loginctl show-user "$USER" 2>/dev/null | grep -q 'Linger=yes'; then ok "serviços continuam sem terminal aberto (linger)"
else sim && faz "loginctl enable-linger $USER" || sudo loginctl enable-linger "$USER"; fi

etapa "2/7 Claude Code (assinatura, Remote Control)"
if tem claude; then ok "Claude Code $(claude --version 2>/dev/null | head -1)"
else sim && faz "instalaria o Claude Code" || curl -fsSL https://claude.ai/install.sh | bash || erro "instalação do Claude Code"; fi
if [[ -f "$CFG/remoto-aceito" ]]; then ok "Remote Control já aceito nesta pasta"
else falta "Uma vez só, num terminal: cd $RAIZ && claude remote-control  → responda y, y, escolha 2 (worktree), confira o QR no celular e Ctrl+C. Depois: touch $CFG/remoto-aceito && just ligar"; fi

etapa "3/7 Ollama e modelos locais (funcionam sem crédito nenhum)"
if curl -fsS -m 3 http://localhost:11434/api/tags >/dev/null 2>&1; then ok "Ollama no ar"
elif tem ollama; then sim && faz "sudo systemctl enable --now ollama" || sudo systemctl enable --now ollama || erro "ligar o Ollama"
else sim && faz "instalaria o Ollama (usa a GTX 1650 se o driver NVIDIA do Windows estiver em dia)" \
  || { { tem zstd || sudo apt-get install -y -qq zstd; } && curl -fsSL https://ollama.com/install.sh | sh || erro "instalação do Ollama"; }; fi  # o instalador do Ollama exige zstd para extrair
# Depois de instalar ou ligar, o serviço leva alguns segundos para responder: sem esperar, o ollama pull falhava
# com "could not connect to ollama server".
if ! sim && tem ollama; then for _ in $(seq 1 30); do curl -fsS -m 2 http://localhost:11434/api/tags >/dev/null 2>&1 && break; sleep 1; done; fi
for m in "${MODELOS[@]}"; do
  if tem ollama && ollama list 2>/dev/null | grep -q "^${m}"; then ok "modelo $m"
  else sim && faz "ollama pull $m (~4,7 GB)" || { tem ollama && ollama pull "$m" || erro "baixar $m"; }; fi
done

etapa "4/7 aider (agente que roda com qualquer modelo)"
if tem aider; then ok "aider"
elif tem uv; then sim && faz "uv tool install aider-chat" || uv tool install aider-chat || erro "aider"
else erro "uv ausente: rode antes just instalar"; fi

etapa "5/7 Gateway LiteLLM (opcional; precisa do Docker)"
ENV_IA="$RAIZ/infra/ia/.env"
if [[ ! -f "$ENV_IA" ]]; then
  if sim; then faz "criaria infra/ia/.env com chave mestra nova"
  else
    cp "$RAIZ/infra/ia/ia.env.example" "$ENV_IA" && chmod 600 "$ENV_IA"
    sed -i "s|^LITELLM_MASTER_KEY=.*|LITELLM_MASTER_KEY=$(openssl rand -hex 24)|" "$ENV_IA"
    falta "Copie a LITELLM_MASTER_KEY de infra/ia/.env para o KeePassXC e cole a GEMINI_API_KEY grátis (aistudio.google.com) no mesmo arquivo."
  fi
fi
if ! grep -q '^GEMINI_API_KEY=.' "$ENV_IA" 2>/dev/null; then falta "Sem GEMINI_API_KEY em infra/ia/.env, a fila pula a cota grátis e vai do Claude direto para o local."; fi
if tem docker && docker info >/dev/null 2>&1; then
  if sim; then faz "docker compose up -d em infra/ia"
  elif (cd "$RAIZ/infra/ia" && docker compose up -d >/dev/null 2>&1); then ok "LiteLLM em http://localhost:4000"
  else erro "subir o LiteLLM (cd infra/ia && docker compose up -d mostra o motivo)"; fi
else ok "Docker desligado: a fila funciona sem o gateway (Gemini direto e Ollama direto)"; fi

etapa "6/7 Serviços que ficam no ar"
mkdir -p "$UNIDADES" "$CFG" && chmod 700 "$CFG"
escrever() { # nome, descrição, comando, pasta
  local destino="$UNIDADES/$1.service"
  local corpo
  corpo="[Unit]
Description=$2
After=network-online.target

[Service]
WorkingDirectory=$4
Environment=PATH=$HOME/.local/bin:$HOME/.local/share/mise/shims:/usr/local/bin:/usr/bin:/bin
ExecStart=$3
Restart=always
RestartSec=30

[Install]
WantedBy=default.target"
  if [[ -f "$destino" ]] && [[ "$(cat "$destino")" == "$corpo" ]]; then ok "$1 já configurado"
  elif sim; then faz "gravaria $destino"
  else printf '%s\n' "$corpo" > "$destino" && ok "$1 gravado"; fi
}
CLAUDE_BIN="$(command -v claude || echo "$HOME/.local/bin/claude")"
escrever amtech-fila "Fila de pedidos do celular (AMtech)" "/usr/bin/python3 $RAIZ/tools/remoto/fila.py trabalhar" "$HOME/dev"
escrever amtech-remoto "Claude Code Remote Control (AMtech)" "$CLAUDE_BIN remote-control --name \"Setup AMtech\" --spawn worktree" "$RAIZ"
[[ -f "$CFG/telegram.env" ]] && escrever amtech-bot "Bot do Telegram (AMtech)" "/usr/bin/python3 $RAIZ/tools/remoto/bot.py" "$RAIZ" \
  || falta "Telegram: crie o bot no @BotFather e siga docs/operacao/celular.md (passo 3). Sem ele, o celular usa só o app do Claude."

if ! sim; then
  systemctl --user daemon-reload
  ligar=(amtech-fila)
  [[ -f "$CFG/remoto-aceito" ]] && ligar+=(amtech-remoto)
  [[ -f "$UNIDADES/amtech-bot.service" ]] && ligar+=(amtech-bot)
  systemctl --user enable --now "${ligar[@]}" >/dev/null 2>&1 && ok "no ar: ${ligar[*]}" || erro "ligar ${ligar[*]} (veja: journalctl --user -u amtech-fila)"
fi

etapa "7/7 Windows: não deixar o WSL nem o notebook dormirem"
PS1="$RAIZ/scripts/windows/manter-ligado.ps1"
if [[ -f "$CFG/windows-ok" ]]; then ok "WSL e energia já configurados no Windows"
elif sim; then faz "abriria o PowerShell (pede permissão de administrador) com manter-ligado.ps1"
elif tem powershell.exe && tem wslpath; then
  echo "  O Windows vai pedir permissão de administrador (uma vez só)."
  powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$(wslpath -w "$PS1")" -Distro "${WSL_DISTRO_NAME:-Ubuntu}" \
    && touch "$CFG/windows-ok" && ok "tarefa de inicialização criada no Windows" || erro "manter-ligado.ps1 (rode de novo e aceite a permissão)"
else falta "No PowerShell: powershell -ExecutionPolicy Bypass -File $PS1"; fi

status
echo
if ((${#pendentes[@]})); then echo "O que é com você (${#pendentes[@]}):"; printf '  - %s\n' "${pendentes[@]}"; fi
if sim; then echo "Simulação. Rode sem --simular para aplicar."
elif ((falhas)); then echo "$falhas erro(s) acima. Corrija e rode just ligar de novo (o que já está pronto é pulado)."; exit 1
else echo "Pronto. Do celular: app do Claude → Code → 'Setup AMtech'; ou Telegram /pedir."; fi
