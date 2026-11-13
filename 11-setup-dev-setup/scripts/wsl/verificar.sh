#!/usr/bin/env bash
# shellcheck disable=SC2088  # "~/" nos rótulos é só texto exibido
# Confere se o lado Linux (WSL) do setup está pronto. SOMENTE LEITURA.
#   bash scripts/wsl/verificar.sh              # ferramentas, Git, pastas
#   bash scripts/wsl/verificar.sh --servicos   # também os serviços da automação (n8n, métricas, Grafana...)
#   bash scripts/wsl/verificar.sh --json       # saída para máquinas
# Sai com código 1 se faltar algo obrigatório.
set -uo pipefail

SERVICOS=0; JSON=0
for a in "$@"; do case "$a" in --servicos) SERVICOS=1 ;; --json) JSON=1 ;; -h|--help) sed -n '2,6p' "$0"; exit 0 ;; esac; done
export PATH="$HOME/.local/bin:$PATH"
if command -v mise >/dev/null 2>&1; then eval "$(mise env -s bash 2>/dev/null)"; elif command -v fnm >/dev/null 2>&1; then eval "$(fnm env --shell bash 2>/dev/null)"; fi

RES=(); FALTAS=0; OKS=0
r() {  # r <area> <item> <OK|FALTA|AVISO> <detalhe> [obrigatorio=1]
  local obr="${5:-1}"
  RES+=("$1|$2|$3|$4|$obr")
  [[ "$3" == "OK" ]] && OKS=$((OKS + 1))
  [[ "$3" == "FALTA" && "$obr" == "1" ]] && FALTAS=$((FALTAS + 1))
  return 0
}
cmd() {  # cmd <item> <comando> <como instalar> [obrigatorio]
  local item="$1" c="$2" dica="$3" obr="${4:-1}"
  if command -v "$c" >/dev/null 2>&1; then
    local v; v="$("$c" --version 2>/dev/null | head -1 | cut -c1-48)"
    r ferramenta "$item" OK "${v:-instalado}" "$obr"
  else r ferramenta "$item" "$([[ $obr == 1 ]] && echo FALTA || echo AVISO)" "$dica" "$obr"; fi
}

# Ambiente
if grep -qi microsoft /proc/version 2>/dev/null; then r ambiente WSL OK "$(uname -r | cut -c1-40)"; elif [[ -r /etc/amtech-release ]]; then r ambiente "AMtech OS" OK "$(uname -r | cut -c1-40)"; else r ambiente WSL AVISO "não parece WSL" 0; fi
[[ "$(ps -p 1 -o comm= 2>/dev/null)" == "systemd" ]] && r ambiente systemd OK "" || r ambiente systemd FALTA "bootstrap.sh configura; depois wsl --shutdown"

# Ferramentas
cmd git git "sudo apt install git"
cmd "GitHub CLI" gh "bootstrap.sh"
if command -v dotnet >/dev/null 2>&1 && dotnet --list-sdks 2>/dev/null | grep -q '^10\.'; then r ferramenta ".NET 10 SDK" OK "$(dotnet --list-sdks | grep '^10\.' | tail -1 | cut -d' ' -f1)"
else r ferramenta ".NET 10 SDK" FALTA "sudo apt install dotnet-sdk-10.0"; fi
if command -v node >/dev/null 2>&1 && [[ "$(node -v | tr -d v | cut -d. -f1)" -ge 22 ]]; then r ferramenta "Node 22+" OK "$(node -v)"
else r ferramenta "Node 22+" FALTA "mise use -g node@lts"; fi
cmd "uv (Python)" uv "bootstrap.sh"
cmd gitleaks gitleaks "bootstrap.sh"
cmd trivy trivy "bootstrap.sh"
cmd "Claude Code" claude "curl -fsSL https://claude.ai/install.sh | bash"
cmd ai-jail ai-jail "bootstrap.sh"
cmd "bubblewrap (sandbox)" bwrap "sudo apt install bubblewrap"
cmd restic restic "sudo apt install restic"
cmd pandoc pandoc "sudo apt install pandoc"
cmd nmap nmap "sudo apt install nmap" 0
cmd "dig (DNS)" dig "sudo apt install bind9-dnsutils" 0
cmd "Azure CLI" az "bash scripts/wsl/nuvem.sh" 0
cmd Terraform terraform "bash scripts/wsl/nuvem.sh" 0
cmd "Vercel CLI" vercel "bash scripts/wsl/nuvem.sh" 0
cmd "Wrangler (Cloudflare)" wrangler "bash scripts/wsl/nuvem.sh" 0
if command -v nvidia-smi >/dev/null 2>&1 && nvidia-smi >/dev/null 2>&1; then r ferramenta "GPU no WSL" OK "$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null | head -1)" 0
else r ferramenta "GPU no WSL" AVISO "atualize o driver NVIDIA no Windows" 0; fi
[[ -f "$HOME/dev/lab-ia/pyproject.toml" ]] && r ferramenta "Laboratório de dados e IA" OK "~/dev/lab-ia" 0 || r ferramenta "Laboratório de dados e IA" AVISO "bash scripts/wsl/lab-ia.sh" 0
cmd "TeX Live" latexmk "bootstrap.sh (sem --sem-tex)" 0
cmd "Whisper local" whisper-ctranslate2 "bootstrap.sh --com-whisper" 0
if command -v docker >/dev/null 2>&1 && docker info >/dev/null 2>&1; then r ferramenta Docker OK "$(docker version --format '{{.Server.Version}}' 2>/dev/null)"
else r ferramenta Docker FALTA "Docker Desktop > Settings > Resources > WSL integration"; fi

