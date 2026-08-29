---
tags: [stack, portfolio-ams]
tipo: stack
status: completo
---

# Revisão da Stack Tecnológica — Portfólio Completo
### Levantamento de toda tecnologia mencionada nos 21 documentos, separando decisão de fornecedor de tecnologia genuinamente nova a estudar

---

## 1. Stack fixo confirmado (sem mudança)

C#/.NET 10, ASP.NET Core (Controllers), Clean Architecture + DDD, Entity Framework Core, PostgreSQL, Redis, SignalR, JWT + BCrypt, Docker, xUnit, GitHub Actions, TypeScript/Next.js/Tailwind CSS. Continua sendo a base de praticamente todo o portfólio — nenhum dos 21 documentos contradiz isso.

**PostGIS** deixou de ser opcional: hoje é usado em Aura Delivery, AuraVet (atendimento domiciliar) e potencialmente AuraObra (visita a canteiro de obra) — vale tratá-lo como parte do stack fixo, não mais como exceção pontual.

---

## 2. Desvios já conscientes do stack .NET (decisão tomada, com justificativa registrada)

| Tecnologia | Onde | Por quê o desvio é aceito |
|---|---|---|
| **Clojure + Datomic** | `aura-historico` | Vantagem estrutural real em consulta temporal (`as-of`) e transação especulativa (`d/with`) — não existe equivalente direto em .NET com a mesma maturidade |
| **Python + FastAPI** | `aura-analytics` | Ecossistema de dado/ML (Prophet, statsmodels, Google OR-Tools) é substancialmente mais maduro em Python que em .NET para esse tipo de problema |
| **GraphQL (via HotChocolate)** | `AgileFlow` | Paradigma de API diferente do REST usado no resto do portfólio — mas **dentro do .NET**, não troca de runtime. Revisado: a versão anterior (Node/React/TS/GraphQL completo) foi corrigida por não atender ao critério abaixo |

Os dois primeiros já eram conhecidos. Nada novo neles nesta revisão.

### Critério pra qualquer desvio futuro, nos próximos sistemas também

Só desviar da stack fixa quando o .NET **literalmente não conseguir** resolver o problema com maturidade equivalente — nunca só porque outra ferramenta resolve *de um jeito diferente*, e nunca por valor de currículo isolado. Portfólio profundo e coeso em poucos ecossistemas pesa mais, pra quem contrata júnior/pleno, do que amplitude rasa em muitos. `aura-historico` e `aura-analytics` passam nesse critério (não existe equivalente maduro em .NET); o desvio completo de stack do AgileFlow não passava — GraphQL como paradigma se resolve dentro do próprio .NET via HotChocolate, sem abrir um runtime novo.

---

## 3. Decisões de fornecedor ainda em aberto — não exigem "estudar tecnologia nova", exigem escolher e integrar

| Decisão | Sistemas afetados | Categoria |
|---|---|---|
| Gateway de pagamento (Stripe/Vindi/Iugu/Asaas) | Praticamente todos os sistemas com cobrança — é a pendência mais repetida do portfólio inteiro | Integração de API, não tecnologia nova |
| AWS vs. Azure | Todo o portfólio | Infraestrutura, decisão única, não muda o código |
| Provedor de WhatsApp Business API (oficial Meta vs. BSP) | `aura-notifications`, e por extensão todo sistema que notifica | Integração de API |
| Provedor de SMS/e-mail transacional | `aura-notifications` | Integração de API |
| Provedor de transportadora (Correios/privada) | `aura-logistics`, AuraFix | Integração de API |
| Provedor de assinatura eletrônica (DocuSign/Clicksign/D4Sign) | AuraObra | Integração de API, mas com peso jurídico — a escolha importa mais que o padrão, por causa de validade legal |
| Provedor de videoaula síncrona (solução própria vs. Zoom/Meet) | AuraEdu | Integração de API, exceto se decidir construir solução própria (aí vira estudo real) |
| Fornecedor de hardware de portaria (interfone IP, fechadura eletrônica) | AuraCondo | Integração de protocolo de hardware, mais próxima de "tecnologia nova" que as demais desta lista |
| Provedor de KMS/HSM (AWS KMS/Azure Key Vault/HashiCorp Vault) | `aura-vault` | Infraestrutura de segurança gerenciada — exige entender o conceito, não construir do zero |
| Certificado de assinatura de código (Code Signing) | AuraPOS (instalador) | Processo administrativo/comercial, não técnico |

---

## 4. Tecnologia/conceito genuinamente novo — aqui sim vale estudo dedicado

Esta é a parte que realmente responde "o que adicionar para estudo":

