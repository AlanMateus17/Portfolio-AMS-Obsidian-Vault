# Confere se o lado Windows do setup esta pronto. SOMENTE LEITURA: nao instala nem muda nada.
#   powershell -ExecutionPolicy Bypass -File .\verificar.ps1
# Como Administrador ele tambem confere Secure Boot, TPM e criptografia do disco.
# Sai com codigo 1 se faltar algo obrigatorio.

param([switch]$Json)

$ErrorActionPreference = 'SilentlyContinue'
$res = New-Object System.Collections.Generic.List[object]
function Add-Resultado([string]$area, [string]$item, [string]$status, [string]$detalhe = '', [bool]$obrigatorio = $true) {
  $res.Add([pscustomobject]@{Area = $area; Item = $item; Status = $status; Detalhe = $detalhe; Obrigatorio = $obrigatorio}) | Out-Null
}
$admin = $false
try { $admin = (New-Object Security.Principal.WindowsPrincipal ([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) } catch { $admin = $false }

# Programas
if (Get-Command winget) {
  $lista = (& winget list --accept-source-agreements 2>$null | Out-String)
  $grupos = (Get-Content -Raw -Encoding UTF8 (Join-Path $PSScriptRoot 'pacotes.json') | ConvertFrom-Json).grupos
  foreach ($g in $grupos) { foreach ($p in $g.pacotes) {
    if ($lista -match [regex]::Escape($p.id)) { Add-Resultado 'programa' $p.nome 'OK' $p.id $p.obrigatorio }
    else { Add-Resultado 'programa' $p.nome 'FALTA' "winget install --id $($p.id) -e" $p.obrigatorio }
  } }
} else { Add-Resultado 'programa' 'winget' 'FALTA' 'Instalador de Aplicativo da Microsoft Store' }

# WSL
$lv = ((& wsl.exe -l -v 2>$null | Out-String) -replace "`0", '')
$ubuntu = ($lv -split "`r?`n" | Where-Object { $_ -match 'Ubuntu' } | Select-Object -First 1)
if ($ubuntu -and $ubuntu -match '\s2\s*$') { Add-Resultado 'wsl' 'Ubuntu no WSL2' 'OK' ($ubuntu.Trim() -replace '\s+', ' ') }
elseif ($ubuntu) { Add-Resultado 'wsl' 'Ubuntu no WSL2' 'AVISO' "Esta no WSL1: wsl --set-version <nome> 2" }
else { Add-Resultado 'wsl' 'Ubuntu no WSL2' 'FALTA' 'wsl --install -d Ubuntu-24.04' }

$cfg = Join-Path $env:USERPROFILE '.wslconfig'
if (Test-Path $cfg) {
  $m = [regex]::Match((Get-Content -Raw $cfg), 'memory\s*=\s*(\S+)')
  if ($m.Success) { Add-Resultado 'wsl' '.wslconfig (memoria)' 'OK' $m.Groups[1].Value } else { Add-Resultado 'wsl' '.wslconfig (memoria)' 'AVISO' 'sem limite de memoria' $false }
} else { Add-Resultado 'wsl' '.wslconfig' 'FALTA' 'rode instalar.ps1 -Aplicar' }

# Docker Desktop
$dv = (& docker version --format '{{.Server.Version}}' 2>$null)
if ($LASTEXITCODE -eq 0 -and $dv) { Add-Resultado 'docker' 'Docker Desktop' 'OK' "servidor $dv" }
else { Add-Resultado 'docker' 'Docker Desktop' 'FALTA' 'abra o Docker Desktop e espere o icone ficar verde' }

# Ollama (opcional)
try {
  $t = Invoke-RestMethod -Uri 'http://localhost:11434/api/tags' -TimeoutSec 3
  $n = @($t.models).Count
  if ($n -gt 0) { Add-Resultado 'ia' 'Ollama' 'OK' "$n modelo(s)" $false } else { Add-Resultado 'ia' 'Ollama' 'AVISO' 'rodando, sem modelo: ollama pull <modelo de 3 a 4B>' $false }
} catch { Add-Resultado 'ia' 'Ollama' 'AVISO' 'nao respondeu em localhost:11434' $false }

# Seguranca (so como Administrador)
if ($admin) {
  try { if (Confirm-SecureBootUEFI) { Add-Resultado 'seguranca' 'Secure Boot' 'OK' } else { Add-Resultado 'seguranca' 'Secure Boot' 'FALTA' 'ligue na BIOS' } } catch { Add-Resultado 'seguranca' 'Secure Boot' 'AVISO' 'nao foi possivel ler' $false }
  $tpm = Get-Tpm
  if ($tpm -and $tpm.TpmReady) { Add-Resultado 'seguranca' 'TPM' 'OK' } else { Add-Resultado 'seguranca' 'TPM' 'AVISO' 'TPM nao pronto' $false }
  $bl = Get-BitLockerVolume -MountPoint $env:SystemDrive
  if ($bl -and $bl.ProtectionStatus -eq 'On') { Add-Resultado 'seguranca' 'Criptografia do disco' 'OK' $bl.EncryptionMethod }
  else { Add-Resultado 'seguranca' 'Criptografia do disco' 'FALTA' 'Configuracoes > Privacidade e seguranca > Criptografia do dispositivo' }
} else {
  Add-Resultado 'seguranca' 'Secure Boot, TPM, criptografia' 'AVISO' 'rode como Administrador para conferir' $false
}
$mp = Get-MpComputerStatus
if ($mp -and $mp.RealTimeProtectionEnabled) { Add-Resultado 'seguranca' 'Defender (tempo real)' 'OK' } else { Add-Resultado 'seguranca' 'Defender (tempo real)' 'AVISO' 'nao confirmado' $false }

# Saida
if ($Json) { $res | ConvertTo-Json -Depth 3; }
else {
  $res | Format-Table Area, Item, Status, Detalhe -AutoSize | Out-String -Width 220 | Write-Host
}
$faltas = @($res | Where-Object { $_.Status -eq 'FALTA' -and $_.Obrigatorio }).Count
$ok = @($res | Where-Object { $_.Status -eq 'OK' }).Count
if (-not $Json) {
  if ($faltas -eq 0) { Write-Host "Windows pronto: $ok itens OK." -ForegroundColor Green }
  else { Write-Host "Faltam $faltas item(ns) obrigatorio(s)." -ForegroundColor Red }
}
if ($faltas -gt 0) { exit 1 } else { exit 0 }
