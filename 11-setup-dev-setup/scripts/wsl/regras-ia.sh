#!/usr/bin/env bash
# Copia as regras únicas das IAs para um repositório: CLAUDE.md, AGENTS.md e GEMINI.md iguais.
#   bash scripts/wsl/regras-ia.sh ~/dev/aulas
# Se o repositório já tiver CLAUDE.md próprio, as regras entram no topo de AGENTS.md e GEMINI.md e o CLAUDE.md fica como está.
set -euo pipefail
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
FONTE="$RAIZ/infra/templates/regras-ia/regras-ia.md"
REPO="${1:?informe a pasta do repositório}"
for alvo in CLAUDE.md AGENTS.md GEMINI.md; do
  if [[ -e "$REPO/$alvo" ]]; then echo "mantido: $alvo (já existe)"; else cp "$FONTE" "$REPO/$alvo"; echo "criado: $alvo"; fi
done
