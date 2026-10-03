---
tags: [planejamento, seguranca, ferramentas, portfolio-ams]
tipo: planejamento
status: novo
---

# Segurança e Ferramentas — Todas as Frentes
### O que falta pra "todas as empresas seguras" de verdade: técnico e jurídico/financeiro, juntos — pesquisado em 29/08/2026

> Este documento cobre o que **não** estava em nenhum outro lugar do vault: segurança técnica do dia a dia (Git, Git LFS, Claude Code, segredo vazado) e proteção jurídica/financeira (seguro, LGPD) — aplicados às suas frentes reais, não em abstrato. Onde já existe cobertura em outro documento, eu só linko, não repito.

---

## 1. Segurança técnica transversal — vale pra toda frente que envolve código

### 1.1 Git — o que você já vai estudar (Passo 2), mais o que falta

Git básico já está no [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md) (Passo 2). O que falta é **higiene de segredo**, que nenhum curso de Git básico cobre:

- **Gitleaks** — scanner de segredo (chave de API, senha, token) de código aberto, escrito em Go, roda como binário único. Detecta 150+ tipos de segredo (AWS, GitHub, Slack, banco de dados) via regex + análise de entropia.
- **Onde instalar:** (1) hook de pre-commit local — roda em milissegundos, bloqueia segredo antes de virar commit; (2) CI (GitHub Actions/Gitea Actions) — pega o que o hook local não pegou; (3) GitHub push protection — trava no servidor, não depende de disciplina individual.
- **Regra que você precisa saber de cor:** `git rm` ou um commit novo removendo o arquivo **não apaga o segredo do histórico** — o commit antigo continua existindo e acessível por hash. Remoção de verdade exige `git-filter-repo` reescrevendo o histórico + todo colaborador reclonando.
- **Se um segredo vazar:** revogar a credencial na origem (AWS IAM, GitHub, Stripe etc.) **antes** de qualquer limpeza de Git — prioridade máxima, não espera.

### 1.2 Git LFS — quando você vai precisar de verdade

Git normal versiona texto bem, mas fica pesado com arquivo binário grande (vídeo, imagem em alta resolução, PDF grande, asset de design). **Git LFS** (Large File Storage) troca o arquivo binário por um ponteiro leve no repositório, guardando o conteúdo real num storage separado.

**Onde isso te afeta de verdade:**
- **Momentos/Cupido** — fotos/mídia de usuário, se algum dia entrar teste local com asset real no repo (produção já usa Cloudflare R2, então isso é só pra desenvolvimento/design, não pra dado de cliente)
- **AM Saberia** — as 180 apostilas em PDF, se ficarem versionadas no mesmo repo do código do sistema (considere um repo separado só de conteúdo, ou LFS, pra não inchar o clone de quem só quer o código)
- **Infoprodutos (Camada 11 da [infraestrutura-fisica-10-anos](infraestrutura-fisica-10-anos.md))** — vídeo bruto de curso gravado NUNCA deveria ir pro Git, nem com LFS — isso é trabalho pro NAS, não pro controle de versão

**Regra prática:** se o arquivo muda pouco e é grande (PDF final, vídeo), ele não pertence ao Git — nem com LFS. LFS serve pra binário que muda com frequência e precisa de histórico de versão (ex: arquivo de design em edição ativa), não pra armazenamento de mídia finalizada.

### 1.3 Claude Code — o que é, de verdade, e o risco específico que ele traz

Claude Code é a ferramenta agente de codificação da Anthropic — roda no terminal, IDE, app desktop ou navegador, lê seu código, edita arquivo, roda comando, integra com Git (stage, commit, branch, PR) e com ferramenta externa via MCP. Requisito: Node.js 18+, conta Claude.ai (Pro/Max) ou Anthropic Console.

**O risco de segurança específico, achado na pesquisa:** relatório da GitGuardian (março/2026) encontrou que **commits assistidos por IA vazam segredo a uma taxa aproximadamente 2x maior que o baseline humano** — a ferramenta gera configuração/integração rápido demais, e às vezes um token real acaba colado ou reutilizado sem revisão cuidadosa. **Conclusão prática pra você:** o Gitleaks da seção 1.1 não é opcional se for usar Claude Code no dia a dia — é exatamente o tipo de rede de segurança que compensa esse ganho de velocidade.

