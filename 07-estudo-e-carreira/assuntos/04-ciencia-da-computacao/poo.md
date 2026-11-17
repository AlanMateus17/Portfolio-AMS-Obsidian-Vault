---
tags: [estudo, assunto, ciencia-da-computacao, paradigmas]
area: 04 · Ciência da computação
nivel-alvo: N4
quando: T1 (classes, M1–M3) · T4 (design, M10)
professor: o-csharp (classes e erros em TypeScript)
prereq: [logica-de-programacao, typescript-fundamentos]
status: a-estudar
atualizado: 2026-11-17
---

# Programação orientada a objetos (POO)

> **Em uma frase:** POO é organizar o programa em **objetos**, cada um juntando **dados** e o **comportamento** que cuida desses dados, e fazer esses objetos colaborarem por meio de **mensagens** (chamadas de método).
> **Nível-alvo:** N4. Não basta saber criar classe: você precisa decidir **quando** usar objetos, quando usar funções simples, e revisar o design que a IA gerar.
> **Os 20% que resolvem 80%:** (1) encapsular uma regra dentro do objeto que a protege; (2) polimorfismo por interface no lugar de `if/switch`; (3) composição antes de herança; (4) objeto de valor imutável; (5) injeção de dependência para testar.

---

## 1. Por que isso existe (o problema e a história)

Nos anos 60, os programas cresciam e o código virava uma sopa de dados globais mexidos por qualquer função. Mudar uma variável quebrava algo do outro lado do sistema. A pergunta era: **como manter juntos os dados e as regras que valem para eles?**

- **Simula 67** (Noruega, Ole-Johan Dahl e Kristen Nygaard) foi criada para **simulação**: navios, filas, clientes. Ela introduziu **objetos, classes, herança e subclasses**, e já tinha coletor de lixo. Java, décadas depois, não inventou nada disso.
- **Smalltalk** (Xerox PARC, anos 70, equipe de Alan Kay) popularizou o nome "orientação a objetos" e pôs o foco nas **mensagens**: um objeto pede algo ao outro e não sabe como o outro faz. Para Kay, a ideia central era essa troca de mensagens, mais do que as classes.
- **CLU** (MIT, Barbara Liskov, 1974) trouxe os **tipos abstratos de dados**: o que importa é o que o tipo promete, não como ele guarda os dados. Daí vem o "L" do SOLID (princípio de substituição de Liskov).
- **C++** (Bjarne Stroustrup, anos 80) levou objetos para o C, com desempenho de máquina. **Java** (1995) e **C#** (2000) tornaram POO o padrão da indústria corporativa.
- **JavaScript** seguiu outro caminho: objetos com **protótipos**, sem classes. A palavra `class` só chegou em 2015, e por baixo continua sendo protótipo.

**A lição do Akita aqui:** nenhuma linguagem e nenhum paradigma surgem do nada. Toda linguagem é herdeira de outras, e quem conhece a origem entende por que as coisas são como são e para onde vão. POO é uma ferramenta, não uma religião.

## 2. O que é

Os **4 pilares** clássicos:

| Pilar | O que é | Exemplo no AM Gestão |
|---|---|---|
| **Abstração** | Mostrar só o que importa e esconder o resto | `Pagamento` tem `confirmar()`; quem chama não sabe se é Pix ou cartão |
| **Encapsulamento** | O objeto protege o próprio estado; ninguém de fora deixa ele inválido | `Pedido` não aceita item com quantidade zero ou negativa |
| **Herança** | Uma classe reaproveita e especializa outra ("é um") | `PagamentoPix extends PagamentoBase` (use com cuidado, ver seção 6) |
| **Polimorfismo** | O mesmo pedido gera comportamentos diferentes conforme o objeto | `pagamento.confirmar()` faz uma coisa no Pix e outra no cartão |

Os conceitos que o mercado espera junto com os pilares: **classe e objeto**, **interface** (o contrato), **composição** ("tem um"), **coesão e acoplamento**, **injeção de dependência** e os princípios **SOLID**.

## 3. Como funciona por baixo

