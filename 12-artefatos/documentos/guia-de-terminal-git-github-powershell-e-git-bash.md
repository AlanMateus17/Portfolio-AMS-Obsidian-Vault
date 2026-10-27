# Guia de Terminal: Git, GitHub, PowerShell e Git Bash

Sep 28, 2026 · @Alan Mateus

## Como usar este guia

Os comandos do Git são idênticos no PowerShell e no Git Bash; o que muda entre os dois são os comandos de arquivos e pastas e algumas regras de escrita. Cada seção traz o comando, a função, como usar e quando usar.

| Terminal | O que é | Quando preferir |
| --- | --- | --- |
| PowerShell | Terminal nativo do Windows. O Windows 10 e 11 trazem o Windows PowerShell 5.1; o PowerShell 7 é instalado à parte | Automatizar tarefas do Windows e trabalhar com .NET |
| Git Bash | Terminal que vem com o Git para Windows e imita o terminal do Linux | Seguir tutoriais escritos para Linux e macOS, e usar comandos como `ls -la` e `rm -rf` |

**Diferenças que mais causam erro**

| Situação | PowerShell | Git Bash |
| --- | --- | --- |
| Rodar um comando só se o anterior deu certo | `;` executa sempre. `&&` só existe no PowerShell 7 | `comando1 && comando2` |
| Ler uma variável de ambiente | `$env:PATH` | `$PATH` |
| Continuar o comando na linha seguinte | Crase no fim da linha: `` ` `` | Barra invertida no fim da linha: `\` |
| Separador de pastas | `C:\Users\alan\dev` (aceita `/` também) | `/c/Users/alan/dev` |
| Apagar pasta com tudo dentro | `Remove-Item pasta -Recurse -Force` (`rm -rf` dá erro) | `rm -rf pasta` |

**Convenções deste guia:** `<nome>` é algo que você troca pelo seu valor, sem os sinais de menor e maior. Comandos marcados com **⚠** apagam ou reescrevem algo e pedem atenção antes de rodar.

## Navegação e arquivos

Antes de usar o Git, você precisa se mover entre pastas e criar, ler, copiar e apagar arquivos pelo terminal. No PowerShell, `ls`, `cd`, `cat`, `cp`, `mv` e `rm` funcionam como apelidos, mas as opções são as do PowerShell, e não as do Linux.

| Função | PowerShell | Git Bash | Quando usar |
| --- | --- | --- | --- |
| Mostrar em que pasta você está | `Get-Location` ou `pwd` | `pwd` | Sempre que estiver perdido, antes de rodar um comando do Git |
| Listar o conteúdo da pasta | `Get-ChildItem` ou `ls` | `ls -la` | Para ver arquivos, inclusive os ocultos |
| Listar incluindo ocultos | `Get-ChildItem -Force` | `ls -la` | Para ver a pasta `.git` e o arquivo `.gitignore` |
| Entrar numa pasta | `cd projetos\meu-site` | `cd projetos/meu-site` | Para chegar à pasta do projeto |
| Voltar uma pasta | `cd ..` | `cd ..` | Para subir um nível |
| Ir para a pasta do usuário | `cd ~` | `cd ~` | Para voltar ao ponto de partida |
| Criar pasta | `New-Item -ItemType Directory meu-projeto` ou `mkdir meu-projeto` | `mkdir -p meu-projeto/src` | Ao começar um projeto ou organizar pastas |
| Criar arquivo vazio | `New-Item README.md` | `touch README.md` | Para criar um arquivo antes de editá-lo |
| Ler um arquivo | `Get-Content README.md` ou `cat README.md` | `cat README.md` | Para conferir o conteúdo sem abrir o editor |
| Escrever texto num arquivo | `"texto" \| Out-File README.md -Encoding utf8` | `echo "texto" > README.md` | Para criar arquivos simples; `>>` acrescenta no fim em vez de substituir |
| Copiar | `Copy-Item origem.txt destino.txt` | `cp origem.txt destino.txt` | Para fazer uma cópia de trabalho |
| Mover ou renomear | `Move-Item velho.txt novo.txt` | `mv velho.txt novo.txt` | Num projeto versionado, prefira `git mv` (seção 5) |
| ⚠ Apagar arquivo | `Remove-Item arquivo.txt` | `rm arquivo.txt` | Não vai para a lixeira: apaga de vez |
| ⚠ Apagar pasta com tudo dentro | `Remove-Item pasta -Recurse -Force` | `rm -rf pasta` | Confira o caminho duas vezes antes de apertar Enter |
| Abrir a pasta no VS Code | `code .` | `code .` | Para editar o projeto inteiro |
| Abrir a pasta no Explorador | `explorer .` ou `start .` | `explorer .` | Para ver os arquivos na janela do Windows |
| Limpar a tela | `Clear-Host` ou `cls` | `clear` | Quando a tela estiver poluída |
| Ver comandos anteriores | Seta para cima, ou `Get-History` | Seta para cima, ou `history` | Para repetir um comando |
| Completar nomes | Tecla Tab | Tecla Tab | Sempre: evita erros de digitação em nomes de pastas e branches |
| Ajuda de um comando | `Get-Help Remove-Item` | `man ls` ou `ls --help` | Para ver as opções de um comando |

**No Windows, cuidado com a codificação.** No PowerShell 5.1, `>` grava em UTF-16, o que embaralha acentos em arquivos lidos pelo Git e pelo GitHub. Use `Out-File -Encoding utf8` para gravar texto em arquivos.

## Configuração inicial do Git e acesso ao GitHub

Estes comandos rodam uma vez por computador. Sem eles, os commits saem sem autor correto e o GitHub recusa o envio.

### Identidade e padrões

```bash
git --version
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
git config --list
```

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git --version` | Mostra a versão instalada | Para confirmar que o Git está instalado |
| `git config --global user.name` | Define o nome gravado em cada commit | Uma vez, logo após instalar |
| `git config --global user.email` | Define o e-mail do commit. Use o mesmo e-mail da conta do GitHub, ou o e-mail privado `...@users.noreply.github.com` que o GitHub oferece | Uma vez; é por ele que o GitHub liga o commit ao seu perfil |
| `git config --global init.defaultBranch main` | Faz todo repositório novo começar com a branch `main` | Uma vez; evita a antiga `master` |
| `git config --global core.editor "code --wait"` | Abre o VS Code quando o Git pede um texto (mensagem de commit, merge) | Se não quiser cair no editor Vim |
| `git config --list` | Mostra todas as configurações ativas | Para conferir o que está configurado |

