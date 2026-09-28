---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# Sistema Veterinário Completo — Funcionalidades, Requisitos e Fontes de Renda
### (Nome provisório: AuraVet — ajuste quando definir o nome/marca da clínica)

> **Nota sobre estrutura:** este documento foi criado antes do [[template-documento-projeto-final]] existir, então segue numeração própria (por tipo de conteúdo) em vez das 10 seções fixas do template. Conteúdo equivalente às seções 1, 2, 4, 6, 8-9 do template já existe aqui (funcionalidades, RF/RNF, receita, stack, MVP). As seções 12-14, adicionadas ao final, cobrem o que faltava: perfis de usuário, segurança concreta e pendências — mesmo conteúdo que as seções 3, 5 e 10 do template exigem.

**Premissa do produto:** não é um "sistema de agenda de clínica". É uma plataforma de gestão + vendas + relacionamento que cobre veterinária de todos os portes (pequeno, médio e grande porte, exóticos/silvestres), do consultório autônomo até uma estrutura de hospital/franquia — e que também funciona como canal de venda de tudo que ela puder oferecer: serviço clínico, produto físico, assinatura e conteúdo.

**Princípio de organização (importante):** o sistema cresce por **verticais de negócio dentro da mesma empresa**, não por empresas separadas. Ou seja, uma única base de tutores/produtores, um único financeiro, um único painel — mas cada vertical tem seu próprio fluxo, catálogo, público e regras, porque o público e o ticket de "tutor de cachorro" e "produtor rural comprando dose de sêmen" não têm nada a ver um com o outro. É a mesma lógica de módulos independentes que você já usa no restante do ecossistema Aura, aplicada aqui a áreas de atuação em vez de funcionalidades.

### As verticais

| Vertical | Espécies/porte | Público | Natureza da venda |
|---|---|---|---|
| **Pet Care** (já detalhado nas seções seguintes) | Cães, gatos, exóticos de pequeno porte | Tutor pessoa física (B2C) | Ticket baixo/médio, alta recorrência, volume alto |
| **Grandes Animais / Clínica de Produção** | Bovino, equino, suíno, caprino, ovino | Produtor rural, fazenda, cooperativa (B2B) | Ticket médio, visitas técnicas, contratos de sanidade de rebanho |
| **Equinos de alto desempenho** | Equinos esportivos/reprodução | Haras, proprietário de plantel (B2B/B2C híbrido) | Ticket alto, baixo volume, forte componente de reputação/indicação |
| **Reprodução Animal & Biotecnologia Genética** | Bovino principalmente (Brasil é líder mundial em FIV bovina), extensível a equino/caprino/ovino | Fazenda, cooperativa, central de genética, outros veterinários (B2B) | Ticket alto, altíssima escalabilidade — é a vertical com menor dependência do tempo pessoal dela por unidade de receita |
| **Fauna silvestre/exóticos** (opcional, nicho) | Silvestres, animais de cativeiro legal | Zoológicos, criadouros licenciados, órgãos ambientais | Baixo volume, alta especialização, forte para reputação/mídia |

A vertical de **Reprodução Animal & Biotecnologia** merece destaque à parte porque é estruturalmente diferente das outras: <cite index="34-1">o Brasil é líder mundial na produção de embriões bovinos por fertilização in vitro</cite>, o que significa que essa não é uma aposta de nicho pequeno — é um mercado nacional consolidado e ainda em expansão, com produtor rural comprando serviço de melhoramento genético como investimento recorrente, não como gasto pontual.

---

## 1. Funcionalidades máximas (por módulo)

### 1.1 Agendamento e atendimento
- Agenda multiprofissional (vários veterinários, especialidades, salas/boxes) com bloqueio de conflito automático
- Agendamento online self-service pelo tutor (app/site), com escolha de profissional, tipo de serviço e horário
- Encaixe de urgência/emergência com fila de prioridade
- Lembretes automáticos (WhatsApp/SMS/push) de consulta, retorno, vacina e vermifugação
- Check-in digital (QR code na chegada, tempo de espera visível)
- Telemedicina veterinária integrada (teleconsulta, telemonitoramento, teletriagem, teleorientação, telediagnóstico, teleinterconsulta entre profissionais)
- Atendimento domiciliar com agenda de rota (visitas programadas, pet pequeno porte)

### 1.2 Prontuário eletrônico do paciente (pet)
- Ficha completa por animal: espécie, raça, porte, peso, histórico de vacinas, alergias, cirurgias, exames
- Linha do tempo clínica (evolução, anexos de exames, imagens, laudos)
- Prescrição digital, com controle de receituário especial para medicamentos controlados
- Vínculo formal com o tutor (Relação Prévia Veterinária-Animal-Responsável, exigida para telemedicina)
- Assinatura eletrônica de termos de consentimento (procedimentos, internação, eutanásia, telemedicina)
- Compartilhamento de prontuário com outras clínicas/especialistas mediante autorização

### 1.3 Internação, cirurgia e diagnóstico
- Gestão de leitos/UTI/canis de internação com status em tempo real
- Checklist e protocolo cirúrgico digital (pré, trans e pós-operatório)
- Pedido e resultado de exames laboratoriais e de imagem, com upload/anexo de laudo
- Integração com laboratórios parceiros (envio de pedido, recebimento de resultado)
- Painel de acompanhamento do tutor durante internação (fotos, atualizações, "diário do paciente")