- Um **objeto** na memória é um bloco de dados (os campos) mais um jeito de achar os métodos dele.
- Um **método** é só uma função que recebe o objeto como parâmetro escondido: `pedido.total()` é, por baixo, algo como `total(pedido)`. Esse parâmetro é o `this` (`self` em Python).
- **Polimorfismo** funciona por **despacho dinâmico**: na hora da chamada, o programa olha qual é o objeto de verdade e acha o método certo.
  - Em C++, Java e C#, isso usa uma **tabela de métodos virtuais** (vtable): cada classe tem uma tabela de ponteiros para funções.
  - Em **JavaScript/TypeScript**, usa a **cadeia de protótipos**: se o objeto não tem o método, o motor procura no protótipo, depois no protótipo do protótipo, até achar ou chegar em `null`. `class` é uma forma mais bonita de escrever isso.
  - Em **Go** não há classes nem herança. Há `struct` com métodos e **interfaces implícitas**: um tipo satisfaz a interface só por ter os métodos certos, sem declarar `implements`.
- **Custo:** o despacho dinâmico custa um pouco mais que uma chamada direta, mas isso quase nunca importa. O que pesa de verdade é criar objetos demais em laços apertados e a pressão sobre o coletor de lixo (episódios de memória do Akita, #45 e #46).

## 4. Conceitos que você precisa dominar

- [ ] **Classe × objeto:** a classe é a receita; o objeto é o bolo.
- [ ] **Construtor** e estado inicial válido (o objeto nunca nasce quebrado).
- [ ] **Modificadores de acesso:** `public`, `private`, `protected`, `readonly`; e `#campo` (privado de verdade em JavaScript).
- [ ] **Interface × classe abstrata:** contrato puro × contrato com parte da implementação.
- [ ] **Herança × composição:** "é um" × "tem um". Prefira composição.
- [ ] **Polimorfismo por interface** substituindo `switch` sobre tipo.
- [ ] **Objeto de valor:** imutável, comparado pelo valor (ex.: `Dinheiro`, `Cpf`, `Email`).
- [ ] **Entidade:** tem identidade que dura no tempo (ex.: `Pedido #123`).
- [ ] **Coesão** (cada classe faz uma coisa) e **acoplamento** (quanto uma depende da outra).
- [ ] **Injeção de dependência:** o objeto recebe o que precisa em vez de criar.
- [ ] **SOLID:** SRP, OCP, LSP, ISP, DIP (detalhe no assunto próprio, M10).
- [ ] **Tell, don't ask:** peça para o objeto fazer, em vez de pegar os dados dele e decidir fora.
- [ ] **Lei de Deméter:** fale só com os vizinhos próximos (`pedido.cliente.endereco.cidade.nome` é um alerta).
- [ ] **`this` em JavaScript:** como ele se perde em callbacks e como `=>` resolve.
- [ ] **Tipagem estrutural do TypeScript:** dois tipos com a mesma forma são compatíveis, mesmo sem `implements`.

## 5. Qualidades

- **Protege regras de negócio:** a regra mora num lugar só. Se `Pedido` valida a quantidade, nenhum caminho do sistema cria pedido inválido.
- **Troca de comportamento sem mexer em quem usa:** criar `PagamentoBoleto` não exige mudar o caixa (aberto para extensão, fechado para modificação).
- **Testável:** com interfaces e injeção de dependência, você troca a impressora fiscal real por uma falsa no teste.
- **Modela bem domínios com estado e regras:** pedidos, caixa, estoque, contas.
- **Vocabulário comum de equipe:** padrões de projeto, DDD e frameworks como NestJS falam essa língua.

## 6. Defeitos, limites e críticas

- **Herança é frágil.** Mudar a classe-mãe pode quebrar todas as filhas sem aviso (problema da classe base frágil). Hierarquias de 4 ou 5 níveis viram labirinto.
- **"Queria a banana, veio o gorila segurando a banana e a floresta inteira":** a crítica clássica de Joe Armstrong (criador do Erlang) a objetos que arrastam dependências demais.
- **Excesso de cerimônia:** `AbstractPagamentoFactoryProvider` para algo que uma função de 5 linhas resolvia. Padrões de projeto aplicados sem problema real.
- **Estado mutável compartilhado** é a origem de muitos bugs, e piora em concorrência. Por isso a programação funcional (funções puras, dados imutáveis) ganhou espaço.
- **Modelo anêmico:** classes que só têm getters e setters, com a regra espalhada em "services". Parece POO, mas é procedural com mais passos.
- **Objetos × tabelas:** o banco é relacional, o código é de objetos. O ORM tenta esconder essa diferença e às vezes cria consultas lentas (o problema N+1).
- **Não é o único jeito:** Go, Rust e Elixir resolvem bem sem classes. O Akita insiste que você conheça outros paradigmas, porque o mundo é maior do que a sua linguagem favorita.

## 7. Quando usar e quando não usar

| Use POO quando… | Prefira funções simples quando… |
|---|---|
| Há **estado com regras** que precisam ser protegidas (pedido, caixa, conta) | É **transformação de dados**: entra lista, sai lista (`map/filter/reduce`) |
| Há **várias variações** de um mesmo comportamento (formas de pagamento, impressoras) | É script, utilitário ou CLI pequena |
| O framework é orientado a objetos (NestJS) | Você está em Go: use `struct`, interface pequena e composição |
| Você precisa **trocar uma dependência no teste** | Uma classe teria só um método e nenhum estado |

## 8. Erros comuns

- Usar **herança só para reaproveitar código**. Se não é "é um" de verdade, é composição.
- Criar `Utils`, `Manager`, `Helper` com 40 métodos sem relação (baixa coesão).
- Getter e setter para todo campo: aí o objeto não protege nada.
- Deixar o objeto nascer inválido e "validar depois".
- Perder o `this` ao passar um método como callback em JavaScript.
- Quebrar o princípio de Liskov: o clássico `Quadrado extends Retangulo` que quebra quando alguém muda só a largura.
- Comparar objetos de valor por referência (`a === b`) em vez de pelo valor.
- Usar `float` dentro de `Dinheiro` (ver o assunto Dinheiro no código).

## 9. No seu setup e no AM Gestão

- **AM Gestão (TypeScript/NestJS):** NestJS é fortemente orientado a objetos. Módulos, *providers* e **injeção de dependência** pelo construtor são o padrão. Entender POO é pré-requisito para o back-end do produto (M3).
- **Domínio do produto:** `Pedido` (entidade), `ItemPedido`, `Dinheiro` (objeto de valor imutável, em centavos inteiros), `Pagamento` (interface com Pix, dinheiro e cartão). Isso conversa direto com engenharia de sistemas financeiros (M4).
- **Repository com Prisma/Drizzle:** a regra de negócio não conhece o banco, só uma interface `PedidoRepository`.
- **Agente fiscal em Go (M4):** uma interface `Impressora` com a implementação ESC/POS real e uma falsa para os testes. É o mesmo princípio sem classes.
- **Python/FastAPI (T3):** classes com Pydantic para validar dados.
- **Revisão de código de IA (Trilha R):** a IA adora gerar classe para tudo e hierarquia profunda. Seu checklist pergunta: "isso precisava ser classe?" e "herança ou composição?".
- **Professor:** classes entram em `o-csharp` (TypeScript do zero ao confortável); o design (SOLID, padrões, DDD) entra no Mês 10.

## 10. O que o mercado cobra

- **Júnior:** explicar os 4 pilares com exemplo próprio; criar classes, interfaces e construtores em TypeScript; entender `this`.
- **Pleno:** composição × herança com argumento; aplicar SOLID e 3 ou 4 padrões (Strategy, Factory, Repository, Adapter); escrever código testável com injeção de dependência.
- **Sênior:** modelar um domínio (entidades, objetos de valor, agregados); saber **quando não** usar objetos; revisar o design de outras pessoas e da IA; explicar o custo de cada escolha.
- **Perguntas de entrevista comuns:**
  1. Qual a diferença entre interface e classe abstrata? Quando usar cada uma?
  2. Por que preferir composição a herança? Dê um exemplo em que herança deu errado.
  3. Explique o princípio de substituição de Liskov com um exemplo.
  4. Como você testaria uma classe que imprime na impressora fiscal?
  5. Como o `class` do JavaScript funciona por baixo?

## 11. Exercícios

Primeiro sem IA. A IA só corrige depois.

- **N1 (reconhecer):** dado um trecho de código com `Pedido`, `Pagamento` e `PagamentoPix`, aponte onde está cada um dos 4 pilares e um ponto de acoplamento alto.
- **N2 (aplicar):** escreva em TypeScript a classe `Dinheiro`, imutável, guardando **centavos inteiros**, com `somar`, `multiplicar(quantidade)`, `igual` e `formatar()` em reais. Escreva 5 testes.
- **N3 (combinar e achar o erro):**
  - Refatore uma função `calcularTaxa(forma: string)` cheia de `switch` para polimorfismo com uma interface `FormaDePagamento`.
  - Ache o erro: `class Quadrado extends Retangulo`, com `setLargura` e `setAltura`. Explique por que quebra Liskov e corrija.
- **N4 (mini-projeto real):** o núcleo do **módulo Caixa** do AM Gestão: `Pedido`, `ItemPedido`, `Dinheiro` e a interface `Pagamento` (Pix, dinheiro, cartão), com regra de que o pedido não fecha com pagamento menor que o total. Testes com Vitest e uma impressora falsa injetada. Depois, **porte a mesma regra para Go** com `struct` e interfaces e escreva 5 frases comparando os dois jeitos (o método da École 42: primeiro na sua stack, depois em outra linguagem).

## 12. Fontes (na ordem de uso)

1. **Documentação oficial:**
   - [TypeScript Handbook: Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
   - [MDN: herança e a cadeia de protótipos](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
   - [Python: classes](https://docs.python.org/pt-br/3/tutorial/classes.html)
   - [Effective Go: interfaces e embedding](https://go.dev/doc/effective_go#embedding)
2. **Akita:**
   - [#15 Sua linguagem não é especial (parte 1)](https://akitaonrails.com/2018/10/02/akitando-15-sua-linguagem-nao-e-especial-parte-1/): a genealogia das linguagens.
   - [#16 Sua linguagem não é especial (parte 2)](https://akitaonrails.com/2018/10/04/akitando-16-sua-linguagem-nao-e-especial-parte-2/): Simula, CLU, outros paradigmas.
   - [#45](https://akitaonrails.com/2019/03/27/akitando-45-gerenciamento-de-memoria-parte-1-entendendo-back-end-para-iniciantes-parte-5/) e [#46 Gerenciamento de memória](https://akitaonrails.com/2019/04/03/akitando-46-gerenciamento-de-memoria-parte-2-entendendo-back-end-para-iniciantes-parte-6/): onde os objetos vivem e o custo deles.
3. **Alura (antes da aula):** "JavaScript: programação orientada a objetos" e "TypeScript: evoluindo seu JavaScript".
4. **Livros:** *Padrões de Projeto* (Gamma, Helm, Johnson e Vlissides, o "GoF"); *Refatoração* (Martin Fowler); *Domain-Driven Design* (Eric Evans), no Mês 10.

## 13. Como saber que dominou

- [ ] Explico POO em 3 a 5 frases sem jargão, para um aluno do 1º ano.
- [ ] Explico como `class` funciona por baixo em JavaScript (protótipo) e como Go faz o mesmo sem classe.
- [ ] Resolvo o N4 sem consulta e defendo cada escolha de design.
- [ ] Reviso um PR da IA e aponto pelo menos um problema de herança, coesão ou acoplamento.
- [ ] **Registro de entrevista:** contexto (módulo Caixa), decisão (interface `Pagamento` + composição), alternativa descartada (hierarquia de herança), resultado (nova forma de pagamento sem mexer no caixa; número de testes).
- [ ] **N4:** dei a aula de POO na escola ou em vídeo. Onde e quando: ______
