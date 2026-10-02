---
tags: [planejamento, portfolio-ams]
tipo: planejamento
status: completo
---

# Status de Planejamento do Portfólio — o que já existe, o que falta, e o que se reaproveita de onde
### Revisado — a versão anterior deste documento estava desatualizada, listando como pendente coisas já resolvidas

> **Nota de revisão:** a versão anterior deste documento (seções 2 e 3) listava `aura-licensing`, `aura-goals`, `aura-copilot`, Loja Virtual e o "Módulo de Ordem de Serviço" como sem RF/RNF formal. Isso não é mais verdade — todos os 23 sistemas/serviços do portfólio já têm Documento de Projeto Final completo (11 seções, RF com coluna "para que serve"), verificado item por item. O que sobra de genuinamente pendente está na seção 2 abaixo, bem mais curta que antes.

---

## 1. Todos os 23 sistemas/serviços têm planejamento completo

13 sistemas de negócio (ver [[inventario-portfolio-atualizado]]) + 10 serviços compartilhados — todos com Documento de Projeto Final nas 11 seções do [[template-documento-projeto-final|template padrão]]: visão, funcionalidades, RF, interfaces por perfil, RNF, segurança, hardware/distribuição, deploy, modelo de receita, status, pendências.

**Únicos com desenvolvimento ativo:** AM Kaixara (Sprint 3-4, rumo a JWT). Todos os outros estão em planejamento completo, sem código.

**Sobre READMEs separados por sistema:** a preocupação antiga ("falta verificar se existe README-AM Rendara.md") não se aplica mais — este vault não usa README por sistema, o Documento de Projeto Final de cada um já cumpre esse papel sozinho.

---

## 2. O que sobra de genuinamente pendente (poucas coisas, nomeadas)

| Item | Onde está a pendência |
|---|---|
| Física básica do livro | Estrutura provisória até você comprar o livro e mostrar o sumário real — ver [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] |
| `aura-historico` (Clojure/Datomic) | Decisão de stack em aberto — mesma revisão que já foi feita no AM Taskoro (Event Sourcing com Marten resolveria sem sair do .NET), ainda não decidida — ver [[stack-tecnologica]] |
| Decisão de seguro/responsabilidade em trânsito do AM Consertta | Decisão de negócio, não técnica — sinalizada no próprio documento do AM Consertta, ainda não fechada |
| Vertical de Reprodução & Biotecnologia do AuraVet | Condicionada a uma decisão sua sobre atuação nessa área específica |
| Certificação CEA/CFP | Pré-requisito pra destravar a camada de consultoria do AM Rendara — não é lacuna de documento, é pré-requisito de carreira, já mapeado em [[plano-mestre-frentes-alan]] |

---

## 3. Mapa de reaproveitamento entre sistemas

| Componente/módulo | Origem (onde nasceu) | Reaproveitado em | O que precisa ser modificado no destino |
|---|---|---|---|
| **Clean Architecture (Domain/Application/Infrastructure/Api) + DDD** | Padrão definido para todo o ecossistema desde o início | Todos os sistemas, sem exceção | Nada estrutural — só as entidades de domínio mudam por sistema |
| **Autenticação JWT + BCrypt** (`aura-identity`) | AM Kaixara | Todos os sistemas do portfólio | Nada além de regras de perfil/permissão específicas de cada sistema |
| **`tenant_id` + Row-Level Security** | Definido na modularização/comercialização do AM Kaixara | Todos os sistemas SaaS do portfólio | Nenhuma mudança de padrão — só a política RLS por tabela em cada sistema novo |
| **`aura-licensing`** | Serviço compartilhado, com RF/RNF formal próprio | Todos os sistemas SaaS do portfólio | Grafo de dependência de módulos estendido pra cada sistema novo |
| **Interfaces trocáveis (`IFonteDeEstoque`, `IEmissorFiscal`, `IFonteDeMovimentacaoBancaria`, `IFonteDeReceita`)** | AM Kaixara/AM Rendara | Qualquer sistema que venda produto ou processe pagamento (AuraVet incluído) | AuraVet precisa de uma interface nova pra receita por procedimento/dose |
| **PostGIS** | Cogitado desde o início como "só onde há geolocalização" | AM Rotara (rota de entrega), AuraVet (atendimento domiciliar) | Vale desenhar o uso de forma compartilhável entre os dois, mesmo problema de fundo |
| **Cloudflare R2** | Momentos/Cupido (armazenamento de mídia) | AuraVet (laudos, imagens de exame, fotos de internação) | Nenhuma mudança — mesmo provedor, buckets/políticas diferentes |
| **SignalR (tempo real)** | AM Kaixara (dashboard) | AuraVet (status de internação ao vivo) | Nenhuma mudança de tecnologia — só eventos/hubs específicos |
| **Módulo de Ordem de Serviço** | Assistência técnica → formalizado dentro de [[consertta-sistema-assistencia-tecnica|AM Consertta]] | Base do módulo de atendimento do AuraVet | Já é base de código real, não mais conceitual |
| **`aura-goals`** | Momentos/Cupido ↔ AM Rendara, com RF/RNF formal próprio | Nenhum outro sistema do momento | Sem uso adicional previsto |

---

## 🔗 Documentos relacionados
- [[inventario-portfolio-atualizado]] — lista completa dos 23 sistemas/serviços com status
- [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] — ordem de estudo/desenvolvimento de tudo isso
- [[plano-mestre-frentes-alan]] — formas de renda de cada frente, incluindo os sistemas deste portfólio
