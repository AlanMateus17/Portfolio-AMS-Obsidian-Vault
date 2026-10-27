# Aula — Banco de Dados: Conceitos básicos

Oct 20, 2026 · @Alan Mateus

Os alunos saem sabendo o que é banco de dados, o que é SGBD, as partes de uma tabela, os tipos de dados básicos e o que é chave primária. Duração sugerida: 2 aulas de 50 min (1 de quadro + explicação, 1 de exercícios). Todo o conteúdo necessário para os exercícios está nos blocos do quadro.

## Roteiro da aula

1. Pergunta de abertura (5 min): "A escola tem centenas de alunos. Como ela encontra a nota de um aluno em segundos?"
2. Quadro + explicação (40 min): blocos A a F abaixo, nessa ordem.
3. Exercícios no caderno (aula seguinte ou restante do tempo).

## O que escrever no quadro

**Bloco A — O que é banco de dados**

- Banco de dados = conjunto organizado de dados guardados para serem consultados depois.
- Exemplos do dia a dia: cadastro de alunos da escola, contatos do celular, estoque de uma loja, perfis de uma rede social.
- **Dado** = valor solto, sem significado. Ex.: "17".
- **Informação** = dado com significado. Ex.: "Idade do aluno: 17 anos".

**Bloco B — SGBD e SQL**

- **SGBD** = Sistema Gerenciador de Banco de Dados.
- É o programa que cria, guarda, altera e consulta o banco de dados.
- Exemplos de SGBD: MySQL, PostgreSQL, SQL Server, SQLite.
- **Banco relacional** = guarda os dados em tabelas.
- **SQL** = linguagem usada para "conversar" com o banco (criar tabelas, inserir e buscar dados).

**Bloco C — Partes de uma tabela**

- **Tabela** = conjunto de dados sobre um mesmo assunto. Ex.: tabela Alunos.
- **Registro** = cada linha da tabela (um aluno).
- **Campo** = cada coluna da tabela (uma característica: nome, idade...).

Copie a tabela de exemplo:

**T****,****abela: Alunos**

| id | nome | idade | turma |
| --- | --- | --- | --- |
| 1 | Ana Souza | 16 | 2º A |
| 2 | Bruno Lima | 17 | 2º A |
| 3 | Carla Dias | 16 | 2º B |

Anote embaixo: "Esta tabela tem 3 registros (linhas) e 4 campos (colunas)."

**Bloco D — Tipos de dados**

Cada campo tem um tipo, que diz que tipo de valor ele aceita.

| Tipo | Guarda | Exemplo |
| --- | --- | --- |
| INT | Números inteiros | idade: 16 |
| VARCHAR(n) | Texto com até n caracteres | nome: "Ana Souza" |
| DATE | Datas | nascimento: 2010-03-15 |
| DECIMAL | Números com casas decimais | preço: 19.90 |
| BOOLEAN | Verdadeiro ou falso | ativo: true |

**Bloco E — Chave primária**

- Chave primária = campo que identifica cada registro de forma única.
- Regra 1: o valor não pode se repetir.
- Regra 2: o valor não pode ficar vazio.
- Bons exemplos: id, matrícula, CPF.
- Na tabela Alunos, a chave primária é o campo **id**.

**Bloco F — Analogias, erros comuns e pergunta para a turma**

- Analogia do arquivo de aço: banco de dados = o arquivo inteiro; tabela = uma gaveta; registro = uma ficha dentro da gaveta; campo = cada espaço a preencher na ficha.
- Erro 1: usar o nome como chave primária → dois alunos podem ter o mesmo nome, então o valor se repete.
- Erro 2: guardar telefone como INT → o zero da frente some e não aceita parênteses ou traço. Telefone deve ser VARCHAR.
- Erro 3: achar que banco de dados e SGBD são a mesma coisa → o banco são os dados; o SGBD é o programa que cuida deles.
- Pergunta: na tabela Alunos, o campo turma pode ser chave primária?

## Exercícios

1. O que é um banco de dados?
2. Cite 2 exemplos de banco de dados do dia a dia.
3. Qual a diferença entre dado e informação? Dê um exemplo de cada.
4. O que significa a sigla SGBD?
5. Cite 2 exemplos de SGBD.
6. O que é SQL?
7. O que é um registro? E o que é um campo?
8. Quantos registros e quantos campos tem a tabela Alunos do quadro?
9. Qual tipo de dado você usaria para guardar: (a) a idade, (b) o nome, (c) a data de nascimento, (d) o preço de um produto?
10. O que é chave primária? Escreva as 2 regras dela.
11. Por que o nome do aluno não é uma boa chave primária?
12. Por que o telefone deve ser guardado como VARCHAR e não como INT?
13. Usando a analogia do arquivo de aço, explique o que é tabela, registro e campo.
14. **Desafio:** Crie no caderno uma tabela chamada Produtos com 4 campos. Escreva o tipo de dado de cada campo, indique qual é a chave primária e preencha 2 registros.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
