---
tags: [transversal, portfolio-ams]
tipo: regra-transversal
status: completo
---

# Distribuição, Licenciamento e Segurança de Nível Profissional
### Documento transversal — aplicável a todo sistema do portfólio vendido como executável instalável, e à segurança de todos os sistemas, cloud ou local

---

## 0. Duas decisões de arquitetura antes de qualquer funcionalidade

### 0.1 Modelo de distribuição passa a ser híbrido
Até agora todo o portfólio foi pensado como SaaS puro (cloud, multi-tenant). Vender como "pacote de arquivos executável que qualquer pessoa instala no computador" é um modelo de distribuição diferente — **on-premise** — e isso não substitui o SaaS, os dois vão coexistir:
- **AM Kaixara** é o candidato natural a essa distribuição híbrida, porque já depende de um agente local para hardware (impressora fiscal, gaveta, balança, TEF) — esse agente local É basicamente a metade do caminho para um instalador completo
- Sistemas puramente cloud (AM Rendara, Momentos/Cupido, AuraVet) não precisam de instalador — continuam SaaS, acessados via navegador; a distribuição executável se aplica especificamente a sistemas com componente físico/local, e AM Kaixara/AM Consertta são os que se encaixam nesse perfil

### 0.2 Precisa de uma identidade central de cliente (conta Aura única)
Para "conectar o AM Kaixara com o outro sistema online que a pessoa comprou", é preciso que exista uma conta única do cliente que sabe quais produtos ele comprou — hoje o `aura-licensing` sabe quais módulos um `tenant_id` tem ativo, mas não existe ainda o conceito de **uma pessoa dona de múltiplos tenants/produtos diferentes do portfólio**. Isso é uma peça nova, e ela nasce dentro do próprio `aura-licensing` (ou como extensão dele), não como serviço separado.

---

## 1. Pacote executável instalável (foco inicial: AM Kaixara)

### 1.1 O que o instalador contém
- Agente local (já especificado no documento final do AM Kaixara) empacotado como serviço Windows
- Runtime necessário embutido ou verificado na instalação (evita depender do cliente já ter .NET instalado)
- Banco local (SQLite, já previsto para o modo offline) pré-configurado
- Assistente de instalação com poucos passos: inserir chave de licença → validar online → configurar impressora/gaveta/balança conectados → pronto

### 1.2 Empacotamento
- Instalador Windows via **MSIX** (formato moderno, com melhor integração de atualização automática) ou **WiX Toolset** (mais controle, mais maduro) — decisão a tomar antes de construir, ambos são caminhos válidos
- **Assinatura de código (Code Signing / Authenticode)** — obrigatório, não opcional: sem isso, o Windows SmartScreen marca o instalador como não confiável e a maioria dos clientes vai simplesmente desistir da instalação por medo. Exige certificado de assinatura de código de uma autoridade reconhecida.

### 1.3 Licenciamento e ativação
- Chave de licença gerada na compra, vinculada ao `tenant_id` e à conta do cliente no `aura-licensing`
- Ativação online no primeiro uso (chama o `aura-licensing` para validar e vincular a chave a uma "impressão" da máquina/instalação — evita uma chave ativada em várias instalações simultâneas)
- **Validação com tolerância offline**: já que o PDV precisa funcionar offline por até 4h (requisito já definido), a licença precisa continuar válida localmente por um período de graça (ex: 7-14 dias sem contato com o servidor) antes de bloquear o uso — nunca travar o caixa do cliente no meio de uma venda por falha de rede na verificação de licença
- Atualização automática do agente local (canal de update assinado, mesmo princípio do code signing)

### 1.4 Honestidade sobre proteção de licença
Nenhum mecanismo de proteção de licença é inquebrável — engenharia reversa de software local sempre é tecnicamente possível para quem tem motivação e tempo suficientes. O que é realista e vale implementar: dificultar o suficiente para que copiar/burlar não seja trivial (ofuscação do agente local, verificação de integridade do binário, validação periódica online), não prometer a você mesmo que será impossível.

---

## 2. Compra online e configuração final

### 2.1 Fluxo de compra
- Loja Virtual (já no portfólio) vira também a **vitrine de venda dos seus próprios produtos de software** — não só produto físico de terceiros
- Checkout gera a chave de licença automaticamente e envia o instalador (ou link de download) por e-mail

### 2.2 Configuração final pós-compra (wizard web)
- Após pagamento, cliente acessa um painel web de configuração antes ou depois de instalar: nome do negócio, CNPJ, filiais, escolha de emissor fiscal
- Esse painel já provisiona o `tenant_id` e ativa os módulos comprados no `aura-licensing`, para que quando o instalador rodar localmente, ele só precise buscar essa configuração já pronta

