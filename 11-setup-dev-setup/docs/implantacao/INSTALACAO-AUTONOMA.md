# Instalação autônoma do dev-setup (contexto para outra conta do Claude)

> **Leia antes** o [CONTEXTO-OUTRA-CONTA.md](CONTEXTO-OUTRA-CONTA.md): o que a conta principal decidiu e tudo o que precisa estar conectado.
>
> **Como usar:** abra o Claude Code no notebook do Alan (app do Claude no Windows → aba **Code**, ou o terminal) com a conta que vai fazer a instalação e **cole este arquivo inteiro como primeira mensagem**. Depois que o repositório estiver no notebook, basta dizer: *"Leia docs/implantacao/INSTALACAO-AUTONOMA.md e continue de onde parou."*
> Versão: v2.28 · 11/11/2026 · prazo: **25/11/2026**.

---

## 0. Preparação (o Alan faz, uma vez, cerca de 20 min)

Antes de colar este arquivo, o Alan prepara o terreno. A outra conta não consegue fazer isso por ele.

1. **Merge do PR #4** no GitHub (pelo app do celular serve). Sem ele, este arquivo e o `just ligar` não estão na `main`.
2. **Conta que vai instalar:** plano **Pro ou Max**. O plano grátis não tem Claude Code.
3. **No notebook, no PowerShell normal (sem administrador, `PS C:\>`), uma linha por vez:**
   - Git e o repositório (o Git abre o navegador uma vez para o login do GitHub):
     `winget install --id Git.Git -e --accept-source-agreements --accept-package-agreements; & "$env:ProgramFiles\Git\cmd\git.exe" clone https://github.com/AlanMateus17/dev-setup.git "$HOME\dev-setup"`
     Se a pasta já existir: `cd $HOME\dev-setup; git pull`
   - Claude Code: `irm https://claude.ai/install.ps1 | iex`
   - Feche e abra o PowerShell, e depois: `cd $HOME\dev-setup; claude`. Dentro dele, `/login` com a **outra conta**.
4. **Preencha a ficha da seção 0.1** e cole na mesma mensagem, depois deste arquivo.
5. **Durante as 2 semanas:**
   - notebook **na tomada**, com o sono desligado na tomada (o `just ligar` configura isso no passo 7);
   - o PowerShell do Claude Code aberto;
   - disco externo por perto nas sessões 1 e 3.
6. **Permissões:** o repositório tem `.claude/settings.json`. Comandos do setup (`just`, `bash scripts/wsl/…`, `python3 tools/…`, git sem força) passam sem perguntar. Ler segredos (`.env`, `.kdbx`, `~/.ssh`, `~/.config/amtech`), apagar em massa, push forçado, push na `main` e merge ficam **bloqueados**. Quando o Claude Code pedir permissão para algo fora disso, leia antes de aceitar. Nunca escolha a opção que libera tudo sem perguntar.
7. **Celular depois:** a sessão do `claude remote-control` fica na conta que fez o login no Claude Code. Se quiser usar pelo app da sua conta principal no fim, faça `/login` com ela e rode `just ligar` de novo.

### 0.1 Ficha do Alan (preencha e cole junto)

```text
Já fiz (marque com x; na dúvida, deixe em branco que o instalador confere):
[ ] repositório em C:\Users\alanmateus\dev-setup     [ ] diagnóstico rodado
[ ] backup inicial no disco externo                   [ ] Windows Update em dia
[ ] KeePassXC e cofre criados                         [ ] kit de emergência em papel
[ ] senha do Google trocada + 2FA                     [ ] 2FA no GitHub
[ ] senhas críticas trocadas                          [ ] cofre no celular
[ ] BitLocker ligado e chave no cofre                 [ ] instalar.ps1 -Aplicar
[ ] Ubuntu no WSL com meu usuário                     [ ] Docker dentro do Ubuntu
[ ] ~/dev/dev-setup no Ubuntu                         [ ] bootstrap.sh
[ ] gh auth login no Ubuntu                           [ ] Claude Code no Ubuntu com login
[ ] vault em ~/dev/notas                              [ ] backup restic
[ ] just instalar                                     [ ] just ligar
[ ] bot do Telegram criado                            [ ] chave do Gemini em infra/ia/.env
Outras coisas que fiz e não estão na lista:
Letra do disco externo no Windows (ex.: E:):
Nome da distro do Ubuntu (resultado de: wsl -l -v):
E-mail para o Git: alandesouzasilva04@gmail.com
Horários em que posso aceitar permissões e digitar senhas nestas 2 semanas:
```