### 1.4 Estoque e farmácia
- Controle de estoque de medicamentos, vacinas, insumos e materiais cirúrgicos
- Rastreabilidade por lote e validade, com alerta de vencimento
- Controle diferenciado para medicamentos controlados (receituário especial)
- Reposição automática/sugestão de compra por ponto de pedido
- Farmácia própria com venda direta (balcão e online)

### 1.5 Loja / marketplace de produtos
- Catálogo de produtos: ração, medicamentos de venda livre, acessórios, higiene, brinquedos
- E-commerce integrado com entrega/retirada, carrinho, checkout
- Assinatura recorrente de produtos (ex: ração mensal por entrega automática)
- Curadoria por perfil do pet (idade, porte, restrição alimentar) usando o histórico do prontuário

### 1.6 Serviços complementares (para vender "tudo")
- Banho e tosa (agenda própria, pacotes)
- Hotel/creche pet (hospedagem com diária, câmeras ao vivo para o tutor)
- Adestramento e enriquecimento ambiental
- Fisioterapia, reabilitação e acupuntura veterinária
- Odontologia veterinária (limpeza, procedimentos)
- Estética (tosa na tesoura, hidratação, spa pet)
- Pet táxi / transporte para consulta
- Funeral e cremação (parceria ou serviço próprio)

### 1.7 Programas de recorrência e fidelidade
- Plano de saúde pet / clube de assinatura mensal (consultas, vacinas e check-up inclusos, com mensalidade fixa — motor de receita recorrente)
- Programa de pontos/fidelidade (cashback em produtos e serviços)
- Indicação premiada (tutor indica tutor)

### 1.8 Financeiro e cobrança
- Emissão de nota fiscal (produto e serviço, alíquotas diferentes)
- Split de pagamento (ex: parte para a clínica, parte para profissional parceiro/terapeuta associado)
- Múltiplos meios de pagamento (Pix, cartão, boleto, parcelamento, carteira digital do app)
- Orçamento digital aprovável pelo tutor antes do procedimento
- Conta corrente do tutor (créditos, pacotes pré-pagos)
- Relatório de faturamento por profissional, por unidade, por categoria de serviço/produto

### 1.9 Gestão da equipe e da operação
- Escala de profissionais e comissionamento por atendimento/venda
- Multi-unidade (se abrir filial) com visão consolidada e por unidade
- Controle de acesso por papel (recepção, veterinário, financeiro, admin)
- Anotação de Responsabilidade Técnica (ART) vinculada a cada profissional, obrigatória para telemedicina em pessoa jurídica

### 1.10 App e portal do tutor
- Cadastro do(s) pet(s), agendamento, histórico de consultas e vacinas em um só lugar
- Compra de produtos e assinatura do plano de saúde pet
- Carteira de vacinação digital (compartilhável, ex: para viagem/hotel pet)
- Chat/canal direto com a clínica
- Avaliação pós-atendimento (prova social, alimenta reputação/marketing)

### 1.11 Marketing, conteúdo e reputação
- Blog/conteúdo educativo para tutores (gera tráfego orgânico e autoridade — ponto forte pra "ser conhecida em todo o Brasil")
- Integração com redes sociais e captação de leads
- Campanhas segmentadas por perfil do pet (ex: campanha de vacina antirrábica para cães sem reforço no ano)
- Página pública da clínica com portfólio, equipe, avaliações — pensada para SEO local e nacional

### 1.12 Grandes animais / clínica de produção (nova vertical)
- Cadastro de propriedade rural/fazenda como "cliente-conta", com múltiplos animais/rebanho vinculados
- Agenda de visita técnica a campo (rota, não consultório)
- Ficha sanitária de rebanho (não só do indivíduo) — vacinação em massa, controle de doenças notificáveis
- Emissão/controle de GTA (Guia de Trânsito Animal) quando aplicável
- Contrato recorrente de sanidade de rebanho (visita programada + vacinas + exames periódicos)
- Cirurgia e atendimento de campo para grande porte (equino, bovino)

### 1.13 Reprodução animal & biotecnologia genética (nova vertical — maior potencial de escala)
- Cadastro de reprodutores (touros/matrizes doadoras) com ficha genealógica e desempenho
- Central de sêmen: coleta, processamento, congelamento e controle de estoque de doses por reprodutor/lote
- Banco genético: armazenamento rastreável de sêmen, óvulos e embriões (identificação por doador, lote e data)
- Fluxo de Inseminação Artificial (IA) e IA por Tempo Fixo (IATF): protocolo hormonal, data prevista, resultado de diagnóstico de gestação
- Fluxo de Transferência de Embriões (TE): doadora, protocolo de superovulação, coleta, receptoras aptas, resultado
- Fluxo de Fertilização in Vitro (FIV): aspiração folicular, fecundação em laboratório, cultivo, transferência — com rastreabilidade completa doador → embrião → receptora → prenhez confirmada
- Sexagem de sêmen (registro de qual dose é sexada e para qual sexo)
- Consultoria de melhoramento genético / seleção de acasalamento, com indicadores de desempenho por linhagem
- Módulo de conformidade regulatória: registro do estabelecimento junto ao MAPA (centros de coleta e processamento de sêmen), cadastro de reprodutores aptos, rastreabilidade exigida pela legislação de material genético animal
- Painel do produtor/cliente B2B: acompanhamento remoto do status de cada protocolo (gestação confirmada, dose disponível, próxima visita)
- Faturamento por dose/procedimento com contrato recorrente por safra reprodutiva

