# Aula — Laboratório de Software: Terminal e Git no Projeto BSD

Oct 21, 2026 · @Alan Mateus

Aula de aplicação: os alunos usam o que viram nas apostilas 08 a 14 dentro do Projeto Integrador (Casa de Apostas Provably Fair sobre a rede BSD) e aprendem Git, que o projeto exige. Duração sugerida: 3 aulas de 50 min (Blocos A–D, Blocos E–G e exercícios). Tudo o que os exercícios cobram está escrito no quadro.

## Alinhamento

| Item da ementa | Apostila | Onde entra no projeto |
| --- | --- | --- |
| Linha de comando, navegação e arquivos | 08 e 09 | Criar a estrutura do repositório |
| Pipes, redirecionamentos e filtros | 10 e 11 | Consultar o log de apostas |
| Permissões e diretivas de segurança | 12 e 17 | Proteger a chave privada (chmod 600) |
| Comandos em lote | 13 | Script de backup do banco |
| Backup e restore | 14 | Backup e restauração do banco do jogo |
| Adicional (fora da ementa) | — | Git e GitHub (seção 6 do Projeto Integrador) |
|  |  |  |

## Roteiro da aula

1. Pergunta de abertura (5 min): "Se o banco de dados da casa de apostas for apagado agora, quanto da turma perde o saldo em PRIMEs?"
2. Aula 1 — Blocos A a D no quadro (45 min).
3. Aula 2 — Blocos E a G no quadro (45 min). Se houver projetor, execute os comandos no terminal enquanto explica.
4. Aula 3 — Exercícios no caderno.

## O que escrever no quadro

**Bloco A — Navegação e arquivos (revisão das apostilas 08 e 09)**

| Comando (Linux) | O que faz |
| --- | --- |
| pwd | Mostra a pasta atual |
| ls -la | Lista arquivos com detalhes e permissões |
| cd pasta / cd .. | Entra na pasta / volta uma pasta |
| mkdir -p pasta | Cria a pasta (e as pastas do caminho, se faltarem) |
| touch arquivo | Cria um arquivo vazio |
| cp origem destino | Copia |
| mv origem destino | Move ou renomeia |
| rm arquivo | Apaga (no terminal não tem lixeira) |

Exemplo do projeto — criar a estrutura do repositório:

```
mkdir -p bsd-cassino/src bsd-cassino/docs bsd-cassino/scripts
cd bsd-cassino
touch README.md
```

**Bloco B — Pipes, redirecionamentos e filtros no log de apostas (apostilas 10 e 11)**

Arquivo apostas.log (cada linha é uma aposta):

```
10:05 carteira=BSD1a3 jogo=dado aposta=500 resultado=PERDEU
10:06 carteira=BSD7f2 jogo=dado aposta=200 resultado=GANHOU
10:07 carteira=BSD1a3 jogo=dado aposta=300 resultado=PERDEU
```

- | (pipe) = passa a saída de um comando para o próximo.
- > = grava a saída em um arquivo (apaga o que tinha).
- > > = acrescenta no final do arquivo.

| Comando | O que faz |
| --- | --- |
| grep "PERDEU" apostas.log | Mostra só as apostas perdidas |
| grep "PERDEU" apostas.log \| wc -l | Conta quantas apostas foram perdidas |
| tail -3 apostas.log | Mostra as 3 últimas apostas |
| grep "BSD1a3" apostas.log > minhas.txt | Salva as apostas da carteira BSD1a3 em um arquivo |

**Bloco C — Permissões e a chave privada (apostilas 12 e 17)**

- r = ler, w = escrever, x = executar. Valem para 3 grupos: dono, grupo e outros.
- Forma em números: **r = 4, w = 2, x = 1**. Soma-se o que cada grupo pode.
- 6 = 4 + 2 = ler e escrever. 0 = nenhuma permissão.
- **chmod 600 chave\_privada.pem** → dono lê e escreve; grupo e outros não fazem nada.
- O ls -la mostra: -rw------- chave\_privada.pem
- Por quê: quem lê a chave privada consegue gastar os PRIMEs da carteira.

**Bloco D — Script de backup do banco (apostilas 13 e 14)**

