---
tags: [servico/compartilhado, portfolio-ams]
tipo: servico-compartilhado
status: completo
---

# aura-identity — Documento de Projeto Final

Segue a estrutura fixa do [[template-documento-projeto-final]]. Primeiro dos 4 serviços compartilhados pendentes, e o de maior prioridade real — fecha a maior evidência de duplicação de código encontrada em toda a auditoria do portfólio.

---

## 1. Visão do produto

Serviço central de identidade e autenticação, consumido por todos os sistemas do portfólio. Hoje, JWT+BCrypt é implementado de forma independente em 7 sistemas diferentes — a mesma lógica de segurança mais sensível de todo o portfólio, escrita 7 vezes, com 7 chances de erro em vez de uma.

**Diferencial de inovação:** não é só "SSO" no sentido corporativo tradicional — é o que viabiliza de verdade a "conta única de cliente" que o `aura-licensing` hoje só resolve pela metade (ele sabe quais produtos um cliente tem, mas cada produto ainda pede login separado). Com o `aura-identity`, um cliente que compra AM Kaixara e AM Rendara faz login uma vez, navega entre os dois sem re-autenticar.

---

## 2. Funcionalidades completas (estado final)

### 2.1 Autenticação central
- Cadastro, login, recuperação de senha — uma única vez, reaproveitado por todo sistema consumidor
- Emissão de JWT com escopo por sistema (um token não dá acesso automático a todos os produtos, mesmo sendo da mesma pessoa)

### 2.2 Single sign-on entre produtos do portfólio
- Cliente autenticado em um sistema não precisa logar de novo ao navegar para outro produto que também possui
- Baseado na conta única de cliente já iniciada no `aura-licensing` (RF06 daquele documento) — este serviço é a peça de autenticação que faltava para aquele conceito funcionar de ponta a ponta

### 2.3 Controle de acesso por papel, delegado ao sistema consumidor
- O `aura-identity` autentica "quem é" a pessoa; cada sistema consumidor continua decidindo "o que ela pode fazer" dentro dele (operador de caixa vs. gerente, por exemplo) — não centraliza permissão de negócio, só identidade

### 2.4 Recuperação e segurança de conta
- Recuperação de senha, autenticação de dois fatores (opcional, configurável por tenant)
- Revogação de sessão (logout remoto de todos os dispositivos, útil em caso de suspeita de comprometimento)

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Centralizar cadastro, login e recuperação de senha para todo o portfólio | Elimina a duplicação de lógica de autenticação hoje presente em 7 sistemas |
| RF02 | Emitir JWT com escopo por sistema consumidor | Impede que comprometer o token de um sistema dê acesso automático a todos os outros que o cliente possui |
| RF03 | Permitir navegação entre produtos do portfólio sem novo login, quando o cliente possui mais de um | É o benefício direto de experiência que justifica a existência do serviço |
| RF04 | Delegar decisão de permissão de papel (operador, gerente, admin) ao sistema consumidor | Mantém a regra de negócio de cada sistema onde ela pertence, sem acoplar `aura-identity` a lógica específica de cada produto |
| RF05 | Suportar autenticação de dois fatores, configurável por tenant | Eleva segurança sem forçar todo cliente a usar, caso ele não queira |
| RF06 | Permitir revogação remota de todas as sessões ativas de uma conta | Resposta rápida em caso de suspeita de conta comprometida |
| RF07 | Integrar com a conta única de cliente do `aura-licensing` | Fecha de ponta a ponta o conceito de "um cliente, múltiplos produtos" que hoje só existe pela metade |

---

## 4. Sistemas e interfaces paralelas por perfil de usuário

### 4.1 Cliente final (qualquer sistema do portfólio)
- **Cadastro:** único, feito uma vez, reaproveitado em qualquer produto que ele venha a comprar depois
- **Uso:** login, recuperação de senha, navegação entre produtos sem re-autenticar
- **Suporte:** canal do sistema de origem, herdando a mesma lógica dos outros serviços compartilhados — o `aura-identity` não tem canal de suporte próprio

### 4.2 Sistema consumidor (todos os outros do portfólio)
- **Uso:** valida token emitido pelo `aura-identity`, aplica sua própria regra de permissão por papel (RF04)
- Não tem usuário humano direto — integração máquina a máquina

