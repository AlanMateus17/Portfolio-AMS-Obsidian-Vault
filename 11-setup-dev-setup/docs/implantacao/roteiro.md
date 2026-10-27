<!-- Arquivo GERADO por tools/implantacao/gerar.py a partir de data/implantacao.json. Não edite à mão. -->

# Roteiro de implantação

[← Implantação](README.md)

34 fases, 253 passos, cerca de **1097 h 15 min** de trabalho no total. Cada passo tem um critério de pronto que dá para conferir. A versão para marcar o progresso é o [`acompanhamento.html`](acompanhamento.html) (e o artefato Implantação AMtech).

Legenda de quem faz: **Você** (só você pode: contas, senhas, decisões), **Script** (você roda o comando), **Claude com você** (o Claude faz pelo conector ou pelo Claude Code, com a sua aprovação).

**Todo o planejamento está aqui:** os 326 blocos do [mapa do setup](../mapa.html), de todas as 23 camadas, entram em algum passo, com a data ou o gatilho de quando, e cada uma das 47 ofertas do portfólio tem o passo em que entra à venda. Nada fica de fora; o CI falha se um bloco ou uma oferta nova não tiver passo ([quando entra cada bloco](#quando-entra-cada-bloco)).

**Dá para fazer hoje:** 168 dos 253 passos (172 h 35 min) só precisam do notebook e de contas grátis. Os outros dizem o que falta: comprar algo, pagar um serviço, ter um conteúdo seu pronto ou esperar o gatilho da fase.

| Fase | Quando | Passos | Tempo |
|---|---|---:|---:|
| [0 · Diagnóstico: o que você já tem](#f0) | Antes de tudo · semana 1 (out/2026) | 6 | 1 h 40 min |
| [1 · Preparar](#f1) | Semana 1 · out/2026 | 4 | 2 h 40 min |
| [2 · Senhas: recuperar, trocar e guardar](#f2) | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 | 12 | 6 h 20 min |
| [3 · Windows](#f3) | Semana 1 · out/2026 | 9 | 2 h 30 min |
| [4 · Linux (WSL2)](#f4) | Semana 2 · nov/2026 | 10 | 2 h 22 min |
| [5 · GitHub e CI](#f5) | Semana 2 · nov/2026 | 5 | 55 min |
| [6 · Agentes de IA](#f6) | Semana 2 · nov/2026 | 7 | 2 h 27 min |
| [7 · Backup e segurança](#f7) | Semana 3 · nov/2026 | 4 | 1 h 45 min |
| [8 · Acervo: tudo o que você já tem](#f8) | Semanas 3 e 4 · nov/2026 | 7 | 4 h 55 min |
| [9 · Claude e assistentes](#f9) | Semana 4 · nov/2026 | 4 | 1 h 45 min |
| [10 · Automação e medição](#f10) | Semana 4 · nov/2026 | 8 | 1 h 42 min |
| [11 · Pipeline de conteúdo](#f11) | Semana 5 · nov/2026 | 6 | 1 h 24 min |
| [12 · Estúdio de conteúdo](#f12) | Semana 5 · dez/2026 | 5 | 3 h 20 min |
| [13 · Contas, canais e sites](#f13) | Semanas 6 e 7 · dez/2026 | 13 | 9 h 00 min |
| [14 · Vendas e finanças no CPF](#f14) | Semanas 8 a 10 · dez/2026 a jan/2027 | 20 | 12 h 10 min |
| [15 · Vendas medidas](#f15) | Semana 11 · jan/2027 | 4 | 2 h 40 min |
| [16 · Teste do núcleo](#f16) | Semana 11 · jan/2027 | 4 | 1 h 00 min |
| [17 · Primeira venda: o mini-curso no ar](#f17) | Semanas 12 a 15 · jan a fev/2027 | 8 | 22 h 30 min |
| [18 · Base dos sistemas AM](#f18) | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 | 8 | 7 h 40 min |
| [19 · Nuvem e deploy](#f19) | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) | 7 | 6 h 15 min |
| [20 · Editora](#f20) | Quando o capítulo 1 estiver pronto · **gatilho:** O capítulo 1 e o seu modelo de criação prontos | 11 | 18 h 30 min |
| [21 · Dados, IA e pendrives](#f21) | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) | 12 | 16 h 20 min |
| [22 · Mais ofertas, uma por vez](#f22) | Fev a dez/2027, uma oferta por vez · **gatilho:** A primeira venda do mini-curso aconteceu | 20 | 127 h 30 min |
| [23 · Marketing pago e crescimento](#f23) | A partir de fev/2027 · **gatilho:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar | 10 | 37 h 30 min |
| [24 · Linux nativo e laboratório completo](#f24) | 2027, conforme cada compra | 6 | 18 h 00 min |
| [25 · IA dentro dos sistemas AM](#f25) | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 | 1 | 8 h 00 min |
| [26 · Sistemas AM à venda](#f26) | 2027 · **gatilho:** O primeiro sistema AM pronto e testado com um cliente | 5 | 120 h 00 min |
| [27 · CNPJ e formalização](#f27) | Quando a renda pedir · **gatilho:** A renda passou do valor de virada definido com o contador | 4 | 13 h 00 min |
| [28 · Agentes do grupo](#f28) | Junto com o primeiro CNPJ · **gatilho:** Clientes e vendas recorrentes | 7 | 18 h 00 min |
| [29 · Editora: depois do primeiro livro](#f29) | Depois do primeiro livro · **gatilho:** O primeiro livro publicado | 5 | 56 h 00 min |
| [30 · Distribuído, plataforma e segunda nuvem](#f30) | 2028 | 6 | 69 h 00 min |
| [31 · Infraestrutura própria](#f31) | 2028, quando o grupo pedir | 3 | 17 h 00 min |
| [32 · Negócios do grupo em Barbacena](#f32) | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano · **gatilho:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta | 8 | 482 h 00 min |
| [33 · Estudo contínuo](#f33) | Contínuo, desde a semana 2 | 4 | 1 h 25 min |

<a id="f0"></a>

## 0 · Diagnóstico: o que você já tem

Saber exatamente o que o notebook já tem de hardware, segurança, programas, contas e documentos, e começar o roteiro a partir daí.

**Quando:** Antes de tudo · semana 1 (out/2026)

### 0.1 Extrair o dev-setup.zip e deixar a pasta em C:\Users\SEU_USUARIO\dev-setup

**Você** · 5 min

- [ ] **Pronto quando:** Pasta C:\Users\SEU_USUARIO\dev-setup com RODAR-DIAGNOSTICO.cmd e as pastas scripts, data e docs logo dentro dela; nenhuma outra cópia em Downloads
- Botão direito no zip > Extrair tudo. O Windows costuma criar dev-setup\dev-setup: recorte a pasta de dentro (a que tem a pasta scripts) e cole em C:\Users\SEU_USUARIO, a pasta com o seu nome. Apague as cópias que sobraram em Downloads, como "dev-setup (1)". Todos os comandos do Windows deste roteiro apontam para esse lugar, então funcionam de qualquer pasta, até da System32 onde o PowerShell de Administrador abre.

### 0.2 Rodar o diagnóstico: botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador

**Script** · 10 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\diagnostico.ps1
```

- [ ] **Pronto quando:** Pasta diagnostico-AAAAMMDD com diagnostico.md: o que você tem e em que passo cada pendência se resolve
- Somente leitura: não instala nem apaga nada. Em vez do comando, pode clicar com o botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador. Se o Windows avisar "O Windows protegeu o computador", clique em Mais informações > Executar assim mesmo. Mostra modelo, processador, memória e slots livres, placa de vídeo, discos e saúde, espaço livre, bateria, monitores, Secure Boot, TPM, criptografia, Defender, programas do setup que já tem e que faltam, WSL, Docker, modelos do Ollama e extensões do VS Code.
- Implanta: Diagnóstico do notebook · Acer Nitro (32 GB, GTX 1650)

### 0.3 Rodar o inventário de espaço: pastas e arquivos que mais ocupam, programas que iniciam com o Windows

**Script** · 15 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\inventario.ps1
```

- [ ] **Pronto quando:** Pasta inventario-AAAAMMDD gerada; você decidiu o que desinstalar ou mover
- Implanta: Windows 11 Home

### 0.4 Listar as contas e assinaturas que você já tem, sem anotar senha

**Você** · 30 min

- [ ] **Pronto quando:** Nota no Obsidian (ou papel) com quais contas do setup já existem e quais assinaturas você paga
- A lista de contas do setup está no ecossistema, em Contas que você precisa ter. Senha nunca vai para nota: só para o KeePassXC, no passo dele.
- Implanta: Windows 11 Home

### 0.5 Ver quantos documentos você já tem (só a contagem, sem abrir)

**Você** · 10 min

- [ ] **Pronto quando:** Você sabe por alto onde estão as aulas, apostilas, provas e projetos (Drive, notebook, pendrives)
- A organização de verdade vem na fase Acervo, depois do backup.
- Implanta: Google Drive (seus documentos)

### 0.6 Mandar a pasta do diagnóstico para o Claude e ajustar o roteiro

**Claude com você** · 30 min

- [ ] **Pronto quando:** Passos que você já cumpre marcados no acompanhamento; compras e pendências confirmadas
- Anexe na conversa os dois arquivos da pasta C:\Users\SEU_USUARIO\dev-setup\diagnostico-AAAAMMDD: diagnostico.md e diagnostico.json. Eles não têm senha nem documento seu, só hardware e programas.
- Implanta: Roteiro de implantação

<a id="f1"></a>

## 1 · Preparar

Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina.

**Quando:** Semana 1 · out/2026

### 1.1 Copiar documentos, fotos e projetos para um disco externo

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Disco externo com a cópia conferida (abra alguns arquivos)
- Implanta: Disco externo

### 1.2 Montar a mesa: nobreak, base com cooler, 2º monitor, disco e SSD externos, kits de robótica

**Você** · 30 min

- [ ] **Pronto quando:** Notebook no nobreak e na base, 2º monitor funcionando, disco e SSD externos reconhecidos
- O que ainda não comprou fica anotado e não trava as próximas fases. O nobreak vem primeiro: protege o notebook e o backup de queda de energia.
- **Precisa:** comprar algo
- Implanta: Acer Nitro (32 GB, GTX 1650) · Nobreak · Base com cooler · 2º monitor · Disco externo · SSD externo (USB-C 10 Gbps) · Celular · Arduino · ESP32 · Pi

### 1.3 Atualizar o Windows, os drivers e o NitroSense

**Você** · 40 min

- [ ] **Pronto quando:** Windows Update sem pendências
- Implanta: Windows 11 Home · NitroSense + drivers AMD e NVIDIA

### 1.4 Instalar o app de 2FA no celular e ligar a verificação em duas etapas no GitHub, Google e e-mail

**Você** · 30 min

- [ ] **Pronto quando:** 2FA ativo nas três contas, com códigos de recuperação impressos
- Implanta: App 2FA (celular)

<a id="f2"></a>

## 2 · Senhas: recuperar, trocar e guardar

Toda conta com senha única guardada no KeePassXC, verificação em duas etapas nas críticas e um jeito de recuperar tudo se perder o notebook ou o celular.

**Quando:** Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026

### 2.1 Instalar o KeePassXC e criar o cofre com uma senha mestra de 6 palavras

**Você** · 30 min

```powershell
winget install --id KeePassXCTeam.KeePassXC -e
```

- [ ] **Pronto quando:** Arquivo Cofre.kdbx em Documentos\Cofre abre com a senha mestra; bloqueio automático depois de 5 minutos parado
- Gere a senha mestra no próprio KeePassXC (Ferramentas > Gerador de senhas > Frase-senha, 6 palavras) e decore nos primeiros dias. Ela é a única senha que você precisa saber de cor e não pode ser usada em nenhum outro lugar. Não use arquivo-chave: se perder o arquivo, perde o cofre. Ninguém, nem o Claude, precisa ver o cofre ou a senha mestra.
- Implanta: KeePassXC

### 2.2 Montar o kit de emergência em papel

**Você** · 15 min

- [ ] **Pronto quando:** Envelope guardado em casa (fora da carteira e da mochila) com a senha mestra, a senha do e-mail principal e os códigos de recuperação do Google
- É o que salva você se esquecer a senha mestra ou perder o notebook e o celular juntos. Papel, não foto: foto vai para a nuvem do celular.
- Implanta: KeePassXC

### 2.3 Recuperar e trocar primeiro a senha do e-mail principal (conta Google)

**Você** · 30 min

- [ ] **Pronto quando:** Senha nova gerada no KeePassXC; verificação em duas etapas pelo app; telefone e e-mail de recuperação conferidos; códigos de backup salvos no cofre; aparelhos desconhecidos desconectados
- Vem antes de tudo porque todo 'Esqueci minha senha' manda o link para esse e-mail: quem controla o e-mail controla as outras contas. Faça em myaccount.google.com > Segurança e rode a Verificação de segurança no fim. Se não lembrar a senha atual, use g.co/recover no notebook e na rede de casa, onde o Google já reconhece você.
- Implanta: KeePassXC · App 2FA (celular) · Conector Google (Gmail, Drive…)

### 2.4 Trazer para o cofre as senhas salvas no Chrome, no Edge e no Google

**Você** · 30 min

- [ ] **Pronto quando:** Senhas importadas no KeePassXC (Banco de dados > Importar > CSV); o arquivo CSV apagado de vez; navegadores sem salvar senha
- Exporte em chrome://password-manager/settings, edge://wallet/passwords e passwords.google.com. O CSV é a lista de todas as suas senhas em texto puro: importe na hora, apague com Shift+Delete e não deixe em Downloads, no Drive, no e-mail nem no repositório. Não mande esse arquivo para ninguém, nem para o Claude. Só depois de conferir o cofre apague as senhas dos navegadores e desligue 'Oferecer para salvar senhas'.
- Implanta: KeePassXC · Navegador + Claude in Chrome

### 2.5 Ver no KeePassXC quais senhas são fracas, repetidas ou já vazaram

**Você** · 15 min

- [ ] **Pronto quando:** Lista, em ordem, das contas para trocar (Banco de dados > Relatórios > Integridade e Have I Been Pwned)
- A checagem de vazamento manda só um pedaço do resumo da senha, nunca a senha. Senha que aparece como vazada vai para o topo da lista.
- Implanta: KeePassXC

### 2.6 Trocar as senhas críticas, uma por vez: gov.br, bancos, Microsoft, celular, WhatsApp, GitHub, Meta, Mercado Livre e plataformas de venda

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Cada conta crítica com senha nova gerada no cofre, verificação em duas etapas ligada e códigos de backup salvos na entrada dela
- Para cada uma: gere a senha no KeePassXC (20 caracteres ou mais), troque no site, salve no cofre antes de fechar a página e saia de todos os outros aparelhos. Banco, troque pelo app oficial. No WhatsApp é o PIN da confirmação em duas etapas. A senha de 4 dígitos do cartão não vai para o cofre: essa você decora.
- Implanta: KeePassXC · App 2FA (celular) · gov.br (prata ou ouro) · Conta bancária separada (CPF) · GitHub

### 2.7 Recuperar as contas cuja senha você esqueceu e fechar as que não usa mais

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Toda conta da sua lista de contas está no cofre, foi recuperada ou foi excluída
- Use 'Esqueci minha senha' com o e-mail já protegido. Se o e-mail ou o telefone de recuperação forem antigos, cada serviço tem um formulário próprio (Meta: 'Precisa de ajuda?' na tela de login; gov.br: pelo app com reconhecimento facial ou pelo banco). Conta parada que guarda dado seu é risco: exclua.
- Implanta: KeePassXC

### 2.8 Levar o cofre para o celular (KeePassDX no Android ou KeePassium no iPhone)

**Você** · 20 min

- [ ] **Pronto quando:** O cofre abre no celular com a senha mestra; uma senha criada no notebook aparece no celular
- Sincronize o arquivo Cofre.kdbx pelo Syncthing, ou pelo Drive (o arquivo vai criptografado). Edite num aparelho de cada vez para não criar cópias em conflito.
- Implanta: KeePassXC · Celular · Syncthing

### 2.9 Ligar o KeePassXC-Browser para preencher senha e código no navegador

**Você** · 15 min

- [ ] **Pronto quando:** No login de teste, o navegador preenche a senha a partir do cofre
- No KeePassXC: Configurações > Integração com navegador, marque o seu navegador e instale a extensão KeePassXC-Browser.
- Implanta: KeePassXC · Navegador + Claude in Chrome

### 2.10 Pôr o cofre no backup e testar abrir a cópia

**Você** · 15 min

- [ ] **Pronto quando:** Cópia do Cofre.kdbx no disco externo abre com a senha mestra; quando o restic entrar, a pasta Documentos\Cofre está no backup diário
- No WSL o caminho é /mnt/c/Users/SEU_USUARIO/Documents/Cofre: acrescente ao comando do restic no passo do backup.
- Implanta: KeePassXC · Disco externo · Backup 3-2-1

### 2.11 Trocar o resto aos poucos: 5 contas por semana, das mais usadas às menos usadas

**Você** · 20 min

- [ ] **Pronto quando:** Relatório de integridade do KeePassXC sem senha fraca, repetida ou vazada
- Implanta: KeePassXC

### 2.12 Marcar a revisão a cada 3 meses: relatório do cofre, aparelhos conectados no Google e códigos de backup

**Você** · 10 min

- [ ] **Pronto quando:** Lembrete trimestral no calendário
- Implanta: KeePassXC

<a id="f3"></a>

## 3 · Windows

Os programas do setup instalados, o navegador com o Claude e o WSL2 pronto.

**Quando:** Semana 1 · out/2026

### 3.1 Ver o que o instalador faria

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1
```

- [ ] **Pronto quando:** Lista de INSTALARIA conferida
- Implanta: Instaladores (PowerShell e bash)

### 3.2 Instalar programas, WSL2 com Ubuntu 24.04 e .wslconfig (PowerShell como Administrador)

**Script** · 1 h 00 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO; reinicie o Windows
- Implanta: Terminal · PowerShell · winget · VS Code · 7-Zip · PowerToys · SumatraPDF · ShareX · LibreOffice · Firefox (2º navegador) · Obsidian + Git · DBeaver · Bruno · Excalidraw / draw.io · VirtualBox · Arduino IDE 2 · .wslconfig + localhost · OBS Studio · Audacity · Canva · Krita · Inkscape · Wireshark · Syncthing · Anki

### 3.3 Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC

**Você** · 15 min

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra criptografia OK
- No Windows 11 Home a opção se chama Criptografia do dispositivo e depende do hardware. Se não aparecer, anote e siga.
- Implanta: BitLocker · TPM + Secure Boot

### 3.4 Conferir Defender e Firewall ligados

**Você** · 10 min

- [ ] **Pronto quando:** verificar.ps1 como Administrador mostra Defender OK
- Implanta: Defender + Firewall

### 3.5 Instalar as extensões do VS Code (WSL, Claude Code, .NET, LaTeX, revisão em português)

**Script** · 10 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\extensoes-vscode.ps1 -Aplicar
```

- [ ] **Pronto quando:** Termina com 'Pronto'
- Implanta: VS Code

### 3.6 Instalar o Claude in Chrome e entrar com a sua conta

**Você** · 15 min

- [ ] **Pronto quando:** O painel do Claude abre numa aba do navegador
- O uso do computador pelo Claude fica no app do Claude para desktop; ligue só quando for usar e acompanhe o que ele faz.
- Implanta: Navegador + Claude in Chrome · Claude in Chrome + uso do computador

### 3.7 Instalar o DaVinci Resolve pelo site da Blackmagic (opcional)

**Você** · 20 min

- [ ] **Pronto quando:** Abre e reconhece a GPU
- Implanta: DaVinci Resolve ou Kdenlive

### 3.8 Decidir se Unity e Cocos ficam para as aulas de robótica

**Você** · 10 min

```powershell
winget install --id Unity.UnityHub -e
```

- [ ] **Pronto quando:** Decisão anotada; se ficam, Unity Hub instalado
- Implanta: Unity · Cocos

### 3.9 Conferir o Windows

**Script** · 5 min

```powershell
powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\verificar.ps1
```

- [ ] **Pronto quando:** verificar.ps1 termina com 'Windows pronto'
- Implanta: Verificadores

<a id="f4"></a>

## 4 · Linux (WSL2)

O Ubuntu com tudo o que o código precisa, commits assinados e o ambiente versionado.

**Quando:** Semana 2 · nov/2026

### 4.1 Abrir 'Ubuntu 24.04' no menu Iniciar e criar seu usuário Linux

**Você** · 10 min

- [ ] **Pronto quando:** Prompt do Ubuntu aberto
- Implanta: Ubuntu (WSL2)

### 4.2 Ligar o Docker Desktop no Ubuntu: Settings > Resources > WSL integration

**Você** · 5 min

- [ ] **Pronto quando:** 'docker run hello-world' funciona dentro do Ubuntu
- Implanta: Docker + Compose

### 4.3 Copiar este repositório para ~/dev/dev-setup

**Você** · 5 min

```bash
mkdir -p ~/dev && cp -r /mnt/c/Users/SEU_USUARIO/dev-setup ~/dev/dev-setup
```

- [ ] **Pronto quando:** Pasta ~/dev/dev-setup com os arquivos
- Troque SEU_USUARIO pelo seu usuário do Windows. Depois que o repositório estiver no GitHub, use git clone.

### 4.4 Rodar o preparador do Linux

**Script** · 40 min

```bash
bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email SEU_EMAIL --com-whisper
```

- [ ] **Pronto quando:** Termina com 'Pronto' e sem ERRO
- Implanta: .NET 10 · Node · Python · TeX Live · gitleaks · Trivy · Git + SSH + gh · nmap · dig · curl · Whisper (local) · Pranchas TikZ e SVG · CircuiTikZ · Instaladores (PowerShell e bash)

### 4.5 Reiniciar o WSL para o systemd valer (PowerShell)

**Você** · 2 min

```powershell
wsl --shutdown
```

- [ ] **Pronto quando:** Ubuntu reabre normalmente
- Implanta: Ubuntu (WSL2)

### 4.6 Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura

**Você** · 10 min

```bash
gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing
```

- [ ] **Pronto quando:** 'gh auth status' mostra sua conta
- Implanta: Git + SSH + gh · Commits assinados (chave SSH)

### 4.7 Guardar os dotfiles (.bashrc, .gitconfig, .tmux.conf) num repositório privado

**Claude com você** · 30 min

- [ ] **Pronto quando:** Repositório dotfiles privado; clonar e rodar o script de links recria o terminal
- Nunca coloque chaves ou tokens nos dotfiles. O gitleaks do CI confere a cada envio.
- Implanta: dotfiles

### 4.8 Criar o cofre do Obsidian em ~/dev/notas e ligar o plugin Obsidian Git

**Você** · 20 min

```bash
bash scripts/wsl/vault.sh
```

- [ ] **Pronto quando:** Cofre aberto no Obsidian com as pastas e modelos; notas vão sozinhas para um repositório privado a cada 10 minutos
- No Obsidian do Windows, abra a pasta \\wsl.localhost\Ubuntu-24.04\home\SEU_USUARIO\dev\notas.
- Implanta: Obsidian + Git

### 4.9 Ligar o Syncthing entre o celular e o notebook para as gravações (opcional)

**Você** · 15 min

- [ ] **Pronto quando:** Vídeo gravado no celular aparece na pasta Gravacoes do Windows
- Para o pipeline pegar, mova o vídeo para ~/AMtech/entrada/aulas. Vídeo com aluno menor de idade só com autorização do responsável.
- Implanta: Syncthing · Celular

### 4.10 Conferir o Linux

**Script** · 5 min

```bash
bash scripts/wsl/verificar.sh
```

- [ ] **Pronto quando:** verificar.sh termina com 'WSL pronto'
- Implanta: Verificadores

<a id="f5"></a>

## 5 · GitHub e CI

O repositório no ar, com testes automáticos verdes a cada envio e o trabalho organizado.

**Quando:** Semana 2 · nov/2026

### 5.1 Criar o repositório privado e enviar o setup

**Script** · 5 min

```bash
cd ~/dev/dev-setup && git init -q 2>/dev/null; git add -A && git commit -qm 'chore: setup inicial' ; gh repo create AlanMateus17/dev-setup --private --source . --push
```

- [ ] **Pronto quando:** Repositório AlanMateus17/dev-setup privado com o código
- Se você usar o zip, o histórico de commits não vem junto; o repositório começa com um commit novo, já assinado.
- Implanta: GitHub

### 5.2 Conferir o CI no GitHub

**Script** · 5 min

```bash
gh run list --limit 1
```

- [ ] **Pronto quando:** Última execução do workflow 'docs' com sucesso
- Implanta: GitHub Actions

### 5.3 Ligar Dependabot e CodeQL e proteger o branch main

**Claude com você** · 15 min

- [ ] **Pronto quando:** Dependabot e CodeQL ativos; push direto no main exige CI verde
- Peça ao Claude Code no repositório; ele faz pelo gh api com a sua aprovação.
- Implanta: Dependabot + CodeQL

### 5.4 Criar a organização grupo-amtech-digital no GitHub

**Você** · 10 min

- [ ] **Pronto quando:** Organização criada, com 2FA obrigatório para membros
- Implanta: GitHub

### 5.5 Criar o GitHub Project do setup e a pasta de decisões (ADRs)

**Claude com você** · 20 min

- [ ] **Pronto quando:** Quadro com as fases deste roteiro e docs/adr/0001 registrado
- O MkDocs publica a documentação no GitHub Pages quando você quiser tornar algo público; o setup continua privado.
- Implanta: Projects · ADRs · MkDocs

<a id="f6"></a>

## 6 · Agentes de IA

O Claude Code trabalhando dentro da sandbox, com as suas regras, ferramentas e memória.

**Quando:** Semana 2 · nov/2026

### 6.1 Entrar no Claude Code

**Você** · 5 min

```bash
claude
```

- [ ] **Pronto quando:** 'claude doctor' sem erros
- Implanta: Claude Code

### 6.2 Testar a sandbox

**Script** · 2 min

```bash
cd ~/dev/dev-setup && ai-jail --dry-run claude
```

- [ ] **Pronto quando:** Mostra o que seria montado, sem erro
- Implanta: ai-jail

### 6.3 Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura

**Claude com você** · 30 min

- [ ] **Pronto quando:** Arquivos no repositório de cada sistema
- Peça ao Claude Code: o conteúdo está em docs/pecas-autorais.md.
- Implanta: CLAUDE.md, agentes e skills (seus)

### 6.4 Baixar um modelo local de 3 a 4B no Ollama

**Você** · 15 min

```bash
ollama pull <nome do modelo escolhido no catálogo do Ollama>
```

- [ ] **Pronto quando:** verificar.ps1 mostra Ollama OK com 1 modelo
- Implanta: Ollama · Modelos locais: Qwen · Gemma · Llama

### 6.5 Ligar os servidores MCP do Claude Code: GitHub e o banco de métricas só para leitura

**Claude com você** · 20 min

- [ ] **Pronto quando:** 'claude mcp list' mostra os servidores conectados
- O banco entra com o usuário leitor do Grafana, que não apaga nada. Tokens ficam no KeePassXC e em variáveis de ambiente, nunca no repositório.
- Implanta: Servidores MCP

### 6.6 Ligar o ai-memory para o agente lembrar das decisões entre sessões

**Claude com você** · 15 min

- [ ] **Pronto quando:** Uma decisão anotada numa sessão aparece na seguinte
- Implanta: ai-memory

### 6.7 Montar a base de conhecimento das suas notas (Ollama + pgvector, ou NotebookLM e Projects)

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Pergunta sobre uma anotação sua volta com a resposta e a nota de origem
- Entram só as suas anotações, resumos com suas palavras, exercícios resolvidos e aulas que você gravou. Aulas da Udemy, DIO, Alura e afins não entram.
- Implanta: Base de conhecimento (RAG) das suas notas · NotebookLM

<a id="f7"></a>

## 7 · Backup e segurança

Perder o notebook não faz você perder nada.

**Quando:** Semana 3 · nov/2026

### 7.1 Criar o repositório restic no disco externo e o primeiro backup

**Script** · 30 min

```bash
restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech
```

- [ ] **Pronto quando:** 'restic snapshots' lista o backup
- Troque /mnt/d pela letra do seu disco externo (D: vira /mnt/d). Guarde a senha do repositório no KeePassXC.
- Implanta: restic (backup criptografado) · Backup 3-2-1 · Disco externo

### 7.2 Criar a cópia fora de casa (Backblaze B2 ou o armazenamento do seu plano Google)

**Você** · 40 min

- [ ] **Pronto quando:** Segundo repositório restic com snapshot
- Implanta: Backblaze B2 (backup) · Backup 3-2-1

### 7.3 Testar a restauração de uma pasta

**Você** · 15 min

- [ ] **Pronto quando:** Arquivo restaurado abre normalmente
- Implanta: Backup 3-2-1

### 7.4 Agendar o backup diário

**Claude com você** · 20 min

- [ ] **Pronto quando:** Timer do backup ativo
- Implanta: restic (backup criptografado)

<a id="f8"></a>

## 8 · Acervo: tudo o que você já tem

Todos os seus documentos convertidos em conhecimento organizado no Obsidian, os pessoais separados e a lista do que dá para vender.

**Quando:** Semanas 3 e 4 · nov/2026

### 8.1 Baixar uma cópia completa do Google Drive pelo Google Takeout

**Você** · 45 min

- [ ] **Pronto quando:** Os zips do Takeout extraídos numa pasta só, por exemplo C:\Users\SEU_USUARIO\Downloads\Takeout
- Escolha só o Drive e, em formatos, Google Docs como .docx e Apresentações como .pptx. O Drive para computador mostra os Google Docs como atalhos sem conteúdo, por isso a primeira cópia vem do Takeout. Junte também os arquivos do notebook e dos pendrives na mesma pasta.
- Implanta: Google Drive (seus documentos)

### 8.2 Tirar da pasta os documentos pessoais (contracheques, extratos, IRPF, faturas)

**Você** · 30 min

- [ ] **Pronto quando:** Pasta Pessoal separada, guardada só no backup criptografado
- O acervo.py também barra esses arquivos pelo nome e pelo conteúdo e lista o que achou, mas tirar antes é mais seguro.
- Implanta: Backup 3-2-1

### 8.3 Ver o que o acervo faria, sem escrever nada

**Script** · 10 min

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular
```

- [ ] **Pronto quando:** Resumo com arquivos lidos, cópias repetidas, pessoais, de terceiros e da escola
- Implanta: Acervo (seus documentos)

### 8.4 Converter o acervo para o Obsidian e gerar o relatório de produtos

**Script** · 30 min

```bash
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout
```

- [ ] **Pronto quando:** 30-Acervo no Obsidian com os documentos em Markdown e 40-Produtos/Produtos do acervo.md
- Roda no notebook; nada é enviado para fora. Pode rodar de novo quando chegarem documentos novos: o que já foi convertido não é refeito.
- Implanta: Acervo (seus documentos) · Obsidian + Git

### 8.5 Decidir cada alerta: dados de alunos, material de terceiros, material feito para a escola

**Você** · 1 h 30 min

- [ ] **Pronto quando:** Cada alerta com decisão anotada: apagar dados, só estudo, reescrever ou vender
- Material de terceiros (livros, cursos) não vira produto nem treino de IA. Material feito para a escola: confira os direitos antes de vender; o caminho seguro é reescrever do zero, no seu tempo, sem a identidade da escola.
- Implanta: Acervo (seus documentos)

### 8.6 Indexar o acervo e as suas notas na base de conhecimento

**Claude com você** · 30 min

- [ ] **Pronto quando:** Pergunta sobre um documento antigo volta com a resposta e o arquivo de origem
- Implanta: Base de conhecimento (RAG) das suas notas

### 8.7 Escolher no relatório os 3 primeiros produtos e levar para o portfólio de ofertas

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** 3 ofertas novas em data/portfolio.json com estágio, preço alvo e próximo passo
- Implanta: Portfólio de ofertas · Esteira de ofertas

<a id="f9"></a>

## 9 · Claude e assistentes

Cada recurso do Claude e cada assistente com um papel definido no setup.

**Quando:** Semana 4 · nov/2026

### 9.1 Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas

**Você** · 30 min

- [ ] **Pronto quando:** Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
- Implanta: Claude (app) · Projects + memória · Artifacts (Docs, Slides, Sheets…) · Pesquisa aprofundada · Tarefas agendadas

### 9.2 Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ

**Você** · 30 min

- [ ] **Pronto quando:** Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
- Notion, monday, GitBook e Stripe ficam de fora: repetem Obsidian, GitHub Projects, MkDocs e as plataformas de curso. Desconecte para não confundir.
- Implanta: Conector Google (Gmail, Drive…) · Conectores Canva + Figma · Conector MailerLite · Vercel · AWS · Microsoft Learn · Conector Upwork · Lovable + Supabase · Conector Cloudflare · Conector vidIQ · Notion · monday · GitBook · Stripe

### 9.3 Ligar os plugins: small-business, marketing, engineering, design, finance, Hostinger, Adobe e Cloudinary

**Você** · 15 min

- [ ] **Pronto quando:** Os comandos dos plugins aparecem no Claude
- Implanta: Plugins: small- business + marketing · Plugins: engineering + design · Plugins: finance + Fiscal.ai · Plugins: Hostinger · Adobe · Cloudinary

### 9.4 Entrar nos outros assistentes (ChatGPT, Gemini, Grok, DeepSeek, Perplexity, Codex, agentes do Google) e anotar quais são pagos

**Você** · 30 min

- [ ] **Pronto quando:** Acessos no KeePassXC e assinaturas pagas lançadas na tabela ferramentas do banco de métricas
- Implanta: ChatGPT · Gemini (pago) · Grok · DeepSeek · Perplexity · Codex (OpenAI) · Agentes de código do Google

<a id="f10"></a>

## 10 · Automação e medição

n8n, banco de métricas, Grafana e Uptime Kuma rodando.

**Quando:** Semana 4 · nov/2026

### 10.1 Gerar as senhas da stack e guardar no KeePassXC

**Script** · 5 min

```bash
cd infra/automacao && bash gerar-senhas.sh
```

- [ ] **Pronto quando:** .env criado com permissão 600
- Implanta: n8n

### 10.2 Subir a stack

**Script** · 10 min

```bash
cd infra/automacao && docker compose up -d
```

- [ ] **Pronto quando:** 'docker compose ps' com todos healthy
- Implanta: Docker + Compose · n8n · Banco de métricas (PostgreSQL) · PostgreSQL

### 10.3 Conferir os serviços

**Script** · 2 min

```bash
bash scripts/wsl/verificar.sh --servicos
```

- [ ] **Pronto quando:** verificar.sh --servicos sem FALTA na área servico
- Implanta: Verificadores

### 10.4 Entrar no Grafana (admin) e ver a fonte 'Métricas AMtech' conectada

**Você** · 10 min

```text
http://localhost:3001
```

- [ ] **Pronto quando:** Explore > Métricas AMtech > 'select 1' responde
- Implanta: Grafana

### 10.5 Criar a conta do n8n

**Você** · 5 min

```text
http://localhost:5678
```

- [ ] **Pronto quando:** Painel do n8n abre
- Implanta: n8n

### 10.6 Cadastrar no Uptime Kuma os monitores do n8n, Grafana e dos sites

**Você** · 15 min

```text
http://localhost:3002
```

- [ ] **Pronto quando:** Monitores verdes; aviso no Telegram configurado
- Implanta: Uptime Kuma

### 10.7 Pôr o banco de métricas e os fluxos do n8n no backup diário

**Claude com você** · 45 min

- [ ] **Pronto quando:** Dump diário do banco e export dos fluxos em ~/AMtech/backup-dados, copiados pelo restic; uma restauração de teste funcionou
- Os dados ficam em volumes do Docker, fora das pastas que o restic copia. Sem este passo, perder o notebook leva junto o histórico de vendas.
- Implanta: Banco de métricas (PostgreSQL) · n8n · restic (backup criptografado)

### 10.8 Decidir: Postiz agora ou agendador nativo das redes

**Você** · 10 min

- [ ] **Pronto quando:** Decisão anotada em infra/postiz/README.md
- Implanta: Postiz (agendador)

<a id="f11"></a>

## 11 · Pipeline de conteúdo

Gravou ou escreveu, as peças aparecem na fila de aprovação.

**Quando:** Semana 5 · nov/2026

### 11.1 Preencher o guia de marca

**Você** · 40 min

- [ ] **Pronto quando:** config/marca.md sem colchetes
- O Claude pode rascunhar a partir dos documentos de marca e presença; você corrige.
- Implanta: Marca pessoal Alan Mateus

### 11.2 Criar a chave da API no console da Anthropic e colocar no conteudo.env

**Você** · 10 min

- [ ] **Pronto quando:** ANTHROPIC_API_KEY preenchida em ~/.config/amtech/conteudo.env
- A API é cobrada por uso, separada da assinatura do Claude. Defina um limite de gasto mensal no console.
- Implanta: Claude (assinatura e API)

### 11.3 Criar o bot de aviso no Telegram (opcional)

**Você** · 10 min

- [ ] **Pronto quando:** Mensagem de teste chega no celular
- Implanta: Telegram (avisos) · Aprovação no celular

### 11.4 Testar o caminho sem gastar

**Script** · 2 min

```bash
echo teste > ~/AMtech/entrada/ideias/teste.txt && touch -d '-2 min' ~/AMtech/entrada/ideias/teste.txt && python3 tools/conteudo/processar.py --uma-vez --simular
```

- [ ] **Pronto quando:** Uma pasta [SIMULADO] aparece em ~/AMtech/fila
- Implanta: Pipeline de conteúdo

### 11.5 Ligar o timer de 15 minutos

**Script** · 2 min

```bash
bash scripts/wsl/ativar-pipeline.sh
```

- [ ] **Pronto quando:** verificar.sh --servicos mostra o timer OK
- Implanta: Pipeline de conteúdo · Agente editor de conteúdo · Flywheel de conteúdo

### 11.6 Colocar uma aula gravada de verdade em ~/AMtech/entrada/aulas

**Você** · 20 min

- [ ] **Pronto quando:** Peças da aula na fila em até 15 minutos depois de transcrita
- Implanta: Whisper (local) · Flywheel de conteúdo

<a id="f12"></a>

## 12 · Estúdio de conteúdo

Gravar, editar e montar imagens no mesmo padrão toda semana, sem pensar.

**Quando:** Semana 5 · dez/2026

### 12.1 Montar no OBS as cenas de aula, tela com rosto e vídeo vertical

**Você** · 40 min

- [ ] **Pronto quando:** Gravação de teste de 1 minuto com áudio limpo nas três cenas
- Implanta: OBS Studio

### 12.2 Criar no Audacity a cadeia de limpeza da sua voz (ruído, compressor, volume)

**Você** · 20 min

- [ ] **Pronto quando:** A mesma limpeza aplicada com um clique numa gravação nova
- Implanta: Audacity

### 12.3 Criar no DaVinci ou Kdenlive o projeto modelo com abertura, legendas e formato vertical

**Você** · 40 min

- [ ] **Pronto quando:** Um corte de 30 segundos exportado a partir do modelo
- Implanta: DaVinci Resolve ou Kdenlive

### 12.4 Criar os modelos de capa, carrossel e thumbnail com a sua marca (Canva, Krita ou Inkscape)

**Claude com você** · 40 min

- [ ] **Pronto quando:** Três modelos salvos; uma peça da fila montada com eles
- O Claude cria os modelos no Canva pelo conector, a partir do config/marca.md.
- Implanta: Canva · Krita · Inkscape · Conectores Canva + Figma

### 12.5 Clonar a sua própria voz na ElevenLabs (opcional, plano pago)

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Trecho de teste com a sua voz clonada aprovado por você
- Só a sua voz, com 30 minutos ou mais de áudio limpo. Avise o público quando a voz for gerada por IA. Voz de outra pessoa, nunca.
- **Precisa:** pagar um serviço
- Implanta: Voz clonada (ElevenLabs)

<a id="f13"></a>

## 13 · Contas, canais e sites

Perfis, domínio, e-mail e sites prontos para receber o que o pipeline produz.

**Quando:** Semanas 6 e 7 · dez/2026

### 13.1 Completar Instagram, YouTube, TikTok, LinkedIn e Facebook com a mesma identidade

**Você** · 1 h 30 min

- [ ] **Pronto quando:** Foto, nome, bio e link iguais nas cinco redes
- Implanta: Instagram · YouTube · TikTok · LinkedIn · Facebook · Marca pessoal Alan Mateus

### 13.2 Configurar o WhatsApp Business com catálogo, respostas rápidas e horário

**Você** · 30 min

- [ ] **Pronto quando:** Mensagem de teste recebe a saudação automática
- Implanta: WhatsApp Business

### 13.3 Registrar o domínio no Registro.br e apontar para a Cloudflare

**Você** · 30 min

- [ ] **Pronto quando:** DNS ativo na Cloudflare
- **Precisa:** pagar um serviço
- Implanta: Domínio (Registro.br) · Cloudflare (DNS, Pages, e-mail)

### 13.4 Criar o e-mail profissional do domínio

**Você** · 30 min

- [ ] **Pronto quando:** Envia e recebe
- **Precisa:** pagar um serviço
- Implanta: E-mail profissional (enviar e receber)

### 13.5 Criar o Gerenciador de Negócios da Meta, o Pixel e a conta de anúncios

**Você** · 40 min

- [ ] **Pronto quando:** Pixel instalado na página de vendas
- Implanta: Meta Business Suite · Tags de conversão (Pixel, Google…)

### 13.6 Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas

**Claude com você** · 30 min

- [ ] **Pronto quando:** Inscrição de teste recebe o primeiro e-mail
- O Claude faz pelo conector do MailerLite, com a sua aprovação.
- Implanta: MailerLite · Isca grátis + sequência de e-mails · Conector MailerLite

### 13.7 Publicar o site pessoal e blog no GitHub Pages (alanmateus17.github.io)

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Site no ar com portfólio, blog e formulário da newsletter
- Implanta: Site pessoal + blog (Jekyll) · GitHub Pages

### 13.8 Publicar o site do Instituto AMS com a página de pré-venda na Cloudflare Pages

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Página no ar com o domínio e o Pixel
- Fica na Cloudflare Pages porque o plano grátis do Vercel não permite uso comercial. O Claude publica pelo conector da Cloudflare ou pelo Wrangler.
- Implanta: Instituto AMS · Cloudflare (DNS, Pages, e-mail)

### 13.9 Publicar o site do Grupo AMtech e o Catálogo do HTML

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** Os dois sites no ar com domínio e HTTPS
- **Oferta:** Catálogo do HTML (gratuito)
- Implanta: Site Grupo AMtech · Catálogo do HTML

### 13.10 Mostrar o Catálogo do HTML aos alunos e ex-alunos

**Você** · 20 min

- [ ] **Pronto quando:** Alunos publicando os próprios sites pelo Catálogo
- É material grátis da escola, não venda. Nada de oferecer produto pago a aluno menor de idade; ex-alunos adultos podem seguir as redes.
- Implanta: Alunos e ex-alunos

### 13.11 Ligar o Umami nos sites

**Claude com você** · 20 min

- [ ] **Pronto quando:** Uma visita de teste aparece no painel do Umami
- Implanta: Umami (analytics)

### 13.12 Ligar o Google Search Console no domínio e enviar o sitemap de cada site

**Você** · 10 min

- [ ] **Pronto quando:** Propriedade verificada e sitemaps lidos
- Implanta: Google Search Console · Busca Google (SEO)

### 13.13 Separar na Hostinger o espaço dos sites de clientes

**Claude com você** · 30 min

- [ ] **Pronto quando:** Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
- O Claude faz a auditoria pelo plugin da Hostinger e aponta o que precisa de atenção.
- **Oferta:** Sites e lojas para pequenas empresas
- Implanta: Hostinger (clientes WP) · Sites para pequenas empresas

<a id="f14"></a>

## 14 · Vendas e finanças no CPF

Cada oferta pode ser vendida, recebida e declarada do jeito certo.

**Quando:** Semanas 8 a 10 · dez/2026 a jan/2027

### 14.1 Subir a conta gov.br para prata ou ouro

**Você** · 20 min

- [ ] **Pronto quando:** Nível prata ou ouro aparece no app gov.br
- Implanta: gov.br (prata ou ouro)

### 14.2 Abrir a conta bancária separada para o que você vende (no CPF)

**Você** · 30 min

- [ ] **Pronto quando:** Conta aberta; todas as plataformas vão pagar nela
- Implanta: Conta bancária separada (CPF)

### 14.3 Fazer a consulta com o contador: carnê-leão e a partir de que renda abrir CNPJ

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Regras do carnê-leão anotadas e o valor de virada para o CNPJ definido
- **Precisa:** pagar um serviço
- Implanta: Contador

### 14.4 Publicar termos de uso e política de privacidade (LGPD) e ter o contrato padrão de serviço

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Links de termos e privacidade no rodapé de todos os sites; contrato em modelo editável
- O Claude rascunha; antes de usar, peça para o contador ou um advogado revisar. Isto vem antes de coletar e-mail ou vender.
- Implanta: Termos, privacidade (LGPD) e contratos

### 14.5 Criar as contas da Hotmart e da Kiwify no CPF e cadastrar o mini-curso

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Produto em rascunho nas duas
- Implanta: Hotmart · Kiwify · Mini-curso Lógica de Programação

### 14.6 Abrir as contas na Eduzz e na Udemy e publicar artigos e projetos na DIO

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Contas aprovadas; formulário fiscal da Udemy enviado; primeiro artigo publicado na DIO
- Na Udemy o recebimento é por PayPal ou Payoneer e vai para o carnê-leão como renda do exterior.
- **Oferta:** Parceria DIO
- Implanta: Eduzz · Udemy · DIO (parceria)

### 14.7 Ativar o Mercado Pago para Pix e cartão das aulas e dos sites

**Você** · 20 min

- [ ] **Pronto quando:** Link de pagamento de teste pago e estornado
- Implanta: Mercado Pago

### 14.8 Criar a agenda online no Cal.com com pagamento para as aulas particulares

**Você** · 30 min

- [ ] **Pronto quando:** Horário de teste marcado e cobrado
- **Oferta:** Aulas particulares
- Implanta: Agenda online (Cal.com) · Aulas particulares

### 14.9 Criar o CRM em planilha com origem e consentimento de cada cliente

**Claude com você** · 30 min

- [ ] **Pronto quando:** Planilha com colunas de oferta, origem, consentimento LGPD e próximo passo
- Implanta: CRM simples (planilha) · CRM único + LGPD

### 14.10 Abrir a comunidade dos alunos (Discord ou grupo)

**Você** · 30 min

- [ ] **Pronto quando:** Regras publicadas e convite automático na compra
- Implanta: Comunidade (Discord ou grupo)

### 14.11 Entrar nos programas de afiliados (Amazon, Hotmart) e criar a lista de links

**Você** · 30 min

- [ ] **Pronto quando:** Links de afiliado com UTM numa nota do Obsidian
- **Oferta:** Afiliados (ferramentas, livros, equipamentos que você usa)
- Implanta: Afiliados (Amazon, Hotmart…)

### 14.12 Adotar o padrão de UTM em todo link

**Claude com você** · 15 min

- [ ] **Pronto quando:** Gerador de links com UTM salvo e usado no primeiro post
- Implanta: Padrão de UTM

### 14.13 Calcular o lucro por venda de cada oferta e definir as regras de corte dos anúncios

**Você** · 30 min

- [ ] **Pronto quando:** CPA de empate e CPA da margem anotados para cada oferta ativa
- Implanta: Lucro por Venda (calculadora) · Regras de corte

### 14.14 Revisar o portfólio de ofertas: estágio, próximo passo e padrão de qualidade

**Claude com você** · 45 min

- [ ] **Pronto quando:** Uma oferta em construção e uma em validação, cada uma com o checklist de pronto
- O Claude cria o comando /revisar-oferta, que confere um lançamento contra o padrão de qualidade antes de ir ao ar.
- Implanta: Portfólio de ofertas · Esteira de ofertas · Padrão de qualidade · Revisor de oferta

### 14.15 Ligar a pergunta de satisfação depois de cada compra ou serviço e o pedido de avaliação no Google

**Claude com você** · 30 min

- [ ] **Pronto quando:** Compra de teste recebe a pergunta por e-mail
- Implanta: NPS e avaliações

### 14.16 Montar a lista de parceiros e a primeira mensagem de prospecção

**Claude com você** · 45 min

- [ ] **Pronto quando:** 10 parceiros qualificados e a mensagem revisada por você
- O Claude busca e qualifica; quem envia é você.
- Implanta: Prospecção de parceiros

### 14.17 Pesquisar e pedir o registro das marcas no INPI

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Pesquisa sem conflito e pedido protocolado (ou decisão de esperar, anotada)
- **Precisa:** pagar um serviço
- Implanta: Registro de marca (INPI)

### 14.18 Fazer o primeiro carnê-leão do mês e marcar o lembrete mensal

**Você** · 30 min

- [ ] **Pronto quando:** DARF gerado (ou mês sem receita registrado) e lembrete todo dia 20
- Implanta: Carnê-leão (Receita Federal)

### 14.19 Separar a pasta da declaração anual do IR

**Você** · 15 min

- [ ] **Pronto quando:** Pasta com informes e carnês do ano, guardada no backup
- Implanta: Declaração anual do IR

### 14.20 Começar o Caixa da Casa numa planilha até o sistema AM Rendara existir

**Claude com você** · 30 min

- [ ] **Pronto quando:** Entradas e saídas do mês lançadas, separando casa e vendas
- **Oferta:** AM Rendara (finanças), começando pela planilha
- Implanta: Caixa da Casa / AM Rendara

<a id="f15"></a>

## 15 · Vendas medidas

Cada venda chega sozinha ao banco e aparece no painel de lucro.

**Quando:** Semana 11 · jan/2027

### 15.1 Criar o túnel público para os webhooks (Cloudflare Tunnel) e preencher N8N_WEBHOOK_URL

**Você** · 40 min

- [ ] **Pronto quando:** https://n8n.seu-dominio responde fora de casa
- Só o caminho de webhook precisa ficar público; o painel do n8n fica protegido.
- **Precisa:** pagar um serviço
- Implanta: Cloudflare (DNS, Pages, e-mail) · Webhooks de venda

### 15.2 Criar no n8n o fluxo: webhook Hotmart, Kiwify e Eduzz → tabela vendas

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Venda de teste aparece na tabela vendas
- O Claude monta o fluxo com você no n8n; a tabela já tem a trava contra venda duplicada.
- Implanta: Webhooks de venda

### 15.3 Lançar os gastos de anúncio (manual no começo, depois pela API de cada rede)

**Você** · 15 min

- [ ] **Pronto quando:** Tabela gastos com a primeira campanha
- Implanta: Banco de métricas (PostgreSQL)

### 15.4 Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes

**Claude com você** · 45 min

- [ ] **Pronto quando:** Painel mostra receita, anúncio, lucro e CPA por produto
- Implanta: Painel de lucro (Grafana) · Grafana

<a id="f16"></a>

## 16 · Teste do núcleo

Os três testes de ponta a ponta passam: daqui em diante, alimentar o sistema já faz tudo sozinho.

**Quando:** Semana 11 · jan/2027

### 16.1 Dev: mudar algo num repositório, commit assinado, push, CI verde

**Você** · 15 min

- [ ] **Pronto quando:** Selo Verified no commit e CI verde
- Implanta: Commits assinados (chave SSH) · GitHub Actions

### 16.2 Conteúdo: arquivo na entrada → peças na fila → aviso no Telegram

**Você** · 20 min

- [ ] **Pronto quando:** Pasta nova na fila e mensagem no celular
- Implanta: Pipeline de conteúdo

### 16.3 Venda: compra de teste na Hotmart → linha na tabela vendas → painel de lucro

**Você** · 20 min

- [ ] **Pronto quando:** Venda de teste no Grafana
- Implanta: Webhooks de venda · Painel de lucro (Grafana)

### 16.4 Rodar os três verificadores juntos

**Script** · 5 min

- [ ] **Pronto quando:** verificar.ps1, verificar.sh e verificar.sh --servicos sem FALTA
- Implanta: Verificadores · Roteiro de implantação

<a id="f17"></a>

## 17 · Primeira venda: o mini-curso no ar

A primeira venda real pela internet, com entrega, suporte, imposto e números no painel.

**Quando:** Semanas 12 a 15 · jan a fev/2027

### 17.1 Fechar o roteiro das 5 primeiras aulas do mini-curso a partir do acervo

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** 5 aulas com objetivo, exemplo e exercício, no Obsidian
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Mini-curso Lógica de Programação

### 17.2 Gravar e editar as 5 aulas

**Você** · 10 h 00 min

- [ ] **Pronto quando:** 5 vídeos finais exportados no modelo do estúdio
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: OBS Studio · DaVinci Resolve ou Kdenlive

### 17.3 Subir as aulas na Hotmart com preço e garantia de 7 dias

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Produto aprovado na Hotmart, com checkout funcionando
- A garantia de 7 dias é o direito de arrependimento do Código de Defesa do Consumidor para compra pela internet.
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Hotmart

### 17.4 Página de vendas no Instituto AMS: promessa, conteúdo, preço e garantia

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Página no ar levando ao checkout, com Pixel e UTM
- Sem depoimento inventado: só depoimentos reais, com autorização, quando existirem.
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Instituto AMS · Tags de conversão (Pixel, Google…) · Padrão de UTM

### 17.5 Isca grátis (aula 1) com a sequência de e-mails que leva à venda

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** Inscrição de teste recebe os 5 e-mails e o último leva ao checkout
- **Oferta:** Mini-curso Lógica de Programação · Newsletter (patrocínio e vendas)
- Implanta: Isca grátis + sequência de e-mails · MailerLite

### 17.6 Abrir a pré-venda: lista de e-mail, Instagram, WhatsApp e LinkedIn

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Lançamento publicado em todos os canais, com UTM
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Instagram · WhatsApp Business · LinkedIn

### 17.7 Primeira venda real: acesso, suporte, painel e carnê-leão

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Venda paga, aluno com acesso, dúvida respondida em até 24 h, linha na tabela vendas e venda lançada no carnê-leão
- **Oferta:** Mini-curso Lógica de Programação
- Implanta: Hotmart · Webhooks de venda · Carnê-leão (Receita Federal)

### 17.8 Publicar o mini-curso também na Kiwify, Eduzz e Udemy

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Mini-curso à venda nas quatro plataformas
- **Oferta:** Mini-curso Lógica de Programação · Versões dos cursos na Udemy (português e inglês)
- Implanta: Kiwify · Eduzz · Udemy

<a id="f18"></a>

## 18 · Base dos sistemas AM

Um sistema novo nasce pronto: arquitetura, testes, login, observabilidade e deploy.

**Quando:** Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6

### 18.1 Gerar o modelo de sistema com /novo-sistema-aura

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Sistema exemplo sobe com 'dotnet run' e passa nos testes
- Clean Architecture + DDD, EF Core com Npgsql, multi-tenant com RLS, SignalR com Redis, OpenAPI com Scalar, Next.js com o Aura Design System e Storybook, testes com xUnit, Playwright e k6.
- Implanta: Clean Arch + DDD · EF Core + Npgsql · SignalR · Multi-tenant (RLS) · API ASP.NET Core · Next.js + Aura Design System · OpenAPI + Scalar · Storybook · PostgreSQL · Redis · Testes: xUnit, Playwright, k6

### 18.2 Ligar o login: Keycloak no dev e Entra ID na nuvem

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Usuário de teste entra e só vê os dados da própria empresa
- Implanta: Keycloak / Entra ID

### 18.3 Ligar a observabilidade do dev: .NET Aspire, OpenTelemetry, Prometheus, Seq, Mailpit e Caddy

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Painel do Aspire mostra trace de uma requisição; e-mail de teste cai no Mailpit
- Implanta: .NET Aspire · OpenTelemetry · Prometheus · Seq (logs) · Mailpit · Caddy (proxy + HTTPS)

### 18.4 Criar o projeto no Sentry e ligar no modelo

**Você** · 20 min

- [ ] **Pronto quando:** Erro de teste aparece no Sentry
- Implanta: Sentry (erros)

### 18.5 Ligar o SonarQube Cloud no repositório do modelo

**Você** · 20 min

- [ ] **Pronto quando:** Nota de qualidade aparece no pull request
- O plano grátis cobre repositório público; confira o limite para privado antes de ligar.
- Implanta: SonarQube Cloud

### 18.6 Publicar a imagem Docker da API no GHCR pelo CI

**Claude com você** · 30 min

- [ ] **Pronto quando:** Imagem com a tag do commit aparece nos pacotes do GitHub
- Implanta: GHCR (imagens)

### 18.7 Separar o que do modelo pode virar template à venda

**Você** · 30 min

- [ ] **Pronto quando:** Lista de templates no portfólio de ofertas
- **Oferta:** Templates e código-fonte
- Implanta: Templates e código-fonte

### 18.8 Candidatar-se às vagas de dev .NET com GitHub, LinkedIn e site prontos — quando o Passo 8 da trilha de estudo estiver feito (≈ jul a dez/2027)

**Você** · 2 h 00 min

- [ ] **Pronto quando:** 10 candidaturas enviadas com o portfólio do sistema exemplo
- Implanta: Recrutadores

<a id="f19"></a>

## 19 · Nuvem e deploy

As contas de nuvem criadas por código, com custo sob controle.

**Quando:** Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028)

### 19.1 Instalar Azure CLI, Terraform, Vercel CLI e Wrangler

**Script** · 15 min

```bash
bash scripts/wsl/nuvem.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto'; verificar.sh mostra as quatro ferramentas
- Implanta: Azure CLI · AWS CLI · Terraform

### 19.2 Criar a conta Azure com alerta de orçamento

**Você** · 30 min

- [ ] **Pronto quando:** 'az login' entra e o alerta de gasto está ligado
- Ligue o alerta antes de criar qualquer recurso. O Microsoft Learn do conector ajuda a escolher o serviço mais barato.
- Implanta: Azure

### 19.3 Criar com Terraform o grupo de recursos, o banco e o Key Vault do primeiro sistema

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** 'terraform plan' sem diferenças depois do apply
- Implanta: Terraform · Azure

### 19.4 Criar o armazenamento de arquivos (R2 da Cloudflare ou Blob)

**Claude com você** · 30 min

- [ ] **Pronto quando:** Upload de teste pelo sistema exemplo
- Implanta: Armazenamento de arquivos (Blob/R2)

### 19.5 Configurar o e-mail transacional (Resend) com o domínio verificado

**Você** · 30 min

- [ ] **Pronto quando:** E-mail de confirmação de conta chega na caixa de entrada, não no spam
- Implanta: E-mail transacional (Resend, SES…)

### 19.6 Fazer o primeiro deploy do sistema exemplo

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Sistema no ar com HTTPS, login e erro de teste no Sentry
- Implanta: Vercel · Azure · Cloudflare (DNS, Pages, e-mail)

### 19.7 Criar o aura-status: painel de repositórios, backup e Dependabot

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Painel mostra o estado de todos os repositórios
- Implanta: aura-status

<a id="f20"></a>

## 20 · Editora

O livro sai de um repositório com CI, pronto para virar PDF, EPUB e impressão.

**Quando:** Quando o capítulo 1 estiver pronto

**Começa quando:** O capítulo 1 e o seu modelo de criação prontos

### 20.1 Entregar o seu modelo de criação e o seu método passo a passo

**Você** · 2 h 00 min

- [ ] **Pronto quando:** metodo.yaml com cada etapa, entrada, saída e critério de conclusão; template de capítulo pronto
- Implanta: Seu modelo de criação · Seu método (metodo.yaml) · Projeto do capítulo · Mapa de pré-requisitos

### 20.2 Criar o repositório do livro com fonte única, classe LaTeX, exercícios em YAML e CI

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Um push gera PDF, EPUB e o gabarito sem erro
- Depende do capítulo 1 e do seu modelo. O conteúdo é seu; nada de material de terceiros.
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Repositório do livro · Fonte única (Markdown + Pandoc) · Classe LaTeX do livro · Exercícios em YAML · Pipeline do livro (CI) · Revisão automática (LanguageTool, Vale) · Errata e edições · Livro Lógica e Máquina

### 20.3 Construir o pipeline de imagens do livro: busca nos acervos, filtro de licença, folha de contato e créditos

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Uma figura do capítulo 1 sai com licença conferida, ficha e crédito; o build falha se faltar ficha
- Implanta: Acervos de imagens (APIs) · Busca automática de imagens · Filtro de licença e fichas · Folha de contato (artefato) · Créditos e legendas

### 20.4 Figuras, tabelas e texto alternativo gerados por código

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Gráficos e tabelas do capítulo 1 gerados no build, com texto alternativo revisado por você
- Implanta: Figuras por código (Matplotlib…) · Geradores de tabelas · Texto alternativo

### 20.5 Criar os agentes da editora: revisor técnico, gabarito, leitor iniciante e consistência

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Os agentes apontam problemas reais no capítulo 1 e você corrige
- Implanta: Agentes da editora

### 20.6 Montar a matriz de editais e o quadro de referências

**Claude com você** · 1 h 00 min

- [ ] **Pronto quando:** Cada tópico dos editais ligado a um capítulo; lacunas listadas
- Implanta: Matriz de editais · Quadro de referências

### 20.7 Definir o selo Editora AMS Silva (nome, logo e uso no CPF)

**Você** · 30 min

- [ ] **Pronto quando:** Logo aprovado e aplicado na classe LaTeX
- Implanta: Selo Editora AMS Silva

### 20.8 Comprar os ISBNs na CBL e pedir a ficha catalográfica

**Você** · 1 h 00 min

- [ ] **Pronto quando:** ISBN do impresso e do ebook, código de barras e ficha no verso da folha de rosto
- **Precisa:** pagar um serviço, conteúdo seu pronto (livro, capítulo)
- Implanta: ISBN + código de barras (CBL) · Ficha catalográfica

### 20.9 Escolher 3 a 5 leitores beta e um revisor técnico

**Você** · 30 min

- [ ] **Pronto quando:** Nomes confirmados e formulário de retorno pronto
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Leitores beta e revisão técnica

### 20.10 Criar a conta no Amazon KDP e cadastrar o livro em rascunho

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Livro em rascunho com capa, preço e prévia conferida
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- **Oferta:** Livro Lógica e Máquina
- Implanta: Amazon KDP

### 20.11 Enviar o depósito legal à Biblioteca Nacional até 30 dias depois de publicar

**Você** · 30 min

- [ ] **Pronto quando:** Comprovante de envio guardado
- **Precisa:** conteúdo seu pronto (livro, capítulo)
- Implanta: Depósito legal

<a id="f21"></a>

## 21 · Dados, IA e pendrives

O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot.

**Quando:** Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029)

### 21.1 Gravar o pendrive do Kali com persistência criptografada

**Você** · 1 h 30 min

```powershell
winget install --id Rufus.Rufus -e
```

- [ ] **Pronto quando:** O Kali abre pelo F12 e um arquivo salvo continua lá depois de reiniciar
- Siga kali.org/docs/usb. Antes do primeiro boot: suspenda o BitLocker, desligue o Secure Boot e, ao voltar ao Windows, religue o Secure Boot e reative o BitLocker (veja Secure Boot e BitLocker no mapa). Só contra alvos seus ou autorizados.
- Implanta: Pendrive Kali (persistência) · Rufus (grava pendrives)

### 21.2 Instalar o Arch num pendrive rápido ou SSD USB, pelo guia oficial

**Você** · 3 h 00 min

- [ ] **Pronto quando:** O Arch portátil dá boot e abre o terminal com os seus dotfiles
- Use um pendrive para a ISO e outro (64 GB ou mais, USB 3) ou um SSD USB como disco do sistema. Mesmo cuidado com Secure Boot e BitLocker.
- **Precisa:** comprar algo
- Implanta: Pendrive Arch (instalação portátil)

### 21.3 Conferir a GPU dentro do Ubuntu

**Script** · 5 min

```bash
nvidia-smi
```

- [ ] **Pronto quando:** Aparece a GTX 1650 com o driver do Windows
- Implanta: PyTorch + CUDA (WSL2)

### 21.4 Montar o laboratório de dados e de IA

**Script** · 30 min

```bash
bash scripts/wsl/lab-ia.sh
```

- [ ] **Pronto quando:** Termina com 'Pronto' e mostra a GPU vista pelo PyTorch
- Implanta: Python de dados (Polars, Jupyter) · DuckDB + Parquet · Spark (PySpark) · PyTorch + CUDA (WSL2) · MLflow (experimentos) · llama.cpp (GGUF)

### 21.5 Rodar um modelo 8B no Ollama com parte na GPU

**Você** · 15 min

```bash
ollama run llama3.1:8b
```

- [ ] **Pronto quando:** 'ollama ps' mostra o modelo dividido entre CPU e GPU e ele responde
- Mais lento que um 3B ou 4B, que cabem inteiros na placa. Use o 8B quando a qualidade importar mais que a velocidade.
- Implanta: Modelos locais: Qwen · Gemma · Llama · Ollama

### 21.6 Fazer o Data Engineering Zoomcamp e os cursos de IA, um módulo por semana

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Módulo 1 entregue no GitHub e anotado no Obsidian
- O tempo é só para começar; o curso leva 10 semanas. Para a IA vão as suas anotações, nunca o material do curso.
- Implanta: Zoomcamp de dados + cursos de IA

### 21.7 Criar o projeto dbt sobre o banco de métricas

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** 'dbt build' verde e o painel de lucro lendo os modelos
- Implanta: dbt Core

### 21.8 Subir o Airflow e agendar o dbt todo dia

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** A rotina diária aparece verde no Airflow por 3 dias seguidos
- Implanta: Airflow (orquestração)

### 21.9 Criar as contas do Hugging Face e do Kaggle (e do RunPod, só se precisar)

**Você** · 30 min

- [ ] **Pronto quando:** Token do Hugging Face no KeePassXC; Kaggle com telefone verificado para liberar a GPU
- No RunPod, só crédito pré-pago. Nunca ponha token em notebook público.
- Implanta: Hugging Face (modelos e Hub) · Kaggle · Colab (GPU grátis) · GPU por hora (RunPod e afins)

### 21.10 Montar o primeiro dataset só com conteúdo seu

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Algumas centenas de pares de pergunta e resposta revisados por você, com conjunto de teste separado
- Fontes: suas notas, exercícios, livro e aulas que você gravou. Nada de cursos de terceiros; nada de dados de alunos sem consentimento.
- Implanta: Seus datasets (só conteúdo seu) · Avaliação dos modelos

### 21.11 Primeiro fine-tuning QLoRA de um 8B no Kaggle

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Adaptador salvo no Hugging Face privado e o treino registrado no MLflow
- Implanta: Unsloth (QLoRA) · Kaggle · Colab (GPU grátis)

### 21.12 Avaliar contra o modelo base e levar o seu modelo para o Ollama

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** O seu modelo ganha do base no conjunto de teste e responde no Ollama do notebook
- Implanta: Avaliação dos modelos · llama.cpp (GGUF) · Ollama

<a id="f22"></a>

## 22 · Mais ofertas, uma por vez

Cada oferta do portfólio entra na esteira na ordem da pontuação: uma em construção e uma em validação por vez.

**Quando:** Fev a dez/2027, uma oferta por vez

**Começa quando:** A primeira venda do mini-curso aconteceu

### 22.1 Página 'meu setup' com links de afiliado

**Claude com você** · 1 h 30 min

- [ ] **Pronto quando:** Página publicada com links marcados com UTM
- **Oferta:** Afiliados (ferramentas, livros, equipamentos que você usa)
- Implanta: Site pessoal + blog (Jekyll) · Afiliados (Amazon, Hotmart…)

### 22.2 Pôr no Catálogo do HTML a chamada para o mini-curso e para a newsletter

**Claude com você** · 30 min

- [ ] **Pronto quando:** Chamadas no ar, medidas por UTM
- **Oferta:** Catálogo do HTML (gratuito)
- Implanta: Catálogo do HTML

### 22.3 Kit de aulas prontas para professores: uma disciplina que você já leciona

**Você** · 10 h 00 min

- [ ] **Pronto quando:** Kit de 1 disciplina (planos, slides, avaliações) à venda
- Material feito para a escola: reescreva do zero, no seu tempo e sem a identidade da escola, ou confirme os direitos.
- **Oferta:** Pacote de aulas prontas para professores de informática
- Implanta: Acervo (seus documentos) · Hotmart

### 22.4 Vender a planilha do Caixa da Casa antes de construir o AM Rendara

**Você** · 3 h 00 min

- [ ] **Pronto quando:** 10 planilhas vendidas
- **Oferta:** AM Rendara (finanças), começando pela planilha
- Implanta: Caixa da Casa / AM Rendara · Hotmart

### 22.5 Automação com IA para pequenos negócios: 1 implantação grátis em troca de caso

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Um negócio usando a automação e um caso escrito com autorização
- **Oferta:** Automação com IA para pequenos negócios (WhatsApp, n8n, agenda)
- Implanta: n8n · Agente atendente (WhatsApp)

### 22.6 Banco de questões para concursos: 50 questões comentadas grátis para medir a procura

**Você** · 8 h 00 min

- [ ] **Pronto quando:** 50 questões publicadas e a procura medida
- **Oferta:** Banco de questões de TI para concursos (PF, PRF, Forças Armadas)
- Implanta: Exercícios em YAML

### 22.7 Baralhos Anki de TI e concursos: o primeiro, do capítulo 1

**Você** · 3 h 00 min

- [ ] **Pronto quando:** Primeiro baralho à venda
- **Oferta:** Baralhos Anki de TI e concursos
- Implanta: Anki · Exercícios em YAML

### 22.8 Newsletter com patrocínio e vendas

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Edição semanal por 8 semanas e o primeiro patrocinador
- **Oferta:** Newsletter (patrocínio e vendas)
- Implanta: MailerLite

### 22.9 Presença digital para comércio local, oferecida a 5 clientes de sites

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Primeiro cliente mensal
- **Oferta:** Presença digital para comércio local (Google Perfil, redes, avaliações)
- Implanta: Google Perfil da Empresa · Sites para pequenas empresas

### 22.10 Sites: 3 pacotes fixos com preço público

**Você** · 3 h 00 min

- [ ] **Pronto quando:** Pacotes publicados e primeiro cliente fechado
- **Oferta:** Sites e lojas para pequenas empresas
- Implanta: Sites para pequenas empresas · Hostinger (clientes WP)

### 22.11 Suporte remoto com plano mensal para empresas

**Você** · 4 h 00 min

- [ ] **Pronto quando:** 3 empresas no plano mensal
- **Oferta:** Suporte remoto e planos mensais para empresas
- Implanta: Tailscale (VPN)

### 22.12 Implantação de ficha técnica e engenharia de cardápio para restaurantes

**Você** · 8 h 00 min

- [ ] **Pronto quando:** Um estudo de caso, com autorização do dono
- **Oferta:** Implantação de ficha técnica e engenharia de cardápio
- Implanta: AM Kaixara (PDV e cardápio)

### 22.13 AM Mentor: banco de exercícios com correção, começando pelo capítulo 1

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** Primeiros alunos usando
- **Oferta:** AM Mentor: banco de exercícios com correção
- Implanta: Exercícios em YAML

### 22.14 Canais sem rosto: 3 vídeos por semana por 8 semanas e medir

**Você** · 20 h 00 min

- [ ] **Pronto quando:** 24 vídeos publicados e o resultado medido
- **Oferta:** Canais sem rosto (YouTube, TikTok, Instagram, Facebook)
- Implanta: Agente editor de conteúdo · YouTube

### 22.15 Comunidade paga do Instituto AMS

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Comunidade aberta com os primeiros assinantes
- Só com 200 alunos pagantes.
- **Oferta:** Comunidade paga do Instituto AMS
- Implanta: Comunidade (Discord ou grupo)

### 22.16 Oficinas de robótica e programação para escolas: plano de 8 encontros

**Você** · 10 h 00 min

- [ ] **Pronto quando:** Primeira escola contratando
- **Oferta:** Oficinas de robótica e programação para escolas
- Implanta: Arduino · ESP32 · Pi · Arduino IDE 2

### 22.17 Sistemas sob encomenda, com 50% de entrada

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Primeiro contrato assinado
- **Oferta:** Sistemas sob encomenda
- Implanta: API ASP.NET Core · Next.js + Aura Design System

### 22.18 Aula de sushi e sushiman para eventos: 2 eventos de teste

**Você** · 4 h 00 min

- [ ] **Pronto quando:** 2 eventos pagos, com as regras sanitárias conferidas
- **Oferta:** Aula de sushi e sushiman para eventos
- Implanta: Agenda online (Cal.com)

### 22.19 Workshop presencial para pequenos empresários: piloto com 10 vagas

**Você** · 8 h 00 min

- [ ] **Pronto quando:** Piloto realizado com 10 inscritos pagantes
- **Oferta:** Workshops presenciais para pequenos empresários (IA, planilhas, presença digital)
- Implanta: Agenda online (Cal.com) · Mercado Pago

### 22.20 Revisar a cada trimestre as ofertas pausadas (AM Taskoro)

**Você** · 30 min

- [ ] **Pronto quando:** Decisão anotada: retomar ou manter pausada
- **Oferta:** AM Taskoro (gestão de projetos ágeis)
- Implanta: Portfólio de ofertas

<a id="f23"></a>

## 23 · Marketing pago e crescimento

Pôr dinheiro em anúncio só quando a venda orgânica provou a oferta.

**Quando:** A partir de fev/2027

**Começa quando:** O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar

### 23.1 Primeira campanha na Meta com orçamento de teste

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Campanha com CPA abaixo do de empate por 2 semanas
- **Precisa:** pagar um serviço
- Implanta: Meta Ads (Instagram, Facebook)

### 23.2 Google e YouTube Ads, depois TikTok Ads

**Você** · 3 h 00 min

- [ ] **Pronto quando:** Cada canal com a primeira campanha medida no painel
- **Precisa:** pagar um serviço
- Implanta: Google e YouTube Ads · TikTok Ads

### 23.3 Kwai, Pinterest, LinkedIn, Spotify e mídia nativa, um por vez

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Cada canal testado e mantido ou cortado pelas regras
- **Precisa:** pagar um serviço
- Implanta: Kwai Ads · Pinterest Ads · LinkedIn Ads · Spotify Ad Studio · Mídia nativa (Taboola, Outbrain)

### 23.4 Influenciadores e newsletters parceiras com cupom

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Primeira parceria medida por cupom e UTM
- **Precisa:** pagar um serviço
- Implanta: Influenciadores e newsletters

### 23.5 Abrir o programa de afiliados do mini-curso

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Primeiro afiliado vendendo
- Implanta: Programa de afiliados

### 23.6 Ligar o algoritmo de horário com 3 meses de dados de publicação

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** 80% dos posts nas melhores faixas, 20% testando
- Implanta: Algoritmo de horário

### 23.7 Canal build in public: um vídeo por semana das decisões reais

**Você** · 1 h 00 min

- [ ] **Pronto quando:** 4 vídeos seguidos publicados
- **Oferta:** Canal com rosto: construindo o Grupo AMtech em público
- Implanta: Canal build in public

### 23.8 Dublar os melhores vídeos para outros idiomas

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Um vídeo com faixa de áudio em inglês ou espanhol
- **Precisa:** pagar um serviço
- Implanta: Dublagem (YouTube + ElevenLabs)

### 23.9 Membros do YouTube quando o canal for elegível

**Você** · 30 min

- [ ] **Pronto quando:** Assinatura de membros ativa
- **Oferta:** Monetização das plataformas (YouTube, Instagram)
- Implanta: YouTube (membros)

### 23.10 Primeira formação completa (TI, Matemática ou Finanças)

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Formação gravada e à venda
- **Oferta:** Formação Téc. em Desenvolvimento de Sistemas (13 disciplinas) · Formação em Matemática · Curso de finanças pessoais (conteúdo próprio)
- Implanta: Formações (TI, Matemática, Finanças)

<a id="f24"></a>

## 24 · Linux nativo e laboratório completo

Arch com boot próprio, VMs de laboratório e a segurança física em dia.

**Quando:** 2027, conforme cada compra

### 24.1 Instalar o 2º NVMe e o Arch + Omarchy com boot próprio

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Escolha entre Windows e Arch ao ligar, cada um no seu disco
- **Precisa:** comprar algo
- Implanta: 2º NVMe (1–4 TB) · Arch + Omarchy (2º NVMe) · Gerenciador de boot

### 24.2 Aprender o Neovim aos poucos

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Uma semana editando só no Neovim
- Implanta: Neovim

### 24.3 Montar as VMs do laboratório: Kali, Arch, Ubuntu Server, Windows Server e Rocky

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Duas VMs numa rede isolada, atacante e alvo
- Implanta: VMs: Kali · Arch · Servidores

### 24.4 SSD SATA na baia livre para as VMs

**Você** · 1 h 00 min

- [ ] **Pronto quando:** VMs rodando do SSD novo
- **Precisa:** comprar algo
- Implanta: SSD SATA 2,5"

### 24.5 Chave física no GitHub, Google e Microsoft

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Login com a chave nas três contas
- **Precisa:** comprar algo
- Implanta: Chave física (YubiKey)

### 24.6 Microfone e câmera

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Gravação de teste com áudio limpo sem pós-produção
- **Precisa:** comprar algo
- Implanta: Microfone + câmera

<a id="f25"></a>

## 25 · IA dentro dos sistemas AM

Busca e assistente com os seus dados dentro de um sistema AM.

**Quando:** Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5

### 25.1 RAG com pgvector dentro do primeiro sistema AM

**Claude com você** · 8 h 00 min

- [ ] **Pronto quando:** O sistema responde perguntas com base nos dados do cliente, citando a origem
- Implanta: IA: RAG + pgvector

<a id="f26"></a>

## 26 · Sistemas AM à venda

Os sistemas viram produto por assinatura.

**Quando:** 2027

**Começa quando:** O primeiro sistema AM pronto e testado com um cliente

### 26.1 Lançar o primeiro sistema AM como SaaS, com cobrança por módulo

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Primeiro cliente pagando por assinatura
- Implanta: Sistemas AM (SaaS) · aura-licensing

### 26.2 AM Kaixara: PDV, cardápio, fichas técnicas e estoque

**Claude com você** · 40 h 00 min

- [ ] **Pronto quando:** Rodando num negócio real
- **Oferta:** AM Kaixara (PDV, ficha técnica, cardápio)
- Implanta: AM Kaixara (PDV e cardápio)

### 26.3 AM Rotara: pedidos, rotas e mapas

**Claude com você** · 40 h 00 min

- [ ] **Pronto quando:** Entregas rastreadas no mapa em tempo real
- **Oferta:** AM Rotara (pedidos e entregas)
- Implanta: AM Rotara (entregas) · PostGIS + MapLibre

### 26.4 Serviços aura- compartilhados, só quando um sistema precisar

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Um serviço compartilhado usado por dois sistemas
- Implanta: Serviços aura- (10) · Datomic local

### 26.5 App de delivery com a marca do restaurante (white-label)

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** Primeiro restaurante usando o app com a marca dele
- Comece oferecendo a 3 restaurantes que pagam 23% ao iFood.
- **Oferta:** App de delivery com a marca do restaurante (white-label)
- Implanta: AM Rotara (entregas)

<a id="f27"></a>

## 27 · CNPJ e formalização

Sair do CPF na hora certa, com nota fiscal e cobrança automáticas.

**Quando:** Quando a renda pedir

**Começa quando:** A renda passou do valor de virada definido com o contador

### 27.1 Abrir a AMtech Tecnologia (ME no Simples, sócio único)

**Você** · 4 h 00 min

- [ ] **Pronto quando:** CNPJ ativo, conta PJ aberta e contador contratado
- **Precisa:** pagar um serviço
- Implanta: CNPJ (futuro) · 3 CNPJs por frente

### 27.2 Certificado digital e-CNPJ

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Certificado instalado e guardado no KeePassXC
- **Precisa:** pagar um serviço
- Implanta: Certificado digital (e-CNPJ)

### 27.3 Nota fiscal automática pela API de NFS-e

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Venda de teste emite nota sozinha
- Implanta: API de NFS-e (ex.: Focus NFe)

### 27.4 Cobrança recorrente por Pix Automático

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Assinatura de teste cobrada por Pix
- Implanta: Pix Automático + gateway (ex.: Asaas)

<a id="f28"></a>

## 28 · Agentes do grupo

Atendimento, orçamento, cobrança e análise rodando com a sua aprovação.

**Quando:** Junto com o primeiro CNPJ

**Começa quando:** Clientes e vendas recorrentes

### 28.1 Analista semanal: o que funcionou e o que mudar

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Relatório toda segunda no Telegram
- Implanta: Analista semanal

### 28.2 Atendente do WhatsApp com passagem para você

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Dúvida comum respondida sozinha; o resto chega para você
- Implanta: Agente atendente (WhatsApp)

### 28.3 Orçamentista de sites e sistemas

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Rascunho de orçamento em 5 minutos, revisado por você
- Implanta: Agente orçamentista

### 28.4 Cobrador educado (lembrete antes e depois do vencimento)

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Atraso cai pela metade
- Implanta: Agente cobrador

### 28.5 Pós-venda: NPS e pedido de avaliação

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** NPS medido em cada venda
- Implanta: Agente pós-venda

### 28.6 Organizador fiscal para o contador

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Pasta do mês pronta no dia 5
- Implanta: Organizador fiscal

### 28.7 Comprador com estoque mínimo

**Claude com você** · 3 h 00 min

- [ ] **Pronto quando:** Pedido de reposição sugerido antes de faltar
- Implanta: Agente comprador

<a id="f29"></a>

## 29 · Editora: depois do primeiro livro

O mesmo livro em mais formatos, públicos e idiomas.

**Quando:** Depois do primeiro livro

**Começa quando:** O primeiro livro publicado

### 29.1 Gráfica sob demanda no Brasil

**Você** · 2 h 00 min

- [ ] **Pronto quando:** Cópia de prova aprovada
- **Precisa:** pagar um serviço
- Implanta: Gráfica sob demanda (Brasil)

### 29.2 Kit edição especial

**Você** · 4 h 00 min

- [ ] **Pronto quando:** Primeira tiragem vendida
- **Precisa:** pagar um serviço
- **Oferta:** Kit do livro e edição do professor
- Implanta: Kit edição especial

### 29.3 Curso por seção do livro, com animações

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Primeira seção gravada e à venda
- Implanta: Curso por seção · Manim (animações)

### 29.4 Edição do professor com licença para escolas

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Primeira escola licenciada
- **Oferta:** Adoção do livro por escolas
- Implanta: Edição do professor

### 29.5 Traduções para espanhol e inglês

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** Primeiro volume traduzido e revisado
- **Precisa:** pagar um serviço
- **Oferta:** Traduções do livro
- Implanta: Traduções (espanhol, inglês)

<a id="f30"></a>

## 30 · Distribuído, plataforma e segunda nuvem

O que pesa em vaga pleno e sênior.

**Quando:** 2028

### 30.1 RabbitMQ e depois Kafka entre dois sistemas AM

**Claude com você** · 10 h 00 min

- [ ] **Pronto quando:** Evento de um sistema chega no outro sem chamada direta
- Implanta: RabbitMQ · Kafka

### 30.2 Kubernetes local com kind, kubectl, Helm e k9s

**Você** · 10 h 00 min

- [ ] **Pronto quando:** Um sistema AM rodando no cluster local
- Implanta: Kubernetes local (kind) · kubectl · Helm · k9s

### 30.3 Logs e rastreamento com Loki e Tempo no Grafana

**Claude com você** · 4 h 00 min

- [ ] **Pronto quando:** Uma requisição seguida de ponta a ponta
- Implanta: Loki + Tempo

### 30.4 AWS: Cloud Practitioner e o mesmo sistema rodando lá

**Você** · 20 h 00 min

- [ ] **Pronto quando:** Certificação e post comparando Azure e AWS
- **Precisa:** pagar um serviço
- Implanta: AWS

### 30.5 Google Cloud só o básico, quando um projeto de IA ou dados pedir

**Você** · 5 h 00 min

- [ ] **Pronto quando:** Um serviço usado num projeto real
- Implanta: Google Cloud

### 30.6 App mobile dos sistemas AM com .NET MAUI

**Claude com você** · 20 h 00 min

- [ ] **Pronto quando:** App publicado para teste interno
- Implanta: App mobile (.NET MAUI)

<a id="f31"></a>

## 31 · Infraestrutura própria

Servidor em casa e máquina de IA quando o grupo pedir.

**Quando:** 2028, quando o grupo pedir

### 31.1 Servidor caseiro com backup local e os serviços 24 horas

**Você** · 8 h 00 min

- [ ] **Pronto quando:** n8n, banco e painel rodando no servidor; notebook livre
- **Precisa:** comprar algo
- Implanta: Servidor caseiro (NAS + serviços)

### 31.2 Tailscale entre notebook, celular e servidor

**Você** · 1 h 00 min

- [ ] **Pronto quando:** Acesso ao servidor de fora de casa sem abrir porta
- Implanta: Tailscale (VPN)

### 31.3 Workstation com GPU para treinar e gerar voz e vídeo em casa

**Você** · 8 h 00 min

- [ ] **Pronto quando:** Fine-tuning de 8B rodando local
- **Precisa:** comprar algo
- Implanta: Workstation com GPU

<a id="f32"></a>

## 32 · Negócios do grupo em Barbacena

Um negócio por vez, cada um só depois que o anterior passa no portão.

**Quando:** Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano

**Começa quando:** Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta

### 32.1 Planejador do grupo com os números reais

**Claude com você** · 2 h 00 min

- [ ] **Pronto quando:** Capital mínimo e portões calculados com os seus dados
- Implanta: Planejador do Grupo

### 32.2 A1 · AMtech Software

**Você** · 40 h 00 min

- [ ] **Pronto quando:** 3 meses seguidos com lucro e 10 clientes pagantes
- **Precisa:** pagar um serviço
- Implanta: AMtech Software (projetos e SaaS)

### 32.3 A2 · Loja AMtech, peças sob encomenda, ponto de retirada e Maker

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Loja acima do equilíbrio por 3 meses e técnico que abre e fecha sem você
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Assistência técnica · Peças e acessórios sem estoque · Ponto de retirada (Shopee e Mercado Livre) · AMtech Maker (robótica e automação)
- Implanta: Loja AMtech (assistência) · Peças sem estoque (sob encomenda) · Ponto de retirada (Shopee e ML) · AMtech Maker (robótica) · Anatel e Inmetro · Google Perfil da Empresa

### 32.4 B1 · AM Entregas e Mercado Envios Flex

**Você** · 80 h 00 min

- [ ] **Pronto quando:** 1.000 entregas por mês e 5 contratos fixos
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** AM Entregas
- Implanta: AM Entregas (moto e carro) · Mercado Envios Flex

### 32.5 B2 · AM Delivery

**Você** · 80 h 00 min

- [ ] **Pronto quando:** 20 lojistas ativos e 1.500 pedidos por mês
- **Precisa:** pagar um serviço
- **Oferta:** AM Delivery · Licença do AM Delivery para outras cidades
- Implanta: AM Delivery (várias empresas)

### 32.6 C1 · Sushi, delivery primeiro

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Lucro por 3 meses e sushiman que toca a noite sem você
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Sushi (delivery)
- Implanta: Sushi (delivery) · Vigilância sanitária (RDC 216) · iFood (canal de descoberta)

### 32.7 C2 · Padaria com café da manhã e almoço

**Você** · 80 h 00 min

- [ ] **Pronto quando:** Gerente no comando e CMV dentro da meta por 3 meses
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Padaria com café da manhã e almoço
- Implanta: Padaria + café da manhã + almoço

### 32.8 C3 · Cafeteria

**Você** · 40 h 00 min

- [ ] **Pronto quando:** Cafeteria acima do equilíbrio
- **Precisa:** comprar algo, pagar um serviço
- **Oferta:** Cafeteria
- Implanta: Cafeteria

<a id="f33"></a>

## 33 · Estudo contínuo

As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém.

**Quando:** Contínuo, desde a semana 2

### 33.1 Pedir o GitHub Education como professor e ligar o Copilot

**Você** · 20 min

- [ ] **Pronto quando:** Benefícios aprovados e Copilot ativo no VS Code
- Implanta: GitHub Education · GitHub Copilot

### 33.2 Montar as trilhas: Microsoft Learn, AWS Skill Builder, roadmap.sh e laboratórios do TryHackMe

**Você** · 30 min

- [ ] **Pronto quando:** Uma trilha de cada em andamento, anotada no Obsidian
- Implanta: Microsoft Learn + AWS Skill Builder · roadmap.sh + Akita · TryHackMe / Hack The Box

### 33.3 Organizar as contas de aluno (Alura, Rocketseat, DIO, Udemy)

**Você** · 15 min

- [ ] **Pronto quando:** Acessos no KeePassXC e cursos em andamento listados no Obsidian
- A licença é para assistir e estudar. Para a IA vão só as suas anotações e os seus projetos.
- Implanta: Alura · Rocketseat · DIO · Udemy

### 33.4 Criar os baralhos do Anki (comandos, conceitos, certificações)

**Você** · 20 min

- [ ] **Pronto quando:** Revisão do dia feita no notebook e no celular
- Implanta: Anki

<a id="quando-entra-cada-bloco"></a>

## Quando entra cada bloco

Camada por camada, na mesma ordem do mapa. O número é o passo do roteiro.

### Operação do grupo (esteira, marca, qualidade)

| Bloco | Passo | Quando |
|---|---|---|
| Portfólio de ofertas | 8.7, 14.14, 22.20 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Esteira de ofertas | 8.7, 14.14 | Semanas 3 e 4 · nov/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Padrão de qualidade | 14.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Marca pessoal Alan Mateus | 11.1, 13.1 | Semana 5 · nov/2026; Semanas 6 e 7 · dez/2026 |
| NPS e avaliações | 14.15 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| CRM único + LGPD | 14.9 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Flywheel de conteúdo | 11.5, 11.6 | Semana 5 · nov/2026 |
| Canal build in public | 23.7 | A partir de fev/2027 |
| Agente atendente (WhatsApp) | 22.5, 28.2 | Fev a dez/2027, uma oferta por vez; Junto com o primeiro CNPJ |
| Agente orçamentista | 28.3 | Junto com o primeiro CNPJ |
| Agente cobrador | 28.4 | Junto com o primeiro CNPJ |
| Agente pós-venda | 28.5 | Junto com o primeiro CNPJ |
| Agente editor de conteúdo | 11.5, 22.14 | Semana 5 · nov/2026; Fev a dez/2027, uma oferta por vez |
| Analista semanal | 28.1 | Junto com o primeiro CNPJ |
| Organizador fiscal | 28.6 | Junto com o primeiro CNPJ |
| Revisor de oferta | 14.14 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Agente comprador | 28.7 | Junto com o primeiro CNPJ |
| Diagnóstico do notebook | 0.2 | Antes de tudo · semana 1 (out/2026) |
| Roteiro de implantação | 0.6, 16.4 | Antes de tudo · semana 1 (out/2026); Semana 11 · jan/2027 |
| Instaladores (PowerShell e bash) | 3.1, 4.4 | Semana 1 · out/2026; Semana 2 · nov/2026 |
| Verificadores | 3.9, 4.10, 10.3, 16.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Pipeline de conteúdo | 11.4, 11.5, 16.2 | Semana 5 · nov/2026; Semana 11 · jan/2027 |
| Acervo (seus documentos) | 8.3, 8.4, 8.5, 22.3 | Semanas 3 e 4 · nov/2026; Fev a dez/2027, uma oferta por vez |

### Público e canais

| Bloco | Passo | Quando |
|---|---|---|
| Meta Business Suite | 13.5 | Semanas 6 e 7 · dez/2026 |
| Instagram | 13.1, 17.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| YouTube | 13.1, 22.14 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| LinkedIn | 13.1, 17.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| WhatsApp Business | 13.2, 17.6 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Google Perfil da Empresa | 22.9, 32.3 | Fev a dez/2027, uma oferta por vez; Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Comunidade (Discord ou grupo) | 14.10, 22.15 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Busca Google (SEO) | 13.12 | Semanas 6 e 7 · dez/2026 |
| Alunos e ex-alunos | 13.10 | Semanas 6 e 7 · dez/2026 |
| Recrutadores | 18.8 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| TikTok | 13.1 | Semanas 6 e 7 · dez/2026 |
| Facebook | 13.1 | Semanas 6 e 7 · dez/2026 |

### Marketing, automação e medição

| Bloco | Passo | Quando |
|---|---|---|
| Meta Ads (Instagram, Facebook) | 23.1 | A partir de fev/2027 |
| Isca grátis + sequência de e-mails | 13.6, 17.5 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| MailerLite | 13.6, 17.5, 22.8 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027; Fev a dez/2027, uma oferta por vez |
| Postiz (agendador) | 10.8 | Semana 4 · nov/2026 |
| Aprovação no celular | 11.3 | Semana 5 · nov/2026 |
| Telegram (avisos) | 11.3 | Semana 5 · nov/2026 |
| n8n | 10.1, 10.2, 10.5, 10.7, 22.5 | Semana 4 · nov/2026; Fev a dez/2027, uma oferta por vez |
| Algoritmo de horário | 23.6 | A partir de fev/2027 |
| Tags de conversão (Pixel, Google…) | 13.5, 17.4 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Padrão de UTM | 14.12, 17.4 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Google e YouTube Ads | 23.2 | A partir de fev/2027 |
| TikTok Ads | 23.2 | A partir de fev/2027 |
| Regras de corte | 14.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Lucro por Venda (calculadora) | 14.13 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Webhooks de venda | 15.1, 15.2, 16.3, 17.7 | Semana 11 · jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Banco de métricas (PostgreSQL) | 10.2, 10.7, 15.3 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| Painel de lucro (Grafana) | 15.4, 16.3 | Semana 11 · jan/2027 |
| Programa de afiliados | 23.5 | A partir de fev/2027 |
| Prospecção de parceiros | 14.16 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Dublagem (YouTube + ElevenLabs) | 23.8 | A partir de fev/2027 |
| Spotify Ad Studio | 23.3 | A partir de fev/2027 |
| Kwai Ads | 23.3 | A partir de fev/2027 |
| Pinterest Ads | 23.3 | A partir de fev/2027 |
| LinkedIn Ads | 23.3 | A partir de fev/2027 |
| Mídia nativa (Taboola, Outbrain) | 23.3 | A partir de fev/2027 |
| Influenciadores e newsletters | 23.4 | A partir de fev/2027 |

### Plataformas de venda e recebimento

| Bloco | Passo | Quando |
|---|---|---|
| Pix Automático + gateway (ex.: Asaas) | 27.4 | Quando a renda pedir |
| Agenda online (Cal.com) | 14.8, 22.18, 22.19 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| CRM simples (planilha) | 14.9 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Hotmart | 14.5, 17.3, 17.7, 22.3, 22.4 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027; Fev a dez/2027, uma oferta por vez |
| Kiwify | 14.5, 17.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Eduzz | 14.6, 17.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Udemy | 14.6, 17.8 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| DIO (parceria) | 14.6 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| YouTube (membros) | 23.9 | A partir de fev/2027 |
| Mercado Pago | 14.7, 22.19 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |
| Afiliados (Amazon, Hotmart…) | 14.11, 22.1 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |

### Pessoa física: impostos e finanças

| Bloco | Passo | Quando |
|---|---|---|
| Registro de marca (INPI) | 14.17 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Termos, privacidade (LGPD) e contratos | 14.4 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Certificado digital (e-CNPJ) | 27.2 | Quando a renda pedir |
| API de NFS-e (ex.: Focus NFe) | 27.3 | Quando a renda pedir |
| CNPJ (futuro) | 27.1 | Quando a renda pedir |
| gov.br (prata ou ouro) | 2.6, 14.1 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Carnê-leão (Receita Federal) | 14.18, 17.7 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Declaração anual do IR | 14.19 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Conta bancária separada (CPF) | 2.6, 14.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semanas 8 a 10 · dez/2026 a jan/2027 |
| Contador | 14.3 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Caixa da Casa / AM Rendara | 14.20, 22.4 | Semanas 8 a 10 · dez/2026 a jan/2027; Fev a dez/2027, uma oferta por vez |

### Vitrine web (sites e domínio)

| Bloco | Passo | Quando |
|---|---|---|
| E-mail profissional (enviar e receber) | 13.4 | Semanas 6 e 7 · dez/2026 |
| Domínio (Registro.br) | 13.3 | Semanas 6 e 7 · dez/2026 |
| Site pessoal + blog (Jekyll) | 13.7, 22.1 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Instituto AMS | 13.8, 17.4 | Semanas 6 e 7 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Site Grupo AMtech | 13.9 | Semanas 6 e 7 · dez/2026 |
| Catálogo do HTML | 13.9, 22.2 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Umami (analytics) | 13.11 | Semanas 6 e 7 · dez/2026 |
| Google Search Console | 13.12 | Semanas 6 e 7 · dez/2026 |
| Hostinger (clientes WP) | 13.13, 22.10 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |

### Produtos (o que você vende)

| Bloco | Passo | Quando |
|---|---|---|
| Mini-curso Lógica de Programação | 14.5, 17.1 | Semanas 8 a 10 · dez/2026 a jan/2027; Semanas 12 a 15 · jan a fev/2027 |
| Formações (TI, Matemática, Finanças) | 23.10 | A partir de fev/2027 |
| Templates e código-fonte | 18.7 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Livro Lógica e Máquina | 20.2 | Quando o capítulo 1 estiver pronto |
| Aulas particulares | 14.8 | Semanas 8 a 10 · dez/2026 a jan/2027 |
| Sites para pequenas empresas | 13.13, 22.9, 22.10 | Semanas 6 e 7 · dez/2026; Fev a dez/2027, uma oferta por vez |
| Sistemas AM (SaaS) | 26.1 | 2027 |

### Negócios do grupo (Barbacena)

| Bloco | Passo | Quando |
|---|---|---|
| AMtech Software (projetos e SaaS) | 32.2 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Loja AMtech (assistência) | 32.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Peças sem estoque (sob encomenda) | 32.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Ponto de retirada (Shopee e ML) | 32.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AMtech Maker (robótica) | 32.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Entregas (moto e carro) | 32.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Mercado Envios Flex | 32.4 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| AM Delivery (várias empresas) | 32.5 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Sushi (delivery) | 32.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Cafeteria | 32.8 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Padaria + café da manhã + almoço | 32.7 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| 3 CNPJs por frente | 27.1 | Quando a renda pedir |
| Planejador do Grupo | 32.1 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| iFood (canal de descoberta) | 32.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Vigilância sanitária (RDC 216) | 32.6 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |
| Anatel e Inmetro | 32.3 | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano |

### Editora AMS Silva (produção de livros)

| Bloco | Passo | Quando |
|---|---|---|
| Selo Editora AMS Silva | 20.7 | Quando o capítulo 1 estiver pronto |
| Repositório do livro | 20.2 | Quando o capítulo 1 estiver pronto |
| Seu modelo de criação | 20.1 | Quando o capítulo 1 estiver pronto |
| Fonte única (Markdown + Pandoc) | 20.2 | Quando o capítulo 1 estiver pronto |
| Exercícios em YAML | 20.2, 22.6, 22.7, 22.13 | Quando o capítulo 1 estiver pronto; Fev a dez/2027, uma oferta por vez |
| Pranchas TikZ e SVG | 4.4 | Semana 2 · nov/2026 |
| Classe LaTeX do livro | 20.2 | Quando o capítulo 1 estiver pronto |
| Pipeline do livro (CI) | 20.2 | Quando o capítulo 1 estiver pronto |
| Revisão automática (LanguageTool, Vale) | 20.2 | Quando o capítulo 1 estiver pronto |
| Agentes da editora | 20.5 | Quando o capítulo 1 estiver pronto |
| Leitores beta e revisão técnica | 20.9 | Quando o capítulo 1 estiver pronto |
| Errata e edições | 20.2 | Quando o capítulo 1 estiver pronto |
| ISBN + código de barras (CBL) | 20.8 | Quando o capítulo 1 estiver pronto |
| Ficha catalográfica | 20.8 | Quando o capítulo 1 estiver pronto |
| Depósito legal | 20.11 | Quando o capítulo 1 estiver pronto |
| Amazon KDP | 20.10 | Quando o capítulo 1 estiver pronto |
| Gráfica sob demanda (Brasil) | 29.1 | Depois do primeiro livro |
| Kit edição especial | 29.2 | Depois do primeiro livro |
| Curso por seção | 29.3 | Depois do primeiro livro |
| Edição do professor | 29.4 | Depois do primeiro livro |
| Traduções (espanhol, inglês) | 29.5 | Depois do primeiro livro |
| Quadro de referências | 20.6 | Quando o capítulo 1 estiver pronto |
| Matriz de editais | 20.6 | Quando o capítulo 1 estiver pronto |
| Projeto do capítulo | 20.1 | Quando o capítulo 1 estiver pronto |
| Mapa de pré-requisitos | 20.1 | Quando o capítulo 1 estiver pronto |
| Seu método (metodo.yaml) | 20.1 | Quando o capítulo 1 estiver pronto |
| Acervos de imagens (APIs) | 20.3 | Quando o capítulo 1 estiver pronto |
| Busca automática de imagens | 20.3 | Quando o capítulo 1 estiver pronto |
| Filtro de licença e fichas | 20.3 | Quando o capítulo 1 estiver pronto |
| Folha de contato (artefato) | 20.3 | Quando o capítulo 1 estiver pronto |
| Créditos e legendas | 20.3 | Quando o capítulo 1 estiver pronto |
| Figuras por código (Matplotlib…) | 20.4 | Quando o capítulo 1 estiver pronto |
| CircuiTikZ | 4.4 | Semana 2 · nov/2026 |
| Geradores de tabelas | 20.4 | Quando o capítulo 1 estiver pronto |
| Manim (animações) | 29.3 | Depois do primeiro livro |
| Texto alternativo | 20.4 | Quando o capítulo 1 estiver pronto |

### Estudo e carreira

| Bloco | Passo | Quando |
|---|---|---|
| Microsoft Learn + AWS Skill Builder | 33.2 | Contínuo, desde a semana 2 |
| TryHackMe / Hack The Box | 33.2 | Contínuo, desde a semana 2 |
| Alura · Rocketseat · DIO · Udemy | 33.3 | Contínuo, desde a semana 2 |
| Anki | 3.2, 22.7, 33.4 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez; Contínuo, desde a semana 2 |
| roadmap.sh + Akita | 33.2 | Contínuo, desde a semana 2 |
| GitHub Education | 33.1 | Contínuo, desde a semana 2 |
| Zoomcamp de dados + cursos de IA | 21.6 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |

### Produção de conteúdo

| Bloco | Passo | Quando |
|---|---|---|
| OBS Studio | 3.2, 12.1, 17.2 | Semana 1 · out/2026; Semana 5 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| DaVinci Resolve ou Kdenlive | 3.7, 12.3, 17.2 | Semana 1 · out/2026; Semana 5 · dez/2026; Semanas 12 a 15 · jan a fev/2027 |
| Audacity | 3.2, 12.2 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Canva · Krita · Inkscape | 3.2, 12.4 | Semana 1 · out/2026; Semana 5 · dez/2026 |
| Whisper (local) | 4.4, 11.6 | Semana 2 · nov/2026; Semana 5 · nov/2026 |
| Voz clonada (ElevenLabs) | 12.5 | Semana 5 · dez/2026 |

### Nuvem, código e entrega

| Bloco | Passo | Quando |
|---|---|---|
| Armazenamento de arquivos (Blob/R2) | 19.4 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| E-mail transacional (Resend, SES…) | 19.5 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| SonarQube Cloud | 18.5 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Projects · ADRs · MkDocs | 5.5 | Semana 2 · nov/2026 |
| Dependabot + CodeQL | 5.3 | Semana 2 · nov/2026 |
| Google Cloud | 30.5 | 2028 |
| GitHub | 2.6, 5.1, 5.4 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 2 · nov/2026 |
| GitHub Actions | 5.2, 16.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| GHCR (imagens) | 18.6 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| GitHub Pages | 13.7 | Semanas 6 e 7 · dez/2026 |
| Cloudflare (DNS, Pages, e-mail) | 13.3, 13.8, 15.1, 19.6 | Semanas 6 e 7 · dez/2026; Semana 11 · jan/2027; Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Vercel | 19.6 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Azure | 19.2, 19.3, 19.6 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| AWS | 30.4 | 2028 |
| Backblaze B2 (backup) | 7.2 | Semana 3 · nov/2026 |
| GPU por hora (RunPod e afins) | 21.9 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Google Drive (seus documentos) | 0.5, 8.1 | Antes de tudo · semana 1 (out/2026); Semanas 3 e 4 · nov/2026 |

### Aplicação: sistemas AM (Aura)

| Bloco | Passo | Quando |
|---|---|---|
| OpenAPI + Scalar | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| PostGIS + MapLibre | 26.3 | 2027 |
| Storybook | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Clean Arch + DDD | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| EF Core + Npgsql | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| SignalR | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Multi-tenant (RLS) | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Testes: xUnit, Playwright, k6 | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Serviços aura- (10) | 26.4 | 2027 |
| Next.js + Aura Design System | 18.1, 22.17 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6; Fev a dez/2027, uma oferta por vez |
| API ASP.NET Core | 18.1, 22.17 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6; Fev a dez/2027, uma oferta por vez |
| Keycloak / Entra ID | 18.2 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| IA: RAG + pgvector | 25.1 | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 |
| aura-licensing | 26.1 | 2027 |
| aura-status | 19.7 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| AM Kaixara (PDV e cardápio) | 22.12, 26.2 | Fev a dez/2027, uma oferta por vez; 2027 |
| AM Rotara (entregas) | 26.3, 26.5 | 2027 |
| App mobile (.NET MAUI) | 30.6 | 2028 |

### Observabilidade

| Bloco | Passo | Quando |
|---|---|---|
| Sentry (erros) | 18.4 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Uptime Kuma | 10.6 | Semana 4 · nov/2026 |
| Seq (logs) | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Loki + Tempo | 30.3 | 2028 |
| OpenTelemetry | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Prometheus | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Grafana | 10.4, 15.4 | Semana 4 · nov/2026; Semana 11 · jan/2027 |
| .NET Aspire | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |

### Containers, Kubernetes e infra como código

| Bloco | Passo | Quando |
|---|---|---|
| Caddy (proxy + HTTPS) | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Mailpit | 18.3 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Kafka | 30.1 | 2028 |
| kubectl · Helm · k9s | 30.2 | 2028 |
| Azure CLI · AWS CLI | 19.1 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| Datomic local | 26.4 | 2027 |
| Docker + Compose | 4.2, 10.2 | Semana 2 · nov/2026; Semana 4 · nov/2026 |
| PostgreSQL | 10.2, 18.1 | Semana 4 · nov/2026; Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| Redis | 18.1 | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| RabbitMQ | 30.1 | 2028 |
| Kubernetes local (kind) | 30.2 | 2028 |
| Terraform | 19.1, 19.3 | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |

### Claude: recursos, conectores e plugins

| Bloco | Passo | Quando |
|---|---|---|
| Projects + memória | 9.1 | Semana 4 · nov/2026 |
| Artifacts (Docs, Slides, Sheets…) | 9.1 | Semana 4 · nov/2026 |
| Pesquisa aprofundada | 9.1 | Semana 4 · nov/2026 |
| Tarefas agendadas | 9.1 | Semana 4 · nov/2026 |
| Claude in Chrome + uso do computador | 3.6 | Semana 1 · out/2026 |
| Claude (assinatura e API) | 11.2 | Semana 5 · nov/2026 |
| Conector Google (Gmail, Drive…) | 2.3, 9.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 4 · nov/2026 |
| Conectores Canva + Figma | 9.2, 12.4 | Semana 4 · nov/2026; Semana 5 · dez/2026 |
| Conector MailerLite | 9.2, 13.6 | Semana 4 · nov/2026; Semanas 6 e 7 · dez/2026 |
| Vercel · AWS · Microsoft Learn | 9.2 | Semana 4 · nov/2026 |
| Conector Upwork | 9.2 | Semana 4 · nov/2026 |
| Lovable + Supabase | 9.2 | Semana 4 · nov/2026 |
| Notion · monday · GitBook · Stripe | 9.2 | Semana 4 · nov/2026 |
| Plugins: small- business + marketing | 9.3 | Semana 4 · nov/2026 |
| Plugins: engineering + design | 9.3 | Semana 4 · nov/2026 |
| Plugins: finance + Fiscal.ai | 9.3 | Semana 4 · nov/2026 |
| Plugins: Hostinger · Adobe · Cloudinary | 9.3 | Semana 4 · nov/2026 |
| Conector Cloudflare | 9.2 | Semana 4 · nov/2026 |
| Conector vidIQ | 9.2 | Semana 4 · nov/2026 |

### Assistentes de IA (chat, pesquisa e estudo)

| Bloco | Passo | Quando |
|---|---|---|
| Claude (app) | 9.1 | Semana 4 · nov/2026 |
| ChatGPT | 9.4 | Semana 4 · nov/2026 |
| Gemini (pago) | 9.4 | Semana 4 · nov/2026 |
| NotebookLM | 6.7 | Semana 2 · nov/2026 |
| Grok | 9.4 | Semana 4 · nov/2026 |
| DeepSeek | 9.4 | Semana 4 · nov/2026 |
| Codex (OpenAI) | 9.4 | Semana 4 · nov/2026 |
| Agentes de código do Google | 9.4 | Semana 4 · nov/2026 |
| Perplexity | 9.4 | Semana 4 · nov/2026 |
| GitHub Copilot | 33.1 | Contínuo, desde a semana 2 |

### Dados e treino de IA

| Bloco | Passo | Quando |
|---|---|---|
| Python de dados (Polars, Jupyter) | 21.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| DuckDB + Parquet | 21.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| dbt Core | 21.7 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Airflow (orquestração) | 21.8 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Spark (PySpark) | 21.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Seus datasets (só conteúdo seu) | 21.10 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| PyTorch + CUDA (WSL2) | 21.3, 21.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Hugging Face (modelos e Hub) | 21.9 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Unsloth (QLoRA) | 21.11 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Kaggle · Colab (GPU grátis) | 21.9, 21.11 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| MLflow (experimentos) | 21.4 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Avaliação dos modelos | 21.10, 21.12 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| llama.cpp (GGUF) | 21.4, 21.12 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |

### Agentes de IA e sandbox

| Bloco | Passo | Quando |
|---|---|---|
| Modelos locais: Qwen · Gemma · Llama | 6.4, 21.5 | Semana 2 · nov/2026; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Base de conhecimento (RAG) das suas notas | 6.7, 8.6 | Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Claude Code | 6.1 | Semana 2 · nov/2026 |
| ai-jail | 6.2 | Semana 2 · nov/2026 |
| ai-memory | 6.6 | Semana 2 · nov/2026 |
| Servidores MCP | 6.5 | Semana 2 · nov/2026 |
| CLAUDE.md, agentes e skills (seus) | 6.3 | Semana 2 · nov/2026 |
| Ollama | 6.4, 21.5, 21.12 | Semana 2 · nov/2026; Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |

### Linux (Ubuntu no WSL2, Arch no 2º disco)

| Bloco | Passo | Quando |
|---|---|---|
| Neovim | 24.2 | 2027, conforme cada compra |
| nmap · dig · curl | 4.4 | Semana 2 · nov/2026 |
| Ubuntu (WSL2) | 4.1, 4.5 | Semana 2 · nov/2026 |
| Git + SSH + gh | 4.4, 4.6 | Semana 2 · nov/2026 |
| .NET 10 · Node · Python | 4.4 | Semana 2 · nov/2026 |
| TeX Live | 4.4 | Semana 2 · nov/2026 |
| gitleaks · Trivy | 4.4 | Semana 2 · nov/2026 |
| dotfiles | 4.7 | Semana 2 · nov/2026 |
| Arch + Omarchy (2º NVMe) | 24.1 | 2027, conforme cada compra |

### Windows 11, apps e máquinas virtuais

| Bloco | Passo | Quando |
|---|---|---|
| Tailscale (VPN) | 22.11, 31.2 | Fev a dez/2027, uma oferta por vez; 2028, quando o grupo pedir |
| .wslconfig + localhost | 3.2 | Semana 1 · out/2026 |
| Terminal · PowerShell · winget | 3.2 | Semana 1 · out/2026 |
| Excalidraw / draw.io | 3.2 | Semana 1 · out/2026 |
| Unity · Cocos | 3.8 | Semana 1 · out/2026 |
| Gerenciador de boot | 24.1 | 2027, conforme cada compra |
| NitroSense + drivers AMD e NVIDIA | 1.3 | Semana 1 · out/2026 |
| 7-Zip | 3.2 | Semana 1 · out/2026 |
| PowerToys | 3.2 | Semana 1 · out/2026 |
| SumatraPDF | 3.2 | Semana 1 · out/2026 |
| ShareX | 3.2 | Semana 1 · out/2026 |
| LibreOffice | 3.2 | Semana 1 · out/2026 |
| Firefox (2º navegador) | 3.2 | Semana 1 · out/2026 |
| Windows 11 Home | 0.3, 0.4, 1.3 | Antes de tudo · semana 1 (out/2026); Semana 1 · out/2026 |
| VS Code | 3.2, 3.5 | Semana 1 · out/2026 |
| Obsidian + Git | 3.2, 4.8, 8.4 | Semana 1 · out/2026; Semana 2 · nov/2026; Semanas 3 e 4 · nov/2026 |
| Syncthing | 2.8, 3.2, 4.9 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 1 · out/2026; Semana 2 · nov/2026 |
| DBeaver · Bruno | 3.2 | Semana 1 · out/2026 |
| Navegador + Claude in Chrome | 2.4, 2.9, 3.6 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 1 · out/2026 |
| VirtualBox | 3.2 | Semana 1 · out/2026 |
| Wireshark | 3.2 | Semana 1 · out/2026 |
| VMs: Kali · Arch · Servidores | 24.3 | 2027, conforme cada compra |
| Arduino IDE 2 | 3.2, 22.16 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez |
| Rufus (grava pendrives) | 21.1 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |

### Segurança e cofre

| Bloco | Passo | Quando |
|---|---|---|
| Commits assinados (chave SSH) | 4.6, 16.1 | Semana 2 · nov/2026; Semana 11 · jan/2027 |
| restic (backup criptografado) | 7.1, 7.4, 10.7 | Semana 3 · nov/2026; Semana 4 · nov/2026 |
| Chave física (YubiKey) | 24.5 | 2027, conforme cada compra |
| TPM + Secure Boot | 3.3 | Semana 1 · out/2026 |
| BitLocker | 3.3 | Semana 1 · out/2026 |
| Defender + Firewall | 3.4 | Semana 1 · out/2026 |
| KeePassXC | 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.10, 2.11, 2.12 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 |
| App 2FA (celular) | 1.4, 2.3, 2.6 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 |
| Backup 3-2-1 | 2.10, 7.1, 7.2, 7.3, 8.2 | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 3 · nov/2026; Semanas 3 e 4 · nov/2026 |

### Hardware

| Bloco | Passo | Quando |
|---|---|---|
| Nobreak | 1.2 | Semana 1 · out/2026 |
| Base com cooler | 1.2 | Semana 1 · out/2026 |
| SSD SATA 2,5" | 24.4 | 2027, conforme cada compra |
| Acer Nitro (32 GB, GTX 1650) | 0.2, 1.2 | Antes de tudo · semana 1 (out/2026); Semana 1 · out/2026 |
| 2º NVMe (1–4 TB) | 24.1 | 2027, conforme cada compra |
| 2º monitor | 1.2 | Semana 1 · out/2026 |
| Microfone + câmera | 24.6 | 2027, conforme cada compra |
| Celular | 1.2, 2.8, 4.9 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 2 · nov/2026 |
| Disco externo | 1.1, 1.2, 2.10, 7.1 | Semana 1 · out/2026; Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; Semana 3 · nov/2026 |
| Pendrive Kali (persistência) | 21.1 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Pendrive Arch (instalação portátil) | 21.2 | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| Arduino · ESP32 · Pi | 1.2, 22.16 | Semana 1 · out/2026; Fev a dez/2027, uma oferta por vez |
| Servidor caseiro (NAS + serviços) | 31.1 | 2028, quando o grupo pedir |
| SSD externo (USB-C 10 Gbps) | 1.2 | Semana 1 · out/2026 |
| Workstation com GPU | 31.3 | 2028, quando o grupo pedir |
