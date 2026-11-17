---
tags: [estudo, assunto, engenharia-de-software, git]
area: 08 · Engenharia de software
nivel-alvo: N4
quando: M1 (semana 2)
professor: s-git
prereq: [terminal-linux]
status: a-estudar
verificado-em: pendente (reescrever pelo protocolo antes de estudar)
atualizado: 2026-11-17
---

# Git e controle de versão

> **Em uma frase:** Git guarda **fotos completas do seu projeto ao longo do tempo** (commits), deixa você trabalhar em linhas paralelas (branches), juntar o trabalho e voltar a qualquer ponto, sem depender de servidor.
> **Nível-alvo:** N4. É a ferramenta que você mais vai usar na vida, e no seu setup é o canal por onde a IA entrega trabalho para você revisar (PR).
> **Os 20% que resolvem 80%:** `status`, `add`, `commit` · branch e merge · `push`/`pull` e pull request · desfazer sem medo (`restore`, `revert`, `reflog`) · commits pequenos com boa mensagem.

---

## 1. Por que isso existe (o problema e a história)

- Sem controle de versão, a história de um projeto é `site-final-v2-AGORA-VAI.zip`. Duas pessoas mexendo no mesmo arquivo se atropelam, e um erro apagado não volta.
- Os primeiros sistemas (RCS, CVS, Subversion) eram **centralizados**: um servidor guardava a história, e sem ele você não fazia nada.
- Em **2005**, o kernel Linux perdeu a licença gratuita do BitKeeper, o sistema que usava. **Linus Torvalds** escreveu o Git em poucas semanas, com três metas: ser **rápido**, **distribuído** (cada cópia tem a história inteira) e **impossível de corromper sem perceber**.
- O **GitHub** (2008) somou pull requests, issues e uma rede social de código. Hoje Git é padrão absoluto.

