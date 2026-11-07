#!/usr/bin/env bash
# Ferramentas de engenharia reversa no Ubuntu do WSL2 (o Ghidra abre em janela pelo WSLg).
# Seguro para rodar várias vezes: o que já está instalado é pulado.
#
#   bash scripts/wsl/ferramentas-re.sh --simular   # mostra o que faria
#   bash scripts/wsl/ferramentas-re.sh             # instala
#
# Instala: gcc, gdb, binutils (objdump, strings), strace, ltrace, xxd, radare2 (triagem rápida), gocryptfs (pasta dos alvos cifrada), Java 21, Ghidra (última versão, da NSA),
# o pacote do GhidraMCP (IA dentro do Ghidra) e o ilspycmd (descompilador de .NET).
# Pede o gh logado (passo do GitHub) para baixar das páginas oficiais de release.
# Regra: só analise binários seus, dos seus alunos em aula ou desafios feitos para isso (crackmes).
set -euo pipefail

SIMULAR=0; PASTA="$HOME/ferramentas"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --simular) SIMULAR=1 ;;
    --pasta) PASTA="${2:?informe a pasta}"; shift ;;
    -h|--help) sed -n '2,11p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done

SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
APT="DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold"
mkdir -p "$HOME/.local/state" "$HOME/.local/bin"
LOG="$HOME/.local/state/ferramentas-re-$(date +%Y%m%d-%H%M).log"
ERROS=0
export PATH="$HOME/.local/bin:$HOME/.dotnet/tools:$PATH"

linha() { printf '%-8s %-26s %-11s %s\n' "$1" "$2" "$3" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "INSTALARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "INSTALADO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}

echo "Registro em: $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

# 1. Pacotes do sistema
PACOTES=(build-essential gdb binutils strace ltrace xxd file unzip openjdk-21-jdk radare2 gocryptfs)
FALTAM=()
for p in "${PACOTES[@]}"; do dpkg -s "$p" >/dev/null 2>&1 || FALTAM+=("$p"); done
if [[ ${#FALTAM[@]} -eq 0 ]]; then linha base "pacotes (${#PACOTES[@]})" "JA TEM"
else rodar base "pacotes (${#FALTAM[@]})" bash -c "$SUDO apt-get update -y && $SUDO env $APT install ${FALTAM[*]}"; fi

# 2. Ghidra (release oficial da NSA no GitHub)
if [[ -x "$HOME/.local/bin/ghidra" ]]; then linha ghidra "Ghidra" "JA TEM" "$(readlink -f "$HOME/.local/bin/ghidra")"
elif ! tem gh || ! gh auth status >/dev/null 2>&1; then linha ghidra "Ghidra" "FALTA" "faça login no gh antes (gh auth login)"; ERROS=$((ERROS + 1))
else
  rodar ghidra "Ghidra" bash -c "
    set -euo pipefail
    tmp=\$(mktemp -d)
    gh release download -R NationalSecurityAgency/ghidra --pattern 'ghidra_*_PUBLIC_*.zip' -D \"\$tmp\"
    mkdir -p '$PASTA'
    unzip -q \"\$tmp\"/ghidra_*.zip -d '$PASTA'
    dir=\$(find '$PASTA' -maxdepth 1 -type d -name 'ghidra_*_PUBLIC' | sort | tail -1)
    ln -sf \"\$dir/ghidraRun\" '$HOME/.local/bin/ghidra'
    rm -rf \"\$tmp\""
fi

# 3. GhidraMCP: plugin do Ghidra + ponte MCP em Python (instale o .zip em File > Install Extensions)
if compgen -G "$PASTA/ghidramcp/*.zip" >/dev/null; then linha ghidra "GhidraMCP (pacote)" "JA TEM" "$PASTA/ghidramcp"
elif tem gh && gh auth status >/dev/null 2>&1; then
  rodar ghidra "GhidraMCP (pacote)" bash -c "mkdir -p '$PASTA/ghidramcp' && gh release download -R LaurieWired/GhidraMCP --pattern '*.zip' -D '$PASTA/ghidramcp'"
else linha ghidra "GhidraMCP (pacote)" "FALTA" "faça login no gh antes (gh auth login)"; fi

# 4. ilspycmd: descompilador de .NET pela linha de comando
if tem ilspycmd; then linha dotnet "ilspycmd" "JA TEM"
elif tem dotnet; then rodar dotnet "ilspycmd" dotnet tool install -g ilspycmd
else linha dotnet "ilspycmd" "FALTA" "instale o .NET pelo bootstrap.sh antes"; ERROS=$((ERROS + 1)); fi

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta. Rode sem --simular para aplicar."
elif [[ $ERROS -gt 0 ]]; then echo "$ERROS item(ns) com problema. Veja $LOG"; exit 1
else
  echo "Pronto. Abra o Ghidra com: ghidra"
  echo "GhidraMCP: no Ghidra, File > Install Extensions > + > o .zip em $PASTA/ghidramcp; depois veja docs/seguranca/01-engenharia-reversa.md"
fi