**Fim de linha no Windows.** O Windows e o Linux marcam o fim de linha de formas diferentes. Se você usa só o Windows, mantenha o padrão do instalador (`core.autocrlf true`). Se alterna entre Windows e WSL no mesmo projeto, a forma mais segura é um arquivo `.gitattributes` na raiz do repositório com a linha `* text=auto eol=lf`.

### Opção 1: acesso por chave SSH

A chave SSH prova ao GitHub quem você é, sem digitar senha a cada envio.

```bash
ssh-keygen -t ed25519 -C "seu-email@exemplo.com"
```

Função: cria um par de chaves em `~/.ssh/`: `id_ed25519` (privada, nunca compartilhe) e `id_ed25519.pub` (pública, vai para o GitHub). Quando usar: uma vez por computador.

Para não digitar a senha da chave toda hora, carregue-a no agente SSH:

| PowerShell (como administrador, uma vez) | Git Bash |
| --- | --- |
| `Get-Service ssh-agent \| Set-Service -StartupType Automatic` | `eval "$(ssh-agent -s)"` |
| `Start-Service ssh-agent` | `ssh-add ~/.ssh/id_ed25519` |
| `ssh-add $env:USERPROFILE\.ssh\id_ed25519` |  |

Depois, copie a chave pública e cole no GitHub em **Settings → SSH and GPG keys → New SSH key**:

| PowerShell | Git Bash |
| --- | --- |
| `Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub \| Set-Clipboard` | `cat ~/.ssh/id_ed25519.pub \| clip` |

Para testar a conexão:

```bash
ssh -T git@github.com
```

A resposta esperada começa com "Hi seu-usuario!". Com SSH, os endereços dos repositórios têm o formato `git@github.com:usuario/repositorio.git`.

### Opção 2: GitHub CLI

O GitHub CLI (`gh`) é a ferramenta oficial do GitHub para o terminal. Além de autenticar, ele cria repositórios, Pull Requests e issues sem abrir o navegador.

```bash
gh auth login
gh auth status
```

| Comando | Função | Quando usar |
| --- | --- | --- |
| `gh auth login` | Faz login no GitHub pelo navegador e configura o Git para usar essa conta | Uma vez por computador |
| `gh auth status` | Mostra com qual conta você está conectado | Quando um envio for recusado por permissão |

No Windows, o `gh` é instalado com `winget install --id GitHub.cli`.

## Criar ou obter um projeto