### 2.3 Conexão entre sistemas comprados (o pedido específico seu)
- Na conta única do cliente (item 0.2), ele vê todos os produtos do portfólio que possui
- Um botão de "conectar" entre dois produtos (ex: AM Kaixara local + AM Rendara cloud) dispara um fluxo de autorização — o cliente aprova explicitamente a conexão, o sistema gera uma credencial de integração (API key ou token com escopo limitado, nunca a senha da conta), e a partir daí o `FonteReceitaAM Kaixara` (já especificado no AM Rendara) passa a alimentar o fluxo de caixa automaticamente
- Esse consentimento explícito do cliente antes de conectar dois sistemas é requisito de segurança e também de LGPD — nunca conectar automaticamente sem ação do cliente

---

## 3. Segurança de nível profissional — checklist por categoria

Organizado do jeito que uma auditoria de segurança de verdade organizaria: não é uma lista de "features", é postura em cada camada.

### 3.1 Código e desenvolvimento (Secure SDLC)
- Scan de dependência vulnerável automatizado no pipeline (Dependabot/Snyk ou equivalente) — vocês já encontraram e corrigiram 2 CVEs reais no AM Kaixara; isso deveria ser automático a cada build, não descoberto manualmente
- SAST (análise estática de código) no CI/CD, antes de qualquer merge
- Nunca segredo/senha hardcoded — já foi corrigido uma vez nos `docker-compose.yml`; formalizar isso como gate automático de CI (falha o build se detectar segredo em texto plano)
- Revisão de código obrigatória em qualquer mudança que toque autenticação, pagamento ou dado sensível

### 3.2 Instalador e agente local (superfície física/on-premise)
- Assinatura de código (já detalhado acima)
- Agente local rodando com o **menor privilégio possível** — não pedir permissão de administrador além do estritamente necessário para acessar hardware
- Verificação de integridade do binário na inicialização (detecta alteração/tampering)
- Canal de atualização automática assinado e verificado

### 3.3 Rede e API
- TLS obrigatório em qualquer comunicação (já implícito no stack, mas vale formalizar como requisito não negociável)
- Autenticação JWT com expiração curta + refresh token, rate limiting por IP/tenant em endpoints sensíveis (login, pagamento)
- Princípio de menor privilégio também na API: cada token/chave de integração (item 2.3) com escopo mínimo necessário, nunca acesso total por padrão

### 3.4 Dados
- Criptografia em repouso para dado sensível (banco local SQLite do agente pode usar SQLCipher; banco cloud já deve ter criptografia em disco no provedor)
- `tenant_id` + Row-Level Security (já no padrão do portfólio) como camada adicional de isolamento, não a única
- Backup criptografado e testado (não só existir — testar restauração periodicamente)

### 3.5 Operação e monitoramento
- Reaproveita diretamente o RNFT-E05 (observabilidade/alerta) já definido no documento transversal de escala — log estruturado de tentativa de acesso suspeita, não só de operação financeira
- Plano de resposta a incidente por escrito, mesmo que simples: o que fazer nas primeiras horas se uma chave vazar ou uma conta for comprometida

### 3.6 O item que nenhum documento interno substitui: auditoria externa real
Isso é o ponto mais importante desta seção. Tudo acima é o que reduz a superfície de ataque — mas "as boas práticas que uma empresa de PenTest aplica" inclui, por definição, **uma pessoa de fora tentando invadir de propósito**, coisa que nenhum checklist interno reproduz sozinho. Antes de vender o AM Kaixara como instalador para o público (não só como MVP de portfólio), vale contratar um pentest externo real — mesmo que pontual e de escopo pequeno no início — porque é o único jeito de validar que as proteções acima realmente seguram na prática, não só no papel.

---

## 4. Requisitos formais novos (referenciáveis pelos outros documentos)

| ID | Requisito |
|---|---|
| RNFT-S01 | Todo executável distribuído publicamente deve ser assinado digitalmente (code signing) antes do lançamento |
| RNFT-S02 | Toda licença deve validar online na ativação e manter um período de graça offline definido (mínimo 7 dias) antes de bloquear uso |
| RNFT-S03 | Toda conexão entre dois sistemas do portfólio pertencentes ao mesmo cliente deve exigir consentimento explícito do cliente, nunca ligação automática |
| RNFT-S04 | Toda credencial de integração entre sistemas deve ter escopo mínimo necessário, nunca acesso total por padrão |
| RNFT-S05 | Todo pipeline de CI/CD deve incluir scan automatizado de dependência vulnerável e falhar o build em caso de segredo exposto em texto plano |
| RNFT-S06 | Antes de qualquer lançamento público (não-portfólio) de um sistema, deve haver ao menos um pentest externo de escopo definido |

---

## 5. Impacto direto no AM Kaixara (documento de projeto final)

Este documento adiciona ao AM Kaixara, além do que já estava consolidado:
- Empacotamento como instalador Windows assinado (novo bloco de trabalho, além do agente local já previsto)
- Licenciamento com ativação online + tolerância offline
- Painel de configuração pós-compra
- Fluxo de conexão com outros sistemas do portfólio (depende da conta única de cliente, item 0.2, que precisa nascer no `aura-licensing`)

Nada disso invalida o que já está em código (Sprint 3-4, JWT) — é uma camada adicional que se conecta ao que já existe, na mesma lógica dos outros itens transversais: mais barato planejar agora do que retrofitar depois.
