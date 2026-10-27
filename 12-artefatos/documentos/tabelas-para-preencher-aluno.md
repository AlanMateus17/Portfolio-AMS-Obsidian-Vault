# Banco de Dados — Tabelas para Preencher (Aluno)

Oct 21, 2026 · @Alan Mateus

Preencha os espaços em branco usando o conteúdo que o professor passou no quadro.

Nome: ..................................................   Turma: ..............   Data: ...... / ...... / ............

Para cada tabela: (a) escreva o tipo de dado de cada campo e marque qual é a chave primária; (b) leia o texto e preencha os registros. Datas no formato ano-mês-dia.

## Tabela 1 — Aluno

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| matricula | 1001 | ............ | ............ |
| nome | Ana Souza | ............ | ............ |
| data\_nascimento | 2010-03-15 | ............ | ............ |
| turma | 2º A | ............ | ............ |
| media | 8.5 | ............ | ............ |
| ativo | true | ............ | ............ |

**(b) Registros** — A aluna Ana Souza, matrícula 1001, nasceu em 15/03/2010, é do 2º A, tem média 8.5 e está ativa. O aluno Bruno Lima, matrícula 1002, nasceu em 02/07/2009, é do 3º B, tem média 6.0 e não está mais ativo.

| matricula | nome | data\_nascimento | turma | media | ativo |
| --- | --- | --- | --- | --- | --- |
| ...... | ............ | ............ | ...... | ...... | ...... |
| ...... | ............ | ............ | ...... | ...... | ...... |

**(c)** Por que a matrícula é uma chave primária melhor que o nome? ....................................................................

## Tabela 2 — Professor

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| id\_professor | 15 | ............ | ............ |
| nome | Carla Dias | ............ | ............ |
| disciplina | Banco de Dados | ............ | ............ |
| telefone | (32) 99999-0000 | ............ | ............ |
| data\_admissao | 2025-02-10 | ............ | ............ |
| efetivo | false | ............ | ............ |

**(b) Registros** — A professora Carla Dias (id 15) dá aula de Banco de Dados, tem o telefone (32) 99999-0000, foi admitida em 10/02/2025 e não é efetiva. O professor Diego Rocha (id 16) dá aula de Matemática, tem o telefone (32) 98888-1111, foi admitido em 01/03/2020 e é efetivo.

| id\_professor | nome | disciplina | telefone | data\_admissao | efetivo |
| --- | --- | --- | --- | --- | --- |
| ...... | ............ | ............ | ............ | ............ | ...... |
| ...... | ............ | ............ | ............ | ............ | ...... |

**(c)** Por que o telefone não pode ser guardado como INT? ....................................................................

## Tabela 3 — Escola

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| codigo | 31000123 | ............ | ............ |
| nome | Escola Estadual Monte Azul | ............ | ............ |
| cidade | Barbacena | ............ | ............ |
| total\_alunos | 850 | ............ | ............ |
| fundada\_em | 1965-08-20 | ............ | ............ |
| tempo\_integral | true | ............ | ............ |

**(b) Registros** — A Escola Estadual Monte Azul, código 31000123, fica em Barbacena, tem 850 alunos, foi fundada em 20/08/1965 e é de tempo integral. A Escola Estadual Vale Verde, código 31000456, fica em Juiz de Fora, tem 420 alunos, foi fundada em 05/04/1990 e não é de tempo integral.

| codigo | nome | cidade | total\_alunos | fundada\_em | tempo\_integral |
| --- | --- | --- | --- | --- | --- |
| ...... | ............ | ............ | ...... | ............ | ...... |
| ...... | ............ | ............ | ...... | ............ | ...... |

**(c)** Quantos registros e quantos campos tem a tabela Escola que você preencheu? ....................................................................

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