Há três pontos de partida: transformar uma pasta sua em repositório, baixar um repositório que já existe no GitHub, ou criar tudo de uma vez com o GitHub CLI.

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git init` | Transforma a pasta atual em repositório Git, criando a pasta oculta `.git`, onde fica todo o histórico | Ao começar um projeto do zero no seu computador |
| `git clone <endereço>` | Baixa um repositório do GitHub com todo o histórico, já ligado ao original | Para trabalhar num projeto que já existe, seu ou de outra pessoa |
| `git clone <endereço> <pasta>` | O mesmo, com outro nome de pasta | Quando o nome original não serve |
| `gh repo create` | Cria o repositório no GitHub pelo terminal | Para não precisar abrir o site |
| `gh repo clone <usuario>/<repositorio>` | Clona usando o GitHub CLI, sem copiar o endereço completo | Atalho para o `git clone` |
| `gh repo fork <usuario>/<repositorio> --clone` | Cria uma cópia sua de um repositório de outra pessoa e a baixa | Para contribuir com um projeto em que você não tem permissão de escrita |

**Projeto novo, do computador para o GitHub:**

```bash
mkdir meu-projeto
cd meu-projeto
git init
gh repo create meu-projeto --private --source . --remote origin
```

O último comando cria o repositório no GitHub (privado; troque por `--public` se quiser), liga a pasta a ele com o nome `origin` e dispensa o `git remote add`.

**Projeto que já existe no GitHub:**

```bash
git clone git@github.com:AlanMateus17/ensino-ti.git
cd ensino-ti
```

**Evite repositório dentro de repositório.** Rodar `git init` numa pasta que já está dentro de outro repositório cria confusão no histórico dos dois. Antes do `git init`, rode `git status`: se ele responder que não é um repositório, pode seguir.

## O ciclo do dia a dia

Todo trabalho no Git passa por três lugares: a **pasta de trabalho** (os arquivos como estão agora), a **área de preparação** (o que vai entrar no próximo commit) e o **histórico** (os commits gravados). O ciclo é sempre: conferir, preparar, gravar.

1. `git status` — ver o que mudou.
2. `git add` — escolher o que entra no commit.
3. `git commit` — gravar no histórico com uma mensagem.
4. `git push` — enviar ao GitHub (seção 6).

### Conferir

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git status` | Mostra a branch atual, os arquivos alterados, os novos e os já preparados | Antes e depois de qualquer outro comando. É o comando mais usado |
| `git status -s` | O mesmo, em formato curto: `M` modificado, `A` adicionado, `??` não rastreado | Quando há muitos arquivos |
| `git diff` | Mostra, linha por linha, o que mudou e ainda **não** foi preparado | Para revisar o próprio trabalho antes do `add` |
| `git diff --staged` | Mostra o que **já** foi preparado e vai entrar no commit | Última conferência antes do `commit` |

### Preparar

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git add <arquivo>` | Coloca um arquivo específico na área de preparação | Quando só parte das mudanças deve entrar no commit |
| `git add .` | Prepara todas as mudanças da pasta atual para baixo | Quando tudo o que mudou pertence ao mesmo assunto. Rode `git status` antes para não levar lixo junto |
| `git add -p` | Mostra cada trecho alterado e pergunta se entra (`y`) ou não (`n`) | Quando um arquivo tem mudanças de assuntos diferentes, para dividi-las em commits separados |
| `git mv <velho> <novo>` | Renomeia ou move um arquivo já registrando a mudança no Git | Para renomear arquivos versionados |
| `git rm <arquivo>` | Apaga o arquivo e registra a remoção | Para remover arquivos versionados |

### Gravar

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git commit -m "mensagem"` | Grava no histórico tudo o que foi preparado, com a mensagem | Sempre que terminar uma mudança pequena e completa |
| `git commit` | Abre o editor para escrever uma mensagem longa: título na primeira linha, linha em branco, explicação abaixo | Quando a mudança precisa de explicação |

**Mensagens no padrão Conventional Commits:** `tipo: descrição curta no imperativo`.

```bash
git commit -m "feat: cria tela inicial do jogo"
git commit -m "fix: impede aposta com valor vazio"
git commit -m "docs: explica a instalação no README"
```

Os tipos mais usados são `feat` (funcionalidade nova), `fix` (correção), `docs` (documentação), `test` (testes), `refactor` (reorganização sem mudar o comportamento) e `chore` (manutenção).

