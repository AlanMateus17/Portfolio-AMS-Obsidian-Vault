# Inventario do notebook - SOMENTE LEITURA. Nao apaga, nao desinstala, nao altera nada.
# Rode no PowerShell (de preferencia como Administrador para ver tudo):
#   powershell -ExecutionPolicy Bypass -File .\inventario.ps1
# Gera a pasta inventario-AAAAMMDD na mesma pasta do script.

$ErrorActionPreference = 'SilentlyContinue'
$out = Join-Path $PSScriptRoot ("inventario-" + (Get-Date -Format 'yyyyMMdd'))
New-Item -ItemType Directory -Force -Path $out | Out-Null
function Size($path) {
  if (Test-Path $path) {
    $b = (Get-ChildItem -LiteralPath $path -Recurse -Force -File | Measure-Object Length -Sum).Sum
    [math]::Round($b / 1GB, 2)
  } else { 0 }
}

Write-Host "1/7 Programas instalados..."
$keys = 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
        'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*'
Get-ItemProperty $keys |
  Where-Object { $_.DisplayName -and -not $_.SystemComponent } |
  Select-Object DisplayName, DisplayVersion, Publisher, InstallDate,
    @{n='TamanhoMB';e={ if ($_.EstimatedSize) { [math]::Round($_.EstimatedSize/1024,0) } else { '' } }} |
  Sort-Object DisplayName -Unique |
  Export-Csv (Join-Path $out '1-programas.csv') -NoTypeInformation -Encoding UTF8

Write-Host "2/7 Apps da Microsoft Store..."
Get-AppxPackage |
  Where-Object { -not $_.IsFramework -and $_.SignatureKind -ne 'System' } |
  Select-Object Name, Publisher, Version |
  Sort-Object Name |
  Export-Csv (Join-Path $out '2-apps-store.csv') -NoTypeInformation -Encoding UTF8

Write-Host "3/7 Programas que iniciam com o Windows..."
Get-CimInstance Win32_StartupCommand |
  Select-Object Name, Command, Location, User |
  Export-Csv (Join-Path $out '3-inicializacao.csv') -NoTypeInformation -Encoding UTF8

Write-Host "4/7 Espaco em disco..."
Get-PSDrive -PSProvider FileSystem |
  Select-Object Name, @{n='UsadoGB';e={[math]::Round($_.Used/1GB,1)}}, @{n='LivreGB';e={[math]::Round($_.Free/1GB,1)}} |
  Export-Csv (Join-Path $out '4-discos.csv') -NoTypeInformation -Encoding UTF8

Write-Host "5/7 Pastas que mais ocupam (pode demorar alguns minutos)..."
$alvos = @(
  "$env:USERPROFILE\Downloads", "$env:USERPROFILE\Desktop", "$env:USERPROFILE\Documents",
  "$env:USERPROFILE\Videos", "$env:USERPROFILE\Pictures", "$env:USERPROFILE\Music",
  "$env:USERPROFILE\dev", "$env:LOCALAPPDATA\Temp", "C:\Windows\Temp",
  "C:\Windows\SoftwareDistribution\Download", "$env:LOCALAPPDATA\Packages",
  "$env:LOCALAPPDATA\Docker", "$env:LOCALAPPDATA\wsl", "$env:USERPROFILE\.nuget\packages",
  "$env:APPDATA\npm-cache", "$env:LOCALAPPDATA\npm-cache", "$env:LOCALAPPDATA\pip\cache",
  "$env:USERPROFILE\.ollama", "C:\Program Files\Unity", "C:\Program Files\Epic Games",
  "$env:LOCALAPPDATA\CrashDumps", "C:\`$Recycle.Bin"
)
$alvos | ForEach-Object { [pscustomobject]@{ Pasta = $_; TamanhoGB = (Size $_) } } |
  Sort-Object TamanhoGB -Descending |
  Export-Csv (Join-Path $out '5-pastas.csv') -NoTypeInformation -Encoding UTF8

Write-Host "6/7 Arquivos grandes (acima de 300 MB) na sua pasta de usuario..."
Get-ChildItem $env:USERPROFILE -Recurse -Force -File |
  Where-Object { $_.Length -gt 300MB } |
  Sort-Object Length -Descending | Select-Object -First 60 |
  Select-Object FullName, @{n='TamanhoGB';e={[math]::Round($_.Length/1GB,2)}}, LastWriteTime |
  Export-Csv (Join-Path $out '6-arquivos-grandes.csv') -NoTypeInformation -Encoding UTF8

Write-Host "7/7 Distros do WSL..."
wsl.exe --list --verbose 2>$null | Out-File (Join-Path $out '7-wsl.txt') -Encoding UTF8

Write-Host ""
Write-Host "Pronto. Nada foi alterado. Resultado em: $out"
Write-Host "Envie os arquivos dessa pasta para o Claude."
