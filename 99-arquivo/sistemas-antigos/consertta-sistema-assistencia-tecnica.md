---
tags: [sistema/negocio, portfolio-ams]
tipo: sistema-negocio
status: completo
---

# AM Consertta — Sistema Central da Assistência Técnica e Loja (Nome provisório)
### Ordem de Serviço + Loja Física (PDV) + Loja Online

> **Nota sobre estrutura:** documento criado antes do [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md) existir, com numeração própria. Conteúdo equivalente às seções 1, 2, 4, 6, 8-9 do template já existe aqui. As seções 8-10, adicionadas ao final, cobrem perfis de usuário, segurança concreta e pendências — equivalente às seções 3, 5 e 10 do template.

## 0. O insight mais importante antes de qualquer funcionalidade

Você pediu "mais um sistema perfeito" — mas a notícia boa é que **isso não é um sistema novo do zero**. É a convergência de três peças que já existem ou já estavam planejadas no seu portfólio, nunca antes juntadas com esse propósito:

| Peça | Situação atual | Papel no AM Consertta |
|---|---|---|
| **AM Kaixara** | Em desenvolvimento ativo (Sprint 3-4) | Vira o motor de PDV/estoque da loja física — reaproveitado quase inteiro, sem reescrever nada de produto/estoque/venda/caixa |
| **Loja Virtual** | Já tinha documento de visão (e-commerce integrado ao estoque do AM Kaixara) | Vira a loja online do AM Consertta — é literalmente o produto que você já tinha concebido pra isso, só nunca com a assistência técnica como o caso de uso concreto |
| **Módulo de Ordem de Serviço** | Só identificado como ideia, nunca formalizado (gap apontado no documento de status do portfólio) | É a única peça genuinamente nova — e ao formalizá-la aqui, você fecha ao mesmo tempo a pendência que travava o módulo de atendimento do AuraVet |

Ou seja: planejar o AM Consertta bem feito **resolve duas dívidas do portfólio de uma vez** — dá à assistência técnica o sistema que ela precisa, e entrega ao AuraVet a base de Ordem de Serviço que ele já estava esperando reaproveitar.

---

## 0.1 Ajuste de premissa: operação remota, alcance nacional

Como você vai trabalhar só de casa e quer clientes em todo o Brasil, o modelo original ("loja física com cliente presencial + loja online como canal adicional") estava invertido. O padrão precisa ser o oposto: **operação remota como fluxo principal, presencial (se você atender alguém local) como exceção que o mesmo sistema também sabe lidar**. Isso muda três fluxos que antes eram tratados como presenciais por padrão:

1. **Recebimento de aparelho para conserto** — hoje modelado como "cliente traz na loja"; precisa nascer também como "cliente envia pelo correio/transportadora"
2. **Envio de produto vendido** — a loja online já previa isso, mas agora é o fluxo principal, não secundário
3. **Devolução do aparelho consertado** — precisa do mesmo tratamento de envio nacional, com o cuidado adicional de ser um aparelho de terceiro (maior sensibilidade que uma venda nova)

Isso não é só "adicionar uma funcionalidade de frete" — é um módulo novo e transversal, porque os três fluxos acima compartilham a mesma necessidade: gerar etiqueta, calcular frete, rastrear, confirmar recebimento/entrega. Detalhado abaixo.

## 1. Funcionalidades

### 1.0 Logística e Envios (módulo novo — transversal aos outros três)

- **Postagem de entrada (cliente → você):** geração de instruções/etiqueta para o cliente enviar o aparelho, com checklist de embalagem recomendada (evitar dano em trânsito) e opção de seguro sobre o valor declarado do aparelho
- **Conferência de recebimento remoto:** check-in do aparelho ao chegar, com fotos e comparação com o que o cliente declarou ter enviado (mesmo espírito do checklist presencial, adaptado pra quem não está na sua frente)
- **Cálculo de frete por CEP** — integrado ao checkout da loja online e à abertura de OS remota
- **Geração de etiqueta e rastreio** — integração com Correios e/ou transportadora privada, com código de rastreio vinculado à OS ou ao pedido
- **Postagem de saída (você → cliente):** aplica-se tanto para produto vendido quanto para aparelho consertado devolvido — mesmo módulo, dois motivos de envio diferentes
- **Notificação automática de status de envio** (postado, em trânsito, entregue) — mesmo canal de notificação já usado para status de OS (WhatsApp)
- **Política de seguro/responsabilidade em trânsito** — precisa estar clara pro cliente antes do envio, especialmente em aparelhos de alto valor; isso é decisão de negócio (o que você cobre, o que exige seguro à parte), não só técnica — vale definir antes de formalizar o RF
- **Suporte a atendimento local presencial como opção, não como padrão** — se algum cliente de Barbacena preferir entregar em mãos, o mesmo módulo de OS aceita isso sem exigir código de rastreio, mas o design não pressupõe mais que esse é o caminho principal

