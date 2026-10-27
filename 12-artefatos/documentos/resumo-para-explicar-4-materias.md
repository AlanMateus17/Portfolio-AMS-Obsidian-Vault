# Resumo para Explicar — 4 Matérias

Oct 27, 2026 · @Alan Mateus

Um resumo por matéria, com o que é mais importante falar em sala. Cada um segue a aula completa que já está pronta.

## 1. Laboratório de Software — Terminal, segurança e recuperação

**Ideia central:** o técnico controla o sistema pelo terminal, protege o que é importante e sabe recuperar tudo quando algo quebra. Tudo aplicado na casa de apostas BSD.

**Os 6 pontos para falar**

1. **Terminal:** pwd (onde estou), ls -la (o que tem aqui), cd (entrar/sair), mkdir, cp, mv, rm. No terminal não tem lixeira.
2. **Pipes e filtros:** o | liga um comando no outro. grep "PERDEU" apostas.log | wc -l conta as apostas perdidas. > grava apagando; >> acrescenta.
3. **Permissões:** r = 4, w = 2, x = 1. chmod 600 na chave privada = só o dono lê e escreve. Quem lê a chave gasta os PRIMEs.
4. **Script e backup:** o backup.sh copia o banco com a data no nome. chmod +x para executar. Regra 3-2-1: 3 cópias, 2 mídias, 1 fora do local.
5. **VM e imagem:** VM = computador dentro do computador; snapshot = foto para voltar depois. Imagem de sistema = cópia do disco inteiro (Clonezilla, dd).
6. **Segurança e falhas:** diretivas no gpedit.msc; firewall com ufw (liberar a porta, depois ligar). Disco com erro: chkdsk (Windows) e fsck (Linux).

**Git (adicional):** Trabalho → git add → Staging → git commit → Repositório → git push → GitHub. A chave privada vai no .gitignore.

**Frase para fechar:** "Backup guarda os dados, commit guarda o código, imagem guarda o disco inteiro."

**Pergunta rápida para a turma:** "Editei o backup.sh. Qual comando coloca ele no próximo commit?" (git add)

## 2. Laboratório de Hardware — Segurança, medição, montagem e diagnóstico

**Ideia central:** antes de mexer, proteger a pessoa e a peça; depois montar na ordem certa, medir e diagnosticar com método. Tudo aplicado na máquina de validação do projeto BSD.

**Os 6 pontos para falar**

1. **Bancada segura:** desligar e tirar da tomada (NR-12), tirar anéis e relógio, pulseira e manta ligadas ao terra, parafusos separados.
2. **Aterramento e ESD:** o fio terra leva para o chão a corrente de fuga e a estática. Na tomada, o terra é o pino do meio. 10 V já podem queimar um chip; a gente só sente acima de 3.000 V.
3. **Multímetro na fonte:** escala VDC, ponta preta no fio preto. Amarelo +12 V, vermelho +5 V, laranja +3,3 V, preto 0 V.
4. **Consumo:** P = V × I. Medir em repouso e sob estresse. Fonte = consumo sob estresse + 20% (250 W → 300 W).
5. **Montagem:** de fora para dentro: CPU, cooler, RAM e M.2 fora do gabinete; espaçadores antes da placa-mãe; GPU por último. SSD NVMe é o mais rápido. Drive = peça; driver = programa.
6. **Diagnóstico:** POST = check-up ao ligar. Bipes curtos repetidos = RAM. Boot mínimo = placa-mãe + CPU + 1 pente de RAM, devolvendo uma peça por vez. Nunca trocar várias peças juntas.

**Frase para fechar:** "Do mais simples para o mais complexo: muito PC 'queimado' é só cabo solto."

**Pergunta rápida para a turma:** "A máquina desliga sozinha depois de 20 minutos de estresse. O que você verifica primeiro?" (temperatura e cooler, depois a potência da fonte)

## 3. Sistemas Operacionais — Conceitos, kernel e processos

**Ideia central:** o SO é a ponte entre o hardware e os programas. Sem ele o computador liga, mas nada funciona.

**Os 6 pontos para falar**

1. **O que é:** software que gerencia os recursos do PC. Camadas: Usuário → Aplicativos → SO → Hardware. Abstração = esconder a complexidade dos circuitos.
2. **Tipos:** código aberto = Linux e Android. Proprietário = Windows, macOS e iOS. O Android é baseado no Linux.
3. **As 5 funções:** gerenciar processos, memória, armazenamento, dispositivos e a interface com o usuário.
4. **Kernel:** o núcleo do SO, primeiro a ligar e último a desligar. Modo Usuário (app trava sozinho) x Modo Kernel (trava tudo: tela azul ou kernel panic). System Call = o pedido do app ao kernel.
5. **Interface e driver:** GUI = janelas e mouse; CLI = comandos digitados. Driver = tradutor entre o SO e a peça.
6. **Processos:** programa = parado no disco; processo = em execução. Escalonamento organiza quem usa a CPU; multitarefa = alternar tão rápido que parece simultâneo. Ver: Ctrl + Shift + Esc (Windows) e htop (Linux).

**Analogias:** o SO é o maestro da orquestra. A System Call é o balcão de um banco blindado: o app não entra no cofre, ele faz o pedido e o kernel busca.

**Frase para fechar:** "Chrome e Word não são sistemas operacionais; eles rodam em cima do SO."

**Pergunta rápida para a turma:** "Um aplicativo travou no Modo Usuário. O computador inteiro trava?" (não, só o aplicativo fecha)

## 4. Banco de Dados — Conceitos, tabelas, chaves e SQL

**Ideia central:** banco de dados guarda informação organizada para achar rápido. No relacional, cada assunto fica na sua tabela e as tabelas se ligam pelas chaves.

**Os 7 pontos para falar**

1. **Dado x informação:** "500000" é dado; "saldo da carteira BSD1a3: 500.000 PRIMEs" é informação.
2. **Tipos de banco:** hierárquico (árvore), relacional (tabelas), orientado a objetos, NoSQL (documentos, chave-valor) e georreferenciado (mapas).
3. **SGBD e SQL:** SGBD é o programa que cuida do banco (MySQL). SQL é a linguagem para conversar com ele. phpMyAdmin acessa o banco pelo navegador.
4. **Tabela:** registro = linha; campo = coluna.
5. **Tipos de dados:** INT (inteiro), BIGINT (inteiro gigante, como o saldo em PRIMEs), VARCHAR (texto, inclusive telefone), DATE (ano-mês-dia), DECIMAL (casas decimais), BOOLEAN (verdadeiro ou falso).
6. **Chave primária:** identifica cada registro. Não repete, não fica vazia, não muda. Ex.: matrícula, nunca o nome.
7. **Chave estrangeira:** liga duas tabelas. O aluno guarda o id\_turma, sem repetir a sala e o regente em cada linha. Uma turma tem muitos alunos (1 para N).

**Comandos SQL básicos:** CREATE TABLE (cria), INSERT INTO (insere), SELECT \* FROM (mostra), WHERE (filtra), JOIN (junta duas tabelas).

**Analogia:** o banco é um arquivo de aço; a tabela é a gaveta; o registro é a ficha; o campo é cada espaço da ficha.

**Frase para fechar:** "Cada informação em um lugar só: mudou a sala da turma, muda uma linha, não trinta."

**Pergunta rápida para a turma:** "Por que o nome do aluno não pode ser a chave primária?" (pode se repetir)

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
