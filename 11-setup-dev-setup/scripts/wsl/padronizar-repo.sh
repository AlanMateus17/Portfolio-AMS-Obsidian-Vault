#!/usr/bin/env bash
# Aplica o padrão de elite num repositório: copia só o que falta do modelo e liga os hooks.
#   bash scripts/wsl/padronizar-repo.sh ~/dev/aulas          # um repositório
#   bash scripts/wsl/padronizar-repo.sh --todos              # todos em ~/dev
# Nunca sobrescreve arquivo existente. Depois: revise, commit e push.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODELO="$RAIZ/infra/templates/repo-padrao"
aplicar() {
  local repo="$1" n=0
  [[ -d "$repo/.git" ]] || { echo "pulando $repo (não é repositório git)"; return 0; }
  # O próprio dev-setup não recebe o modelo: ele já tem o padrão dele, e o docs/adr/0001-modelo.md
  # colidiria com o ADR 0001 de verdade (quebrava o just check depois do just instalar).
  [[ "$(cd "$repo" && pwd -P)" == "$(cd "$RAIZ" && pwd -P)" ]] && { echo "pulando $repo (é o próprio dev-setup)"; return 0; }
  # O vault do Obsidian (~/dev/notas) não é repositório de código: o modelo poluía a raiz dele
  # (.aiderignore, .claude/, .github/, docs/, scripts/...). Reconhecido pela pasta ou pelos arquivos-guia.
  if [[ "$(cd "$repo" && pwd -P)" == "$(cd "$HOME/dev/notas" 2>/dev/null && pwd -P)" ]] || [[ -f "$repo/PLANO-UNICO-AMtech.md" || -f "$repo/CARTAO-voce-esta-aqui.md" ]]; then
    echo "pulando $repo (é o vault do Obsidian, não um repositório de código)"; return 0
  fi
  while IFS= read -r f; do
    rel="${f#"$MODELO"/}"; [[ "$rel" == "LEIA.md" ]] && continue
    if [[ ! -e "$repo/$rel" ]]; then mkdir -p "$(dirname "$repo/$rel")"; cp "$f" "$repo/$rel"; n=$((n + 1)); echo "  + $rel"; fi
  done < <(find "$MODELO" -type f)
  if command -v pre-commit >/dev/null 2>&1; then
    (cd "$repo" && pre-commit install >/dev/null && pre-commit install --hook-type commit-msg >/dev/null && echo "  hooks ligados")
  else
    echo "  instale o pre-commit: pip install --user pre-commit (ou pipx install pre-commit)"
  fi
  echo "$repo: $n arquivo(s) novos"
}
if [[ "${1:-}" == "--todos" ]]; then
  while IFS= read -r g; do aplicar "$(dirname "$g")"; done < <(find "$HOME/dev" -maxdepth 2 -name .git -type d)
elif [[ -n "${1:-}" ]]; then aplicar "$1"
else sed -n '2,5p' "$0"; exit 1; fi
