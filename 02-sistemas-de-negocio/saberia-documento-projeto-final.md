---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Saberia — Documento de Projeto Final (Nome provisório)
### Sistema de Gestão Escolar, Cursinho e Curso Livre

Segue a estrutura fixa do [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md).

---

## 1. Visão do produto

Plataforma de gestão para escola particular pequena, cursinho preparatório, curso técnico ou curso livre (idiomas, reforço), cobrindo matrícula, diário de classe, financeiro recorrente e conteúdo didático — reaproveitando ~85-90% da arquitetura já validada no AuraVet (agendamento + histórico + assinatura recorrente + loja de produto), aplicada ao domínio educacional.

**Diferencial de inovação, e o mais pessoal de todo o portfólio:** você é professor de verdade, já tem 180 apostilas prontas do EMTI, e entende a dor de quem vai comprar isso de um jeito que nenhum desenvolvedor comum entende. Nenhum outro sistema do portfólio tem essa vantagem de proximidade real com o comprador. Além disso, o sistema já nasce com um diferencial de conteúdo — as apostilas existentes viram material didático embutido, não um produto vazio esperando o cliente preencher.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Cadastro e matrícula
- Cadastro de aluno e responsável (obrigatório para menor de idade)
- Matrícula em turma/curso, com turno e horário
- Fluxo de matrícula/rematrícula anual — diferente de assinatura contínua, tem sazonalidade própria (janela de rematrícula, desconto por antecipação)

### 2.2 Diário de classe e avaliação
- Frequência, nota, boletim — especialização do mesmo "prontuário eletrônico" já formalizado no AuraVet, aqui adaptado a histórico acadêmico
- Prova/avaliação online, com correção automática para questão objetiva
- Emissão de declaração, histórico escolar e certificado (para cursinho/curso técnico)

### 2.3 Comunicação e portal
- Agenda digital escola-responsável (recado, ocorrência, aviso de reunião)
- Portal do aluno/responsável: nota, frequência, financeiro, material didático

### 2.4 Financeiro
- Mensalidade recorrente com escada de inadimplência graduada — mesmo padrão do `aura-licensing`, aplicado a aluno em vez de tenant de software
- Desconto por irmão/antecipação, taxa de matrícula separada da mensalidade

### 2.5 Conteúdo e aula
- Aula síncrona (EAD ao vivo) e assíncrona (gravada) — especialização do mesmo módulo de telemedicina do AuraVet, aqui aplicado a aula em vez de consulta
- Biblioteca de material didático, incluindo as 180 apostilas já existentes como conteúdo inicial embutido

### 2.6 Loja de material
- Venda de apostila física/digital, uniforme, material escolar — reaproveitando o padrão de loja já validado em AM Consertta/AuraVet, com envio via `aura-logistics` quando físico

### 2.7 Gestão de professor
- Alocação de turma, carga horária, remuneração por aula/turma — reaproveitando o padrão de comissionamento já formalizado no AM Consertta

### 2.8 Vertical B2B
- Venda do sistema para outras escolas pequenas ou professores particulares que queiram usar a mesma plataforma — mesmo modelo de licenciamento já aplicado ao AuraVet

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Cadastro de aluno vinculado a responsável legal quando menor de idade | Base de identidade e de comunicação — responsável precisa estar sempre acessível para menor |
| RF02 | Matrícula em turma/curso com turno e horário, e fluxo específico de rematrícula anual | Cobre a sazonalidade real do calendário escolar, diferente de assinatura contínua sem ciclo |
| RF03 | Registro de frequência e nota por aula, consolidado em boletim | Substitui controle manual/planilha, com histórico sempre disponível |
| RF04 | Aplicação de avaliação online, com correção automática de questão objetiva | Reduz tempo de correção manual para o professor |
| RF05 | Emissão de declaração, histórico escolar e certificado | Formaliza documento que o aluno/responsável frequentemente precisa apresentar em outra instituição |
| RF06 | Agenda digital de comunicação escola-responsável | Reduz dependência de grupo de WhatsApp informal e desorganizado, hoje comum no setor |
| RF07 | Portal do aluno/responsável com nota, frequência, financeiro e material | Centraliza tudo que hoje normalmente está espalhado entre caderno, e-mail e ligação |
| RF08 | Cobrança de mensalidade recorrente com escada de inadimplência graduada | Reduz inadimplência sem gerar corte abrupto, mesmo padrão já validado em outros sistemas do portfólio |
| RF09 | Suporte a aula síncrona (ao vivo) e assíncrona (gravada) | Cobre tanto o modelo presencial quanto EAD, sem exigir sistema separado |
| RF10 | Biblioteca de material didático, com suporte a conteúdo pré-carregado | Viabiliza lançar o sistema já com conteúdo real (as 180 apostilas), não vazio |
| RF11 | Loja de material didático/uniforme, com envio via `aura-logistics` quando físico | Reaproveita o módulo de logística compartilhado em vez de reconstruir |
| RF12 | Alocação de turma e comissionamento por professor | Reaproveita o padrão de comissionamento já formalizado no AM Consertta |
| RF13 | Licenciamento do sistema para outras escolas/professores particulares via `aura-licensing` | Abre a vertical B2B sem reescrever nada da base |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Aluno
- **Cadastro:** próprio (se maior de idade) ou vinculado a responsável (se menor)
- **Uso:** portal do aluno, aula, avaliação online
- **Suporte:** canal da escola/cursinho, não do Grupo AMtech diretamente — mesma lógica já aplicada a outros sistemas do portfólio

