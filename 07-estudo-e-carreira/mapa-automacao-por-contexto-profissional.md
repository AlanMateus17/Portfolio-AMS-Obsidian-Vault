---
tags: [execucao, automacao, portfolio-ams, carreira]
tipo: planejamento
status: novo
---

# Mapa de Automação por Contexto Profissional
### O quarto documento do conjunto — os três anteriores assumiam que você decide tudo (seu próprio portfólio); este cobre os outros dois contextos onde você não decide, e precisa saber operar dentro do que já existe

> A diferença central: em `ordem-e-sequencia-de-execucao-automacoes`, você é quem constrói cada automação do zero, na ordem que quiser. **Aqui não** — em freelance e, principalmente, como empregado numa empresa grande, a maior parte da automação **já existe antes de você chegar**. A habilidade que importa muda de "eu sei construir" pra "eu sei entender, seguir corretamente, e sugerir melhoria sem quebrar o que já funciona".

---

## O mapa completo — mesma categoria, três realidades diferentes

| Categoria | 🏠 Sozinho / empresa própria | 💼 Freelance pra cliente | 🏢 Empregado em empresa grande |
|---|---|---|---|
| **Commit-time** (formatação, Gitleaks, pre-commit) | Você decide e configura tudo do zero | Configurar no projeto do cliente é diferencial profissional real — poucos freelancers entregam isso | Quase certo que já existe, configurado pelo time. **Seu trabalho é nunca usar `--no-verify` pra pular** — e sugerir melhoria só depois de entender por que está do jeito que está |
| **CI** (build + teste automático) | Você monta do zero (GitHub Actions) | Propor mesmo em projeto pequeno eleva a percepção de profissionalismo | Já existe (Jenkins, GitHub Actions, Azure DevOps, GitLab CI) — seu trabalho no início é **entender o pipeline existente**, não recriar. Contribuir/otimizar vem com senioridade, não no primeiro mês |
| **CD** (deploy automático) | Você decide a estratégia inteira | Raramente você tem acesso à produção do cliente — normalmente entrega código, quem faz deploy é o time dele | Processo formal já definido (staging, gate de aprovação, checklist) — **seguir o processo é o trabalho**, decidir a estratégia não é papel de quem está chegando |
| **Infraestrutura como código** | Terraform/Ansible que você mesmo escreve | Raro fazer parte do escopo, a não ser que contratado especificamente pra isso | Time de Platform Engineering/DevOps já mantém — você aprende a **ler** antes de escrever; PR nessa área, no início, é revisado com mais rigor que PR de aplicação |
| **Observabilidade** (log, alerta, monitoramento) | Você monta Uptime Kuma/log estruturado do zero | Só entra no escopo se a manutenção pós-entrega for contratada | Ferramenta corporativa já existe (Datadog, New Relic, Grafana) — aprender a **interpretar dashboard e criar alerta novo** é a parte que cabe a você, montar a infraestrutura de observabilidade não |
| **Segurança contínua** (SAST/DAST, scan de dependência) | Você ativa Dependabot/scanner por conta própria | Ativar Dependabot no repositório do cliente é rápido e agrega valor real à entrega | Time de segurança define a política — o seu trabalho é **corrigir o que o scanner aponta no seu código**, não escolher a ferramenta |
| **Documentação automática** (Swagger, MkDocs) | Você escolhe e configura | Swagger/OpenAPI em entrega de API já é praticamente padrão esperado, mesmo freelance | Já é convenção do time — seguir o padrão existente, não introduzir um novo sem alinhar antes |
| **Gestão de processo** (CODEOWNERS, fila de merge) | Opcional — mais clareza pessoal que necessidade | Raramente aplicável, você é o único dev do projeto | Estrutura já definida — aprender a **trabalhar dentro dela** (revisar PR de colega, respeitar dono de área) é uma habilidade em si, avaliada em performance review |
| **Ambiente de dev automatizado** (Dev Container, script de setup) | Você cria do zero | Acelera se o projeto crescer e outro dev entrar depois de você | Geralmente já existe — seu primeiro dia de trabalho **usa** isso, não cria. Se não existir, propor é sinal de senioridade, mas só depois de estabelecido no time |
| **Notificação automática** (Discord/Slack/Teams) | Você configura webhook próprio | Opcional, mais organização pessoal do projeto | Já integrado ao Slack/Teams corporativo, com canal e convenção próprios do time |
| **Backup e disaster recovery** | Responsabilidade 100% sua | Normalmente responsabilidade do ambiente do cliente — mas seu código/trabalho local continua sendo sua responsabilidade | Time de infraestrutura cuida disso — sua responsabilidade vira **seguir a política** (nunca só local, sempre commitado, nunca dado sensível fora do lugar certo) |
| **Teste de carga** | Você decide se e quando vale a pena | Raro estar no escopo, a não ser pedido explícito | Pode existir time de QA/performance dedicado, ou ser parte de um processo formal antes de lançamento grande — raramente você monta isso sozinho no início |
| **IA no pipeline / Claude Code** | Você decide livremente | Pode acelerar seu trabalho, **mas cuidado real:** nunca colar código do cliente numa ferramenta de IA sem autorização explícita dele — é dado proprietário de terceiro | **Verificar a política de uso de IA da empresa antes de usar qualquer coisa** — muita empresa grande tem regra específica sobre ferramenta de IA e código proprietário; usar sem verificar pode ser falta grave, não só descuido técnico |

---

## O que isso muda na prática, resumido numa frase por contexto

- **Sozinho/empresa própria:** a pergunta certa é "como eu construo isso". Os três documentos anteriores (`automacao-total-ambiente-trabalho`, `por-que-automatizar-riscos-e-testes`, `ordem-e-sequencia-de-execucao-automacoes`) já respondem essa pergunta por completo.
- **Freelance:** a pergunta certa é "o que eu ofereço que me diferencia, dentro do que cabe no escopo contratado". Automação de commit-time e CI/segurança básica são as que mais valem a pena propor, mesmo em projeto pequeno — custam pouco tempo seu e mostram profissionalismo real.
- **Empregado em empresa grande:** a pergunta certa é "o que eu preciso entender e seguir corretamente primeiro, antes de sugerir qualquer mudança". A maior parte da automação já existe — a habilidade que te diferencia não é saber construir do zero (embora ajude), é saber **operar dentro de um sistema já em produção sem quebrar nada**, e ganhar confiança suficiente pra sugerir melhoria só depois de entender por que está do jeito que está.

---

## Onde isso se conecta com seu plano de carreira

Isso é exatamente o gap que `perfil-senior-completo-auditoria` já identificou como "genuinamente novo" — infraestrutura além do que o plano cobre, processo e colaboração. Este mapa é a resposta prática: as três colunas da tabela acima são, na prática, os três estágios que você vai atravessar — hoje construindo sozinho, e um dia entrando numa empresa grande onde a coluna certa a estudar não é mais "sozinho", é "empregado".

---

## 🔗 Documentos relacionados
- [[automacao-total-ambiente-trabalho]] — o "como" de cada categoria, pro contexto onde você constrói do zero
- [[por-que-automatizar-riscos-e-testes]] — o "por quê" e os riscos, válidos nos três contextos
- [[ordem-e-sequencia-de-execucao-automacoes]] — a ordem de construção específica do seu próprio portfólio
- [[perfil-senior-completo-auditoria]] — onde este mapa se conecta com o que falta pro perfil sênior
