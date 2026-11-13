<!-- GERADO por tools/nucleo/agenda.py a partir de data/implantacao-rapida.json. Edite o JSON. -->
# Trilha rápida: o setup funcionando e as 3 empresas prontas para vender

O setup funcionando e as 3 empresas prontas para vender, no menor caminho. O resto do roteiro continua valendo, mas espera esta trilha terminar.

**Como usar:** Uma sessão por dia (ou duas no fim de semana). Os scripts rodam sozinhos: enquanto rodam, você faz os passos marcados como 'em paralelo'. Terminou um passo: just feito ID.

São 7 sessões, cerca de 17 horas no total. Antes do Ubuntu existir (sessões 1 e 2), leia por esta página; depois, `just rapido` no Ubuntu do WSL mostra só o que falta.

## Sessão 1 · Base no Windows e o cofre (cerca de 2h30)

Comece o backup-inicial e o windows-update (rodam sozinhos, em janelas separadas do PowerShell) e, enquanto isso, crie o cofre e troque a senha do Google.

**Rode (segue sozinho)**

- [ ] `diag-pasta` · Baixar o dev-setup do GitHub para C:\Users\SEU_USUARIO\dev-setup (5 min). Pronto quando: Pasta C:\Users\SEU_USUARIO\dev-setup com RODAR-DIAGNOSTICO.cmd e as pastas scripts, data e docs logo dentro dela (o Git pede o login do GitHub no navegador uma vez)
  - PowerShell do Windows (`PS C:\>`): `if (Test-Path $HOME\dev-setup) { Write-Host "Ja existe $HOME\dev-setup" } else { winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements; & "$env:ProgramFiles\Git\cmd\git.exe" clone https://github.com/AlanMateus17/dev-setup.git "$HOME\dev-setup" }`
- [ ] `diag-rodar` · Rodar o diagnóstico: botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador (10 min). Pronto quando: Pasta diagnostico-AAAAMMDD com diagnostico.md: o que você tem e em que passo cada pendência se resolve
  - PowerShell do Windows (`PS C:\>`): `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\diagnostico.ps1`
- [ ] `backup-inicial` · Copiar documentos, fotos e projetos para um disco externo ou pendrive (60 min). Pronto quando: Mensagem "Copiado: ... 0 pasta(s) com erro" e alguns arquivos abertos no disco para conferir. Troque E: pela letra certa (Get-Volume); a partição RUFUS_BOOT de um pendrive de instalação tem 0 GB e não serve
  - PowerShell do Windows (`PS C:\>`): `$d = 'E:'; if (-not (Test-Path "$d\")) { Write-Host "Nao existe o disco $d (veja a letra com Get-Volume)" } else { $pastas = @('Desktop','Documents','Pictures','Videos','Music','OneDrive','dev','dev-setup','source','Downloads') | Where-Object { Test-Path "$HOME\$_" }; $precisa = (Get-ChildItem -Path ($pastas | ForEach-Object { "$HOME\$_" }) -Recurse -File -Force -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum; $livre = (Get-PSDrive $d.TrimEnd(':')).Free; if ($precisa -gt $livre) { Write-Host ("Nao cabe: precisa {0:N1} GB e $d tem {1:N1} GB livres. Tire 'Downloads' da lista ou use um disco maior." -f ($precisa/1GB), ($livre/1GB)) } else { $log = "$HOME\backup-inicial.log"; Remove-Item $log -ErrorAction SilentlyContinue; $falhas = 0; foreach ($p in $pastas) { robocopy "$HOME\$p" "$d\backup-inicial\$p" /E /R:1 /W:1 /XJ /XF ".????????-????-????-????-????????????" /NFL /NDL /NP /NJH "/LOG+:$log"; if ($LASTEXITCODE -ge 8) { $falhas++; Write-Host "Falhou: $p (veja ERRO em $log)" } }; Write-Host ("Copiado: {0:N1} GB para $d\backup-inicial, {1} pasta(s) com erro" -f ($precisa/1GB), $falhas) } }`
- [ ] `windows-update` · Atualizar o Windows, os drivers e o NitroSense (40 min). Pronto quando: Windows Update sem pendências
  - PowerShell do Windows (`PS C:\>`): `winget upgrade --all --accept-source-agreements --accept-package-agreements; Install-PackageProvider NuGet -Force -Scope CurrentUser | Out-Null; Install-Module PSWindowsUpdate -Force -Scope CurrentUser; Import-Module PSWindowsUpdate; Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -IgnoreReboot`

**Em paralelo, enquanto o script roda**

