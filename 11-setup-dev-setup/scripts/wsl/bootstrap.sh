#!/usr/bin/env bash
# Prepara o Ubuntu (24.04 ou mais novo) do WSL2, ou o AMtech OS nativo (os/instalar.sh chama este script), para o setup: ferramentas, linguagens, segurança, agentes e pastas.
# Seguro para rodar várias vezes: o que já está pronto é pulado.
#
#   bash scripts/wsl/bootstrap.sh --simular                      # mostra o que faria, sem mudar nada
#   bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email voce@exemplo.com
#
# Opções:
#   --simular        não instala nada, só relata
#   --sem-tex        pula o TeX Live (cerca de 1 GB)
#   --com-whisper    instala a transcrição local (whisper-ctranslate2) para o pipeline de conteúdo
#   --nome / --email identidade do Git (obrigatórios na primeira vez)
set -euo pipefail

SIMULAR=0; COM_TEX=1; COM_WHISPER=0; NOME=""; EMAIL=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --simular) SIMULAR=1 ;;
    --sem-tex) COM_TEX=0 ;;
    --com-whisper) COM_WHISPER=1 ;;
    --nome) NOME="${2:-}"; shift ;;
    --email) EMAIL="${2:-}"; shift ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done

SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
# Instala sem perguntar e mantém arquivos de configuração que você já editou
APT="DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
LOG="${HOME}/bootstrap-$(date +%Y%m%d-%H%M).log"
ERROS=0
export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"
mkdir -p "$HOME/.local/bin"
versao_mais_recente() {  # maior tag x.y.z de um repositório do GitHub (via git, sem limite de API)
  git ls-remote --tags --refs "https://github.com/$1.git" | sed 's#.*/v\{0,1\}##' | grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' | sort -V | tail -1
}

