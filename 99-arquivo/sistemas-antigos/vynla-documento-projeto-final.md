---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# Momentos/Cupido — Documento de Projeto Final

Segue a estrutura fixa definida no [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md). Consolida o PRD de 17 seções já existente, cruzado com o rigor aplicado aos outros 5 sistemas do portfólio.

---

## 1. Visão do produto

Plataforma que acompanha um casal do primeiro "sim" até os grandes marcos da vida a dois — combinando um motor de páginas de pedido viral (namoro, casamento, madrinha/padrinho, revelação de gênero, aniversário, reconciliação), um sistema privado de compatibilidade e planejamento (Cupido), e um site permanente que cresce com a relação (Site da Vida a Dois).

**Diferencial de inovação:** nenhum concorrente pesquisado combina essas três camadas — a maioria resolve só "página de pedido bonita" (produto descartável, usado uma vez) ou só "app de casal" (Between e similares). Aqui a página de pedido é a porta de entrada, mas o produto continua crescendo com o casal ao longo dos anos, o que muda o modelo de receita de pagamento único para recorrência de longo prazo.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Motor de Momentos
- 6+ templates de página (namoro, casamento, madrinha/padrinho, revelação de bebê, aniversário, reconciliação), reaproveitando a mesma base técnica
- Botão "Não" que foge do toque, celebração com confete ao "Sim"
- Linha do tempo com metadados ricos por foto: data, local, ocasião, descrição de sentimento de cada parceiro lado a lado
- Trilha sonora via player oficial embutido do Spotify
- Cápsula do Tempo (mensagem que só abre numa data futura), contagem regressiva, revelação por geolocalização e "revelar agora" remoto (controle na hora, sem exigir local pré-definido)
- Selo de autenticidade: GPS + horário reais capturados no momento do pedido, não digitados depois — resolve o problema de autenticidade sem exigir que o local seja definido com antecedência

### 2.2 Cupido
- Perfil privado por pessoa (planos de vida, valores, gostos), nunca exposto em bruto ao parceiro
- Insights de compatibilidade gerados a partir dos dois perfis
- Metas e planejamento do casal: cofrinho de metas compartilhadas, contribuição individual com privacidade opcional, sugestão de aporte mensal — via `aura-goals` (compartilhado com o AM Rendara)

### 2.3 Meu Círculo
- Sistema de relacionamentos em 4 camadas, com isolamento técnico entre elas: notas privadas (nunca sai da camada estritamente privada), vínculos confirmados (exigem confirmação mútua, nunca unilaterais), árvore genealógica, preferências de presente declaradas pela própria pessoa
- Lembretes de data comemorativa e sugestão de presente via afiliados

### 2.4 Site da Vida a Dois
- Domínio próprio que acumula capítulos ao longo da relação — pedido, casamento, revelação de bebê, tudo no mesmo lugar, cronologicamente
- Controle de visibilidade por capítulo (público/privado)

### 2.5 Mural do Amor e Crescimento
- Feed público opt-in de celebrações, moderado com IA + revisão humana + hash-matching contra bancos de conteúdo abusivo (PhotoDNA/StopNCII)
- Card automático para Stories, contador de relacionamento (widget de bio), lista de presentes integrada, livro de recados colaborativo
- Mecânicas de crescimento: programa de indicação com recompensa real (desconto/período grátis), marca d'água como divulgação orgânica no plano gratuito, páginas públicas indexáveis no Google (SEO), programa de embaixadores com criadores de nicho, lembrete de reengajamento por data comemorativa

