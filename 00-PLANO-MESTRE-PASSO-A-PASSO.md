---
tags: [plano-mestre, passo-a-passo, setup, estudo, renda]
---

# 🧭 Plano Mestre — tudo em um só passo a passo

> **Este é o único lugar para saber o que fazer a seguir.** Ele junta os dois planejamentos:
> o **setup** (repositório `dev-setup`, 34 fases, hoje dentro deste vault na pasta `11-setup-dev-setup`) e o **estudo** (este vault, 14 Passos), mais
> as **fontes de renda**, as **finanças da casa**, a **faculdade**, as **certificações** e as **decisões**.
> São **391 itens**, cada um com um código, o que fazer, como saber que terminou e com quais outros itens ele se liga.

## Como usar (leia uma vez)

1. Vá até a **etapa** em que você está (começa na Etapa 0).
2. Dentro dela, faça os itens **de cima para baixo** em cada trilha. As trilhas andam juntas: na mesma semana você mexe no setup, estuda e corre atrás de renda.
3. Um item só está feito quando o **✅ Pronto quando** for verdade. Marque o `[ ]` como `[x]`.
4. **🔗 Liga com** mostra os códigos dos itens relacionados (o que vem antes, o que depende dele). Use Ctrl+F com o código para achar.
5. Itens com **⏸ gatilho** só começam quando o gatilho acontecer, mesmo que a etapa já tenha chegado.
6. A etapa termina quando os itens dela estão feitos. Datas são estimativas: se atrasar, **a ordem continua a mesma**.
7. Há uma versão interativa (página “Plano Mestre AMS”) com caixinhas, filtros e busca. Os dois têm os mesmos códigos.

**Legenda das trilhas:** 🛠️ Setup (257) · 📚 Estudo (46) · 💰 Renda (58) · 🏦 Finanças pessoais (14) · 🎓 Formação e certificações (12) · ⚖️ Decisões (4)

**Códigos:** `S-` setup · `E-` estudo · `R-` renda · `F-` finanças · `A-` faculdade · `C-` certificação · `H-` hábito · `D-` decisão

**Quem faz (setup):** Você = clique ou decisão sua · Script = você roda o comando · Claude com você = abre o Claude e pede.

## Mapa das etapas

