---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AuraArquiteto — Documento de Projeto Final
### 23º sistema do portfólio — encontrado numa conversa separada, formalizado agora no padrão canônico dos demais

---

## 1. Visão do produto

Sistema de diagnóstico de setup e geração de arquitetura por IA, escalável — o cliente preenche um formulário adaptativo por perfil, e recebe um relatório personalizado de arquitetura de infraestrutura (workstation, rede, hospedagem, segurança, etc.) sem intervenção manual.

**Diferencial:** monetização em camadas por venda única — taxa do relatório, comissão de afiliado sobre produto recomendado, upsell de kit físico pré-configurado, e assinatura recorrente de manutenção. Reaproveita a infraestrutura de serviços compartilhados já validada no portfólio, sem duplicar nenhum deles.

**Público-alvo:** gamers/streamers, devs/freelancers, pequeno empresário, criador de conteúdo, produtor rural, day trader caseiro, família, trabalhador remoto, oficina automotiva, escola.

---

## 2. Funcionalidades completas (estado final)

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Diagnóstico | Formulário adaptativo por perfil/persona; cálculo de Gap Score | Novo |
| Base de Conhecimento | CRUD versionado de regras; fluxo de aprovação antes de publicar | Novo |
| Geração | Orquestra chamada ao motor de IA e monta o relatório estruturado | Novo (lógica) + `aura-copilot` (acesso à IA) |
| QA Automático | Valida orçamento, disponibilidade de produto, coerência regional | Novo |
| Renderização de Documento | Gera `.docx`/PDF com a marca do cliente | Novo |
| Catálogo & Afiliados | Produto vinculado a recomendação, link e comissão | Novo |
| Config Forge | Gera arquivo de configuração do instalador automatizado | Novo |
| Kits Físicos | Gestão de estoque e expedição de hardware pré-configurado | Novo (domínio) + `aura-logistics` (envio) |
| Acompanhamento (Outcomes) | Checklist de execução + follow-up 7/30/90 dias | Novo (lógica) + `aura-notifications` (disparo) |
| Painel Administrativo | Fila de amostragem, edição de regra, métricas | Novo (telas) + `aura-analytics` (coleta) |
| Autenticação | Login de cliente e admin | 100% reaproveitado — `aura-identity` |
| Cobrança recorrente | Assinatura de manutenção | 100% reaproveitado — `aura-licensing` |
| Proteção de dado sensível | Criptografia de dado de rede/financeiro do cliente | 100% reaproveitado — `aura-vault` |

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve | Origem |
|---|---|---|---|
| RF01 | Formulário adaptativo de diagnóstico por perfil/persona | Coleta os dados certos por tipo de cliente, sem formulário genérico que perde precisão | Novo |
| RF02 | Cálculo automático de Gap Score a partir das respostas | Traduz resposta bruta em prioridade objetiva de investimento, sem julgamento manual | Novo |
| RF03 | CRUD versionado de regras da Base de Conhecimento | Permite atualizar recomendação sem reescrever código, mantendo histórico de mudança | Novo |
| RF04 | Fluxo de aprovação obrigatório antes de publicar nova regra | Impede que uma regra errada vá pro ar sem revisão — ela impacta recomendação real de compra | Novo |
| RF05 | Orquestração da chamada ao motor de IA e montagem do relatório estruturado | É o núcleo do produto — transforma diagnóstico bruto em relatório pronto pro cliente | Novo (lógica) + `aura-copilot` |
| RF06 | QA automático de orçamento, disponibilidade de produto e coerência regional | Impede entregar relatório recomendando produto fora de estoque ou fora do orçamento informado | Novo |
| RF07 | Renderização do relatório em `.docx`/PDF com a marca do cliente | Entrega final apresentável, sem trabalho manual de formatação | Novo |
| RF08 | Vínculo entre item recomendado no relatório e produto de afiliado rastreável | Habilita a receita de comissão sem acompanhamento manual | Novo |
| RF09 | Rastreio de conversão de link de afiliado por relatório emitido | Mostra quanto cada relatório efetivamente gerou de receita de comissão | Novo |
| RF10 | Geração de arquivo de configuração do instalador automatizado (Config Forge) | Reduz o setup do kit físico recomendado a um único arquivo, sem instalação manual passo a passo | Novo |
| RF11 | Gestão de estoque de kit físico pré-configurado | Evita vender um kit que não existe fisicamente disponível | Novo |
| RF12 | Expedição de kit físico via integração com `aura-logistics` | Reaproveita o motor de frete/rastreio já validado, sem recriar logística do zero | Reaproveitado |
| RF13 | Checklist de execução do plano recomendado | Dá ao cliente um caminho concreto de implementação, não só um relatório pra ler e esquecer | Novo |
| RF14 | Job agendado de follow-up em 7/30/90 dias após entrega do relatório | Mantém engajamento pós-venda e abre oportunidade de upsell de manutenção | Novo |
| RF15 | Fila de amostragem manual de relatório gerado, para revisão de qualidade | Detecta erro sistemático da IA antes que vire padrão recorrente de reclamação | Novo |
| RF16 | Painel de métricas de uso e conversão (relatórios gerados, conversão de afiliado, follow-up concluído) | Dá visibilidade de negócio sem precisar consultar banco de dado direto | Novo |
| RF17 | Cobrança recorrente de manutenção via assinatura | Sustenta receita recorrente além da venda única do relatório | Reaproveitado — `aura-licensing` |
| RF18 | Login de cliente e administrador | Protege acesso ao relatório pessoal (dado financeiro) e ao painel de gestão | Reaproveitado — `aura-identity` |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