### 1.14 BI e relatórios
- Dashboard de faturamento, ticket médio, taxa de retorno, ocupação de agenda
- Indicadores por serviço/produto mais rentável
- Previsão de demanda (sazonalidade de vacinas, banho e tosa etc.)

---

## 2. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | O sistema deve permitir cadastro de tutores e múltiplos pets vinculados a cada tutor | Base de identidade para qualquer atendimento, venda ou comunicação futura |
| RF02 | O sistema deve permitir agendamento por tutor (self-service) e por recepção, com validação de conflito de horário/profissional | Reduz carga da recepção e evita conflito de agenda entre profissionais |
| RF03 | O sistema deve registrar prontuário eletrônico por pet, com histórico cronológico de todos os atendimentos | Histórico clínico é a base de qualquer decisão médica futura, e também obrigação legal |
| RF04 | O sistema deve emitir prescrição digital, diferenciando medicamento comum de controlado (fluxo de receituário especial) | Cumpre exigência regulatória para medicamento controlado, evitando prescrição irregular |
| RF05 | O sistema deve suportar teleconsulta com vínculo obrigatório de RPVAR antes da liberação, exceto em urgência/emergência | Cumpre a Resolução CFMV — sem RPVAR, teleconsulta como porta de entrada é irregular |
| RF06 | O sistema deve gerar e armazenar termo de consentimento assinado eletronicamente para procedimentos, internação e telemedicina | Protege juridicamente a clínica e formaliza a autorização do tutor |
| RF07 | O sistema deve controlar estoque com baixa automática vinculada ao uso em atendimento/venda, por lote e validade | Evita usar medicamento vencido e mantém estoque real sempre atualizado |
| RF08 | O sistema deve permitir venda de produto avulso (loja/e-commerce) independente de haver consulta associada | Capta receita de quem só quer comprar produto, sem precisar forçar vínculo com atendimento |
| RF09 | O sistema deve suportar assinatura recorrente (plano de saúde pet e clube de produtos), com cobrança automática mensal | É a fonte de receita recorrente mais previsível do sistema — motor de crescimento |
| RF10 | O sistema deve permitir emissão de nota fiscal por venda de produto e por prestação de serviço, com tratamento fiscal distinto | Cumpre obrigação fiscal, que é diferente entre produto e serviço |
| RF11 | O sistema deve permitir split de pagamento entre a clínica e profissionais/parceiros associados | Elimina acerto manual de comissão entre a clínica e veterinário parceiro |
| RF12 | O sistema deve permitir gestão de múltiplas unidades com visão consolidada e segregada por unidade | Permite crescer para mais de uma unidade sem trocar de sistema |
| RF13 | O sistema deve permitir controle de acesso por perfil (recepção, veterinário, financeiro, administrador, tutor) | Limita o que cada perfil pode ver/fazer, reduzindo erro e uso indevido |
| RF14 | O sistema deve registrar a ART do profissional responsável, obrigatória para telemedicina como pessoa jurídica | Cumpre exigência do CFMV para prestação de telemedicina pela clínica |
| RF15 | O sistema deve permitir acompanhamento em tempo real de pets internados, visível ao tutor de forma controlada | Reduz ansiedade do tutor e diferencia a clínica pela transparência |
| RF16 | O sistema deve permitir agendamento e cobrança de serviços complementares com agendas independentes da agenda clínica | Evita que banho e tosa trave a agenda de consulta médica, e vice-versa |
| RF17 | O sistema deve gerar carteira de vacinação digital exportável/compartilhável pelo tutor | Serviço de valor percebido alto, útil para viagem/hotel pet, com baixo custo de implementação |
| RF18 | O sistema deve enviar lembretes automáticos (consulta, retorno, vacina) por WhatsApp/push/SMS | Reduz falta em consulta e mantém vacinação em dia sem esforço manual |
| RF19 | O sistema deve permitir avaliação do atendimento pelo tutor após o serviço | Gera prova social e sinaliza problema de qualidade cedo |
| RF20 | O sistema deve gerar relatórios financeiros e operacionais | Dá visibilidade de negócio sem exigir exportação manual para planilha |
| RF21 | O sistema deve permitir orçamento prévio digital, com aprovação do tutor antes de procedimento de custo elevado | Evita disputa sobre valor cobrado e formaliza consentimento financeiro |
| RF22 | O sistema deve suportar atendimento domiciliar com agenda de rota, respeitando a exigência de pequeno porte da Resolução CFMV vigente | Cumpre a regulamentação específica de atendimento domiciliar (Resolução CFMV nº 1.690/2026) |
| RF23 | O sistema deve cadastrar propriedade rural/fazenda como conta-cliente, com rebanho vinculado e ficha sanitária coletiva | Pré-requisito para operar a vertical B2B de Grandes Animais |
| RF24 | O sistema deve suportar contrato recorrente de sanidade de rebanho, com agenda de visitas técnicas programadas | Cria receita recorrente B2B, equivalente ao plano de saúde pet na vertical de produção |
| RF25 | O sistema deve rastrear cada dose de sêmen, óvulo ou embrião por doador, lote, data e destino | Exigência legal de rastreabilidade de material genético animal, além de prevenir fraude |
| RF26 | O sistema deve suportar o fluxo completo de FIV, vinculando cada etapa ao lote de origem | Sem rastreio ponta a ponta, o procedimento de maior ticket do sistema fica sem controle de qualidade |
| RF27 | O sistema deve suportar o fluxo de Transferência de Embriões | Viabiliza operacionalmente a vertical de maior potencial de escala do AuraVet |
| RF28 | O sistema deve suportar o fluxo de Inseminação Artificial e IATF | Cobre o procedimento reprodutivo de maior volume antes de escalar para FIV/TE |
| RF29 | O sistema deve manter cadastro de reprodutores com ficha genealógica e histórico de desempenho | Base de dado que sustenta a consultoria de melhoramento genético, outra fonte de receita |
| RF30 | O sistema deve manter registro de conformidade com o cadastro exigido pelo MAPA | Sem esse registro, a clínica não pode legalmente faturar pela vertical de reprodução |
| RF31 | O sistema deve oferecer painel remoto ao produtor/cliente B2B para acompanhar status de protocolos | Reduz visita/ligação de acompanhamento, e é o tipo de experiência que justifica o ticket alto B2B |
| RF32 | O sistema deve suportar publicação de conteúdo (blog educativo) e campanha segmentada por perfil de pet | É o que sustenta a aquisição orgânica de cliente novo, sem depender só de indicação boca a boca |
| RF33 | O sistema deve gerar indicador de sazonalidade/demanda (ex: pico de vacina antirrábica) a partir do histórico de atendimento | Permite planejar estoque e agenda antes do pico acontecer, não reagir depois |