- [ ] `keepass` · Instalar o KeePassXC e criar o cofre com uma senha mestra de 6 palavras (30 min). Pronto quando: Arquivo Cofre.kdbx em Documentos\Cofre abre com a senha mestra; bloqueio automático depois de 5 minutos parado
  - PowerShell do Windows (`PS C:\>`): `winget install --id KeePassXCTeam.KeePassXC -e; New-Item -ItemType Directory -Force "$HOME\Documents\Cofre" | Out-Null; & "$env:ProgramFiles\KeePassXC\keepassxc-cli.exe" db-create --set-password "$HOME\Documents\Cofre\Cofre.kdbx"`
- [ ] `senhas-kit` · Montar o kit de emergência em papel (15 min). Pronto quando: Envelope guardado em casa (fora da carteira e da mochila) com a senha mestra, a senha do e-mail principal e os códigos de recuperação do Google
  - Fora do terminal: Papel e caneta, de propósito: o kit não pode depender do computador.
- [ ] `senhas-email` · Recuperar e trocar primeiro a senha do e-mail principal (conta Google) (30 min). Pronto quando: Senha nova gerada no KeePassXC; verificação em duas etapas pelo app; telefone e e-mail de recuperação conferidos; códigos de backup salvos no cofre; aparelhos desconhecidos desconectados
  - PowerShell do Windows (`PS C:\>`): `Start-Process 'https://myaccount.google.com/security-checkup'`
  - Fora do terminal: O comando abre a página; trocar a senha e ligar a verificação é no site do Google, com o celular.
- [ ] `github-2fa` · Instalar o app de 2FA no celular e ligar a verificação em duas etapas no GitHub, Google e e-mail (30 min). Pronto quando: 2FA ativo nas três contas, com códigos de recuperação impressos
  - Fora do terminal: Cada site liga a verificação em duas etapas na própria página, lendo o QR code com o celular; nenhum deixa fazer isso por terminal.

## Sessão 2 · Instalador do Windows e o Ubuntu (cerca de 2h00)

O win-aplicar leva cerca de 1 hora e não precisa de você. Nesse tempo, troque só as 4 senhas que a trilha usa (Google, GitHub, gov.br e banco); as outras ficam para o passo senhas-resto, 5 por semana.

**Rode (segue sozinho)**

- [ ] `win-aplicar` · Instalar programas, WSL2 com Ubuntu (instala o 24.04 só se não houver nenhum) e .wslconfig (PowerShell como Administrador) (60 min). Pronto quando: Termina com 'Pronto' e sem ERRO; reinicie o Windows
  - PowerShell do Windows (`PS C:\>`): `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1 -Aplicar`
- [ ] `vscode-ext` · Instalar as extensões do VS Code (WSL, Claude Code, .NET, LaTeX, revisão em português) (10 min). Pronto quando: Termina com 'Pronto'
  - PowerShell do Windows (`PS C:\>`): `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\extensoes-vscode.ps1 -Aplicar`
- [ ] `win-verificar` · Conferir o Windows (5 min). Pronto quando: verificar.ps1 termina com 'Windows pronto'
  - PowerShell do Windows (`PS C:\>`): `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\verificar.ps1`

**Em paralelo, enquanto o script roda**

- [ ] `senhas-criticas` · Trocar as senhas críticas, uma por vez: gov.br, bancos, Microsoft, celular, WhatsApp, GitHub, Meta, Mercado Livre e plataformas de venda (120 min). Pronto quando: Cada conta crítica com senha nova gerada no cofre, verificação em duas etapas ligada e códigos de backup salvos na entrada dela
  - Fora do terminal: Cada serviço troca a senha no próprio site ou app; o cofre gera a senha (keepassxc-cli generate -L 24) e você cola lá.
- [ ] `senhas-celular` · Levar o cofre para o celular (KeePassDX no Android ou KeePassium no iPhone) (20 min). Pronto quando: O cofre abre no celular com a senha mestra; uma senha criada no notebook aparece no celular
  - Fora do terminal: Instalar e abrir o app é no celular.
- [ ] `cripto` · Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC (15 min). Pronto quando: verificar.ps1 como Administrador mostra criptografia OK
  - PowerShell do Windows (`PS C:\>`): `manage-bde -status C:; manage-bde -protectors -get C:`

**Depois**

- [ ] `ubuntu-usuario` · Abrir o Ubuntu do WSL e criar (ou confirmar) seu usuário Linux (10 min). Pronto quando: Prompt do Ubuntu aberto
  - PowerShell do Windows (`PS C:\>`): `wsl -l -v; wsl -d Ubuntu`
