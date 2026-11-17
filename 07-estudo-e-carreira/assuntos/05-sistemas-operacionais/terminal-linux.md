---
tags: [estudo, assunto, sistemas-operacionais, linux]
area: 05 · Sistemas operacionais
nivel-alvo: N4
quando: M1 (semana 2)
professor: s-terminal
prereq: []
status: a-estudar
atualizado: 2026-11-17
---

# Terminal Linux e shell

> **Em uma frase:** o terminal é a janela onde você conversa com o sistema por texto; o **shell** (Bash, Zsh) é o programa que lê o que você digita, roda os comandos e liga um comando no outro.
> **Nível-alvo:** N4. Todo o seu setup é operado por terminal (`just`, Git, Docker, Claude Code). E você dá aula de Sistemas Operacionais.
> **Os 20% que resolvem 80%:** navegar e ler arquivos · procurar (`grep`, `find`) · pipes e redirecionamento · permissões · processos e variáveis de ambiente.

---

## 1. Por que isso existe (o problema e a história)

- Antes das telas gráficas, a única interface era o texto: primeiro o teletipo, depois o terminal de vídeo. "Terminal" vem daí, a ponta do fio ligada ao computador central.
- O **Unix** (Bell Labs, anos 70, Ken Thompson e Dennis Ritchie) criou a filosofia que vale até hoje: **programas pequenos que fazem uma coisa bem e se combinam por texto**. O pipe (`|`) é a cola.
- O **shell** evoluiu: Thompson shell → Bourne shell → **Bash** (projeto GNU, 1989) → Zsh e outros. O **Linux** (Linus Torvalds, 1991) juntou o kernel ao conjunto GNU e virou o sistema que roda a maioria dos servidores do mundo.
- Por que ainda usar texto? Porque é **repetível, automatizável e combinável**. Um comando vira script, o script vira tarefa agendada, a tarefa vira o seu setup rodando sozinho.

**A lição do Akita:** entender o que acontece por baixo do que você usa. O PC, o boot, o sistema de arquivos e o WSL2 têm episódios próprios no canal, porque quem não entende a máquina fica refém dela.

## 2. O que é

| Termo | O que é |
|---|---|
| **Terminal** (emulador) | O programa com a janela de texto (Windows Terminal, Ghostty, Kitty) |
| **Shell** | O interpretador de comandos que roda dentro dele (Bash, Zsh) |
| **Comando** | Um programa (`ls`, `grep`) ou um comando embutido do shell (`cd`, `export`) |
| **Prompt** | A linha que espera o seu comando (`alan@notebook:~$`) |
| **Script** | Um arquivo com comandos que o shell executa em sequência |

## 3. Como funciona por baixo