---

## 3. Requisitos Não Funcionais (RNF)

| Categoria | Requisito | Para que serve |
|---|---|---|
| **Segurança/LGPD** | Dados de tutor e prontuário são dados pessoais sensíveis por associação; exige criptografia em repouso e trânsito, controle de acesso granular e log de auditoria de quem acessou cada prontuário | Cumpre LGPD e reduz dano em caso de vazamento |
| **Conformidade CFMV** | Toda funcionalidade de telemedicina deve seguir a Resolução CFMV nº 1.465/2022 | Evita que a clínica preste telemedicina de forma irregular |
| **Conformidade CFMV** | Atendimento domiciliar deve seguir a Resolução CFMV nº 1.690/2026 | Mesma razão, para o serviço domiciliar |
| **Disponibilidade** | Sistema crítico (agenda, prontuário, internação) deve ter alta disponibilidade | Indisponibilidade em horário de atendimento é risco de segurança do paciente, não só comercial |
| **Performance** | Busca de prontuário e histórico deve responder em tempo curto mesmo com anos de histórico acumulado | Consulta lenta no meio de um atendimento é risco clínico, não só incômodo |
| **Escalabilidade** | Arquitetura deve suportar do consultório autônomo até rede multi-unidade, sem reescrita | Evita migração cara de sistema quando o negócio crescer |
| **Usabilidade** | Interface da recepção/veterinário precisa ser rápida sob pressão; interface do tutor precisa ser simples para qualquer público | Reduz erro operacional e amplia o público que consegue usar o sistema sozinho |
| **Auditabilidade** | Toda alteração em prontuário, prescrição e termo de consentimento deve ser versionada/auditável | Prova em caso de disputa e rastreio de erro |
| **Integração** | Deve prever integração com meios de pagamento, emissor fiscal, WhatsApp Business API, e futuramente laboratórios parceiros | Evita retrabalho de arquitetura quando essas integrações forem ativadas |
| **Continuidade** | Backup e plano de recuperação de desastre para prontuário | Perda de histórico clínico é risco de negócio e também ético/legal |
| **Acessibilidade** | Interface do tutor deve atender critérios básicos de acessibilidade | O público-alvo é "todo tipo de público", incluindo tutor idoso |
| **Rastreabilidade genética** | Toda dose de sêmen, óvulo ou embrião deve ser rastreável de ponta a ponta, sem perda de vínculo | Exigência legal, e também prevenção de fraude |
| **Conformidade MAPA** | Módulo de reprodução/biotecnologia deve refletir os registros exigidos para material genético animal | Sem isso, a clínica não pode legalmente faturar por essa vertical |
| **Segregação de público** | Experiência de uso claramente distinta entre tutor pessoa física e produtor/conta B2B | Reduz confusão de interface e superfície de erro/vazamento entre os dois perfis |

---

## 4. Fontes de renda (tudo que ela pode vender através do sistema)

### 4.1 Receita clínica (por atendimento)
- Consultas de rotina e retorno
- Consultas de urgência/emergência (ticket premium)
- Consultas por especialidade (cardiologia, dermatologia, oftalmologia, ortopedia, oncologia veterinária — conforme ela for se especializando ou trouxer parceiros)
- Teleconsulta e teleorientação
- Cirurgias eletivas e emergenciais
- Internação e diária de UTI
- Exames laboratoriais e de imagem (próprios ou repasse de parceiro com margem)
- Odontologia veterinária
- Vacinação e vermifugação