### Ver o histórico

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git log` | Lista os commits com autor, data e mensagem | Para entender o que já foi feito |
| `git log --oneline` | Um commit por linha, com o código curto (hash) | Para ter uma visão rápida |
| `git log --oneline --graph --all` | Desenha as branches e os merges em forma de árvore | Para entender como as branches se ligam |
| `git show <hash>` | Mostra o que um commit específico mudou | Para investigar uma mudança |

Para sair das telas longas do `git log` e do `git diff`, aperte `q`.

**Regra de ouro:** commits pequenos e frequentes, cada um com um único assunto. Um commit que diz "várias mudanças" é difícil de revisar e impossível de desfazer com precisão.

## Repositório remoto: enviar e receber

O remoto é a cópia do repositório no GitHub, chamada por convenção de `origin`. Os commits ficam só no seu computador até você enviá-los com `git push`.

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git remote -v` | Mostra os remotos ligados ao repositório e seus endereços | Para conferir para onde o `push` vai |
| `git remote add origin <endereço>` | Liga o repositório local a um repositório do GitHub | Uma vez, em projeto criado com `git init` sem o `gh repo create` |
| `git remote set-url origin <endereço>` | Troca o endereço do remoto | Ao mudar de HTTPS para SSH, ou quando o repositório foi renomeado ou transferido |
| `git push -u origin main` | Envia a branch `main` e grava que ela acompanha a `main` do GitHub | Na primeira vez que envia uma branch |
| `git push` | Envia os commits novos da branch atual | Depois do primeiro envio com `-u`, sempre que quiser publicar commits |
| `git fetch` | Baixa as novidades do GitHub **sem** mexer nos seus arquivos | Para ver o que mudou antes de juntar |
| `git pull` | Baixa as novidades **e** junta na sua branch atual (`fetch` + `merge`) | Antes de começar a trabalhar, todo dia |
| `git pull --rebase` | Baixa e coloca os seus commits locais depois dos que vieram do GitHub, sem criar commit de merge | Para manter o histórico em linha reta quando você e colegas mexeram na mesma branch |
| `git fetch --prune` | Apaga da sua lista as branches que já foram apagadas no GitHub | Para limpar branches antigas depois de merges |

**Quando o `git push` é recusado** com a mensagem "rejected" ou "fetch first", o GitHub tem commits que você não tem. Rode `git pull` (ou `git pull --rebase`), resolva algum conflito se houver (seção 10) e rode `git push` de novo. **Nunca** resolva isso com `git push --force` numa branch compartilhada: ele apaga o trabalho dos colegas (seção 13).

**Rotina recomendada:**

```bash
git pull            # ao começar
# ... trabalhar, add, commit ...
git pull --rebase   # antes de enviar
git push            # ao terminar
```

## Branches e merge

Uma branch é uma linha de trabalho separada: você muda o que quiser nela sem afetar a `main`. O fluxo usado em equipe é: criar uma branch por tarefa, trabalhar nela, abrir um Pull Request e, depois de aprovado, juntar na branch principal.

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git branch` | Lista as branches locais; a atual aparece com `*` | Para saber onde você está |
| `git branch -a` | Lista também as branches do GitHub | Para ver o trabalho dos colegas |
| `git switch -c feature/<nome>` | Cria uma branch nova a partir da atual e já entra nela | No início de cada tarefa |
| `git switch <branch>` | Troca para outra branch | Para mudar de tarefa |
| `git switch -` | Volta para a branch anterior | Para alternar rapidamente entre duas |
| `git checkout <branch>` | Versão antiga do `git switch` | Você vai encontrar em tutoriais antigos; faz o mesmo |
| `git merge <branch>` | Junta a branch indicada na branch atual | Para trazer para a sua branch o que foi feito em outra |
| `git branch -d <branch>` | Apaga uma branch local que já foi juntada | Depois do merge, para limpar |
| ⚠ `git branch -D <branch>` | Apaga a branch mesmo que o trabalho dela não tenha sido juntado | Só quando tiver certeza de que o trabalho pode ser descartado |
| `git push -u origin <branch>` | Envia a branch nova ao GitHub | Para abrir um Pull Request ou guardar o trabalho |
| `git push origin --delete <branch>` | Apaga a branch no GitHub | Depois do merge, para limpar |

**Nomes de branch:** tipo, barra, descrição curta, sem acentos nem espaços. Exemplos: `feature/tela-inicial`, `fix/aposta-vazia`, `docs/readme-instalacao`.

**Antes de trocar de branch**, rode `git status`. Se houver mudanças não gravadas, faça commit ou guarde com `git stash` (seção 9). Caso contrário, o Git pode recusar a troca ou levar as mudanças junto para a outra branch.

**Manter a sua branch atualizada** com a `main`, enquanto a tarefa demora:

```bash
git switch main
git pull
git switch feature/tela-inicial
git merge main
```

## Pull Requests e issues pelo terminal

O Pull Request (PR) é o pedido para juntar uma branch na outra, com espaço para revisão. O Git não tem esse conceito: ele é do GitHub, e o GitHub CLI (`gh`) permite fazer tudo sem abrir o navegador.

### Pull Requests

| Comando | Função | Quando usar |
| --- | --- | --- |
| `gh pr create` | Abre um PR da branch atual, perguntando título e descrição | Depois do `git push -u origin <branch>` |
| `gh pr create --base develop --title "feat: tela inicial" --body "Closes #12"` | O mesmo, sem perguntas, apontando para a branch `develop` | Quando a equipe junta tudo em `develop` antes da `main` |
| `gh pr create --draft` | Abre um PR marcado como rascunho | Para mostrar um trabalho em andamento e pedir opinião cedo |
| `gh pr list` | Lista os PRs abertos do repositório | Para ver o que espera revisão |
| `gh pr checkout <número>` | Baixa a branch de um PR para o seu computador | Para testar o trabalho de um colega antes de aprovar |
| `gh pr view <número> --web` | Abre o PR no navegador | Para comentar linha por linha |
| `gh pr review <número> --approve` | Aprova o PR | Depois de revisar e testar |
| `gh pr review <número> --request-changes -b "texto"` | Pede correções | Quando encontrar problemas na revisão |
| `gh pr merge <número> --squash --delete-branch` | Junta o PR, transformando os commits num só, e apaga a branch | Depois da aprovação e com os testes passando |
| `gh pr status` | Mostra os seus PRs e os que esperam a sua revisão | No começo do dia |

Escrever `Closes #12` na descrição do PR faz o GitHub fechar a issue 12 automaticamente quando o PR for juntado; se o quadro Kanban tiver a automação ligada, o cartão também vai para Done.