- Quando você digita `ls -la`, o shell **separa** as palavras, **procura** o programa `ls` nas pastas listadas em `PATH`, cria um **processo filho** (chamadas `fork` e `exec`), espera ele terminar e lê o **código de saída** (0 = deu certo; outro número = erro).
- Todo processo nasce com 3 canais abertos: **0 stdin** (entrada), **1 stdout** (saída), **2 stderr** (erros). Redirecionar é ligar esses canais a arquivos; o **pipe** liga o stdout de um processo ao stdin do próximo.
- No Linux, **"tudo é arquivo"**: discos, terminais e até informações do kernel aparecem como arquivos (`/dev`, `/proc`).
- **Permissões:** cada arquivo tem dono, grupo e os bits `rwx` (ler, escrever, executar) para dono, grupo e outros.
- **WSL2:** é um kernel Linux de verdade numa máquina virtual leve dentro do Windows. Arquivos do projeto devem ficar no lado Linux (`~/dev`), não em `/mnt/c`, porque atravessar a fronteira é bem mais lento ([#60 Entendendo WSL 2](https://akitaonrails.com/2019/09/04/akitando-60-entendendo-wsl-2-e-uma-curta-historia-sobre-windows-nt/)).

## 4. Conceitos que você precisa dominar

- [ ] Estrutura de pastas do Linux (FHS): `/`, `/home`, `/etc`, `/var`, `/usr`, `/tmp`, `/dev`, `/proc`.
- [ ] Caminho absoluto × relativo; `~`, `.`, `..`.
- [ ] Navegar e ler: `pwd`, `cd`, `ls -la`, `cat`, `less`, `head`, `tail -f`.
- [ ] Criar, copiar, mover, apagar: `mkdir -p`, `cp -r`, `mv`, `rm` (e por que `rm -rf` exige atenção).
- [ ] Procurar: `grep -rn`, `find`, `which`; e `rg` (ripgrep) no dia a dia.
- [ ] Pipes e redirecionamento: `|`, `>`, `>>`, `2>`, `2>&1`, `<`.
- [ ] Combinar: `wc -l`, `sort`, `uniq -c`, `cut`, `xargs`.
- [ ] Permissões: `chmod`, `chown`, `sudo`, o que significa `-rwxr-xr--`.
- [ ] Processos: `ps`, `top`/`htop`, `kill`, sinais (`SIGTERM`, `SIGKILL`), `&`, `jobs`.
- [ ] Variáveis de ambiente: `echo $PATH`, `export`, `.bashrc`/`.zshrc`.
- [ ] Código de saída: `$?`, `&&`, `||`.
- [ ] Ajuda: `man`, `--help`, `tldr`.
- [ ] Script básico: shebang (`#!/usr/bin/env bash`), `set -euo pipefail`, variáveis, `if`, `for`, funções; ShellCheck.
- [ ] Pacotes: `apt` (Ubuntu do WSL) e, no T2, `pacman` (Arch).

## 5. Qualidades

- **Automatizável:** o que você digita duas vezes vira script, e o que roda três vezes vira tarefa do setup.
- **Rápido** para procurar e transformar milhares de arquivos.
- **Funciona igual** no notebook, no servidor, na VM e no container.
- **Remoto por SSH** com pouca banda.
- **Base de tudo** no setup: `just`, Git, Docker, Claude Code, deploy.

## 6. Defeitos, limites e críticas

- **Curva de entrada** e mensagens de erro secas.
- **Um comando errado pode destruir dados** (`rm -rf` no lugar errado, `>` sobrescrevendo um arquivo). Por isso o backup com restic e os snapshots.
- **Scripts de shell crescem mal:** acima de umas 100 linhas, quebram em casos estranhos (espaços em nomes de arquivo, erros ignorados). Aí a ferramenta vira Python ou Go.
- **Diferenças entre sistemas:** comandos do macOS (BSD) e do Linux (GNU) têm opções diferentes; o PowerShell do Windows é outro mundo.

## 7. Quando usar e quando não usar

| Use terminal e shell para… | Prefira outra coisa para… |
|---|---|
| Operar o setup, Git, Docker, deploy | Lógica de negócio → TypeScript |
| Procurar e transformar arquivos | Script que passou de ~100 linhas ou precisa de testes → Python ou Go |
| Automatizar tarefas curtas e agendar | Edição visual de design ou planilha |

## 8. Erros comuns

- Rodar comando colado da internet (ou da IA) sem ler o que ele faz.
- `sudo` em tudo.
- Trabalhar no `/mnt/c` dentro do WSL e achar que o Linux é lento.
- Esquecer as aspas em `"$variavel"` e quebrar com nomes que têm espaço.
- Script sem `set -euo pipefail`, que continua depois de um erro.
- Não ler a mensagem de erro inteira antes de pedir ajuda.

## 9. No seu setup e no AM Gestão

- **A porta única do setup é o `just`** (`just professor hoje`, `just agora`, `just check`), que roda comandos de shell por baixo.
- **Scripts do setup:** `scripts/wsl/bootstrap.sh`, `ligar-tudo.sh`, `verificar.sh`, conferidos pelo **ShellCheck** no `just check` e no CI.
- **Segurança de agentes:** o Claude Code roda dentro do `ai-jail`; parte do seu trabalho é **ler o comando que a IA quer rodar** antes de aprovar.
- **Professor:** módulo `s-terminal`. Prática do módulo: no Ubuntu do WSL, achar todos os arquivos `.md` do dev-setup que citam "restic" e contar quantos são, **num comando só**.

## 10. O que o mercado cobra

- **Júnior:** navegar, ler logs, usar Git e npm pelo terminal, rodar o projeto localmente sem interface gráfica.
- **Pleno:** scripts simples, diagnosticar processo travado, porta ocupada, permissão negada; SSH em servidor.
- **Sênior:** automação confiável, investigar incidente em produção pelos logs, saber quando o script deve virar programa.
- **Perguntas comuns:** como achar qual processo está usando a porta 3000? Como ver as últimas linhas de um log em tempo real? Diferença entre `>` e `>>`? O que faz `chmod 755`? O que é `PATH`?

## 11. Exercícios

Sem IA. Use `man` e `--help`.

- **N1:** explique o que cada parte faz: `grep -rn "restic" docs | wc -l`.
- **N2:** crie a estrutura `~/dev/logica-ts/{src,testes}`, um arquivo em cada pasta, e liste tudo com tamanhos.
- **N3:**
  - A prática do `s-terminal` (contar os `.md` que citam "restic" num comando).
  - Ache o erro: `for f in $(ls *.md); do cat $f; done` quebra com um arquivo chamado `minhas notas.md`. Por quê? Corrija.
  - Descubra qual processo está usando uma porta e encerre-o com o sinal correto.
- **N4:** um script `resumo-dia.sh` que mostra espaço em disco, os 5 maiores arquivos de `~/dev`, o último commit de cada repositório em `~/dev` e a idade do último backup, com `set -euo pipefail`, passando no ShellCheck. Depois, decida e escreva em 3 frases se ele deveria virar Go (Go-4 da trilha de ferramentas).

## 12. Fontes (na ordem de uso)

1. **Oficial:** [Documentação do WSL](https://learn.microsoft.com/pt-br/windows/wsl/) · [Manual do Bash](https://www.gnu.org/software/bash/manual/) · `man bash` · [roadmap.sh/linux](https://roadmap.sh/linux)
2. **Akita:** [#54 Guia definitivo de Ubuntu para devs iniciantes](https://akitaonrails.com/2019/07/12/akitando-54-o-guia-definitivo-de-ubuntu-para-devs-iniciantes/) · #60 Entendendo WSL 2 · [#127 Como funciona o boot de um Linux](https://akitaonrails.com/2022/09/12/akitando-127-como-funciona-o-boot-de-um-linux-o-que-tem-num-livecd/) · [Coisas que "iniciantes" ignoram sobre PCs](https://akitaonrails.com/2025/09/14/coisas-que-iniciantes-ignoram-sobre-pcs/)
3. **Livro:** *The Linux Command Line* (William Shotts), gratuito no site do autor
4. **Seu material:** [trilha-linux-arch-profissional](../../trilha-linux-arch-profissional.md), fase 1

## 13. Como saber que dominou

- [ ] Opero um dia inteiro do setup só pelo terminal.
- [ ] Explico em 3 a 5 frases o que acontece entre apertar Enter e o comando terminar (PATH, processo filho, stdin/stdout/stderr, código de saída).
- [ ] Leio um comando proposto pela IA e digo o que ele faz antes de aprovar.
- [ ] **Registro de entrevista:** contexto (setup no WSL lento), decisão (projetos em `~/dev`), alternativa descartada (`/mnt/c`), resultado (tempo medido antes e depois).
- [ ] **N4:** dei a aula de terminal em Sistemas Operacionais. Onde e quando: ______
