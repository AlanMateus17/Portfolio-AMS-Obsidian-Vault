---
tags: [planejamento, juridico, portfolio-ams]
tipo: planejamento
status: completo
---

# Estrutura Jurídica — Grupo AMtech Digital
### Trazido de uma conversa anterior (22/08/2026) — decisão já fechada, falta só confirmar com contador antes de abrir

> **Não sou contador nem advogado.** O que está aqui é o caminho já decidido nas conversas anteriores, pronto pra levar a um profissional confirmar o CNAE exato e o enquadramento tributário antes de abrir — principalmente o Fator R, que só se calcula com faturamento real rodando.

---

## 1. Tipo de empresa — decidido

**SLU (Sociedade Limitada Unipessoal)**, enquadrada como **ME no Simples Nacional**.

- Você é o único titular, sem precisar de sócio fictício ("laranja") nem sócio cotista real — ambos avaliados e descartados (o primeiro é ilegal — interposição fraudulenta de pessoa; o segundo tira sua autonomia de decisão sem resolver nada que a SLU sozinha não resolva).
- **MEI está fora de cogitação** — não pelo vínculo CLT (isso não impede nada), mas porque desenvolvimento de software (CNAEs 6201-6204) não está na lista de ocupações permitidas pro MEI, mesmo faturando pouco.
- **CLT na escola não impede nada:** sem cláusula de exclusividade (comum em CLT, raro fora de cargos estatutários — vale só confirmar no seu contrato), sem aviso automático ao empregador, sem vínculo público entre CNPJ e contrato de trabalho.

---

## 2. CNAEs — tudo dentro de uma CNPJ só, por decisão sua

Você decidiu explicitamente manter tudo que é TI (desenvolvimento, licenciamento, manutenção de sistemas, manutenção de hardware) numa única empresa, e depois expandiu pra incluir venda de peças/produtos física e online.

### Serviços de TI (Anexo III ou V do Simples — decidido pelo Fator R)

| CNAE | Atividade | Cobre |
|---|---|---|
| `6201-5/01` (principal) | Desenvolvimento sob encomenda | Freelas avulsos, projetos fechados |
| `6202-3/00` | Licenciamento de software customizável | AM Kaixara e demais sistemas Aura |
| `6203-1/00` | Licenciamento de software não customizável | AM Vynla (SaaS por assinatura) |
| `6209-1/00` | Suporte técnico e manutenção de sistemas | Manutenção vendida a clientes |
| `6204-0/00` | Consultoria em TI | Diagnóstico avulso (ex: AM Projeta como serviço) |
| `9511-8/00` | Reparação e manutenção de computadores e periféricos | Mão de obra de conserto |

### Comércio (Anexo I do Simples — bloco tributário diferente)

| CNAE | Atividade |
|---|---|
| `4751-2/01` | Equipamentos e suprimentos de informática |
| `4752-1/00` | Equipamentos de telefonia e comunicação |
| `4789-0/99` | Outros produtos não especificados |
| Equivalente `/02` (versão "via internet") | Cobre a venda online, além da física |

**Por que os dois blocos juntos, na mesma CNPJ:** o Simples Nacional calcula por bloco automaticamente — serviço cai no Anexo III/V, comércio cai no Anexo I (~4% inicial) — o contador segrega isso todo mês. Não é gambiarra, é rotina pra quem já opera assim. O que muda é a mecânica de custo (ver seção 4) e a exigência de estrutura física (alvará, endereço comercial, Inscrição Estadual) que o comércio traz e o serviço puro não trazia.

**Decisão consciente, não ingenuidade:** a versão inicial desta conversa recomendava separar loja física numa "fase 2" à parte, por ser operacionalmente mais pesada. Você decidiu manter tudo junto mesmo assim — registrado aqui pra você lembrar da trade-off que aceitou (mais burocracia mensal, em troca de não gerenciar duas empresas separadas).

---

## 3. O que já emitir nota, por atividade

| CNAE | Quando começar a faturar |
|---|---|
| `6201` (freela) | Assim que fechar o primeiro contrato avulso |
| `6202`/`6203` (Aura/AM Vynla) | Quando o primeiro cliente pagar pela licença/assinatura — ainda em desenvolvimento |
| `6209` (manutenção de sistemas) | Pode começar a oferecer e faturar desde já — fonte de caixa rápida enquanto os produtos próprios amadurecem |
| `9511` (manutenção de hardware) | Mesma lógica — rápido de monetizar |
| CNAEs de comércio | Quando a loja física/online estiver operando de fato |

**Ponto de atenção:** se a manutenção de hardware cobrar só mão de obra, é 100% serviço, sem complicação. Se também vender a peça trocada (fonte, RAM, SSD), essa fatia vira comércio — não impede de ficar na mesma CNPJ, só exige que o contador segregue essa receita separadamente.

---

## 4. Custos — dois cenários

### Cenário A — só serviço de TI (sem loja física)

| Item | Valor |
|---|---|
| Taxas Junta Comercial/Prefeitura (abertura) | R$ 100–500 |
| Certificado digital e-CNPJ | R$ 150–300/ano |
| Honorários de abertura | R$ 400–1.000 (muitas contabilidades zeram no plano mensal) |
| Capital social sugerido | R$ 1.000 |
| Contabilidade mensal | R$ 150–350/mês |
| DAS (variável) | ~6% a ~15,5%, conforme Fator R |

### Cenário B — com loja física + venda de peças (o que você decidiu ter)

| Item | Valor |
|---|---|
| Tudo do Cenário A, mais: | |
| Alvará de funcionamento | R$ 100–400, varia por município |
| Inscrição Estadual (obrigatória pra ICMS) | Geralmente gratuita, mas exige regularidade |
| Contabilidade mensal (comércio + serviço, estoque, NF-e+NFS-e) | R$ 350–900/mês |
| Endereço comercial (aluguel real, não "endereço fiscal" barato) | R$ 500+/mês |
| DAS comércio (variável) | ~4% inicial (Anexo I) |

**Piso mensal estimado com loja física, antes de imposto sobre faturamento: R$ 850–1.800/mês** — o salto em relação ao cenário só-serviço (R$ 150–350/mês) vem quase todo da estrutura física.

### Extras a considerar

- Registro de marca "AMtech Digital" no INPI: R$ 355–1.115 (protege por 10 anos)
- Seguro do estabelecimento físico (recomendável com estoque de peças)
- Sistema de gestão/PDV da loja — o próprio AM Kaixara que você já está construindo cobre isso, sem custo adicional de licença de terceiro

---

## 5. Pendências reais

1. **Confirmar com contador:** CNAE principal exato, enquadramento Fator R (III vs V), e se a lista completa de CNAEs secundários precisa estar no contrato social desde a abertura (evita alteração contratual depois)
2. **Decidir o momento de abrir** — ver [plano-mestre-frentes-alan](plano-mestre-frentes-alan.md), que trata a formalização do CNPJ de tecnologia como prioridade 2 (depois da assistência técnica MEI, que é mais rápida/barata)
3. **Confirmar no seu contrato de professor** se existe cláusula de dedicação exclusiva (improvável em CLT/contrato temporário, mas vale checar antes de abrir)

---

## 🔗 Documentos relacionados
- [plano-mestre-frentes-alan](plano-mestre-frentes-alan.md) — quando abrir isso em relação às outras frentes, e o cronograma de fases
- [status-planejamento-portfolio](status-planejamento-portfolio.md) — status geral do portfólio que essa empresa vai comercializar