### 2.6 Produto físico
- Cartão NFC complementar — único ponto do sistema com componente físico e logística de envio (ver seção 7)

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Motor de template genérico, reutilizável entre os 6+ tipos de página | Evita reescrever a base técnica a cada novo tipo de momento lançado |
| RF02 | Captura de selo de autenticidade (GPS + horário) no momento da interação, não editável depois | É o diferencial competitivo central — perde valor se puder ser falsificado |
| RF03 | Revelação remota em tempo real ("revelar agora"), via mesma infraestrutura de notificação instantânea | Resolve o problema de quem não sabe o local do pedido com antecedência |
| RF04 | Perfil privado do Cupido, nunca exposto em bruto ao parceiro — só insight derivado | Preserva a genuinidade da resposta de compatibilidade; se exposto em bruto, vira jogo de agradar o parceiro, não avaliação real |
| RF05 | Meta compartilhada via `aura-goals`, com contribuição individual e privacidade opcional | Permite casal planejar objetivo financeiro comum sem forçar exposição total de dado individual |
| RF06 | Isolamento técnico entre as 4 camadas do Meu Círculo, com vínculo exigindo confirmação mútua | Impede que um usuário declare vínculo unilateral sobre terceiro sem consentimento dele |
| RF07 | Site da Vida a Dois com capítulo acumulativo e controle de visibilidade por capítulo | Sustenta o modelo de receita recorrente de longo prazo, diferente da página de pedido única |
| RF08 | Moderação híbrida do Mural do Amor (filtro automático + revisão humana + hash-matching) | Sem isso, um feed público de conteúdo de usuário sempre acaba virando canal de abuso |
| RF09 | Programa de indicação com recompensa real, mensurável por conversão | É o motor de aquisição orgânica de novo usuário, sem depender só de mídia paga |
| RF10 | Página pública indexável (SEO técnico correto) | Cada página de pedido publicada vira potencial canal de descoberta de novo cliente |
| RF11 | Lembrete de reengajamento por data comemorativa | Traz o casal de volta ao produto meses/anos depois, sustentando a assinatura de longo prazo |
| RF12 | Emissão e ativação de cartão NFC físico, vinculado à conta do casal | Viabiliza o produto físico como extensão do digital, não como item avulso |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Quem propõe (cria a página)
- **Cadastro:** self-service, escolhe template e monta a página
- **Uso:** editor de página, captura de selo de autenticidade, gatilho de revelação remota
- **Suporte:** canal padrão do Grupo AMtech

### 4.2 Parceiro(a) que recebe
- **Cadastro:** geralmente entra depois, ao aceitar/responder — precisa de fluxo de "reivindicar" a própria conta vinculada à página recebida
- **Uso:** responde ao pedido, depois passa a coeditar o Site da Vida a Dois e usar o Cupido/Meu Círculo junto com o parceiro
- **Suporte:** mesmo canal padrão

### 4.3 Visitante do Mural do Amor (não é necessariamente usuário cadastrado)
- **Cadastro:** não exige conta para visualizar; exige para interagir (curtir, comentar)
- **Uso:** navega feed público, potencial conversão para novo cadastro (RF09/RF10)
- **Suporte:** canal de denúncia de conteúdo — obrigatório, não opcional, dado o risco de abuso de feed público

### 4.4 Moderador de conteúdo (interno — perfil que nenhum outro sistema do portfólio tem)
- **Cadastro:** não se aplica — você ou futura pessoa contratada especificamente para isso
- **Uso:** fila de revisão humana de conteúdo sinalizado pelo filtro automático, decisão de remoção/banimento
- **Lacuna:** esse painel de moderação **precisa existir antes do Mural do Amor entrar em produção**, diferente do painel de suporte técnico interno genérico (que é uma dívida comum a todo o portfólio) — aqui é pré-requisito de lançamento, não débito técnico aceitável

### 4.5 Suporte técnico interno
- Mesma lacuna recorrente do portfólio — ainda sem RF formal. Aqui soma-se ao 4.4: são dois painéis internos diferentes (suporte técnico geral vs. moderação de conteúdo), não devem ser confundidos como o mesmo painel.

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no Momentos/Cupido | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado de relacionamento (Cupido, Meu Círculo) é dado pessoal sensível por natureza afetiva/relacional | Cumpre obrigação legal; reduz dano em caso de vazamento de dado íntimo |
| RNFT07 (BOLA) | Rota de página/capítulo privado deve validar que só os donos da conta acessam, mesmo sabendo o ID | Impede acesso não autorizado a conteúdo privado do casal |
| RNFT-E02 (idempotência de pagamento) | Cobrança de assinatura (Cupido Premium, Site Legado) e pagamento único de página avulsa | Evita cobrança duplicada em reenvio de webhook |
| RNFT-S03/S04 (conexão entre sistemas) | Integração com `aura-goals` só com consentimento explícito de ambos os parceiros, nunca automática | Meta financeira compartilhada é dado sensível de dois usuários, não de um só |
| Moderação de conteúdo (próprio) | Todo conteúdo do Mural do Amor passa por filtro automático antes de publicação pública, com fila de revisão humana para caso sinalizado | Reduz exposição a conteúdo abusivo antes que ele fique público, não depois |
| Isolamento de camada (Meu Círculo, próprio) | Notas da camada privada nunca trafegam para nenhuma API ou view que sirva outro usuário além do dono | É o requisito técnico que sustenta a garantia de privacidade prometida ao usuário |
| Continuidade de longo prazo | Site da Vida a Dois precisa de garantia de retenção de dado por anos (é literalmente um produto de "legado"), diferente de qualquer outro sistema do portfólio | Perder capítulo acumulado de anos de relação é o pior cenário de falha possível deste produto especificamente |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no Momentos/Cupido |
|---|---|
| Dados | Dado afetivo/relacional é categoria sensível por natureza — mesmo sem ser "dado bancário" como no AM Rendara, um vazamento aqui tem dano reputacional e emocional real para o usuário |
| Conteúdo público (RNFT-S06 aplicado a moderação) | Hash-matching contra PhotoDNA/StopNCII precisa estar ativo antes do Mural do Amor sair do MVP — não é opcional, é o que evita a plataforma virar veículo de conteúdo abusivo |
| Conexão entre sistemas | `aura-goals` só conecta com consentimento mútuo explícito, credencial de escopo mínimo — mesmo padrão do resto do portfólio |
| Se a plataforma avançar para mensageria entre desconhecidos | Isso exige uma fase própria de segurança (verificação de idade, denúncia, bloqueio, moderação dedicada) — não deve ser adicionado de forma incremental ao MVP; é decisão que merece projeto de segurança à parte, não um RF a mais |
| Auditoria externa (RNFT-S06) | Prioridade alta antes do lançamento do Mural do Amor especificamente — é o componente com maior superfície de exposição pública do sistema |

