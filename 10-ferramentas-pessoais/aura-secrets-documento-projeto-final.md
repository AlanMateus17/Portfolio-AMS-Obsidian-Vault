---
tags: [ferramenta-pessoal, portfolio-ams, aprendizado]
tipo: ferramenta-pessoal
status: completo
---

# aura-secrets — Documento de Projeto Final
### Cofre de segredo mínimo — uso 100% interno, sem modelo de receita por decisão de segurança, não só de mercado (razão explicada na seção 9)

> **Não confundir com [aura-vault](../03-servicos-compartilhados/aura-vault-documento-projeto-final.md)**, o 10º serviço compartilhado já existente no portfólio — são coisas diferentes, apesar do nome parecido com a primeira versão deste documento (renomeado de `aura-vault-simples` justamente para evitar essa confusão). `aura-vault` protege **dado sensível de cliente** (prontuário, dado bancário, contrato), com regra legal de retenção e acesso. `aura-secrets` guarda **credencial de infraestrutura** (senha de banco, chave de API externa) que os próprios sistemas usam pra funcionar — problema diferente, nunca o mesmo serviço.

---

## 1. Visão do produto

API pequena e autenticada que guarda segredo criptografado e devolve só pra quem tem permissão explícita. Ensina por que segredo não deveria nunca ficar em arquivo de configuração, e como um serviço central de segredo funciona — sem a política granular de acesso e rotação automática distribuída do HashiCorp Vault real.

**Público:** exclusivamente interno — os próprios sistemas Aura em produção, nunca exposto como produto externo.

---

## 2. Funcionalidades completas

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Armazenamento de segredo | Guarda segredo criptografado, associado a um sistema/serviço | Novo |
| Devolução de segredo | Devolve o valor mediante requisição autenticada | Novo |
| Registro de acesso | Toda leitura de segredo fica registrada (quem, quando) | Novo |

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Armazenar segredo criptografado no banco, associado a um sistema/serviço | Nunca guarda segredo em texto puro |
| RF02 | Devolver segredo mediante requisição autenticada | Só quem tem permissão explícita recebe o valor |
| RF03 | Registrar toda leitura de segredo (auditoria mínima) | Permite saber quem acessou o quê, e quando |

---

## 4. Sistemas e interfaces paralelas

| Sistema Aura | Papel |
|---|---|
| Qualquer sistema Aura em produção | Consome segredo (string de conexão de banco, chave de API externa) via chamada autenticada, no lugar de variável de ambiente solta |

Sem interface de usuário final — infraestrutura interna, consumida só por código.

---

## 5. Requisitos Não Funcionais (RNF)

| ID | Aplicação no aura-secrets | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Nenhum dado pessoal de cliente é guardado aqui — só segredo de infraestrutura (credencial, chave) | Escopo restrito reduz superfície de risco |
| Criptografia | Segredo nunca gravado em texto puro no banco | Mesmo com acesso direto ao banco, o segredo não fica exposto |
| Auditoria | Toda leitura registrada, nunca silenciosa | Rastreabilidade de quem acessou cada segredo |

---

## 6. Segurança de nível profissional

Este é o ponto mais sensível dos 4 documentos deste conjunto. Segredo armazenado com criptografia forte (nunca reversível sem a chave mestra, guardada fora do banco). Acesso só via requisição autenticada, nunca aberto. **Nunca exposto como produto externo** — um cofre de segredo malfeito é pior que nenhum cofre; o risco reputacional de vender "segurança" sem o rigor de anos que o Vault real tem não compensa, mesmo que houvesse demanda de mercado.

---

## 7. Hardware, instalador e distribuição

**Não aplicável.** Serviço interno do portfólio Aura, nunca distribuído ou instalado por terceiros.

---

## 8. Deploy e CI/CD

Deploy junto da infraestrutura de produção do primeiro sistema Aura que for pro ar (Passo 10) — não tem pipeline separado.

---

## 9. Modelo de receita

**Nenhum, por decisão deliberada de segurança, não só de mercado.** Mesmo que houvesse demanda, vender gerenciamento de segredo malfeito é o tipo de risco que pode custar reputação profissional inteira se der errado — o oposto do que [seguranca-e-ferramentas-todas-as-frentes](../01-planejamento-geral/seguranca-e-ferramentas-todas-as-frentes.md) inteiro defende. Quem precisa de cofre de segredo de verdade já usa HashiCorp Vault (núcleo gratuito) ou AWS Secrets Manager.

---

## 10. Status atual de desenvolvimento

Não iniciado — só entra no Passo 10 (primeira produção real), quando existe segredo de produção de verdade precisando de um lugar melhor que variável de ambiente solta.

---

## 11. Pendências e decisões em aberto

1. Definir onde a chave mestra de criptografia fica guardada (fora do banco, obrigatoriamente) — decisão técnica a fechar antes de qualquer linha de código
2. Nenhuma outra pendência — escopo deliberadamente mínimo, sem política granular

---

## 🔗 Documentos relacionados
- [painel-central-arquitetura-todas-fases](../06-execucao-e-desenvolvimento/painel-central-arquitetura-todas-fases.md) — a arquitetura de fonte plugável que este documento complementa
- [aura-status-documento-projeto-final](aura-status-documento-projeto-final.md) — a única das 4 ferramentas com modelo de receita real
- [veredito-clonar-ou-nao-ferramenta-paga](../06-execucao-e-desenvolvimento/veredito-clonar-ou-nao-ferramenta-paga.md) — por que não clonar o Vault real
- [seguranca-e-ferramentas-todas-as-frentes](../01-planejamento-geral/seguranca-e-ferramentas-todas-as-frentes.md) — a base de segurança que este serviço reforça
- [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md) — o padrão que este documento segue, igual aos 23 sistemas de negócio
