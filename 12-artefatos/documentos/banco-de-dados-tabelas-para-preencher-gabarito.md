# Banco de Dados — Tabelas para Preencher (Gabarito)

Oct 21, 2026 · @Alan Mateus

Respostas de acordo com os Blocos D, E, F e G da aula de Banco de Dados. As respostas em **negrito** são as que o aluno preenche.

## Tabela 1 — Aluno

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| matricula | 1001 | **INT** | **Sim** |
| nome | Ana Souza | **VARCHAR** | **Não** |
| data\_nascimento | 2010-03-15 | **DATE** | **Não** |
| turma | 2º A | **VARCHAR** | **Não** |
| media | 8.5 | **DECIMAL** | **Não** |
| ativo | true | **BOOLEAN** | **Não** |

**(b) Registros**

| matricula | nome | data\_nascimento | turma | media | ativo |
| --- | --- | --- | --- | --- | --- |
| **1001** | **Ana Souza** | **2010-03-15** | **2º A** | **8.5** | **true** |
| **1002** | **Bruno Lima** | **2009-07-02** | **3º B** | **6.0** | **false** |

**(c)** **Dois alunos podem ter o mesmo nome, então o valor se repetiria. A matrícula é única e nunca fica vazia.**

## Tabela 2 — Professor

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| id\_professor | 15 | **INT** | **Sim** |
| nome | Carla Dias | **VARCHAR** | **Não** |
| disciplina | Banco de Dados | **VARCHAR** | **Não** |
| telefone | (32) 99999-0000 | **VARCHAR** | **Não** |
| data\_admissao | 2025-02-10 | **DATE** | **Não** |
| efetivo | false | **BOOLEAN** | **Não** |

**(b) Registros**

| id\_professor | nome | disciplina | telefone | data\_admissao | efetivo |
| --- | --- | --- | --- | --- | --- |
| **15** | **Carla Dias** | **Banco de Dados** | **(32) 99999-0000** | **2025-02-10** | **false** |
| **16** | **Diego Rocha** | **Matemática** | **(32) 98888-1111** | **2020-03-01** | **true** |

**(c)** **Como INT, o zero da frente sumiria e o campo não aceitaria parênteses nem traço. Por isso o telefone é VARCHAR.**

## Tabela 3 — Escola

**(a) Estrutura**

| Campo | Exemplo de valor | Tipo de dado | Chave primária? (Sim/Não) |
| --- | --- | --- | --- |
| codigo | 31000123 | **INT** | **Sim** |
| nome | Escola Estadual Monte Azul | **VARCHAR** | **Não** |
| cidade | Barbacena | **VARCHAR** | **Não** |
| total\_alunos | 850 | **INT** | **Não** |
| fundada\_em | 1965-08-20 | **DATE** | **Não** |
| tempo\_integral | true | **BOOLEAN** | **Não** |

**(b) Registros**

| codigo | nome | cidade | total\_alunos | fundada\_em | tempo\_integral |
| --- | --- | --- | --- | --- | --- |
| **31000123** | **Escola Estadual Monte Azul** | **Barbacena** | **850** | **1965-08-20** | **true** |
| **31000456** | **Escola Estadual Vale Verde** | **Juiz de Fora** | **420** | **1990-04-05** | **false** |

**(c)** **2 registros (linhas) e 6 campos (colunas).**

## Observações para a correção

- Aceite VARCHAR com tamanho (ex.: VARCHAR(100) para nome, VARCHAR(10) para turma, VARCHAR(15) para telefone).
- Aceite true/false escrito como TRUE/FALSE, 1/0 ou verdadeiro/falso.
- Datas: cobre o formato ano-mês-dia, que é o formato do tipo DATE. Se o aluno escrever dia/mês/ano, aponte o erro.
- Escola: o nome também poderia ser único, mas o código é a melhor chave primária porque é um número que não muda.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🏫 Trabalho na escola (EMTI): aulas, atividades e projetos](../../01-planejamento-geral/docencia-escola-emti.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