Arquivo scripts/backup.sh:

```
#!/bin/bash
# Backup do banco da casa de apostas
DATA=$(date +%Y-%m-%d)
mkdir -p backup
cp banco.db backup/banco_$DATA.db
echo "Backup feito: banco_$DATA.db" >> backup.log
```

- Tornar executável: chmod +x backup.sh
- Executar: ./backup.sh
- Restaurar depois de uma falha: cp backup/banco\_2026-10-21.db banco.db
- Regra 3-2-1: 3 cópias, 2 mídias diferentes, 1 fora do local.

**Bloco E — Git: controle de versão (conteúdo adicional do projeto)**

- Controle de versão = sistema que guarda o histórico de mudanças de um projeto.
- Permite voltar a uma versão antiga e saber quem mudou o quê.
- **Git** = programa instalado no computador; funciona sem internet.
- **GitHub** = site que guarda o repositório na nuvem para a equipe toda.
- No projeto, cada função (Frontend, Backend, DevOps, Hardware) envia o seu trabalho pelo GitHub.

As 3 áreas — desenhe 3 caixas com setas:

**Trabalho → (git add) → Staging → (git commit) → Repositório → (git push) → GitHub**

**Bloco F — Comandos Git e o .gitignore**

| Comando | O que faz |
| --- | --- |
| git init | Cria um repositório na pasta |
| git status | Mostra quais arquivos foram modificados |
| git add arquivo | Envia o arquivo para o staging |
| git commit -m "mensagem" | Salva uma versão (commit) com descrição |
| git log | Mostra o histórico de commits |
| git push | Envia os commits para o GitHub |

- Commit = uma "foto" do projeto. Guarda mensagem, autor, data e um código único (hash).
- Boa mensagem: curta e diz o que mudou. Ex.: "Adiciona script de backup do banco".
- **.gitignore** = arquivo com a lista do que o Git NÃO deve enviar.
- No projeto, o .gitignore tem: chave\_privada.pem, banco.db e a pasta backup/.

**Bloco G — Analogias, erros comuns e pergunta para a turma**

- Commit = checkpoint do jogo: estragou o código, volta ao último checkpoint.
- Backup = cópia dos dados. Commit = cópia do código. Um não substitui o outro.
- Erro 1: usar > quando queria >> → o arquivo de log antigo é apagado.
- Erro 2: esquecer o chmod +x → o script não executa com ./backup.sh.
- Erro 3: enviar a chave privada para o GitHub → qualquer pessoa pode gastar os PRIMEs. Por isso ela vai no .gitignore.
- Erro 4: fazer commit sem git add → o arquivo não entra no commit.
- Pergunta: quero contar quantas apostas a carteira BSD7f2 fez. Qual comando uso?

## Exercícios

1. Qual comando mostra a pasta atual? E qual lista os arquivos com as permissões?
2. Escreva o comando que cria as pastas src, docs e scripts dentro de bsd-cassino de uma vez.
3. Qual a diferença entre > e >>?
4. O que faz o pipe ( | )?
5. Escreva o comando que mostra só as apostas perdidas do arquivo apostas.log.
6. Escreva o comando que conta quantas apostas foram perdidas.
7. Qual comando mostra as 3 últimas apostas do log?
8. Quanto vale r, w e x na forma em números? Quanto vale o 6?
9. O que significa chmod 600 chave\_privada.pem? Por que a chave precisa dessa permissão?
10. Explique o que cada linha do script backup.sh faz.
11. Quais dois comandos tornam o script executável e o executam?
12. Escreva o comando que restaura o banco a partir do arquivo backup/banco\_2026-10-21.db.
13. O que é a regra 3-2-1 de backup?
14. Qual a diferença entre Git e GitHub?
15. Escreva, na ordem, as 3 áreas do Git e o comando que leva o arquivo de uma área para a outra.
16. Para que serve o .gitignore? Cite 3 arquivos do projeto que devem estar nele.
17. Qual a diferença entre backup e commit?
18. **Desafio:** Um colega rodou git add chave\_privada.pem, fez o commit e o push. Explique o risco para o projeto e o que deveria ter feito antes (use os Blocos C e F).

## Conteúdo complementar — itens da ementa que faltavam