| Etapa | Quando | Objetivo | Itens |
|---|---|---|---|
| [Etapa 0 · Arrumar a base](#e0) | out a início de nov/2026 | Arrumar a base: diagnóstico, senhas, Windows, finanças e o primeiro passo de estudo e de renda. | 35 |
| [Etapa 1 · Primeiros clientes](#e1) | nov a dez/2026 | Montar o núcleo do setup, terminar os Passos 1 e 2 e fazer entrar o primeiro dinheiro extra. | 82 |
| [Etapa 2 · Primeira venda de produto](#e2) | jan a fev/2027 | Vender no CPF com tudo medido, lançar o mini-curso e começar C#, TypeScript e Python. | 49 |
| [Etapa 3 · Rendas crescendo](#e3) | mar a jun/2027 | API, frontend e testes do Kaixara; uma oferta nova por vez; contabilidade e matemática financeira. | 88 |
| [Etapa 4 · Bater os R$ 7 mil](#e4) | jul a dez/2027 | Kaixara completo, arquitetura, candidaturas a vagas e a meta de renda. | 21 |
| [Etapa 5 · Virar sênior e empresa](#e5) | 2028 | Produção, plataforma interna, dados e IA, CNPJ, sistemas à venda e certificações. | 47 |
| [Etapa 6 · Especialização e expansão](#e6) | 2029 em diante | Segundo e terceiro sistemas, fase sênior, 42, segurança, IA do zero, fundos e negócios físicos. | 54 |
| [Sempre · Hábitos e rotinas](#ec) | contínuo | O que roda toda semana, do início ao fim. | 15 |

## A regra do dinheiro (resumo)

- Gastos fixos: cerca de **R$ 2.045/mês**. Restaurante em 2027: **R$ 2.200**. Meta: **R$ 7.000/mês** → faltam **R$ 4.800** de renda extra.
- **Sair da escola** só com renda extra acima de **R$ 1.500/mês por 2 meses seguidos** (`F-sairescola`).
- **Sair do restaurante** só com manutenção de sites acima de **R$ 2.200 por 3 meses** e reserva de 3 meses (`F-sairrest`).
- Uma oferta nova por vez; cada uma precisa de uma métrica antes da próxima (`S-` fase 22).

## Ligações entre os dois planejamentos (as mais importantes)

| Quando no estudo | O que destrava no setup / na renda |
|---|---|
| Passo 2 (Git, SQL, Docker) | Fases 4–5 do setup (Linux/WSL2, GitHub e CI) — o setup é a prática do Passo 2 |
| Passo 3 (C#, TypeScript) | Bloco paralelo de Python `E-py` |
| Passo 5 (EF Core) | Finanças F1–F2 `F-f1` |
| Passo 7 (Kaixara fechado) | Renda do Kaixara, carnê-leão `S-carne-leao`, tributação `F-f3` |
| Passo 4 a 6 (API, testes) | Base dos sistemas AM (fase 18); conta na nuvem e deploy do sistema exemplo (fase 19) com o Passo 5 |
| Passo 8 (Arquitetura) | Candidatura a vagas `S-vaga`; destrava as trilhas paralelas (Finanças F4–F5 → Dados e IA → 42 → Pentest) |
| IA2 da trilha de Dados e IA (≈ 2028) | Zoomcamp, dbt e Airflow da fase 21 |
| Passo 9 + IA0 (≈ 2028) | IA dentro dos sistemas AM (fase 25), junto do IA5 |
| IA6 da trilha (≈ 2029) | Dataset, fine-tuning do 8B e modelo no Ollama (fase 21) |
| Passo 10 (Produção real) | Deploy de produção do AM Kaixara na nuvem montada na fase 19 |
| Passo 12 (Plataforma interna) | Sistemas AM à venda; espanhol começa |
| Passo 14 + fase sênior | Rendara, consultoria, fundo; decisão do aura-historico |


---

## Etapa 0 · Arrumar a base
<a id="e0"></a>

**Quando:** out a início de nov/2026 · **Objetivo:** Arrumar a base: diagnóstico, senhas, Windows, finanças e o primeiro passo de estudo e de renda.

### 🛠️ Setup (31)


**Fase 0 do setup** — Diagnóstico: o que você já tem

- [ ] `S-diag-pasta` **0.1** Extrair o dev-setup.zip e deixar a pasta em C:\Users\SEU_USUARIO\dev-setup · _Você, ~5 min_
  - ✅ Pronto quando: Pasta C:\Users\SEU_USUARIO\dev-setup com RODAR-DIAGNOSTICO.cmd e as pastas scripts, data e docs logo dentro dela; nenhuma outra cópia em Downloads
  - 📝 Botão direito no zip > Extrair tudo. O Windows costuma criar dev-setup\dev-setup: recorte a pasta de dentro (a que tem a pasta scripts) e cole em C:\Users\SEU_USUARIO, a pasta com o seu nome. Apague as cópias que sobraram em Downloads, como "dev-setup (1)". Todos os comandos do Windows deste roteiro apontam para esse lugar, então funcionam de qualquer pasta, até da System32 onde o PowerShell de Administrador abre.
  - 🔗 Liga com: `S-diag-rodar`
- [ ] `S-diag-rodar` **0.2** Rodar o diagnóstico: botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador · _Script, ~10 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\diagnostico.ps1`
  - ✅ Pronto quando: Pasta diagnostico-AAAAMMDD com diagnostico.md: o que você tem e em que passo cada pendência se resolve
  - 📝 Somente leitura: não instala nem apaga nada. Em vez do comando, pode clicar com o botão direito em RODAR-DIAGNOSTICO.cmd > Executar como administrador. Se o Windows avisar "O Windows protegeu o computador", clique em Mais informações > Executar assim mesmo. Mostra modelo, processador, memória e slots livres, placa de vídeo, discos e saúde, espaço livre, bateria, monitores, Secure Boot, TPM, criptografia, Defender, programas do setup que já tem e que faltam, WSL, Docker, modelos do Ollama e extensões do VS Code.
  - 🔗 Liga com: `S-diag-pasta`, `S-inventario`
- [ ] `S-inventario` **0.3** Rodar o inventário de espaço: pastas e arquivos que mais ocupam, programas que iniciam com o Windows · _Script, ~15 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\inventario.ps1`
  - ✅ Pronto quando: Pasta inventario-AAAAMMDD gerada; você decidiu o que desinstalar ou mover
  - 🔗 Liga com: `S-diag-rodar`, `S-diag-contas`
- [ ] `S-diag-contas` **0.4** Listar as contas e assinaturas que você já tem, sem anotar senha · _Você, ~30 min_
  - ✅ Pronto quando: Nota no Obsidian (ou papel) com quais contas do setup já existem e quais assinaturas você paga
  - 📝 A lista de contas do setup está no ecossistema, em Contas que você precisa ter. Senha nunca vai para nota: só para o KeePassXC, no passo dele.
  - 🔗 Liga com: `S-inventario`, `S-diag-documentos`
- [ ] `S-diag-documentos` **0.5** Ver quantos documentos você já tem (só a contagem, sem abrir) · _Você, ~10 min_
  - ✅ Pronto quando: Você sabe por alto onde estão as aulas, apostilas, provas e projetos (Drive, notebook, pendrives)
  - 📝 A organização de verdade vem na fase Acervo, depois do backup.
  - 🔗 Liga com: `S-diag-contas`, `S-diag-claude`
- [ ] `S-diag-claude` **0.6** Mandar a pasta do diagnóstico para o Claude e ajustar o roteiro · _Claude com você, ~30 min_
  - ✅ Pronto quando: Passos que você já cumpre marcados no acompanhamento; compras e pendências confirmadas
  - 📝 Anexe na conversa os dois arquivos da pasta C:\Users\SEU_USUARIO\dev-setup\diagnostico-AAAAMMDD: diagnostico.md e diagnostico.json. Eles não têm senha nem documento seu, só hardware e programas.
  - 🔗 Liga com: `S-diag-documentos`, `S-backup-inicial`

**Fase 1 do setup** — Preparar

- [ ] `S-backup-inicial` **1.1** Copiar documentos, fotos e projetos para um disco externo · _Você, ~60 min_
  - ✅ Pronto quando: Disco externo com a cópia conferida (abra alguns arquivos)
  - 🔗 Liga com: `S-diag-claude`, `S-hardware`
- [ ] `S-hardware` **1.2** Montar a mesa: nobreak, base com cooler, 2º monitor, disco e SSD externos, kits de robótica · _Você, ~30 min_
  - ✅ Pronto quando: Notebook no nobreak e na base, 2º monitor funcionando, disco e SSD externos reconhecidos
  - 📝 O que ainda não comprou fica anotado e não trava as próximas fases. O nobreak vem primeiro: protege o notebook e o backup de queda de energia.
  - 🔗 Liga com: `S-backup-inicial`, `S-windows-update`
- [ ] `S-windows-update` **1.3** Atualizar o Windows, os drivers e o NitroSense · _Você, ~40 min_
  - ✅ Pronto quando: Windows Update sem pendências
  - 🔗 Liga com: `S-hardware`, `S-github-2fa`
- [ ] `S-github-2fa` **1.4** Instalar o app de 2FA no celular e ligar a verificação em duas etapas no GitHub, Google e e-mail · _Você, ~30 min_
  - ✅ Pronto quando: 2FA ativo nas três contas, com códigos de recuperação impressos
  - 🔗 Liga com: `S-windows-update`, `S-keepass`

**Fase 2 do setup** — Senhas: recuperar, trocar e guardar

- [ ] `S-keepass` **2.1** Instalar o KeePassXC e criar o cofre com uma senha mestra de 6 palavras · _Você, ~30 min_
  - 💻 `winget install --id KeePassXCTeam.KeePassXC -e`
  - ✅ Pronto quando: Arquivo Cofre.kdbx em Documentos\Cofre abre com a senha mestra; bloqueio automático depois de 5 minutos parado
  - 📝 Gere a senha mestra no próprio KeePassXC (Ferramentas > Gerador de senhas > Frase-senha, 6 palavras) e decore nos primeiros dias. Ela é a única senha que você precisa saber de cor e não pode ser usada em nenhum outro lugar. Não use arquivo-chave: se perder o arquivo, perde o cofre. Ninguém, nem o Claude, precisa ver o cofre ou a senha mestra.
  - 🔗 Liga com: `S-github-2fa`, `S-senhas-kit`
- [ ] `S-senhas-kit` **2.2** Montar o kit de emergência em papel · _Você, ~15 min_
  - ✅ Pronto quando: Envelope guardado em casa (fora da carteira e da mochila) com a senha mestra, a senha do e-mail principal e os códigos de recuperação do Google
  - 📝 É o que salva você se esquecer a senha mestra ou perder o notebook e o celular juntos. Papel, não foto: foto vai para a nuvem do celular.
  - 🔗 Liga com: `S-keepass`, `S-senhas-email`
- [ ] `S-senhas-email` **2.3** Recuperar e trocar primeiro a senha do e-mail principal (conta Google) · _Você, ~30 min_
  - ✅ Pronto quando: Senha nova gerada no KeePassXC; verificação em duas etapas pelo app; telefone e e-mail de recuperação conferidos; códigos de backup salvos no cofre; aparelhos desconhecidos desconectados
  - 📝 Vem antes de tudo porque todo 'Esqueci minha senha' manda o link para esse e-mail: quem controla o e-mail controla as outras contas. Faça em myaccount.google.com > Segurança e rode a Verificação de segurança no fim. Se não lembrar a senha atual, use g.co/recover no notebook e na rede de casa, onde o Google já reconhece você.
  - 🔗 Liga com: `S-senhas-kit`, `S-senhas-importar`
- [ ] `S-senhas-importar` **2.4** Trazer para o cofre as senhas salvas no Chrome, no Edge e no Google · _Você, ~30 min_
  - ✅ Pronto quando: Senhas importadas no KeePassXC (Banco de dados > Importar > CSV); o arquivo CSV apagado de vez; navegadores sem salvar senha
  - 📝 Exporte em chrome://password-manager/settings, edge://wallet/passwords e passwords.google.com. O CSV é a lista de todas as suas senhas em texto puro: importe na hora, apague com Shift+Delete e não deixe em Downloads, no Drive, no e-mail nem no repositório. Não mande esse arquivo para ninguém, nem para o Claude. Só depois de conferir o cofre apague as senhas dos navegadores e desligue 'Oferecer para salvar senhas'.
  - 🔗 Liga com: `S-senhas-email`, `S-senhas-relatorio`
- [ ] `S-senhas-relatorio` **2.5** Ver no KeePassXC quais senhas são fracas, repetidas ou já vazaram · _Você, ~15 min_
  - ✅ Pronto quando: Lista, em ordem, das contas para trocar (Banco de dados > Relatórios > Integridade e Have I Been Pwned)
  - 📝 A checagem de vazamento manda só um pedaço do resumo da senha, nunca a senha. Senha que aparece como vazada vai para o topo da lista.
  - 🔗 Liga com: `S-senhas-importar`, `S-senhas-criticas`
- [ ] `S-senhas-criticas` **2.6** Trocar as senhas críticas, uma por vez: gov.br, bancos, Microsoft, celular, WhatsApp, GitHub, Meta, Mercado Livre e plataformas de venda · _Você, ~120 min_
  - ✅ Pronto quando: Cada conta crítica com senha nova gerada no cofre, verificação em duas etapas ligada e códigos de backup salvos na entrada dela
  - 📝 Para cada uma: gere a senha no KeePassXC (20 caracteres ou mais), troque no site, salve no cofre antes de fechar a página e saia de todos os outros aparelhos. Banco, troque pelo app oficial. No WhatsApp é o PIN da confirmação em duas etapas. A senha de 4 dígitos do cartão não vai para o cofre: essa você decora.
  - 🔗 Liga com: `S-senhas-relatorio`, `S-senhas-esquecidas`
- [ ] `S-senhas-esquecidas` **2.7** Recuperar as contas cuja senha você esqueceu e fechar as que não usa mais · _Você, ~60 min_
  - ✅ Pronto quando: Toda conta da sua lista de contas está no cofre, foi recuperada ou foi excluída
  - 📝 Use 'Esqueci minha senha' com o e-mail já protegido. Se o e-mail ou o telefone de recuperação forem antigos, cada serviço tem um formulário próprio (Meta: 'Precisa de ajuda?' na tela de login; gov.br: pelo app com reconhecimento facial ou pelo banco). Conta parada que guarda dado seu é risco: exclua.
  - 🔗 Liga com: `S-senhas-criticas`, `S-senhas-celular`
- [ ] `S-senhas-celular` **2.8** Levar o cofre para o celular (KeePassDX no Android ou KeePassium no iPhone) · _Você, ~20 min_
  - ✅ Pronto quando: O cofre abre no celular com a senha mestra; uma senha criada no notebook aparece no celular
  - 📝 Sincronize o arquivo Cofre.kdbx pelo Syncthing, ou pelo Drive (o arquivo vai criptografado). Edite num aparelho de cada vez para não criar cópias em conflito.
  - 🔗 Liga com: `S-senhas-esquecidas`, `S-senhas-navegador`
- [ ] `S-senhas-navegador` **2.9** Ligar o KeePassXC-Browser para preencher senha e código no navegador · _Você, ~15 min_
  - ✅ Pronto quando: No login de teste, o navegador preenche a senha a partir do cofre
  - 📝 No KeePassXC: Configurações > Integração com navegador, marque o seu navegador e instale a extensão KeePassXC-Browser.
  - 🔗 Liga com: `S-senhas-celular`, `S-senhas-backup`
- [ ] `S-senhas-backup` **2.10** Pôr o cofre no backup e testar abrir a cópia · _Você, ~15 min_
  - ✅ Pronto quando: Cópia do Cofre.kdbx no disco externo abre com a senha mestra; quando o restic entrar, a pasta Documentos\Cofre está no backup diário
  - 📝 No WSL o caminho é /mnt/c/Users/SEU_USUARIO/Documents/Cofre: acrescente ao comando do restic no passo do backup.
  - 🔗 Liga com: `S-senhas-navegador`, `S-senhas-resto`
- [ ] `S-senhas-resto` **2.11** Trocar o resto aos poucos: 5 contas por semana, das mais usadas às menos usadas · _Você, ~20 min_
  - ✅ Pronto quando: Relatório de integridade do KeePassXC sem senha fraca, repetida ou vazada
  - 🔗 Liga com: `S-senhas-backup`, `S-senhas-revisao`, `H-senhas`
- [ ] `S-senhas-revisao` **2.12** Marcar a revisão a cada 3 meses: relatório do cofre, aparelhos conectados no Google e códigos de backup · _Você, ~10 min_
  - ✅ Pronto quando: Lembrete trimestral no calendário
  - 🔗 Liga com: `S-senhas-resto`, `S-win-simular`, `H-senhas`

**Fase 3 do setup** — Windows

- [ ] `S-win-simular` **3.1** Ver o que o instalador faria · _Script, ~5 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1`
  - ✅ Pronto quando: Lista de INSTALARIA conferida
  - 🔗 Liga com: `S-senhas-revisao`, `S-win-aplicar`
- [ ] `S-win-aplicar` **3.2** Instalar programas, WSL2 com Ubuntu 24.04 e .wslconfig (PowerShell como Administrador) · _Script, ~60 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\instalar.ps1 -Aplicar`
  - ✅ Pronto quando: Termina com 'Pronto' e sem ERRO; reinicie o Windows
  - 🔗 Liga com: `S-win-simular`, `S-cripto`
- [ ] `S-cripto` **3.3** Ligar a criptografia do dispositivo e guardar a chave de recuperação no KeePassXC · _Você, ~15 min_
  - ✅ Pronto quando: verificar.ps1 como Administrador mostra criptografia OK
  - 📝 No Windows 11 Home a opção se chama Criptografia do dispositivo e depende do hardware. Se não aparecer, anote e siga.
  - 🔗 Liga com: `S-win-aplicar`, `S-defender`
- [ ] `S-defender` **3.4** Conferir Defender e Firewall ligados · _Você, ~10 min_
  - ✅ Pronto quando: verificar.ps1 como Administrador mostra Defender OK
  - 🔗 Liga com: `S-cripto`, `S-vscode-ext`
- [ ] `S-vscode-ext` **3.5** Instalar as extensões do VS Code (WSL, Claude Code, .NET, LaTeX, revisão em português) · _Script, ~10 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\extensoes-vscode.ps1 -Aplicar`
  - ✅ Pronto quando: Termina com 'Pronto'
  - 🔗 Liga com: `S-defender`, `S-navegador`
- [ ] `S-navegador` **3.6** Instalar o Claude in Chrome e entrar com a sua conta · _Você, ~15 min_
  - ✅ Pronto quando: O painel do Claude abre numa aba do navegador
  - 📝 O uso do computador pelo Claude fica no app do Claude para desktop; ligue só quando for usar e acompanhe o que ele faz.
  - 🔗 Liga com: `S-vscode-ext`, `S-davinci`
- [ ] `S-davinci` **3.7** Instalar o DaVinci Resolve pelo site da Blackmagic (opcional) · _Você, ~20 min_
  - ✅ Pronto quando: Abre e reconhece a GPU
  - 🔗 Liga com: `S-navegador`, `S-unity-decisao`
- [ ] `S-unity-decisao` **3.8** Decidir se Unity e Cocos ficam para as aulas de robótica · _Você, ~10 min_
  - 💻 `winget install --id Unity.UnityHub -e`
  - ✅ Pronto quando: Decisão anotada; se ficam, Unity Hub instalado
  - 🔗 Liga com: `S-davinci`, `S-win-verificar`
- [ ] `S-win-verificar` **3.9** Conferir o Windows · _Script, ~5 min_
  - 💻 `powershell -ExecutionPolicy Bypass -File $HOME\dev-setup\scripts\windows\verificar.ps1`
  - ✅ Pronto quando: verificar.ps1 termina com 'Windows pronto'
  - 🔗 Liga com: `S-unity-decisao`, `S-ubuntu-usuario`
### 📚 Estudo (1)

- [ ] `E-epic` **Abrir o EPIC-01 e fazer a primeira User Story do Passo 1**
  - ✅ Pronto quando: Uma User Story marcada como feita
  - 🔗 Liga com: `E-P1`
### 💰 Renda (1)

- [ ] `R-msg` **Mandar mensagem a contatos e pais de alunos oferecendo aulas particulares e manutenção de computador**
  - ✅ Pronto quando: Mensagem enviada
  - 🔗 Liga com: `R-aulas`
### 🏦 Finanças pessoais (1)

- [ ] `F-gastos` **Lançar no Caixa da Casa os gastos fixos (R$ 2.045) e as parcelas do cartão**
  - ✅ Pronto quando: Você sabe quanto sobra por mês
  - 🔗 Liga com: `H-caixa`
### ⚖️ Decisões (1)

- [ ] `D-devsetup` **Publicar o dev-setup no GitHub (passo de criar o repositório privado)**
  - 🔗 Liga com: `S-repo-criar`

---

## Etapa 1 · Primeiros clientes
<a id="e1"></a>

**Quando:** nov a dez/2026 · **Objetivo:** Montar o núcleo do setup, terminar os Passos 1 e 2 e fazer entrar o primeiro dinheiro extra.

### 🛠️ Setup (74)


**Fase 4 do setup** — Linux (WSL2)

- [ ] `S-ubuntu-usuario` **4.1** Abrir 'Ubuntu 24.04' no menu Iniciar e criar seu usuário Linux · _Você, ~10 min_
  - ✅ Pronto quando: Prompt do Ubuntu aberto
  - 🔗 Liga com: `S-win-verificar`, `S-docker-wsl`, `E-P2`
- [ ] `S-docker-wsl` **4.2** Ligar o Docker Desktop no Ubuntu: Settings > Resources > WSL integration · _Você, ~5 min_
  - ✅ Pronto quando: 'docker run hello-world' funciona dentro do Ubuntu
  - 🔗 Liga com: `S-ubuntu-usuario`, `S-clonar`, `E-P2`
- [ ] `S-clonar` **4.3** Copiar este repositório para ~/dev/dev-setup · _Você, ~5 min_
  - 💻 `mkdir -p ~/dev && cp -r /mnt/c/Users/SEU_USUARIO/dev-setup ~/dev/dev-setup`
  - ✅ Pronto quando: Pasta ~/dev/dev-setup com os arquivos
  - 📝 Troque SEU_USUARIO pelo seu usuário do Windows. Depois que o repositório estiver no GitHub, use git clone.
  - 🔗 Liga com: `S-docker-wsl`, `S-bootstrap`, `E-P2`
- [ ] `S-bootstrap` **4.4** Rodar o preparador do Linux · _Script, ~40 min_
  - 💻 `bash scripts/wsl/bootstrap.sh --nome "Alan Mateus" --email SEU_EMAIL --com-whisper`
  - ✅ Pronto quando: Termina com 'Pronto' e sem ERRO
  - 🔗 Liga com: `S-clonar`, `S-wsl-reiniciar`, `E-P2`
- [ ] `S-wsl-reiniciar` **4.5** Reiniciar o WSL para o systemd valer (PowerShell) · _Você, ~2 min_
  - 💻 `wsl --shutdown`
  - ✅ Pronto quando: Ubuntu reabre normalmente
  - 🔗 Liga com: `S-bootstrap`, `S-gh-login`, `E-P2`
- [ ] `S-gh-login` **4.6** Entrar no GitHub pelo terminal e cadastrar a chave SSH para login e assinatura · _Você, ~10 min_
  - 💻 `gh auth login && gh ssh-key add ~/.ssh/id_ed25519.pub --type authentication && gh ssh-key add ~/.ssh/id_ed25519.pub --type signing`
  - ✅ Pronto quando: 'gh auth status' mostra sua conta
  - 🔗 Liga com: `S-wsl-reiniciar`, `S-dotfiles`, `E-P2`
- [ ] `S-dotfiles` **4.7** Guardar os dotfiles (.bashrc, .gitconfig, .tmux.conf) num repositório privado · _Claude com você, ~30 min_
  - ✅ Pronto quando: Repositório dotfiles privado; clonar e rodar o script de links recria o terminal
  - 📝 Nunca coloque chaves ou tokens nos dotfiles. O gitleaks do CI confere a cada envio.
  - 🔗 Liga com: `S-gh-login`, `S-obsidian-git`, `E-P2`
- [ ] `S-obsidian-git` **4.8** Criar o cofre do Obsidian em ~/dev/notas e ligar o plugin Obsidian Git · _Você, ~20 min_
  - 💻 `bash scripts/wsl/vault.sh`
  - ✅ Pronto quando: Cofre aberto no Obsidian com as pastas e modelos; notas vão sozinhas para um repositório privado a cada 10 minutos
  - 📝 No Obsidian do Windows, abra a pasta \\wsl.localhost\Ubuntu-24.04\home\SEU_USUARIO\dev\notas.
  - 🔗 Liga com: `S-dotfiles`, `S-syncthing`, `E-P2`
- [ ] `S-syncthing` **4.9** Ligar o Syncthing entre o celular e o notebook para as gravações (opcional) · _Você, ~15 min_
  - ✅ Pronto quando: Vídeo gravado no celular aparece na pasta Gravacoes do Windows
  - 📝 Para o pipeline pegar, mova o vídeo para ~/AMtech/entrada/aulas. Vídeo com aluno menor de idade só com autorização do responsável.
  - 🔗 Liga com: `S-obsidian-git`, `S-wsl-verificar`, `E-P2`
- [ ] `S-wsl-verificar` **4.10** Conferir o Linux · _Script, ~5 min_
  - 💻 `bash scripts/wsl/verificar.sh`
  - ✅ Pronto quando: verificar.sh termina com 'WSL pronto'
  - 🔗 Liga com: `S-syncthing`, `S-repo-criar`, `E-P2`

**Fase 5 do setup** — GitHub e CI

- [ ] `S-repo-criar` **5.1** Criar o repositório privado e enviar o setup · _Script, ~5 min_
  - 💻 `cd ~/dev/dev-setup && git init -q 2>/dev/null; git add -A && git commit -qm 'chore: setup inicial' ; gh repo create AlanMateus17/dev-setup --private --source . --push`
  - ✅ Pronto quando: Repositório AlanMateus17/dev-setup privado com o código
  - 📝 Se você usar o zip, o histórico de commits não vem junto; o repositório começa com um commit novo, já assinado.
  - 🔗 Liga com: `S-wsl-verificar`, `S-ci-verde`, `E-P2`, `D-devsetup`
- [ ] `S-ci-verde` **5.2** Conferir o CI no GitHub · _Script, ~5 min_
  - 💻 `gh run list --limit 1`
  - ✅ Pronto quando: Última execução do workflow 'docs' com sucesso
  - 🔗 Liga com: `S-repo-criar`, `S-protecao-main`, `E-P2`
- [ ] `S-protecao-main` **5.3** Ligar Dependabot e CodeQL e proteger o branch main · _Claude com você, ~15 min_
  - ✅ Pronto quando: Dependabot e CodeQL ativos; push direto no main exige CI verde
  - 📝 Peça ao Claude Code no repositório; ele faz pelo gh api com a sua aprovação.
  - 🔗 Liga com: `S-ci-verde`, `S-org`, `E-P2`
- [ ] `S-org` **5.4** Criar a organização grupo-amtech-digital no GitHub · _Você, ~10 min_
  - ✅ Pronto quando: Organização criada, com 2FA obrigatório para membros
  - 🔗 Liga com: `S-protecao-main`, `S-projetos-adr`, `E-P2`
- [ ] `S-projetos-adr` **5.5** Criar o GitHub Project do setup e a pasta de decisões (ADRs) · _Claude com você, ~20 min_
  - ✅ Pronto quando: Quadro com as fases deste roteiro e docs/adr/0001 registrado
  - 📝 O MkDocs publica a documentação no GitHub Pages quando você quiser tornar algo público; o setup continua privado.
  - 🔗 Liga com: `S-org`, `S-claude-login`, `E-P2`

**Fase 6 do setup** — Agentes de IA

- [ ] `S-claude-login` **6.1** Entrar no Claude Code · _Você, ~5 min_
  - 💻 `claude`
  - ✅ Pronto quando: 'claude doctor' sem erros
  - 🔗 Liga com: `S-projetos-adr`, `S-ai-jail-teste`
- [ ] `S-ai-jail-teste` **6.2** Testar a sandbox · _Script, ~2 min_
  - 💻 `cd ~/dev/dev-setup && ai-jail --dry-run claude`
  - ✅ Pronto quando: Mostra o que seria montado, sem erro
  - 🔗 Liga com: `S-claude-login`, `S-claude-md`
- [ ] `S-claude-md` **6.3** Criar o CLAUDE.md padrão do Aura e os comandos /commit e /novo-sistema-aura · _Claude com você, ~30 min_
  - ✅ Pronto quando: Arquivos no repositório de cada sistema
  - 📝 Peça ao Claude Code: o conteúdo está em docs/pecas-autorais.md.
  - 🔗 Liga com: `S-ai-jail-teste`, `S-ollama-modelo`
- [ ] `S-ollama-modelo` **6.4** Baixar um modelo local de 3 a 4B no Ollama · _Você, ~15 min_
  - 💻 `ollama pull <nome do modelo escolhido no catálogo do Ollama>`
  - ✅ Pronto quando: verificar.ps1 mostra Ollama OK com 1 modelo
  - 🔗 Liga com: `S-claude-md`, `S-mcp`
- [ ] `S-mcp` **6.5** Ligar os servidores MCP do Claude Code: GitHub e o banco de métricas só para leitura · _Claude com você, ~20 min_
  - ✅ Pronto quando: 'claude mcp list' mostra os servidores conectados
  - 📝 O banco entra com o usuário leitor do Grafana, que não apaga nada. Tokens ficam no KeePassXC e em variáveis de ambiente, nunca no repositório.
  - 🔗 Liga com: `S-ollama-modelo`, `S-ai-memory`
- [ ] `S-ai-memory` **6.6** Ligar o ai-memory para o agente lembrar das decisões entre sessões · _Claude com você, ~15 min_
  - ✅ Pronto quando: Uma decisão anotada numa sessão aparece na seguinte
  - 🔗 Liga com: `S-mcp`, `S-rag`
- [ ] `S-rag` **6.7** Montar a base de conhecimento das suas notas (Ollama + pgvector, ou NotebookLM e Projects) · _Claude com você, ~60 min_
  - ✅ Pronto quando: Pergunta sobre uma anotação sua volta com a resposta e a nota de origem
  - 📝 Entram só as suas anotações, resumos com suas palavras, exercícios resolvidos e aulas que você gravou. Aulas da Udemy, DIO, Alura e afins não entram.
  - 🔗 Liga com: `S-ai-memory`, `S-restic-local`

**Fase 7 do setup** — Backup e segurança

- [ ] `S-restic-local` **7.1** Criar o repositório restic no disco externo e o primeiro backup · _Script, ~30 min_
  - 💻 `restic -r /mnt/d/backup-restic init && restic -r /mnt/d/backup-restic backup ~/dev ~/AMtech ~/.config/amtech`
  - ✅ Pronto quando: 'restic snapshots' lista o backup
  - 📝 Troque /mnt/d pela letra do seu disco externo (D: vira /mnt/d). Guarde a senha do repositório no KeePassXC.
  - 🔗 Liga com: `S-rag`, `S-restic-nuvem`
- [ ] `S-restic-nuvem` **7.2** Criar a cópia fora de casa (Backblaze B2 ou o armazenamento do seu plano Google) · _Você, ~40 min_
  - ✅ Pronto quando: Segundo repositório restic com snapshot
  - 🔗 Liga com: `S-restic-local`, `S-restaurar`
- [ ] `S-restaurar` **7.3** Testar a restauração de uma pasta · _Você, ~15 min_
  - ✅ Pronto quando: Arquivo restaurado abre normalmente
  - 🔗 Liga com: `S-restic-nuvem`, `S-agendar-backup`
- [ ] `S-agendar-backup` **7.4** Agendar o backup diário · _Claude com você, ~20 min_
  - ✅ Pronto quando: Timer do backup ativo
  - 🔗 Liga com: `S-restaurar`, `S-acervo-copia`

**Fase 8 do setup** — Acervo: tudo o que você já tem

- [ ] `S-acervo-copia` **8.1** Baixar uma cópia completa do Google Drive pelo Google Takeout · _Você, ~45 min_
  - ✅ Pronto quando: Os zips do Takeout extraídos numa pasta só, por exemplo C:\Users\SEU_USUARIO\Downloads\Takeout
  - 📝 Escolha só o Drive e, em formatos, Google Docs como .docx e Apresentações como .pptx. O Drive para computador mostra os Google Docs como atalhos sem conteúdo, por isso a primeira cópia vem do Takeout. Junte também os arquivos do notebook e dos pendrives na mesma pasta.
  - 🔗 Liga com: `S-agendar-backup`, `S-separar-pessoais`
- [ ] `S-separar-pessoais` **8.2** Tirar da pasta os documentos pessoais (contracheques, extratos, IRPF, faturas) · _Você, ~30 min_
  - ✅ Pronto quando: Pasta Pessoal separada, guardada só no backup criptografado
  - 📝 O acervo.py também barra esses arquivos pelo nome e pelo conteúdo e lista o que achou, mas tirar antes é mais seguro.
  - 🔗 Liga com: `S-acervo-copia`, `S-acervo-simular`
- [ ] `S-acervo-simular` **8.3** Ver o que o acervo faria, sem escrever nada · _Script, ~10 min_
  - 💻 `uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular`
  - ✅ Pronto quando: Resumo com arquivos lidos, cópias repetidas, pessoais, de terceiros e da escola
  - 🔗 Liga com: `S-separar-pessoais`, `S-acervo-rodar`
- [ ] `S-acervo-rodar` **8.4** Converter o acervo para o Obsidian e gerar o relatório de produtos · _Script, ~30 min_
  - 💻 `uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout`
  - ✅ Pronto quando: 30-Acervo no Obsidian com os documentos em Markdown e 40-Produtos/Produtos do acervo.md
  - 📝 Roda no notebook; nada é enviado para fora. Pode rodar de novo quando chegarem documentos novos: o que já foi convertido não é refeito.
  - 🔗 Liga com: `S-acervo-simular`, `S-acervo-alertas`
- [ ] `S-acervo-alertas` **8.5** Decidir cada alerta: dados de alunos, material de terceiros, material feito para a escola · _Você, ~90 min_
  - ✅ Pronto quando: Cada alerta com decisão anotada: apagar dados, só estudo, reescrever ou vender
  - 📝 Material de terceiros (livros, cursos) não vira produto nem treino de IA. Material feito para a escola: confira os direitos antes de vender; o caminho seguro é reescrever do zero, no seu tempo, sem a identidade da escola.
  - 🔗 Liga com: `S-acervo-rodar`, `S-acervo-rag`
- [ ] `S-acervo-rag` **8.6** Indexar o acervo e as suas notas na base de conhecimento · _Claude com você, ~30 min_
  - ✅ Pronto quando: Pergunta sobre um documento antigo volta com a resposta e o arquivo de origem
  - 🔗 Liga com: `S-acervo-alertas`, `S-acervo-produtos`
- [ ] `S-acervo-produtos` **8.7** Escolher no relatório os 3 primeiros produtos e levar para o portfólio de ofertas · _Claude com você, ~60 min_
  - ✅ Pronto quando: 3 ofertas novas em data/portfolio.json com estágio, preço alvo e próximo passo
  - 🔗 Liga com: `S-acervo-rag`, `S-claude-app`

**Fase 9 do setup** — Claude e assistentes

- [ ] `S-claude-app` **9.1** Organizar o app do Claude: um Project por frente, memória, artefatos, pesquisa e tarefas agendadas · _Você, ~30 min_
  - ✅ Pronto quando: Projects AMtech, Instituto, Editora e Setup criados; uma tarefa agendada de teste rodou
  - 🔗 Liga com: `S-acervo-produtos`, `S-conectores`
- [ ] `S-conectores` **9.2** Conferir os conectores: Google, Canva, Figma, MailerLite, Vercel, Microsoft Learn, Upwork, Lovable, Supabase, Cloudflare e vidIQ · _Você, ~30 min_
  - ✅ Pronto quando: Cada conector usado responde a um pedido simples; o da Cloudflare trocado pelo Cloudflare API MCP
  - 📝 Notion, monday, GitBook e Stripe ficam de fora: repetem Obsidian, GitHub Projects, MkDocs e as plataformas de curso. Desconecte para não confundir.
  - 🔗 Liga com: `S-claude-app`, `S-plugins`
- [ ] `S-plugins` **9.3** Ligar os plugins: small-business, marketing, engineering, design, finance, Hostinger, Adobe e Cloudinary · _Você, ~15 min_
  - ✅ Pronto quando: Os comandos dos plugins aparecem no Claude
  - 🔗 Liga com: `S-conectores`, `S-assistentes`
- [ ] `S-assistentes` **9.4** Entrar nos outros assistentes (ChatGPT, Gemini, Grok, DeepSeek, Perplexity, Codex, agentes do Google) e anotar quais são pagos · _Você, ~30 min_
  - ✅ Pronto quando: Acessos no KeePassXC e assinaturas pagas lançadas na tabela ferramentas do banco de métricas
  - 🔗 Liga com: `S-plugins`, `S-senhas`

**Fase 10 do setup** — Automação e medição

- [ ] `S-senhas` **10.1** Gerar as senhas da stack e guardar no KeePassXC · _Script, ~5 min_
  - 💻 `cd infra/automacao && bash gerar-senhas.sh`
  - ✅ Pronto quando: .env criado com permissão 600
  - 🔗 Liga com: `S-assistentes`, `S-subir-stack`
- [ ] `S-subir-stack` **10.2** Subir a stack · _Script, ~10 min_
  - 💻 `cd infra/automacao && docker compose up -d`
  - ✅ Pronto quando: 'docker compose ps' com todos healthy
  - 🔗 Liga com: `S-senhas`, `S-servicos-verificar`
- [ ] `S-servicos-verificar` **10.3** Conferir os serviços · _Script, ~2 min_
  - 💻 `bash scripts/wsl/verificar.sh --servicos`
  - ✅ Pronto quando: verificar.sh --servicos sem FALTA na área servico
  - 🔗 Liga com: `S-subir-stack`, `S-grafana-login`
- [ ] `S-grafana-login` **10.4** Entrar no Grafana (admin) e ver a fonte 'Métricas AMtech' conectada · _Você, ~10 min_
  - 💻 `http://localhost:3001`
  - ✅ Pronto quando: Explore > Métricas AMtech > 'select 1' responde
  - 🔗 Liga com: `S-servicos-verificar`, `S-n8n-conta`
- [ ] `S-n8n-conta` **10.5** Criar a conta do n8n · _Você, ~5 min_
  - 💻 `http://localhost:5678`
  - ✅ Pronto quando: Painel do n8n abre
  - 🔗 Liga com: `S-grafana-login`, `S-kuma-monitores`
- [ ] `S-kuma-monitores` **10.6** Cadastrar no Uptime Kuma os monitores do n8n, Grafana e dos sites · _Você, ~15 min_
  - 💻 `http://localhost:3002`
  - ✅ Pronto quando: Monitores verdes; aviso no Telegram configurado
  - 🔗 Liga com: `S-n8n-conta`, `S-backup-banco`
- [ ] `S-backup-banco` **10.7** Pôr o banco de métricas e os fluxos do n8n no backup diário · _Claude com você, ~45 min_
  - ✅ Pronto quando: Dump diário do banco e export dos fluxos em ~/AMtech/backup-dados, copiados pelo restic; uma restauração de teste funcionou
  - 📝 Os dados ficam em volumes do Docker, fora das pastas que o restic copia. Sem este passo, perder o notebook leva junto o histórico de vendas.
  - 🔗 Liga com: `S-kuma-monitores`, `S-postiz-decisao`
- [ ] `S-postiz-decisao` **10.8** Decidir: Postiz agora ou agendador nativo das redes · _Você, ~10 min_
  - ✅ Pronto quando: Decisão anotada em infra/postiz/README.md
  - 🔗 Liga com: `S-backup-banco`, `S-marca`

**Fase 11 do setup** — Pipeline de conteúdo

- [ ] `S-marca` **11.1** Preencher o guia de marca · _Você, ~40 min_
  - ✅ Pronto quando: config/marca.md sem colchetes
  - 📝 O Claude pode rascunhar a partir dos documentos de marca e presença; você corrige.
  - 🔗 Liga com: `S-postiz-decisao`, `S-api-key`
- [ ] `S-api-key` **11.2** Criar a chave da API no console da Anthropic e colocar no conteudo.env · _Você, ~10 min_
  - ✅ Pronto quando: ANTHROPIC_API_KEY preenchida em ~/.config/amtech/conteudo.env
  - 📝 A API é cobrada por uso, separada da assinatura do Claude. Defina um limite de gasto mensal no console.
  - 🔗 Liga com: `S-marca`, `S-telegram-bot`
- [ ] `S-telegram-bot` **11.3** Criar o bot de aviso no Telegram (opcional) · _Você, ~10 min_
  - ✅ Pronto quando: Mensagem de teste chega no celular
  - 🔗 Liga com: `S-api-key`, `S-simular-pipeline`
- [ ] `S-simular-pipeline` **11.4** Testar o caminho sem gastar · _Script, ~2 min_
  - 💻 `echo teste > ~/AMtech/entrada/ideias/teste.txt && touch -d '-2 min' ~/AMtech/entrada/ideias/teste.txt && python3 tools/conteudo/processar.py --uma-vez --simular`
  - ✅ Pronto quando: Uma pasta [SIMULADO] aparece em ~/AMtech/fila
  - 🔗 Liga com: `S-telegram-bot`, `S-ativar-pipeline`
- [ ] `S-ativar-pipeline` **11.5** Ligar o timer de 15 minutos · _Script, ~2 min_
  - 💻 `bash scripts/wsl/ativar-pipeline.sh`
  - ✅ Pronto quando: verificar.sh --servicos mostra o timer OK
  - 🔗 Liga com: `S-simular-pipeline`, `S-primeira-aula`, `H-ensina`
- [ ] `S-primeira-aula` **11.6** Colocar uma aula gravada de verdade em ~/AMtech/entrada/aulas · _Você, ~20 min_
  - ✅ Pronto quando: Peças da aula na fila em até 15 minutos depois de transcrita
  - 🔗 Liga com: `S-ativar-pipeline`, `S-obs-cenas`

**Fase 12 do setup** — Estúdio de conteúdo

- [ ] `S-obs-cenas` **12.1** Montar no OBS as cenas de aula, tela com rosto e vídeo vertical · _Você, ~40 min_
  - ✅ Pronto quando: Gravação de teste de 1 minuto com áudio limpo nas três cenas
  - 🔗 Liga com: `S-primeira-aula`, `S-audio-modelo`
- [ ] `S-audio-modelo` **12.2** Criar no Audacity a cadeia de limpeza da sua voz (ruído, compressor, volume) · _Você, ~20 min_
  - ✅ Pronto quando: A mesma limpeza aplicada com um clique numa gravação nova
  - 🔗 Liga com: `S-obs-cenas`, `S-edicao-modelo`
- [ ] `S-edicao-modelo` **12.3** Criar no DaVinci ou Kdenlive o projeto modelo com abertura, legendas e formato vertical · _Você, ~40 min_
  - ✅ Pronto quando: Um corte de 30 segundos exportado a partir do modelo
  - 🔗 Liga com: `S-audio-modelo`, `S-imagens-modelos`
- [ ] `S-imagens-modelos` **12.4** Criar os modelos de capa, carrossel e thumbnail com a sua marca (Canva, Krita ou Inkscape) · _Claude com você, ~40 min_
  - ✅ Pronto quando: Três modelos salvos; uma peça da fila montada com eles
  - 📝 O Claude cria os modelos no Canva pelo conector, a partir do config/marca.md.
  - 🔗 Liga com: `S-edicao-modelo`, `S-voz-clonada`
- [ ] `S-voz-clonada` **12.5** Clonar a sua própria voz na ElevenLabs (opcional, plano pago) · _Você, ~60 min_
  - ✅ Pronto quando: Trecho de teste com a sua voz clonada aprovado por você
  - 📝 Só a sua voz, com 30 minutos ou mais de áudio limpo. Avise o público quando a voz for gerada por IA. Voz de outra pessoa, nunca.
  - 🔗 Liga com: `S-imagens-modelos`, `S-perfis`

**Fase 13 do setup** — Contas, canais e sites

- [ ] `S-perfis` **13.1** Completar Instagram, YouTube, TikTok, LinkedIn e Facebook com a mesma identidade · _Você, ~90 min_
  - ✅ Pronto quando: Foto, nome, bio e link iguais nas cinco redes
  - 🔗 Liga com: `S-voz-clonada`, `S-whatsapp-business`, `H-posts`
- [ ] `S-whatsapp-business` **13.2** Configurar o WhatsApp Business com catálogo, respostas rápidas e horário · _Você, ~30 min_
  - ✅ Pronto quando: Mensagem de teste recebe a saudação automática
  - 🔗 Liga com: `S-perfis`, `S-dominio`
- [ ] `S-dominio` **13.3** Registrar o domínio no Registro.br e apontar para a Cloudflare · _Você, ~30 min_
  - ✅ Pronto quando: DNS ativo na Cloudflare
  - 🔗 Liga com: `S-whatsapp-business`, `S-email-prof`
- [ ] `S-email-prof` **13.4** Criar o e-mail profissional do domínio · _Você, ~30 min_
  - ✅ Pronto quando: Envia e recebe
  - 🔗 Liga com: `S-dominio`, `S-meta-business`
- [ ] `S-meta-business` **13.5** Criar o Gerenciador de Negócios da Meta, o Pixel e a conta de anúncios · _Você, ~40 min_
  - ✅ Pronto quando: Pixel instalado na página de vendas
  - 🔗 Liga com: `S-email-prof`, `S-mailerlite`
- [ ] `S-mailerlite` **13.6** Montar no MailerLite os grupos, o formulário da isca e a sequência de boas-vindas · _Claude com você, ~30 min_
  - ✅ Pronto quando: Inscrição de teste recebe o primeiro e-mail
  - 📝 O Claude faz pelo conector do MailerLite, com a sua aprovação.
  - 🔗 Liga com: `S-meta-business`, `S-site-pessoal`
- [ ] `S-site-pessoal` **13.7** Publicar o site pessoal e blog no GitHub Pages (alanmateus17.github.io) · _Claude com você, ~60 min_
  - ✅ Pronto quando: Site no ar com portfólio, blog e formulário da newsletter
  - 🔗 Liga com: `S-mailerlite`, `S-vercel-pagina`
- [ ] `S-vercel-pagina` **13.8** Publicar o site do Instituto AMS com a página de pré-venda na Cloudflare Pages · _Claude com você, ~60 min_
  - ✅ Pronto quando: Página no ar com o domínio e o Pixel
  - 📝 Fica na Cloudflare Pages porque o plano grátis do Vercel não permite uso comercial. O Claude publica pelo conector da Cloudflare ou pelo Wrangler.
  - 🔗 Liga com: `S-site-pessoal`, `S-site-grupo`
- [ ] `S-site-grupo` **13.9** Publicar o site do Grupo AMtech e o Catálogo do HTML · _Claude com você, ~90 min_
  - ✅ Pronto quando: Os dois sites no ar com domínio e HTTPS
  - 🔗 Liga com: `S-vercel-pagina`, `S-catalogo-alunos`, `R-catalogo`
- [ ] `S-catalogo-alunos` **13.10** Mostrar o Catálogo do HTML aos alunos e ex-alunos · _Você, ~20 min_
  - ✅ Pronto quando: Alunos publicando os próprios sites pelo Catálogo
  - 📝 É material grátis da escola, não venda. Nada de oferecer produto pago a aluno menor de idade; ex-alunos adultos podem seguir as redes.
  - 🔗 Liga com: `S-site-grupo`, `S-umami`
- [ ] `S-umami` **13.11** Ligar o Umami nos sites · _Claude com você, ~20 min_
  - ✅ Pronto quando: Uma visita de teste aparece no painel do Umami
  - 🔗 Liga com: `S-catalogo-alunos`, `S-search-console`
- [ ] `S-search-console` **13.12** Ligar o Google Search Console no domínio e enviar o sitemap de cada site · _Você, ~10 min_
  - ✅ Pronto quando: Propriedade verificada e sitemaps lidos
  - 🔗 Liga com: `S-umami`, `S-hostinger`
- [ ] `S-hostinger` **13.13** Separar na Hostinger o espaço dos sites de clientes · _Claude com você, ~30 min_
  - ✅ Pronto quando: Auditoria da Hostinger sem pendências e um site modelo pronto para copiar
  - 📝 O Claude faz a auditoria pelo plugin da Hostinger e aponta o que precisa de atenção.
  - 🔗 Liga com: `S-search-console`, `S-govbr`, `R-sites`

**Fase 21 do setup** — Dados, IA e pendrives

- [ ] `S-pendrive-kali` **21.1** Gravar o pendrive do Kali com persistência criptografada · _Você, ~90 min_
  - 💻 `winget install --id Rufus.Rufus -e`
  - ✅ Pronto quando: O Kali abre pelo F12 e um arquivo salvo continua lá depois de reiniciar
  - 📝 Siga kali.org/docs/usb. Antes do primeiro boot: suspenda o BitLocker, desligue o Secure Boot e, ao voltar ao Windows, religue o Secure Boot e reative o BitLocker (veja Secure Boot e BitLocker no mapa). Só contra alvos seus ou autorizados.
  - 🔗 Liga com: `S-deposito-legal`, `S-pendrive-arch`, `E-seguranca`
- [ ] `S-pendrive-arch` **21.2** Instalar o Arch num pendrive rápido ou SSD USB, pelo guia oficial · _Você, ~180 min_
  - ✅ Pronto quando: O Arch portátil dá boot e abre o terminal com os seus dotfiles
  - 📝 Use um pendrive para a ISO e outro (64 GB ou mais, USB 3) ou um SSD USB como disco do sistema. Mesmo cuidado com Secure Boot e BitLocker.
  - 🔗 Liga com: `S-pendrive-kali`, `S-gpu-wsl`, `E-linux`
- [ ] `S-gpu-wsl` **21.3** Conferir a GPU dentro do Ubuntu · _Script, ~5 min_
  - 💻 `nvidia-smi`
  - ✅ Pronto quando: Aparece a GTX 1650 com o driver do Windows
  - 🔗 Liga com: `S-pendrive-arch`, `S-lab-ia`
- [ ] `S-lab-ia` **21.4** Montar o laboratório de dados e de IA · _Script, ~30 min_
  - 💻 `bash scripts/wsl/lab-ia.sh`
  - ✅ Pronto quando: Termina com 'Pronto' e mostra a GPU vista pelo PyTorch
  - 🔗 Liga com: `S-gpu-wsl`, `S-ollama-8b`, `E-ia0`
- [ ] `S-ollama-8b` **21.5** Rodar um modelo 8B no Ollama com parte na GPU · _Você, ~15 min_
  - 💻 `ollama run llama3.1:8b`
  - ✅ Pronto quando: 'ollama ps' mostra o modelo dividido entre CPU e GPU e ele responde
  - 📝 Mais lento que um 3B ou 4B, que cabem inteiros na placa. Use o 8B quando a qualidade importar mais que a velocidade.
  - 🔗 Liga com: `S-lab-ia`, `S-zoomcamp`
### 📚 Estudo (3)

- [ ] `E-P1` **Passo 1 — Lógica + Matemática Parte I + Inglês (início)**
  - ✅ Pronto quando: resolve os três exercícios sem travar.
  - 🕒 2-3 semanas
  - 🔗 Liga com: `E-epic`, `E-P2`, `H-fimbloco`, `H-akita`
- [ ] `E-P2` **Passo 2 — Git, SQL, Docker**
  - ✅ Pronto quando: lê um `EXPLAIN ANALYZE` e identifica full scan; ambiente sobe com `docker-compose up`.
  - 🕒 1-2 semanas
  - 🔗 Liga com: `E-P1`, `S-ubuntu-usuario`, `S-docker-wsl`, `S-clonar`, `S-bootstrap`, `S-wsl-reiniciar`, `S-gh-login`, `S-dotfiles`, `S-obsidian-git`, `S-syncthing`, `S-wsl-verificar`, `S-repo-criar`, `S-ci-verde`, `S-protecao-main`, `S-org`, `S-projetos-adr`, `E-P3`
- [ ] `E-robotica-r1` **Robótica R1: Arduino Uno e Leonardo no projeto agro da escola**
  - ✅ Pronto quando: Sensores da escola identificados e testados
  - 🔗 Liga com: `E-robotica-r2`
### 💰 Renda (4)

- [ ] `R-catalogo` **Catálogo do HTML (gratuito) — Pôr chamada para o mini-curso e para a newsletter** · ⭐ 16 pts
  - ✅ Pronto quando: Métrica: visitas e inscritos vindos dele
  - 🕒 passo 13.9 · Semanas 6 e 7 · dez/2026
  - 🔗 Liga com: `S-site-grupo`
- [ ] `R-sites` **Sites e lojas para pequenas empresas — Criar 3 pacotes fixos com preço público** · ⭐ 14 pts
  - ✅ Pronto quando: Métrica: contratos por mês
  - 🕒 passo 13.13 · Semanas 6 e 7 · dez/2026
  - 🔗 Liga com: `S-hostinger`, `R-sitemodelo`, `R-sites3`, `R-sites7`
- [ ] `R-manutpc` **Primeiro cliente de manutenção de PC/notebook (formatação, limpeza, troca por SSD)**
  - ✅ Pronto quando: Primeiro serviço pago
  - 🔗 Liga com: `R-assist`
- [ ] `R-sitemodelo` **Montar 1 site modelo de restaurante para mostrar aos clientes**
  - ✅ Pronto quando: Site publicado e no portfólio
  - 🔗 Liga com: `R-sites`
### 🏦 Finanças pessoais (1)

- [ ] `F-cartao` **Zerar o cartão de crédito**
  - ✅ Pronto quando: Fatura sem parcelas antigas
  - 🔗 Liga com: `F-reserva3`

---

## Etapa 2 · Primeira venda de produto
<a id="e2"></a>

**Quando:** jan a fev/2027 · **Objetivo:** Vender no CPF com tudo medido, lançar o mini-curso e começar C#, TypeScript e Python.

### 🛠️ Setup (36)


**Fase 14 do setup** — Vendas e finanças no CPF

- [ ] `S-govbr` **14.1** Subir a conta gov.br para prata ou ouro · _Você, ~20 min_
  - ✅ Pronto quando: Nível prata ou ouro aparece no app gov.br
  - 🔗 Liga com: `S-hostinger`, `S-banco`
- [ ] `S-banco` **14.2** Abrir a conta bancária separada para o que você vende (no CPF) · _Você, ~30 min_
  - ✅ Pronto quando: Conta aberta; todas as plataformas vão pagar nela
  - 🔗 Liga com: `S-govbr`, `S-contador`
- [ ] `S-contador` **14.3** Fazer a consulta com o contador: carnê-leão e a partir de que renda abrir CNPJ · _Você, ~60 min_
  - ✅ Pronto quando: Regras do carnê-leão anotadas e o valor de virada para o CNPJ definido
  - 🔗 Liga com: `S-banco`, `S-legal`
- [ ] `S-legal` **14.4** Publicar termos de uso e política de privacidade (LGPD) e ter o contrato padrão de serviço · _Claude com você, ~60 min_
  - ✅ Pronto quando: Links de termos e privacidade no rodapé de todos os sites; contrato em modelo editável
  - 📝 O Claude rascunha; antes de usar, peça para o contador ou um advogado revisar. Isto vem antes de coletar e-mail ou vender.
  - 🔗 Liga com: `S-contador`, `S-plataformas`
- [ ] `S-plataformas` **14.5** Criar as contas da Hotmart e da Kiwify no CPF e cadastrar o mini-curso · _Você, ~60 min_
  - ✅ Pronto quando: Produto em rascunho nas duas
  - 🔗 Liga com: `S-legal`, `S-outras-plataformas`
- [ ] `S-outras-plataformas` **14.6** Abrir as contas na Eduzz e na Udemy e publicar artigos e projetos na DIO · _Você, ~60 min_
  - ✅ Pronto quando: Contas aprovadas; formulário fiscal da Udemy enviado; primeiro artigo publicado na DIO
  - 📝 Na Udemy o recebimento é por PayPal ou Payoneer e vai para o carnê-leão como renda do exterior.
  - 🔗 Liga com: `S-plataformas`, `S-mercado-pago`, `R-dio`
- [ ] `S-mercado-pago` **14.7** Ativar o Mercado Pago para Pix e cartão das aulas e dos sites · _Você, ~20 min_
  - ✅ Pronto quando: Link de pagamento de teste pago e estornado
  - 🔗 Liga com: `S-outras-plataformas`, `S-agenda`
- [ ] `S-agenda` **14.8** Criar a agenda online no Cal.com com pagamento para as aulas particulares · _Você, ~30 min_
  - ✅ Pronto quando: Horário de teste marcado e cobrado
  - 🔗 Liga com: `S-mercado-pago`, `S-crm`, `R-aulas`
- [ ] `S-crm` **14.9** Criar o CRM em planilha com origem e consentimento de cada cliente · _Claude com você, ~30 min_
  - ✅ Pronto quando: Planilha com colunas de oferta, origem, consentimento LGPD e próximo passo
  - 🔗 Liga com: `S-agenda`, `S-comunidade`
- [ ] `S-comunidade` **14.10** Abrir a comunidade dos alunos (Discord ou grupo) · _Você, ~30 min_
  - ✅ Pronto quando: Regras publicadas e convite automático na compra
  - 🔗 Liga com: `S-crm`, `S-afiliados`
- [ ] `S-afiliados` **14.11** Entrar nos programas de afiliados (Amazon, Hotmart) e criar a lista de links · _Você, ~30 min_
  - ✅ Pronto quando: Links de afiliado com UTM numa nota do Obsidian
  - 🔗 Liga com: `S-comunidade`, `S-utm`, `R-afiliados`
- [ ] `S-utm` **14.12** Adotar o padrão de UTM em todo link · _Claude com você, ~15 min_
  - ✅ Pronto quando: Gerador de links com UTM salvo e usado no primeiro post
  - 🔗 Liga com: `S-afiliados`, `S-calc-regras`
- [ ] `S-calc-regras` **14.13** Calcular o lucro por venda de cada oferta e definir as regras de corte dos anúncios · _Você, ~30 min_
  - ✅ Pronto quando: CPA de empate e CPA da margem anotados para cada oferta ativa
  - 🔗 Liga com: `S-utm`, `S-ofertas`
- [ ] `S-ofertas` **14.14** Revisar o portfólio de ofertas: estágio, próximo passo e padrão de qualidade · _Claude com você, ~45 min_
  - ✅ Pronto quando: Uma oferta em construção e uma em validação, cada uma com o checklist de pronto
  - 📝 O Claude cria o comando /revisar-oferta, que confere um lançamento contra o padrão de qualidade antes de ir ao ar.
  - 🔗 Liga com: `S-calc-regras`, `S-avaliacoes`
- [ ] `S-avaliacoes` **14.15** Ligar a pergunta de satisfação depois de cada compra ou serviço e o pedido de avaliação no Google · _Claude com você, ~30 min_
  - ✅ Pronto quando: Compra de teste recebe a pergunta por e-mail
  - 🔗 Liga com: `S-ofertas`, `S-prospeccao`
- [ ] `S-prospeccao` **14.16** Montar a lista de parceiros e a primeira mensagem de prospecção · _Claude com você, ~45 min_
  - ✅ Pronto quando: 10 parceiros qualificados e a mensagem revisada por você
  - 📝 O Claude busca e qualifica; quem envia é você.
  - 🔗 Liga com: `S-avaliacoes`, `S-inpi`
- [ ] `S-inpi` **14.17** Pesquisar e pedir o registro das marcas no INPI · _Você, ~60 min_
  - ✅ Pronto quando: Pesquisa sem conflito e pedido protocolado (ou decisão de esperar, anotada)
  - 🔗 Liga com: `S-prospeccao`, `S-carne-leao`
- [ ] `S-carne-leao` **14.18** Fazer o primeiro carnê-leão do mês e marcar o lembrete mensal · _Você, ~30 min_
  - ✅ Pronto quando: DARF gerado (ou mês sem receita registrado) e lembrete todo dia 20
  - 🔗 Liga com: `S-inpi`, `S-irpf`, `F-f3`
- [ ] `S-irpf` **14.19** Separar a pasta da declaração anual do IR · _Você, ~15 min_
  - ✅ Pronto quando: Pasta com informes e carnês do ano, guardada no backup
  - 🔗 Liga com: `S-carne-leao`, `S-caixa`
- [ ] `S-caixa` **14.20** Começar o Caixa da Casa numa planilha até o sistema AM Rendara existir · _Claude com você, ~30 min_
  - ✅ Pronto quando: Entradas e saídas do mês lançadas, separando casa e vendas
  - 🔗 Liga com: `S-irpf`, `S-tunel`, `R-rendara`

**Fase 15 do setup** — Vendas medidas

- [ ] `S-tunel` **15.1** Criar o túnel público para os webhooks (Cloudflare Tunnel) e preencher N8N_WEBHOOK_URL · _Você, ~40 min_
  - ✅ Pronto quando: https://n8n.seu-dominio responde fora de casa
  - 📝 Só o caminho de webhook precisa ficar público; o painel do n8n fica protegido.
  - 🔗 Liga com: `S-caixa`, `S-fluxo-vendas`
- [ ] `S-fluxo-vendas` **15.2** Criar no n8n o fluxo: webhook Hotmart, Kiwify e Eduzz → tabela vendas · _Claude com você, ~60 min_
  - ✅ Pronto quando: Venda de teste aparece na tabela vendas
  - 📝 O Claude monta o fluxo com você no n8n; a tabela já tem a trava contra venda duplicada.
  - 🔗 Liga com: `S-tunel`, `S-gastos`
- [ ] `S-gastos` **15.3** Lançar os gastos de anúncio (manual no começo, depois pela API de cada rede) · _Você, ~15 min_
  - ✅ Pronto quando: Tabela gastos com a primeira campanha
  - 🔗 Liga com: `S-fluxo-vendas`, `S-painel-lucro`
- [ ] `S-painel-lucro` **15.4** Montar o painel de lucro no Grafana sobre a view lucro_por_produto_mes · _Claude com você, ~45 min_
  - ✅ Pronto quando: Painel mostra receita, anúncio, lucro e CPA por produto
  - 🔗 Liga com: `S-gastos`, `S-teste-dev`

**Fase 16 do setup** — Teste do núcleo

- [ ] `S-teste-dev` **16.1** Dev: mudar algo num repositório, commit assinado, push, CI verde · _Você, ~15 min_
  - ✅ Pronto quando: Selo Verified no commit e CI verde
  - 🔗 Liga com: `S-painel-lucro`, `S-teste-conteudo`
- [ ] `S-teste-conteudo` **16.2** Conteúdo: arquivo na entrada → peças na fila → aviso no Telegram · _Você, ~20 min_
  - ✅ Pronto quando: Pasta nova na fila e mensagem no celular
  - 🔗 Liga com: `S-teste-dev`, `S-teste-venda`
- [ ] `S-teste-venda` **16.3** Venda: compra de teste na Hotmart → linha na tabela vendas → painel de lucro · _Você, ~20 min_
  - ✅ Pronto quando: Venda de teste no Grafana
  - 🔗 Liga com: `S-teste-conteudo`, `S-tudo-verde`
- [ ] `S-tudo-verde` **16.4** Rodar os três verificadores juntos · _Script, ~5 min_
  - ✅ Pronto quando: verificar.ps1, verificar.sh e verificar.sh --servicos sem FALTA
  - 🔗 Liga com: `S-teste-venda`, `S-mc-roteiro`

**Fase 17 do setup** — Primeira venda: o mini-curso no ar

- [ ] `S-mc-roteiro` **17.1** Fechar o roteiro das 5 primeiras aulas do mini-curso a partir do acervo · _Claude com você, ~120 min_
  - ✅ Pronto quando: 5 aulas com objetivo, exemplo e exercício, no Obsidian
  - 🔗 Liga com: `S-tudo-verde`, `S-mc-gravar`, `R-minicurso`
- [ ] `S-mc-gravar` **17.2** Gravar e editar as 5 aulas · _Você, ~600 min_
  - ✅ Pronto quando: 5 vídeos finais exportados no modelo do estúdio
  - 🔗 Liga com: `S-mc-roteiro`, `S-mc-hotmart`
- [ ] `S-mc-hotmart` **17.3** Subir as aulas na Hotmart com preço e garantia de 7 dias · _Você, ~120 min_
  - ✅ Pronto quando: Produto aprovado na Hotmart, com checkout funcionando
  - 📝 A garantia de 7 dias é o direito de arrependimento do Código de Defesa do Consumidor para compra pela internet.
  - 🔗 Liga com: `S-mc-gravar`, `S-mc-pagina`
- [ ] `S-mc-pagina` **17.4** Página de vendas no Instituto AMS: promessa, conteúdo, preço e garantia · _Claude com você, ~120 min_
  - ✅ Pronto quando: Página no ar levando ao checkout, com Pixel e UTM
  - 📝 Sem depoimento inventado: só depoimentos reais, com autorização, quando existirem.
  - 🔗 Liga com: `S-mc-hotmart`, `S-mc-isca`
- [ ] `S-mc-isca` **17.5** Isca grátis (aula 1) com a sequência de e-mails que leva à venda · _Claude com você, ~90 min_
  - ✅ Pronto quando: Inscrição de teste recebe os 5 e-mails e o último leva ao checkout
  - 🔗 Liga com: `S-mc-pagina`, `S-mc-lancar`, `R-newsletter`
- [ ] `S-mc-lancar` **17.6** Abrir a pré-venda: lista de e-mail, Instagram, WhatsApp e LinkedIn · _Você, ~120 min_
  - ✅ Pronto quando: Lançamento publicado em todos os canais, com UTM
  - 🔗 Liga com: `S-mc-isca`, `S-mc-primeira-venda`
- [ ] `S-mc-primeira-venda` **17.7** Primeira venda real: acesso, suporte, painel e carnê-leão · _Você, ~60 min_
  - ✅ Pronto quando: Venda paga, aluno com acesso, dúvida respondida em até 24 h, linha na tabela vendas e venda lançada no carnê-leão
  - 🔗 Liga com: `S-mc-lancar`, `S-mc-outras`
- [ ] `S-mc-outras` **17.8** Publicar o mini-curso também na Kiwify, Eduzz e Udemy · _Você, ~120 min_
  - ✅ Pronto quando: Mini-curso à venda nas quatro plataformas
  - 🔗 Liga com: `S-mc-primeira-venda`, `S-template-aura`, `R-udemy`
### 📚 Estudo (3)

- [ ] `E-P3` **Passo 3 — C# Fundamentals + TypeScript + Matemática Parte II (início)**
  - ✅ Pronto quando: entidades compilam sem warning de nulo; Euclides testado.
  - 🕒 2-3 semanas
  - 🔗 Liga com: `E-P2`, `E-py`, `E-P4`
- [ ] `E-py` **Começar o bloco paralelo de Python (1–2 h/semana, refazendo os exercícios de cada Passo)**
  - ✅ Pronto quando: Exercícios do Passo 3 refeitos em Python e testados com pytest
  - 🔗 Liga com: `E-P3`, `E-ia0`
- [ ] `E-fisica` **Comprar o livro de Física básica e mandar o índice para montar a trilha**
  - ✅ Pronto quando: Trilha de Física escrita no vault
  - 🔗 Liga com: `E-matematica`
### 💰 Renda (7)

- [ ] `R-afiliados` **Afiliados (ferramentas, livros, equipamentos que você usa) — Montar a página 'meu setup' com links de afiliado** · ⭐ 16 pts
  - ✅ Pronto quando: Métrica: comissões por mês
  - 🕒 passo 14.11 · Semanas 8 a 10 · dez/2026 a jan/2027
  - 🔗 Liga com: `S-afiliados`
- [ ] `R-minicurso` **Mini-curso Lógica de Programação — Gravar as 5 primeiras aulas e abrir a pré-venda com a isca grátis** · ⭐ 16 pts
  - ✅ Pronto quando: Métrica: vendas por semana e conversão da página
  - 🕒 passo 17.1 · Semanas 12 a 15 · jan a fev/2027
  - 🔗 Liga com: `S-mc-roteiro`, `R-meta7k`
- [ ] `R-rendara` **AM Rendara (finanças), começando pela planilha — Vender a planilha do Caixa da Casa antes de construir o sistema** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: vendas da planilha
  - 🕒 passo 14.20 · Semanas 8 a 10 · dez/2026 a jan/2027
  - 🔗 Liga com: `S-caixa`, `E-P14`, `E-f4`, `E-ia3`, `R-consultoria`
- [ ] `R-newsletter` **Newsletter (patrocínio e vendas) — Fazer a isca grátis e a sequência de boas-vindas** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: inscritos e cliques
  - 🕒 passo 17.5 · Semanas 12 a 15 · jan a fev/2027
  - 🔗 Liga com: `S-mc-isca`
- [ ] `R-udemy` **Versões dos cursos na Udemy (português e inglês) — Publicar o mini-curso depois do lançamento próprio** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: vendas e avaliação média
  - 🕒 passo 17.8 · Semanas 12 a 15 · jan a fev/2027
  - 🔗 Liga com: `S-mc-outras`
- [ ] `R-aulas` **Aulas particulares — Publicar a agenda com pagamento antecipado** · ⭐ 13 pts
  - ✅ Pronto quando: Métrica: horas vendidas por semana
  - 🕒 passo 14.8 · Semanas 8 a 10 · dez/2026 a jan/2027
  - 🔗 Liga com: `S-agenda`, `R-msg`, `R-aulasmeta`, `H-ensina`
- [ ] `R-dio` **Parceria DIO — Publicar 3 artigos e um projeto na DIO** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: convite ou resposta
  - 🕒 passo 14.6 · Semanas 8 a 10 · dez/2026 a jan/2027
  - 🔗 Liga com: `S-outras-plataformas`
### 🏦 Finanças pessoais (3)

- [ ] `F-reserva3` **Reserva de emergência de 3 meses de gastos fixos**
  - ✅ Pronto quando: Valor guardado em caixa separado
  - 🔗 Liga com: `F-cartao`, `F-consorcio`, `F-acoes`, `F-reserva6`
- [ ] `F-sairescola` **Decisão: sair da escola só se a renda extra passou de R$ 1.500/mês por 2 meses seguidos**
  - ✅ Pronto quando: Decisão tomada com os números
  - 🔗 Liga com: `R-meta7k`
- [ ] `F-consorcio` **Decidir o lance de R$ 14 mil no consórcio da moto sem furar a reserva**
  - ✅ Pronto quando: Decisão anotada
  - 🔗 Liga com: `F-reserva3`

---

## Etapa 3 · Rendas crescendo
<a id="e3"></a>

**Quando:** mar a jun/2027 · **Objetivo:** API, frontend e testes do Kaixara; uma oferta nova por vez; contabilidade e matemática financeira.

### 🛠️ Setup (55)


**Fase 18 do setup** — Base dos sistemas AM

- [ ] `S-template-aura` **18.1** Gerar o modelo de sistema com /novo-sistema-aura · _Claude com você, ~120 min_
  - ✅ Pronto quando: Sistema exemplo sobe com 'dotnet run' e passa nos testes
  - 📝 Clean Architecture + DDD, EF Core com Npgsql, multi-tenant com RLS, SignalR com Redis, OpenAPI com Scalar, Next.js com o Aura Design System e Storybook, testes com xUnit, Playwright e k6.
  - 🔗 Liga com: `S-mc-outras`, `S-auth`, `E-P4`, `E-P12`
- [ ] `S-auth` **18.2** Ligar o login: Keycloak no dev e Entra ID na nuvem · _Claude com você, ~60 min_
  - ✅ Pronto quando: Usuário de teste entra e só vê os dados da própria empresa
  - 🔗 Liga com: `S-template-aura`, `S-observabilidade-dev`, `E-P4`
- [ ] `S-observabilidade-dev` **18.3** Ligar a observabilidade do dev: .NET Aspire, OpenTelemetry, Prometheus, Seq, Mailpit e Caddy · _Claude com você, ~60 min_
  - ✅ Pronto quando: Painel do Aspire mostra trace de uma requisição; e-mail de teste cai no Mailpit
  - 🔗 Liga com: `S-auth`, `S-sentry`, `E-P9`
- [ ] `S-sentry` **18.4** Criar o projeto no Sentry e ligar no modelo · _Você, ~20 min_
  - ✅ Pronto quando: Erro de teste aparece no Sentry
  - 🔗 Liga com: `S-observabilidade-dev`, `S-sonar`
- [ ] `S-sonar` **18.5** Ligar o SonarQube Cloud no repositório do modelo · _Você, ~20 min_
  - ✅ Pronto quando: Nota de qualidade aparece no pull request
  - 📝 O plano grátis cobre repositório público; confira o limite para privado antes de ligar.
  - 🔗 Liga com: `S-sentry`, `S-ghcr`, `E-P6`
- [ ] `S-ghcr` **18.6** Publicar a imagem Docker da API no GHCR pelo CI · _Claude com você, ~30 min_
  - ✅ Pronto quando: Imagem com a tag do commit aparece nos pacotes do GitHub
  - 🔗 Liga com: `S-sonar`, `S-templates-venda`
- [ ] `S-templates-venda` **18.7** Separar o que do modelo pode virar template à venda · _Você, ~30 min_
  - ✅ Pronto quando: Lista de templates no portfólio de ofertas
  - 🔗 Liga com: `S-ghcr`, `S-vaga`, `R-templates`

**Fase 19 do setup** — Nuvem e deploy

- [ ] `S-nuvem-clis` **19.1** Instalar Azure CLI, Terraform, Vercel CLI e Wrangler · _Script, ~15 min_
  - 💻 `bash scripts/wsl/nuvem.sh`
  - ✅ Pronto quando: Termina com 'Pronto'; verificar.sh mostra as quatro ferramentas
  - 🔗 Liga com: `S-vaga`, `S-azure-conta`, `E-P10`
- [ ] `S-azure-conta` **19.2** Criar a conta Azure com alerta de orçamento · _Você, ~30 min_
  - ✅ Pronto quando: 'az login' entra e o alerta de gasto está ligado
  - 📝 Ligue o alerta antes de criar qualquer recurso. O Microsoft Learn do conector ajuda a escolher o serviço mais barato.
  - 🔗 Liga com: `S-nuvem-clis`, `S-terraform-base`, `E-P10`
- [ ] `S-terraform-base` **19.3** Criar com Terraform o grupo de recursos, o banco e o Key Vault do primeiro sistema · _Claude com você, ~90 min_
  - ✅ Pronto quando: 'terraform plan' sem diferenças depois do apply
  - 🔗 Liga com: `S-azure-conta`, `S-arquivos-nuvem`, `E-P10`
- [ ] `S-arquivos-nuvem` **19.4** Criar o armazenamento de arquivos (R2 da Cloudflare ou Blob) · _Claude com você, ~30 min_
  - ✅ Pronto quando: Upload de teste pelo sistema exemplo
  - 🔗 Liga com: `S-terraform-base`, `S-email-transacional`, `E-P10`
- [ ] `S-email-transacional` **19.5** Configurar o e-mail transacional (Resend) com o domínio verificado · _Você, ~30 min_
  - ✅ Pronto quando: E-mail de confirmação de conta chega na caixa de entrada, não no spam
  - 🔗 Liga com: `S-arquivos-nuvem`, `S-deploy-teste`, `E-P10`
- [ ] `S-deploy-teste` **19.6** Fazer o primeiro deploy do sistema exemplo · _Claude com você, ~60 min_
  - ✅ Pronto quando: Sistema no ar com HTTPS, login e erro de teste no Sentry
  - 🔗 Liga com: `S-email-transacional`, `S-aura-status`, `E-P5`, `E-P10`
- [ ] `S-aura-status` **19.7** Criar o aura-status: painel de repositórios, backup e Dependabot · _Claude com você, ~120 min_
  - ✅ Pronto quando: Painel mostra o estado de todos os repositórios
  - 🔗 Liga com: `S-deploy-teste`, `S-modelo-metodo`, `E-P10`

**Fase 20 do setup** — Editora · ⏸ gatilho: O capítulo 1 e o seu modelo de criação prontos

- [ ] `S-modelo-metodo` **20.1** Entregar o seu modelo de criação e o seu método passo a passo · _Você, ~120 min_
  - ✅ Pronto quando: metodo.yaml com cada etapa, entrada, saída e critério de conclusão; template de capítulo pronto
  - 🔗 Liga com: `S-aura-status`, `S-livro-repo`
- [ ] `S-livro-repo` **20.2** Criar o repositório do livro com fonte única, classe LaTeX, exercícios em YAML e CI · _Claude com você, ~120 min_
  - ✅ Pronto quando: Um push gera PDF, EPUB e o gabarito sem erro
  - 📝 Depende do capítulo 1 e do seu modelo. O conteúdo é seu; nada de material de terceiros.
  - 🔗 Liga com: `S-modelo-metodo`, `S-editora-imagens`
- [ ] `S-editora-imagens` **20.3** Construir o pipeline de imagens do livro: busca nos acervos, filtro de licença, folha de contato e créditos · _Claude com você, ~240 min_
  - ✅ Pronto quando: Uma figura do capítulo 1 sai com licença conferida, ficha e crédito; o build falha se faltar ficha
  - 🔗 Liga com: `S-livro-repo`, `S-editora-figuras`
- [ ] `S-editora-figuras` **20.4** Figuras, tabelas e texto alternativo gerados por código · _Claude com você, ~180 min_
  - ✅ Pronto quando: Gráficos e tabelas do capítulo 1 gerados no build, com texto alternativo revisado por você
  - 🔗 Liga com: `S-editora-imagens`, `S-editora-agentes`
- [ ] `S-editora-agentes` **20.5** Criar os agentes da editora: revisor técnico, gabarito, leitor iniciante e consistência · _Claude com você, ~180 min_
  - ✅ Pronto quando: Os agentes apontam problemas reais no capítulo 1 e você corrige
  - 🔗 Liga com: `S-editora-figuras`, `S-editais`
- [ ] `S-editais` **20.6** Montar a matriz de editais e o quadro de referências · _Claude com você, ~60 min_
  - ✅ Pronto quando: Cada tópico dos editais ligado a um capítulo; lacunas listadas
  - 🔗 Liga com: `S-editora-agentes`, `S-selo`
- [ ] `S-selo` **20.7** Definir o selo Editora AMS Silva (nome, logo e uso no CPF) · _Você, ~30 min_
  - ✅ Pronto quando: Logo aprovado e aplicado na classe LaTeX
  - 🔗 Liga com: `S-editais`, `S-isbn-ficha`
- [ ] `S-isbn-ficha` **20.8** Comprar os ISBNs na CBL e pedir a ficha catalográfica · _Você, ~60 min_
  - ✅ Pronto quando: ISBN do impresso e do ebook, código de barras e ficha no verso da folha de rosto
  - 🔗 Liga com: `S-selo`, `S-beta`
- [ ] `S-beta` **20.9** Escolher 3 a 5 leitores beta e um revisor técnico · _Você, ~30 min_
  - ✅ Pronto quando: Nomes confirmados e formulário de retorno pronto
  - 🔗 Liga com: `S-isbn-ficha`, `S-kdp`
- [ ] `S-kdp` **20.10** Criar a conta no Amazon KDP e cadastrar o livro em rascunho · _Você, ~60 min_
  - ✅ Pronto quando: Livro em rascunho com capa, preço e prévia conferida
  - 🔗 Liga com: `S-beta`, `S-deposito-legal`, `R-livro`
- [ ] `S-deposito-legal` **20.11** Enviar o depósito legal à Biblioteca Nacional até 30 dias depois de publicar · _Você, ~30 min_
  - ✅ Pronto quando: Comprovante de envio guardado
  - 🔗 Liga com: `S-kdp`, `S-pendrive-kali`

**Fase 22 do setup** — Mais ofertas, uma por vez · ⏸ gatilho: A primeira venda do mini-curso aconteceu

- [ ] `S-of-meu-setup` **22.1** Página 'meu setup' com links de afiliado · _Claude com você, ~90 min_
  - ✅ Pronto quando: Página publicada com links marcados com UTM
  - 🔗 Liga com: `S-modelo-no-ollama`, `S-of-catalogo`
- [ ] `S-of-catalogo` **22.2** Pôr no Catálogo do HTML a chamada para o mini-curso e para a newsletter · _Claude com você, ~30 min_
  - ✅ Pronto quando: Chamadas no ar, medidas por UTM
  - 🔗 Liga com: `S-of-meu-setup`, `S-of-aulasprof`
- [ ] `S-of-aulasprof` **22.3** Kit de aulas prontas para professores: uma disciplina que você já leciona · _Você, ~600 min_
  - ✅ Pronto quando: Kit de 1 disciplina (planos, slides, avaliações) à venda
  - 📝 Material feito para a escola: reescreva do zero, no seu tempo e sem a identidade da escola, ou confirme os direitos.
  - 🔗 Liga com: `S-of-catalogo`, `S-of-planilha`, `R-aulasprof`
- [ ] `S-of-planilha` **22.4** Vender a planilha do Caixa da Casa antes de construir o AM Rendara · _Você, ~180 min_
  - ✅ Pronto quando: 10 planilhas vendidas
  - 🔗 Liga com: `S-of-aulasprof`, `S-of-automacao`
- [ ] `S-of-automacao` **22.5** Automação com IA para pequenos negócios: 1 implantação grátis em troca de caso · _Claude com você, ~600 min_
  - ✅ Pronto quando: Um negócio usando a automação e um caso escrito com autorização
  - 🔗 Liga com: `S-of-planilha`, `S-of-simulados`, `R-automacaoia`
- [ ] `S-of-simulados` **22.6** Banco de questões para concursos: 50 questões comentadas grátis para medir a procura · _Você, ~480 min_
  - ✅ Pronto quando: 50 questões publicadas e a procura medida
  - 🔗 Liga com: `S-of-automacao`, `S-of-anki`, `R-simulados`
- [ ] `S-of-anki` **22.7** Baralhos Anki de TI e concursos: o primeiro, do capítulo 1 · _Você, ~180 min_
  - ✅ Pronto quando: Primeiro baralho à venda
  - 🔗 Liga com: `S-of-simulados`, `S-of-newsletter`, `R-anki`
- [ ] `S-of-newsletter` **22.8** Newsletter com patrocínio e vendas · _Você, ~120 min_
  - ✅ Pronto quando: Edição semanal por 8 semanas e o primeiro patrocinador
  - 🔗 Liga com: `S-of-anki`, `S-of-agencia`
- [ ] `S-of-agencia` **22.9** Presença digital para comércio local, oferecida a 5 clientes de sites · _Você, ~240 min_
  - ✅ Pronto quando: Primeiro cliente mensal
  - 🔗 Liga com: `S-of-newsletter`, `S-of-sites`, `R-agencialocal`
- [ ] `S-of-sites` **22.10** Sites: 3 pacotes fixos com preço público · _Você, ~180 min_
  - ✅ Pronto quando: Pacotes publicados e primeiro cliente fechado
  - 🔗 Liga com: `S-of-agencia`, `S-of-remoto`
- [ ] `S-of-remoto` **22.11** Suporte remoto com plano mensal para empresas · _Você, ~240 min_
  - ✅ Pronto quando: 3 empresas no plano mensal
  - 🔗 Liga com: `S-of-sites`, `S-of-consultoria`, `R-remoto`
- [ ] `S-of-consultoria` **22.12** Implantação de ficha técnica e engenharia de cardápio para restaurantes · _Você, ~480 min_
  - ✅ Pronto quando: Um estudo de caso, com autorização do dono
  - 🔗 Liga com: `S-of-remoto`, `S-of-ammentor`, `R-consultoriaresto`
- [ ] `S-of-ammentor` **22.13** AM Mentor: banco de exercícios com correção, começando pelo capítulo 1 · _Claude com você, ~1200 min_
  - ✅ Pronto quando: Primeiros alunos usando
  - 🔗 Liga com: `S-of-consultoria`, `S-of-dark`, `R-ammentor`
- [ ] `S-of-dark` **22.14** Canais sem rosto: 3 vídeos por semana por 8 semanas e medir · _Você, ~1200 min_
  - ✅ Pronto quando: 24 vídeos publicados e o resultado medido
  - 🔗 Liga com: `S-of-ammentor`, `S-of-comunidade`, `R-dark`
- [ ] `S-of-comunidade` **22.15** Comunidade paga do Instituto AMS · _Você, ~240 min_
  - ✅ Pronto quando: Comunidade aberta com os primeiros assinantes
  - 📝 Só com 200 alunos pagantes.
  - 🔗 Liga com: `S-of-dark`, `S-of-oficinas`, `R-comunidade`
- [ ] `S-of-oficinas` **22.16** Oficinas de robótica e programação para escolas: plano de 8 encontros · _Você, ~600 min_
  - ✅ Pronto quando: Primeira escola contratando
  - 🔗 Liga com: `S-of-comunidade`, `S-of-encomenda`, `R-oficinas`
- [ ] `S-of-encomenda` **22.17** Sistemas sob encomenda, com 50% de entrada · _Você, ~240 min_
  - ✅ Pronto quando: Primeiro contrato assinado
  - 🔗 Liga com: `S-of-oficinas`, `S-of-aulasushi`, `R-encomenda`
- [ ] `S-of-aulasushi` **22.18** Aula de sushi e sushiman para eventos: 2 eventos de teste · _Você, ~240 min_
  - ✅ Pronto quando: 2 eventos pagos, com as regras sanitárias conferidas
  - 🔗 Liga com: `S-of-encomenda`, `S-of-workshop`, `R-aulasushi`
- [ ] `S-of-workshop` **22.19** Workshop presencial para pequenos empresários: piloto com 10 vagas · _Você, ~480 min_
  - ✅ Pronto quando: Piloto realizado com 10 inscritos pagantes
  - 🔗 Liga com: `S-of-aulasushi`, `S-of-pausadas`, `R-workshop`
- [ ] `S-of-pausadas` **22.20** Revisar a cada trimestre as ofertas pausadas (AM Taskoro) · _Você, ~30 min_
  - ✅ Pronto quando: Decisão anotada: retomar ou manter pausada
  - 🔗 Liga com: `S-of-workshop`, `S-ads-meta`, `R-taskoro`

**Fase 23 do setup** — Marketing pago e crescimento · ⏸ gatilho: O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar

- [ ] `S-ads-meta` **23.1** Primeira campanha na Meta com orçamento de teste · _Você, ~120 min_
  - ✅ Pronto quando: Campanha com CPA abaixo do de empate por 2 semanas
  - 🔗 Liga com: `S-of-pausadas`, `S-ads-google-tiktok`
- [ ] `S-ads-google-tiktok` **23.2** Google e YouTube Ads, depois TikTok Ads · _Você, ~180 min_
  - ✅ Pronto quando: Cada canal com a primeira campanha medida no painel
  - 🔗 Liga com: `S-ads-meta`, `S-ads-outros`
- [ ] `S-ads-outros` **23.3** Kwai, Pinterest, LinkedIn, Spotify e mídia nativa, um por vez · _Você, ~240 min_
  - ✅ Pronto quando: Cada canal testado e mantido ou cortado pelas regras
  - 🔗 Liga com: `S-ads-google-tiktok`, `S-influenciadores`
- [ ] `S-influenciadores` **23.4** Influenciadores e newsletters parceiras com cupom · _Você, ~120 min_
  - ✅ Pronto quando: Primeira parceria medida por cupom e UTM
  - 🔗 Liga com: `S-ads-outros`, `S-afiliados-proprios`
- [ ] `S-afiliados-proprios` **23.5** Abrir o programa de afiliados do mini-curso · _Você, ~60 min_
  - ✅ Pronto quando: Primeiro afiliado vendendo
  - 🔗 Liga com: `S-influenciadores`, `S-horario`
- [ ] `S-horario` **23.6** Ligar o algoritmo de horário com 3 meses de dados de publicação · _Claude com você, ~120 min_
  - ✅ Pronto quando: 80% dos posts nas melhores faixas, 20% testando
  - 🔗 Liga com: `S-afiliados-proprios`, `S-build-in-public`
- [ ] `S-build-in-public` **23.7** Canal build in public: um vídeo por semana das decisões reais · _Você, ~60 min_
  - ✅ Pronto quando: 4 vídeos seguidos publicados
  - 🔗 Liga com: `S-horario`, `S-dublagem`, `R-buildpublic`
- [ ] `S-dublagem` **23.8** Dublar os melhores vídeos para outros idiomas · _Você, ~120 min_
  - ✅ Pronto quando: Um vídeo com faixa de áudio em inglês ou espanhol
  - 🔗 Liga com: `S-build-in-public`, `S-membros`
- [ ] `S-membros` **23.9** Membros do YouTube quando o canal for elegível · _Você, ~30 min_
  - ✅ Pronto quando: Assinatura de membros ativa
  - 🔗 Liga com: `S-dublagem`, `S-formacao`, `R-monetizacao`
- [ ] `S-formacao` **23.10** Primeira formação completa (TI, Matemática ou Finanças) · _Você, ~1200 min_
  - ✅ Pronto quando: Formação gravada e à venda
  - 🔗 Liga com: `S-membros`, `S-nvme-arch`, `R-formti`, `R-formmat`, `R-financas`
### 📚 Estudo (6)

- [ ] `E-P4` **Passo 4 — API, Autenticação e Frontend base**
  - ✅ Pronto quando: login funcional, protegido, com tela real usando os tokens corretos.
  - 🕒 3-4 semanas
  - 🔗 Liga com: `E-P3`, `S-template-aura`, `S-auth`, `F-f1`, `E-P5`
- [ ] `E-P5` **Passo 5 — EF Core + CRUD molde**
  - ✅ Pronto quando: CRUD funciona com teste de concorrência passando.
  - 🕒 1-2 semanas
  - 🔗 Liga com: `E-P4`, `F-f1`, `F-f2`, `S-deploy-teste`, `E-P6`
- [ ] `E-P6` **Passo 6 — Teste como disciplina**
  - ✅ Pronto quando: cobertura real no fluxo de venda, backend e frontend.
  - 🕒 1-2 semanas
  - 🔗 Liga com: `E-P5`, `S-sonar`, `E-P7`
- [ ] `E-linux` **Trilha Linux/Arch até o nível que o dev usa (F1–F2)**
  - ✅ Pronto quando: Fases F1 e F2 da trilha concluídas
  - 🔗 Liga com: `S-pendrive-arch`, `E-robotica-r3`, `E-horizonte`
- [ ] `E-redes` **Trilha de Redes**
  - ✅ Pronto quando: Fases da trilha concluídas com algo testável
  - 🔗 Liga com: `C-comptia`
- [ ] `E-robotica-r2` **Robótica R2: ESP32, sensores e MQTT**
  - ✅ Pronto quando: Coleta de dados do projeto agro funcionando
  - 🔗 Liga com: `E-robotica-r1`
### 💰 Renda (23)

- [ ] `R-aulasprof` **Pacote de aulas prontas para professores de informática — Empacotar uma disciplina que você já leciona (planos, slides, avaliações)** · ⭐ 16 pts
  - ✅ Pronto quando: Métrica: vendas por disciplina
  - 🕒 passo 22.3 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-aulasprof`
- [ ] `R-automacaoia` **Automação com IA para pequenos negócios (WhatsApp, n8n, agenda) — Implantar de graça em um negócio conhecido em troca de caso e depoimento** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: contratos e horas por implantação
  - 🕒 passo 22.5 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-automacao`
- [ ] `R-simulados` **Banco de questões de TI para concursos (PF, PRF, Forças Armadas) — Publicar 50 questões comentadas grátis e medir a procura** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: assinantes
  - 🕒 passo 22.6 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-simulados`
- [ ] `R-anki` **Baralhos Anki de TI e concursos — Gerar o primeiro baralho do Capítulo 1** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: vendas
  - 🕒 passo 22.7 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-anki`
- [ ] `R-buildpublic` **Canal com rosto: construindo o Grupo AMtech em público — Gravar 1 vídeo por semana mostrando uma decisão real (números do planejador, setup, aula)** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: inscritos e vendas atribuídas
  - 🕒 passo 23.7 · A partir de fev/2027
  - 🔗 Liga com: `S-build-in-public`
- [ ] `R-agencialocal` **Presença digital para comércio local (Google Perfil, redes, avaliações) — Oferecer a 5 clientes de sites como complemento** · ⭐ 14 pts
  - ✅ Pronto quando: Métrica: clientes ativos
  - 🕒 passo 22.9 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-agencia`
- [ ] `R-remoto` **Suporte remoto e planos mensais para empresas — Fechar 3 empresas com o plano de R$ 250** · ⭐ 14 pts
  - ✅ Pronto quando: Métrica: contratos ativos
  - 🕒 passo 22.11 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-remoto`
- [ ] `R-consultoriaresto` **Implantação de ficha técnica e engenharia de cardápio — Usar o restaurante onde você trabalha como estudo de caso, se o dono aceitar** · ⭐ 13 pts
  - ✅ Pronto quando: Métrica: contratos
  - 🕒 passo 22.12 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-consultoria`
- [ ] `R-monetizacao` **Monetização das plataformas (YouTube, Instagram) — Consequência dos canais; não é meta em si** · ⭐ 13 pts
  - ✅ Pronto quando: Métrica: receita por mil visualizações
  - 🕒 passo 23.9 · A partir de fev/2027
  - 🔗 Liga com: `S-membros`
- [ ] `R-templates` **Templates e código-fonte — Empacotar o primeiro frontend já pronto com documentação** · ⭐ 13 pts
  - ✅ Pronto quando: Métrica: vendas por template
  - 🕒 passo 18.7 · Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6
  - 🔗 Liga com: `S-templates-venda`
- [ ] `R-ammentor` **AM Mentor: banco de exercícios com correção — Começar com o Capítulo 1 do livro em YAML** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: assinantes e exercícios resolvidos
  - 🕒 passo 22.13 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-ammentor`, `E-ia5`
- [ ] `R-dark` **Canais sem rosto (YouTube, TikTok, Instagram, Facebook) — Publicar 3 vídeos por semana por 8 semanas e medir** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: retenção e cliques para os produtos
  - 🕒 passo 22.14 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-dark`
- [ ] `R-formti` **Formação Téc. em Desenvolvimento de Sistemas (13 disciplinas) — Só depois do mini-curso vender 100 cópias** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: alunos ativos e conclusão
  - 🕒 passo 23.10 · A partir de fev/2027
  - 🔗 Liga com: `S-formacao`
- [ ] `R-livro` **Livro Lógica e Máquina — Entregar o Capítulo 1 para avaliação** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: capítulos prontos e leitores beta
  - 🕒 passo 20.10 · Quando o capítulo 1 estiver pronto
  - 🔗 Liga com: `S-kdp`
- [ ] `R-comunidade` **Comunidade paga do Instituto AMS — Só com 200 alunos pagantes** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: membros e cancelamento
  - 🕒 passo 22.15 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-comunidade`
- [ ] `R-oficinas` **Oficinas de robótica e programação para escolas — Montar o plano de 8 encontros com o kit** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: turmas vendidas
  - 🕒 passo 22.16 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-oficinas`
- [ ] `R-encomenda` **Sistemas sob encomenda — Primeiro cliente via loja ou indicação, com 50% de entrada** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: margem por projeto
  - 🕒 passo 22.17 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-encomenda`
- [ ] `R-aulasushi` **Aula de sushi e sushiman para eventos — Testar 2 eventos com amigos pagantes; confirme as regras sanitárias para preparo na casa do cliente** · ⭐ 10 pts
  - ✅ Pronto quando: Métrica: eventos por mês e pedidos de 'quando abre o restaurante?'
  - 🕒 passo 22.18 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-aulasushi`
- [ ] `R-formmat` **Formação em Matemática — Usar os capítulos de matemática do livro como base** · ⭐ 10 pts
  - ✅ Pronto quando: Métrica: vendas
  - 🕒 passo 23.10 · A partir de fev/2027
  - 🔗 Liga com: `S-formacao`
- [ ] `R-workshop` **Workshops presenciais para pequenos empresários (IA, planilhas, presença digital) — Fazer um piloto com 10 vagas** · ⭐ 10 pts
  - ✅ Pronto quando: Métrica: ingressos vendidos e clientes gerados
  - 🕒 passo 22.19 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-workshop`
- [ ] `R-financas` **Curso de finanças pessoais (conteúdo próprio) — Validar com a planilha do Caixa da Casa antes do curso** · ⭐ 9 pts
  - ✅ Pronto quando: Métrica: vendas da planilha
  - 🕒 passo 23.10 · A partir de fev/2027
  - 🔗 Liga com: `S-formacao`
- [ ] `R-taskoro` **AM Taskoro (gestão de projetos ágeis) — Fica como projeto de portfólio até o Kaixara ter clientes** · ⭐ 6 pts
  - ✅ Pronto quando: Métrica: —
  - 🕒 passo 22.20 · Fev a dez/2027, uma oferta por vez
  - 🔗 Liga com: `S-of-pausadas`
- [ ] `R-sites3` **Sites com manutenção mensal: 3 a 4 clientes**
  - ✅ Pronto quando: 3 contratos de manutenção ativos
  - 🔗 Liga com: `R-sites`
### 🏦 Finanças pessoais (3)

- [ ] `F-acoes` **Próximo pilar do ARCA: ações escolhidas por Barsi e Bazin**
  - ✅ Pronto quando: Primeira compra justificada pelo método
  - 🔗 Liga com: `F-reserva3`
- [ ] `F-f1` **Finanças F1–F2: contabilidade (partidas dobradas, DRE) e matemática financeira**
  - ✅ Pronto quando: Simulador de financiamento bate com o banco
  - 🔗 Liga com: `E-P5`, `E-P7`, `E-P4`
- [ ] `F-f2` **Simulador de financiamento do apartamento e de aportes**
  - ✅ Pronto quando: Simulador conferido
  - 🔗 Liga com: `F-apto`, `E-P5`
### ⚖️ Decisões (1)

- [ ] `D-socia` **Sócia do Rendara: trocar o alvo de CEA (extinta) para CPA + C-Pro I ou CFP**
  - 🔗 Liga com: `R-consultoria`

---

## Etapa 4 · Bater os R$ 7 mil
<a id="e4"></a>

**Quando:** jul a dez/2027 · **Objetivo:** Kaixara completo, arquitetura, candidaturas a vagas e a meta de renda.

### 🛠️ Setup (11)


**Fase 18 do setup** — Base dos sistemas AM

- [ ] `S-vaga` **18.8** Candidatar-se às vagas de dev .NET com GitHub, LinkedIn e site prontos — quando o Passo 8 da trilha de estudo estiver feito (≈ jul a dez/2027) · _Você, ~120 min_
  - ✅ Pronto quando: 10 candidaturas enviadas com o portfólio do sistema exemplo
  - 📝 Data ligada ao Passo 8 do estudo.
  - 🔗 Liga com: `S-templates-venda`, `S-nuvem-clis`, `E-P8`

**Fase 24 do setup** — Linux nativo e laboratório completo

- [ ] `S-nvme-arch` **24.1** Instalar o 2º NVMe e o Arch + Omarchy com boot próprio · _Você, ~300 min_
  - ✅ Pronto quando: Escolha entre Windows e Arch ao ligar, cada um no seu disco
  - 🔗 Liga com: `S-formacao`, `S-neovim`
- [ ] `S-neovim` **24.2** Aprender o Neovim aos poucos · _Você, ~300 min_
  - ✅ Pronto quando: Uma semana editando só no Neovim
  - 🔗 Liga com: `S-nvme-arch`, `S-vms-lab`
- [ ] `S-vms-lab` **24.3** Montar as VMs do laboratório: Kali, Arch, Ubuntu Server, Windows Server e Rocky · _Você, ~300 min_
  - ✅ Pronto quando: Duas VMs numa rede isolada, atacante e alvo
  - 🔗 Liga com: `S-neovim`, `S-ssd-sata`
- [ ] `S-ssd-sata` **24.4** SSD SATA na baia livre para as VMs · _Você, ~60 min_
  - ✅ Pronto quando: VMs rodando do SSD novo
  - 🔗 Liga com: `S-vms-lab`, `S-yubikey`
- [ ] `S-yubikey` **24.5** Chave física no GitHub, Google e Microsoft · _Você, ~60 min_
  - ✅ Pronto quando: Login com a chave nas três contas
  - 🔗 Liga com: `S-ssd-sata`, `S-mic-camera`
- [ ] `S-mic-camera` **24.6** Microfone e câmera · _Você, ~60 min_
  - ✅ Pronto quando: Gravação de teste com áudio limpo sem pós-produção
  - 🔗 Liga com: `S-yubikey`, `S-rag-sistema`

**Fase 27 do setup** — CNPJ e formalização · ⏸ gatilho: A renda passou do valor de virada definido com o contador

- [ ] `S-cnpj` **27.1** Abrir a AMtech Tecnologia (ME no Simples, sócio único) · _Você, ~240 min_
  - ✅ Pronto quando: CNPJ ativo, conta PJ aberta e contador contratado
  - 🔗 Liga com: `S-whitelabel`, `S-ecnpj`
- [ ] `S-ecnpj` **27.2** Certificado digital e-CNPJ · _Você, ~60 min_
  - ✅ Pronto quando: Certificado instalado e guardado no KeePassXC
  - 🔗 Liga com: `S-cnpj`, `S-nfse-api`
- [ ] `S-nfse-api` **27.3** Nota fiscal automática pela API de NFS-e · _Claude com você, ~240 min_
  - ✅ Pronto quando: Venda de teste emite nota sozinha
  - 🔗 Liga com: `S-ecnpj`, `S-pix-automatico`
- [ ] `S-pix-automatico` **27.4** Cobrança recorrente por Pix Automático · _Claude com você, ~240 min_
  - ✅ Pronto quando: Assinatura de teste cobrada por Pix
  - 🔗 Liga com: `S-nfse-api`, `S-ag-analista`
### 📚 Estudo (3)

- [ ] `E-P7` **Passo 7 — Fechar o AM Kaixara: pagamento e cobrança**
  - ✅ Pronto quando: AM Kaixara com fluxo de venda ponta a ponta, pagamento idempotente, ledger fechando em zero.
  - 🕒 2-3 semanas
  - 🔗 Liga com: `E-P6`, `F-f1`, `F-f3`, `R-kaixara`, `S-kaixara`, `E-P8`
- [ ] `E-P8` **Passo 8 — Arquitetura de verdade**
  - ✅ Pronto quando: você refatora uma classe e explica por que segue SOLID.
  - 🕒 contínuo, consolida aqui
  - 🔗 Liga com: `E-P7`, `S-vaga`, `E-f4`, `E-ia0`, `E-P9`
- [ ] `E-f4` **Finanças F4: finanças corporativas e valuation (trilha paralela, depois do Passo 8)**
  - ✅ Pronto quando: Preço-teto Bazin e Graham calculado pelo sistema e conferido à mão
  - 🔗 Liga com: `R-rendara`, `E-P8`, `A-decidir`, `D-paralelas`
### 💰 Renda (3)

- [ ] `R-sites7` **Sites com manutenção mensal: 7 clientes (pagam o salário do restaurante)**
  - ✅ Pronto quando: Manutenção líquida acima de R$ 2.200 por 3 meses
  - 🔗 Liga com: `R-sites`, `F-sairrest`, `R-meta7k`
- [ ] `R-aulasmeta` **Aulas particulares: 8 alunos individuais + 2 turmas online**
  - ✅ Pronto quando: R$ 2.800/mês em aulas
  - 🔗 Liga com: `R-aulas`, `R-meta7k`
- [ ] `R-meta7k` **Meta: R$ 7.000 líquidos por mês**
  - ✅ Pronto quando: 3 meses seguidos acima de R$ 7.000
  - 🔗 Liga com: `R-sites7`, `R-aulasmeta`, `R-minicurso`, `F-sairescola`
### 🏦 Finanças pessoais (2)

- [ ] `F-f3` **Finanças F3: tributação (carnê-leão, IRPF, Simples, notas fiscais)**
  - ✅ Pronto quando: Declaração de IR feita com os dados do seu sistema
  - 🔗 Liga com: `S-carne-leao`, `E-P7`
- [ ] `F-reserva6` **Reserva de 6 meses**
  - ✅ Pronto quando: Valor guardado
  - 🔗 Liga com: `F-reserva3`, `F-reserva12`
### 🎓 Formação e certificações (1)

- [ ] `A-decidir` **Decidir a ordem entre Economia e a faculdade para IA (regra: Economia primeiro se os sistemas precisarem dela)**
  - ✅ Pronto quando: Decisão anotada em formacao-academica.md
  - 🔗 Liga com: `E-f4`, `A-licenciatura`, `A-economia`, `A-ia`
### ⚖️ Decisões (1)

- [ ] `D-paralelas` **Confirmar a ordem das trilhas paralelas (Finanças → IA → 42 → Pentest)**
  - 🔗 Liga com: `E-f4`, `E-ia0`, `E-42`, `E-seguranca`

---

## Etapa 5 · Virar sênior e empresa
<a id="e5"></a>

**Quando:** 2028 · **Objetivo:** Produção, plataforma interna, dados e IA, CNPJ, sistemas à venda e certificações.

### 🛠️ Setup (26)


**Fase 21 do setup** — Dados, IA e pendrives

- [ ] `S-zoomcamp` **21.6** Fazer o Data Engineering Zoomcamp e os cursos de IA, um módulo por semana · _Você, ~60 min_
  - ✅ Pronto quando: Módulo 1 entregue no GitHub e anotado no Obsidian
  - 📝 Junto do IA2 da Trilha de Dados e IA (depois do Passo 8 e das Finanças F4–F5). O tempo é só para começar; o curso leva 10 semanas. Para a IA vão as suas anotações, nunca o material do curso.
  - 🔗 Liga com: `S-ollama-8b`, `S-dbt-metricas`, `E-ia2`
- [ ] `S-dbt-metricas` **21.7** Criar o projeto dbt sobre o banco de métricas · _Claude com você, ~90 min_
  - ✅ Pronto quando: 'dbt build' verde e o painel de lucro lendo os modelos
  - 📝 Junto do IA2 da Trilha de Dados e IA (depois do Passo 8 e das Finanças F4–F5).
  - 🔗 Liga com: `S-zoomcamp`, `S-airflow`, `E-ia2`
- [ ] `S-airflow` **21.8** Subir o Airflow e agendar o dbt todo dia · _Claude com você, ~90 min_
  - ✅ Pronto quando: A rotina diária aparece verde no Airflow por 3 dias seguidos
  - 📝 Junto do IA2 da Trilha de Dados e IA (depois do Passo 8 e das Finanças F4–F5).
  - 🔗 Liga com: `S-dbt-metricas`, `S-contas-ia`, `E-ia2`
- [ ] `S-contas-ia` **21.9** Criar as contas do Hugging Face e do Kaggle (e do RunPod, só se precisar) · _Você, ~30 min_
  - ✅ Pronto quando: Token do Hugging Face no KeePassXC; Kaggle com telefone verificado para liberar a GPU
  - 📝 Junto do IA2 da Trilha de Dados e IA (depois do Passo 8 e das Finanças F4–F5). No RunPod, só crédito pré-pago. Nunca ponha token em notebook público.
  - 🔗 Liga com: `S-airflow`, `S-dataset`

**Fase 25 do setup** — IA dentro dos sistemas AM

- [ ] `S-rag-sistema` **25.1** RAG com pgvector dentro do primeiro sistema AM · _Claude com você, ~480 min_
  - ✅ Pronto quando: O sistema responde perguntas com base nos dados do cliente, citando a origem
  - 🔗 Liga com: `S-mic-camera`, `S-saas`, `E-ia5`

**Fase 26 do setup** — Sistemas AM à venda · ⏸ gatilho: O primeiro sistema AM pronto e testado com um cliente

- [ ] `S-saas` **26.1** Lançar o primeiro sistema AM como SaaS, com cobrança por módulo · _Claude com você, ~600 min_
  - ✅ Pronto quando: Primeiro cliente pagando por assinatura
  - 🔗 Liga com: `S-rag-sistema`, `S-kaixara`, `E-P12`
- [ ] `S-kaixara` **26.2** AM Kaixara: PDV, cardápio, fichas técnicas e estoque · _Claude com você, ~2400 min_
  - ✅ Pronto quando: Rodando num negócio real
  - 🔗 Liga com: `S-saas`, `S-rotara`, `E-P7`, `R-kaixara`
- [ ] `S-rotara` **26.3** AM Rotara: pedidos, rotas e mapas · _Claude com você, ~2400 min_
  - ✅ Pronto quando: Entregas rastreadas no mapa em tempo real
  - 🔗 Liga com: `S-kaixara`, `S-servicos-aura`, `E-P13`, `R-rotara`
- [ ] `S-servicos-aura` **26.4** Serviços aura- compartilhados, só quando um sistema precisar · _Claude com você, ~600 min_
  - ✅ Pronto quando: Um serviço compartilhado usado por dois sistemas
  - 🔗 Liga com: `S-rotara`, `S-whitelabel`, `E-P14`
- [ ] `S-whitelabel` **26.5** App de delivery com a marca do restaurante (white-label) · _Claude com você, ~1200 min_
  - ✅ Pronto quando: Primeiro restaurante usando o app com a marca dele
  - 📝 Comece oferecendo a 3 restaurantes que pagam 23% ao iFood.
  - 🔗 Liga com: `S-servicos-aura`, `S-cnpj`, `R-whitelabel`

**Fase 28 do setup** — Agentes do grupo · ⏸ gatilho: Clientes e vendas recorrentes

- [ ] `S-ag-analista` **28.1** Analista semanal: o que funcionou e o que mudar · _Claude com você, ~120 min_
  - ✅ Pronto quando: Relatório toda segunda no Telegram
  - 🔗 Liga com: `S-pix-automatico`, `S-ag-atendente`
- [ ] `S-ag-atendente` **28.2** Atendente do WhatsApp com passagem para você · _Claude com você, ~240 min_
  - ✅ Pronto quando: Dúvida comum respondida sozinha; o resto chega para você
  - 🔗 Liga com: `S-ag-analista`, `S-ag-orcamento`
- [ ] `S-ag-orcamento` **28.3** Orçamentista de sites e sistemas · _Claude com você, ~180 min_
  - ✅ Pronto quando: Rascunho de orçamento em 5 minutos, revisado por você
  - 🔗 Liga com: `S-ag-atendente`, `S-ag-cobranca`
- [ ] `S-ag-cobranca` **28.4** Cobrador educado (lembrete antes e depois do vencimento) · _Claude com você, ~120 min_
  - ✅ Pronto quando: Atraso cai pela metade
  - 🔗 Liga com: `S-ag-orcamento`, `S-ag-posvenda`
- [ ] `S-ag-posvenda` **28.5** Pós-venda: NPS e pedido de avaliação · _Claude com você, ~120 min_
  - ✅ Pronto quando: NPS medido em cada venda
  - 🔗 Liga com: `S-ag-cobranca`, `S-ag-fiscal`
- [ ] `S-ag-fiscal` **28.6** Organizador fiscal para o contador · _Claude com você, ~120 min_
  - ✅ Pronto quando: Pasta do mês pronta no dia 5
  - 🔗 Liga com: `S-ag-posvenda`, `S-ag-comprador`
- [ ] `S-ag-comprador` **28.7** Comprador com estoque mínimo · _Claude com você, ~180 min_
  - ✅ Pronto quando: Pedido de reposição sugerido antes de faltar
  - 🔗 Liga com: `S-ag-fiscal`, `S-grafica`

**Fase 30 do setup** — Distribuído, plataforma e segunda nuvem

- [ ] `S-mensageria` **30.1** RabbitMQ e depois Kafka entre dois sistemas AM · _Claude com você, ~600 min_
  - ✅ Pronto quando: Evento de um sistema chega no outro sem chamada direta
  - 🔗 Liga com: `S-traducoes`, `S-kubernetes`
- [ ] `S-kubernetes` **30.2** Kubernetes local com kind, kubectl, Helm e k9s · _Você, ~600 min_
  - ✅ Pronto quando: Um sistema AM rodando no cluster local
  - 🔗 Liga com: `S-mensageria`, `S-loki-tempo`
- [ ] `S-loki-tempo` **30.3** Logs e rastreamento com Loki e Tempo no Grafana · _Claude com você, ~240 min_
  - ✅ Pronto quando: Uma requisição seguida de ponta a ponta
  - 🔗 Liga com: `S-kubernetes`, `S-aws`
- [ ] `S-aws` **30.4** AWS: Cloud Practitioner e o mesmo sistema rodando lá · _Você, ~1200 min_
  - ✅ Pronto quando: Certificação e post comparando Azure e AWS
  - 🔗 Liga com: `S-loki-tempo`, `S-gcp`
- [ ] `S-gcp` **30.5** Google Cloud só o básico, quando um projeto de IA ou dados pedir · _Você, ~300 min_
  - ✅ Pronto quando: Um serviço usado num projeto real
  - 🔗 Liga com: `S-aws`, `S-mobile`
- [ ] `S-mobile` **30.6** App mobile dos sistemas AM com .NET MAUI · _Claude com você, ~1200 min_
  - ✅ Pronto quando: App publicado para teste interno
  - 🔗 Liga com: `S-gcp`, `S-nas`

**Fase 31 do setup** — Infraestrutura própria

- [ ] `S-nas` **31.1** Servidor caseiro com backup local e os serviços 24 horas · _Você, ~480 min_
  - ✅ Pronto quando: n8n, banco e painel rodando no servidor; notebook livre
  - 🔗 Liga com: `S-mobile`, `S-tailscale`
- [ ] `S-tailscale` **31.2** Tailscale entre notebook, celular e servidor · _Você, ~60 min_
  - ✅ Pronto quando: Acesso ao servidor de fora de casa sem abrir porta
  - 🔗 Liga com: `S-nas`, `S-workstation`
- [ ] `S-workstation` **31.3** Workstation com GPU para treinar e gerar voz e vídeo em casa · _Você, ~480 min_
  - ✅ Pronto quando: Fine-tuning de 8B rodando local
  - 🔗 Liga com: `S-tailscale`, `S-planejador-real`
### 📚 Estudo (13)

- [ ] `E-P9` **Passo 9 — Ponte técnica pro próximo sistema**
  - ✅ Pronto quando: dashboard atualiza em tempo real sem refresh.
  - 🕒 após MVP do AM Kaixara
  - 🔗 Liga com: `E-P8`, `S-observabilidade-dev`, `E-P10`
- [ ] `E-P10` **Passo 10 — Produção real**
  - ✅ Pronto quando: sistema no ar, observável, deploy automático a cada push.
  - 🕒 2-3 semanas
  - 🔗 Liga com: `E-P9`, `S-nuvem-clis`, `S-azure-conta`, `S-terraform-base`, `S-arquivos-nuvem`, `S-email-transacional`, `S-deploy-teste`, `S-aura-status`, `E-P11`
- [ ] `E-P11` **Passo 11 — Performance com dado real**
  - ✅ Pronto quando: tem "antes e depois" medido de uma otimização real.
  - 🕒 após meses em produção
  - 🔗 Liga com: `E-P10`, `E-P12`
- [ ] `E-P12` **Passo 12 — Extração da plataforma interna**
  - ✅ Pronto quando: gera a estrutura de um sistema novo com um comando, autenticado, com tema, sem escrever do zero.
  - 🕒 2-3 semanas — ponto de virada do cronograma
  - 🔗 Liga com: `E-P11`, `S-template-aura`, `S-saas`, `E-P13`, `E-espanhol`
- [ ] `E-robotica-r3` **Robótica R3: Raspberry Pi e Linux embarcado**
  - ✅ Pronto quando: Central da casa inteligente rodando
  - 🔗 Liga com: `E-linux`
- [ ] `E-f5` **Finanças F5: mercado financeiro, regulação (CVM 19/20/21), Pix e Open Finance**
  - ✅ Pronto quando: Cada tela do Rendara classificada como informação, educação ou recomendação
  - 🔗 Liga com: `C-cpa`
- [ ] `E-f6` **Finanças F6: economia aplicada, indicadores e econometria em Python**
  - ✅ Pronto quando: Painel de indicadores atualizando sozinho pelas APIs do BCB e IBGE
  - 🔗 Liga com: `A-economia`, `E-ia2`
- [ ] `E-ia0` **IA0: Python para IA e FastAPI (aura-analytics)**
  - ✅ Pronto quando: Endpoint FastAPI testado com pytest
  - 🔗 Liga com: `E-py`, `S-lab-ia`, `E-P8`, `D-paralelas`
- [ ] `E-ia1` **IA1: matemática para IA (álgebra linear, cálculo, probabilidade)**
  - ✅ Pronto quando: Gradiente e regressão feitos à mão
  - 🔗 Liga com: `E-matematica`
- [ ] `E-ia2` **IA2: dados e engenharia de dados**
  - ✅ Pronto quando: Pipeline BCB/IBGE gravando no PostgreSQL
  - 🔗 Liga com: `S-zoomcamp`, `S-dbt-metricas`, `S-airflow`, `E-f6`
- [ ] `E-ia3` **IA3: machine learning clássico**
  - ✅ Pronto quando: Previsão de fluxo de caixa do Rendara melhor que a média simples
  - 🔗 Liga com: `R-rendara`, `E-ia4`
- [ ] `E-ia5` **IA5: LLMs aplicados (RAG, function calling, avaliação)**
  - ✅ Pronto quando: Tutor do AM Mentor respondendo com citação do capítulo
  - 🔗 Liga com: `S-rag-sistema`, `R-ammentor`
- [ ] `E-espanhol` **Espanhol (começa no Passo 12)**
  - ✅ Pronto quando: B1–B2
  - 🔗 Liga com: `E-P12`, `E-mandarim`
### 💰 Renda (3)

- [ ] `R-whitelabel` **App de delivery com a marca do restaurante (white-label) — Oferecer a 3 restaurantes que pagam 23% ao iFood** · ⭐ 14 pts
  - ✅ Pronto quando: Métrica: lojas ativas
  - 🕒 passo 26.5 · 2027
  - 🔗 Liga com: `S-whitelabel`
- [ ] `R-kaixara` **AM Kaixara (PDV, ficha técnica, cardápio) — Rodar primeiro num cliente piloto pagante** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: MRR e cancelamento
  - 🕒 passo 26.2 · 2027
  - 🔗 Liga com: `S-kaixara`, `E-P7`
- [ ] `R-rotara` **AM Rotara (pedidos e entregas) — Nasce junto com a AM Entregas** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: entregas roteirizadas
  - 🕒 passo 26.3 · 2027
  - 🔗 Liga com: `S-rotara`, `E-P13`
### 🏦 Finanças pessoais (1)

- [ ] `F-sairrest` **Sair do restaurante: manutenção de sites acima de R$ 2.200 por 3 meses + reserva de 3 meses**
  - ✅ Pronto quando: Gatilho cumprido
  - 🔗 Liga com: `R-sites7`
### 🎓 Formação e certificações (4)

- [ ] `A-economia` **Ciências Econômicas (bacharelado EAD, MEC 4 ou 5)**
  - ✅ Pronto quando: Matrícula feita; depois, diploma
  - 🔗 Liga com: `A-decidir`, `E-f6`, `E-f8`
- [ ] `C-cpa` **Certificação CPA (ANBIMA)**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `E-f5`, `C-cnpi`
- [ ] `C-cnpi` **Certificação CNPI (APIMEC) — consultor e relatórios de análise**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `C-cpa`, `R-consultoria`
- [ ] `C-comptia` **CompTIA A+ e Network+**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `E-redes`, `C-security`

---

## Etapa 6 · Especialização e expansão
<a id="e6"></a>

**Quando:** 2029 em diante · **Objetivo:** Segundo e terceiro sistemas, fase sênior, 42, segurança, IA do zero, fundos e negócios físicos.

### 🛠️ Setup (16)


**Fase 21 do setup** — Dados, IA e pendrives

- [ ] `S-dataset` **21.10** Montar o primeiro dataset só com conteúdo seu · _Claude com você, ~120 min_
  - ✅ Pronto quando: Algumas centenas de pares de pergunta e resposta revisados por você, com conjunto de teste separado
  - 📝 Junto do IA6 da Trilha de Dados e IA (treino e fine-tuning). Fontes: suas notas, exercícios, livro e aulas que você gravou. Nada de cursos de terceiros; nada de dados de alunos sem consentimento.
  - 🔗 Liga com: `S-contas-ia`, `S-fine-tune`, `E-ia6`
- [ ] `S-fine-tune` **21.11** Primeiro fine-tuning QLoRA de um 8B no Kaggle · _Claude com você, ~180 min_
  - ✅ Pronto quando: Adaptador salvo no Hugging Face privado e o treino registrado no MLflow
  - 📝 Junto do IA6 da Trilha de Dados e IA (treino e fine-tuning).
  - 🔗 Liga com: `S-dataset`, `S-modelo-no-ollama`, `E-ia6`
- [ ] `S-modelo-no-ollama` **21.12** Avaliar contra o modelo base e levar o seu modelo para o Ollama · _Claude com você, ~90 min_
  - ✅ Pronto quando: O seu modelo ganha do base no conjunto de teste e responde no Ollama do notebook
  - 📝 Junto do IA6 da Trilha de Dados e IA (treino e fine-tuning).
  - 🔗 Liga com: `S-fine-tune`, `S-of-meu-setup`, `E-ia6`

**Fase 29 do setup** — Editora: depois do primeiro livro · ⏸ gatilho: O primeiro livro publicado

- [ ] `S-grafica` **29.1** Gráfica sob demanda no Brasil · _Você, ~120 min_
  - ✅ Pronto quando: Cópia de prova aprovada
  - 🔗 Liga com: `S-ag-comprador`, `S-kit-especial`
- [ ] `S-kit-especial` **29.2** Kit edição especial · _Você, ~240 min_
  - ✅ Pronto quando: Primeira tiragem vendida
  - 🔗 Liga com: `S-grafica`, `S-curso-secao`, `R-kitlivro`
- [ ] `S-curso-secao` **29.3** Curso por seção do livro, com animações · _Você, ~1200 min_
  - ✅ Pronto quando: Primeira seção gravada e à venda
  - 🔗 Liga com: `S-kit-especial`, `S-edicao-professor`
- [ ] `S-edicao-professor` **29.4** Edição do professor com licença para escolas · _Claude com você, ~600 min_
  - ✅ Pronto quando: Primeira escola licenciada
  - 🔗 Liga com: `S-curso-secao`, `S-traducoes`, `R-adocao`
- [ ] `S-traducoes` **29.5** Traduções para espanhol e inglês · _Claude com você, ~1200 min_
  - ✅ Pronto quando: Primeiro volume traduzido e revisado
  - 🔗 Liga com: `S-edicao-professor`, `S-mensageria`, `R-traducao`

**Fase 32 do setup** — Negócios do grupo em Barbacena · ⏸ gatilho: Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta

- [ ] `S-planejador-real` **32.1** Planejador do grupo com os números reais · _Claude com você, ~120 min_
  - ✅ Pronto quando: Capital mínimo e portões calculados com os seus dados
  - 🔗 Liga com: `S-workstation`, `S-neg-a1`
- [ ] `S-neg-a1` **32.2** A1 · AMtech Software · _Você, ~2400 min_
  - ✅ Pronto quando: 3 meses seguidos com lucro e 10 clientes pagantes
  - 🔗 Liga com: `S-planejador-real`, `S-neg-a2`
- [ ] `S-neg-a2` **32.3** A2 · Loja AMtech, peças sob encomenda, ponto de retirada e Maker · _Você, ~4800 min_
  - ✅ Pronto quando: Loja acima do equilíbrio por 3 meses e técnico que abre e fecha sem você
  - 🔗 Liga com: `S-neg-a1`, `S-neg-b1`, `R-assist`, `R-maker`, `R-pecas`, `R-ponto`
- [ ] `S-neg-b1` **32.4** B1 · AM Entregas e Mercado Envios Flex · _Você, ~4800 min_
  - ✅ Pronto quando: 1.000 entregas por mês e 5 contratos fixos
  - 🔗 Liga com: `S-neg-a2`, `S-neg-b2`, `R-entregas`
- [ ] `S-neg-b2` **32.5** B2 · AM Delivery · _Você, ~4800 min_
  - ✅ Pronto quando: 20 lojistas ativos e 1.500 pedidos por mês
  - 🔗 Liga com: `S-neg-b1`, `S-neg-c1`, `R-licencadelivery`, `R-delivery`
- [ ] `S-neg-c1` **32.6** C1 · Sushi, delivery primeiro · _Você, ~4800 min_
  - ✅ Pronto quando: Lucro por 3 meses e sushiman que toca a noite sem você
  - 🔗 Liga com: `S-neg-b2`, `S-neg-c2`, `R-sushi`, `R-congelados`
- [ ] `S-neg-c2` **32.7** C2 · Padaria com café da manhã e almoço · _Você, ~4800 min_
  - ✅ Pronto quando: Gerente no comando e CMV dentro da meta por 3 meses
  - 🔗 Liga com: `S-neg-c1`, `S-neg-c3`, `R-padaria`
- [ ] `S-neg-c3` **32.8** C3 · Cafeteria · _Você, ~2400 min_
  - ✅ Pronto quando: Cafeteria acima do equilíbrio
  - 🔗 Liga com: `S-neg-c2`, `S-github-education`, `R-cafeteria`
### 📚 Estudo (12)

- [ ] `E-P13` **Passo 13 — Segundo sistema: AM Rotara**
  - ✅ Pronto quando: segundo sistema em produção — meça quanto tempo real foi economizado vs. o primeiro.
  - 🕒 bem mais rápido que o primeiro
  - 🔗 Liga com: `E-P12`, `S-rotara`, `R-rotara`, `E-P14`
- [ ] `E-P14` **Passo 14 — Terceiro sistema e além**
  - 🔗 Liga com: `E-P13`, `R-rendara`, `S-servicos-aura`, `E-senior`, `D-clojure`
- [ ] `E-robotica-r45` **Robótica R4–R5: robôs e produto vendável (com homologação Anatel se tiver rádio)**
  - ✅ Pronto quando: Primeiro produto pronto para vender
  - 🔗 Liga com: `R-maker`
- [ ] `E-f8` **Finanças F8: finanças quantitativas**
  - ✅ Pronto quando: Backtest de uma estratégia com risco medido
  - 🔗 Liga com: `A-economia`
- [ ] `E-ia4` **IA4: deep learning do zero (autograd sem biblioteca, depois PyTorch)**
  - ✅ Pronto quando: Rede treinada com o seu próprio autograd
  - 🔗 Liga com: `E-ia3`
- [ ] `E-ia6` **IA6: tokenizer e transformer do zero; modelo pequeno pré-treinado; fine-tuning de 8B**
  - ✅ Pronto quando: Modelo próprio comparado contra o modelo base
  - 🔗 Liga com: `S-dataset`, `S-fine-tune`, `S-modelo-no-ollama`, `E-ia7`
- [ ] `E-ia7` **IA7: MLOps (servir, versionar, monitorar)**
  - ✅ Pronto quando: Modelo atrás do aura-analytics com observabilidade
  - 🔗 Liga com: `E-ia6`
- [ ] `E-42` **École 42: Circles 00–06, na sua stack e depois em C/C++**
  - ✅ Pronto quando: 25 entregáveis e 5 Exam Ranks
  - 🔗 Liga com: `E-horizonte`, `D-paralelas`
- [ ] `E-seguranca` **Segurança ofensiva: laboratórios até eJPT e OSCP**
  - ✅ Pronto quando: Writeups publicados
  - 🔗 Liga com: `C-ejpt`, `C-oscp`, `S-pendrive-kali`, `D-paralelas`
- [ ] `E-senior` **Fase sênior: system design, SLO e postmortem, Kubernetes, entrevista em inglês**
  - ✅ Pronto quando: Passa num system design de 45 minutos em inglês
  - 🔗 Liga com: `E-P14`, `E-ingles`
- [ ] `E-horizonte` **Horizonte longo: Linux internals, reverse, kernel, AM-OS e AM Linux**
  - ✅ Pronto quando: Gatilhos do mapa de horizonte longo
  - 🔗 Liga com: `E-linux`, `E-42`
- [ ] `E-mandarim` **Mandarim (depois do espanhol)**
  - ✅ Pronto quando: —
  - 🔗 Liga com: `E-espanhol`
### 💰 Renda (17)

- [ ] `R-kitlivro` **Kit do livro e edição do professor — Depois do volume 1** · ⭐ 15 pts
  - ✅ Pronto quando: Métrica: adoções
  - 🕒 passo 29.2 · Depois do primeiro livro
  - 🔗 Liga com: `S-kit-especial`
- [ ] `R-adocao` **Adoção do livro por escolas — Piloto na sua própria escola, se permitido** · ⭐ 13 pts
  - ✅ Pronto quando: Métrica: escolas e alunos
  - 🕒 passo 29.4 · Depois do primeiro livro
  - 🔗 Liga com: `S-edicao-professor`
- [ ] `R-assist` **Assistência técnica — Começar atendendo em casa e por agendamento antes de alugar a loja** · ⭐ 12 pts
  - ✅ Pronto quando: Métrica: serviços por semana e retorno em garantia
  - 🕒 passo 32.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-a2`, `R-manutpc`
- [ ] `R-maker` **AMtech Maker (robótica e automação) — Primeiro kit sem rádio testado com seus alunos** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: kits vendidos
  - 🕒 passo 32.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-a2`, `E-robotica-r45`
- [ ] `R-licencadelivery` **Licença do AM Delivery para outras cidades — Só depois de Barbacena dar lucro por 6 meses** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: cidades licenciadas
  - 🕒 passo 32.5 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-b2`
- [ ] `R-pecas` **Peças e acessórios sem estoque — Só junto com a assistência** · ⭐ 11 pts
  - ✅ Pronto quando: Métrica: margem por pedido
  - 🕒 passo 32.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-a2`
- [ ] `R-ponto` **Ponto de retirada (Shopee e Mercado Livre) — Junto com a loja** · ⭐ 10 pts
  - ✅ Pronto quando: Métrica: conversão de retiradas em vendas
  - 🕒 passo 32.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-a2`
- [ ] `R-traducao` **Traduções do livro — Depois de 500 cópias em português** · ⭐ 8 pts
  - ✅ Pronto quando: Métrica: vendas fora do Brasil
  - 🕒 passo 29.5 · Depois do primeiro livro
  - 🔗 Liga com: `S-traducoes`
- [ ] `R-entregas` **AM Entregas — Fase B, depois do portão da loja** · ⭐ 6 pts
  - ✅ Pronto quando: Métrica: entregas por rota
  - 🕒 passo 32.4 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-b1`
- [ ] `R-delivery` **AM Delivery — Fase B2** · ⭐ 5 pts
  - ✅ Pronto quando: Métrica: pedidos por lojista
  - 🕒 passo 32.5 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-b2`
- [ ] `R-sushi` **Sushi (delivery) — Fase C1** · ⭐ 4 pts
  - ✅ Pronto quando: Métrica: pedidos por noite e CMV
  - 🕒 passo 32.6 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-c1`
- [ ] `R-cafeteria` **Cafeteria — Fase C3, dentro da padaria** · ⭐ 3 pts
  - ✅ Pronto quando: Métrica: ticket médio
  - 🕒 passo 32.8 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-c3`
- [ ] `R-padaria` **Padaria com café da manhã e almoço — Fase C2** · ⭐ 1 pts
  - ✅ Pronto quando: Métrica: CMV e perdas
  - 🕒 passo 32.7 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano
  - 🔗 Liga com: `S-neg-c2`
- [ ] `R-congelados` **Congelados (harumakis): só com licença sanitária e cozinha adequada**
  - ✅ Pronto quando: Licença e primeiro lote vendido
  - 🔗 Liga com: `S-neg-c1`
- [ ] `R-consultoria` **Consultoria de investimentos do Rendara (com certificação e registro na CVM)**
  - ✅ Pronto quando: Primeiro cliente de consultoria
  - 🔗 Liga com: `C-cnpi`, `R-rendara`, `D-socia`
- [ ] `R-fundo` **Gestora e fundo próprio (gestora na CVM, diretor de compliance, administrador e custodiante)**
  - ✅ Pronto quando: Fundo registrado
  - 🔗 Liga com: `C-cga`, `C-cfa`
- [ ] `R-status` **aura-status como produto (dev solo e freelancer)**
  - ✅ Pronto quando: Primeira venda
  - 🔗 Liga com: `H-status`
### 🏦 Finanças pessoais (2)

- [ ] `F-reserva12` **Reserva de 12 meses**
  - ✅ Pronto quando: Valor guardado
  - 🔗 Liga com: `F-reserva6`, `F-apto`
- [ ] `F-apto` **Financiar o apartamento (entrada, parcela até 30% da renda)**
  - ✅ Pronto quando: Financiamento aprovado
  - 🔗 Liga com: `F-reserva12`, `F-f2`
### 🎓 Formação e certificações (6)

- [ ] `A-ia` **Faculdade para IA: Ciência da Computação EAD ou bacharelado presencial em IA (UFU, UFG, UFMS)**
  - ✅ Pronto quando: Matrícula feita
  - 🔗 Liga com: `A-decidir`
- [ ] `C-cga` **Certificação CGA (ANBIMA) — gestor de carteiras e fundos**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `R-fundo`
- [ ] `C-cfa` **CFA (3 níveis, em inglês) — exterior e gestão**
  - ✅ Pronto quando: Nível III
  - 🔗 Liga com: `E-ingles`, `R-fundo`
- [ ] `C-security` **CompTIA Security+ (CCNA opcional)**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `C-comptia`
- [ ] `C-ejpt` **eJPT**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `E-seguranca`, `C-oscp`
- [ ] `C-oscp` **OSCP**
  - ✅ Pronto quando: Aprovado
  - 🔗 Liga com: `C-ejpt`, `E-seguranca`
### ⚖️ Decisões (1)

- [ ] `D-clojure` **aura-historico: Clojure/Datomic ou Event Sourcing com Marten em .NET**
  - 🔗 Liga com: `E-P14`

---

## Sempre · Hábitos e rotinas
<a id="ec"></a>

**Quando:** contínuo · **Objetivo:** O que roda toda semana, do início ao fim.

### 🛠️ Setup (8)


**Fase 33 do setup** — Estudo contínuo

- [ ] `S-github-education` **33.1** Pedir o GitHub Education como professor e ligar o Copilot · _Você, ~20 min_
  - ✅ Pronto quando: Benefícios aprovados e Copilot ativo no VS Code
  - 🔗 Liga com: `S-neg-c3`, `S-trilhas`
- [ ] `S-trilhas` **33.2** Montar as trilhas: Microsoft Learn, AWS Skill Builder, roadmap.sh e laboratórios do TryHackMe · _Você, ~30 min_
  - ✅ Pronto quando: Uma trilha de cada em andamento, anotada no Obsidian
  - 🔗 Liga com: `S-github-education`, `S-plataformas-aluno`
- [ ] `S-plataformas-aluno` **33.3** Organizar as contas de aluno (Alura, Rocketseat, DIO, Udemy) · _Você, ~15 min_
  - ✅ Pronto quando: Acessos no KeePassXC e cursos em andamento listados no Obsidian
  - 📝 A licença é para assistir e estudar. Para a IA vão só as suas anotações e os seus projetos.
  - 🔗 Liga com: `S-trilhas`, `S-anki`
- [ ] `S-anki` **33.4** Criar os baralhos do Anki (comandos, conceitos, certificações) · _Você, ~20 min_
  - ✅ Pronto quando: Revisão do dia feita no notebook e no celular
  - 🔗 Liga com: `S-plataformas-aluno`, `H-anki`
- [ ] `H-ensina` **Estuda → ensina → grava: cada tópico vira aula paga e conteúdo**
  - 🔗 Liga com: `R-aulas`, `S-ativar-pipeline`
- [ ] `H-status` **aura-status toda segunda-feira**
  - 🔗 Liga com: `R-status`
- [ ] `H-posts` **3 posts por semana tirados das aulas**
  - 🔗 Liga com: `S-perfis`
- [ ] `H-senhas` **5 contas por semana no cofre até dez/2026; revisão do cofre a cada 3 meses**
  - 🔗 Liga com: `S-senhas-resto`, `S-senhas-revisao`
### 📚 Estudo (5)

- [ ] `E-ingles` **Inglês: Fase A → B → C (meta C1, essencial para o exterior)**
  - ✅ Pronto quando: Conversa técnica fluente e entrevista em inglês
  - 🔗 Liga com: `E-senior`, `C-cfa`
- [ ] `E-matematica` **Matemática pelo livro do VHSlins, integrada aos Passos**
  - ✅ Pronto quando: Capítulo do Passo atual resolvido
  - 🔗 Liga com: `E-fisica`, `E-ia1`, `A-licenciatura`
- [ ] `H-anki` **Anki todo dia, 10–20 min**
  - 🔗 Liga com: `S-anki`
- [ ] `H-fimbloco` **Protocolo de fim de bloco a cada sessão de estudo**
  - 🔗 Liga com: `E-P1`
- [ ] `H-akita` **1 conteúdo do Fábio Akita por semana**
  - 🔗 Liga com: `E-P1`
### 🏦 Finanças pessoais (1)

- [ ] `H-caixa` **Revisão mensal do Caixa da Casa**
  - 🔗 Liga com: `F-gastos`
### 🎓 Formação e certificações (1)

- [ ] `A-licenciatura` **Licenciatura em Matemática (em curso)**
  - ✅ Pronto quando: Diploma
  - 🔗 Liga com: `E-matematica`, `A-decidir`

---

## Onde está cada coisa

- Setup completo explicado: [[setup-completo-dev-setup]] · tudo do dev-setup (documentos, fluxogramas, roteiro, páginas e scripts): [índice do setup](11-setup-dev-setup/00-INDICE-DO-SETUP.md) · roteiro passo a passo: [roteiro de implantação](11-setup-dev-setup/docs/implantacao/roteiro.md)
- Estudo detalhado: [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] · currículo sênior: [[curriculo-dev-senior-completo]]
- Rendas: [[fontes-de-renda-completas]] · faculdade e certificações: [[formacao-academica]]
- Palavras difíceis: [[00-GLOSSARIO]] · versão curta: [[00-GUIA-DO-INICIANTE]]

_Gerado em 2026-10-26 a partir de `plano-mestre.json` (dados do dev-setup + vault). Ordem verificada: nenhum pré-requisito cai numa etapa posterior (0 problemas)._
