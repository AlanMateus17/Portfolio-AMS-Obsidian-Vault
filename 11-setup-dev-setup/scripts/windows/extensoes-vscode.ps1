# Instala as extensoes do VS Code listadas em vscode-extensoes.txt.
# Seguro para rodar varias vezes: o que ja esta instalado e pulado.
#   powershell -ExecutionPolicy Bypass -File .\extensoes-vscode.ps1           # so mostra
#   powershell -ExecutionPolicy Bypass -File .\extensoes-vscode.ps1 -Aplicar  # instala
param([switch]$Aplicar)

$ErrorActionPreference = 'Stop'
$lista = Join-Path $PSScriptRoot 'vscode-extensoes.txt'
$desejadas = Get-Content $lista | ForEach-Object { $_.Trim() } | Where-Object { $_ -and -not $_.StartsWith('#') }

if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
  Write-Host 'VS Code nao encontrado no PATH. Rode antes o instalar.ps1 -Aplicar e abra um terminal novo.'
  exit 1
}
# cmd /c: avisos do Node no stderr do code.cmd viram erro no Windows PowerShell 5.1 com ErrorActionPreference Stop
$instaladas = @(cmd /c 'code --list-extensions 2>nul' | ForEach-Object { $_.ToLowerInvariant() })
$erros = 0
foreach ($e in $desejadas) {
  if ($instaladas -contains $e.ToLowerInvariant()) { $st = 'JA TEM' }
  elseif (-not $Aplicar) { $st = 'INSTALARIA' }
  else {
    cmd /c "code --install-extension $e --force >nul 2>&1"
    if ($LASTEXITCODE -eq 0) { $st = 'INSTALADO' } else { $st = 'ERRO'; $erros++ }
  }
  Write-Host ("{0,-40} {1}" -f $e, $st)
}
if (-not $Aplicar) { Write-Host 'Simulacao. Rode com -Aplicar para instalar.'; exit 0 }
if ($erros -gt 0) { Write-Host "$erros extensao(oes) com erro: confira o nome no Marketplace."; exit 1 }
Write-Host 'Pronto.'
