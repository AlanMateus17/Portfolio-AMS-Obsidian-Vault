---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Rendara — Documento de Projeto Final

Segue a estrutura fixa definida no [[template-documento-projeto-final]].

---

## 1. Visão do produto

Plataforma de inteligência financeira e gestão patrimonial para Pessoa Física e Pessoa Jurídica, aplicando as metodologias ARCA, Barsi (Carteira Previdenciária) e Value Investing (Buffett) de forma automatizada — não é um app de controle de gasto, é um motor de decisão de alocação.

**Diferencial de inovação:** a maioria dos apps financeiros brasileiros (Organizze, Mobills, GuiaBolso) resolve *rastreamento* de gasto. O AM Rendara resolve *alocação* — monitora desvio de cada quadrante da metodologia ARCA em relação à meta e sugere aporte de rebalanceamento automaticamente, calcula preço-teto dinâmico por ação (metodologia Barsi) e pontua empresa por critério de Value Investing numa janela de 5-10 anos. É motor de decisão determinístico e auditável, não dashboard passivo — e isso importa de verdade aqui, porque erro em cálculo financeiro que orienta decisão de terceiro tem consequência real, diferente de um app de gasto pessoal onde um erro é só inconveniente.

---

## 2. Funcionalidades completas (estado final)

### 2.0 Modo pessoal standalone (sem conexão a nenhum outro sistema do portfólio)
Isso faltava por completo na primeira versão: nem todo usuário do AM Rendara é investidor ou dono de negócio — a maioria das pessoas que procura controle financeiro pessoal ainda não chegou no estágio de alocação de patrimônio, está tentando sair do vermelho ou formar uma reserva. Esse modelo de três fases já foi validado na prática (é o mesmo raciocínio usado no seu próprio planejamento financeiro pessoal com as faturas do Nubank) e deveria ser um módulo formal do produto, não uma exceção:
- **Diagnóstico financeiro inicial** — ao entrar pela primeira vez, o sistema identifica em qual das três fases a pessoa está, a partir do que ela informa (dívida existente, reserva atual, renda fixa)
- **Fase 1 — Quitação de dívida**: acompanhamento de parcelamento existente (ex: fatura de cartão), com simulação de quando quita no ritmo atual vs. acelerando pagamento
- **Fase 2 — Reserva de emergência**: meta de 6-12 meses de custo fixo (mesmo cálculo do quadrante Caixa do ARCA, mas aqui como objetivo isolado, não parte de uma carteira maior), em renda fixa líquida
- **Fase 3 — Renda de investimento cobrindo despesa fixa**: só a partir daqui o motor de alocação ARCA/Barsi (seção 2.2) entra em cena — a pessoa "sobe de fase" dentro do próprio produto, sem precisar migrar de sistema
- Isso significa que o Básico não é "ARCA sem os extras" — é este módulo de diagnóstico e progressão de fase, disponível para qualquer pessoa física, com ou sem PJ, com ou sem qualquer outro sistema do portfólio conectado
- Orçamento por categoria de gasto pessoal (lazer, assinaturas, fundo de reserva para hardware/setup — mesmas categorias já usadas no seu próprio planejamento), aplicável independente da fase

---

### 2.1 Organização financeira
- Segregação hermética PF/PJ — nunca se misturam, garantida por regra de autorização em nível de schema, não só convenção de código
- Fluxo de caixa categorizado, com duas fontes possíveis via `IFonteDeReceita`: `FonteReceitaManual` (lançamento manual) ou `FonteReceitaAM Kaixara` (automático, a partir do fechamento de caixa, para cliente que também usa o AM Kaixara)
- Dashboard consolidado de patrimônio segundo os quatro quadrantes ARCA (Ações, Real Estate, Caixa, Ativos Internacionais)