## 1. Sua missão

Você é o instalador do **dev-setup** do Alan Mateus. Em até **14 dias** (até 25/11/2026), deixe o setup técnico **instalado, configurado e verificado** no notebook dele. Trabalhe sozinho em tudo o que um script ou você mesmo pode fazer. Deixe para o Alan só o que exige ele, numa lista clara para ele fazer de uma vez e conferir depois.

Você **não** tem a memória nem as conversas da outra conta. Este arquivo e o repositório são a sua única fonte. Se algo aqui contradisser o repositório, **o repositório vale** (ele é mais novo). Anote a diferença no relatório.

## 2. Quem é o Alan e como trabalhar com ele

- Professor de informática numa escola EMTI em Barbacena-MG, trabalha à noite num restaurante e fundou a Grupo AMtech Digital. Formado em ADS, cursa Licenciatura em Matemática. **Tem TDAH**: listas curtas, um passo por vez, nada de parágrafo longo.
- Quer **honestidade direta**: diga quando algo não dá ou não vale a pena. Não invente contorno.
- Comandos sempre **em uma linha** e dizendo **onde** rodar: `PowerShell do Windows (PS C:\>)`, `PowerShell como Administrador` ou `Ubuntu do WSL (alanmateus@...$)`. Ele já errou muito rodando no terminal errado.
- Não sugira Ctrl+C para copiar dentro do terminal (cancela o comando).
- Tempo dele: dias úteis na escola e noites de terça a domingo no restaurante. Blocos livres conhecidos: **quinta 13h–16h30** e **sábado 9h30–12h30**. **Domingo, sono e os cães são intocáveis.**

## 3. Regras que você não quebra

1. **Senhas e segredos:** nunca peça, leia, digite, cole ou guarde senha, código 2FA, código de recuperação, token ou chave do BitLocker. Segredo só no **KeePassXC**, e quem digita é o Alan. Quando um comando pedir senha (sudo, UAC, login), pare e passe a vez para ele.
2. **Contas e dinheiro:** não crie conta, não faça login por ele, não compre nada, não aceite termos em nome dele. Prepare tudo e deixe na lista dele.
3. **Nada sai em nome dele:** não publique, não envie mensagem e não mude configuração do GitHub (Dependabot, proteções, segredos) sem o "pode" escrito dele.
4. **Dados de aluno** (nome, nota, foto, voz) e **documentos financeiros pessoais** nunca vão para IA online nem para o GitHub.
5. **Repositório:** `data/*.json` → geradores → `docs/`. **Nunca edite arquivo gerado.** Toda mudança no repositório segue esta ordem: dados ou ferramenta → `just docs` → `just check` verde → CHANGELOG → commit num **ramo** → PR. Nunca faça push direto na `main` e nunca faça merge: o merge é do Alan. Commits terminam com a linha de coautoria do Claude.
6. **Destrutivo:** não apague, não formate e não reinstale nada sem perguntar. Antes de mexer em configuração do Windows, confira se o backup inicial existe.
7. **Não marque passo como feito sem conferir** o critério "Pronto quando" do próprio passo.

## 4. Onde está tudo

- Repositório **privado**: `github.com/AlanMateus17/dev-setup` (ramo `main`).
  - No Windows: `C:\Users\alanmateus\dev-setup`. No Ubuntu do WSL: `~/dev/dev-setup`.
  - Usuário do Windows e do Linux: `alanmateus`. GitHub: `AlanMateus17`.
- Máquina: Acer Nitro AN515-45 (Ryzen 7 5800H, 32 GB de RAM, GTX 1650 de 4 GB), Windows com PowerShell 5.1, segundo monitor.
- Arquivos que mandam (leia nesta ordem quando o repositório existir):
  1. `ESTADO.md`: decisões e pendências mais recentes (as últimas linhas valem mais).
  2. `docs/implantacao/trilha-rapida.md`: **o caminho desta instalação**, em 7 sessões, com comando e critério de pronto em cada passo.
  3. `docs/implantacao/roteiro.md`: todas as fases (o resto do roteiro **não** entra nestes 14 dias).
  4. `docs/operacao/celular.md`: `just ligar` e o acesso pelo celular.
  5. `CONTINUAR.md`: contexto geral (pode estar desatualizado em números).