### 4.3 Você (administração de conta em caso de disputa/suporte)
- **Uso:** forçar revogação de sessão, resetar acesso de conta comprometida
- **Lacuna:** mesma recorrente do portfólio — sem painel formal ainda; aqui a urgência é maior que a média, porque é literalmente a porta de entrada de todo o portfólio

---

## 5. Requisitos Não Funcionais (RNF) — próprios + transversais

| ID | Aplicação no aura-identity | Para que serve |
|---|---|---|
| Alta disponibilidade (próprio, elevado a crítico) | Indisponibilidade do `aura-identity` bloqueia login em **todo** o portfólio simultaneamente | É o segundo SPOF do portfólio, depois do `aura-licensing` — talvez o primeiro em severidade, porque sem login nenhum sistema é usável, mesmo com módulo pago ativo |
| RNFT-S01/S02 (série de segurança) | Emissão de token e gestão de credencial seguem o mesmo padrão de segurança já formalizado para licenciamento de instalador | Autenticação é a superfície mais sensível de qualquer sistema — não admite padrão inferior ao já estabelecido |
| RNFT06 (LGPD) | Concentra credencial e dado de identidade de todos os clientes de todos os sistemas | Cumpre obrigação legal — é, depois do AM Rendara e do `aura-licensing`, o terceiro maior alvo de valor para um atacante |
| Rate limiting agressivo (próprio) | Login e recuperação de senha devem ter limite de tentativa rígido, mais restritivo que qualquer outro endpoint do portfólio | É o alvo natural de ataque de força bruta e credential stuffing, dado que concentra acesso a tudo |

---

## 6. Segurança de nível profissional

| Categoria | Aplicação específica no aura-identity |
|---|---|
| Dados | Concentra credencial (mesmo com hash/salt) de todos os clientes de todos os sistemas — comprometer este serviço é o pior cenário de segurança possível do portfólio inteiro |
| Rede/API | Cada sistema consumidor autentica com credencial própria pra validar token, nunca compartilhada — mesmo princípio já aplicado ao `aura-licensing` |
| Isolamento de escopo | Token de um sistema nunca deve ser aceito por outro sistema sem validação explícita de escopo (RF02) |
| Auditoria externa (RNFT-S06) | **Prioridade máxima absoluta do portfólio inteiro** — acima até do AM Rendara e do `aura-licensing`, porque comprometer o `aura-identity` compromete o acesso a todos os outros |

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno, consumido via API por todo o portfólio, sem instalador nem distribuição direta.

---

## 8. Deploy e CI/CD

Mesmo padrão do restante — Dockerfile multi-stage, `docker-compose.yml`, pipeline GitHub Actions. Dado o papel de SPOF crítico (seção 5), exige redundância de deploy desde o primeiro dia — mais ainda que o `aura-licensing`, porque uma falha aqui não degrada só cobrança, impede login em tudo.

---

## 9. Modelo de receita — incluindo forma de venda nova

| Fonte | Modelo |
|---|---|
| Uso interno (padrão) | Não gera receita direta — é infraestrutura de segurança e experiência para todo o portfólio |
| **Licenciamento white-label do serviço de identidade** | Mesmo ângulo já identificado para o `aura-licensing` — outras empresas de software que precisam de SSO entre produtos próprios e não querem construir do zero |

---

## 10. Status atual de desenvolvimento

**Nenhum código escrito ainda.** Este é o primeiro documento formal deste serviço — antes só existia como conceito mencionado dentro do `aura-licensing` e do documento de Distribuição/Segurança.

---

## 11. Pendências e decisões em aberto

1. **Redundância de deploy** — mesma decisão do `aura-licensing`, aqui com urgência ainda maior.
2. **Política de dois fatores** (RF05) — obrigatório por padrão ou opt-in por tenant, ainda não decidido.
3. **Painel de administração de conta** (seção 4.3) — ainda sem RF formal, prioridade alta dado o papel central do serviço.
4. **Ordem de migração dos 7 sistemas que hoje implementam autenticação própria** — o AM Kaixara já está em código (Sprint 3-4); migrar um sistema já em desenvolvimento para um serviço central externo é decisão que precisa de plano próprio, não é só "trocar depois".