### 2.2 Inteligência de investimento
- **Alocação automatizada (ARCA):** monitora desvio de cada quadrante em relação à meta de 25% e sugere aporte de rebalanceamento, com cálculo real do quadrante Caixa (6-12 meses de custo fixo, baseado no fluxo de caixa real registrado, não estimativa)
- **Filtro de ações (Barsi):** prioriza setores perenes (Bancos, Energia, Saneamento, Telecomunicações, Seguros) com Dividend Yield histórico acima de parâmetro configurável
- **Preço-teto dinâmico:** calcula o valor máximo a pagar por uma ação para garantir o retorno mínimo desejado em dividendos
- **Scoring Value Investing:** pontua empresa por ROE, endividamento e margem operacional numa janela de 5 a 10 anos

### 2.3 Dados bancários
- `IFonteDeMovimentacaoBancaria` com duas implementações: `FonteOpenFinance` (automática, mas depende de credenciamento junto ao Banco Central, fora do seu controle de prazo) e `FonteImportacaoManual` (CSV/OFX exportado pelo próprio banco do cliente, sem credenciamento, disponível desde o primeiro dia) — a segunda existe justamente para não travar o produto na dependência da primeira

### 2.4 Simulação e projeção
- **Simulador de cenário "e se"** — transação especulativa via `aura-historico` (Clojure/Datomic, `d/with`), permitindo simular rebalanceamento antes de executar de fato
- **Projeção de crescimento patrimonial de longo prazo** — via `aura-analytics` (Python), simulação estatística de aportes recorrentes

### 2.5 Conformidade e consultoria
- **Relatório de Recomendação formal** — em conformidade com a Resolução CVM 19, documento PDF com descrição específica da operação e campo de aprovação prévia do cliente; condicional a validação jurídica confirmando enquadramento como consultoria de valores mobiliários
- **Camada de consultoria premium** — bloqueada até certificação (CPA + C-Pro I, caminho atualizado após a reestruturação ANBIMA de 2026) e registro como Consultor de Valores Mobiliários pessoa física na CVM

### 2.6 Integração com o restante do portfólio — **faltava por completo na primeira versão**
O AM Rendara não deveria se conectar só ao AM Kaixara. Qualquer sistema do portfólio que gera receita de negócio para o mesmo cliente é candidato à mesma lógica de `IFonteDeReceita`:
- **`FonteReceitaAM Kaixara`** (já especificada) — fechamento de caixa alimenta o fluxo de caixa PJ
- **`FonteReceitaAM Consertta`** — faturamento de Ordem de Serviço e loja (física/online) alimentando o fluxo de caixa PJ de quem roda a assistência técnica
- **`FonteReceitaAuraVet`** — faturamento da clínica veterinária, mesmo princípio, para o cliente que for dona do AuraVet
- **`FonteReceitaDelivery`** — comissão/repasse de entrega, quando aplicável
- Em todos os casos, a integração segue o mesmo padrão já definido: consentimento explícito do cliente, credencial de escopo mínimo (só leitura do fechamento/faturamento, nunca acesso amplo ao outro sistema)