- [ ] `docker-wsl` · Ligar o Docker Desktop dentro do Ubuntu (integração com o WSL) (5 min). Pronto quando: 'docker run hello-world' funciona dentro do Ubuntu
  - PowerShell do Windows (`PS C:\>`): `$f="$env:APPDATA\Docker\settings-store.json"; if (-not (Test-Path $f)) { Write-Host "Nao achei $f : abra o Docker Desktop uma vez e rode de novo" } else { Copy-Item $f "$f.bak" -Force; $j=Get-Content $f -Raw | ConvertFrom-Json; $j | Add-Member -Force NoteProperty EnableIntegrationWithDefaultWslDistro $true; $j | Add-Member -Force NoteProperty IntegratedWslDistros @('Ubuntu'); [IO.File]::WriteAllText($f, ($j | ConvertTo-Json -Depth 10)); Get-Process 'Docker Desktop' -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep 3; Start-Process "$env:ProgramFiles\Docker\Docker\Docker Desktop.exe"; $i=0; do { Start-Sleep 5; $i++; docker info *> $null } until ($LASTEXITCODE -eq 0 -or $i -ge 36); if ($LASTEXITCODE -eq 0) { Write-Host "Docker pronto com o Ubuntu ligado" } else { Write-Host "Docker nao respondeu em 3 min: veja a janela dele" } }`
- [ ] `clonar` · Copiar o dev-setup do Windows para ~/dev/dev-setup (com o GitHub como origem) (5 min). Pronto quando: Pasta ~/dev/dev-setup com os arquivos
  - Ubuntu do WSL: `mkdir -p ~/dev && { [ -d ~/dev/dev-setup ] || git clone "$(wslpath "$(cmd.exe /c 'echo %USERPROFILE%' 2>/dev/null | tr -d '\r')")/dev-setup" ~/dev/dev-setup; } && git -C ~/dev/dev-setup remote set-url origin git@github.com:AlanMateus17/dev-setup.git && ls ~/dev/dev-setup`
- [ ] `wsl-reiniciar` · Reiniciar o WSL para o systemd valer (PowerShell) (2 min). Pronto quando: Ubuntu reabre normalmente
  - PowerShell do Windows (`PS C:\>`): `wsl --shutdown`

## Sessão 3 · Linux, GitHub e Claude Code (cerca de 2h00)

Rode o comando do passo bootstrap no Ubuntu do WSL (o just ainda não existe antes dele): você digita a senha do sudo no começo e ele segue sozinho por cerca de 40 minutos. Nesse tempo, organize o app do Claude e confira os conectores. Depois do bootstrap, just rapido mostra o resto.

**Rode (segue sozinho)**

- [ ] `bootstrap` · Rodar o preparador do Linux (40 min). Pronto quando: Termina com 'Pronto' e sem ERRO
  - Ubuntu do WSL: `bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email SEU_EMAIL --com-whisper`

**Em paralelo, enquanto o script roda**

- [ ] `claude-app` · Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas (30 min). Pronto quando: Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
  - Fora do terminal: Projects, memória e tarefas agendadas ficam no app do Claude.
- [ ] `conectores` · Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ (30 min). Pronto quando: Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
  - Fora do terminal: Conectores se ligam e desligam nas configurações do app do Claude.

**Depois**

- [ ] `gh-login` · Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura (10 min). Pronto quando: 'gh auth status' mostra sua conta
  - Ubuntu do WSL: `gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing`
- [ ] `repo-criar` · Ligar o repositório ao GitHub (cria só se ainda não existir) (5 min). Pronto quando: Repositório AlanMateus17/dev-setup privado com o código
  - Ubuntu do WSL: `cd ~/dev/dev-setup && if gh repo view AlanMateus17/dev-setup >/dev/null 2>&1; then git pull --ff-only && echo "Ja existe no GitHub: so atualizei"; else git add -A && git commit -qm "chore: setup inicial"; gh repo create AlanMateus17/dev-setup --private --source . --push; fi`
- [ ] `ci-verde` · Conferir o CI no GitHub (5 min). Pronto quando: Última execução do workflow 'docs' com sucesso
  - Ubuntu do WSL: `gh run list --limit 1`
- [ ] `claude-login` · Entrar no Claude Code (5 min). Pronto quando: 'claude doctor' sem erros
  - Ubuntu do WSL: `claude`
- [ ] `obsidian-git` · Trazer o seu vault (Portfolio-AMS-Obsidian-Vault) para ~/dev/notas, ligar o Obsidian Git e espelhar o setup na pasta 11 (20 min). Pronto quando: Vault aberto no Obsidian a partir de ~/dev/notas; a pasta 11-setup-dev-setup igual ao repositório; notas vão sozinhas para o GitHub a cada 10 minutos
  - Ubuntu do WSL: `bash scripts/wsl/vault.sh && just vault-espelho`
