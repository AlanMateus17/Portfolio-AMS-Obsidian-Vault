---
tags: [estudo, assunto, linguagens, typescript]
area: 07 · Linguagens de programação
nivel-alvo: N4 (ao fim do T4) · N2 no M1 · N3 no M3
quando: M1 → T4
professor: o-csharp (TypeScript do zero ao confortável) · o-dotnet (projeto TypeScript de verdade)
prereq: [logica-de-programacao]
status: estudando
atualizado: 2026-11-17
---

# TypeScript: fundamentos

> **Em uma frase:** TypeScript é JavaScript com **tipos verificados antes de rodar**: você escreve `.ts`, o compilador confere os tipos e gera JavaScript comum, que roda no navegador ou no Node.
> **Nível-alvo:** N2 no Mês 1 (escrever os exercícios com o Handbook aberto), N3 no Mês 3 (API do AM Gestão sem consulta), N4 no fim do ano (revisar código da IA e ensinar).
> **Os 20% que resolvem 80%:** tipos básicos e inferência · arrays com `map/filter/reduce` · funções tipadas · `type` e `interface` com union types · `async/await`.

---

## 1. Por que isso existe (o problema e a história)

- **JavaScript** nasceu em 1995, feito em poucos dias por Brendan Eich na Netscape para dar vida às páginas. Virou a única linguagem que todo navegador entende, e depois, com o **Node.js** (2009), passou a rodar no servidor também.
- O problema: JavaScript é **dinâmico**. Um erro como chamar `.toUpperCase()` num número só aparece **quando roda**, às vezes na mão do cliente. Em projetos grandes, isso vira medo de mexer.
- **TypeScript** (Microsoft, 2012, com Anders Hejlsberg, o mesmo do Turbo Pascal, do Delphi e do C#) adicionou tipos **sem mudar o JavaScript por baixo**: todo JavaScript válido é TypeScript válido, e os tipos somem na compilação.
- Hoje é o padrão em front-end e cresce no back-end. JavaScript lidera há mais de uma década as pesquisas de linguagem mais usada da Stack Overflow, e é por isso que TypeScript é o núcleo da sua stack (ADR 0017).

**A lição do Akita:** nenhuma linguagem surge sozinha; TypeScript herda de JavaScript, que herda de Scheme (funções) e Self (protótipos). Entender essa herança explica as esquisitices (o `this`, o `==`, o `0.1 + 0.2`).

## 2. O que é

- **Superset de JavaScript:** tudo do JavaScript, mais tipos.
- **Tipagem estática e gradual:** os tipos são conferidos antes de rodar, e você pode tipar aos poucos.
- **Tipagem estrutural:** o que importa é a **forma** do objeto, não o nome da classe. Se tem `nome: string` e `preco: number`, serve onde se pede `{ nome: string; preco: number }`.
- **Inferência:** em `const total = 10`, o TypeScript já sabe que é `number`; você não precisa escrever tudo.
- **Compilação:** `tsc` (ou ferramentas como `tsx` e o próprio Node recente) transforma `.ts` em `.js`. Os tipos não existem em tempo de execução, por isso dados que vêm de fora (formulário, API) precisam ser **validados** (Zod, no Mês 3).

## 3. Como funciona por baixo

- O compilador lê o código, monta uma **árvore de sintaxe** (AST), confere os tipos e **apaga** tudo o que é tipo, sobrando JavaScript.
- Quem roda é o **motor JavaScript** (V8 no Chrome e no Node): ele interpreta e depois **compila em tempo de execução (JIT)** os trechos que rodam muito.
- O JavaScript roda numa **única thread** com um **event loop**: tarefas de I/O (ler arquivo, chamar API, consultar banco) são entregues ao sistema e, quando terminam, o resultado entra numa fila. `async/await` é uma forma legível de escrever isso. **Não é paralelismo**: é concorrência numa thread só (episódios [#43](https://akitaonrails.com/2019/03/13/akitando-43-concorrencia-e-paralelismo-parte-1-entendendo-back-end-para-iniciantes-parte-3/) e [#44](https://akitaonrails.com/2019/03/20/akitando-44-concorrencia-e-paralelismo-parte-2-entendendo-back-end-para-iniciantes-parte-4/) do Akita).
- **Números** são todos ponto flutuante de 64 bits (IEEE 754). Inteiros exatos só até 2^53. Para dinheiro, centavos inteiros; para valores enormes, `bigint`.

## 4. Conceitos que você precisa dominar

**Mês 1 (N2):**
- [ ] `let` e `const`; tipos `number`, `string`, `boolean`, `null`, `undefined`.
- [ ] Inferência e quando anotar o tipo.
- [ ] Arrays tipados (`number[]`, `Item[]`) e `for...of`.
- [ ] `map`, `filter`, `reduce`, `find`, `some`, `every`.
- [ ] Funções com parâmetros e retorno tipados; arrow functions (`=>`).
- [ ] Objetos e `type` / `interface`.
- [ ] Union types (`"ativo" | "atraso" | "restrito" | "suspenso"`) e narrowing com `if`.
- [ ] Template strings e formatação (`Intl.NumberFormat` para reais).
- [ ] `async/await`, `Promise` e `try/catch`.

**Mês 2 e 3 (N3):**
- [ ] Generics (`function primeiro<T>(lista: T[]): T | undefined`).
- [ ] Classes, modificadores de acesso e interfaces (ver [POO](../04-ciencia-da-computacao/poo.md)).
- [ ] Módulos (`import` / `export`), `package.json`, npm.
- [ ] `tsconfig.json` com `strict: true`.
- [ ] Tipos utilitários: `Partial`, `Pick`, `Omit`, `Record`, `Readonly`.
- [ ] Erros: lançar, capturar, tipar o erro desconhecido (`unknown`).
- [ ] Validação na borda com Zod; tipos derivados do esquema.

**T4 (N4):**
- [ ] Tipos condicionais e mapeados (o suficiente para ler bibliotecas).
- [ ] Event loop por dentro (microtasks × macrotasks).
- [ ] Desempenho: o que custa no V8, vazamento de memória em Node.

## 5. Qualidades

- **Erros aparecem no editor**, não no cliente.
- **Autocompletar e refatorar com segurança:** renomear um campo em 30 arquivos sem medo.
- **Uma linguagem para tudo:** front (Next.js), back (NestJS), scripts e IA (Vercel AI SDK).
- **Mercado enorme** e ecossistema gigante (npm).
- **Os tipos documentam o código**, e ajudam a IA a gerar código mais correto, e você a revisá-lo.

## 6. Defeitos, limites e críticas

- **Os tipos somem ao rodar:** dados de fora podem mentir. Sem validação (Zod), o tipo é só uma promessa.
- **Herda as esquisitices do JavaScript:** `this`, coerção com `==`, `0.1 + 0.2`, `typeof null === "object"`.
- **`any` desliga a segurança:** um `any` espalha e vira JavaScript sem tipos com mais trabalho.
- **Ecossistema npm:** dependências demais, pacotes abandonados, ataques de cadeia de suprimentos. Cada dependência é risco (gitleaks, Dependabot e Trivy no seu CI).
- **Uma thread só:** trabalho pesado de CPU trava o servidor. Para isso, Go (ferramentas) ou Python (dados) no seu setup.
- **Sistema de tipos complexo:** dá para escrever tipos ilegíveis. Simplicidade vence.

## 7. Quando usar e quando não usar

| Use TypeScript para… | Prefira outra coisa para… |
|---|---|
| Front-end e back-end web do AM Gestão | Ferramenta de linha de comando que precisa ser um binário único e rápido → **Go** |
| Integração com IA por API | Análise de dados, machine learning, notebooks → **Python** |
| Scripts de automação que já vivem num projeto Node | Firmware e baixo nível → **C / Rust** |

## 8. Erros comuns

- Usar `any` para "fazer passar".
- Confiar no tipo de um dado vindo de API ou formulário sem validar.
- Esquecer o `await` e trabalhar com uma `Promise` no lugar do valor.
- `forEach` com `async` dentro esperando que espere (não espera; use `for...of` ou `Promise.all`).
- Mutar arrays com `push` dentro de `map`.
- Dinheiro em `number` com casas decimais.
- `strict: false` no `tsconfig`.

## 9. No seu setup e no AM Gestão

- **Núcleo da stack** (ADR 0017): Next.js no front, NestJS no back, Prisma/Drizzle no banco, Vitest nos testes, Zod nas bordas.
- **Mês 1:** os 3 exercícios de lógica em TypeScript, no repositório `logica-ts`.
- **Mês 2:** site do cliente em Next.js pela esteira (issue → agente → PR → você revisa).
- **Mês 3:** API do AM Gestão e a **primeira chamada de IA em TypeScript** (Vercel AI SDK com saída validada por Zod).
- **Professor:** `o-csharp` (TypeScript do zero ao confortável) e `o-dotnet` (projeto TypeScript de verdade). Os nomes dos ids ficaram da stack antiga; o conteúdo já é TypeScript.

## 10. O que o mercado cobra

- **Júnior:** tipos, funções, arrays com `map/filter/reduce`, `async/await`, consumir API, um projeto React/Next no GitHub.
- **Pleno:** generics, organização em módulos, testes, tratamento de erro, Node no servidor, validação de dados.
- **Sênior:** event loop por dentro, desempenho, desenho de tipos para uma base grande, revisar código (humano e de IA), escolher quando **não** usar TypeScript.
- **Perguntas comuns:** diferença entre `type` e `interface`; o que é `unknown` × `any`; como funciona o event loop; `Promise.all` × `Promise.allSettled`; por que `0.1 + 0.2 !== 0.3`.

## 11. Exercícios

Sem IA no aprendizado; a IA revisa depois.

- **N1:** dado um trecho com `type`, `interface`, union e generic, diga o tipo de cada variável sem rodar.
- **N2:** os 3 exercícios de lógica em TypeScript ([lógica de programação](../04-ciencia-da-computacao/logica-de-programacao.md), seção 11).
- **N3:**
  - Reescreva o carrinho usando só `map/filter/reduce`, sem `for`.
  - Ache o erro: um `forEach(async ...)` que deveria somar 3 chamadas de API e devolve 0.
  - Tipar o status da inadimplência como union type e fazer o compilador reclamar se um caso faltar.
- **N4:** um script em Node + TypeScript que lê um CSV de vendas, calcula o total por dia com `reduce` e escreve um JSON; com `strict: true`, testes com Vitest e README.

## 12. Fontes (na ordem de uso)

1. **Oficial:** [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) · [TS Playground](https://www.typescriptlang.org/play) · [MDN JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) · [roadmap.sh/typescript](https://roadmap.sh/typescript)
2. **Akita:** [#15](https://akitaonrails.com/2018/10/02/akitando-15-sua-linguagem-nao-e-especial-parte-1/) e [#16 Sua linguagem não é especial](https://akitaonrails.com/2018/10/04/akitando-16-sua-linguagem-nao-e-especial-parte-2/) · [#39 A história do front-end](https://akitaonrails.com/2019/02/13/akitando-39-a-historia-do-front-end-para-iniciantes-em-programacao-serie-comecando-aos-40/) · #43 e #44 (concorrência, seção 3) · [#117 Compilada × interpretada](https://akitaonrails.com/2022/04/15/akitando-117-linguagem-compilada-vs-interpretada-qual-e-melhor/)
3. **Alura:** "TypeScript: evoluindo seu JavaScript", "JavaScript: trabalhando com arrays e coleções", "TypeScript: tipagem avançada e generics", "JavaScript: tratando erros e exceções"
4. **Livro:** *Programming TypeScript* (Boris Cherny), quando chegar no N3

## 13. Como saber que dominou

- [ ] (M1) Escrevo os 3 exercícios em TypeScript com `strict: true` sem `any`.
- [ ] (M3) Explico o event loop e por que `async/await` não é paralelismo.
- [ ] (M3) Valido na borda com Zod e explico por que os tipos não bastam.
- [ ] (T4) Reviso um PR em TypeScript da IA e acho problemas de tipo, erro e desempenho.
- [ ] **Registro de entrevista:** contexto (API do AM Gestão), decisão (Zod na borda + tipos derivados), alternativa descartada (confiar nos tipos), resultado (erros pegos antes de produção, com número).
- [ ] **N4:** dei aula de TypeScript (Programação Web ou vídeo). Onde e quando: ______