### 2.7 Integração com o `aura-goals` (Momentos/Cupido) — **também faltava por completo**
O `aura-goals` já foi definido como serviço compartilhado entre AM Rendara e Momentos/Cupido para metas financeiras de casal, mas essa conexão nunca tinha entrado neste documento:
- Casal com conta no Momentos/Cupido pode ter meta financeira conjunta (ex: viagem, entrada de imóvel) visível tanto no Momentos/Cupido (contexto afetivo do casal) quanto no AM Rendara (contexto financeiro de cada um)
- Cada parceiro mantém sua própria segregação PF (seção 2.1) — a meta compartilhada é a única informação que atravessa os dois sistemas, nunca o extrato ou fluxo de caixa individual completo
- Isso é a prova real de por que o `aura-goals` precisa de RF/RNF formal próprio (gap já apontado no documento de status do portfólio) — ele está no caminho crítico de dois produtos diferentes, não é um detalhe secundário de nenhum dos dois

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Diagnóstico financeiro inicial, classificando a pessoa em Fase 1/2/3 | Direciona cada usuário ao módulo certo desde o primeiro acesso, sem exigir que ele já saiba o que precisa |
| RF02 | Acompanhamento de quitação de dívida com simulação de ritmo de pagamento | Ajuda quem está na Fase 1 a visualizar quando sai da dívida, motivando continuidade |
| RF03 | Meta de reserva de emergência (6-12 meses de custo fixo) | Formaliza o objetivo mais recomendado antes de qualquer investimento de risco |
| RF04 | Segregação hermética PF/PJ, garantida em nível de schema | Impede que dado pessoal e empresarial se misturem, mesmo por erro de código |
| RF05 | Fluxo de caixa via `IFonteDeReceita` (`FonteReceitaManual` ou automática) | Dá liberdade de uso imediato (manual) sem travar o cliente que ainda não tem AM Kaixara/AM Consertta/AuraVet conectado |
| RF06 | Dashboard de patrimônio pelos 4 quadrantes ARCA | Visão única de alocação, sem precisar consolidar manualmente em planilha |
| RF07 | Motor de alocação ARCA com sugestão de aporte de rebalanceamento | Automatiza a decisão de "onde colocar o próximo aporte", que é o maior ponto de dúvida de investidor iniciante |
| RF08 | Filtro de ações Barsi (setor perene + DY histórico) | Reduz universo de ação a analisar a um conjunto com histórico de perenidade |
| RF09 | Cálculo de preço-teto dinâmico por ação | Evita comprar acima do valor que garante o retorno mínimo desejado |
| RF10 | Scoring Value Investing (ROE, endividamento, margem, janela 5-10 anos) | Dá critério objetivo de qualidade de empresa, não só preço |
| RF11 | Conciliação bancária via `FonteOpenFinance` ou `FonteImportacaoManual` | A segunda existe para não travar o produto na dependência de credenciamento do Banco Central |
| RF12 | Simulador de cenário "e se" antes de executar rebalanceamento | Permite testar decisão sem comprometer a carteira real |
| RF13 | Projeção de crescimento patrimonial de longo prazo | Ajuda o cliente a visualizar o efeito composto de aportes recorrentes, motivando consistência |
| RF14 | Relatório de Recomendação formal (CVM 19) | Exigido legalmente se o enquadramento como consultoria for confirmado — protege tanto o cliente quanto você |
| RF15 | Camada de consultoria premium, gateada por certificação | Impede oferecer consultoria sem estar regularmente habilitado, evitando risco regulatório |
| RF16 | Integração `FonteReceitaAM Kaixara`/`AM Consertta`/`AuraVet` com consentimento explícito | Automatiza fluxo de caixa PJ sem exigir lançamento manual duplicado |
| RF17 | Meta financeira compartilhada via `aura-goals` (Momentos/Cupido) | Permite casal acompanhar objetivo comum sem expor o extrato individual de cada parceiro |
| RF18 | Orçamento por categoria de gasto pessoal (lazer, assinaturas, fundo de reserva) | Dá controle de gasto no dia a dia, independente da fase (1, 2 ou 3) em que a pessoa está |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.0 Pessoa física standalone (sem PJ, sem nenhum outro sistema conectado) — **faltava por completo**
- **Cadastro:** self-service, sem exigir CNPJ nem qualquer conexão com outro produto
- **Uso:** módulo de diagnóstico e progressão de fase (seção 2.0) como porta de entrada — só migra para o motor de alocação (seção 2.2) quando alcançar a Fase 3
- **Suporte:** mesmo canal do restante, sem diferenciação — é o perfil de maior volume esperado, e o que valida o produto fora do nicho de quem já é investidor

### 4.1 Cliente PF (investidor, ou dono de negócio pessoa física)
- **Cadastro:** self-service
- **Uso:** dashboard, fluxo de caixa manual, módulos de alocação conforme o tier contratado
- **Suporte:** canal com o Grupo AMtech — mesma lacuna transversal já identificada nos outros sistemas, ainda não formalizada aqui também

