# Aulas de Laboratório — Software e Hardware (3º EMTI)

Oct 20, 2026 · @Alan Mateus

## Aula 1 — Laboratório de Software: Controle de versão com Git

Os alunos saem sabendo o que é Git, as três áreas de trabalho e os 6 comandos básicos. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios).

### Roteiro da aula

1. Pergunta de abertura (5 min): "Quem já salvou um arquivo como trabalho\_final\_AGORA\_VAI\_v3.docx?"
2. Quadro + explicação (35 min): blocos A, B, C e D abaixo, nessa ordem.
3. Demonstração rápida no computador do professor, se houver projetor (10 min).
4. Exercícios no caderno (aula seguinte ou restante do tempo).

### O que escrever no quadro

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

### Pontos para falar na explicação

- **Analogia do jogo:** commit é o checkpoint. Se morrer (estragar o código), volta ao último checkpoint.
- **Analogia da foto:** o staging é arrumar as pessoas para a foto; o commit é apertar o botão.
- **Erro comum:** achar que Git e GitHub são a mesma coisa. Git funciona sem internet; GitHub é só onde o projeto fica guardado online.
- **Erro comum:** fazer commit sem dar git add antes. Nada vai para o commit se não passar pelo staging.
- **Erro comum:** mensagem "aaa" ou "mudei". Daqui a um mês ninguém sabe o que foi feito.
- **Checagem rápida (pergunte à turma):** "Editei o index.html. Qual o próximo comando para ele entrar no commit?" (git add).

### Exercícios

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

## Aula 2 — Laboratório de Hardware: Diagnóstico de falhas (POST, bipes e sintomas)

Os alunos saem sabendo o que é o POST, como ler os bipes e qual peça testar primeiro em cada sintoma. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios).

### Roteiro da aula

1. Pergunta de abertura (5 min): "O PC liga, a ventoinha gira, mas a tela fica preta. O que vocês fariam?"
2. Quadro + explicação (35 min): blocos A, B, C e D abaixo, nessa ordem.
3. Demonstração em bancada, se houver uma máquina de sucata (10 min): tire a memória RAM, ligue e deixe a turma ouvir os bipes.
4. Exercícios no caderno.

### O que escrever no quadro

**Bloco A — O que é o POST**

- POST = Power-On Self Test (autoteste ao ligar).
- É feito pela BIOS/UEFI toda vez que o computador liga.
- Testa: processador, memória RAM, placa de vídeo e teclado.
- Passou no teste → 1 bipe curto (na maioria das placas) e o sistema carrega.
- Falhou → sequência de bipes ou LED de erro na placa-mãe.

**Bloco B — Códigos de bipe comuns (BIOS AMI)**

| Bipes | Provável problema |
| --- | --- |
| 1 curto | Tudo OK |
| Nenhum bipe e nada liga | Fonte, cabo de energia ou botão |
| Bipes curtos repetidos | Memória RAM |
| 1 longo + 2 ou 3 curtos | Placa de vídeo |
| Bipe contínuo | Memória RAM ou fonte |

Anote embaixo: "Os códigos mudam de fabricante para fabricante. Sempre confira o manual da placa-mãe."

**Bloco C — Sintomas e primeiro teste**

| Sintoma | Testar primeiro |
| --- | --- |
| Não liga nada (sem luz, sem ventoinha) | Tomada, cabo, chave da fonte, fonte |
| Liga, mas tela preta | Cabo do monitor, memória RAM, placa de vídeo |
| Desliga sozinho depois de um tempo | Superaquecimento (cooler e pasta térmica) |
| Hora e data sempre erradas | Bateria da placa-mãe (CR2032) |
| "No boot device" na tela | HD/SSD ou cabo SATA |

**Bloco D — Método de diagnóstico (passo a passo)**

1. Observar: ouvir bipes, ver LEDs, ler mensagens na tela.
2. Começar pelo mais simples: cabos, tomada, conexões.
3. Testar uma peça por vez.
4. Trocar por uma peça que funciona (teste de substituição).
5. Anotar o que foi testado e o resultado.

### Pontos para falar na explicação

- **Analogia do médico:** o POST é o check-up do PC; os bipes são o PC "dizendo onde dói".
- **Regra de ouro:** do mais simples para o mais complexo. Muito "PC queimado" é só cabo solto.
- **Erro comum:** trocar várias peças de uma vez. Se funcionar, você não sabe qual era o defeito.
- **Erro comum:** mexer com o PC ligado na tomada. Sempre desligar e tirar o cabo antes de abrir.
- **Erro comum:** decorar a tabela de bipes como se fosse igual em toda placa. Ela muda por fabricante.
- **Dica prática:** limpar os contatos da memória RAM com borracha branca resolve muitos casos de tela preta.
- **Checagem rápida (pergunte à turma):** "O PC dá bipes curtos repetidos. Qual peça você tira primeiro?" (memória RAM).

### Exercícios

1. O que significa a sigla POST?
2. Quem faz o POST quando o computador liga?
3. Cite 3 componentes testados no POST.
4. Na maioria das placas, o que significa 1 bipe curto?
5. O computador dá bipes curtos repetidos. Qual peça provavelmente está com problema?
6. O computador não acende nenhuma luz e a ventoinha não gira. Cite 2 coisas para verificar primeiro.
7. A data e a hora do computador voltam sempre para 2010. Qual peça deve ser trocada?
8. O PC desliga sozinho depois de 20 minutos de uso. Qual a causa mais provável e o que deve ser verificado?
9. Aparece "No boot device" na tela. Qual componente deve ser testado?
10. Por que não se deve trocar várias peças ao mesmo tempo durante um diagnóstico?
11. Escreva, na ordem, os 5 passos do método de diagnóstico.
12. Por que é importante consultar o manual da placa-mãe ao ouvir os bipes?
13. **Desafio:** Um cliente diz: "Meu PC liga, faz barulho de ventoinha, dá 1 bipe longo e 3 curtos e a tela fica preta." Descreva o que você testaria e em que ordem.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