| Perfil | Interface/fluxo | Caminho completo |
|---|---|---|
| Cliente comprador | Formulário público + Área do Cliente | Formulário → pagamento → relatório na área do cliente → checklist marcável → suporte |
| Alan/Admin | Painel de gestão | Edita Base de Conhecimento → aprova mudança → acompanha QA → vê métricas |
| Suporte (interno) | Fila do `aura-support` vinculada ao relatório | Recebe ticket → contexto automático → responde → registra resolução |
| Parceiro de afiliado (futuro) | Painel de indicação | Fora do escopo do MVP — mapeado pra não travar a arquitetura de dado |

---

## 5. Requisitos Não Funcionais (RNF) — próprios e transversais

Este sistema **origina** a série transversal `RNFT-IA01–04` (governança de geração por IA), aplicável a qualquer sistema futuro do portfólio que gere conteúdo pra cliente final via IA — ver [[rnft-ia-governanca-geracao-ia]] pro detalhamento completo de cada item.

| ID | Aplicação no AuraArquiteto | Para que serve |
|---|---|---|
| RNFT-IA01 (validação estrutural / golden file) | Todo relatório gerado por IA passa por comparação de schema contra a Base de Conhecimento antes de ser entregue | Garante que a IA não "alucine" uma estrutura fora do padrão esperado |
| RNFT-IA02 (QA automático de coerência) | Validação de orçamento, disponibilidade e coerência regional (RF06) roda antes da entrega, nunca depois | Impede que um erro de coerência chegue até o cliente final |
| RNFT-IA03 (amostragem manual periódica) | Fila de amostragem (RF15) — parcela dos relatórios revisada manualmente por semana | Detecta erro sistemático que passou pelo QA automático |
| RNFT-IA04 (acompanhamento pós-entrega estruturado) | Follow-up agendado 7/30/90 dias (RF14) | Garante que a recomendação da IA teve resultado real, não só geração pontual |
| RNFT06 (LGPD) | Dado de rede/financeiro do cliente coletado no diagnóstico é dado sensível | Cumpre obrigação legal e evita exposição indevida de informação financeira/de infraestrutura do cliente |
| RNFT07 (BOLA) | Toda rota que acessa relatório por ID deve validar que o cliente autenticado é o dono daquele relatório específico | Impede que um cliente veja o relatório (com dado financeiro) de outro só trocando o ID na URL |
| RNFT-S01 (assinatura de código) | Se o Config Forge (RF10) acompanhar instalador executável, este deve ser assinado digitalmente | Evita que o instalador seja bloqueado por antivírus ou gere desconfiança no cliente |
| RNFT-E05 (observabilidade) | Falha no job agendado de follow-up (RF14) ou na chamada ao motor de IA (RF05) gera log estruturado + alerta | Evita que um follow-up simplesmente não aconteça, sem ninguém perceber |

---

## 6. Segurança de nível profissional

Proteção de dado de rede/financeiro do cliente via `aura-vault` (100% reaproveitado, mesma camada de isolamento já aplicada a AuraWealth/AuraVet/AuraAgenda/AuraObra). Teste `xUnit` "golden file" comparando estrutura gerada por IA contra o schema esperado da Base de Conhecimento — satisfaz RNFT-IA01.

---

## 7. Hardware, instalador e distribuição

**Config Forge** gera arquivo de configuração pro instalador automatizado do kit físico recomendado — é a única ponte do sistema com hardware real, sem agente local próprio (diferente do AuraPOS).

---

## 8. Deploy e CI/CD

Padrão do portfólio (Docker, GitHub Actions/Gitea Actions), sem desvio.

---

## 9. Modelo de receita — todas as formas de venda

| Fonte | Modelo |
|---|---|
| Relatório | Taxa única por diagnóstico |
| Comissão de afiliado | Sobre produto recomendado no relatório |
| Kit físico | Upsell de hardware pré-configurado |
| Manutenção recorrente | Assinatura via `aura-licensing` |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito.** Documentação completa produzida em conversa separada (13/08), nunca antes formalizada neste vault.

---

## 11. Pendências e decisões em aberto

1. **Pré-requisito explícito de sequência, já registrado como trava formal no Backlog EPIC-AA01:** não começar antes de `aura-copilot` estar validado com uso real em outro sistema (ex: AuraPOS), e `aura-licensing` já cobrando de verdade em pelo menos um sistema
2. **Fase 0 jurídica específica** (CNPJ, contrato, seguro de responsabilidade profissional, LGPD) deve rodar em paralelo à maturação técnica acima, não depois dela
3. Stack com 4 adições específicas sobre o padrão do portfólio: `DocumentFormat.OpenXml` (geração de `.docx`), `QuestPDF` (PDF), `System.Text.Json` + `FluentValidation` (validação de saída de IA), `Hangfire` ou `Quartz.NET` com armazenamento Redis (job agendado pro follow-up 7/30/90 dias)

---

## 🔗 Documentos relacionados
- [[rnft-ia-governanca-geracao-ia]] — a série transversal nova que este sistema origina, reaproveitável por qualquer sistema futuro com IA voltada ao cliente final
- [[aura-copilot-documento-projeto-final]] — pré-requisito de validação antes do Backlog EPIC-AA01 começar
- [[inventario-portfolio-atualizado]] — posição deste sistema no portfólio de 23