### 4.2 Cliente PJ (dono de negócio, possivelmente também usuário do AM Kaixara)
- **Cadastro:** self-service, com opção de conectar `FonteReceitaAM Kaixara` via consentimento explícito (RNFT-S03)
- **Uso:** mesmo dashboard, com fluxo de caixa PJ alimentado automaticamente quando conectado
- **Suporte:** mesmo canal do cliente PF

### 4.3 Consultor certificado (você, ou futuro consultor contratado)
- **Cadastro:** perfil elevado, existe só depois da certificação CPA/C-Pro I e registro CVM
- **Uso:** acesso à camada de consultoria premium, geração de Relatório de Recomendação
- **Observação:** se algum dia houver mais de um consultor atendendo clientes diferentes na mesma plataforma, isso exige controle de acesso por carteira de cliente — ainda não desenhado, porque hoje o cenário é um único consultor (você)

### 4.4 Suporte técnico interno
- Mesma lacuna recorrente identificada em todos os outros sistemas do portfólio — ainda sem RF formal. Aqui o painel de suporte precisaria de cuidado extra: qualquer acesso a dado financeiro de cliente para diagnóstico é sensível por natureza, exige justificativa e log de acesso mais rígido que nos outros sistemas.

---

## 5. Requisitos Não Funcionais — próprios + transversais

