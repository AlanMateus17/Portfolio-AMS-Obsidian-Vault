@echo off
rem Diagnostico do notebook - SOMENTE LEITURA: nao instala, nao apaga, nao altera nada.
rem Botao direito neste arquivo > Executar como administrador.
rem (Com dois cliques normais tambem roda, mas sem ler Secure Boot, TPM, BitLocker e bateria.)
cd /d "%~dp0"
if not exist "%~dp0scripts\windows\diagnostico.ps1" (
  echo Este arquivo precisa ficar na pasta principal do dev-setup, junto da pasta scripts.
  pause
  exit /b 1
)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\windows\diagnostico.ps1"
echo.
echo O relatorio esta na pasta diagnostico-AAAAMMDD, dentro de:
echo %~dp0
pause
