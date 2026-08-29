---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AuraCondo — Documento de Projeto Final (Nome provisório)
### Sistema de Gestão de Condomínio

Segue a estrutura fixa do [[template-documento-projeto-final]].

---

## 1. Visão do produto

Plataforma de gestão de condomínio cobrindo os três perfis que nenhum outro sistema do portfólio tem ao mesmo tempo: síndico/administradora (gestor), morador (cliente cativo), e prestador de serviço terceirizado (portaria, limpeza, manutenção). Reaproveita peças já maduras do portfólio (módulo de OS do AuraFix para chamado de manutenção, padrão de cobrança recorrente do `aura-licensing`, `aura-notifications` para aviso/boleto), aplicadas a uma dinâmica de negócio genuinamente nova.

**Diferencial de inovação:** a maioria do mercado (Superlógica e afins) vende para administradora com contrato pesado e onboarding lento. Aqui a arquitetura modular do portfólio permite vender direto para síndico de condomínio pequeno/médio — sem contrato robusto, sem venda consultiva — e também para administradora que gerencia carteira de vários condomínios (ver seção 9), sem manter dois produtos diferentes.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Cadastro e estrutura
- Cadastro de condomínio, blocos, unidades e moradores (proprietário e/ou inquilino)
- Vaga de garagem vinculada à unidade, com controle de vaga extra/rotativa

### 2.2 Financeiro
- Cobrança de taxa condominial recorrente (boleto/Pix), com escada de inadimplência graduada — mesmo padrão do `aura-licensing`, aplicado a morador em vez de tenant de software
- Prestação de contas mensal/anual, balancete, categorização de despesa
- Gestão de fundo de reserva e orçamento anual
- Cobrança de multa/advertência por infração ao regulamento interno

### 2.3 Manutenção e operação
- Chamado de manutenção (área comum ou unidade privativa) — especialização do mesmo módulo de Ordem de Serviço já formalizado no AuraFix
- Escala e ponto de funcionário do condomínio (porteiro, zelador, faxineira)
- Livro de ocorrências

### 2.4 Controle de acesso (componente físico — ver seção 7)
- Liberação de acesso para visitante, entrega e prestador de serviço pontual
- Registro de entrada/saída, integrado a hardware de portaria

### 2.5 Reserva de área comum
- Agenda de salão de festas, churrasqueira, quadra — mesmo padrão de agendamento já usado no AuraVet/AuraFix

### 2.6 Assembleia e governança
- Convocação, pauta e ata digital
- Votação eletrônica em conformidade com a Lei 14.309/2022 (assembleia virtual ou híbrida), respeitando o mesmo direito de voz e voto da presencial
- Verificação obrigatória se a convenção do condomínio proíbe a modalidade virtual antes de habilitar a funcionalidade para aquele condomínio específico

### 2.7 Portal do morador
- 2ª via de boleto, abertura de chamado, reserva de área comum, comunicado, acesso a ata de assembleia

### 2.8 Seguro do condomínio
- Gestão de apólice e registro de sinistro (módulo simples, sem intermediação direta na v1)

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Cadastro de condomínio, bloco, unidade e morador (proprietário/inquilino) | Base de identidade para qualquer cobrança, comunicado ou chamado |
| RF02 | Cobrança recorrente de taxa condominial com escada de inadimplência graduada | Reduz inadimplência sem gerar corte abrupto/disputa desnecessária |
| RF03 | Prestação de contas com balancete categorizado | Obrigação legal do síndico perante os condôminos, formalizada sem planilha manual |
| RF04 | Chamado de manutenção com checklist e status, reaproveitando o módulo de OS | Padroniza atendimento de manutenção sem reescrever lógica já validada no AuraFix |
| RF05 | Escala e ponto de funcionário do condomínio | Substitui controle manual de ponto, reduzindo disputa trabalhista por registro impreciso |
| RF06 | Liberação de acesso e registro de entrada/saída de visitante/prestador | É o requisito de segurança física central do sistema — sem isso não é "gestão de condomínio", é só financeiro |
| RF07 | Agenda de reserva de área comum, com regra de bloqueio de conflito | Evita dois moradores reservando o mesmo espaço no mesmo horário |
| RF08 | Convocação, pauta, ata e votação eletrônica de assembleia, em conformidade com a Lei 14.309/2022 | Dá validade jurídica real à assembleia virtual, não só conveniência |
| RF09 | Verificação de que a convenção do condomínio não veda a modalidade virtual, antes de habilitar votação eletrônica | A lei condiciona a validade a isso — sem essa checagem, a assembleia pode ser juridicamente contestável |
| RF10 | Portal do morador com 2ª via de boleto, chamado, reserva e comunicado | Reduz volume de ligação/mensagem direta ao síndico para tarefa que o morador pode resolver sozinho |
| RF11 | Registro de apólice de seguro do condomínio e abertura de sinistro | Centraliza informação que hoje normalmente fica só com o síndico ou a administradora |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Síndico/administradora
- **Cadastro:** self-service (síndico individual) ou onboarding assistido (administradora com carteira de condomínios)
- **Uso:** painel financeiro, aprovação de chamado, gestão de assembleia
- **Suporte:** canal com o Grupo AMtech — mesma lacuna transversal do portfólio

