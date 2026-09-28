---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-vault — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Décimo serviço compartilhado — nasceu da observação de que AM Rendara, AuraVet, AM Horaria e AM Canteira estavam reimplementando, cada um à sua maneira, o mesmo problema: como proteger e isolar dado de sensibilidade máxima.

---

## 1. Visão do produto

Serviço central de proteção de dado extra-sensível: criptografia de campo, gestão de chave, controle de acesso reforçado e trilha de auditoria imutável. Consumido hoje por AM Rendara (dado bancário), AuraVet (prontuário clínico veterinário), AM Horaria (prontuário psicológico) e AM Canteira (documento contratual e dado pessoal de alto valor).

**Diferencial de inovação:** não é só "criptografar campo" — é reconhecer que cada um desses quatro sistemas tem uma **regra de acesso e retenção legalmente diferente** (LGPD financeiro, sigilo profissional do CFMV, sigilo profissional do CFP, obrigação contratual), e ainda assim compartilhar o mesmo motor técnico. A complexidade de "qual regra se aplica a qual dado" fica centralizada e configurável, em vez de cada sistema decidir sozinho e correr risco de errar de forma diferente.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Criptografia de campo
- API de criptografia/decriptografia de campo sensível, com chave gerenciada centralmente — nunca a mesma chave entre sistemas ou entre tenants
- Rotação periódica de chave, sem exigir reprocessamento manual de dado já protegido

### 2.2 Controle de acesso reforçado por categoria de dado
- Cada categoria de dado (bancário, prontuário clínico, prontuário psicológico, contratual) tem sua própria política de quem pode acessar — reaproveitando as regras já formalizadas individualmente em cada sistema de origem, agora centralizadas aqui
- Suporte ao caso mais restrito já identificado no portfólio: prontuário psicológico, onde nem o administrador do sistema consumidor nem o suporte técnico interno têm acesso ao conteúdo

### 2.3 Trilha de auditoria de acesso
- Todo acesso a dado protegido por este serviço gera evento imutável, integrado ao `aura-historico` — reaproveitamento direto em vez de construir um segundo motor de auditoria

### 2.4 Política de retenção e exclusão por categoria
- Prazo de retenção configurável por categoria (ex: prontuário psicológico 5-20 anos conforme CFP/Lei 13.787/2018, dado bancário conforme LGPD, histórico contratual conforme prazo de garantia)
- Suporte a anonimização/tombstone quando exclusão física conflita com outra obrigação de retenção — mesma tensão já identificada no `aura-historico`, resolvida uma vez aqui e reaproveitada por ele

### 2.5 Procedimento de acesso emergencial (break-glass)
- Mecanismo formal e auditado para acesso excepcional a dado protegido em situação legítima de emergência (ex: ordem judicial), sempre com registro obrigatório e nunca silencioso

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Expor API de criptografia/decriptografia de campo sensível com chave gerenciada centralmente, isolada por sistema/tenant | Elimina a duplicação de lógica de proteção de dado sensível hoje espalhada em 4 sistemas diferentes |
| RF02 | Rotacionar chave de criptografia periodicamente, sem exigir reprocessamento manual | Reduz o risco de uma chave comprometida expor dado histórico indefinidamente |
| RF03 | Aplicar política de controle de acesso configurável por categoria de dado | Permite que cada sistema consumidor herde a regra correta (LGPD, CFMV, CFP, contratual) sem reimplementar |
| RF04 | Registrar todo acesso a dado protegido como evento imutável, via integração com `aura-historico` | Sustenta auditoria e defesa em caso de disputa, sem duplicar motor de histórico |
| RF05 | Aplicar prazo de retenção e regra de exclusão/anonimização por categoria de dado | Cumpre obrigação legal específica de cada categoria sem depender de controle manual por sistema |
| RF06 | Suportar procedimento de acesso emergencial formal, sempre auditado, nunca silencioso | Cobre o caso legítimo de exceção (ordem judicial) sem abrir brecha de acesso não controlado |
| RF07 | Impedir que o `aura-support` acesse conteúdo de dado protegido por categoria restrita (ex: prontuário psicológico), mesmo em diagnóstico de suporte | Formaliza, de forma centralizada, a mesma restrição já identificada individualmente no AM Horaria — agora vale para qualquer sistema que usar este serviço |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Sistema consumidor (AM Rendara, AuraVet, AM Horaria, AM Canteira, e futuros)
- **Uso:** solicita criptografia/decriptografia e validação de acesso via API — máquina a máquina
- Não tem usuário humano direto neste papel

### 4.2 Profissional responsável pelo dado (veterinário, psicólogo, consultor financeiro)
- **Uso:** acessa o próprio dado protegido através do sistema consumidor de origem, nunca diretamente pelo `aura-vault` — este serviço não tem interface própria voltada ao usuário final
- **Observação:** a experiência do profissional não muda — o `aura-vault` é invisível para ele, só o sistema de origem interage diretamente

