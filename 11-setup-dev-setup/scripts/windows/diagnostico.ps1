# Diagnostico do notebook - SOMENTE LEITURA. Nao instala, nao apaga, nao altera nada.
# Ve o hardware, a seguranca e os programas que voce ja tem, compara com o setup
# e diz em que passo do roteiro cada pendencia se resolve.
#
#   Botao direito em RODAR-DIAGNOSTICO.cmd (na raiz) > Executar como administrador
#   ou: powershell -ExecutionPolicy Bypass -File .\scripts\windows\diagnostico.ps1
# (como Administrador ve tambem Secure Boot, TPM, BitLocker e a saude da bateria)
#
# Gera a pasta diagnostico-AAAAMMDD na raiz do repositorio com:
#   diagnostico.md   - o relatorio para voce ler
#   diagnostico.json - os dados brutos (mande para o Claude montar o seu plano)

param([string]$Saida = '')

$ErrorActionPreference = 'Stop'
$raiz = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
if (-not $Saida) { $Saida = Join-Path $raiz ("diagnostico-" + (Get-Date -Format 'yyyyMMdd')) }
New-Item -ItemType Directory -Force -Path $Saida | Out-Null

function Tentar([scriptblock]$Bloco, $Padrao = $null) {
  try { $r = & $Bloco; if ($null -eq $r) { $Padrao } else { $r } } catch { $Padrao }
}
function Tem([string]$Comando) { [bool](Get-Command $Comando -ErrorAction SilentlyContinue) }
function GB($bytes) { if ($bytes) { [math]::Round([double]$bytes / 1GB, 1) } else { $null } }

$admin = Tentar { ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) } $false
$d = [ordered]@{ gerado = (Get-Date -Format 's'); administrador = $admin }

Write-Host "1/6 Sistema e hardware..."
$os = Tentar { Get-CimInstance Win32_OperatingSystem }
$cs = Tentar { Get-CimInstance Win32_ComputerSystem }
$cpu = Tentar { Get-CimInstance Win32_Processor | Select-Object -First 1 }
$d.sistema = [ordered]@{
  windows = Tentar { $os.Caption }; versao = Tentar { $os.Version }; build = Tentar { if ($os) { [int]$os.BuildNumber } }
  fabricante = Tentar { $cs.Manufacturer }; modelo = Tentar { $cs.Model }
  bios = Tentar { (Get-CimInstance Win32_BIOS).SMBIOSBIOSVersion }
}
$d.cpu = [ordered]@{
  nome = Tentar { $cpu.Name.Trim() }; nucleos = Tentar { $cpu.NumberOfCores }; threads = Tentar { $cpu.NumberOfLogicalProcessors }
  virtualizacao = Tentar { $cpu.VirtualizationFirmwareEnabled }
}
$pentes = @(Tentar { Get-CimInstance Win32_PhysicalMemory } @())
$d.memoria = [ordered]@{
  totalGB = Tentar { GB $cs.TotalPhysicalMemory }
  pentes = @($pentes | ForEach-Object { [ordered]@{ GB = (GB $_.Capacity); MHz = $_.Speed; fabricante = $_.Manufacturer } })
  slots = Tentar { (Get-CimInstance Win32_PhysicalMemoryArray | Measure-Object MemoryDevices -Sum).Sum }
  maximoGB = Tentar { [math]::Round((Get-CimInstance Win32_PhysicalMemoryArray | Measure-Object MaxCapacityEx -Sum).Sum / 1MB, 0) }
}
$d.gpu = @(Tentar { Get-CimInstance Win32_VideoController } @() | ForEach-Object { [ordered]@{ nome = $_.Name; driver = $_.DriverVersion; data = (Tentar { $_.DriverDate.ToString('yyyy-MM-dd') }) } })
$d.gpuNvidia = Tentar { if (Tem 'nvidia-smi') { (& nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader) -join '; ' } }
$d.discos = @(Tentar { Get-PhysicalDisk } @() | ForEach-Object { [ordered]@{ nome = $_.FriendlyName; tipo = "$($_.MediaType)"; barramento = "$($_.BusType)"; GB = (GB $_.Size); saude = "$($_.HealthStatus)" } })
$d.volumes = @(Tentar { Get-Volume | Where-Object { $_.DriveLetter } } @() | ForEach-Object { [ordered]@{ letra = "$($_.DriveLetter)"; nome = $_.FileSystemLabel; totalGB = (GB $_.Size); livreGB = (GB $_.SizeRemaining) } })
$d.monitores = Tentar { @(Get-CimInstance -Namespace root\wmi -ClassName WmiMonitorID).Count } $null
$d.bateria = Tentar {
  $proj = (Get-CimInstance -Namespace root\wmi -ClassName BatteryStaticData | Select-Object -First 1).DesignedCapacity
  $real = (Get-CimInstance -Namespace root\wmi -ClassName BatteryFullChargedCapacity | Select-Object -First 1).FullChargedCapacity
  if ($proj) { [ordered]@{ saudePct = [math]::Round(100 * $real / $proj, 0) } }
}
$d.rede = @(Tentar { Get-NetAdapter | Where-Object Status -eq 'Up' } @() | ForEach-Object { [ordered]@{ nome = $_.Name; velocidade = $_.LinkSpeed } })