### Issues (tarefas)

| Comando | Função | Quando usar |
| --- | --- | --- |
| `gh issue create --title "..." --body "..."` | Registra uma tarefa, bug ou ideia | Sempre que surgir algo a fazer; é o cartão do Backlog |
| `gh issue list` | Lista as issues abertas | Para escolher a próxima tarefa |
| `gh issue list --assignee @me` | Lista só as suas | Para planejar o seu dia |
| `gh issue view <número>` | Mostra os detalhes de uma issue | Antes de começar a tarefa |
| `gh issue close <número>` | Fecha a issue | Quando ela foi resolvida sem PR |

### Outros atalhos úteis

| Comando | Função |
| --- | --- |
| `gh repo view --web` | Abre o repositório no navegador |
| `gh run list` | Lista as últimas execuções da integração contínua (GitHub Actions) |
| `gh run watch` | Acompanha ao vivo os testes que estão rodando |

## Desfazer e corrigir erros

Quase tudo no Git pode ser desfeito. A regra que decide o comando certo é uma só: **o erro já foi enviado ao GitHub ou não?** O que ainda está só no seu computador pode ser reescrito; o que já foi enviado deve ser corrigido com um commit novo, para não quebrar o histórico dos colegas.

### Antes do commit

| Situação | Comando | Função |
| --- | --- | --- |
| ⚠ Quero descartar as mudanças de um arquivo | `git restore <arquivo>` | Volta o arquivo ao estado do último commit. As mudanças não gravadas se perdem |
| Preparei um arquivo por engano | `git restore --staged <arquivo>` | Tira o arquivo da área de preparação, mantendo as mudanças |
| Preciso trocar de tarefa sem gravar o que fiz | `git stash` | Guarda as mudanças numa gaveta e deixa a pasta limpa |
| Quero de volta o que guardei | `git stash pop` | Devolve as mudanças guardadas e as tira da gaveta |
| Quero ver o que está guardado | `git stash list` | Lista as gavetas |
| Quero guardar com um nome | `git stash push -m "login pela metade"` | Facilita achar depois |

### Depois do commit, antes do push

| Situação | Comando | Função |
| --- | --- | --- |
| Errei a mensagem do último commit ou esqueci um arquivo | `git add <arquivo>` e depois `git commit --amend` | Refaz o último commit com a correção |
| Quero desfazer o último commit, mas manter as mudanças | `git reset --soft HEAD~1` | Apaga o commit e deixa tudo preparado de novo |
| Quero desfazer o último commit e as mudanças voltarem para a pasta | `git reset HEAD~1` | Apaga o commit e deixa as mudanças soltas, sem preparar |
| ⚠ Quero jogar fora o último commit e as mudanças | `git reset --hard HEAD~1` | Apaga o commit e as mudanças. Use só com certeza |