### 4.3 Você (configuração de política e auditoria)
- **Uso:** define política de retenção por categoria, aciona procedimento de acesso emergencial quando legitimamente necessário, consulta trilha de auditoria via `aura-historico`
- **Lacuna:** mesma recorrente do portfólio — sem painel formal ainda; aqui a urgência é alta, dado o poder de configuração deste serviço sobre dado de máxima sensibilidade

### 4.4 Suporte técnico interno (`aura-support`)
- **Uso:** consulta metadado (existe registro, data, categoria) via `aura-support`, nunca o conteúdo protegido — RF07 formaliza essa restrição como regra deste serviço, não como boa vontade do `aura-support`

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-vault | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | É o serviço com maior concentração de dado sensível de todo o portfólio, por definição | Cumpre obrigação legal na camada onde o risco de exposição é mais grave |
| RNFT-S06 (auditoria externa) | Prioridade máxima, no mesmo nível do `aura-identity` — talvez maior, porque aqui o dano de um vazamento é sobre o conteúdo mais sensível possível, não só acesso | Justifica pentest dedicado antes de qualquer sistema consumidor entrar em produção com dado real |
| Isolamento de chave (próprio) | Nenhuma chave de criptografia é compartilhada entre sistema ou tenant | Compromete um sistema/tenant nunca deve comprometer o dado protegido de outro |
| Não-silêncio de acesso emergencial (próprio, RF06) | Todo acesso via break-glass gera alerta automático, nunca passa despercebido | Impede que a exceção legítima vire porta de abuso não detectado |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-vault |
|---|---|
| Dados | É, junto com o `aura-identity`, o serviço de maior criticidade de segurança do portfólio inteiro — mas por um motivo diferente: o `aura-identity` comprometido dá acesso a tudo, o `aura-vault` comprometido expõe o conteúdo mais sensível de tudo |
| Gestão de chave | Recomendado uso de KMS gerenciado (AWS KMS, Azure Key Vault ou HashiCorp Vault) em vez de gestão de chave própria — reduz superfície de erro de implementação em um dos pontos mais sensíveis de todo o sistema |
| Autenticação administrativa | 2FA obrigatório para qualquer configuração de política ou acesso emergencial, sem exceção — mesmo padrão já definido como obrigatório (não opcional) no `aura-support` |
| Auditoria externa | Prioridade máxima absoluta, empatada com `aura-identity` — os dois juntos formam o núcleo de segurança crítica de todo o portfólio |

---

## 7. Hardware, instalador e distribuição

**Não aplicável no sentido de instalador.** Serviço interno, consumido via API. A única decisão de infraestrutura relevante é o provedor de gestão de chave (KMS/HSM gerenciado — seção 6), que não é hardware físico distribuído, é infraestrutura de nuvem.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Dado o papel crítico de segurança (seção 6), exige redundância de deploy desde o primeiro dia, no mesmo nível do `aura-identity` e do `aura-licensing`.

---

## 9. Modelo de receita — incluindo forma de venda nova

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — reduz risco e duplicação de código de proteção de dado sensível em 4 sistemas |
| **"Proteção de dado sensível como serviço" para terceiros** | Mesmo ângulo já identificado no `aura-historico` e no `aura-analytics` — fintech, healthtech ou qualquer negócio que precise de conformidade robusta de dado sensível sem construir a própria camada de criptografia/auditoria — cobrança por volume de dado protegido ou por assinatura |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Primeira formalização deste serviço — nasceu da análise cruzada dos 4 sistemas que já tinham RNF de proteção de dado sensível definidos individualmente.

---

## 11. Pendências e decisões em aberto

1. **Escolha do provedor de KMS/HSM** (AWS KMS, Azure Key Vault, HashiCorp Vault) — decisão técnica ainda não tomada.
2. **Consolidação formal das políticas de retenção por categoria** — hoje cada sistema de origem (AM Rendara, AuraVet, AM Horaria, AM Canteira) descreve sua própria regra em texto; precisa virar configuração formal única dentro deste serviço, sem perder nenhuma nuance legal específica de cada um.
3. **Painel de configuração de política e auditoria** (seção 4.3) — ainda sem RF formal, prioridade alta dado o poder deste serviço.
4. **Definição precisa do procedimento de break-glass** (RF06) — quem pode acionar, sob qual justificativa documentada, ainda não desenhado com detalhe operacional.
5. **Ordem de migração dos 4 sistemas que hoje descrevem proteção própria** — nenhum ainda tem código escrito, então a migração aqui é mais simples que a do `aura-identity` (que já lida com um sistema em produção), mas ainda exige planejamento de qual sistema integra primeiro.