Write-Host "2/6 Seguranca..."
$d.seguranca = [ordered]@{
  secureBoot = Tentar { Confirm-SecureBootUEFI }
  tpm = Tentar { $t = Get-Tpm; if ($t) { [ordered]@{ presente = $t.TpmPresent; pronto = $t.TpmReady } } }
  criptografia = Tentar { (Get-BitLockerVolume -MountPoint $env:SystemDrive).ProtectionStatus.ToString() }
  defender = Tentar { $m = Get-MpComputerStatus; [ordered]@{ ligado = $m.AntivirusEnabled; tempoReal = $m.RealTimeProtectionEnabled } }
}

Write-Host "3/6 Programas instalados..."
$chaves = 'HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*',
          'HKLM:\Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\*',
          'HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall\*'
$programas = @(Tentar { Get-ItemProperty $chaves | Where-Object { $_.DisplayName -and -not $_.SystemComponent } | Select-Object -ExpandProperty DisplayName | Sort-Object -Unique } @())
$d.totalProgramas = $programas.Count
$wingetIds = @()
if (Tem 'winget') {
  $tmp = Join-Path $env:TEMP 'diag-winget.json'
  Tentar { & winget export -o $tmp --accept-source-agreements --disable-interactivity *> $null } | Out-Null
  $wingetIds = @(Tentar { (Get-Content $tmp -Raw | ConvertFrom-Json).Sources.Packages.PackageIdentifier } @())
}
$pacotes = Get-Content (Join-Path $PSScriptRoot 'pacotes.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$d.programasDoSetup = @()
foreach ($g in $pacotes.grupos) {
  foreach ($p in $g.pacotes) {
    $palavra = ($p.id -split '\.')[-1]
    $tem = ($wingetIds -contains $p.id) -or [bool]($programas | Where-Object { $_ -like "*$palavra*" } | Select-Object -First 1)
    $d.programasDoSetup += [ordered]@{ id = $p.id; nome = $p.nome; obrigatorio = [bool]$p.obrigatorio; temos = $tem }
  }
}

Write-Host "4/6 Ferramentas de desenvolvimento..."
function Versao([string]$c, [string[]]$a) { if (Tem $c) { Tentar { ((& $c @a 2>&1) | Select-Object -First 1).ToString().Trim() } 'instalado' } }
$d.ferramentas = [ordered]@{
  git = Versao 'git' @('--version'); gh = Versao 'gh' @('--version'); code = Versao 'code' @('--version')
  docker = Versao 'docker' @('--version'); ollama = Versao 'ollama' @('--version'); node = Versao 'node' @('--version')
  python = Versao 'python' @('--version'); dotnet = Versao 'dotnet' @('--version'); winget = Versao 'winget' @('--version')
}
$d.wsl = Tentar { if (Tem 'wsl') { ((& wsl.exe --list --verbose) -join "`n") -replace "`0", '' } }
$d.modelosOllama = @(Tentar { if (Tem 'ollama') { & ollama list | Select-Object -Skip 1 | ForEach-Object { ($_ -split '\s+')[0] } } } @())
$extDesejadas = @(Get-Content (Join-Path $PSScriptRoot 'vscode-extensoes.txt') | ForEach-Object { $_.Trim() } | Where-Object { $_ -and -not $_.StartsWith('#') })
$extTem = @(Tentar { if (Tem 'code') { & code --list-extensions } } @() | ForEach-Object { $_.ToLowerInvariant() })
$d.extensoesFaltando = @($extDesejadas | Where-Object { $extTem -notcontains $_.ToLowerInvariant() })

Write-Host "5/6 Comparando com o setup..."
$im = Tentar { Get-Content (Join-Path $raiz 'data\implantacao.json') -Raw -Encoding UTF8 | ConvertFrom-Json }
function Passo([string]$id) {
  if (-not $im) { return $id }
  for ($i = 0; $i -lt $im.fases.Count; $i++) {
    $ps = @($im.fases[$i].passos)
    for ($j = 0; $j -lt $ps.Count; $j++) { if ($ps[$j].id -eq $id) { return ("passo {0}.{1} ({2})" -f $i, ($j + 1), $ps[$j].titulo) } }
  }
  $id
}
$achados = New-Object System.Collections.Generic.List[object]
function Achado([string]$nivel, [string]$texto, [string]$passo) { $achados.Add([ordered]@{ nivel = $nivel; texto = $texto; passo = $passo }) | Out-Null }

$ram = $d.memoria.totalGB
if ($ram -and $ram -lt 16) { Achado 'ATENCAO' "RAM de $ram GB: o setup pede 16 GB ou mais (Docker, WSL e IA local)." (Passo 'hardware') }
elseif ($ram) { Achado 'OK' "RAM de $ram GB." '' }
if ($d.cpu.virtualizacao -eq $false) { Achado 'FALTA' 'Virtualizacao desligada no firmware: o WSL2 e o Docker nao funcionam sem ela. Ligue no BIOS (F2) antes de instalar.' (Passo 'win-aplicar') }
$livreC = ($d.volumes | Where-Object { $_.letra -eq 'C' } | Select-Object -First 1).livreGB
if ($null -ne $livreC -and $livreC -lt 100) { Achado 'ATENCAO' "So $livreC GB livres no C: o setup completo usa uns 100 GB. Veja o inventario para liberar espaco." (Passo 'inventario') }
if ($d.sistema.build -and $d.sistema.build -lt 22000) { Achado 'ATENCAO' 'Este Windows nao e o 11.' (Passo 'windows-update') }
if (-not ($d.gpu | Where-Object { $_.nome -match 'NVIDIA' })) { Achado 'ATENCAO' 'Nenhuma placa NVIDIA encontrada: sem CUDA, a IA local roda so na CPU.' (Passo 'gpu-wsl') }
if ($d.seguranca.criptografia -and $d.seguranca.criptografia -ne 'On') { Achado 'FALTA' 'Disco sem criptografia ligada.' (Passo 'cripto') }
if ($d.seguranca.secureBoot -eq $false) { Achado 'ATENCAO' 'Secure Boot desligado.' (Passo 'cripto') }
if ($d.seguranca.defender -and -not $d.seguranca.defender.tempoReal) { Achado 'FALTA' 'Defender sem protecao em tempo real.' (Passo 'defender') }
if ($d.bateria -and $d.bateria.saudePct -lt 70) { Achado 'ATENCAO' "Bateria com $($d.bateria.saudePct)% da capacidade original: use o notebook no nobreak." (Passo 'hardware') }
if ($d.monitores -eq 1) { Achado 'INFO' 'Um monitor so: o 2o monitor esta no passo da mesa.' (Passo 'hardware') }
$faltaObr = @($d.programasDoSetup | Where-Object { $_.obrigatorio -and -not $_.temos })
$faltaOpc = @($d.programasDoSetup | Where-Object { -not $_.obrigatorio -and -not $_.temos })
if ($faltaObr.Count) { Achado 'FALTA' ("Programas obrigatorios que faltam: " + (($faltaObr | ForEach-Object { $_.nome }) -join ', ') + '.') (Passo 'win-aplicar') }
if ($faltaOpc.Count) { Achado 'INFO' ("Opcionais que faltam: " + (($faltaOpc | ForEach-Object { $_.nome }) -join ', ') + '.') (Passo 'win-aplicar') }
if (-not $d.wsl -or $d.wsl -notmatch 'Ubuntu') { Achado 'FALTA' 'Ubuntu no WSL2 ainda nao instalado.' (Passo 'win-aplicar') }
if (-not $d.ferramentas.docker) { Achado 'FALTA' 'Docker Desktop ainda nao instalado.' (Passo 'win-aplicar') }
if (-not $d.modelosOllama.Count) { Achado 'INFO' 'Nenhum modelo baixado no Ollama.' (Passo 'ollama-modelo') }
if ($d.extensoesFaltando.Count) { Achado 'INFO' ("Extensoes do VS Code que faltam: " + $d.extensoesFaltando.Count + '.') (Passo 'vscode-ext') }
if (-not $admin) { Achado 'INFO' 'Rodou sem Administrador: Secure Boot, TPM, criptografia e bateria podem ter ficado de fora.' '' }
$d.achados = $achados

Write-Host "6/6 Escrevendo o relatorio..."
$d | ConvertTo-Json -Depth 6 | Out-File (Join-Path $Saida 'diagnostico.json') -Encoding UTF8
$t = New-Object System.Collections.Generic.List[string]
$t.Add('# Diagnostico do notebook'); $t.Add('')
$t.Add("Gerado em $($d.gerado). Somente leitura: nada foi alterado."); $t.Add('')
$t.Add('## O que voce tem'); $t.Add('')
$t.Add('| Item | Encontrado |'); $t.Add('|---|---|')
$t.Add("| Modelo | $($d.sistema.fabricante) $($d.sistema.modelo) |")
$t.Add("| Windows | $($d.sistema.windows) (build $($d.sistema.build)) |")
$t.Add("| Processador | $($d.cpu.nome) ($($d.cpu.nucleos) nucleos, $($d.cpu.threads) threads) |")
$t.Add("| Memoria | $($d.memoria.totalGB) GB em $(@($d.memoria.pentes).Count) de $($d.memoria.slots) slots (maximo $($d.memoria.maximoGB) GB) |")
$t.Add("| Placa de video | $((@($d.gpu) | ForEach-Object { $_.nome }) -join ' + ')$(if ($d.gpuNvidia) { ' (' + $d.gpuNvidia + ')' }) |")
$t.Add("| Discos | $((@($d.discos) | ForEach-Object { "$($_.nome) $($_.tipo) $($_.GB) GB ($($_.saude))" }) -join '; ') |")
$t.Add("| Espaco livre | $((@($d.volumes) | ForEach-Object { "$($_.letra): $($_.livreGB) de $($_.totalGB) GB" }) -join '; ') |")
$t.Add("| Monitores | $($d.monitores) |")
$t.Add("| Bateria | $(if ($d.bateria) { "$($d.bateria.saudePct)% da original" } else { 'sem leitura (rode como Administrador)' }) |")
$t.Add("| Programas instalados | $($d.totalProgramas) |")
$t.Add("| Do setup, ja instalados | $(@($d.programasDoSetup | Where-Object { $_.temos }).Count) de $(@($d.programasDoSetup).Count) |")
$t.Add("| WSL | $(if ($d.wsl) { ($d.wsl -split "`n" | Select-Object -Skip 1 | ForEach-Object { $_.Trim() } | Where-Object { $_ }) -join '; ' } else { 'nao instalado' }) |")
$t.Add("| Modelos no Ollama | $(if ($d.modelosOllama.Count) { $d.modelosOllama -join ', ' } else { 'nenhum' }) |")
$t.Add('')
$t.Add('## O que fazer, e em que passo do roteiro'); $t.Add('')
foreach ($a in ($achados | Sort-Object { @{ FALTA = 0; ATENCAO = 1; INFO = 2; OK = 3 }[$_.nivel] })) {
  $t.Add("- **$($a.nivel)** $($a.texto)$(if ($a.passo) { " Resolve no $($a.passo)." })")
}
$t.Add('')
$t.Add('## Programas do setup'); $t.Add('')
$t.Add('| Programa | Obrigatorio | Situacao |'); $t.Add('|---|---|---|')
foreach ($p in $d.programasDoSetup) { $t.Add("| $($p.nome) | $(if ($p.obrigatorio) { 'sim' } else { 'nao' }) | $(if ($p.temos) { 'ja tem' } else { 'falta' }) |") }
$t.Add('')
$t.Add('Mande a pasta inteira para o Claude: ele marca no seu acompanhamento o que ja esta feito e ajusta o que falta.')
$t | Out-File (Join-Path $Saida 'diagnostico.md') -Encoding UTF8

Write-Host ""
Write-Host ("Pronto. {0} pendencia(s), {1} aviso(s). Relatorio: {2}" -f @($achados | Where-Object nivel -eq 'FALTA').Count, @($achados | Where-Object nivel -eq 'ATENCAO').Count, (Join-Path $Saida 'diagnostico.md'))