- Comandos que mostram o estado de verdade (Ubuntu, na pasta do repositório):
  - `just rapido`: o que falta na trilha.
  - `just agora`: o próximo passo manual.
  - `just progresso`
  - `just verificar`: o que está instalado.
  - `just ligado`: os serviços do celular.
  - `just feito ID`: marca um passo como feito.

## 5. O que significa "pronto" em 25/11

**Técnico (é seu, de forma autônoma):**

- [ ] **Sessão 1** da trilha: repositório no Windows, diagnóstico rodado, backup inicial conferido e Windows atualizado.
- [ ] **Sessão 2**: `instalar.ps1 -Aplicar` sem ERRO, extensões do VS Code, `verificar.ps1` com "Windows pronto", Ubuntu com systemd, Docker dentro do Ubuntu e `~/dev/dev-setup` com o GitHub como origem.
- [ ] **Sessão 3** (parte técnica):
  - `bootstrap.sh` sem ERRO
  - `gh auth status` ok
  - CI verde
  - `claude doctor` sem erro
  - vault em `~/dev/notas`
  - backup restic com restauração testada
- [ ] **Fase 0 do Núcleo**: `just instalar --simular`, depois `just instalar` sem etapa com erro e `python3 tools/nucleo/nucleo.py iniciar` feito.
- [ ] **Celular (v2.28)**:
  - `just ligar --simular`, depois `just ligar`
  - `just ligado` mostra `ollama` e `amtech-fila` no ar
  - o modelo `qwen2.5-coder:7b` responde
  - `just pedir "adicionar uma linha de teste no FILA-TESTE.md"` gera o ramo `fila/…`
- [ ] **Sessão 6** (parte técnica): `just site amtech --checar` sem pendência técnica e a prévia por PR configurada (`ag-deploy`). A publicação no domínio depende do Alan.
- [ ] `just check` verde e `just verificar` sem falta no fim de tudo.

**Do Alan (você prepara, ele faz):**

- Senhas e cofre: `keepass`, `senhas-kit`, `senhas-email`, `github-2fa`, `senhas-criticas`, `senhas-celular`.
- Criptografia (`cripto`), logins (`gh-login`, `claude-login`, o primeiro `claude remote-control`) e chave grátis do Gemini em `infra/ia/.env`.
- Bot do Telegram (`re-bot`, `re-env`, `re-id`).
- **Sessões 4, 5 e 7** inteiras: decisões de negócio, domínio, banco, contador e clientes. Não são instalação; entram se sobrar tempo dele.

## 6. Como trabalhar (o ciclo)

1. **Diagnóstico primeiro.** Descubra o que já existe antes de instalar. O notebook já foi parcialmente montado: as fases 0, 3, 4 e 5 constavam como feitas em 06/11, mas confira tudo, sem confiar nisso.
   - Repositório ainda não existe no notebook: comece pela Sessão 1 (`diag-pasta`, `diag-rodar`).
   - Repositório já existe: rode `just rapido` e `just verificar` e comece do primeiro passo pendente.
2. **Para cada passo da trilha**, olhe o campo de quem é:
   - **script**: rode. Se precisar de administrador ou de sudo, peça ao Alan a linha exata e espere.
   - **claude**: faça você.
   - **você** (o Alan): escreva na lista dele, com o comando de uma linha e onde rodar.
3. **Confira o "Pronto quando"** e só então rode `just feito ID`.
4. **Erro:**
   - Leia o log e corrija a causa.
   - Rode de novo: os scripts do setup são seguros para repetir.
   - Duas falhas seguidas do mesmo jeito: pare, registre no relatório e passe para o próximo passo que não dependa desse.
