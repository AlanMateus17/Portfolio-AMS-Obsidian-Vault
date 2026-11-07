#!/usr/bin/env bash
# Ferramentas complementares do setup (contexto mestre da empresa solo), no Ubuntu do WSL.
# Seguro para rodar várias vezes: o que já está instalado é pulado. Rode depois do bootstrap.sh.
#
#   bash scripts/wsl/extras.sh --simular   # mostra o que faria
#   bash scripts/wsl/extras.sh             # instala
#
# Instala: chezmoi (dotfiles), as CLIs do ~/.config/mise/config.toml (zellij, yazi, d2, vegeta, age, sops,
# bore, gum, soft-serve, goreleaser, cargo-dist, probe-rs, tree-sitter, stripe, litestream, pocketbase),
# ferramentas Python pelo uv (posting, harlequin, aider, llm com o plugin do Ollama, beancount, fava),
# e do apt: podman, git-lfs, hledger e neovim.
set -euo pipefail

SIMULAR=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --simular) SIMULAR=1 ;;
    -h|--help) sed -n '2,11p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done

SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
APT="DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
mkdir -p "$HOME/.local/state" "$HOME/.local/bin"
LOG="$HOME/.local/state/extras-$(date +%Y%m%d-%H%M).log"
ERROS=0
export PATH="$HOME/.local/bin:$PATH"
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

linha() { printf '%-10s %-34s %-12s %s\n' "$1" "$2" "$3" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "INSTALARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "INSTALADO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}
echo "Registro em: $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

# ------------------------------------------------------------------ 1. apt
PACOTES=(podman git-lfs hledger neovim)
FALTAM=()
for p in "${PACOTES[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || FALTAM+=("$p"); done
if [[ ${#FALTAM[@]} -eq 0 ]]; then linha "apt" "podman, git-lfs, hledger, neovim" "JA TEM"
else rodar "apt" "${FALTAM[*]}" bash -c "$SUDO apt-get update -y && $SUDO env $APT install ${FALTAM[*]}"; fi
if [[ $SIMULAR -eq 0 ]] && tem git-lfs; then git lfs install --skip-repo >>"$LOG" 2>&1 || true; fi

# ------------------------------------------------------------------ 2. chezmoi e dotfiles
if tem chezmoi; then linha "dotfiles" "chezmoi" "JA TEM"
else rodar "dotfiles" "chezmoi" bash -c 'sh -c "$(curl -fsLS get.chezmoi.io)" -- -b "$HOME/.local/bin"'; fi
if [[ -f "$HOME/.config/mise/config.toml" ]]; then linha "dotfiles" "config do mise" "JA TEM"
elif [[ $SIMULAR -eq 1 ]]; then linha "dotfiles" "config do mise" "COPIARIA" "de infra/dotfiles (o chezmoi assume depois)"
else mkdir -p "$HOME/.config/mise" && cp "$RAIZ/infra/dotfiles/dot_config/mise/config.toml" "$HOME/.config/mise/config.toml"; linha "dotfiles" "config do mise" "COPIADO"; fi

# ------------------------------------------------------------------ 3. CLIs pelo mise
if ! tem mise; then linha "mise" "mise" "FALTA" "rode antes: bash scripts/wsl/bootstrap.sh"
else rodar "mise" "runtimes e CLIs (mise install)" mise install --yes; fi

# ------------------------------------------------------------------ 4. ferramentas Python pelo uv
if ! tem uv; then linha "uv" "uv" "FALTA" "rode antes: bash scripts/wsl/bootstrap.sh"
else
  for item in "posting" "harlequin[postgres]" "aider-chat" "llm" "beancount" "fava"; do
    nome="${item%%[*}"; [[ "$nome" == "aider-chat" ]] && cmd="aider" || cmd="$nome"
    if tem "$cmd"; then linha "uv" "$nome" "JA TEM"; else rodar "uv" "$nome" uv tool install --python 3.12 "$item"; fi
  done
  if tem llm && [[ $SIMULAR -eq 0 ]]; then llm install llm-ollama >>"$LOG" 2>&1 || true; fi
fi

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $ERROS -gt 0 ]]; then echo "$ERROS erro(s). Veja $LOG"; exit 1
else echo "Pronto. Próximo: aplicar os dotfiles (passo solo-chezmoi) e abrir o zellij."; fi
