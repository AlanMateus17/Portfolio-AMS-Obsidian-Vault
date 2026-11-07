# Engenharia reversa com IA

[← Segurança](README.md)

Engenharia reversa é ler um programa compilado para entender o que ele faz sem ter o código-fonte. Para você ela serve a três coisas: estudar como compiladores e sistemas operacionais funcionam de verdade, mostrar aos alunos o caminho do código até a máquina, e descobrir o que um atacante enxerga nos **seus** programas.

## O laboratório

| Ferramenta | Para quê | Onde |
|---|---|---|
| Compiler Explorer (godbolt.org) | Ver o C virar assembly ao vivo | Navegador |
| `strings`, `objdump`, `file`, `xxd` | Primeira olhada: textos, seções, cabeçalho | Ubuntu (WSL) |
| `strace`, `ltrace`, `gdb` | Ver o programa rodando: chamadas de sistema, de biblioteca e passo a passo | Ubuntu (WSL) |
| Ghidra (NSA) | Desmontar e descompilar para um pseudo-C | Ubuntu (WSLg abre a janela) |
| ILSpy / `ilspycmd` | Descompilar .NET: o C# volta quase igual | Windows (ILSpy) ou Ubuntu (`ilspycmd`) |
| GhidraMCP | O Claude lê, renomeia e explica funções dentro do Ghidra | Ghidra + cliente MCP |

Instalação: `bash scripts/wsl/ferramentas-re.sh` (passo sg-ferramentas). Rode antes com `--simular`.

## Onde a IA entra

O trabalho lento da engenharia reversa é dar sentido a funções chamadas `FUN_00101169` com variáveis `local_48`. A IA acelera exatamente isso:

1. Você abre o binário no Ghidra e deixa a análise automática rodar.
2. O GhidraMCP expõe ao Claude as funções, as strings, os imports e o pseudo-C.
3. Você pede: "liste as funções, ache a que confere a licença, renomeie e explique o fluxo".
4. Você **confere** cada renomeação no pseudo-C. A IA erra com confiança; o Ghidra é a fonte da verdade.

### Ligar o GhidraMCP (passo sg-ghidramcp)

1. No Ghidra: `File > Install Extensions > +` e escolha o `.zip` baixado em `~/ferramentas/ghidramcp`. Reinicie o Ghidra.
2. Em `File > Configure > Developer`, marque o `GhidraMCPPlugin`. Ele abre um servidor local na porta 8080 (muda em `Edit > Tool Options > GhidraMCP HTTP Server`).
3. No cliente MCP (Claude Code ou Claude Desktop), cadastre a ponte em Python que vem no pacote, apontando para `http://127.0.0.1:8080/`. O README do projeto (github.com/LaurieWired/GhidraMCP) traz o bloco de configuração de cada cliente; a ponte precisa dos pacotes `mcp` e `requests` (`uv run --with mcp --with requests bridge_mcp_ghidra.py`).
4. Teste com o crackme da aula: peça ao Claude para listar as funções do `licenca`.

**Binário de cliente:** nunca mande para IA na nuvem. Use o mesmo fluxo com um modelo local pelo Ollama (bloco `oll`) e só se o contrato permitir análise com ferramenta automatizada.

## Trilha de exercícios (1 h por semana)

| Semana | Exercício | O que aprende |
|---|---|---|
| 1 | Crackme da aula em C (`infra/templates/seguranca/aula-re/licenca.c`), com `strings` e depois Ghidra | Segredo no binário aparece em texto puro |
| 2 | O mesmo em C# no ILSpy | .NET é quase código-fonte; ofuscação só atrasa |
| 3 | Mesmo C com `-O0` e `-O2` no Compiler Explorer | O que o otimizador faz com o seu código |
| 4 | `strace` e `ltrace` num programa seu | Que arquivos, rede e bibliotecas ele usa |
| 5 a 8 | Android UnCrackable L1 e L2 (OWASP MAS) | Engenharia reversa de app, com soluções da comunidade para comparar |
| 9 em diante | crackmes.one por dificuldade | Ritmo próprio; anote cada um no Obsidian como writeup |