### 4.2 Morador (proprietário ou inquilino)
- **Cadastro:** convite do síndico/administradora, self-service para completar cadastro
- **Uso:** portal do morador (2.7)
- **Suporte:** canal com o síndico primeiro (mesma lógica do operador de caixa do AuraPOS — dúvida operacional é do síndico, não do Grupo AMtech), escalando para o suporte técnico só em problema do sistema em si

### 4.3 Prestador de serviço terceirizado (portaria, limpeza, manutenção)
- **Cadastro:** criado pelo síndico/administradora
- **Uso:** app simplificado — chamado atribuído, registro de execução; porteiro usa a interface de controle de acesso (2.4)
- **Suporte:** mesmo canal do síndico

### 4.4 Suporte técnico interno
- Mesma lacuna recorrente do portfólio inteiro.

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no AuraCondo | Para que serve |
|---|---|---|
| RNFT-E01 (concorrência) | Reserva de área comum não pode aceitar dois moradores no mesmo horário simultaneamente | Mesmo princípio de concorrência já aplicado a estoque, aqui aplicado a agenda |
| RNFT-E02 (idempotência de pagamento) | Cobrança de taxa condominial recorrente | Evita cobrança duplicada em reenvio de webhook |
| RNFT06 (LGPD) | Dado de morador (pessoal e financeiro de inadimplência) | Cumpre obrigação legal — inadimplência é dado sensível, exposição indevida gera constrangimento real |
| Disponibilidade de controle de acesso (próprio) | Falha no sistema de liberação de acesso não pode deixar portaria sem alternativa manual de contingência | Segurança física real — diferente de qualquer outro sistema do portfólio, aqui uma falha de software pode virar risco físico |
| Integridade de voto eletrônico (próprio) | Cada voto deve ser auditável e não alterável após registrado | É o que sustenta a validade jurídica da assembleia virtual perante eventual contestação |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no AuraCondo |
|---|---|
| Controle de acesso físico | Maior superfície de risco físico de todo o portfólio — integração com hardware de portaria (interfone IP, fechadura eletrônica) exige o mesmo cuidado de menor privilégio já aplicado ao agente local do AuraPOS |
| Dados | Dado de inadimplência do morador é sensível e pode gerar constrangimento/dano reputacional se exposto indevidamente a vizinho |
| Integridade de votação | Log de auditoria imutável por voto — mesma lógica de rastreabilidade já usada no aura-historico, candidato natural de integração |
| Auditoria externa | Prioridade alta, dado o componente de segurança física (controle de acesso) e o valor legal da votação eletrônica |

---

## 7. Hardware, instalador e distribuição

**Aplicável, diferente da maioria dos serviços recentes.** O controle de acesso (2.4) exige integração com hardware de portaria:
- Interfone IP / videoporteiro, leitor de RFID/QR code para portão, fechadura eletrônica
- Mesmo padrão de agente local já usado no AuraPOS (RF09 daquele documento), adaptado para hardware de portaria em vez de hardware de PDV
- Distribuição do software segue o padrão SaaS do restante do portfólio; o hardware de portaria pode ser vendido como bundle opcional (equipamento + instalação + assinatura), reaproveitando a mesma lógica de instalador/licenciamento já definida para o AuraPOS

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml` de produção, pipeline GitHub Actions. Ponto de atenção: se o controle de acesso depender de hardware local, o mesmo cuidado de resiliência offline do AuraPOS (fila local, sincronização) se aplica aqui — portaria não pode parar de liberar acesso por instabilidade de internet.

---

## 9. Modelo de receita — todas as formas de venda

| Fonte | Modelo |
|---|---|
| Assinatura SaaS por unidade ou por condomínio | Mensalidade recorrente, escalando com o tamanho do condomínio |
| Taxa de setup/onboarding | Cobrança única na implantação |
| Bundle de hardware de portaria | Venda de equipamento + instalação + assinatura de software (mesmo modelo híbrido do AuraPOS) |
| **Canal B2B2C — administradora de condomínio** | Venda por carteira: uma administradora que gerencia dezenas de condomínios contrata o sistema para toda a carteira de uma vez — é o canal de maior alavancagem comercial deste sistema, uma única venda equivale a dezenas de clientes finais |
| Comissão sobre seguro do condomínio | Se o módulo de seguro (2.8) evoluir para intermediação real, não só registro |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Sistema em estágio de planejamento completo, primeira formalização de RF/RNF.

---

## 11. Pendências e decisões em aberto

1. **Fornecedor e protocolo de hardware de portaria** — decisão de parceiro técnico ainda não tomada.
2. **Validação jurídica por convenção** (RF09) — o sistema precisa de um fluxo claro para o síndico confirmar que a convenção não veda assembleia virtual; avaliar se vale checklist assistido ou exigência de upload da convenção para análise.
3. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado, que também é candidato natural a incorporar o log de auditoria de voto eletrônico (seção 6).
4. **Provedor de gateway de pagamento** — mesma pendência transversal do restante do portfólio.
5. **Modelo comercial do canal administradora** (seção 9) — precificação por carteira ainda não definida, provavelmente diferente do preço unitário por condomínio avulso.