---

## 7. Hardware, instalador e distribuição

**Majoritariamente não aplicável** — SaaS puro, sem instalador. **Exceção: o cartão NFC físico (seção 2.6)**, que precisa de:
- Fabricação e estoque do cartão (fornecedor a definir)
- Logística de envio nacional — candidato direto a reaproveitar o **Módulo de Logística e Envios** já especificado no AM Consertta, em vez de construir um fluxo de frete/rastreio próprio para este produto isolado

---

## 8. Deploy e CI/CD

Um ponto de atenção real aqui: o protótipo inicial deste sistema foi construído em **Node.js/Express/SQLite**, fora do stack fixo do portfólio (C#/.NET 10 + PostgreSQL). Isso precisa ser resolvido antes de qualquer desenvolvimento de produção — ou o protótipo é descartado e o sistema recomeça no stack padrão (Clean Architecture, .NET 10, PostgreSQL, mesmo Dockerfile multi-stage e pipeline GitHub Actions dos demais), ou existe uma decisão consciente de manter esse sistema fora do padrão, o que quebraria o princípio de reaproveitamento que rege todo o resto do portfólio. Recomendo a primeira opção.

---

## 9. Modelo de receita

| Fonte | Modelo | Ticket estimado |
|---|---|---|
| Página avulsa (motor de templates) | Pagamento único via Pix/cartão | R$ 14,90 – R$ 29,90 |
| Site Legado da Vida a Dois | Assinatura anual — domínio próprio + hospedagem + armazenamento crescente de fotos-memória | R$ 99 – R$ 199/ano |
| Cupido Premium | Assinatura mensal, um plano libera os dois parceiros | R$ 19,90 – R$ 34,90/mês |
| Comissão sobre presentes | Afiliados Amazon/Mercado Livre integrados ao fluxo pós-"sim" e ao Cupido | % por venda, sem custo extra ao cliente |
| Produto físico complementar | Venda direta de cartão/placa com NFC | R$ 39,90 – R$ 79,90 |
| Parcerias comerciais locais | Comissão por indicação (floriculturas, buffets, joalherias) | Variável, % por conversão |
| Marketplace de temas | Criadores terceiros publicam temas, plataforma retém comissão | % por venda de tema |
| White-label | Licenciamento da plataforma para outras marcas (B2B) | Contrato sob consulta |

**Nota de custo:** para o pagamento único de baixo ticket, atenção ao piso mínimo de tarifa de algumas adquirentes — pode consumir fatia desproporcional da margem em cobranças pequenas.

---

## 10. Status atual de desenvolvimento

Existe um **protótipo funcional** (Node.js/Express/SQLite) construído durante a fase de exploração do produto, além de demo animado em formato Stories e landing page com captura de waitlist. **Nenhum código no stack final do portfólio (.NET/PostgreSQL) foi escrito ainda** — ver decisão pendente na seção 8.

---

## 11. Pendências e decisões em aberto

1. **Migração do protótipo Node.js/SQLite para o stack fixo do portfólio** — decisão mais urgente deste documento (seção 8).
2. **Painel de moderação de conteúdo** (seção 4.4) — pré-requisito de lançamento do Mural do Amor, não débito técnico aceitável como o painel de suporte genérico.
3. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, com a distinção formal de que moderação de conteúdo (seção 4.4) continua sendo painel separado, não o mesmo `aura-support`.
4. **Fornecedor de fabricação do cartão NFC** — ainda não definido.
5. **Decisão formal de não avançar para mensageria entre desconhecidos** sem projeto de segurança dedicado — registrar como princípio de produto, não deixar como "talvez depois".
6. **Provedor de pagamento** para o piso mínimo de tarifa em cobrança de baixo ticket — mesma pendência transversal de gateway do restante do portfólio.
