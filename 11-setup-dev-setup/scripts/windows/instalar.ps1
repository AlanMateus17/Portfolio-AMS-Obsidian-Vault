# Instala a base do setup no Windows 11: programas (winget), WSL2 com Ubuntu 24.04 e o .wslconfig.
# Seguro para rodar varias vezes: o que ja esta instalado e pulado.
#
# Primeiro, veja o que ele faria (nao muda nada):
#   powershell -ExecutionPolicy Bypass -File .\instalar.ps1
# Depois, aplique de verdade (como Administrador, por causa do WSL):
#   powershell -ExecutionPolicy Bypass -File .\instalar.ps1 -Aplicar
#
# Opcoes:
#   -SoObrigatorios         instala so os programas marcados como obrigatorios
#   -MemoriaWSL 12GB        limite de memoria do WSL (padrao 12GB, metade dos 32 GB deixa folga para o Windows)
#   -SobrescreverWslconfig  troca um .wslconfig que ja existe (o antigo vira .wslconfig.bak)

param(
  [switch]$Aplicar,
  [switch]$SoObrigatorios,
  [string]$MemoriaWSL = '12GB',
  [switch]$SobrescreverWslconfig
)

$ErrorActionPreference = 'Stop'
$log = Join-Path $PSScriptRoot ("instalar-" + (Get-Date -Format 'yyyyMMdd-HHmm') + ".log")
$resumo = New-Object System.Collections.Generic.List[object]

function Registrar([string]$etapa, [string]$item, [string]$status, [string]$detalhe = '') {
  $linha = "{0,-10} {1,-34} {2,-10} {3}" -f $etapa, $item, $status, $detalhe
  Write-Host $linha
  Add-Content -Path $log -Value $linha
  $resumo.Add([pscustomobject]@{Etapa = $etapa; Item = $item; Status = $status; Detalhe = $detalhe}) | Out-Null
}

function EhAdmin {
  try {
    $id = [Security.Principal.WindowsIdentity]::GetCurrent()
    return (New-Object Security.Principal.WindowsPrincipal $id).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
  } catch { return $false }
}

function PacoteInstalado([string]$id) {
  $saida = & winget list --id $id -e --accept-source-agreements 2>$null | Out-String
  return ($LASTEXITCODE -eq 0 -and $saida -match [regex]::Escape($id))
}

Write-Host ""
if ($Aplicar) { Write-Host "MODO: APLICAR (vai instalar e configurar)" -ForegroundColor Yellow }
else { Write-Host "MODO: SIMULAR (nada sera alterado; use -Aplicar para instalar)" -ForegroundColor Cyan }
Write-Host "Registro em: $log"
Write-Host ""

# ------------------------------------------------------------------ 1. winget
if (-not (Get-Command winget -ErrorAction SilentlyContinue)) {
  Registrar 'winget' 'winget' 'FALTA' 'Instale o "Instalador de Aplicativo" pela Microsoft Store e rode de novo.'
  exit 1
}
Registrar 'winget' 'winget' 'OK'

$pacotes = (Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot 'pacotes.json') | ConvertFrom-Json).grupos
foreach ($g in $pacotes) {
  foreach ($p in $g.pacotes) {
    if ($SoObrigatorios -and -not $p.obrigatorio) { continue }
    if (PacoteInstalado $p.id) { Registrar 'programa' $p.nome 'JA TEM' $p.id; continue }
    if (-not $Aplicar) { Registrar 'programa' $p.nome 'INSTALARIA' $p.id; continue }
    & winget install --id $p.id -e --silent --accept-package-agreements --accept-source-agreements | Out-Null
    if ($LASTEXITCODE -eq 0) { Registrar 'programa' $p.nome 'INSTALADO' $p.id }
    else { Registrar 'programa' $p.nome 'ERRO' "winget saiu com codigo $LASTEXITCODE; tente: winget install --id $($p.id) -e" }
  }
}

