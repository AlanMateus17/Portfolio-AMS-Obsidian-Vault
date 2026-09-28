---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Passo a Passo Mestre — Portfólio para Vaga Júnior
### Tudo que precisa ser desenvolvido e entregue, do zero até pronto pra aplicar em qualquer empresa

> Este documento tem um recorte **diferente** do `passo-a-passo-mestre-desde-o-inicio` (que segue construindo os 21 sistemas do Grupo AMtech Digital, no seu ritmo, sem prazo). Aqui o objetivo é específico: **o que é suficiente e necessário pra um recrutador de vaga júnior olhar seu portfólio e querer te chamar pra entrevista.** Os dois planos não competem — a base técnica (Fases 0-6 do plano de estudo) é a mesma para os dois.

---

## Fase 0 — Base técnica (pré-requisito, não repetido aqui)

Siga os **Passos 1 a 10** do `passo-a-passo-mestre-desde-o-inicio` — lógica, Git/SQL/Docker, C#, API, EF Core, testes, frontend, arquitetura, deploy. Isso é o alicerce dos dois planos ao mesmo tempo, não é trabalho extra específico de vaga.

---

## Fase 1 — Escopo de funcionalidade do AM Kaixara pra vitrine (não é o AM Kaixara "100% completo")

### Tier 1 — Essencial, sem isso o portfólio não está pronto

| Funcionalidade | Referência no documento original |
|---|---|
| Login com JWT + BCrypt, isolado por tenant | RF01 |
| Controle de acesso por papel | RF02 |
| CRUD de produto e categoria | RF03 |
| **Controle de concorrência no estoque** (`RowVersion`, atualização condicional) | RNFT-E01 — é o diferencial técnico mais forte e mais barato de implementar |
| Carrinho de venda com pagamento | RF04 |
| Abertura/fechamento de caixa | RF05 |
| Cancelamento de venda com restauração de estoque | RF06 |
| Testes automatizados (unitário + integração) | Fase 2.4 do plano de estudo |
| Pipeline de CI rodando os testes a cada push | Fase 6 |
| Deploy real, com link acessível | Fase 6 |

### Tier 2 — Forte diferencial, inclua se o tempo permitir

| Funcionalidade | Por que vale o esforço extra |
|---|---|
| Dashboard com indicador (RF12) + atualização em tempo real via SignalR | Mostra que sabe mais que requisição-resposta simples |
| Reserva de estoque (RF11) | Reforça o mesmo raciocínio de concorrência do Tier 1, com mais profundidade |
| Recibo de venda não-fiscal (RF15, sem a complexidade de emissão fiscal real) | Prova de fluxo de venda ponta a ponta, sem depender de integração externa complexa |
| Modo offline básico (fila local + sincronização, RF10) | O diferencial mais raro de todos num portfólio júnior — mas é o mais caro de construir; só entre nele se o Tier 1 já estiver 100% sólido |
| Um ADR documentando a decisão de concorrência | Prova de raciocínio de arquitetura, não só resultado — ver `[[github-estrutura-profissional-autoridade]]` |

### Tier 3 — Mencione como "planejado", não precisa estar funcionando

Emissão fiscal real (NFC-e/SEFAZ), integração TEF com adquirente real, agente de hardware físico (impressora fiscal, gaveta, balança), `aura-licensing`, `aura-historico`, `aura-analytics`. Essas dependem de decisão de fornecedor e hardware físico que não fazem sentido pra demonstrar numa entrevista júnior. Uma linha no README tipo "arquitetura pronta pra integração fiscal e de hardware (interfaces `IEmissorFiscal`/`ITefService` já definidas), próxima fase" já comunica maturidade de planejamento sem exigir que esteja pronto.

---

## Fase 2 — Qualidade e apresentação (o que faz o recrutador parar de rolar a página)

1. **README com GIF ou screenshot do sistema rodando**, não só texto — prova visual em segundos
2. **Documentação Swagger/OpenAPI** da API, gerada automaticamente
3. **Badge de CI passando** visível no topo do README
4. **Link de deploy clicável**, testado antes de aplicar pra qualquer vaga (nada mais frustrante pro recrutador que link quebrado)
5. Estrutura de README na ordem: frase de impacto → problema que resolve → stack usada → como rodar localmente → link de deploy → decisões técnicas de destaque (com link pro ADR)

---

## Fase 3 — Presença no GitHub, especificamente pra quem recruta

Diferente da estratégia de "empresa" (organização separada, já planejada em `[[github-estrutura-profissional-autoridade]]`), pra busca de vaga o que mais pesa é o **seu perfil pessoal**:

1. **Fixe o repositório do AM Kaixara** no topo do seu perfil pessoal (mesmo que o código "de verdade" esteja também replicado na organização)
2. **Profile README** — quem você é, o que estuda, link pro projeto principal, contato
3. **Consistência de commit visível** (o "gráfico verde") — recrutador técnico olha isso como sinal de disciplina, mesmo sabendo que não é métrica perfeita
4. Repositório com nome claro, descrição preenchida, tópicos/tags corretos (`dotnet`, `csharp`, `postgresql`, `clean-architecture`)

---

## Fase 4 — Prontidão de aplicação (além do código)

1. **Treinar explicar o projeto em 2 minutos**, sem gaguejar — grave você mesmo falando e reescute
2. **Método STAR** pra pergunta comportamental ("me conte uma vez que você resolveu um problema difícil") — já detalhado em `[[perfil-senior-completo-auditoria]]`
3. **LinkedIn atualizado**, com o mesmo projeto em destaque, e headline clara ("Desenvolvedor Full Stack Júnior | C#/.NET, TypeScript/Next.js")
4. **Currículo de uma página**, projeto do AM Kaixara com link, sem enumerar os outros 20 sistemas do portfólio de negócio — mesma lógica de foco já discutida
5. Inglês básico de entrevista, se for aplicar em vaga remota internacional — ver `[[ingles-espanhol-integrado]]`, nível B1-B2 já é suficiente pra maioria das entrevistas júnior

---

## Ordem recomendada de execução

```
Fase 0 (base técnica, Passos 1-10 do plano geral)
        ↓
Fase 1, Tier 1 (funcionalidade essencial)
        ↓
Fase 2 (qualidade: teste, CI, deploy, README)
        ↓
Fase 3 (GitHub pessoal)
        ↓
   → já pode começar a aplicar pra vaga aqui ←
        ↓
Fase 1, Tier 2 (diferencial, em paralelo às primeiras aplicações)
        ↓
Fase 4 (prontidão de entrevista, antes da primeira entrevista real acontecer)
```

**Não espere terminar o Tier 2 pra começar a aplicar.** O Tier 1 completo, bem testado, com deploy real, já é portfólio suficiente pra abrir processo seletivo júnior — o Tier 2 continua sendo construído em paralelo, e pode até virar assunto de conversa em entrevista ("estou terminando o modo offline agora, quer ver o que já fiz?").

---

## O que isso não muda

O `passo-a-passo-mestre-desde-o-inicio` e os 21 sistemas do portfólio de negócio continuam existindo, no seu ritmo — este documento é uma lente de foco temporária em cima do mesmo AM Kaixara, não um substituto do plano maior.
