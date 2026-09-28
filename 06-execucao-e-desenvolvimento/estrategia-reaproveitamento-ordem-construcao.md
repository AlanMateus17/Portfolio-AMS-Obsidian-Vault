---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# Estratégia de Reaproveitamento e Ordem de Construção
### Como fazer cada sistema depois do primeiro custar uma fração do tempo do anterior

---

## O reframe que precisa vir primeiro

"Desenvolver ao mesmo tempo" tem duas leituras possíveis, e só uma é real pra um desenvolvedor solo:

- **Leitura errada:** codar os 21 sistemas em paralelo, literalmente. Impossível — você só consegue escrever código num lugar por vez.
- **Leitura real, e é essa que este documento resolve:** construir uma **fundação reaproveitável de verdade** (não só "parecida"), de forma que o sistema #2 leve uma fração do tempo do #1, o #3 uma fração do #2, e por aí em diante. Isso é o que empresa de software de verdade chama de "plataforma interna" — e é inteiramente possível pra você, dado que 19 dos 21 sistemas já compartilham a mesma base técnica.

O AM Kaixara continua sendo o primeiro sistema a construir (nada muda no seu plano de estudo já existente) — o que muda é **o que fazer logo depois dele estar pronto**, antes de começar o segundo sistema.

---

## A etapa que ninguém pula sem querer, mas que é a mais importante: extração

Isso é o ponto central deste documento. Enquanto você constrói o AM Kaixara (Fases 0-6C do plano de estudo), a Clean Architecture, a autenticação JWT, o sistema de tokens de design — tudo isso nasce **dentro do AM Kaixara**, específico dele. Reaproveitamento de verdade não acontece sozinho só porque o código é parecido — precisa de um passo deliberado de **extrair** essa base pra fora do AM Kaixara, transformando-a em algo instalável/importável pelos próximos sistemas. Sem esse passo, "reaproveitar" vira "copiar e colar", que é exatamente o retrabalho que você está tentando evitar.

**Esse passo de extração é trabalho novo, real, que precisa entrar no cronograma — não é grátis, mas se paga já no segundo sistema.**

---

## Ordem de construção por alavancagem (quanto cada peça acelera o restante)

### Tier 1 — Fundação universal (todos os 19 sistemas .NET dependem disso)

| # | O que extrair/construir | De onde vem | Impacto |
|---|---|---|---|
| 1 | **Template de projeto** (`dotnet new` customizado) com Clean Architecture já configurada (Domain/Application/Infrastructure/Api), `tenant_id`+RLS já no esqueleto | AM Kaixara, depois de pronto | Sistema novo nasce em minutos com a estrutura certa, não em dias montando pasta por pasta |
| 2 | **`aura-identity`** funcionando de verdade (não só documentado) | Extraído do JWT do AM Kaixara | Elimina reescrever autenticação nos outros 6 sistemas que ainda a implementam própria |
| 3 | **Pacote interno de multi-tenancy** (biblioteca com o filtro global de `tenant_id`, convenção de RLS) | Extraído do AM Kaixara | Isolamento correto "de graça" em todo sistema novo, sem reimplementar a regra |
| 4 | **Pipeline de CI/CD reutilizável** (GitHub Actions composite action ou template de workflow) | Extraído do AM Kaixara | Sistema novo herda build→teste→deploy funcionando, só troca o nome do projeto |
| 5 | **Component library de frontend com o sistema de tokens (RNFT-D01-D07)** | Extraído da tela de PDV do AM Kaixara | Todo painel/portal novo já nasce com a paleta e o contraste certos, sem reconstruir a base visual |

### Tier 2 — Infraestrutura usada por metade ou mais dos sistemas

| # | O que construir | Impacto |
|---|---|---|
| 6 | Cliente/SDK interno do `aura-licensing` | Ativar módulo comercial vira 3 linhas de configuração, não integração do zero |
| 7 | Cliente/SDK interno do `aura-notifications` | Notificação (WhatsApp/push/e-mail) vira uma chamada de método, não integração de API repetida |
| 8 | `aura-support` funcionando | Resolve a lacuna que apareceu em 9 documentos diferentes, uma vez só |
| 9 | **Biblioteca de concorrência/idempotência** (RNFT-E01/E02 como base de repositório genérica — atualização condicional, chave de idempotência) | Todo sistema que mexe em estoque/pagamento herda a proteção certa, sem reescrever a lógica de concorrência a cada vez |

### Tier 3 — Módulos de domínio, reaproveitados por grupos menores