### 4.2 Receita recorrente (o motor de crescimento previsível)
- **Plano de saúde pet / clube de assinatura** — mensalidade fixa cobrindo consultas, vacinas e check-ups; é o item de maior potencial de escala porque garante receita previsível mês a mês, não depende de vender uma consulta de cada vez
- Assinatura de entrega recorrente de ração/produtos
- Pacotes pré-pagos de sessões (fisioterapia, banho e tosa)

### 4.3 Receita de produto (loja/e-commerce)
- Ração, medicamentos de venda livre, acessórios, higiene, brinquedos
- Farmácia veterinária própria (margem de revenda de medicamento controlado e não controlado)
- Marca própria de produtos no médio prazo (white label de ração/suplemento, se o volume justificar)

### 4.4 Receita de serviços complementares
- Banho e tosa / estética
- Hotel/creche pet
- Adestramento
- Fisioterapia, reabilitação, acupuntura
- Pet táxi / atendimento domiciliar
- Funeral/cremação (serviço próprio ou comissão de parceria)

### 4.5 Receita de conteúdo e autoridade (aproveitando sua experiência com educação)
- Cursos/lives para tutores (nutrição pet, primeiros socorros, comportamento animal)
- Parcerias pagas com marcas de produtos pet (divulgação/indicação)
- Conteúdo que gera tráfego orgânico → vira canal de aquisição de cliente novo pra todas as outras receitas acima (esse é o efeito que ajuda ela a "ser conhecida em todo o Brasil", mesmo a operação clínica sendo local)

### 4.6 Receita B2B — Grandes animais / clínica de produção
- Contrato recorrente de sanidade de rebanho (visita técnica programada + vacinação em massa + exames)
- Atendimento de campo avulso (cirurgia, emergência de grande porte)
- Consultoria de manejo sanitário para propriedades rurais

### 4.7 Receita B2B — Reprodução animal & biotecnologia genética (maior potencial de escala do sistema todo)
- Venda de dose de sêmen (própria central ou revenda com margem)
- Procedimento de Inseminação Artificial / IATF (por animal, por safra reprodutiva)
- Procedimento de Transferência de Embriões
- Procedimento de Fertilização in Vitro (ticket mais alto do sistema)
- Armazenamento de banco genético (sêmen/embrião/óvulo) — cobrança recorrente por custódia, semelhante a um "aluguel" de armazenamento criogênico
- Consultoria de melhoramento genético / seleção de acasalamento
- Sexagem de sêmen (serviço agregado de maior margem)
- Esta vertical é a que menos depende do tempo pessoal dela por real faturado: uma vez o protocolo/central estruturado, o volume escala por contrato com fazenda/cooperativa, não por hora de atendimento individual — é a vertical mais alinhada ao seu objetivo de "aposentadoria" citado abaixo.

### 4.8 Receita B2B — Diversos
- Comissão de indicação para laboratórios/parceiros externos
- Venda por atacado a outros pequenos negócios pet locais (se tiver escala de compra)
- Licenciamento de conhecimento técnico (ela treinando outros veterinários em protocolos de FIV/TE, por exemplo — reaproveita a Frente de Educação do seu próprio portfólio)

### 4.7 Oportunidade de longo prazo para o Grupo AMtech Digital
Vale registrar separado, sem misturar com a receita dela: se o sistema for bem construído e genuinamente resolver a dor do setor, ele mesmo vira um **produto licenciável para outras clínicas veterinárias** — seguindo exatamente o mesmo padrão comercial que você já usa no aura-licensing para o resto do ecossistema Aura. Não é prioridade agora, mas é a razão pela qual vale construir isso com o mesmo rigor arquitetural dos outros produtos Aura, e não como um sistema descartável de uso único.

---

## 5. Observação sobre porte e regulamentação

Como ela vai atender "todos os portes" (pequeno, médio, grande e possivelmente exóticos/silvestres), o sistema precisa suportar campos e fluxos clínicos diferentes por espécie desde o desenho do prontuário — não dá para tratar isso como campo de texto livre depois. Dois pontos regulatórios já confirmados que impactam diretamente o desenho de funcionalidades:

- <cite index="25-1">A telemedicina veterinária só pode ser realizada por médicos-veterinários com inscrição ativa no CFMV/CRMV, exige um Termo de Consentimento assinado eletronicamente pelo responsável do paciente</cite>, e depende da RPVAR (relação prévia estabelecida por atendimento presencial anterior) — ou seja, o sistema não pode permitir teleconsulta como "porta de entrada" sem essa relação prévia registrada, exceto em urgência/emergência.
- <cite index="29-1">O atendimento domiciliar foi regulamentado pela Resolução CFMV nº 1.690/2026, que estabelece regras para atendimento a animais de pequeno porte, exclusivo a profissional com inscrição ativa</cite> — então o módulo de "pet táxi/domiciliar" precisa restringir por porte do animal conforme essa norma.

---