linha() { printf '%-11s %-30s %-13s %s\n' "$1" "$2" "$3" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {  # rodar <etapa> <item> <comando...>
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "INSTALARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "INSTALADO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}

echo "Registro em: $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

# ------------------------------------------------------------------ 0. ambiente
NO_WSL=0; grep -qi microsoft /proc/version 2>/dev/null && NO_WSL=1
if [[ $NO_WSL -eq 1 ]]; then linha "ambiente" "WSL" "OK"; else linha "ambiente" "Linux nativo" "OK" "AMtech OS ou Ubuntu em VM"; fi
if [[ "$(ps -p 1 -o comm= 2>/dev/null)" == "systemd" ]]; then
  linha "ambiente" "systemd" "OK"
elif [[ $NO_WSL -eq 0 ]]; then
  linha "ambiente" "systemd" "AVISO" "não é o PID 1 (container?); serviços e timers não vão subir"
elif [[ $SIMULAR -eq 1 ]]; then
  linha "ambiente" "systemd" "CRIARIA" "/etc/wsl.conf com systemd=true"
else
  printf '[boot]\nsystemd=true\n' | $SUDO tee /etc/wsl.conf >/dev/null
  linha "ambiente" "systemd" "CONFIGURADO" "no PowerShell: wsl --shutdown, depois abra o Ubuntu de novo"
fi

# ------------------------------------------------------------------ 1. pacotes do sistema
PACOTES=(build-essential curl wget git unzip zip zstd jq ripgrep fzf tmux zsh ca-certificates gnupg
         bubblewrap restic pandoc sqlite3 postgresql-client python3-venv shellcheck openssh-client
         nmap bind9-dnsutils)
FALTAM=()
for p in "${PACOTES[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || FALTAM+=("$p"); done
if [[ ${#FALTAM[@]} -eq 0 ]]; then linha "apt" "pacotes base (${#PACOTES[@]})" "JA TEM"
else rodar "apt" "pacotes base (${#FALTAM[@]} faltando)" bash -c "$SUDO apt-get update -y && $SUDO env $APT install ${FALTAM[*]}"; fi

# ------------------------------------------------------------------ 2. GitHub CLI
if tem gh; then linha "github" "gh" "JA TEM" "$(gh --version | head -1)"
else rodar "github" "gh" bash -c "
  $SUDO install -d -m 0755 /etc/apt/keyrings &&
  curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | $SUDO tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null &&
  echo \"deb [arch=\$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main\" | $SUDO tee /etc/apt/sources.list.d/github-cli.list >/dev/null &&
  $SUDO apt-get update -y && $SUDO env $APT install gh"; fi

# ------------------------------------------------------------------ 3. linguagens
if tem dotnet && dotnet --list-sdks 2>/dev/null | grep -q '^10\.'; then linha "linguagem" ".NET 10 SDK" "JA TEM"
else rodar "linguagem" ".NET 10 SDK" bash -c "$SUDO apt-get update -y && $SUDO env $APT install dotnet-sdk-10.0"; fi

# Runtimes pelo mise (ADR 0008): Node, Go e Rust num gerenciador só; o fnm fica só como reserva se já existir.
if tem mise; then linha "linguagem" "mise" "JA TEM" "$(mise --version 2>/dev/null | cut -d' ' -f1)"
else rodar "linguagem" "mise" bash -c 'curl -fsSL https://mise.run | MISE_INSTALL_PATH="$HOME/.local/bin/mise" sh'; fi
tem mise && eval "$(mise env -s bash 2>/dev/null)"
if tem mise && mise where node >/dev/null 2>&1; then linha "linguagem" "Node LTS (mise)" "JA TEM" "$(mise exec -- node -v 2>/dev/null)"
elif tem mise || [[ $SIMULAR -eq 1 ]]; then rodar "linguagem" "Node LTS (mise)" mise use -g --yes node@lts
else linha "linguagem" "Node LTS (mise)" "FALTA" "o mise não instalou; veja $LOG"; fi
# A linha no .bashrc põe ~/.local/bin no PATH antes: no shell de login do WSL o .bashrc roda antes do .profile acrescentar a pasta.
MISE_LINHA='export PATH="$HOME/.local/bin:$PATH"; if command -v mise >/dev/null; then eval "$(mise activate bash)"; elif command -v fnm >/dev/null; then eval "$(fnm env --use-on-cd --shell bash)"; fi'
if [[ $SIMULAR -eq 0 ]] && ! grep -qxF "$MISE_LINHA" "$HOME/.bashrc" 2>/dev/null; then
  grep -v 'fnm env' "$HOME/.bashrc" > "$HOME/.bashrc.tmp" 2>/dev/null; cat "$HOME/.bashrc.tmp" > "$HOME/.bashrc"; rm -f "$HOME/.bashrc.tmp"
  echo "$MISE_LINHA" >> "$HOME/.bashrc"
fi

if tem uv; then linha "linguagem" "uv (Python)" "JA TEM" "$(uv --version)"
else rodar "linguagem" "uv (Python)" bash -c "curl -LsSf https://astral.sh/uv/install.sh | sh"; fi

# ------------------------------------------------------------------ 4. segurança no código
if tem gitleaks; then linha "seguranca" "gitleaks" "JA TEM" "$(gitleaks version 2>/dev/null)"
else
  V="$( [[ $SIMULAR -eq 1 ]] || versao_mais_recente gitleaks/gitleaks )"
  rodar "seguranca" "gitleaks ${V}" bash -c "curl -fsSL https://github.com/gitleaks/gitleaks/releases/download/v${V}/gitleaks_${V}_linux_x64.tar.gz | tar -xz -C \"\$HOME/.local/bin\" gitleaks"
fi
if tem trivy; then linha "seguranca" "trivy" "JA TEM"
else
  V="$( [[ $SIMULAR -eq 1 ]] || versao_mais_recente aquasecurity/trivy )"
  rodar "seguranca" "trivy ${V}" bash -c "curl -fsSL -o /tmp/trivy.deb https://github.com/aquasecurity/trivy/releases/download/v${V}/trivy_${V}_Linux-64bit.deb && $SUDO dpkg -i /tmp/trivy.deb && rm -f /tmp/trivy.deb"
fi

# ------------------------------------------------------------------ 4b. terminal moderno e porta única (just)
# Binários únicos, sem runtime: just (receitas do justfile), zoxide, eza, fd, btop, hyperfine, tio (serial da bancada) e tcpdump.
TERMINAL=(just zoxide eza fd-find btop hyperfine tio tcpdump)
FALTAM_T=()
for p in "${TERMINAL[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || FALTAM_T+=("$p"); done
if [[ ${#FALTAM_T[@]} -eq 0 ]]; then linha "terminal" "just, zoxide, eza, fd, btop…" "JA TEM"
else rodar "terminal" "terminal moderno (${#FALTAM_T[@]} faltando)" bash -c "$SUDO apt-get update -y && $SUDO env $APT install ${FALTAM_T[*]}"; fi
for ferramenta in lazygit lazydocker; do
  if tem "$ferramenta"; then linha "terminal" "$ferramenta" "JA TEM"; continue; fi
  V="$( [[ $SIMULAR -eq 1 ]] || versao_mais_recente "jesseduffield/$ferramenta" )"
  rodar "terminal" "$ferramenta ${V}" bash -c "curl -fsSL https://github.com/jesseduffield/$ferramenta/releases/download/v${V}/${ferramenta}_${V}_Linux_x86_64.tar.gz | tar -xz -C \"\$HOME/.local/bin\" $ferramenta"
done
if tem starship; then linha "terminal" "Starship" "JA TEM"
else rodar "terminal" "Starship" bash -c 'curl -fsSL https://starship.rs/install.sh | sh -s -- -y -b "$HOME/.local/bin"'; fi
# Uma linha só no .bashrc liga o prompt, o cd inteligente e o nome curto do fd (no Ubuntu o binário chama fdfind)
TERM_LINHA='command -v starship >/dev/null && eval "$(starship init bash)"; command -v zoxide >/dev/null && eval "$(zoxide init bash)"; command -v fdfind >/dev/null && alias fd=fdfind'
if [[ $SIMULAR -eq 0 ]] && ! grep -qxF "$TERM_LINHA" "$HOME/.bashrc" 2>/dev/null; then echo "$TERM_LINHA" >> "$HOME/.bashrc"; fi

# ------------------------------------------------------------------ 5. agentes de IA
if tem claude; then linha "agentes" "Claude Code" "JA TEM" "$(claude --version 2>/dev/null)"
else rodar "agentes" "Claude Code" bash -c "curl -fsSL https://claude.ai/install.sh | bash"; fi
if tem ai-jail; then linha "agentes" "ai-jail" "JA TEM"
else rodar "agentes" "ai-jail" bash -c 'd=$(mktemp -d) && curl -fsSL https://github.com/akitaonrails/ai-jail/releases/latest/download/ai-jail-linux-x86_64.tar.gz | tar -xz -C "$d" && mkdir -p "$HOME/.local/bin" && install -m755 "$d/ai-jail" "$HOME/.local/bin/ai-jail" && rm -rf "$d"'; fi

# ------------------------------------------------------------------ 6. livro e conteúdo
if [[ $COM_TEX -eq 1 ]]; then
  if tem latexmk; then linha "livro" "TeX Live" "JA TEM"
  else rodar "livro" "TeX Live (latex-extra, pt-BR)" bash -c "$SUDO env $APT install texlive-latex-extra texlive-lang-portuguese texlive-pictures latexmk"; fi
fi
if [[ $COM_WHISPER -eq 1 ]]; then
  if tem whisper-ctranslate2; then linha "conteudo" "Whisper local" "JA TEM"
  else rodar "conteudo" "Whisper local" bash -c "uv tool install whisper-ctranslate2"; fi
fi

# ------------------------------------------------------------------ 7. Git, SSH e commits assinados
if [[ -n "$NOME" ]]; then [[ $SIMULAR -eq 1 ]] || git config --global user.name "$NOME"; fi
if [[ -n "$EMAIL" ]]; then [[ $SIMULAR -eq 1 ]] || git config --global user.email "$EMAIL"; fi
if [[ $SIMULAR -eq 1 && -n "$NOME" && -n "$EMAIL" ]]; then
  linha "git" "identidade" "CONFIGURARIA" "$NOME <$EMAIL>"
elif [[ -z "$(git config --global user.name || true)" || -z "$(git config --global user.email || true)" ]]; then
  linha "git" "identidade" "FALTA" "rode de novo com --nome e --email"
else
  linha "git" "identidade" "OK" "$(git config --global user.name) <$(git config --global user.email)>"
fi
CHAVE="$HOME/.ssh/id_ed25519"
if [[ -f "$CHAVE" ]]; then linha "git" "chave SSH" "JA TEM" "$CHAVE.pub"
elif [[ $SIMULAR -eq 1 ]]; then linha "git" "chave SSH" "CRIARIA" "ed25519 com senha"
else
  mkdir -p "$HOME/.ssh" && chmod 700 "$HOME/.ssh"
  echo "Crie uma senha para a chave SSH (guarde no KeePassXC):"
  ssh-keygen -t ed25519 -C "${EMAIL:-$(git config --global user.email)}" -f "$CHAVE"
  linha "git" "chave SSH" "CRIADA" "adicione no GitHub: gh ssh-key add $CHAVE.pub --type authentication e --type signing"
fi
if [[ $SIMULAR -eq 0 ]]; then
  git config --global init.defaultBranch main
  git config --global core.autocrlf input
  git config --global gpg.format ssh
  git config --global user.signingkey "$CHAVE.pub"
  git config --global commit.gpgsign true
  git config --global tag.gpgsign true
fi
linha "git" "commits assinados" "$([[ $SIMULAR -eq 1 ]] && echo CONFIGURARIA || echo OK)" "gpg.format=ssh"

# ------------------------------------------------------------------ 8. pastas do setup
PASTAS=("$HOME/dev" "$HOME/AMtech/entrada/aulas" "$HOME/AMtech/entrada/capitulos" "$HOME/AMtech/entrada/reparos"
        "$HOME/AMtech/entrada/decisoes" "$HOME/AMtech/entrada/ideias" "$HOME/AMtech/fila" "$HOME/AMtech/processados"
        "$HOME/AMtech/publicado")
FALTA_P=0; for d in "${PASTAS[@]}"; do [[ -d "$d" ]] || FALTA_P=$((FALTA_P + 1)); done
if [[ $FALTA_P -eq 0 ]]; then linha "pastas" "pastas dev e AMtech" "JA TEM"
elif [[ $SIMULAR -eq 1 ]]; then linha "pastas" "pastas dev e AMtech" "CRIARIA" "$FALTA_P pasta(s)"
else mkdir -p "${PASTAS[@]}"; linha "pastas" "pastas dev e AMtech" "CRIADO" "$FALTA_P pasta(s)"; fi

# ------------------------------------------------------------------ 9. Docker (no WSL vem do Docker Desktop; no Linux nativo, do os/instalar.sh)
if tem docker && docker info >/dev/null 2>&1; then linha "docker" "Docker" "OK" "$(docker version --format '{{.Server.Version}}' 2>/dev/null)"
elif [[ $NO_WSL -eq 1 ]]; then linha "docker" "Docker no WSL" "MANUAL" "Docker Desktop > Settings > Resources > WSL integration > ${WSL_DISTRO_NAME:-Ubuntu}"
else linha "docker" "Docker nativo" "MANUAL" "bash os/instalar.sh (perfil dev) instala o Docker; depois saia e entre na sessão"; fi

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $ERROS -gt 0 ]]; then echo "$ERROS erro(s). Veja $LOG"; exit 1
else echo "Pronto. Abra um terminal novo e rode: bash scripts/wsl/verificar.sh"; fi