Estes blocos completam a ementa de Laboratório de Software e seguem as apostilas 01 a 07 e 15 a 18. Sugestão: mais 2 aulas de 50 min (Blocos H–J e Blocos K–M). Tudo o que a avaliação cobra está nestes blocos ou nos Blocos A a G.

**Bloco H — Instalação e desinstalação de SO e aplicativos (apostilas 01 a 04)**

As 5 etapas da instalação de um SO:

1. Preparar a mídia: baixar a ISO e gravar no pen drive (Rufus no Windows, dd no Linux).
2. Configurar o boot: na BIOS/UEFI, colocar o pen drive como primeiro dispositivo.
3. Particionamento: escolher onde o SO será instalado.
4. Instalação: os arquivos são copiados.
5. Pós-instalação: criar usuário, instalar drivers e atualizar.

- Quando reinstalar do zero: SO corrompido que não inicia, vírus grave ou PC muito lento.

| Tarefa | Windows | Linux (Ubuntu) |
| --- | --- | --- |
| Instalar aplicativo | winget install nome | sudo apt install nome |
| Remover aplicativo | winget uninstall nome | sudo apt remove nome |
| Remover aplicativo e configurações | — | sudo apt purge nome |
| Atualizar o sistema | Windows Update | sudo apt update && sudo apt upgrade |

- No projeto: a máquina de validação recebe o Ubuntu e, depois, os aplicativos da stack pelo terminal.

**Bloco I — Máquinas virtuais (apostilas 05 a 07)**

- Máquina virtual (VM) = um computador simulado dentro do computador real (o host). Ex.: VirtualBox.
- Configuração recomendada: 2 GB de RAM (no máximo 50% da RAM do host), disco de 20 GB dinâmico, rede NAT.
- **Snapshot** = "fotografia" do estado completo da VM. Se algo der errado, volta exatamente para aquele ponto.
- **Clone completo** = cópia independente da VM. **Clone vinculado** = usa o disco da VM original e economiza espaço.
- No projeto: a equipe monta a stack em uma VM e tira um snapshot antes de cada instalação nova.

**Bloco J — Imagem de sistema e recuperação a desastres (apostilas 15 e 16)**

- **Imagem de sistema** = cópia exata de todo o disco: SO, programas, configurações e arquivos.
- Diferença: o backup copia os arquivos; a imagem copia o disco inteiro e devolve o PC ao estado exato.
- Ferramentas de imagem: Criar imagem do sistema (Windows), Clonezilla, dd e Timeshift (Linux).
- **Recuperação a desastres** = restaurar o sistema depois de uma falha grave, com ferramentas que rodam fora do SO.

| Ferramenta | Quando usar |
| --- | --- |
| WinRE (Shift + Reiniciar; se o Windows não abrir, pelo pen drive de instalação) | Windows não inicia; reparar o boot ou restaurar imagem |
| Live USB | O SO não inicia de jeito nenhum |
| Clonezilla bootável | Restaurar uma imagem de disco salva |
| TestDisk | Recuperar partições perdidas |

- No projeto: guardar uma imagem da máquina de validação já configurada. Se o disco falhar, ela volta pronta em minutos.

**Bloco K — Diretivas de segurança (apostila 17)**

- Diretivas de segurança = regras que controlam o comportamento do SO e dos usuários.
- No Windows, ficam na Política de Grupo: **Win + R → gpedit.msc**.

| Diretiva | Windows | Linux |
| --- | --- | --- |
| Complexidade de senha | Política de Grupo > Senha | /etc/pam.d/common-password |
| Expiração de senha | Política de Grupo > Senha | sudo chage -M 90 usuario |
| Controle de administrador | UAC | sudo e /etc/sudoers |
| Firewall | Windows Defender Firewall | ufw |
| Ver logins que falharam | Visualizador de Eventos | grep Failed /var/log/auth.log |

- No projeto: liberar a porta do jogo e depois ligar o firewall (ex.: 3000):

```
sudo ufw allow 3000
sudo ufw enable
```

**Bloco L — Correção de falhas no sistema de arquivos (apostila 18)**

- O sistema de arquivos pode corromper com queda de energia, remoção errada de pen drive ou disco com defeito.

