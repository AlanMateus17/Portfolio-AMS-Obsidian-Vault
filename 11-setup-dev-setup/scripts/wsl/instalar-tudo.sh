#!/usr/bin/env bash
# Monta o setup inteiro no Ubuntu do WSL de uma vez (fase 0 do Núcleo AMtech). Seguro para rodar de novo.
#   bash scripts/wsl/instalar-tudo.sh --simular   # mostra o que faria
#   bash scripts/wsl/instalar-tudo.sh             # instala e liga as rotinas
# Ordem: bootstrap (base, just, mise) → extras (CLIs, uv, Podman) → dotfiles (chezmoi) → padrão em todo repositório
#        → rotinas agendadas → banco local do núcleo → conferência. Pede o sudo uma vez no começo.
set -uo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SIMULAR=""; [[ "${1:-}" == "--simular" ]] && SIMULAR="--simular"
etapa() { echo; echo "================ $1"; }
falhas=0
rodar() { "$@" || { echo "!! falhou: $*"; falhas=$((falhas + 1)); }; }

etapa "1/7 Base, just e mise"
rodar bash "$RAIZ/scripts/wsl/bootstrap.sh" $SIMULAR
export PATH="$HOME/.local/bin:$PATH"
command -v mise >/dev/null 2>&1 && eval "$(mise env -s bash 2>/dev/null)"

etapa "2/7 Ferramentas complementares"
rodar bash "$RAIZ/scripts/wsl/extras.sh" $SIMULAR

etapa "3/7 Dotfiles pelo chezmoi"
if [[ -n "$SIMULAR" ]]; then echo "(simulação) chezmoi init + copiar infra/dotfiles + chezmoi apply"
elif command -v chezmoi >/dev/null 2>&1; then
  FONTE="$(chezmoi source-path 2>/dev/null || echo "$HOME/.local/share/chezmoi")"
  mkdir -p "$FONTE" && cp -rn "$RAIZ/infra/dotfiles/." "$FONTE/" && chezmoi init && rodar chezmoi apply --force
else echo "chezmoi ausente: veja a etapa 2"; falhas=$((falhas + 1)); fi

etapa "4/7 Padrão em todo repositório de ~/dev"
if [[ -n "$SIMULAR" ]]; then echo "(simulação) padronizar-repo.sh --todos"; else rodar bash "$RAIZ/scripts/wsl/padronizar-repo.sh" --todos; fi

etapa "5/7 Rotinas agendadas"
if [[ -n "$SIMULAR" ]]; then bash "$RAIZ/scripts/wsl/agendar.sh"; else rodar bash "$RAIZ/scripts/wsl/agendar.sh" --aplicar; fi

etapa "6/7 Banco local do Núcleo"
if [[ -n "$SIMULAR" ]]; then echo "(simulação) python3 tools/nucleo/nucleo.py iniciar"; else rodar python3 "$RAIZ/tools/nucleo/nucleo.py" iniciar; fi

etapa "7/7 Conferência"
bash "$RAIZ/scripts/wsl/verificar.sh" || true

echo
if [[ -n "$SIMULAR" ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $falhas -gt 0 ]]; then echo "$falhas etapa(s) com erro: veja acima e rode de novo (o que já foi feito é pulado)."; exit 1
else echo "Setup montado. Abra um terminal novo e rode: just"; fi