- [ ] `restic-local` · Criar o repositório restic no disco externo e o primeiro backup (30 min). Pronto quando: 'restic snapshots' lista o backup
  - Ubuntu do WSL: `restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech`
- [ ] `restaurar` · Testar a restauração de uma pasta (15 min). Pronto quando: Arquivo restaurado abre normalmente
  - Ubuntu do WSL: `restic -r /mnt/d/backup-restic restore latest --target /tmp/teste-restauracao --include "$HOME/dev/dev-setup/README.md" && find /tmp/teste-restauracao -name README.md`

## Sessão 4 · As decisões da empresa de software (cerca de 2h30)

Sessão só de decidir, sem instalar nada. Cada decisão já tem os fatos no roteiro (just decisoes software). Na dúvida, aceite a recomendação: dá para mudar depois do 1º cliente.

**Depois**

- [ ] `ks-kit` · Ler o kit e definir os preços dos 3 pacotes (30 min). Pronto quando: Preços de criação e mensalidade definidos pela hora mínima
  - Fora do terminal: Decisão sua; o kit está em docs/operacao/kit-sites.md.
- [ ] `sw-ofertas` · Decidir as 3 primeiras ofertas e o preço público de cada uma (60 min). Pronto quando: 3 pacotes com preço, prazo e o que entra, publicados no site da empresa
  - Fora do terminal: Decisão sua, com base no kit de sites e na sua hora mínima. O setup calcula o lucro por venda (passo calc-regras) e o tempo de cada pacote.
- [ ] `sw-contrato` · Revisar o contrato padrão e decidir se passa por um advogado antes do 1º cliente (45 min). Pronto quando: Contrato padrão aprovado por você (e pelo advogado, se escolher), pronto no Documenso
  - Ubuntu do WSL: `cd ~/dev/dev-setup && less docs/operacao/contrato-sites-modelo.md`
- [ ] `sw-hospedagem` · Decidir onde roda cada tipo de cliente: Hostinger, Coolify na VPS dele ou Kamal (20 min). Pronto quando: Regra escrita: site simples na Hostinger, cliente que quer painel no Coolify, sistema no Kamal
  - Ubuntu do WSL: `cd ~/dev/dev-setup && just triagem "hospedar o site de um cliente" --nucleo nao`
- [ ] `sw-marca` · Decidir o nome comercial e buscar a marca no INPI (classe 42) antes de investir nela (30 min). Pronto quando: Busca feita sem conflito; nome confirmado ou trocado
  - Fora do terminal: A busca é no site do INPI (busca de marcas, classe 42: serviços de software). O pedido pode ser no seu CPF; o passo do INPI já está no roteiro.
- [ ] `sw-autonomia` · Decidir o que a empresa faz sem você e o que para no seu ok (30 min). Pronto quando: Tabela de autonomia da empresa revisada por você e gravada no núcleo
  - Ubuntu do WSL: `cd ~/dev/dev-setup && just lembrar "Autonomia da Grupo AMtech Digital: (escreva o que muda em relação ao docs/nucleo/README.md)" padrao`
- [ ] `inst-preco` · Decidir o preço do mini-curso de Lógica e da pré-venda (20 min). Pronto quando: Preço cheio e preço de pré-venda escritos em data/marcas/instituto.json
  - Fora do terminal: Decisão sua. O setup calcula o lucro por venda depois da taxa da plataforma e do carnê-leão (passo calc-regras).
- [ ] `inst-nome` · Confirmar a marca 'Instituto AMS Silva' e buscar no INPI (classe 41, educação) antes de investir nela (30 min). Pronto quando: Busca feita sem conflito; nome confirmado ou trocado em data/marcas/instituto.json
  - Fora do terminal: Busca de marcas no site do INPI, classe 41 (educação). O setup usava 'Instituto AMS'; o nome que você passou a usar é 'Instituto AMS Silva'.

## Sessão 5 · Contas que vendem (cerca de 2h30)

Do contador, só marque a consulta nesta sessão; ela acontece depois. As senhas novas vão direto para o cofre.

**Depois**

