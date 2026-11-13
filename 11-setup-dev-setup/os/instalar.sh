#!/usr/bin/env bash
# Transforma um Ubuntu (24.04 ou mais novo) recém-instalado, nativo ou em VM, no AMtech OS.
# É o mesmo caminho do Omarchy no Arch: instala a base oficial, depois roda este script.
# Não mexe em disco nem em partição. Seguro para rodar várias vezes: o que já está pronto é pulado.
#
#   bash os/instalar.sh --simular                         # mostra o que faria, sem mudar nada
#   bash os/instalar.sh --perfil dev --nome "Alan Mateus" --email voce@exemplo.com
#
# Opções:
#   --perfil P     dev (padrão), escola, empresa, seguranca ou criador
#   --simular      não muda nada, só relata
#   --com-nvidia   instala o driver da NVIDIA recomendado (só em máquina de verdade, não em VM)
#   --sem-setup    não roda o preparador do dev-setup (scripts/wsl/bootstrap.sh)
#   --nome/--email identidade do Git, repassada ao preparador do dev-setup
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RAIZ="$(dirname "$AQUI")"
PERFIL="dev"; SIMULAR=0; NVIDIA=0; SETUP=1; NOME=""; EMAIL=""
PERFIS="dev escola empresa seguranca criador"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --perfil) PERFIL="${2:-}"; shift ;;
    --simular) SIMULAR=1 ;;
    --com-nvidia) NVIDIA=1 ;;
    --sem-setup) SETUP=0 ;;
    --nome) NOME="${2:-}"; shift ;;
    --email) EMAIL="${2:-}"; shift ;;
    -h|--help) sed -n '2,16p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done
if [[ " $PERFIS " != *" $PERFIL "* ]]; then echo "Perfil inválido: $PERFIL (use: $PERFIS)" >&2; exit 64; fi

VERSAO="$(cat "$AQUI/versao")"
USUARIO="${SUDO_USER:-${USER:-$(id -un)}}"
SUDO="sudo"; [[ $EUID -eq 0 ]] && SUDO=""
APT=(env DEBIAN_FRONTEND=noninteractive apt-get -y -o Dpkg::Options::=--force-confdef -o Dpkg::Options::=--force-confold)
LOG="${HOME}/amtech-os-$(date +%Y%m%d-%H%M).log"
ERROS=0; AVISOS=0