Sobre a vertical de reprodução/biotecnologia especificamente: <cite index="38-1">o registro, controle e fiscalização de centros de coleta e processamento de sêmen de bovinos, bubalinos, caprinos e ovinos é regulado por portaria específica do MAPA, e há uma lei de 2024 que trata do controle de material genético animal no Brasil de forma mais ampla, incluindo clonagem.</cite> Isso significa que, diferente do módulo de pet, essa vertical não é só "mais uma funcionalidade" — é uma operação que exige registro formal do estabelecimento junto ao MAPA antes de poder faturar por ela. Vale tratar isso como pré-requisito de negócio, não só técnico, quando chegar a hora de ativar essa vertical.

## 6. Sobre venda do sistema e o objetivo de "aposentadoria"

Isso muda uma coisa importante na priorização técnica: se o objetivo final é você conseguir sair de linha de frente depois que os sistemas estiverem prontos, o critério de "o que construir primeiro" não deve ser só receita — deve ser **o que gera receita com menor dependência contínua de você ou dela pessoalmente**. Nessa lógica, dentro do próprio sistema veterinário, a ordem de prioridade de maturação muda um pouco:

1. **Pet Care** — base do sistema, alto volume, mas também a que mais depende de atendimento pessoal recorrente (menor "passividade")
2. **Grandes animais/produção** — depende de visita técnica, ainda é tempo pessoal, mas com ticket maior por hora
3. **Reprodução & biotecnologia genética** — a mais escalável e a mais alinhada ao objetivo de "aposentar": uma vez a central/protocolo estruturado, o faturamento cresce por contrato e por volume de dose/procedimento, não por hora de atendimento dela
4. **O sistema em si como produto licenciável** (seção 4.7 anterior renumerada) — o degrau final de "aposentadoria" real: se o sistema for bom o suficiente, ele te gera receita recorrente **independente da operação dela**, porque outras clínicas pagam assinatura pra usar — esse é o mesmo modelo de saída que você já está construindo com aura-licensing pro resto do ecossistema.

## 8. Reaproveitamento arquitetural e estratégia de empacotamento

Dois pontos que você confirmou e que mudam como esse sistema deve ser construído desde a base:

### 8.1 Reaproveitamento de módulos já validados no ecossistema
- **Módulo de Ordem de Serviço** (da assistência técnica) — o fluxo entrada → diagnóstico → execução → entrega/checkout se repete quase 1:1 entre "conserto de celular" e "atendimento clínico" (consulta, banho e tosa, procedimento). Em vez de desenhar um módulo de atendimento do zero pro sistema veterinário, ele deve nascer como uma **especialização do mesmo módulo de OS**, com os campos e status próprios de cada domínio adicionados por cima da mesma base — mesma lógica de entidades, mesmo padrão de status de atendimento, mesmo motor de checkout/faturamento.
- **Frente de Educação** — o conteúdo educativo do app do tutor (blog, cursos, orientação) usa a mesma infraestrutura de produção/distribuição de conteúdo que você já está montando pra Frente 4 do seu portfólio pessoal, em vez de ser um sistema de conteúdo isolado dentro do AuraVet.
- **aura-licensing** — continua sendo o motor de cobrança por trás de qualquer pacote que for vendido a outras clínicas, sem reescrever nada específico pro veterinário.
- Esse é o mesmo princípio que já rege o resto do seu ecossistema (~85% de base compartilhada): construir o sistema veterinário reaproveitando o máximo de componente já validado, e não como projeto isolado com stack ou arquitetura própria.

### 8.2 Empacotamento comercial definido só na entrega
Todas as verticais e funcionalidades deste documento (Pet Care, Grandes Animais, Reprodução/Biotecnologia, módulos complementares do brainstorm anterior) devem ser **construídas de forma modular e independente entre si desde o início** — não porque ela vai usar tudo desde o dia 1, mas porque isso é o que permite decidir o pacote comercial só no momento da entrega, sem retrabalho. Na prática:
- Cada vertical/módulo deve poder ser ativado ou desativado por tenant sem impacto nos demais (mesmo padrão de módulos gateados que você já usa nos outros produtos Aura)
- O pacote que ela efetivamente vai usar/vender primeiro (provavelmente Pet Care completo, com Grandes Animais e Reprodução como fases seguintes) só precisa ser decidido perto da entrega — a arquitetura não deve pressupor isso antes
- Isso também é o que viabiliza o modelo de licenciamento a outras clínicas: pacotes diferentes por tipo de clínica (só Pet Care, Pet Care + Grandes Animais, pacote completo com Reprodução), vendidos como planos distintos dentro do mesmo aura-licensing

---

## 9. Stack tecnológico completo

Segue exatamente o stack fixo que você já validou pro resto do ecossistema Aura — nada novo é introduzido aqui, só aplicado ao domínio veterinário.