---

### 1.1 Ordem de Serviço (módulo novo — o core do AM Consertta)
- Abertura de OS com checklist de recebimento (estado do aparelho, acessórios, senha/padrão informado pelo cliente, fotos de entrada)
- Termo de responsabilidade digital assinado pelo cliente na abertura (LGPD — autorização de acesso a dados do aparelho)
- Diagnóstico técnico vinculado à OS, com orçamento gerado a partir do diagnóstico
- Aprovação do orçamento pelo cliente (digital, com registro de quando e como foi aprovado)
- Reserva automática de peça no estoque (integração direta com o módulo de estoque do AM Kaixara) assim que o orçamento é aprovado
- Linha do tempo de status da OS (recebido → em diagnóstico → aguardando aprovação → em reparo → controle de qualidade → pronto → entregue), com notificação automática ao cliente a cada mudança
- Checklist de controle de qualidade antes da entrega
- Garantia vinculada à OS (prazo, cobertura, histórico de retorno em garantia)
- Histórico completo de aparelho por cliente (útil para clientes recorrentes — "esse cliente já trouxe esse iPhone duas vezes")

### 1.2 Loja física (reaproveitando o AM Kaixara)
- Catálogo de peças, acessórios e aparelhos para revenda
- PDV completo (já existe no AM Kaixara — sem necessidade de recriar)
- Controle de estoque compartilhado entre loja física, loja online e reserva automática de OS (é o mesmo estoque, três portas de saída diferentes)
- Venda avulsa (sem vínculo com OS) — cliente que só quer comprar capinha, película, cabo

### 1.3 Loja online (reaproveitando a Loja Virtual)
- Catálogo público, carrinho, checkout
- Mesma base de estoque do PDV físico e da reserva de OS — sem risco de vender online algo que já foi reservado presencialmente
- Rastreamento de pedido (separação → envio/retirada → entregue)
- Possibilidade de "orçamento online": cliente descreve o defeito pelo site e recebe estimativa antes de levar o aparelho — vira porta de entrada de OS

### 1.4 Vendas e receita recorrente
- Assinatura de manutenção preventiva para empresas (frota de celular corporativo — já estava no seu plano original da assistência técnica)
- Garantia estendida como produto vendável à parte (não só a garantia padrão do reparo)
- Programa de fidelidade (pontos por compra/reparo, resgatáveis em produto)

### 1.5 Financeiro e gestão
- Emissão de nota fiscal por produto e por serviço (tratamento fiscal diferente, como no AuraVet)
- Comissionamento por técnico (se/quando contratar o primeiro técnico assistente — já mapeado como gatilho de contratação no plano mestre)
- Relatório de rentabilidade por tipo de serviço (troca de tela vs. microssolda vs. venda de acessório)

---

### 1.6 Escala presencial (multi-unidade, multi-técnico)
- Cadastro de unidade física (endereço, horário, responsável técnico) — hoje o plano assumia uma única bancada em casa; isso muda se você abrir uma segunda unidade ou contratar técnico em outra cidade
- OS e estoque vinculados à unidade de origem, com visão consolidada no painel administrativo (mesmo padrão multi-unidade já usado no AuraVet)
- Transferência de peça entre unidades, com rastreabilidade (evita "sumiço" de estoque quando há mais de uma bancada)
- Agenda de técnico por unidade, para quando o gatilho de contratação do plano mestre for acionado (fila > 5-7 dias)
- Pontos de retirada/postagem físicos distintos do endereço "casa" — se abrir unidade em outra cidade, ela também pode ser ponto de recebimento presencial de aparelho, reduzindo dependência só do envio postal

---

