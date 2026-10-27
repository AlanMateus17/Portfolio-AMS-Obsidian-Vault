# Aula — Banco de Dados: Conceitos, tipos de banco e primeiros comandos SQL

Oct 21, 2026 · @Alan Mateus

Aula introdutória que serve às duas turmas de banco de dados: cobre os conceitos e os tipos de banco (TDS 2º ano) e os primeiros comandos SQL executados no phpMyAdmin (Informática 3º ano). O exemplo usado é a tabela de carteiras da casa de apostas BSD, a mesma cujo backup a turma do 3º ano faz em Laboratório de Software. Duração sugerida: 3 aulas de 50 min (Blocos A–D, Blocos E–G e exercícios). Tudo o que os exercícios cobram está escrito no quadro.

## Alinhamento

| Item da ementa | Turma | Bloco desta aula |
| --- | --- | --- |
| Conceitos e tipos de banco de dados (hierárquico, relacional, orientado a objetos, georreferenciado, NoSQL) | TDS 2º ano | A e B |
| Implantação e manutenção de SGBD | TDS 2º ano | C |
| Tipos de dados | TDS 2º ano | E |
| Ferramentas de acesso a banco remoto (phpMyAdmin) | Informática 3º ano | C |
| Execução de códigos SQL | Informática 3º ano | F |
| Projeto BSD (3º ano) | Informática 3º ano | D, E e F (tabela carteiras) |

Não há apostilas de banco de dados no repositório, então este é conteúdo novo para as duas turmas.

## Roteiro da aula

1. Pergunta de abertura (5 min): "A casa de apostas precisa guardar o saldo de cada carteira. Onde e como esse saldo fica guardado?"
2. Aula 1 — Blocos A a D no quadro (45 min).
3. Aula 2 — Blocos E a G no quadro (45 min). Se houver laboratório com XAMPP, execute os comandos SQL do Bloco F no phpMyAdmin.
4. Aula 3 — Exercícios no caderno.

## O que escrever no quadro

**Bloco A — O que é banco de dados**

- Banco de dados = conjunto organizado de dados guardados para serem consultados depois.
- Exemplos: cadastro de alunos da escola, contatos do celular, estoque de uma loja, carteiras da casa de apostas BSD.
- **Dado** = valor solto, sem significado. Ex.: "500000".
- **Informação** = dado com significado. Ex.: "Saldo da carteira BSD1a3: 500.000 PRIMEs".

**Bloco B — Tipos de banco de dados**

| Tipo | Como organiza os dados | Exemplo |
| --- | --- | --- |
| Hierárquico | Em árvore: cada registro "pai" tem vários "filhos" | Organograma de uma empresa |
| Relacional | Em tabelas com linhas e colunas | MySQL, PostgreSQL |
| Orientado a objetos | Guarda objetos, como na POO (atributos e métodos) | db4o, ObjectDB |
| NoSQL | Sem tabelas fixas: documentos, chave-valor ou grafos | MongoDB, Redis |
| Georreferenciado | Dados com localização (coordenadas e mapas) | PostGIS, sistemas de GPS |

- Nesta aula vamos usar o **relacional**, o tipo mais usado.

**Bloco C — SGBD, SQL e phpMyAdmin**

- **SGBD** = Sistema Gerenciador de Banco de Dados: o programa que cria, guarda, altera e consulta o banco.
- Exemplos de SGBD: MySQL, PostgreSQL, SQL Server, SQLite.
- **SQL** = linguagem usada para conversar com o banco (criar tabelas, inserir e buscar dados).
- **phpMyAdmin** = ferramenta que abre no navegador para acessar e administrar um banco MySQL, inclusive em um servidor remoto.
- **XAMPP** = pacote que instala o MySQL e o phpMyAdmin no computador.

**Bloco D — Partes de uma tabela**

- **Tabela** = conjunto de dados sobre um mesmo assunto.
- **Registro** = cada linha (uma carteira).
- **Campo** = cada coluna (uma característica da carteira).

**Tabela: carteiras**

| id | apelido | saldo\_primes | ativa |
| --- | --- | --- | --- |
| 1 | BSD1a3 | 500000 | true |
| 2 | BSD7f2 | 120000 | true |
| 3 | BSD9c4 | 0 | false |

