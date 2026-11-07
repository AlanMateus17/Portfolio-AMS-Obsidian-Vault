#!/usr/bin/env bash
# Laboratório de alvo isolado (containers): sobe o software que você quer estudar numa rede sem internet,
# junto de um atacante com as ferramentas de pentest, e prova que o isolamento funciona.
#
#   bash scripts/wsl/lab-alvo.sh subir                         # alvo padrão: Juice Shop (porta 3000)
#   ALVO_IMAGEM=minha-api:dev ALVO_PORTA=8080 bash scripts/wsl/lab-alvo.sh subir
#   bash scripts/wsl/lab-alvo.sh verificar                     # alcança o alvo? sai para a internet? (não pode)
#   bash scripts/wsl/lab-alvo.sh entrar                        # terminal do atacante
#   bash scripts/wsl/lab-alvo.sh limpar                        # apaga os containers e o que o ataque mudou
#
# Regra: só software seu, código aberto, apps feitos para isso ou de cliente com termo assinado.
# Programas de desktop e binários de Windows vão para o lab de VMs: scripts/windows/lab-alvo.ps1.
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
COMPOSE=(docker compose -f "$RAIZ/infra/lab-alvo/compose.yaml")
PORTA="${ALVO_PORTA:-3000}"
ACAO="${1:-}"

uso() { sed -n '2,12p' "$0"; }

verificar() {
  local falhas=0
  if "${COMPOSE[@]}" exec -T atacante curl -s -o /dev/null -m 10 "http://alvo:$PORTA/"; then
    echo "OK     o atacante alcança o alvo em http://alvo:$PORTA"
  else
    echo "ERRO   o atacante não alcança http://alvo:$PORTA (o alvo subiu? a porta é essa?)"; falhas=$((falhas + 1))
  fi
  if "${COMPOSE[@]}" exec -T atacante curl -s -o /dev/null -m 8 https://example.com; then
    echo "ERRO   o atacante saiu para a internet: o laboratório NÃO está isolado. Rode 'limpar' e confira o compose."
    falhas=$((falhas + 1))
  else
    echo "OK     o atacante não sai para a internet"
  fi
  if "${COMPOSE[@]}" exec -T alvo sh -c 'command -v wget >/dev/null && wget -q -T 8 -O /dev/null https://example.com' 2>/dev/null; then
    echo "ERRO   o alvo saiu para a internet: o laboratório NÃO está isolado."; falhas=$((falhas + 1))
  else
    echo "OK     o alvo não sai para a internet"
  fi
  if docker ps --filter "label=com.docker.compose.project=lab-alvo" --format '{{.Ports}}' | grep -q '0.0.0.0\|::'; then
    echo "ERRO   há porta publicada na rede de casa; o alvo não deve ter 'ports' no compose."; falhas=$((falhas + 1))
  else
    echo "OK     nenhuma porta publicada fora do laboratório"
  fi
  return "$falhas"
}

case "$ACAO" in
  subir)
    command -v docker >/dev/null || { echo "Docker não encontrado: rode o passo do Docker no WSL antes." >&2; exit 1; }
    "${COMPOSE[@]}" pull --ignore-pull-failures alvo
    "${COMPOSE[@]}" up -d --build
    echo "Laboratório no ar. Aguarde o alvo iniciar e rode: bash scripts/wsl/lab-alvo.sh verificar"
    ;;
  verificar) verificar ;;
  entrar) "${COMPOSE[@]}" exec atacante bash ;;
  limpar) "${COMPOSE[@]}" down -v --remove-orphans; echo "Laboratório apagado." ;;
  -h|--help|"") uso ;;
  *) echo "Ação desconhecida: $ACAO" >&2; uso; exit 64 ;;
esac