## 2. Requisitos Funcionais (RF) — específicos do módulo de Ordem de Serviço

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | O sistema deve permitir abertura de OS com checklist de recebimento e registro fotográfico do estado do aparelho | Evita disputa sobre "em que estado o aparelho chegou" |
| RF02 | O sistema deve gerar termo de responsabilidade digital assinável na abertura da OS | Formaliza autorização de acesso ao aparelho/dado do cliente, protegendo ambas as partes |
| RF03 | O sistema deve vincular um orçamento à OS, gerado a partir do diagnóstico técnico | Formaliza o valor antes de executar o reparo, evitando surpresa pro cliente |
| RF04 | O sistema deve registrar a aprovação do orçamento pelo cliente, com data/hora e meio de aprovação | Evidência de consentimento, essencial em caso de disputa |
| RF05 | O sistema deve reservar automaticamente a peça necessária no estoque compartilhado assim que o orçamento for aprovado | Garante que a peça exista quando o técnico for executar, sem depender de checagem manual |
| RF06 | O sistema deve notificar o cliente automaticamente a cada mudança de status da OS | Reduz ligação de "como está meu aparelho" e melhora percepção de profissionalismo |
| RF07 | O sistema deve manter checklist de controle de qualidade obrigatório antes de marcar a OS como pronta | Reduz retorno por reparo malfeito |
| RF08 | O sistema deve vincular garantia à OS, permitindo abrir OS de retorno vinculada à original | Formaliza cobertura e mantém histórico de reincidência no mesmo aparelho |
| RF09 | O sistema deve manter histórico de aparelhos por cliente, incluindo OS anteriores do mesmo aparelho | Acelera diagnóstico de cliente recorrente e identifica padrão de defeito |
| RF10 | O estoque deve ser único e compartilhado entre loja física, loja online e reserva de peça por OS | Impede vender/reservar a mesma última unidade por dois canais ao mesmo tempo |
| RF11 | O sistema deve permitir venda avulsa de produto sem vínculo com nenhuma OS | Capta receita de quem só quer comprar produto, sem forçar abertura de OS |
| RF12 | O sistema deve permitir orçamento solicitado pela loja online antes da abertura formal da OS presencial | Reduz fricção de entrada — cliente sabe o custo estimado antes de se comprometer |
| RF13 | O sistema deve calcular frete por CEP tanto para venda de produto quanto para envio/devolução de aparelho em reparo | Pré-requisito para operar nacionalmente, cobrando frete correto por região |
| RF14 | O sistema deve gerar etiqueta de postagem e código de rastreio, vinculando o rastreio à OS ou ao pedido de origem | Viabiliza operação remota sem depender de acompanhamento manual do envio |
| RF15 | O sistema deve permitir conferência de recebimento remoto (fotos + checklist) quando o aparelho chegar por envio | Mantém o mesmo rigor de evidência do fluxo presencial, mesmo sem contato visual |
| RF16 | O sistema deve notificar automaticamente o cliente a cada mudança de status do envio | Substitui a confiança do contato presencial por transparência de rastreio |
| RF17 | O sistema deve suportar tanto o fluxo remoto quanto o presencial para o mesmo tipo de OS | Atende tanto o cliente nacional quanto o cliente local de Barbacena, sem exigir dois sistemas |
| RF18 | O sistema deve suportar cadastro de unidade física, com OS e estoque vinculados à unidade de origem e transferência rastreável de peça entre unidades | Viabiliza crescer para mais de uma bancada sem perder controle de onde está cada peça |
| RF19 | O sistema deve suportar plano de manutenção preventiva empresarial, garantia estendida como produto à parte, e programa de fidelidade | Formaliza as três fontes de receita recorrente do sistema, além do reparo avulso |
| RF20 | O sistema deve calcular comissionamento por técnico e relatório de rentabilidade por tipo de serviço | Necessário a partir do primeiro técnico contratado, e dá visibilidade de qual serviço realmente vale a pena priorizar |

*(Requisitos de PDV, estoque, financeiro e loja online seguem os RF/RNF já formalizados do AM Kaixara e da Loja Virtual — não precisam ser reescritos aqui, só referenciados.)*

---

## 3. Requisitos Não Funcionais — específicos deste sistema

| Categoria | Requisito | Para que serve |
|---|---|---|
| **Consistência de estoque** | A reserva de peça por OS precisa ser atômica em relação à venda no PDV e no e-commerce | Impede vender/reservar a mesma última unidade por dois canais ao mesmo tempo |
| **Auditabilidade** | Toda mudança de status de OS e toda aprovação de orçamento deve ser registrada de forma imutável | Evidência em caso de disputa com cliente |
| **LGPD** | Termo de responsabilidade e dado sensível do cliente/aparelho precisa do mesmo padrão de proteção dos outros sistemas | Cumpre obrigação legal e reduz dano em caso de vazamento |
| **Disponibilidade do PDV** | O caixa físico não pode ficar indisponível por instabilidade do módulo de OS ou da loja online | Isola falha de um módulo para não travar a operação de venda presencial |
| **Confiabilidade de rastreio** | Rastreio e notificação de status precisam ser confiáveis o bastante para substituir a confiança do atendimento presencial | Cliente remoto não tem contato visual — falha aqui tem custo de reputação maior que num sistema local |
| **Escala operacional de uma pessoa só** | O sistema deve minimizar cliques/etapas manuais nos fluxos de envio | Você sozinho de casa não escala se cada operação exigir trabalho manual repetitivo |