- [ ] `dominio` · Registrar o domínio no Registro.br e apontar para a Cloudflare (30 min). Pronto quando: DNS ativo na Cloudflare
  - Fora do terminal: Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] `email-prof` · Criar o e-mail profissional do domínio (30 min). Pronto quando: Envia e recebe
  - Fora do terminal: Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] `banco` · Abrir a conta bancária separada para o que você vende (no CPF) (30 min). Pronto quando: Conta aberta; todas as plataformas vão pagar nela
  - Fora do terminal: Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] `agenda` · Criar a agenda online no Cal.com com pagamento para as aulas particulares (30 min). Pronto quando: Horário de teste marcado e cobrado
  - Fora do terminal: Cadastro no site ou app do serviço, com documento e confirmação no celular; nenhum deles deixa criar conta por terminal.
- [ ] `crm` · Criar o CRM em planilha com origem e consentimento de cada cliente (30 min). Pronto quando: Planilha com colunas de oferta, origem, consentimento LGPD e próximo passo
  - Ubuntu do WSL: `cd ~/dev/dev-setup && claude "Passo crm do roteiro: Criar o CRM em planilha com origem e consentimento de cada cliente"`
- [ ] `hostinger` · Separar na Hostinger o espaço dos sites de clientes (30 min). Pronto quando: Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
  - Ubuntu do WSL: `cd ~/dev/dev-setup && claude "Passo hostinger do roteiro: Separar na Hostinger o espaço dos sites de clientes"`
- [ ] `contador` · Fazer a consulta com o contador: carnê-leão e a partir de que renda abrir CNPJ (60 min). Pronto quando: Regras do carnê-leão anotadas e o valor de virada para o CNPJ definido
  - Fora do terminal: Órgão público, contador ou entidade: feito no site do governo ou com atendimento.

## Sessão 6 · Os 3 sites no ar (cerca de 2h30)

just site amtech, just site instituto e just site editora; just site MARCA --checar lista o que falta em cada um. Só publique quando o checador não apontar nada.

**Rode (segue sozinho)**

- [ ] `sw-site` · Gerar o site do Grupo AMtech Digital e publicar quando o checador não apontar pendências (180 min). Pronto quando: just site amtech --checar sem pendências e o site no ar no seu domínio
  - Ubuntu do WSL: `cd ~/dev/dev-setup && just site amtech && just site amtech --checar`
- [ ] `ks-conferir` · Conferir o site e gerar o laudo antes de entregar (10 min). Pronto quando: Nota 80 ou mais no laudo
  - Ubuntu do WSL: `cd ~/dev/dev-setup && python3 tools/kitsites/conferir.py https://ENDERECO-DO-SITE --saida ~/laudo-site.md`

**Depois**

- [ ] `ag-deploy` · Ligar prévia no Cloudflare Pages e deploy por push na Hostinger (20 min). Pronto quando: Merge na main publica o site; cada PR tem link de prévia
  - Fora do terminal: Peça ao Claude com a skill deploy-to-hosting depois do passo ag-hostinger-mcp.
- [ ] `site-grupo` · Publicar o site do Grupo AMtech e o Catálogo do HTML (90 min). Pronto quando: Os dois sites no ar com domínio e HTTPS
  - Ubuntu do WSL: `cd ~/dev/dev-setup && claude "Passo site-grupo do roteiro: Publicar o site do Grupo AMtech e o Catálogo do HTML"`

## Sessão 7 · Primeiro cliente (cerca de 3h00)

Abordagem uma por uma, nunca disparo em massa. O primeiro site pago fecha o critério do trimestre 1.

**Depois**

- [ ] `sw-primeiros` · Escolher 5 negócios da lista do prospector e aprovar a abordagem de cada um (45 min). Pronto quando: 5 abordagens aprovadas e enviadas por você
  - Fora do terminal: O prospector monta a lista com dados públicos e rascunha a mensagem; quem escolhe e envia é você. Nunca disparo em massa.
- [ ] `ar-sites` · Oferecer site com manutenção mensal a 5 comércios (120 min). Pronto quando: 5 ofertas feitas e respostas anotadas no CRM
  - Fora do terminal: Venda é conversa com o cliente; o setup prepara a proposta e o contrato.
- [ ] `ks-primeiro` · Montar o primeiro site com a ficha e o prompt do tipo de negócio (180 min). Pronto quando: Site no ar no Website Builder ou no Horizons
  - Fora do terminal: A montagem é no editor da Hostinger, no navegador; o prompt pronto está no kit.

## Fica para depois da trilha

- O resto das senhas (senhas-resto: 5 por semana) e os extras do KeePassXC
- Acervo, stack de automação (n8n, Grafana), RAG e MCPs extras
- Núcleo autônomo, Operação 24 horas, Escola Akita e as melhorias do Professor
- Mini-curso gravado (fase 17): começa depois do 1º cliente de site, no bloco de sábado