| Camada | Tecnologia | Observação específica do AuraVet |
|---|---|---|
| Backend | C#/.NET 10, ASP.NET Core (Controllers) | Mesmo padrão dos outros produtos — Controllers, não Minimal API |
| Arquitetura | Clean Architecture + DDD (Domain/Application/Infrastructure/Api) | Módulo de atendimento nasce como especialização do módulo de OS já validado na assistência técnica |
| ORM | Entity Framework Core | — |
| Banco de dados | PostgreSQL + **PostGIS** | PostGIS é essencial aqui (diferente de produtos anteriores que usam Postgres puro): atendimento domiciliar e visita técnica de campo em grandes animais precisam de geolocalização real, não endereço em texto |
| Cache/sessão | Redis | Cache de catálogo da loja, sessão de carrinho |
| Tempo real | SignalR | Status de internação em tempo real pro tutor; status de protocolo reprodutivo em tempo real pro produtor (painel B2B) |
| Autenticação | JWT + BCrypt | Mesmo padrão AM Kaixara |
| Frontend web | TypeScript, Next.js, Tailwind CSS | Painel administrativo + loja/e-commerce |
| App/portal do tutor | Next.js (PWA) inicialmente | Decisão de app nativo (React Native ou similar) fica pra quando o volume justificar — não é stack fixado ainda, registrar como pendência |
| Testes | xUnit (backend) | Mesmo padrão dos outros produtos |
| CI/CD | GitHub Actions | — |
| Containerização | Docker / docker-compose | — |
| Cobrança/licenciamento | aura-licensing (serviço compartilhado) | Reaproveitado, sem stack próprio |
| Armazenamento de arquivos | Cloudflare R2 | Laudos, imagens de exame, fotos de internação — mesmo provedor já usado no Momentos/Cupido |
| Pagamentos | Gateway (Pix, cartão, boleto) | A definir provedor (Mercado Pago/PagBank), mesmo critério usado no freela de sites |
| Emissão fiscal | Provedor terceiro de NFe/NFSe | Não reinventar motor fiscal próprio |
| Notificação | WhatsApp Business API + push + e-mail transacional | Lembretes de consulta/vacina/retorno |
| Multi-tenant | Mesmo padrão `tenant_id` + isolamento (RLS quando necessário) | Base para o modelo de licenciamento a outras clínicas no futuro |

**Tecnologias explicitamente fora**, seguindo suas decisões já tomadas pro resto do ecossistema: Bun, Hono, Rust, Tauri, gRPC.

---

## 10. MVP — escopo multi-porte, com vendas e receita recorrente

**Princípio do MVP:** ela não pode ficar limitada por porte/espécie mesmo na primeira versão — mas isso não significa lançar todas as verticais completas de uma vez. Significa que o **modelo de dados** nasce aberto (qualquer espécie/porte cabe no cadastro desde o dia 1), enquanto os **fluxos operacionais mais complexos** (reprodução/biotecnologia, contrato de sanidade de rebanho, GTA) entram em fases seguintes. Fazer o contrário — travar o schema em "cachorro/gato" e ter que migrar depois — é o erro caro de se evitar aqui.

### Escopo incluído no MVP

**Cadastro e atendimento (aberto a qualquer porte)**
- Cadastro de tutor/conta — suporta tanto pessoa física (tutor de pet) quanto conta B2B (propriedade rural), mesmo que o fluxo B2B completo só amadureça depois
- Cadastro de animal com espécie/porte como campo extensível (cão, gato, exótico pequeno, equino, bovino, caprino, ovino, suíno, silvestre — enum aberto, não fixo em "pet")
- Agenda (self-service + recepção), sem limitação por tipo de animal
- Prontuário eletrônico com histórico, adaptável por espécie (campos específicos habilitam conforme o tipo de animal cadastrado)
- Prescrição digital, com distinção de medicamento comum/controlado desde o início

**Vendas e receita (incluído desde o MVP, como você pediu)**
- Loja/e-commerce de produtos: catálogo, carrinho, checkout, controle de estoque básico
- Assinatura recorrente (plano de saúde pet / clube de produtos): cobrança automática mensal, gestão de status ativo/inadimplente
- Financeiro: emissão de NF (produto e serviço), pagamento via Pix/cartão, orçamento prévio aprovável pelo tutor

**Operação**
- Painel administrativo com controle de acesso por papel (recepção, veterinário, financeiro, admin)
- Portal/app do tutor: histórico do pet, agendamento, compra na loja, assinatura do plano

### Fora do MVP (fases seguintes, arquitetura já preparada para receber)
- Fluxo completo de Grandes Animais (GTA, ficha sanitária de rebanho, contrato de visita técnica recorrente)
- Fluxo completo de Reprodução & Biotecnologia (rastreabilidade de dose/embrião, conformidade MAPA, painel B2B de protocolo)
- Telemedicina completa (RPVAR, termo de consentimento eletrônico)
- Hotel/creche, banho e tosa, fisioterapia (agendas de serviço complementar)
- Multi-unidade/franquia e licenciamento a terceiras clínicas

Essa divisão não é sobre "o que é menos importante" — é sobre o que precisa estar certo na modelagem desde o início (porte/espécie, vendas, recorrência) versus o que pode ser construído por cima sem quebrar nada depois (fluxos operacionais mais específicos de cada vertical).

---

## 11. Próximo passo natural

Este documento cobre o quê o sistema precisa ter. O próximo passo é priorizar: dado que a formação dela ainda leva ~3 anos, dá pra tratar isso como um projeto de maturação longa dentro do seu roadmap — provavelmente como uma trilha paralela de baixa intensidade agora (arquitetura e módulos essenciais, começando pelo Pet Care) crescendo perto da formatura dela, sem competir agora com o tempo que o AM Kaixara precisa. As verticais de grandes animais e reprodução/biotecnologia podem entrar como fase 2 desse projeto — depois que ela tiver definido se vai atuar nessas áreas de fato, já que exigem registro MAPA e conhecimento técnico bem mais específico.