### Depois do push

| Situação | Comando | Função |
| --- | --- | --- |
| Um commit já enviado quebrou algo | `git revert <hash>` | Cria um commit novo que desfaz aquele, sem apagar a história. É o jeito seguro em branches compartilhadas |

### A rede de segurança

```bash
git reflog
```

Função: mostra tudo o que o Git fez no seu computador recentemente, inclusive commits "apagados" por `reset` e branches removidas. Quando usar: quando achar que perdeu trabalho. Encontre o hash do ponto que quer recuperar e rode `git switch -c recuperado <hash>` para criar uma branch a partir dele. Só não recupera o que nunca foi gravado em commit nem guardado no stash.

### Limpar arquivos que o Git não conhece

| Comando | Função |
| --- | --- |
| `git clean -n` | Mostra quais arquivos não rastreados seriam apagados, sem apagar |
| ⚠ `git clean -fd` | Apaga de verdade os arquivos e pastas não rastreados. Rode o `-n` antes, sempre |

## Resolver conflitos de merge

Um conflito acontece quando duas branches mudaram as mesmas linhas de um arquivo. O Git não adivinha qual versão está certa: ele para e marca o trecho para você decidir. Não é um erro; é uma pergunta.

O trecho em conflito fica assim dentro do arquivo:

```text
<<<<<<< HEAD
let saldo = 3000;
=======
let saldoPrimes = 3000000n;
>>>>>>> feature/saldo-primes
```

Entre `<<<<<<<` e `=======` está a versão da sua branch; entre `=======` e `>>>>>>>`, a versão que está chegando.

**Passo a passo:**