Anote embaixo: "Esta tabela tem 3 registros (linhas) e 4 campos (colunas)."

**Bloco E — Tipos de dados**

| Tipo | Guarda | Exemplo |
| --- | --- | --- |
| INT | Números inteiros (até cerca de 2,1 bilhões) | id: 1 |
| BIGINT | Números inteiros muito grandes | saldo\_primes: 500000 |
| VARCHAR(n) | Texto com até n caracteres | apelido: "BSD1a3" |
| DATE | Datas (ano-mês-dia) | criada\_em: 2026-10-21 |
| DECIMAL | Números com casas decimais | preço: 19.90 |
| BOOLEAN | Verdadeiro ou falso | ativa: true |

- Por que o saldo é BIGINT: 1 BSD = 100.000.000 PRIMEs. Uma carteira com 100 BSD já tem 10 bilhões de PRIMEs, valor maior que o limite do INT.

**Bloco F — Chave primária e os primeiros comandos SQL**

- **Chave primária** = campo que identifica cada registro de forma única.
- Regra 1: o valor não pode se repetir. Regra 2: o valor não pode ficar vazio.
- Na tabela carteiras, a chave primária é o **id**.

```
CREATE TABLE carteiras (
  id INT PRIMARY KEY,
  apelido VARCHAR(30),
  saldo_primes BIGINT,
  ativa BOOLEAN
);

INSERT INTO carteiras VALUES (1, 'BSD1a3', 500000, true);

SELECT * FROM carteiras;

SELECT apelido FROM carteiras WHERE saldo_primes > 100000;
```

| Comando | O que faz |
| --- | --- |
| CREATE TABLE | Cria uma tabela com seus campos e tipos |
| INSERT INTO | Insere um registro novo |
| SELECT \* FROM | Mostra todos os campos de todos os registros |
| WHERE | Filtra os registros por uma condição |

**Bloco G — Analogias, erros comuns e pergunta para a turma**

- Analogia do arquivo de aço: banco de dados = o arquivo inteiro; tabela = uma gaveta; registro = uma ficha; campo = cada espaço a preencher na ficha.
- Erro 1: usar o apelido ou o nome como chave primária → o valor pode se repetir.
- Erro 2: guardar telefone como INT → o zero da frente some e não aceita parênteses ou traço. Telefone é VARCHAR.
- Erro 3: guardar o saldo em PRIMEs como INT → estoura o limite. Use BIGINT.
- Erro 4: achar que banco de dados e SGBD são a mesma coisa → o banco são os dados; o SGBD é o programa que cuida deles.
- Pergunta: qual comando mostra só as carteiras ativas?

## Exercícios

1. O que é um banco de dados? Cite 2 exemplos.
2. Qual a diferença entre dado e informação? Dê um exemplo de cada.
3. Cite os 5 tipos de banco de dados e como cada um organiza os dados.
4. Qual tipo de banco usa tabelas com linhas e colunas? Cite 2 exemplos.
5. Qual tipo de banco você usaria para um aplicativo de mapas? Por quê?
6. O que significa a sigla SGBD? Cite 2 exemplos.
7. O que é SQL?
8. Para que serve o phpMyAdmin? E o XAMPP?
9. O que é um registro? E um campo?
10. Quantos registros e quantos campos tem a tabela carteiras do quadro?
11. Qual tipo de dado você usaria para: (a) o id, (b) o apelido, (c) a data de criação, (d) o saldo em PRIMEs, (e) se a carteira está ativa?
12. Por que o saldo em PRIMEs não pode ser INT?
13. O que é chave primária? Escreva as 2 regras.
14. Por que o apelido não é uma boa chave primária?
15. O que faz cada comando: CREATE TABLE, INSERT INTO, SELECT \* FROM e WHERE?
16. Escreva o comando que insere a carteira 2 (BSD7f2, saldo 120000, ativa).
17. Escreva o comando que mostra o apelido das carteiras com saldo maior que 100000.
18. **Desafio:** Crie no caderno uma tabela apostas com 4 campos (id, carteira\_id, valor\_primes, resultado). Escreva o tipo de cada campo, indique a chave primária, escreva o CREATE TABLE e um INSERT com uma aposta.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