---

## 4. Fontes de renda

### 4.1 Serviço (Ordem de Serviço)
- Reparo (troca de tela/bateria, diagnóstico, desbloqueio, microssolda)
- Garantia estendida como produto à parte

### 4.2 Produto (loja física + online, mesmo catálogo)
- Peças, acessórios, aparelhos para revenda
- Venda avulsa sem vínculo com reparo

### 4.3 Recorrência
- Plano de manutenção preventiva para empresas (frota corporativa)
- Programa de fidelidade/pontos

### 4.4 Canal digital
- Orçamento online como porta de entrada de novo cliente de OS
- Loja online vendendo fora do horário de funcionamento da loja física

---

## 5. Stack tecnológico

Mesmo stack fixo do restante do ecossistema — a única decisão real aqui é arquitetural (como o módulo de OS se conecta ao que já existe), não de tecnologia nova.

| Camada | Tecnologia | Observação |
|---|---|---|
| Backend | C#/.NET 10, ASP.NET Core (Controllers), Clean Architecture + DDD | Módulo de OS nasce como novo bounded context, consumindo o mesmo serviço de estoque do AM Kaixara em vez de duplicar |
| Banco de dados | PostgreSQL | Sem necessidade de PostGIS aqui (diferente do AuraVet/Delivery) — não há componente de rota neste sistema |
| Cache/sessão | Redis | Cache de catálogo compartilhado entre PDV e loja online |
| Tempo real | SignalR | Status de OS em tempo real (painel interno e notificação ao cliente) |
| Autenticação | JWT + BCrypt | Mesmo padrão |
| Frontend loja física/admin | Next.js, TypeScript, Tailwind | Reaproveita componentes já existentes do AM Kaixara |
| Frontend loja online | Next.js, TypeScript, Tailwind | Reaproveita o que já foi pensado pra Loja Virtual |
| Cobrança/licenciamento | `aura-licensing` | Mesmo motor — precisa ter seu RF/RNF formalizado antes (gap já apontado no documento de status) |
| Frete e rastreio | Integração com API dos Correios e/ou transportadora privada | Novo ponto de integração externa deste sistema — não existia nos outros produtos do portfólio nesse formato |
| Notificação | WhatsApp Business API | Mesmo padrão usado no AuraVet — agora também cobrindo status de envio, não só de OS |
| Multi-tenant | `tenant_id` + RLS | Mesmo padrão — relevante se algum dia licenciar o AM Consertta para outras assistências técnicas |

---

## 6. MVP

**Incluído:**
- Abertura, diagnóstico, orçamento, aprovação e acompanhamento de status de OS
- Reserva automática de peça vinculada ao estoque do AM Kaixara
- PDV físico (reaproveitado do AM Kaixara, sem retrabalho)
- Loja online básica (catálogo, carrinho, checkout, mesmo estoque)
- **Módulo de Logística e Envios**: cálculo de frete por CEP, geração de etiqueta/rastreio, conferência de recebimento remoto, notificação automática de status — cobrindo os três fluxos (aparelho para conserto, produto vendido, aparelho devolvido)
- Notificação automática de status por WhatsApp
- Garantia vinculada à OS

**Fora do MVP (fases seguintes):**
- Programa de fidelidade/pontos
- Plano de manutenção preventiva empresarial
- Comissionamento por técnico (só relevante quando houver mais de uma pessoa na bancada)
- Seguro de transporte como produto formal à parte (o MVP pode nascer só com a política de responsabilidade definida, sem a integração de seguro automatizada)

---

## 7. Consequência direta para o resto do portfólio

Ao formalizar este documento, dois itens da lista de lacunas do status geral do portfólio ficam resolvidos ou parcialmente resolvidos:
- **Módulo de Ordem de Serviço**: sai de "ideia identificada" para "RF/RNF formalizado" — o AuraVet agora tem uma base real para reaproveitar, não só conceitual.
- **Loja Virtual**: ganha um caso de uso concreto e um conjunto de requisitos vindo de um cenário real (assistência técnica), o que ajuda a reduzir a incerteza que a própria Claude tinha sinalizado nesse documento anteriormente.