### 4.1 Otimização combinatória / pesquisa operacional (Google OR-Tools, VRP)
**Onde:** `aura-analytics`, motor por trás do diferencial competitivo do Aura Delivery (roteirização de múltiplas entregas).
**Por que estudar:** isso não é "chamar uma API" — é entender o problema de roteirização de veículos (Vehicle Routing Problem) o suficiente para modelar corretamente as restrições do seu caso de uso (janela de tempo de entrega, capacidade de veículo, múltiplos pontos de origem). Dado seu histórico em matemática, esse é provavelmente o item desta lista mais alinhado ao que você já está estudando — vale considerar como aplicação prática direta da graduação em Matemática, não como tópico isolado de programação.

### 4.2 Machine learning aplicado — séries temporais (Prophet/statsmodels)
**Onde:** `aura-analytics`, previsão de demanda do AuraPOS e projeção patrimonial do AuraWealth.
**Por que estudar:** previsão de série temporal tem armadilha conceitual real (overfitting, sazonalidade mal capturada) que só se evita entendendo o método, não só chamando a biblioteca.

### 4.3 Criptografia aplicada e gestão de chave
**Onde:** `aura-vault`.
**Por que estudar:** você não vai implementar o algoritmo de criptografia do zero (isso seria erro, não estudo — sempre usar biblioteca madura), mas precisa entender o suficiente de gestão de chave (rotação, isolamento por tenant, o que um KMS gerenciado resolve e o que ele não resolve) para configurar corretamente. Erro aqui não é cosmético, é o tipo de erro que vira manchete.

### 4.4 Assinatura eletrônica e validade jurídica de documento digital
**Onde:** AuraObra (contrato de alto valor), potencialmente AuraCondo (ata de assembleia).
**Por que estudar:** não é a tecnologia de assinatura em si (isso o provedor resolve) — é entender o suficiente do arcabouço legal (ICP-Brasil vs. assinatura eletrônica simples/avançada, o que cada nível garante) pra escolher o provedor certo pra cada caso de uso, já que contrato imobiliário de alto valor pode exigir nível de validade jurídica diferente de uma ata de condomínio.

### 4.5 Function-calling e engenharia de contexto para IA aplicada
**Onde:** `aura-copilot`.
**Por que estudar:** você já decidiu não usar RAG — isso significa que o desafio técnico real é desenhar bem as ferramentas (functions) que o modelo pode chamar, e não a infraestrutura de busca. É uma área de estudo genuinamente diferente do resto do stack, mais próxima de design de API pensado para consumo por modelo de linguagem do que de desenvolvimento tradicional.

### 4.6 Acessibilidade web (WCAG)
**Onde:** transversal — já é requisito formal no RNFT-D04 (contraste de cor) e mencionado em vários sistemas (AuraVet, AuraEdu, portal de morador do AuraCondo).
**Por que estudar:** hoje está tratado como "validação de contraste automática", mas acessibilidade é mais amplo que contraste — navegação por teclado, leitor de tela. Vale pelo menos uma passada de estudo geral, mesmo que a implementação completa venha depois.

---

## 5. O que **não** entra nesta lista, por decisão consciente

- Nenhuma tecnologia de frontend mobile nativo foi adicionada — as pendências de "PWA vs. nativo" (Delivery, AuraVet, AuraObra) continuam em aberto como decisão, não como estudo obrigatório; PWA via Next.js já está dentro do que você domina.
- Nenhuma tecnologia de blockchain/Web3 — não apareceu necessidade real em nenhum dos 21 documentos, e não deveria ser adicionada sem essa evidência.

---

## 6. Recomendação de ordem de estudo

Dado que você tem ~9h/semana e já estuda Matemática formalmente, a ordem que faz mais sentido é:

1. **Otimização combinatória (4.1)** — maior sinergia com o que você já estuda, e é pré-requisito direto do diferencial competitivo do Aura Delivery
2. **Criptografia aplicada e gestão de chave (4.3)** — maior risco se malfeito, prioridade de segurança
3. **Assinatura eletrônica/validade jurídica (4.4)** — necessário antes do AuraObra ir a código, dado que já é decisão-bloqueio registrada
4. **Machine learning de série temporal (4.2)** e **function-calling para IA (4.5)** — podem esperar mais, já que `aura-analytics` (previsão) e `aura-copilot` são, respectivamente, prioridade média e a mais baixa de todo o portfólio
5. **Acessibilidade web (4.6)** — pode ser aprendizado contínuo, aplicado progressivamente conforme cada sistema entra em desenvolvimento, não exige bloco de estudo dedicado

---

## 🔗 Documentos relacionados
- [[stack-tecnologica-por-sistema]] — o detalhamento completo do que cada sistema usa
- [[stack-consolidada-estudo]] — a versão organizada pra virar plano de estudo
- [[passo-a-passo-mestre-desde-o-inicio]] — onde essas decisões de "estudar agora vs. depois" se encaixam na sequência real