- Fonte: [Overview oficial](https://code.claude.com/docs/en/overview) · [Docs Claude Code](https://docs.claude.com/en/docs/claude-code/overview)

### 1.4 Onde isso entra no seu setup

Adicionar ao `setup-ambiente-trabalho-final.md` (ver seção 🔗 abaixo, já linkado de volta): Gitleaks (binário + hook de pre-commit) e Git LFS (`git lfs install`) — ambos leves, cabem na Camada 1 do setup atual, sem esperar nenhuma fase futura.

---

## 2. Proteção jurídica/financeira transversal

### 2.1 Seguro de Responsabilidade Civil Profissional (RC Profissional / E&O)

Protege contra reclamação de cliente por erro, falha ou atraso na prestação de serviço de TI (bug que causa prejuízo, sistema fora do ar, conselho técnico errado). Cobre despesa de defesa, acordo e indenização.

**Por que isso importa especialmente pra você:** já está registrado como pendência real em dois dos seus próprios documentos — `projeta-documento-projeto-final` (Fase 0 jurídica) e `consertta-sistema-assistencia-tecnica` (seguro de transporte/responsabilidade). Isso não é exagero de cautela: **contrato corporativo às vezes exige comprovação de cobertura como condição pra fechar parceria** — ter o seguro é vantagem comercial, não só proteção.

### 2.2 Seguro Cibernético (RC Cibernética)

Cobertura separada, específica pra: vazamento de dado, ataque hacker, multa por descumprimento de LGPD, custo de recuperação de dado e de imagem. Muitas seguradoras já vendem os dois combinados (RC Profissional + RC Cibernética + RC de Produto) — vale pedir cotação combinada, não duas apólices separadas.

**Custo:** contratação simplificada — normalmente basta informar faturamento anual estimado e escolher o valor de cobertura (R$100 mil a R$500 mil é faixa comum pra pequena empresa de TI).

### 2.3 LGPD — o que mudou e por que não dá pra adiar

**Achado mais importante da pesquisa:** em fevereiro/2026, a ANPD virou agência reguladora autônoma (Lei nº 15.352/2026), com mais poder de fiscalização. **A primeira multa da história da ANPD foi contra uma microempresa** (Telekall Infoservice, R$14.400, por falta de encarregado de dados e não colaborar com fiscalização) — o mito de "só empresa grande é fiscalizada" já foi derrubado na prática. Multas podem chegar a R$50 mil ou 2% do faturamento por infração.

**O que se aplica a você, mesmo pequeno:**
- **Dispensa de DPO formal** pra ME/EPP/MEI (Resolução ANPD nº 2/2022) — mas isso **não dispensa** proteger o dado, evitar coleta excessiva, nem o dever de notificar incidente
- Toda frente que coleta CPF, telefone, e-mail, geolocalização, dado de saúde (AuraVet), dado financeiro (AM Rendara) está sujeita — "empresa pequena" não é isenção
- Base legal explícita pra cada coleta (consentimento é a mais comum pra pequena empresa)
- Banner de cookie: não pode disparar cookie de terceiro (Analytics, Meta Pixel) antes do aceite; botão "recusar" com o mesmo destaque visual do "aceitar"

**Isso já está parcialmente coberto tecnicamente** pelo `RNFT06 (LGPD)` presente em quase todo sistema do portfólio (ver qualquer `documento-projeto-final`, seção 5) — o que faltava era o lado **legal/operacional** (política de privacidade real, canal de atendimento ao titular, o risco de multa), que é o que esta seção cobre.

---

## 3. Ferramentas específicas por frente de renda

*(numeração seguindo [plano-mestre-frentes-alan](plano-mestre-frentes-alan.md))*

### Frente 2 — Assistência Técnica
Já mapeada em `plano-mestre-frentes-alan` (toolkit por nível, software por marca) — nada novo aqui além da seção 2 acima (RC Profissional cobre erro de reparo que danifica aparelho do cliente).

### Frente 3 — Ecossistema Aura (SaaS)
Coberto pela seção 1 inteira (Git, Git LFS, Gitleaks, Claude Code) + toda a trilha técnica já no [00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md). Nada a acrescentar em ferramenta nova.

### Frente 4 — Educação (apostilas, cursos, mentoria)

**Plataforma de venda — pesquisa feita agora:**

| Plataforma | Taxa padrão | Ponto forte | Ponto fraco |
|---|---|---|---|
| **Hotmart** | 9,9% + R$1,00/venda (ou 5,99%+R$1 no plano Club, R$99/mês) | Rede de afiliados mais robusta do mercado, alcance internacional | Taxa de player de vídeo nativo (R$2,49/venda) se hospedar aula lá |
| **Kiwify** | 8,99% + R$2,49/venda (padrão) ou taxa zero no plano mensal fixo | Checkout mais enxuto, hospedagem de vídeo gratuita na área de membros, Pix com liberação mais rápida | Programa de afiliados menor, convite obrigatório (não é aberto como o da Hotmart) |

**Recomendação pro seu caso:** como você não depende de afiliado pra começar (público já vem dos seus alunos/redes), e o ticket das apostilas tende a ser baixo-médio, a **Kiwify** tende a compensar mais no início — sem a taxa de player de vídeo, hospedagem de vídeo já inclusa. Reavalie pra Hotmart se decidir escalar via rede de afiliados depois.

Ambas aceitam Pix (liberação em ~2 dias, a mais vantajosa pra você e pro aluno) e nenhuma emite nota fiscal automática — isso continua sendo sua responsabilidade via o CNPJ de [estrutura-juridica-amtech](estrutura-juridica-amtech.md).

### Frente 5 — Freelance Web Dev
Já mapeado (WooCommerce + Hostinger + Mercado Pago) — sem ferramenta nova identificada nesta pesquisa além da seção 1 (Git/Gitleaks vale igual pra projeto de cliente).

### Frente 6 — Dropshipping/Afiliados
Sem ferramenta técnica nova além do que `plano-mestre-frentes-alan` já lista (Mercado Livre, Amazon, Shopee, Amazon Associados, ML Afiliados). Segurança aqui é mais sobre a seção 2 (contrato/responsabilidade) do que técnica.

---

## 🔗 Documentos relacionados
- [setup-ambiente-trabalho-final](../06-execucao-e-desenvolvimento/setup-ambiente-trabalho-final.md) — onde Gitleaks e Git LFS entram no checklist de instalação
- [estrutura-juridica-amtech](estrutura-juridica-amtech.md) — o CNPJ que contrata o seguro desta seção 2
- [plano-mestre-frentes-alan](plano-mestre-frentes-alan.md) — as 6 frentes que esta pesquisa cobre uma a uma
- [distribuicao-licenciamento-seguranca](../04-documentos-transversais/distribuicao-licenciamento-seguranca.md) — segurança do *produto* vendido (RNFT-S), diferente da segurança *operacional da empresa* coberta aqui