col() { local LC_ALL=C.UTF-8; local n=$(($2 - ${#1})); ((n < 1)) && n=1; printf '%s%*s' "$1" "$n" ""; }  # alinha por letras, não por bytes (acentos)
linha() { printf '%s%s%s%s\n' "$(col "$1" 12)" "$(col "$2" 33)" "$(col "$3" 10)" "${4:-}" | tee -a "$LOG"; }
tem() { command -v "$1" >/dev/null 2>&1; }
rodar() {  # rodar <etapa> <item> <comando...>
  local etapa="$1" item="$2"; shift 2
  if [[ $SIMULAR -eq 1 ]]; then linha "$etapa" "$item" "FARIA"; return 0; fi
  if "$@" >>"$LOG" 2>&1; then linha "$etapa" "$item" "FEITO"; else linha "$etapa" "$item" "ERRO" "veja $LOG"; ERROS=$((ERROS + 1)); fi
}
aviso() { linha "$1" "$2" "AVISO" "${3:-}"; AVISOS=$((AVISOS + 1)); }
gravar() {  # gravar <destino> <modo>  (conteúdo pela entrada padrão)
  $SUDO install -D -m "$2" /dev/stdin "$1"
}
pacotes_de() { grep -hv '^\s*#' "$@" | sed 's/\s.*//' | grep -v '^$' | sort -u; }

echo "AMtech OS $VERSAO · perfil $PERFIL · registro em $LOG"
[[ $SIMULAR -eq 1 ]] && echo "MODO: SIMULAR (nada será alterado)"

# ------------------------------------------------------------------ 0. ambiente
# shellcheck disable=SC1091
. /etc/os-release
if [[ "$ID" != "ubuntu" && " ${ID_LIKE:-} " != *" ubuntu "* ]]; then
  echo "Este instalador é para Ubuntu (achei: $PRETTY_NAME)." >&2; exit 1
fi
if [[ "$(printf '%s\n24.04\n' "$VERSION_ID" | sort -V | head -1)" != "24.04" ]]; then
  echo "Precisa do Ubuntu 24.04 ou mais novo (achei: $VERSION_ID)." >&2; exit 1
fi
linha "ambiente" "Ubuntu" "OK" "$PRETTY_NAME"
if grep -qi microsoft /proc/version 2>/dev/null; then
  if [[ $SIMULAR -eq 0 ]]; then echo "Isto é o WSL. O AMtech OS é para Ubuntu nativo ou VM (no WSL use scripts/wsl/bootstrap.sh)." >&2; exit 1; fi
  aviso "ambiente" "WSL" "no WSL só o --simular roda"
fi
VIRT="$(systemd-detect-virt 2>/dev/null || echo none)"
if [[ "$VIRT" == "none" ]]; then linha "ambiente" "máquina" "OK" "física"; else linha "ambiente" "máquina" "OK" "VM ($VIRT)"; fi
if [[ "$(ps -p 1 -o comm= 2>/dev/null)" != "systemd" ]]; then aviso "ambiente" "systemd" "não é o PID 1: serviços e timers não vão subir"; fi
RAIZFS="$(findmnt -no FSTYPE / 2>/dev/null || echo ?)"
linha "ambiente" "sistema de arquivos /" "OK" "$RAIZFS"

# ------------------------------------------------------------------ 1. pacotes do perfil
mapfile -t PACOTES < <(pacotes_de "$AQUI/perfis/base.lista" "$AQUI/perfis/$PERFIL.lista")
rodar "pacotes" "lista do apt" $SUDO apt-get update
FALTAM=(); INSTALAR=()
# Docker oficial (docker-ce/containerd.io, do docker.com) já instalado conflita com o docker.io do Ubuntu: mantém o que existe.
DOCKER_OFICIAL=0
if dpkg-query -W -f='${Status}' containerd.io 2>/dev/null | grep -q "install ok installed"; then
  DOCKER_OFICIAL=1
  aviso "pacotes" "Docker" "Docker oficial (docker-ce) já instalado: docker.io e docker-compose-v2 ficam de fora"
fi
for p in "${PACOTES[@]}"; do
  if [[ $DOCKER_OFICIAL -eq 1 && ( "$p" == "docker.io" || "$p" == "docker-compose-v2" ) ]]; then continue; fi
  c="$(apt-cache policy "$p" 2>/dev/null | awk '/Candidate:/{print $2}')"
  if [[ -z "$c" || "$c" == "(none)" ]]; then FALTAM+=("$p"); else INSTALAR+=("$p"); fi
done
[[ ${#FALTAM[@]} -gt 0 ]] && aviso "pacotes" "não existem nesta versão" "${FALTAM[*]}"
rodar "pacotes" "${#INSTALAR[@]} do perfil $PERFIL" $SUDO "${APT[@]}" install "${INSTALAR[@]}"

# ------------------------------------------------------------------ 2. GPU
if [[ $NVIDIA -eq 1 ]]; then
  if [[ "$VIRT" != "none" ]]; then aviso "gpu" "NVIDIA" "VM: driver não instalado"
  elif lspci 2>/dev/null | grep -qi nvidia; then rodar "gpu" "driver NVIDIA recomendado" $SUDO ubuntu-drivers install
  else aviso "gpu" "NVIDIA" "nenhuma placa NVIDIA encontrada"; fi
fi

# ------------------------------------------------------------------ 3. segurança base
if tem ufw || [[ $SIMULAR -eq 1 ]]; then
  rodar "segurança" "firewall: bloqueia entrada" $SUDO ufw default deny incoming
  rodar "segurança" "firewall: libera saída" $SUDO ufw default allow outgoing
  rodar "segurança" "firewall ligado" $SUDO ufw --force enable
fi
if [[ $SIMULAR -eq 1 ]]; then linha "segurança" "atualização de segurança diária" "FARIA"
else
  printf 'APT::Periodic::Update-Package-Lists "1";\nAPT::Periodic::Unattended-Upgrade "1";\n' | gravar /etc/apt/apt.conf.d/20auto-upgrades 0644
  linha "segurança" "atualização de segurança diária" "FEITO"
fi
if tem usbguard; then aviso "segurança" "usbguard instalado, DESLIGADO" "ligue só depois de cadastrar teclado e mouse (os/README.md)"; fi

# ------------------------------------------------------------------ 4. containers
if getent group docker >/dev/null 2>&1 || [[ $SIMULAR -eq 1 && " ${INSTALAR[*]} " == *" docker.io "* ]]; then
  if id -nG "$USUARIO" 2>/dev/null | grep -qw docker; then linha "containers" "$USUARIO no grupo docker" "OK"
  else rodar "containers" "$USUARIO no grupo docker" $SUDO usermod -aG docker "$USUARIO"; fi
fi

# ------------------------------------------------------------------ 5. snapshots
if [[ "$RAIZFS" == "btrfs" ]]; then
  rodar "snapshots" "snapper" $SUDO "${APT[@]}" install snapper
  if [[ -f /etc/snapper/configs/root ]]; then linha "snapshots" "configuração root" "OK"
  else rodar "snapshots" "configuração root" $SUDO snapper -c root create-config /; fi
  rodar "snapshots" "primeiro ponto de volta" $SUDO snapper -c root create --description "AMtech OS $VERSAO instalado"
else
  aviso "snapshots" "raiz em $RAIZFS" "sem ponto de volta; na instalação de verdade escolha Btrfs"
fi

# ------------------------------------------------------------------ 6. identidade e tema
if [[ $SIMULAR -eq 1 ]]; then
  linha "identidade" "/etc/amtech-release" "FARIA"
  linha "identidade" "papel de parede e padrões GNOME" "FARIA"
  linha "identidade" "mensagem do terminal (motd)" "FARIA"
  linha "identidade" "comando amtech" "FARIA"
else
  printf 'NAME="AMtech OS"\nVERSAO="%s"\nPERFIL="%s"\nBASE="%s"\nINSTALADO_EM="%s"\n' \
    "$VERSAO" "$PERFIL" "$PRETTY_NAME" "$(date +%Y-%m-%d)" | gravar /etc/amtech-release 0644
  linha "identidade" "/etc/amtech-release" "FEITO"
  gravar /usr/share/backgrounds/amtech/fundo.svg 0644 < "$AQUI/tema/fundo.svg"
  if tem dconf; then
    [[ -f /etc/dconf/profile/user ]] || printf 'user-db:user\nsystem-db:local\n' | gravar /etc/dconf/profile/user 0644
    gravar /etc/dconf/db/local.d/00-amtech 0644 < "$AQUI/tema/00-amtech"
    rodar "identidade" "papel de parede e padrões GNOME" $SUDO dconf update
  else
    aviso "identidade" "dconf ausente" "papel de parede copiado, padrões GNOME não aplicados"
  fi
  printf '#!/bin/sh\nprintf "\\n  AMtech OS %%s · perfil %%s · amtech ajuda\\n\\n" "%s" "%s"\n' "$VERSAO" "$PERFIL" \
    | gravar /etc/update-motd.d/05-amtech 0755
  linha "identidade" "mensagem do terminal (motd)" "FEITO"
  gravar /usr/local/bin/amtech 0755 < "$AQUI/amtech"
  $SUDO install -d /usr/share/amtech-os
  $SUDO cp -r "$AQUI/perfis" "$AQUI/versao" /usr/share/amtech-os/
  linha "identidade" "comando amtech" "FEITO"
fi

# ------------------------------------------------------------------ 7. dev-setup
if [[ $SETUP -eq 1 && ( "$PERFIL" == "dev" || "$PERFIL" == "seguranca" ) ]]; then
  if [[ ! -f "$RAIZ/scripts/wsl/bootstrap.sh" ]]; then
    aviso "dev-setup" "preparador" "rode este script de dentro do repositório dev-setup"
  elif [[ -z "$NOME" || -z "$EMAIL" ]] && ! git config --global user.email >/dev/null 2>&1; then
    aviso "dev-setup" "preparador" "faltou --nome e --email (identidade do Git); rode de novo com eles"
  else
    args=(); [[ $SIMULAR -eq 1 ]] && args+=(--simular)
    [[ -n "$NOME" ]] && args+=(--nome "$NOME"); [[ -n "$EMAIL" ]] && args+=(--email "$EMAIL")
    echo "---- preparador do dev-setup (scripts/wsl/bootstrap.sh) ----"
    if bash "$RAIZ/scripts/wsl/bootstrap.sh" "${args[@]}"; then linha "dev-setup" "preparador" "$([[ $SIMULAR -eq 1 ]] && echo SIMULADO || echo FEITO)"
    else linha "dev-setup" "preparador" "ERRO" "veja o registro do bootstrap"; ERROS=$((ERROS + 1)); fi
  fi
fi

# ------------------------------------------------------------------ fim
echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação concluída: $ERROS erro(s), $AVISOS aviso(s). Nada foi alterado."
elif [[ $ERROS -gt 0 ]]; then echo "Terminou com $ERROS erro(s) e $AVISOS aviso(s). Veja $LOG"; exit 1
else
  echo "AMtech OS $VERSAO pronto ($AVISOS aviso(s))."
  echo "Saia e entre de novo na sessão (para o tema e o grupo docker valerem) e rode: amtech"
fi