| Ferramenta | SO | O que faz |
| --- | --- | --- |
| chkdsk C: /f /r | Windows | Verifica e corrige erros do disco (NTFS) |
| sfc /scannow | Windows | Restaura arquivos de sistema corrompidos |
| fsck | Linux | Verifica e corrige erros do sistema de arquivos (ext4) |

- O fsck deve ser rodado com a partição desmontada (fora de uso).
- No projeto: queda de energia → o banco não abre → rodar o fsck no disco → se o banco continuar com defeito, restaurar o último backup (Bloco D).

**Bloco M — Erros comuns dos blocos complementares**

- Erro 1: usar apt remove quando queria limpar tudo → as configurações ficam. Use apt purge.
- Erro 2: dar à VM mais da metade da RAM do host → o computador real fica lento.
- Erro 3: achar que backup e imagem são iguais → a imagem copia o disco inteiro, com o SO.
- Erro 4: ligar o firewall sem liberar a porta do jogo → ninguém consegue acessar a casa de apostas.
- Pergunta: o Windows não inicia depois de uma queda de energia. Qual ferramenta você abre pelo pen drive de instalação para reparar o boot?

## Avaliação — Laboratório de Software

Nome: ..................................................   Turma: ..............   Data: ...... / ...... / ............

Marque apenas uma alternativa em cada questão.

1. Qual comando mostra a pasta atual no Linux? a) pwd b) ls -la c) cd .. d) rm
2. O que faz o símbolo >> no terminal? a) Apaga o arquivo b) Passa a saída de um comando para outro c) Acrescenta a saída no final do arquivo d) Ordena as linhas do arquivo
3. Qual comando conta quantas apostas foram perdidas no arquivo apostas.log? a) tail -3 apostas.log b) grep "PERDEU" apostas.log | wc -l c) cat apostas.log d) mkdir PERDEU
4. O que significa chmod 600 chave\_privada.pem? a) Todos podem ler e escrever b) Só os outros usuários podem ler c) Ninguém pode acessar, nem o dono d) Só o dono pode ler e escrever
5. Antes de executar ./backup.sh pela primeira vez, é preciso: a) Apagar o banco de dados b) Rodar git push c) Rodar chmod +x backup.sh d) Reiniciar o computador
6. O que diz a regra 3-2-1 de backup? a) 3 cópias, 2 mídias diferentes, 1 fora do local b) 3 backups por dia, durante 2 semanas, em 1 disco c) 3 pastas, 2 arquivos e 1 disco d) 3 senhas, 2 usuários e 1 administrador
7. Qual arquivo impede que a chave privada seja enviada para o GitHub? a) README.md b) backup.sh c) apostas.log d) .gitignore
8. O que é um snapshot de máquina virtual? a) Uma cópia de um arquivo de texto b) Uma "fotografia" do estado completo da VM, para voltar depois c) Um programa antivírus d) Um tipo de cabo de rede
9. Para que servem o Clonezilla e o dd? a) Editar textos b) Criar uma imagem, cópia exata do disco c) Navegar na internet d) Medir a tensão da fonte
10. O que abre o comando gpedit.msc no Windows? a) O Gerenciador de Tarefas b) O Prompt de Comando c) O VirtualBox d) O Editor de Política de Grupo Local
11. Qual ferramenta corrige erros no sistema de arquivos ext4 do Linux? a) fsck b) chkdsk c) sfc /scannow d) winget
12. Qual comando remove um aplicativo e também as configurações dele no Ubuntu? a) sudo apt install nome b) sudo apt update c) sudo apt purge nome d) ls -la

**Questão Extra** — Qual comando mostra as tentativas de login que falharam no Linux?

- a) sudo ufw enable
- b) grep Failed /var/log/auth.log
- c) git log
- d) cd /

**Desafio** — Houve uma queda de energia no laboratório. O Linux da máquina do projeto até inicia, mas o banco da casa de apostas não abre. Usando os Blocos D, J e L, descreva em ordem o que você faria para colocar o sistema de volta no ar sem perder os saldos em PRIMEs.

...........................................................................................................................

...........................................................................................................................

...........................................................................................................................

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
