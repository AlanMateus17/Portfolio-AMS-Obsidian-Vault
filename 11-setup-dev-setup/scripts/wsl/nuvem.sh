#!/usr/bin/env bash
# Ferramentas de nuvem e deploy no Ubuntu do WSL2. Seguro para rodar várias vezes.
#   bash scripts/wsl/nuvem.sh --simular   # mostra o que faria
#   bash scripts/wsl/nuvem.sh             # instala
# Instala: Azure CLI (uv), Terraform (repositório oficial da HashiCorp),
#          Vercel CLI e Wrangler da Cloudflare (npm global do Node do mise).
# O login em cada uma é seu: az login, vercel login, wrangler login.
set -euo pipefail

SIMULAR=0
for a in "$@"; do case "$a" in --simular) SIMULAR=1 ;; -h|--help) sed -n '2,7p' "$0"; exit 0 ;; *) echo "Opção desconhecida: $a" >&2; exit 64 ;; esac; done
SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
APT="DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
LOG="${HOME}/nuvem-$(date +%Y%m%d-%H%M).log"
ERROS=0
export PATH="$HOME/.local/bin:$PATH"
if command -v mise >/dev/null 2>&1; then eval "$(mise env -s bash 2>/dev/null)"; elif command -v fnm >/dev/null 2>&1; then eval "$(fnm env --shell bash 2>/dev/null)"; fi

linha() { printf '%-9s %-24s %-11s %s\n' "$1" "$2" "$3" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "INSTALARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "INSTALADO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}

echo "Registro em: $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

# Azure CLI: pacote oficial do PyPI, isolado pelo uv
if tem az && az version >/dev/null 2>&1; then linha azure "Azure CLI" "JA TEM" "$(az version --query '"azure-cli"' -o tsv 2>/dev/null)"
elif ! tem uv; then linha azure "Azure CLI" "PULADO" "falta o uv: rode antes o bootstrap.sh"; ERROS=$((ERROS + 1))
else
  # o "az" do pacote chama o python do sistema; o atalho abaixo usa o python do ambiente do uv.
  # --prerelease=allow: o próprio azure-cli depende de versões beta (azure-batch); sem isso o uv cai numa versão antiga.
  rodar azure "Azure CLI" bash -c 'uv tool install --force --python 3.12 --prerelease=allow "azure-cli>=2.70" && printf "#!/usr/bin/env bash\nexec \"%s/azure-cli/bin/python\" -m azure.cli \"\$@\"\n" "$(uv tool dir)" > "$HOME/.local/bin/az" && chmod +x "$HOME/.local/bin/az" && "$HOME/.local/bin/az" version >/dev/null'
fi

# Terraform: repositório apt da HashiCorp
if tem terraform; then linha iac Terraform "JA TEM" "$(terraform version | head -1)"
else rodar iac Terraform bash -c "
  curl -fsSL https://apt.releases.hashicorp.com/gpg | $SUDO gpg --dearmor --yes -o /usr/share/keyrings/hashicorp.gpg &&
  cod=\$(. /etc/os-release && echo \"\$VERSION_CODENAME\") && { curl -fsI https://apt.releases.hashicorp.com/dists/\$cod/Release >/dev/null || cod=noble; } &&
  echo \"deb [signed-by=/usr/share/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com \$cod main\" | $SUDO tee /etc/apt/sources.list.d/hashicorp.list >/dev/null &&
  $SUDO apt-get update -y && $SUDO env $APT install terraform"; fi

# Vercel CLI e Wrangler: precisam do Node 22+ do bootstrap
for par in "vercel:vercel" "wrangler:wrangler"; do
  bin="${par%%:*}"; pkg="${par##*:}"
  if tem "$bin"; then linha deploy "$bin" "JA TEM" "$("$bin" --version 2>/dev/null | head -1 | cut -c1-30)"
  elif ! tem npm; then linha deploy "$bin" "PULADO" "falta o Node: rode antes o bootstrap.sh"; ERROS=$((ERROS + 1))
  else rodar deploy "$bin" npm install -g "$pkg"; fi
done

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $ERROS -gt 0 ]]; then echo "$ERROS item(ns) com problema. Veja $LOG"; exit 1
else echo "Pronto. Agora: az login, vercel login, wrangler login (cada um abre o navegador)."; fi