# ------------------------------------------------------------------ 2. WSL2 + Ubuntu 24.04
$distros = ''
try { $distros = (& wsl.exe --list --quiet 2>$null | Out-String) -replace "`0", '' } catch { $distros = '' }
if ($distros -match 'Ubuntu-24\.04|Ubuntu') {
  Registrar 'wsl' 'Ubuntu no WSL' 'JA TEM' (($distros -split "`r?`n" | Where-Object { $_ -match 'Ubuntu' }) -join ', ')
} elseif (-not $Aplicar) {
  Registrar 'wsl' 'Ubuntu 24.04 no WSL2' 'INSTALARIA' 'wsl --install -d Ubuntu-24.04'
} elseif (-not (EhAdmin)) {
  Registrar 'wsl' 'Ubuntu 24.04 no WSL2' 'PULADO' 'Precisa de Administrador. Abra o PowerShell como Administrador e rode de novo.'
} else {
  & wsl.exe --install -d Ubuntu-24.04 --no-launch
  if ($LASTEXITCODE -eq 0) { Registrar 'wsl' 'Ubuntu 24.04 no WSL2' 'INSTALADO' 'Reinicie o Windows e abra "Ubuntu 24.04" no menu Iniciar para criar seu usuario.' }
  else { Registrar 'wsl' 'Ubuntu 24.04 no WSL2' 'ERRO' "codigo $LASTEXITCODE" }
}

# ------------------------------------------------------------------ 3. .wslconfig
$cfg = Join-Path $env:USERPROFILE '.wslconfig'
$conteudo = @"
# Gerado por dev-setup/scripts/windows/instalar.ps1
[wsl2]
memory=$MemoriaWSL
swap=8GB
localhostForwarding=true
"@
if ((Test-Path $cfg) -and -not $SobrescreverWslconfig) {
  $atual = Get-Content -Raw $cfg
  if ($atual -match "memory\s*=\s*$([regex]::Escape($MemoriaWSL))") { Registrar 'wslconfig' '.wslconfig' 'JA TEM' "memory=$MemoriaWSL" }
  else { Registrar 'wslconfig' '.wslconfig' 'DIFERENTE' 'Ja existe com outros valores. Rode com -SobrescreverWslconfig para trocar (o antigo vira .bak).' }
} elseif (-not $Aplicar) {
  Registrar 'wslconfig' '.wslconfig' 'CRIARIA' "memory=$MemoriaWSL, swap=8GB"
} else {
  if (Test-Path $cfg) { Copy-Item $cfg "$cfg.bak" -Force }
  Set-Content -Path $cfg -Value $conteudo -Encoding ASCII
  Registrar 'wslconfig' '.wslconfig' 'CRIADO' "memory=$MemoriaWSL. Rode 'wsl --shutdown' para valer."
}

# ------------------------------------------------------------------ 4. o que nao da para automatizar
Registrar 'manual' 'DaVinci Resolve' 'MANUAL' 'Nao esta no winget: baixe em blackmagicdesign.com'
Registrar 'manual' 'Docker Desktop -> WSL' 'MANUAL' 'Settings > Resources > WSL integration > ligar Ubuntu-24.04'
Registrar 'manual' 'Criptografia do disco' 'MANUAL' 'Configuracoes > Privacidade e seguranca > Criptografia do dispositivo (guarde a chave no KeePassXC)'

# ------------------------------------------------------------------ resumo
Write-Host ""
$erros = @($resumo | Where-Object { $_.Status -eq 'ERRO' }).Count
$faltam = @($resumo | Where-Object { $_.Status -in 'INSTALARIA', 'CRIARIA' }).Count
if (-not $Aplicar) { Write-Host "Simulacao pronta: $faltam item(ns) seriam instalados ou criados. Rode com -Aplicar." -ForegroundColor Cyan }
elseif ($erros -gt 0) { Write-Host "$erros erro(s). Veja o registro: $log" -ForegroundColor Red; exit 1 }
elseif (@($resumo | Where-Object { $_.Status -eq 'PULADO' }).Count -gt 0) { Write-Host "Quase pronto: ha etapas puladas (veja PULADO acima). Rode de novo como Administrador." -ForegroundColor Yellow; exit 2 }
else { Write-Host "Pronto. Agora rode .\verificar.ps1 para conferir." -ForegroundColor Green }
