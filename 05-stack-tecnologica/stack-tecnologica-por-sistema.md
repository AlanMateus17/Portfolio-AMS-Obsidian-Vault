---
tags: [stack, portfolio-ams]
tipo: stack
status: completo
---

# Stack Tecnológica por Sistema
### O que cada um dos 21 sistemas/serviços usa, e o que é específico dele

---

## Sistemas de negócio

### AM Kaixara
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers, Clean Architecture + DDD |
| Banco | PostgreSQL |
| Cache | Redis |
| Tempo real | SignalR |
| Frontend | Next.js, TypeScript, Tailwind |
| **Específico** | Agente local (.NET, Windows Service) com `IImpressoraFiscal` (ESC/POS), `IGavetaDinheiro`, `IBalanca` (porta serial), `ITefService`; SQLite local para modo offline; instalador MSIX/WiX com Code Signing |

### AM Rotara
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL + **PostGIS** |
| Cache | Redis |
| Tempo real | SignalR |
| **Específico** | Consome `aura-analytics` (Google OR-Tools) para roteirização; apps de entregador/cliente (PWA vs. nativo — pendente) |

### AM Rendara
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL |
| **Específico** | Consome `aura-vault` (criptografia AES-256 de dado bancário); consome `aura-historico` (Datomic) para simulação especulativa "e se"; consome `aura-analytics` (Prophet/statsmodels) para projeção patrimonial; motor de regra determinística (ARCA/Barsi/Value Investing) em C# puro, sem dependência externa |

### AuraVet
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL + **PostGIS** (atendimento domiciliar/campo) |
| Armazenamento de arquivo | Cloudflare R2 (laudo, imagem de exame) |
| **Específico** | Consome `aura-vault` (prontuário clínico); consome `aura-licensing`; app do tutor em Next.js PWA (nativo pendente) |

### AM Consertta
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL |
| **Específico** | Reaproveita motor de PDV/estoque do AM Kaixara; consome `aura-logistics` (frete/rastreio); consome `aura-notifications` |

### Momentos/Cupido
| Camada | Tecnologia |
|---|---|
| Backend (alvo) | C#/.NET 10, ASP.NET Core Controllers — **hoje existe protótipo em Node.js/Express/SQLite, migração pendente** |
| Armazenamento de arquivo | Cloudflare R2 (foto, mídia do Mural do Amor) |
| **Específico** | Consome `aura-goals`; moderação de conteúdo via hash-matching (PhotoDNA/StopNCII) + revisão humana; player Spotify embutido |

### Loja Virtual
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers (módulo do AM Kaixara) |
| **Específico** | Sem stack próprio — é extensão direta do AM Kaixara; consome `aura-logistics` |

### AM Predara
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL |
| **Específico** | Agente local de portaria (protocolo a definir com fornecedor de hardware — interfone IP/RFID/fechadura eletrônica); votação eletrônica com log de auditoria imutável (candidato a integrar `aura-historico`) |

### AM Canteira
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL |
| **Específico** | Consome `aura-vault` (documento contratual); integração de assinatura eletrônica (DocuSign/Clicksign/D4Sign — pendente); app de campo da equipe de obra com modo offline básico |

### AM Saberia
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL |
| **Específico** | Integração de videoaula síncrona (Zoom/Meet, ou solução própria — pendente); consome `aura-logistics` para material físico; consome `aura-licensing` para o canal B2B |

### AM Horaria
| Camada | Tecnologia |
|---|---|
| Backend | C#/.NET 10, ASP.NET Core Controllers |
| Banco | PostgreSQL, com **segregação de schema** para o módulo de prontuário psicológico |
| **Específico** | Consome `aura-vault` com isolamento reforçado (prontuário psicológico); consome `aura-logistics` para produto |

---

## Serviços compartilhados

### `aura-licensing`
C#/.NET 10, PostgreSQL. Integração com plataforma de cobrança recorrente (Stripe Billing/Vindi/Iugu/Asaas — pendente).

### `aura-goals`
C#/.NET 10, PostgreSQL. Sem dependência externa nova — consumido via API por AM Rendara e Momentos/Cupido.

### `aura-historico`
**Clojure + Datomic** (fora do stack .NET). Consumido via Redis Streams (evento) por qualquer sistema, hoje principalmente AM Rendara.

### `aura-analytics`
**Python + FastAPI** (fora do stack .NET). Bibliotecas: **Prophet** ou **statsmodels** (previsão de demanda), **Google OR-Tools** (roteirização/VRP).

### `aura-copilot`
Provedor de modelo de linguagem ainda não decidido (API externa como Anthropic/OpenAI vs. auto-hospedado). Arquitetura de function-calling, sem RAG.

### `aura-identity`
C#/.NET 10, PostgreSQL. JWT centralizado, 2FA opcional por tenant.

### `aura-notifications`
C#/.NET 10, PostgreSQL. Integração com WhatsApp Business API (oficial Meta ou BSP — pendente), provedor de SMS/e-mail transacional (pendente).

### `aura-support`
C#/.NET 10, PostgreSQL. Painel web interno, acesso restrito por VPN/IP allowlist.

### `aura-logistics`
C#/.NET 10, PostgreSQL. Integração com Correios/transportadora privada (pendente).

### `aura-vault`
C#/.NET 10. Integração com **KMS/HSM gerenciado** (AWS KMS, Azure Key Vault ou HashiCorp Vault — pendente), integrado ao `aura-historico` para trilha de auditoria.

---

## Ferramentas pessoais produtizáveis (fora da numeração dos 21 sistemas/serviços — ver [[painel-central-arquitetura-todas-fases]])

### `aura-status`
C#/.NET 10, console app. Sem banco de dados — lê Git local, arquivo de log, `gh` CLI. Multi-provedor futuro (GitHub/GitLab/Bitbucket) via `IFonteDeStatus`.

### `aura-queue`
C#/.NET 10, em memória ou sobre o Redis já usado no stack — sem dependência nova.

### `aura-secrets`
C#/.NET 10, PostgreSQL, criptografia local — sem dependência externa (diferente do `aura-vault` acima, que integra KMS/HSM gerenciado).

### `aura-oncall`
C#/.NET 10 — extensão do `aura-notifications`, sem stack nova.

---

## Tecnologias explicitamente fora do portfólio (decisão já tomada)

Bun, Hono, Rust, Tauri, gRPC — mantido em todos os 21 documentos, nenhuma exceção encontrada na revisão.

---

## 🔗 Documentos relacionados
- [[stack-consolidada-estudo]] — a mesma stack, agora organizada por categoria pra estudo
- [[revisao-stack-tecnologica]] — quais dessas tecnologias são realmente necessárias vs. adiáveis
- [[kaixara-documento-projeto-final|AM Kaixara]] — o sistema onde a maior parte dessa stack é usada primeiro
