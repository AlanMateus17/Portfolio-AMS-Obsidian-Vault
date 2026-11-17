---
tags: [estudo, assunto, modelo]
tipo: modelo
---

# Modelo de arquivo de assunto

> Copie este arquivo para `assuntos/<área>/<assunto>.md` e preencha. Um arquivo por assunto. Ele serve para três coisas ao mesmo tempo: **estudar**, **revisar** (Anki e provas) e **dar aula** (é a base da ficha dupla e do livro *Lógica e Máquina*).

## Como este modelo junta as três fontes

- **O jeito do Akita de aprender:** começar pelo **porquê** e pela **história** (nenhuma tecnologia surge do nada), descer até **como funciona por baixo**, fazer na mão antes de usar a ferramenta pronta, ler a fonte primária e não tratar linguagem ou framework como religião.
- **O método do Professor (dev-setup):** 20/80 em duas passadas, recuperação ativa, exercícios N1–N4, protocolo de fim de bloco, ficha dupla e registro de entrevista.
- **O mercado:** o que se cobra de júnior, pleno e sênior, e como o assunto aparece em entrevista.

---

```markdown
---
tags: [estudo, assunto, <área>]
area: <número e nome da área no MAPA>
nivel-alvo: N1 | N2 | N3 | N4
quando: M1 | T2 | H ...
professor: <id do módulo no curriculo.json, se houver>
prereq: [<assuntos que precisam vir antes>]
status: a-estudar | estudando | dominado | ensinado
atualizado: AAAA-MM-DD
---

# <Assunto>

> **Em uma frase:** ...
> **Nível-alvo:** N? (o que isso quer dizer aqui: ...)
> **Os 20% que resolvem 80%:** os 3 a 5 conceitos que vêm primeiro.

## 1. Por que isso existe (o problema e a história)
Que problema resolveu, quem criou, o que havia antes. A motivação vem antes da definição.

## 2. O que é
Definição precisa, com as palavras certas.

## 3. Como funciona por baixo
O que a máquina, o SO, o compilador ou a rede realmente fazem. Um diagrama simples se ajudar.

## 4. Conceitos que você precisa dominar
- [ ] conceito — explicação curta
(checklist; cada item vira cartão no Anki)

## 5. Qualidades (por que é bom)

## 6. Defeitos, limites e críticas
Inclua as críticas sérias (do Akita e de outros). Nada é bala de prata.

## 7. Quando usar e quando não usar

## 8. Erros comuns
Os erros de iniciante e os de quem acha que já sabe.

## 9. No seu setup e no AM Gestão
Onde isso aparece no dev-setup e no produto, com arquivo ou comando.

## 10. O que o mercado cobra
- **Júnior:** ...
- **Pleno:** ...
- **Sênior:** ...
- **Perguntas de entrevista:** 3 a 5 perguntas reais.

## 11. Exercícios
- **N1 (reconhecer):**
- **N2 (aplicar):**
- **N3 (combinar e achar o erro):**
- **N4 (mini-projeto real):**
Primeiro sem IA. A IA só corrige depois.

## 12. Fontes (na ordem de uso)
1. Documentação oficial ou fonte primária
2. Akita (episódio ou post)
3. Curso da Alura (assistir antes da aula)
4. Livro
(conteúdo pago e página de livro nunca vão para a IA)

## 13. Como saber que dominou
- Explico em 3 a 5 frases sem jargão.
- Resolvo o N4 sem consulta.
- Registro de entrevista: contexto, decisão, alternativa descartada, resultado com número.
- (N4) Dei a aula de verdade: onde e quando.
```