## 12. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml` de produção (separado do ambiente de desenvolvimento), pipeline GitHub Actions (build → teste → deploy automático), deploy em serviço gerenciado (AWS ou Azure — mesma decisão pendente transversal ao portfólio). Como o AuraVet tem maturação natural de ~3 anos até o lançamento real (ligada à formatura dela), essa infraestrutura não precisa estar pronta agora — mas vale já registrar que segue o mesmo padrão dos demais, sem necessidade de decisão especial.

---

## 13. Status atual de desenvolvimento

**Nenhum código foi escrito ainda.** Este documento existe inteiramente como planejamento — funcionalidades, RF/RNF, stack e MVP já formalizados, mas nenhuma linha de backend ou frontend foi iniciada. Diferente dos sistemas com prazo comercial mais próximo, aqui isso é esperado e não é um problema: a trilha de baixa intensidade sugerida (seção 11 do documento original) pressupõe justamente que o código só começa a ganhar ritmo perto da formatura dela.

---

## 14. Sistemas e interfaces paralelas por perfil de usuário

### 12.1 Tutor (pessoa física, vertical Pet Care)
- **Cadastro:** self-service pelo app/portal do tutor
- **Uso:** agendamento, histórico do pet, compra na loja, assinatura do plano de saúde pet
- **Suporte:** chat/canal direto com a clínica (já previsto na seção 1.10)

### 12.2 Produtor/conta B2B (vertical Grandes Animais e Reprodução)
- **Cadastro:** cadastro de propriedade rural como conta-cliente (RF23), provavelmente assistido pela clínica no início, não self-service puro
- **Uso:** painel remoto de acompanhamento de protocolo (RF31)
- **Suporte:** canal técnico distinto do tutor comum — a natureza da dúvida (status de gestação de embrião vs. agendamento de banho) é completamente diferente, não deveria compartilhar o mesmo canal de atendimento

### 12.3 Veterinário/equipe clínica
- **Cadastro:** criado pelo admin da clínica (ela mesma, inicialmente)
- **Uso:** prontuário, prescrição, agenda, painel administrativo (seção 1.9)
- **Suporte:** mesma lógica do operador de caixa do AM Kaixara — dúvida operacional resolvida internamente pela admin da clínica, não pelo seu suporte

### 12.4 Suporte técnico interno (Grupo AMtech)
- **Lacuna, mesmo padrão identificado no AM Kaixara e no Delivery:** nenhum painel de suporte interno foi especificado até agora para o AuraVet. Como este sistema tem a vertical de Reprodução & Biotecnologia com exigência de conformidade MAPA, o suporte interno aqui também precisaria de visibilidade sobre status de registro/conformidade por tenant, não só sobre dado operacional comum.

---

## 15. Segurança de nível profissional

Aplicação concreta do checklist geral ([[distribuicao-licenciamento-seguranca]]) a este sistema:

| Categoria | Aplicação específica no AuraVet |
|---|---|
| Dados sensíveis | Prontuário eletrônico e dado de tutor são dados pessoais sensíveis por associação (RNF já detalhado na seção de RNF de Segurança/LGPD) — criptografia em repouso e trânsito, auditoria de acesso por prontuário. **RESOLVIDO/atualizado:** implementado via `aura-vault`, o serviço compartilhado de proteção de dado extra-sensível, em vez de implementação própria isolada |
| Rastreabilidade genética (vertical Reprodução) | Já é RNF formal (seção 3) — vale reforçar aqui que essa rastreabilidade também é requisito de segurança, não só de conformidade: perda de vínculo de rastreio de material genético é tanto risco legal quanto risco de fraude |
| Conexão entre sistemas (RNFT-S03/S04) | Se o AuraVet for vendido como produto licenciável a outras clínicas (seção 8), a mesma lógica de consentimento explícito e credencial de escopo mínimo se aplica |
| Segregação de público | Interface de tutor pessoa física e de produtor B2B precisam ser claramente segregadas (já é RNF), o que também reduz superfície de erro/vazamento entre os dois perfis |
| Auditoria externa (RNFT-S06) | Prioridade média — este sistema tem maturação de ~3 anos até o lançamento comercial real, então o pentest formal pode ser planejado mais perto do lançamento, não agora |

---

## 16. Pendências e decisões em aberto

1. **Cor base e paleta de marca** — ainda pendente da informação que ela já passou (nome/hex da cor).
2. **Decisão dela sobre atuar ou não na vertical de Reprodução & Biotecnologia** — trava o início do trabalho de conformidade MAPA.
3. **App nativo vs. PWA** para o portal do tutor — mesma pendência já registrada em outros sistemas do portfólio, decisão única recomendada.
4. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado como serviço compartilhado, com a mesma restrição de acesso a metadado (não conteúdo de prontuário) que a seção 12 (Segurança) deste documento já previa.
5. **Provedor de gateway de pagamento** — ainda não definido (mesma pendência transversal do AM Consertta/AM Kaixara).

