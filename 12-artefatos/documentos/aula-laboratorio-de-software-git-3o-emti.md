# Aula — Laboratório de Software: Controle de versão com Git

Oct 20, 2026 · @Alan Mateus

Os alunos saem sabendo o que é Git, as três áreas de trabalho e os 6 comandos básicos. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios).

## Roteiro da aula

1. Pergunta de abertura (5 min): "Quem já salvou um arquivo como trabalho\_final\_AGORA\_VAI\_v3.docx?"
2. Quadro + explicação (35 min): blocos A a E abaixo, nessa ordem.
3. Demonstração rápida no computador do professor, se houver projetor (10 min).
4. Exercícios no caderno (aula seguinte ou restante do tempo).

## O que escrever no quadro

**Bloco A — O que é controle de versão**

- Controle de versão = sistema que guarda o histórico de mudanças de um projeto.
- Permite voltar a uma versão antiga e saber quem mudou o quê.
- **Git** = programa de controle de versão (instalado no computador).
- **GitHub** = site que guarda projetos Git na internet (nuvem).

**Bloco B — As 3 áreas do Git**

1. **Diretório de trabalho** → onde você edita os arquivos.
2. **Staging (área de preparação)** → onde ficam os arquivos escolhidos para salvar.
3. **Repositório** → onde ficam as versões salvas (commits).

Desenhe 3 caixas lado a lado com setas: Trabalho → (git add) → Staging → (git commit) → Repositório → (git push) → GitHub.

**Bloco C — Comandos essenciais**

| Comando | O que faz |
| --- | --- |
| git init | Cria um repositório novo na pasta |
| git status | Mostra o estado dos arquivos |
| git add arquivo | Envia o arquivo para o staging |
| git commit -m "mensagem" | Salva uma versão com uma descrição |
| git log | Mostra o histórico de commits |
| git push | Envia os commits para o GitHub |

**Bloco D — Commit**

- Commit = uma "foto" do projeto em um momento.
- Todo commit tem: mensagem, autor, data e um código único (hash).
- Boa mensagem: curta e diz o que mudou. Ex.: "Adiciona menu na página inicial".

**Bloco E — Analogias, erros comuns e pergunta para a turma**

- Commit = checkpoint do jogo: estragou o código, volta ao último checkpoint.
- Staging = arrumar as pessoas para a foto. Commit = apertar o botão.
- Erro 1: achar que Git e GitHub são a mesma coisa → Git funciona sem internet; GitHub é o lugar online.
- Erro 2: fazer commit sem git add → sem staging, o arquivo não entra no commit.
- Erro 3: mensagem vaga ("aaa", "mudei") → ,depois ninguém sabe o que foi feito.
- Pergunta: editei o index.html. Qual o próximo comando para ele entrar no commit?

## Exercícios

1. O que é controle de versão? Responda com suas palavras.
2. Qual a diferença entre Git e GitHub?
3. Cite as 3 áreas do Git na ordem em que o arquivo passa por elas.
4. Qual comando cria um repositório novo em uma pasta?
5. Qual comando mostra quais arquivos foram modificados?
6. Para que serve o comando git add?
7. O que é um commit? Use a analogia do jogo para explicar.
8. Cite 3 informações que todo commit guarda.
9. Qual comando envia os commits para o GitHub?
10. Escreva os comandos, na ordem, para: criar o repositório, adicionar o arquivo index.html, salvar uma versão com a mensagem "Primeira versão do site" e enviar para o GitHub.
11. Qual das mensagens de commit é melhor? Justifique: (a) "mudanças" (b) "Corrige cor do botão de login".
12. **Desafio:** Um colega editou o arquivo style.css e digitou git commit -m "ajusta cores", mas o arquivo não entrou no commit. O que ele esqueceu de fazer?