**A lição do Akita:** entender o Git por dentro, não decorar comandos. O episódio [#70](https://akitaonrails.com/2020/02/05/akitando-70-entendendo-git-nao-e-um-tutorial/) diz no título que não é tutorial: é sobre como ele funciona. O [#71](https://akitaonrails.com/2020/02/12/akitando-71-usando-git-direito-limpando-seus-commits/) é sobre manter a história limpa.

## 2. O que é

| Conceito | O que é |
|---|---|
| **Repositório** | A pasta do projeto mais a pasta `.git` com toda a história |
| **Commit** | Uma foto completa do projeto, com autor, data, mensagem e um ponteiro para o commit anterior |
| **Área de preparação** (staging/index) | Onde você monta o próximo commit (`git add`) |
| **Branch** | Só um **ponteiro com nome** para um commit; anda sozinho a cada novo commit |
| **HEAD** | Onde você está agora (normalmente, uma branch) |
| **Remoto** | Outra cópia do repositório (o GitHub, chamado `origin`) |
| **Merge** | Junta duas linhas de história num commit novo |
| **Rebase** | Reaplica seus commits em cima de outra base, deixando a história reta |
| **Pull request (PR)** | Pedido para juntar uma branch, com revisão e CI antes do merge (recurso do GitHub, não do Git) |
| **Tag** | Nome fixo para um commit (`v2.30.0`) |

## 3. Como funciona por baixo

- O Git é um **banco de objetos endereçados pelo conteúdo**. Cada objeto é identificado pelo **hash** do próprio conteúdo:
  - **blob**: o conteúdo de um arquivo;
  - **tree**: uma pasta (nomes apontando para blobs e outras trees);
  - **commit**: aponta para uma tree (a foto) e para o commit pai;
  - **tag** anotada.
- Mudou um byte, muda o hash. Por isso o Git percebe qualquer corrupção, e por isso "reescrever a história" cria commits **novos** em vez de alterar os antigos.
- Um arquivo que não mudou não é copiado de novo: a tree nova aponta para o mesmo blob. As fotos são completas, mas baratas.
- **Branch** é um arquivo de texto com um hash dentro. Criar branch é instantâneo.
- O **reflog** guarda por onde o HEAD passou. Quase nada se perde de verdade no Git; o que se perde é o caminho até o commit, e o reflog mostra o caminho.
- Hash, assinatura e criptografia: episódio [#147 Criptografia na prática (Git, BitTorrent, Bitcoin)](https://akitaonrails.com/2023/11/10/akitando-147-criptografia-na-pratica-certificados-bittorrent-git-bitcoin/).

## 4. Conceitos que você precisa dominar

- [ ] As 3 áreas: diretório de trabalho → staging → repositório.
- [ ] `git status`, `add`, `commit`, `log --oneline --graph`, `diff`, `diff --staged`.
- [ ] Mensagem de commit boa: o quê e por quê, no imperativo, curta no título.
- [ ] Commits pequenos e com um assunto só.
- [ ] `branch`, `switch -c`, `merge`; merge fast-forward × merge commit.
- [ ] Resolver conflito: ler os marcadores, decidir, testar, commitar.
- [ ] `push`, `pull`, `fetch`; `pull --rebase`.
- [ ] Fluxo de PR: branch → commits → push → PR → CI → revisão → merge.
- [ ] Desfazer:
  - [ ] `git restore arquivo` (descartar mudança não commitada);
  - [ ] `git restore --staged` (tirar do staging);
  - [ ] `git commit --amend` (corrigir o último commit **antes** do push);
  - [ ] `git revert` (desfazer um commit já publicado, criando outro);
  - [ ] `git reset` (soft, mixed, hard) e o risco do `--hard`;
  - [ ] `git reflog` para recuperar o que parecia perdido.
- [ ] Rebase e a regra de ouro: **nunca reescrever história que outra pessoa já puxou**; se precisar forçar, `--force-with-lease`.
- [ ] Limpar commits antes do PR (rebase interativo, como no #71).
- [ ] `.gitignore`; e por que segredo **nunca** entra no Git (nem cifrado, no seu setup).
- [ ] Tags e versionamento semântico (MAJOR.MINOR.PATCH).
- [ ] `git stash`, `cherry-pick`, `bisect` (achar o commit que introduziu um bug).

## 5. Qualidades

- **Nada se perde:** qualquer ponto do passado é recuperável.
- **Coragem para mudar:** experimente numa branch; se der errado, apague.
- **Trabalho em paralelo** de pessoas e de **agentes de IA** (cada agente na sua branch ou worktree).
- **Distribuído e rápido:** funciona offline.
- **A história explica o código:** `git log` e `git blame` mostram por que cada linha existe.

## 6. Defeitos, limites e críticas

- **Interface confusa:** comandos com nomes pouco intuitivos e várias formas de fazer a mesma coisa (por isso o `switch` e o `restore` foram criados para separar funções do antigo `checkout`).
- **Arquivos binários grandes** (vídeo, modelos de IA) incham o repositório; para eles existe o Git LFS ou outro armazenamento.
- **Reescrever história compartilhada** causa estragos.
- **Git não é backup:** o repositório local some com o disco. Backup é o restic; o GitHub é um remoto, não uma cópia de segurança de tudo.
- **Segredo commitado fica na história** mesmo se apagado depois. A solução é trocar o segredo, não só apagar o arquivo.

## 7. Quando usar e quando não usar

Use para **todo** código, configuração, documentação e notas (o seu vault é um repositório). Não use para segredos, arquivos gerados que podem ser reconstruídos (`node_modules`, `dist`) e arquivos binários enormes.

## 8. Erros comuns

- Commit gigante com "várias coisas" e mensagem "ajustes".
- Trabalhar direto na `main` em vez de branch e PR.
- `git push --force` em branch compartilhada.
- `git reset --hard` sem saber o que vai perder (e sem lembrar do reflog).
- Commitar `.env` com senha.
- Resolver conflito apagando o código do outro sem testar.
- Aprovar PR da IA sem ler o diff.

## 9. No seu setup e no AM Gestão

- **Esteira de sites:** issue → agente → **PR** → prévia → **sua aprovação** → deploy. O PR é onde você exerce a Trilha R (revisar código de IA).
- **Portão antes do commit:** `just check` (dados, documentação gerada, testes, gitleaks e ShellCheck), o mesmo que o CI confere.
- **Tags automáticas:** o hook `pre-push` com `tools/git/taguear.py` cria a tag de cada versão do CHANGELOG.
- **Vault:** o Obsidian Git salva as notas a cada 10 minutos; a pasta 11 é espelho do dev-setup e não se edita à mão (ADR 0013 e 0018).
- **Regras do Akita no setup:** AK-0008 (mudança em banco só por migration versionada), AK-0017 (revisão automática de PR que trata a descrição como não verificada), AK-0018 (bug começa pelo teste que reproduz).
- **Professor:** módulo `s-git` (commit, branch, PR e como desfazer sem medo).

## 10. O que o mercado cobra

- **Júnior:** fluxo básico, branch, PR, resolver conflito simples, mensagem de commit decente. Um GitHub com histórico real conta pontos.
- **Pleno:** rebase, história limpa, revisão de PR, `revert` em produção, `bisect`.
- **Sênior:** estratégia de branch da equipe, proteção da `main`, CI como portão, recuperação de desastres (`reflog`), revisar o trabalho de agentes em paralelo.
- **Perguntas comuns:** diferença entre merge e rebase; como desfazer um commit já publicado; o que é `HEAD`; como achar o commit que introduziu um bug; o que fazer se uma senha foi commitada.

## 11. Exercícios

Sem IA. Use `git help <comando>`.

- **N1:** desenhe no papel o grafo de commits depois de: commit A, commit B, branch `feature`, commit C na `feature`, commit D na `main`, merge da `feature`.
- **N2:** no repositório `logica-ts`: um commit por exercício, uma branch para o ARCA, PR no GitHub, merge.
- **N3:**
  - Crie de propósito um conflito em duas branches e resolva.
  - Faça um `reset --hard` "errado" e recupere o commit pelo `reflog`.
  - Ache o erro: alguém fez `push --force` na `main` depois de um rebase. O que aconteceu com os commits dos outros e como recuperar?
- **N4:** com `git bisect`, ache em qual de 20 commits um teste começou a falhar (crie o cenário num repositório de treino). Depois, revise um PR aberto pelo agente na esteira usando o checklist da Trilha R e escreva os comentários.

## 12. Fontes (na ordem de uso)

1. **Oficial:** [Pro Git, em português](https://git-scm.com/book/pt-br/v2) (capítulos 1 a 3 primeiro; capítulo 10 "Git por dentro" no N3) · [documentação do GitHub sobre pull requests](https://docs.github.com/pt/pull-requests)
2. **Akita:** #70 Entendendo Git · #71 Usando Git direito · [#146 Protegendo e recuperando dados perdidos (Git, backup, BTRFS)](https://akitaonrails.com/2023/10/19/akitando-146-protegendo-e-recuperando-dados-perdidos-git-backup-btrfs/) · #147 (hashes)
3. **Alura:** "Git e GitHub: controle de versão" e "Git e GitHub: branching, conflitos e pull requests"
4. **Treino visual:** [Learn Git Branching](https://learngitbranching.js.org/?locale=pt_BR)

## 13. Como saber que dominou

- [ ] Explico em 3 a 5 frases o que é um commit por dentro (tree, blob, pai, hash).
- [ ] Desfaço qualquer erro comum sem procurar na internet.
- [ ] Meus PRs têm commits pequenos e mensagens que explicam o porquê.
- [ ] Revisei 10 PRs da esteira com o checklist da Trilha R.
- [ ] **Registro de entrevista:** contexto (teste quebrou sem ninguém saber por quê), decisão (`git bisect`), alternativa descartada (ler 20 commits na mão), resultado (commit achado em N passos).
- [ ] **N4:** dei aula de Git (Laboratório de Software). Onde e quando: ______
