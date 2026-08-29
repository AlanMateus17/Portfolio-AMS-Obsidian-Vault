---
tags: [stack, portfolio-ams]
tipo: stack
status: completo
---

# Stack Consolidada — Tudo que Você Vai Estudar e Usar
### União de todos os 21 sistemas/serviços, sem repetição, organizada por categoria

---

## 1. Linguagens de programação

| Linguagem | Onde | Nível de familiaridade esperado |
|---|---|---|
| **C#** | Backend de 19 dos 21 sistemas/serviços | Já é sua base — aprofundar, não aprender do zero |
| **TypeScript** | Todo frontend (Next.js) | Já em uso |
| **Clojure** | `aura-historico` | **Novo de verdade** — linguagem funcional, paradigma diferente de tudo que você já usa |
| **Python** | `aura-analytics` | Provavelmente já tem alguma familiaridade; aqui o foco de estudo é menos "a linguagem" e mais as bibliotecas específicas (seção 5) |

---

## 2. Runtimes e plataformas

- **.NET 10** — runtime de praticamente todo o backend
- **Node.js** — runtime por trás do Next.js (frontend) e do protótipo ainda não migrado do Momentos/Cupido
- **JVM** — runtime por trás do Clojure/Datomic (`aura-historico`)
- **Python runtime** (3.x) — por trás do `aura-analytics`

---

## 3. Frameworks de backend

- **ASP.NET Core (Controllers)** — padrão de todo backend .NET do portfólio, decisão já fixada (nunca Minimal API)
- **FastAPI** — `aura-analytics`, único framework Python do portfólio

## 4. Frameworks e bibliotecas de frontend

- **Next.js** — todo painel administrativo e portal público
- **Tailwind CSS** — estilização, junto com o sistema de tokens de design (RNFT-D01 a D07)
- **React Native** (avaliação pendente) — só se a decisão de app nativo (várias pendências recorrentes) for tomada; hoje o padrão é PWA

---

## 5. Bibliotecas específicas por domínio — a parte que exige estudo dedicado, não só "instalar e usar"

| Biblioteca/técnica | Para quê | Sistema |
|---|---|---|
| **Google OR-Tools** | Otimização combinatória — roteirização de veículos (VRP) | `aura-analytics` → Aura Delivery |
| **Prophet** ou **statsmodels** | Previsão de série temporal | `aura-analytics` → AuraPOS, AuraWealth |
| **Datomic (client API)** | Consulta temporal e transação especulativa | `aura-historico` |
| Criptografia de campo (biblioteca .NET nativa, ex: `System.Security.Cryptography`) | Proteção de dado sensível | `aura-vault` |
| **SQLCipher** | Criptografia de banco local SQLite | AuraPOS (modo offline) |
| **ESC/POS** (protocolo de impressora) | Comunicação com impressora não-fiscal | AuraPOS (agente local) |

---

## 6. Dados e persistência

- **PostgreSQL** — banco relacional padrão de todo o portfólio
- **PostGIS** — extensão geoespacial, usada em Aura Delivery, AuraVet, potencialmente AuraObra e AuraCondo
- **Datomic** — banco imutável de fato, exclusivo do `aura-historico`
- **SQLite** — só localmente, no agente do AuraPOS (modo offline) e no protótipo ainda não migrado do Momentos/Cupido
- **Redis** — cache e sessão em todo o portfólio
- **Redis Streams** — fila de mensageria entre sistemas e serviços compartilhados (ingestão de evento do `aura-historico`, fila do `aura-notifications`, do `aura-logistics`)

---

## 7. Comunicação em tempo real e assíncrona

- **SignalR** — tempo real (status de pedido, internação, protocolo reprodutivo)
- **Redis Streams** — já listado acima, mas vale destacar como o padrão de fila único do portfólio, evitando introduzir RabbitMQ/Kafka sem necessidade comprovada

---

## 8. Autenticação e segurança

- **JWT** + **BCrypt** — padrão de autenticação, a ser centralizado no `aura-identity`
- **2FA** (TOTP ou similar) — a definir biblioteca específica, obrigatório no `aura-support`, opcional configurável nos demais
- **KMS/HSM gerenciado** (AWS KMS, Azure Key Vault ou HashiCorp Vault) — `aura-vault`
- **Code Signing/Authenticode** — assinatura de instalador executável (AuraPOS)

