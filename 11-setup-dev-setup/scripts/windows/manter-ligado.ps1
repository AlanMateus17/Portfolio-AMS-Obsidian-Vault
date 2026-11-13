<#
  Mantém o Ubuntu (WSL) e o notebook acordados na tomada, para o celular alcançar o setup (v2.28).
  Rodado pelo "just ligar" (pede administrador uma vez) ou à mão:
    powershell -ExecutionPolicy Bypass -File manter-ligado.ps1 [-Distro Ubuntu] [-SemEnergia] [-Desfazer]

  O que faz:
    1. Tarefa "AMtech WSL" no login: liga o Ubuntu escondido; o systemd sobe Ollama, fila, bot e Remote Control.
    2. %USERPROFILE%\.wslconfig: vmIdleTimeout=-1 (o WSL não desliga sozinho quando você fecha o terminal).
    3. Só NA TOMADA: não dormir e tampa fechada não suspende. Na bateria nada muda. Pule com -SemEnergia.
  -Desfazer remove a tarefa e devolve a tampa e o sono na tomada ao padrão (dormir em 30 min, tampa suspende).
#>
param([string]$Distro = "Ubuntu", [switch]$SemEnergia, [switch]$Desfazer)
$ErrorActionPreference = "Stop"

$admin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole(
  [Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $admin) {
  $argumentos = @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "`"$PSCommandPath`"", "-Distro", $Distro)
  if ($SemEnergia) { $argumentos += "-SemEnergia" }
  if ($Desfazer) { $argumentos += "-Desfazer" }
  $p = Start-Process powershell -Verb RunAs -ArgumentList $argumentos -Wait -PassThru
  exit $p.ExitCode
}

$nome = "AMtech WSL"
if ($Desfazer) {
  Unregister-ScheduledTask -TaskName $nome -Confirm:$false -ErrorAction SilentlyContinue
  powercfg /change standby-timeout-ac 30
  powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 1
  powercfg /setactive SCHEME_CURRENT
  Write-Host "Desfeito. O .wslconfig ficou como está (apague a linha vmIdleTimeout se quiser)."
  exit 0
}

# 1. Tarefa no login (sem janela: conhost --headless, Windows 11)
$acao = New-ScheduledTaskAction -Execute "conhost.exe" -Argument "--headless wsl.exe -d $Distro --exec /bin/sleep infinity"
$gatilho = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
$ajustes = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit ([TimeSpan]::Zero) -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -TaskName $nome -Action $acao -Trigger $gatilho -Settings $ajustes -Force | Out-Null
Start-ScheduledTask -TaskName $nome
Write-Host "[ok] Tarefa '$nome' criada e ligada."

# 2. .wslconfig
$cfg = Join-Path $env:USERPROFILE ".wslconfig"
$texto = if (Test-Path $cfg) { Get-Content $cfg -Raw } else { "" }
if ($texto -notmatch "vmIdleTimeout") {
  if ($texto -notmatch "\[wsl2\]") { $texto = $texto.TrimEnd() + "`r`n[wsl2]`r`n" }
  $texto = $texto -replace "\[wsl2\]\r?\n", "[wsl2]`r`nvmIdleTimeout=-1`r`n"
  Set-Content -Path $cfg -Value $texto.Trim() -Encoding ascii
  Write-Host "[ok] .wslconfig: vmIdleTimeout=-1 (vale depois do próximo 'wsl --shutdown')."
} else { Write-Host "[ok] .wslconfig já tem vmIdleTimeout." }

# 3. Energia, só na tomada
if (-not $SemEnergia) {
  powercfg /change standby-timeout-ac 0
  powercfg /setacvalueindex SCHEME_CURRENT SUB_BUTTONS LIDACTION 0
  powercfg /setactive SCHEME_CURRENT
  Write-Host "[ok] Na tomada: não dorme e a tampa fechada não suspende. Na bateria, nada mudou."
}
exit 0