| # | Módulo | Reaproveitado por |
|---|---|---|
| 10 | Ordem de Serviço | AM Consertta → AuraVet → AM Predara (manutenção) → AM Canteira (assistência pós-entrega) |
| 11 | Motor de agendamento genérico | AuraVet → AM Saberia → AM Horaria |
| 12 | `aura-vault` | AM Rendara, AuraVet, AM Horaria, AM Canteira |
| 13 | `aura-logistics` | AM Consertta, Loja Virtual, AuraVet, Momentos/Cupido |
| 14 | `aura-goals` | AM Rendara, Momentos/Cupido |

---

## Técnicas que você ainda precisa aprender pra fazer isso de verdade (não é intuitivo, é técnica específica)

### 1. Template de projeto customizado (`dotnet new`)
Empacotar uma estrutura de projeto inteira como template instalável (`dotnet new install`), com parâmetro (nome do projeto, etc.). É o que transforma "copiar uma pasta e trocar nome" (frágil, gera erro) em "comando que gera projeto correto sempre".

### 2. Pacote interno privado (NuGet privado / GitHub Packages)
Empacotar a biblioteca de multi-tenancy, o SDK do `aura-licensing`, a biblioteca de concorrência como pacotes NuGet versionados, hospedados em feed privado (GitHub Packages resolve isso sem custo adicional). Isso é diferente de "copiar arquivo de um projeto pro outro" — quando você corrige um bug na biblioteca, todo sistema que a usa atualiza com um `dotnet add package` numa versão nova, não com busca-e-substitui manual em 21 lugares.

### 3. Monorepo vs. polyrepo (decisão a tomar, não default automático)
Com 21 sistemas + bibliotecas compartilhadas, vale decidir cedo: um repositório Git só pra tudo (monorepo, mais fácil de coordenar mudança que afeta vários sistemas de uma vez) ou um repositório por sistema (polyrepo, mais isolado, mas exige versionamento de pacote mais disciplinado). Não existe resposta certa universal — mas decidir cedo evita migração dolorosa depois.

### 4. Geração de código (scaffolding, opcional/avançado)
Depois que o padrão de CRUD se repetir várias vezes (entidade → repositório → controller → teste), vale considerar uma ferramenta simples de geração de código (mesmo que um script CLI seu, não precisa ser Roslyn Source Generator sofisticado no início) que gera o esqueleto a partir da definição da entidade. Isso é otimização de última milha — só vale depois que o padrão já se repetiu 3-4 vezes de verdade, não antes.

### 5. Feature flag / module gating como padrão formal
Você já tem isso descrito no `aura-licensing` (ativar módulo por `tenant_id`) — a técnica geral por trás disso (feature flag) vale entender como padrão nomeado, porque aparece de novo em outros contextos (ativar funcionalidade nova gradualmente, não só cobrar por módulo).

---

## Onde isso se encaixa no plano de estudo já existente

Não é uma fase nova separada — é o que você faz **entre** o fim da Fase 6C (AM Kaixara pronto, sênior) e o início do próximo sistema (AM Rotara, Fase 5 do plano de estudo). Chame isso de:

**Fase 6D — Extração da plataforma interna (nova, 2-3 semanas, depois do AM Kaixara em produção, antes do AM Rotara começar)**

Conteúdo: os 5 itens do Tier 1, priorizados nessa ordem. Não é opcional se o objetivo é "reduzir tempo de todos os sistemas" — é literalmente o mecanismo que produz essa redução. Pular essa fase significa que cada sistema novo vai continuar custando quase o mesmo tempo do anterior, porque nada foi de fato extraído pra reaproveitar.

---

## O que isso muda na prática, com número honesto

Sem essa extração, o AM Rotara provavelmente custaria quase o mesmo tempo de estudo+desenvolvimento que o AM Kaixara custou — porque você reescreveria autenticação, estrutura de projeto, multi-tenancy do zero, mesmo já sabendo fazer.

Com a extração feita, o AM Rotara herda tudo isso pronto — o tempo dele fica concentrado só no que é genuinamente novo dele (PostGIS, roteirização, SignalR de pedido). O terceiro sistema (AM Rendara ou o que vier depois) herda ainda mais, porque a biblioteca de concorrência e o `aura-support` já existem também.

**Isso é o que "desenvolver todos ao mesmo tempo" significa de verdade para quem trabalha sozinho: não é simultaneidade, é aceleração composta** — cada sistema deixando o próximo mais barato, não porque fica mais fácil, mas porque menos coisa precisa ser reconstruída.