---

## 9. Testes e qualidade

- **xUnit** — testes de backend .NET
- **Teste de contrato de integração externa** — mencionado como prática necessária (AuraFix, `aura-logistics`), ferramenta específica ainda a escolher
- Framework de teste em Python (pytest, provável) — `aura-analytics`
- `clojure.test` (padrão da linguagem) — `aura-historico`

---

## 10. Infraestrutura, deploy e CI/CD

- **Docker** / **docker-compose** — containerização de todo o portfólio
- **GitHub Actions** — CI/CD padrão
- **AWS ou Azure** (decisão pendente, única para todo o portfólio) — hospedagem
- **MSIX** ou **WiX Toolset** (decisão pendente) — empacotamento de instalador Windows

---

## 11. Armazenamento e mídia

- **Cloudflare R2** — armazenamento de arquivo/mídia (laudo, imagem, foto), usado por AuraVet e Momentos/Cupido

---

## 12. Integrações externas (SDK/API de terceiro — não é "estudar tecnologia", é aprender a integração específica)

| Integração | Decisão pendente | Sistemas |
|---|---|---|
| Gateway de pagamento | Stripe/Vindi/Iugu/Asaas | Transversal a quase todo o portfólio |
| WhatsApp Business API | Oficial Meta vs. BSP | `aura-notifications` |
| SMS/e-mail transacional | Provedor a definir | `aura-notifications` |
| Transportadora | Correios vs. privada | `aura-logistics`, AuraFix |
| Assinatura eletrônica | DocuSign/Clicksign/D4Sign | AuraObra |
| Videoaula síncrona | Zoom/Meet vs. solução própria | AuraEdu |
| Emissão fiscal (NFC-e/NFSe) | Gateway terceirizado vs. SEFAZ própria | AuraPOS |
| Modelo de linguagem (IA) | API externa vs. auto-hospedado | `aura-copilot` |
| Hardware de portaria | Fornecedor a definir | AuraCondo |

---

## 13. Padrões arquiteturais transversais (não são tecnologia, mas fazem parte do "o que aprender")

- **Clean Architecture + DDD** — já dominado, mas vale reforço contínuo conforme sistemas novos entram em código
- **Multi-tenant com `tenant_id` + Row-Level Security** — padrão de isolamento em todo banco PostgreSQL do portfólio
- **Outbox pattern** — usado no `aura-historico` para integração confiável com o núcleo .NET
- **Otimização combinatória / pesquisa operacional** — não é biblioteca, é área de conhecimento matemático por trás do OR-Tools; maior sinergia com sua formação em Matemática

---

## Resumo do que é genuinamente novo pra estudar (cruzando com a seção 4 do documento de revisão de stack anterior)

1. Clojure + Datomic (paradigma novo)
2. Otimização combinatória / OR-Tools (matemática aplicada)
3. Previsão estatística de série temporal (Prophet/statsmodels)
4. Criptografia aplicada e gestão de chave (KMS/HSM)
5. Function-calling para IA sem RAG
6. Fundamentos legais de assinatura eletrônica (ICP-Brasil vs. assinatura simples/avançada)

Tudo o resto do documento é: C#/.NET que você já domina, integração de API de terceiro (trabalho de engenharia, não lacuna de conhecimento), ou decisão de fornecedor (decisão de negócio, não de estudo).

---

## 🔗 Documentos relacionados
- [[stack-tecnologica-por-sistema]] — a mesma stack, organizada por sistema em vez de por categoria
- [[revisao-stack-tecnologica]] — o corte entre o que é decisão de fornecedor e o que é estudo genuíno
- [[plano-estudos-basico-avancado-entrelacado]] — onde cada tecnologia desta lista entra no cronograma de estudo
- [[trilha-42-circles-oficial-verificado]] — C/C++ como bloco de linguagem adicional, fora desta lista de stack padrão
- [[agileflow-decisao-stack-portfolio]] — GraphQL via HotChocolate no próprio .NET, revisado a partir da versão anterior (React/Node/GraphQL completo)