1. `git status` — lista os arquivos em conflito, marcados como "both modified".
2. Abra cada arquivo e escolha: uma versão, a outra, ou uma combinação das duas. O VS Code mostra botões "Accept Current", "Accept Incoming" e "Accept Both".
3. Apague as três linhas de marcação (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Teste o projeto: o código precisa funcionar depois da escolha.
5. `git add <arquivo>` — marca o conflito daquele arquivo como resolvido.
6. `git commit` — grava o merge. Se o conflito veio de um `git pull --rebase`, use `git rebase --continue` em vez de commit.

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git merge --abort` | Cancela o merge e volta tudo ao estado anterior | Quando o conflito ficou confuso e você quer recomeçar |
| `git rebase --abort` | Cancela um rebase em andamento | O mesmo, durante um `git pull --rebase` |
| `git diff --name-only --diff-filter=U` | Lista só os arquivos ainda em conflito | Quando há muitos arquivos |

**Como ter menos conflitos:** branches curtas, que vivem poucos dias; `git pull` antes de começar; combinar no quadro Kanban quem mexe em qual arquivo; commits pequenos.

## Tags, versões e releases

Uma tag é uma etiqueta permanente num commit, usada para marcar versões publicadas. O padrão mais comum é o versionamento semântico: `vMAIOR.MENOR.CORREÇÃO`, como `v1.4.2`.

| Parte da versão | Sobe quando | Exemplo |
| --- | --- | --- |
| MAIOR | Muda algo que quebra quem já usava | `v1.4.2` → `v2.0.0` |
| MENOR | Entra funcionalidade nova, sem quebrar nada | `v1.4.2` → `v1.5.0` |
| CORREÇÃO | Só correções | `v1.4.2` → `v1.4.3` |

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git tag` | Lista as tags | Para ver as versões já marcadas |
| `git tag -a v1.0.0 -m "Primeira versão"` | Cria uma tag anotada, com autor, data e mensagem, no commit atual | Ao fechar uma versão |
| `git push origin v1.0.0` | Envia uma tag ao GitHub | As tags não vão com o `git push` comum |
| `git push --tags` | Envia todas as tags de uma vez | Quando criou várias |
| `git switch --detach v1.0.0` | Abre o projeto exatamente como estava naquela versão | Para investigar um problema numa versão antiga |
| `gh release create v1.0.0 --generate-notes` | Publica uma release no GitHub, com notas geradas a partir dos PRs | Para anunciar a versão e anexar arquivos |

**Para voltar do modo "detached"**, em que você está vendo uma versão antiga sem estar numa branch, rode `git switch main`.

## O .gitignore e a investigação do histórico

### O que não deve ir para o repositório

O arquivo `.gitignore`, na raiz do projeto, lista o que o Git deve ignorar: dependências baixadas, arquivos gerados, configurações locais e, principalmente, senhas e chaves. Crie-o **antes** do primeiro commit.

```text
# Dependências e arquivos gerados
node_modules/
bin/
obj/
dist/

# Segredos e configurações locais
.env
*.pem
chaves/

# Sistema e editor
.DS_Store
Thumbs.db
.vscode/
```

O GitHub mantém modelos prontos por linguagem no repositório [github/gitignore](https://github.com/github/gitignore). O `gh repo create` também oferece um modelo com a opção `--gitignore Node` (ou `VisualStudio`, `Python` etc.).

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git check-ignore -v <arquivo>` | Diz qual linha do `.gitignore` está ignorando o arquivo | Quando um arquivo não aparece no `git status` e você não sabe por quê |
| `git rm --cached <arquivo>` | Para de versionar o arquivo, mas o mantém na sua pasta | Quando um arquivo que devia ser ignorado já foi commitado; depois, acrescente-o ao `.gitignore` |
| `git rm -r --cached node_modules` | O mesmo, para uma pasta inteira | Quando a pasta de dependências entrou no repositório por engano |

### Investigar o histórico

| Comando | Função | Quando usar |
| --- | --- | --- |
| `git log -p <arquivo>` | Mostra cada mudança feita num arquivo, commit por commit | Para entender como um arquivo chegou ao estado atual |
| `git log --author="Ana"` | Filtra os commits de uma pessoa | Para ver as contribuições de alguém |
| `git log --since="2 weeks ago"` | Filtra por período | Para revisar o que a equipe fez no ciclo |
| `git log --grep="fix"` | Filtra pela mensagem | Para achar correções ou uma tarefa específica |
| `git blame <arquivo>` | Mostra, linha por linha, o último commit e o autor que a alteraram | Para descobrir quando e por que uma linha mudou |
| `git shortlog -sn` | Conta os commits por autor | Para ver a participação de cada integrante da equipe |
| `git grep "texto"` | Procura um texto em todos os arquivos versionados | Para encontrar onde algo é usado |
| `git diff main..feature/tela` | Compara duas branches | Para ver o que uma branch traz antes de juntar |

Para um professor, `git shortlog -sn` e `git log --author` mostram a participação de cada aluno. Contagem de commits, porém, mede frequência e não qualidade: combine com a revisão dos Pull Requests.

## Segurança: segredos, assinatura e comandos perigosos

### Senha ou chave enviada por engano

Se uma senha, token ou chave foi commitada e enviada ao GitHub, considere-a **roubada**, mesmo que o repositório seja privado e mesmo que você apague o arquivo em seguida: ela continua no histórico. A ordem certa é:

1. **Troque a credencial imediatamente** (gere uma nova e desative a antiga). É o único passo que realmente protege.
2. Pare de versionar o arquivo: `git rm --cached .env`, acrescente `.env` ao `.gitignore` e faça commit.
3. Se precisar limpar o histórico, use a ferramenta `git filter-repo` e avise a equipe, porque todos precisarão clonar o repositório de novo. Em repositórios públicos, assuma que a credencial já foi copiada.

Nas configurações do repositório no GitHub, ative a **varredura de segredos com bloqueio de envio** (Settings → Code security → Secret scanning e Push protection). Com ela, o próprio GitHub recusa um `git push` que contenha chaves conhecidas.

### Commits assinados

Qualquer pessoa pode configurar o Git com o seu nome e e-mail e criar commits "em seu nome". A assinatura prova que o commit saiu de você, e o GitHub mostra o selo **Verified**. Dá para usar a mesma chave SSH da autenticação:

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

No PowerShell, troque o caminho por `$env:USERPROFILE\.ssh\id_ed25519.pub`. Depois, cadastre a mesma chave pública no GitHub em **Settings → SSH and GPG keys → New SSH key**, escolhendo o tipo **Signing Key**.

### Comandos perigosos

| Comando | O que pode destruir | Alternativa segura |
| --- | --- | --- |
| `git push --force` | O trabalho dos colegas na branch remota | `git push --force-with-lease`, que recusa se alguém enviou algo que você não tem; e nunca na `main` |
| `git reset --hard` | Todas as mudanças não gravadas | `git stash` antes; ou `git reset --soft` |
| `git clean -fd` | Arquivos que nunca foram versionados | `git clean -n` antes, para ver a lista |
| `git branch -D` | Uma branch com trabalho não juntado | `git branch -d`, que recusa se houver trabalho pendente |
| `git checkout .` ou `git restore .` | Todas as mudanças não gravadas da pasta | `git stash` antes |
| `rm -rf` ou `Remove-Item -Recurse -Force` | Pastas inteiras, sem lixeira | Conferir o caminho com `pwd` e `ls` antes |

### Proteções no GitHub (uma vez por repositório)

- [ ] Proteger a branch `main`: sem envio direto, Pull Request obrigatório com aprovação e testes passando (Settings → Branches).
- [ ] Exigir segundo fator de autenticação de todos os membros da organização.
- [ ] Ativar a varredura de segredos e o bloqueio de envio.
- [ ] Ativar os alertas do Dependabot.

## Fluxo completo, do zero ao Pull Request

Um exemplo real do começo ao fim: criar um projeto, publicá-lo, trabalhar numa tarefa numa branch e abrir o Pull Request. Os comandos do Git são os mesmos nos dois terminais; só a criação de pastas e arquivos muda.

### 1. Criar o projeto e publicar

**PowerShell**

```powershell
cd ~\dev
New-Item -ItemType Directory meu-site
cd meu-site
git init
"# Meu Site" | Out-File README.md -Encoding utf8
"node_modules/`n.env" | Out-File .gitignore -Encoding utf8
git add .
git commit -m "chore: estrutura inicial do projeto"
gh repo create meu-site --private --source . --remote origin --push
```

**Git Bash**

```bash
cd ~/dev
mkdir meu-site && cd meu-site
git init
echo "# Meu Site" > README.md
printf "node_modules/\n.env\n" > .gitignore
git add .
git commit -m "chore: estrutura inicial do projeto"
gh repo create meu-site --private --source . --remote origin --push
```

No PowerShell, `` `n `` dentro de aspas duplas é a quebra de linha. A opção `--push` do `gh repo create` já envia o primeiro commit.

### 2. Trabalhar numa tarefa

```bash
git switch main
git pull
git switch -c feature/pagina-contato
# ... editar os arquivos no VS Code ...
git status
git diff
git add contato.html estilo.css
git commit -m "feat: cria página de contato"
```

### 3. Enviar e abrir o Pull Request

```bash
git pull --rebase origin main
git push -u origin feature/pagina-contato
gh pr create --base main --title "feat: página de contato" --body "Closes #3"
```

### 4. Depois da aprovação

```bash
gh pr merge --squash --delete-branch
git switch main
git pull
git fetch --prune
```

No fim, a `main` do seu computador está igual à do GitHub, com a página de contato, a branch da tarefa foi apagada nos dois lugares, e a issue 3 foi fechada.

## Referência rápida

Os comandos mais usados, organizados pela pergunta que você está fazendo no momento.

| Eu quero... | Comando |
| --- | --- |
| Saber o que mudou | `git status` |
| Ver as mudanças linha por linha | `git diff` (ainda não preparadas) · `git diff --staged` (preparadas) |
| Começar um projeto | `git init` · `gh repo create <nome> --private --source . --remote origin` |
| Baixar um projeto | `git clone <endereço>` |
| Preparar mudanças | `git add <arquivo>` · `git add .` · `git add -p` |
| Gravar | `git commit -m "tipo: descrição"` |
| Enviar ao GitHub | `git push` (primeira vez: `git push -u origin <branch>`) |
| Receber do GitHub | `git pull` · `git pull --rebase` |
| Começar uma tarefa | `git switch -c feature/<nome>` |
| Trocar de branch | `git switch <branch>` |
| Juntar uma branch | `git merge <branch>` |
| Abrir um Pull Request | `gh pr create` |
| Testar o PR de um colega | `gh pr checkout <número>` |
| Ver o histórico | `git log --oneline --graph --all` |
| Guardar mudanças sem gravar | `git stash` · `git stash pop` |
| Descartar mudanças de um arquivo | `git restore <arquivo>` |
| Tirar um arquivo da preparação | `git restore --staged <arquivo>` |
| Corrigir o último commit (não enviado) | `git commit --amend` |
| Desfazer um commit já enviado | `git revert <hash>` |
| Recuperar algo que parecia perdido | `git reflog` |
| Resolver conflito | editar o arquivo → `git add <arquivo>` → `git commit` |
| Desistir de um merge | `git merge --abort` |
| Marcar uma versão | `git tag -a v1.0.0 -m "..."` → `git push origin v1.0.0` |
| Parar de versionar um arquivo | `git rm --cached <arquivo>` + `.gitignore` |
| Saber quem mudou uma linha | `git blame <arquivo>` |
| Ver a participação da equipe | `git shortlog -sn` |
| Sair de uma tela do Git | `q` |

**Três hábitos que evitam a maioria dos problemas:** rodar `git status` antes de qualquer comando; `git pull` antes de começar a trabalhar; commits pequenos, com um assunto cada.