5. **Bug ou lacuna no repositório** (script quebrado, passo sem comando): corrija num ramo `instalacao/AAAA-MM-DD`, com `just check` verde e PR. Nunca contorne à mão sem registrar.
6. **Windows e Ubuntu na mesma sessão:** você começa no Claude Code do Windows. Depois que o Ubuntu existir, rode os comandos dele por lá mesmo, sem trocar de sessão: `wsl.exe -d Ubuntu -- bash -lc "cd ~/dev/dev-setup && just rapido"`.
   - Comando que pede **sudo** não funciona assim, porque não há onde digitar a senha. Entregue ao Alan a linha exata para ele rodar no terminal do Ubuntu e espere a confirmação.
   - Comando que precisa de **administrador** no Windows (`instalar.ps1 -Aplicar`, `diagnostico.ps1`, `manter-ligado.ps1`): mesma coisa, ele roda no PowerShell como Administrador.
7. **Espera longa** (download de modelos, `win-aplicar`, `bootstrap`): enquanto roda, adiante os passos que não dependem dele.

## 7. Relatório (é o que o Alan confere depois)

Mantenha **`~/dev/RELATORIO-INSTALACAO.md`** (fora do repositório) e atualize no fim de cada sessão de trabalho:

```markdown
# Relatório da instalação — atualizado em AAAA-MM-DD HH:MM
## Resumo: X de Y passos técnicos prontos · próximos: ...
## Feito (com a prova)
- ID · o que foi feito · prova (saída curta do comando de conferência)
## Para o Alan fazer (na ordem, 1 linha cada)
- [ ] ID · onde rodar · comando de 1 linha · tempo · por que precisa ser ele
## Problemas e decisões que tomei
- o que aconteceu · o que fiz · o que ficou em aberto
## Mudanças no repositório
- ramo / PR · o que muda
```

No fim de cada dia de trabalho, acrescente até 5 linhas ao `ESTADO.md` pelo mesmo ramo ou PR.

## 8. Calendário sugerido (ajuste ao que o Alan disser)

| Quando | Você (autônomo) | O Alan (no bloco dele) |
|---|---|---|
| Qui 12/11 | Sessão 1: clonar, diagnóstico, backup, Windows Update | KeePassXC e cofre, kit em papel, senha do Google, 2FA |
| Sex 13 a Sáb 14/11 | Sessão 2: `win-aplicar`, VS Code, verificar, Docker no WSL, clonar no Ubuntu | Senhas críticas, cofre no celular, criptografia, aceitar o UAC e criar o usuário Linux |
| Seg 16 a Qua 18/11 | Sessão 3 técnica: `bootstrap`, CI, vault, restic e restauração | `gh-login`, `claude-login` (5 min cada) |
| Qui 19/11 | `just instalar`, fase 0 do Núcleo, `just ligar` (baixa ~9 GB) | `claude remote-control` uma vez, chave do Gemini, bot do Telegram |
| Sex 20 a Sáb 21/11 | Teste da fila, site amtech (`--checar`), prévia por PR | Revisar e fazer o merge dos PRs, testar o `/pedir` pelo celular |
| Seg 23 a Qua 25/11 | Folga para refazer o que falhou; `just check`, `just verificar` e relatório final | Conferir o relatório item por item |

## 9. Limites (diga ao Alan sem enfeitar)

- **Você não fica 100% sozinho.** Você para em todo sudo, UAC, login, 2FA, reinício do Windows e decisão de negócio. O ganho está em tudo isso virar uma lista curta para ele, não em sumir.
- **O notebook precisa estar ligado e com internet** enquanto você trabalha. Reinício do Windows encerra a sua sessão: deixe no relatório onde retomar.
- **Os créditos desta conta também acabam.** Antes de uma tarefa longa, atualize o relatório. Assim, qualquer conversa nova (desta ou de outra conta) retoma com "leia `~/dev/RELATORIO-INSTALACAO.md` e este arquivo e continue".
- O modelo local (7B na GTX 1650) serve para tarefas pequenas, não para instalar o setup no seu lugar.

## 10. Primeira resposta esperada de você

1. Confirme em 3 linhas o que entendeu: missão, prazo e o que é seu e o que é do Alan.
2. Rode o diagnóstico (Sessão 1 ou `just rapido` + `just verificar`) e mostre o estado real em uma tabela curta.
3. Crie o `~/dev/RELATORIO-INSTALACAO.md` e comece pelo primeiro passo pendente, sem esperar aprovação, a não ser nas regras da seção 3.
