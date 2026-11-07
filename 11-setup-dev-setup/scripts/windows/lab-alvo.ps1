# Laboratorio de alvo isolado no VirtualBox: a VM Kali (atacante) e a VM Alvo (o programa que voce estuda)
# so conversam entre si, numa rede interna sem internet, sem pasta compartilhada e sem area de transferencia.
#
#   powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\lab-alvo.ps1 -Acao status
#   ... -Acao isolar        # liga a rede interna lab-alvo nas duas VMs (com elas desligadas)
#   ... -Acao snapshot      # tira a foto "limpo" do Alvo antes de atacar
#   ... -Acao restaurar     # volta o Alvo para "limpo" depois do teste (desfaz o que o ataque mudou)
#   ... -Acao liberar-kali  # devolve a internet so ao Kali, para atualizar (com o Alvo desligado)
#   Nomes diferentes: -Kali "Kali 2026" -Alvo "Windows Alvo"
#
# Regra: no Alvo so entra programa seu, de codigo aberto, feito para isso, ou de cliente com termo assinado.
# Instale o programa no Alvo ANTES de isolar (ou por ISO/disco virtual); depois disso ele nao sai mais da rede interna.

[CmdletBinding()]
param(
  [ValidateSet('status', 'isolar', 'snapshot', 'restaurar', 'liberar-kali')]
  [string]$Acao = 'status',
  [string]$Kali = 'Kali',
  [string]$Alvo = 'Alvo',
  [string]$Rede = 'lab-alvo'
)

$ErrorActionPreference = 'Stop'
$vbox = Join-Path $env:ProgramFiles 'Oracle\VirtualBox\VBoxManage.exe'
if (-not (Test-Path $vbox)) {
  Write-Host "VirtualBox nao encontrado em $vbox. Instale pelo instalar.ps1 (passo do Windows)."
  exit 1
}

function Invoke-VBox {
  param([string[]]$Argumentos)
  $saida = & $vbox @Argumentos 2>&1
  if ($LASTEXITCODE -ne 0) { throw "VBoxManage $($Argumentos -join ' ') falhou: $saida" }
  return $saida
}

function Get-InfoVm {
  param([string]$Nome)
  $info = @{}
  foreach ($linha in (Invoke-VBox -Argumentos @('showvminfo', $Nome, '--machinereadable'))) {
    if ($linha -match '^"?([^"=]+)"?="?([^"]*)"?$') { $info[$Matches[1]] = $Matches[2] }
  }
  return $info
}

function Test-VmExiste {
  param([string]$Nome)
  $lista = (Invoke-VBox -Argumentos @('list', 'vms')) | Out-String
  return $lista -match ('"' + [regex]::Escape($Nome) + '"')
}

function Assert-Desligada {
  param([string]$Nome)
  $estado = (Get-InfoVm -Nome $Nome)['VMState']
  if ($estado -ne 'poweroff' -and $estado -ne 'aborted' -and $estado -ne 'saved') {
    throw "A VM '$Nome' esta '$estado'. Desligue-a antes (Maquina > ACPI desligar)."
  }
}

function Show-Status {
  param([string]$Nome, [string]$NomeRede)
  if (-not (Test-VmExiste -Nome $Nome)) { Write-Host "FALTA  VM '$Nome' nao existe no VirtualBox"; return $false }
  $i = Get-InfoVm -Nome $Nome
  $isolada = $true
  $placas = @()
  foreach ($n in 1..4) {
    $tipo = $i["nic$n"]
    if ($tipo -and $tipo -ne 'none') {
      $placas += "nic$n=$tipo" + $(if ($tipo -eq 'intnet') { "($($i["intnet$n"]))" } else { '' })
      if ($tipo -ne 'intnet' -or $i["intnet$n"] -ne $NomeRede) { $isolada = $false }
    }
  }
  $pastas = @($i.Keys | Where-Object { $_ -like 'SharedFolderNameMachineMapping*' }).Count
  if ($pastas -gt 0) { $isolada = $false }
  $clip = $i['clipboard']
  $status = if ($isolada) { 'ISOLADA' } else { 'ABERTA' }
  Write-Host ("{0,-8} {1,-14} estado={2}; placas: {3}; pastas compartilhadas: {4}; clipboard: {5}" -f $status, $Nome, $i['VMState'], ($placas -join ', '), $pastas, $clip)
  return $isolada
}

function Invoke-Isolamento {
  param([string]$Nome, [string]$NomeRede)
  Assert-Desligada -Nome $Nome
  Invoke-VBox -Argumentos @('modifyvm', $Nome, '--nic1', 'intnet', '--intnet1', $NomeRede, '--nic2', 'none', '--nic3', 'none', '--nic4', 'none',
                            '--clipboard-mode', 'disabled', '--drag-and-drop', 'disabled') | Out-Null
  $i = Get-InfoVm -Nome $Nome
  foreach ($k in @($i.Keys | Where-Object { $_ -like 'SharedFolderNameMachineMapping*' })) {
    Invoke-VBox -Argumentos @('sharedfolder', 'remove', $Nome, '--name', $i[$k]) | Out-Null
  }
  Write-Host "OK     '$Nome' so fala na rede interna $NomeRede, sem pasta compartilhada e sem area de transferencia"
}

switch ($Acao) {
  'status' {
    $a = Show-Status -Nome $Kali -NomeRede $Rede
    $b = Show-Status -Nome $Alvo -NomeRede $Rede
    if ($a -and $b) { Write-Host "Laboratorio isolado. Dentro do Kali: ip a, e nmap na faixa da rede interna." }
    else { Write-Host "Rode -Acao isolar com as duas VMs desligadas." }
  }
  'isolar' {
    Invoke-Isolamento -Nome $Kali -NomeRede $Rede
    Invoke-Isolamento -Nome $Alvo -NomeRede $Rede
    Write-Host "Na rede interna nao ha DHCP: configure IP fixo nas duas (ex.: Kali 10.66.0.10/24 e Alvo 10.66.0.20/24)."
  }
  'snapshot' {
    Assert-Desligada -Nome $Alvo
    Invoke-VBox -Argumentos @('snapshot', $Alvo, 'take', 'limpo', '--description', 'Antes do ataque') | Out-Null
    Write-Host "OK     foto 'limpo' do '$Alvo' tirada"
  }
  'restaurar' {
    Assert-Desligada -Nome $Alvo
    Invoke-VBox -Argumentos @('snapshot', $Alvo, 'restore', 'limpo') | Out-Null
    Write-Host "OK     '$Alvo' voltou ao estado 'limpo'"
  }
  'liberar-kali' {
    Assert-Desligada -Nome $Kali
    Assert-Desligada -Nome $Alvo
    Invoke-VBox -Argumentos @('modifyvm', $Kali, '--nic1', 'nat') | Out-Null
    Write-Host "OK     Kali com internet (NAT) para atualizar. Rode -Acao isolar antes de ligar o Alvo de novo."
  }
}