# Git e GitHub
n="$(git config --global user.name 2>/dev/null)"; e="$(git config --global user.email 2>/dev/null)"
[[ -n "$n" && -n "$e" ]] && r git identidade OK "$n <$e>" || r git identidade FALTA "bootstrap.sh --nome --email"
[[ -f "$HOME/.ssh/id_ed25519" ]] && r git "chave SSH" OK "~/.ssh/id_ed25519" || r git "chave SSH" FALTA "bootstrap.sh cria"
[[ "$(git config --global commit.gpgsign 2>/dev/null)" == "true" && "$(git config --global gpg.format 2>/dev/null)" == "ssh" ]] \
  && r git "commits assinados" OK "ssh" || r git "commits assinados" FALTA "bootstrap.sh configura"
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then r git "login no GitHub" OK "gh auth status"
else r git "login no GitHub" FALTA "gh auth login"; fi

# Pastas
for d in dev AMtech/entrada AMtech/fila AMtech/processados; do
  [[ -d "$HOME/$d" ]] && r pastas "~/$d" OK "" || r pastas "~/$d" FALTA "bootstrap.sh cria"
done

# Serviços da automação
porta() { curl -fsS -o /dev/null --max-time 3 "$1" >/dev/null 2>&1; }
if [[ $SERVICOS -eq 1 ]]; then
  porta http://localhost:5678/healthz && r servico n8n OK ":5678" || r servico n8n FALTA "cd infra/automacao && docker compose up -d"
  if command -v pg_isready >/dev/null 2>&1 && pg_isready -h localhost -p 5433 -q; then r servico "PostgreSQL de métricas" OK ":5433"
  else r servico "PostgreSQL de métricas" FALTA "docker compose up -d (infra/automacao)"; fi
  porta http://localhost:3001/api/health && r servico Grafana OK ":3001" || r servico Grafana FALTA "docker compose up -d (infra/automacao)"
  porta http://localhost:3002 && r servico "Uptime Kuma" OK ":3002" || r servico "Uptime Kuma" FALTA "docker compose up -d (infra/automacao)"
  porta http://localhost:4007 && r servico Postiz OK ":4007" 0 || r servico Postiz AVISO "opcional: infra/postiz/README.md" 0
  if [[ -f "$HOME/.config/amtech/conteudo.env" ]]; then r conteudo "configuração do pipeline" OK "~/.config/amtech/conteudo.env"
  else r conteudo "configuração do pipeline" FALTA "tools/conteudo/README.md"; fi
  if systemctl --user is-active --quiet amtech-conteudo.timer 2>/dev/null; then r conteudo "timer do pipeline" OK "a cada 15 min"
  else r conteudo "timer do pipeline" AVISO "scripts/wsl/ativar-pipeline.sh" 0; fi
fi

# Saída
if [[ $JSON -eq 1 ]]; then
  printf '['; sep=""
  for x in "${RES[@]}"; do IFS='|' read -r a i s d o <<<"$x"
    printf '%s{"area":"%s","item":"%s","status":"%s","detalhe":"%s","obrigatorio":%s}' "$sep" "$a" "$i" "$s" "${d//\"/\'}" "$([[ $o == 1 ]] && echo true || echo false)"; sep=","; done
  printf ']\n'
else
  for x in "${RES[@]}"; do IFS='|' read -r a i s d o <<<"$x"; printf '%-11s %-28s %-6s %s\n' "$a" "$i" "$s" "$d"; done
  echo
  if [[ $FALTAS -eq 0 ]]; then echo "WSL pronto: $OKS itens OK."; else echo "Faltam $FALTAS item(ns) obrigatório(s)."; fi
fi
[[ $FALTAS -eq 0 ]]