### 4.2 Responsável (obrigatório para aluno menor de idade)
- **Cadastro:** vinculado ao aluno, com acesso próprio ao portal
- **Uso:** acompanha nota, frequência e financeiro do menor
- **Suporte:** mesmo canal do aluno

### 4.3 Professor
- **Cadastro:** criado pela direção da escola/cursinho
- **Uso:** diário de classe, lançamento de nota, ministrar aula síncrona/assíncrona
- **Suporte:** canal interno da própria instituição

### 4.4 Direção/coordenação (dono do negócio ou responsável administrativo)
- **Cadastro:** criado na configuração inicial pós-compra
- **Uso:** gestão financeira, alocação de professor, emissão de documento oficial
- **Suporte:** canal com o Grupo AMtech Digital

### 4.5 Suporte técnico interno
- Reaproveita o `aura-support` já formalizado — sem lacuna nova aqui, diferente de quando este documento teria sido escrito antes daquele serviço existir.

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no AM Saberia | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado de menor de idade é categoria com proteção reforçada — exige consentimento do responsável, não do próprio titular | Cumpre obrigação legal específica para dado de criança/adolescente, mais rígida que dado de adulto |
| RNFT-E01 (concorrência) | Matrícula em turma com vaga limitada não pode aceitar mais alunos que o limite simultaneamente | Mesmo princípio de concorrência já aplicado a estoque, aqui aplicado a vaga de turma |
| RNFT-E02 (idempotência de pagamento) | Cobrança de mensalidade recorrente | Evita cobrança duplicada em reenvio de webhook |
| Retenção de histórico acadêmico (próprio) | Histórico escolar e nota devem ser mantidos por prazo compatível com a vida útil do documento (o aluno pode precisar do histórico décadas depois) | Diferente da maioria dos dados do portfólio, aqui a obrigação de guarda é de muito longo prazo, não só alguns anos |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no AM Saberia |
|---|---|
| Dados de menor | Consentimento do responsável, não do aluno, quando menor de idade — controle de acesso deve refletir isso na própria estrutura de permissão, não só na política |
| Auditoria externa | Prioridade média — não processa pagamento de alto valor nem dado altamente sensível como saúde, mas tem volume de dado pessoal de menor de idade relevante |
| Conexão entre sistemas | Se a escola também usar AM Consertta/AuraVet, mesma regra de consentimento explícito e escopo mínimo do restante do portfólio |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** SaaS puro, sem componente físico dedicado — diferente do AM Kaixara/AM Predara. O único "hardware" indireto é o dispositivo do professor/aluno para aula síncrona, sem integração especial exigida.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions.

---

## 9. Modelo de receita — todas as formas de venda

| Fonte | Modelo |
|---|---|
| Assinatura SaaS por aluno ativo ou por escola | Mensalidade recorrente, escalando com o tamanho da instituição |
| Taxa de setup/onboarding | Cobrança única na implantação |
| Módulo de conteúdo (apostilas incluídas) | Diferencial de venda — parte do valor percebido já vem pronto, não é add-on separado |
| Loja de material didático | Comissão/margem sobre venda de apostila física, uniforme, material |
| **Licenciamento a outras escolas/professores particulares** | Canal B2B — mesma lógica de venda white-label já aplicada a outros serviços do portfólio |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização completa deste sistema, adiado conscientemente até a infraestrutura compartilhada estar pronta — condição já cumprida.

---

## 11. Pendências e decisões em aberto

1. **Validação com profissional de gestão educacional** sobre exigências específicas de credenciamento junto à Secretaria de Educação (para escola regular, diferente de cursinho livre) — recomendo essa validação antes de tratar RF05 (emissão de histórico escolar oficial) como pronto para produção, mesmo raciocínio já aplicado ao AM Canteira com advogado.
2. **Provedor de videoaula síncrona** — solução própria vs. integração com Zoom/Google Meet, ainda não decidido.
3. **Prazo formal de retenção de histórico acadêmico** — precisa de definição mais precisa que "muito longo prazo".
4. **Provedor de gateway de pagamento** — mesma pendência transversal do restante do portfólio.
