#!/usr/bin/env bash
# Teste de restauração do backup (restic): backup que nunca foi restaurado não é backup.
#   bash scripts/wsl/teste-restauracao.sh
# Usa RESTIC_REPOSITORY e pede a senha do repositório (digite à mão ou use segredos.sh).
# Restaura o último snapshot numa pasta temporária, confere e apaga a pasta temporária.
set -euo pipefail
command -v restic >/dev/null 2>&1 || { echo "Instale: sudo apt install restic"; exit 1; }
[[ -n "${RESTIC_REPOSITORY:-}" ]] || { echo "Defina RESTIC_REPOSITORY (o repositório do backup do roteiro)."; exit 1; }
tmp="$(mktemp -d)"; trap 'rm -rf "$tmp"' EXIT
echo "== Integridade do repositório (5% dos dados)"
restic check --read-data-subset=5%
echo "== Restaurando o último snapshot em $tmp"
restic restore latest --target "$tmp" >/dev/null
n="$(find "$tmp" -type f | wc -l)"; tam="$(du -sh "$tmp" | cut -f1)"
echo "Restaurados $n arquivos ($tam)."
[[ "$n" -gt 0 ]] && echo "TESTE OK: o backup restaura." || { echo "FALHOU: nada restaurado."; exit 1; }