| ID | Aplicação no AM Rendara | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado bancário é a categoria mais sensível do portfólio inteiro — política de retenção e exclusão precisa ser mais rígida que a padrão | Cumprir obrigação legal e reduzir dano em caso de vazamento |
| RNFT07 (BOLA) | Crítico aqui — vazamento de carteira de um cliente para outro é o pior cenário de falha possível neste sistema especificamente | Impede que um cliente veja a carteira/patrimônio de outro só trocando um ID na URL |
| RNFT-E02 (idempotência de pagamento) | Cobrança de assinatura recorrente (Básico/Investidor) | Evita cobrança duplicada em caso de webhook de pagamento reenviado |
| RNFT-E06 (reconciliação) | Reporta dados de assinatura para reconciliação central do `aura-licensing` | Detecta se algum evento de cobrança se perdeu silenciosamente |
| Motor determinístico auditável | Requisito próprio, fora da série RNFT: as fórmulas financeiras (ARCA, Barsi, scoring) rodam em C# com estruturas imutáveis e cobertura de teste próxima de 100% | Um erro de cálculo aqui influencia decisão financeira real de terceiro — o padrão de qualidade precisa refletir esse risco |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no AM Rendara |
|---|---|
| Dados | Criptografia de dado bancário em repouso (AES-256), já definida anteriormente — é o único sistema do portfólio com esse requisito explícito de algoritmo, por ser o de maior sensibilidade. **RESOLVIDO/atualizado:** esse requisito agora é implementado via `aura-vault`, o serviço compartilhado de proteção de dado extra-sensível, em vez de implementação própria isolada — ver [[aura-vault-documento-projeto-final]] |
| Rede/API | Auditoria de rota contra BOLA já era requisito próprio antes mesmo da série RNFT transversal existir — mantido e reforçado |
| Conexão entre sistemas (RNFT-S03/S04) | `FonteReceitaAM Kaixara` só se conecta com consentimento explícito do cliente; credencial de escopo mínimo (só leitura de fechamento de caixa, nunca acesso amplo ao AM Kaixara) |
| Auditoria externa (RNFT-S06) | Prioridade máxima do portfólio inteiro — é o sistema que processa o dado mais sensível (financeiro) e tem o maior custo de reputação em caso de falha; pentest externo aqui não é opcional antes de qualquer lançamento público |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** SaaS puro, sem componente físico. Distribuição via pacote comercial padrão (`aura-licensing`), sem necessidade de instalador executável.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml` de produção, pipeline GitHub Actions (build → teste → deploy), deploy em serviço gerenciado (AWS ou Azure, decisão pendente transversal ao portfólio). Dado o nível de sensibilidade do dado processado, vale considerar ambiente de produção com isolamento de rede mais rígido que os demais sistemas — decisão a formalizar.

---

## 9. Modelo de receita

| Pacote | Cobertura |
|---|---|
| **AM Rendara Básico** | Módulo de diagnóstico e progressão de fase (seção 2.0) + fluxo de caixa (manual ou automático) + dashboard — vendável para qualquer pessoa física, com ou sem PJ, com ou sem qualquer outro sistema conectado |
| **AM Rendara Investidor** | Tudo do Básico + motor de alocação completo (ARCA, Barsi, scoring, preço-teto) — natural upgrade de quem alcançou a Fase 3 |
| **Consultoria premium** | Camada adicional, condicional à certificação CPA/C-Pro I — cobrança separada, fora do modelo de assinatura padrão |
| **Combo AMS Wealth Business** (AM Kaixara + AM Rendara) | Soma dos dois, com fechamento de caixa do AM Kaixara alimentando automaticamente o fluxo de caixa PJ via `FonteReceitaAM Kaixara` |
| **Combos equivalentes com AM Consertta e AuraVet** | Mesmo modelo do combo acima, usando `FonteReceitaAM Consertta`/`FonteReceitaAuraVet` (seção 2.6) |
| **Módulo de meta compartilhada** (com Momentos/Cupido) | Não é pacote vendido separadamente — é um diferencial incluído em qualquer tier, para quem também usa o Momentos/Cupido |

---

## 10. Status atual de desenvolvimento

**Nenhum código foi escrito ainda.** Assim como o AM Rotara, o AM Rendara está inteiramente em estágio de planejamento — RF/RNF, arquitetura de módulos e README já existem como documentos, mas nenhuma linha de backend foi iniciada. Vantagem real: toda a auditoria de escala, segurança e o template completo já entram desde o primeiro commit.

---

## 11. Pendências e decisões em aberto

1. **Validação jurídica do enquadramento como consultoria de valores mobiliários** — trava a formalização definitiva do Relatório de Recomendação (Resolução CVM 19).
2. **Confirmação de que C-Pro I (pós-reestruturação ANBIMA 2026) é aceito pela CVM no lugar da antiga CEA** — pendência sinalizada anteriormente, ainda não verificada em edital oficial.
3. **Credenciamento Open Finance junto ao Banco Central** — prazo fora do seu controle; o produto não deve depender dele para lançar (mitigado pela `FonteImportacaoManual`).
4. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado, com cuidado extra de acesso justificado e logado dado a sensibilidade do dado financeiro (ver seção 5 do [[aura-support-documento-projeto-final]]).
5. **Isolamento de rede em produção** — decisão de infraestrutura específica deste sistema, ainda não formalizada (seção 8).
6. **Comportamento padrão de `FonteReceitaAM Kaixara`** — o que acontece se o cliente desconectar a integração depois de já ter dado histórico importado; ainda não definido.
7. **RF/RNF formal do `aura-goals`** — reforçado agora pela seção 2.7: ele está no caminho crítico do AM Rendara e do Momentos/Cupido ao mesmo tempo, não é mais só uma pendência de baixa prioridade.
8. **Padronizar `FonteReceitaAM Consertta` e `FonteReceitaAuraVet`** — precisam ser especificadas formalmente quando esses dois sistemas avançarem além do estágio atual de planejamento, seguindo o mesmo contrato de interface do `FonteReceitaAM Kaixara`.
9. **Regra de visibilidade da meta compartilhada** (seção 2.7) — precisa ficar claro para o usuário, na interface, que só a meta atravessa os dois sistemas, nunca o extrato — isso é tanto decisão de produto quanto de confiança do usuário, vale validar com ele antes de formalizar o RF.