## Da engenharia reversa ao pentest, no seu laboratório

A engenharia reversa mostra onde procurar; o pentest prova se dá para explorar. O setup junta os dois num ciclo:

1. **Estudar:** o programa abre no Ghidra ou no ILSpy, com o Claude pelo GhidraMCP. Onde confere senha e licença, que dados guarda, com quem fala na rede.
2. **Isolar:** uma cópia dele roda numa rede **sem internet**, só com o atacante.
   - Sistema web ou API: `bash scripts/wsl/lab-alvo.sh subir` (containers). Outro alvo: `ALVO_IMAGEM=imagem ALVO_PORTA=porta` antes do comando.
   - Programa de desktop ou binário de Windows: VMs `Kali` e `Alvo` no VirtualBox, isoladas com `scripts/windows/lab-alvo.ps1 -Acao isolar`, foto do estado limpo com `-Acao snapshot` e volta com `-Acao restaurar`.
3. **Provar o isolamento antes de atacar:** `bash scripts/wsl/lab-alvo.sh verificar` (ou `-Acao status` nas VMs). Se algo sair para a internet, o script avisa.
4. **Atacar:** `bash scripts/wsl/lab-alvo.sh entrar` abre o terminal do atacante (nmap, sqlmap, ffuf, nikto, gobuster); Burp e ZAP ficam na VM Kali.
5. **Relatar:** os achados vão para o `tools/seguranca/relatorio.py`.

### O que pode entrar no laboratório

| Situação | Pode? |
|---|---|
| Software seu (AM Kaixara, sites, o crackme da aula) | Sim, e é o melhor uso |
| Desafios e apps feitos para isso (crackmes, Juice Shop, WebGoat, OWASP MAS) | Sim |
| Software de código aberto | Sim. Falha real achada: aviso em particular ao projeto antes de publicar |
| Programa comercial instalado no seu PC | Depende da licença; quebrar proteção para usar sem pagar é crime |
| Sistema de cliente | Só com termo assinado, passando pela guarda `escopo.py` |
| Servidor, site ou app online de outra empresa | **Não.** Sem autorização escrita é crime (Lei 12.737/2012); o laboratório roda só cópias na sua máquina |

## A aula para os alunos (passo sg-aula)

Encaixa em Arquitetura e Manutenção de Computadores (e serve de ponte para Lógica e POO):

1. **Do C ao assembly** (15 min): o `licenca.c` no Compiler Explorer, apontando `main`, a chamada a `strcmp` e a constante.
2. **De volta** (20 min): cada aluno compila o próprio `licenca` e procura a chave com `strings`. Depois, quem quiser abre no Ghidra.
3. **Discussão** (15 min): por que a checagem de licença, de senha ou de preço tem que ficar no servidor?

Regra da turma, dita no início: só analisamos binários que nós mesmos compilamos. Nada de dado de aluno em IA.

## Como usar nos seus próprios sistemas

Faça engenharia reversa do que você publica antes que alguém faça:

- **Front-end (Next.js):** abra o bundle publicado nas ferramentas do navegador. Procure chave de API, regra de preço ou de permissão. Tudo que estiver lá, o cliente pode mudar.
- **Desktop ou PDV (.NET, MAUI):** abra a `.dll` no ILSpy. Se aparecer connection string, chave ou regra de licença, mova para o servidor.
- **Licenciamento (aura-licensing):** a decisão "pode usar o módulo" vem assinada do servidor; o cliente só confere a assinatura com a chave pública.
- **Dependências:** saber ler um binário ajuda a investigar pacote suspeito, como os casos de bibliotecas comprometidas no npm e no NuGet.

## O que é legal e o que não é

- Estudar binário seu, de crackme ou de desafio: legal.
- Analisar software de terceiro para interoperabilidade ou segurança tem regras próprias na Lei 9.609/98 e na licença de cada programa; na dúvida, não faça e pergunte a um advogado.
- Quebrar proteção de software pago, de streaming ou de jogo para usar sem pagar: crime e quebra de contrato, sem exceção para "estudo". Esta frente não cobre isso.