Um terceiro ponto, que surge só agora: como você quer alcance nacional em **todos** os sistemas que vendem produto físico, o **Módulo de Logística e Envios** não deveria nascer só dentro do AM Consertta — ele é candidato natural a virar um serviço compartilhado (nos mesmos moldes do `aura-licensing`), reaproveitável por qualquer sistema do portfólio que precise enviar algo fisicamente: a Loja Virtual (quando vender fora do contexto de assistência técnica) e a loja de produtos do AuraVet (ração, medicamento, acessórios) são os dois candidatos mais óbvios. Vale registrar isso como decisão a tomar antes de codificar — construir o módulo já pensando em ser consumido por mais de um sistema custa pouco a mais agora e evita reescrever depois.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante do ecossistema — Dockerfile multi-stage, `docker-compose.yml` de produção, pipeline GitHub Actions (build → teste → deploy). Ponto de atenção específico deste sistema: como o módulo de Logística (seção 1.0) depende de integração externa (Correios/transportadora), vale incluir teste de contrato dessa integração no pipeline, não só teste unitário interno — é o tipo de dependência externa que quebra silenciosamente se a API do provedor mudar.

---

## 9. Status atual de desenvolvimento

**Nenhum código foi escrito ainda.** Este documento existe inteiramente como planejamento — funcionalidades, RF/RNF, stack e MVP já formalizados, mas nenhuma linha de backend ou frontend foi iniciada.

---

## 10. Sistemas e interfaces paralelas por perfil de usuário

### 8.1 Cliente (remoto ou presencial)
- **Cadastro:** self-service na loja online, ou cadastro rápido no balcão presencial
- **Uso:** abertura de OS (remota via postagem ou presencial), acompanhamento de status, compra na loja
- **Suporte:** canal via WhatsApp — já previsto nas notificações automáticas, mas falta um canal de contestação formal (peça errada, prazo estourado, aparelho danificado em trânsito)

### 8.2 Técnico (você hoje, futuro técnico contratado)
- **Cadastro:** criado por você mesmo enquanto for só você; painel de usuário/permissão quando contratar o primeiro técnico (gatilho já definido no plano mestre: fila > 5-7 dias)
- **Uso:** diagnóstico, checklist de qualidade, atualização de status de OS
- **Suporte:** não se aplica — é você/equipe interna

### 8.3 Suporte/Operação interna (mesma lacuna dos outros sistemas)
- Painel para reatribuir OS entre unidades (relevante quando houver mais de uma bancada, seção 1.6), forçar reembolso, gerenciar disputa de aparelho danificado em trânsito
- **Ainda não especificado como RF formal** — mesmo ponto cego já identificado no AM Kaixara, Delivery e AuraVet; vale resolver isso uma vez, de forma reaproveitável entre os quatro sistemas, em vez de reinventar por sistema

---

## 11. Segurança de nível profissional

Aplicação concreta do checklist geral ([distribuicao-licenciamento-seguranca](../04-documentos-transversais/distribuicao-licenciamento-seguranca.md)) a este sistema:

| Categoria | Aplicação específica no AM Consertta |
|---|---|
| Dados sensíveis | Termo de responsabilidade e dado de acesso ao aparelho (senha/padrão informado pelo cliente) — categoria de dado mais sensível deste sistema, exige tratamento equivalente a credencial, nunca texto plano em log |
| Logística/envio | Endereço de entrega e código de rastreio não deveriam ficar visíveis além do necessário para as partes envolvidas — mesmo princípio de minimização já aplicado à geolocalização do entregador no Delivery |
| Conexão entre sistemas (RNFT-S03/S04) | O reaproveitamento do módulo de OS pelo AuraVet precisa seguir o mesmo padrão de escopo mínimo — o AuraVet não deve herdar acesso a dado de cliente da assistência técnica só por reaproveitar o módulo |
| Auditoria externa (RNFT-S06) | Prioridade alta, mesmo nível do AM Kaixara — ambos processam pagamento e têm componente físico/local |

---

## 12. Pendências e decisões em aberto

1. **Política de seguro/responsabilidade em trânsito** (já sinalizada na seção 1.0) — decisão de negócio pendente antes de formalizar o RF de envio.
2. **Provedor de frete/transportadora** — Correios, transportadora privada, ou ambos.
3. **`aura-logistics` como serviço compartilhado ou módulo interno do AM Consertta** — decisão arquitetural sinalizada acima, ainda não fechada.
4. **Painel de suporte técnico interno** — RESOLVIDO: reaproveita o `aura-support`, já formalizado como serviço compartilhado.
5. **Nome definitivo do sistema** — "AM Consertta" é provisório.
