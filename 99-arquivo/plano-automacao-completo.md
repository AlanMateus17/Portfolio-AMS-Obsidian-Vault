---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: novo
---

# Plano de Automação Completo — Padrão de Mercado + O Que Só Você Constrói
### Documento único: o que empresa grande já automatiza (adote, não reinvente), o que só você precisa construir (porque é específico do seu portfólio), seu próprio setup 100% conectado, e as práticas que não têm exceção

---

## 1. O que já é automatizado por ferramenta gratuita — você adota, não constrói

Cada linha tem três colunas: **a ferramenta gratuita que você usa de verdade**, **o nome que você vai ouvir numa empresa grande** (pra reconhecer, mesmo sem usar — a maioria é paga, versão "enterprise" do mesmo problema), e o que a categoria resolve.

| Categoria | Você adota (gratuito) | Nome comum em empresa grande | O que resolve |
|---|---|---|---|
| Formatar código | `dotnet format` | Mesmo padrão, ou Prettier | Estilo consistente sem revisão manual de espaçamento |
| Segredo vazado no commit | Gitleaks | GitGuardian, TruffleHog | Bloqueia senha/chave antes de virar commit |
| Build + teste automático | GitHub Actions (grátis até um limite generoso) | Jenkins, CircleCI, GitLab CI, Azure DevOps | Roda teste a cada push, sem depender de lembrar |
| Dependência vulnerável | Dependabot | Snyk, Mend (ex-WhiteSource) | Abre PR de correção sozinho quando uma lib tem falha conhecida |
| Análise estática de segurança (SAST) | CodeQL (grátis em repositório público, incluso no GitHub) | Checkmarx, Veracode | Aponta padrão perigoso no código antes de rodar |
| Deploy automático (CD) | GitHub Actions + script | Spinnaker, ArgoCD, Harness | Publica versão nova sem passo manual |
| Infraestrutura como código | Terraform (núcleo open source) | Terraform Enterprise, Pulumi | Recria servidor/recurso de nuvem a partir de um arquivo, não de clique |
| Monitoramento / "está no ar?" | Uptime Kuma, Grafana + Prometheus | Datadog, New Relic | Avisa antes do cliente perceber que caiu |
| Log centralizado | Grafana Loki | Splunk, ELK Stack (Elastic, pago em escala) | Busca em log de vários serviços num lugar só |
| Documentação de API | Swagger/OpenAPI | Mesmo — é padrão de mercado, não muda com o tamanho da empresa | Documentação nasce do código, nunca desatualiza |
| Site de documentação | MkDocs + GitHub Pages | Confluence (geralmente pago) | Onde o time lê a documentação do sistema |
| Changelog | semantic-release | Mesmo | Histórico de versão gerado sozinho a partir do commit |
| Teste de carga | k6 (open source) | k6 Cloud, Gatling, JMeter | Simula muito usuário ao mesmo tempo antes do lançamento real |
| Revisão de PR assistida por IA | Claude Code Action, GitHub Copilot | Mesmo, ou ferramenta interna própria da empresa | Primeira leitura automática antes da sua revisão |
| **Gestão de tarefa/sprint** | GitHub Projects (grátis) | **Jira** — de longe o mais citado em empresa grande | Onde o time rastreia tarefa, bug, sprint |
| **Gestão de incidente/plantão** | Uptime Kuma + notificação manual | **PagerDuty**, Opsgenie | Quem é acionado às 3h quando produção cai, com escalonamento automático se ninguém responder |
| **Cofre de segredo em produção** | `dotnet user-secrets` (local) / variável de ambiente | **HashiCorp Vault**, AWS Secrets Manager | Onde a senha do banco de produção realmente fica — nunca em arquivo de configuração versionado |
| **Registro de imagem Docker** | GitHub Container Registry (grátis) | Docker Hub, AWS ECR, Google Artifact Registry | Onde a imagem fica guardada antes do deploy puxar ela |
| **Fila de mensagem/evento** | RabbitMQ (open source, roda em Docker) | **Kafka** — o nome que mais aparece em entrevista técnica | Como sistemas grandes trocam evento sem ficar esperando resposta um do outro — relevante se seus 23 sistemas Aura um dia precisarem conversar de forma assíncrona, não só via API direta |

**A resposta direta pra sua pergunta:** tudo que está na coluna do meio já existe, pronto, gratuito — você não precisa escrever nenhuma dessas ferramentas do zero, só configurar e usar. A coluna da direita é pra você **reconhecer o nome** quando aparecer numa vaga ou numa reunião — não pra você adotar agora, principalmente as pagas.

Detalhe de cada uma, com vantagem/desvantagem/cuidado em produção: [[por-que-automatizar-riscos-e-testes]]. Ordem de quando construir cada uma na sua sequência real: [[ordem-e-sequencia-de-execucao-automacoes]].

---

## 2. O que ninguém construiu pra você — porque é seu, não é genérico

Ferramenta de mercado assume "um time, um repositório". Você tem 23 sistemas + um sistema pessoal de estudo — isso é seu, então a ferramenta é sua também: **`aura-status`**, um único console app C#, sem custo, sem serviço externo.

| Função | O que resolve |
|---|---|
| Painel de status (`aura-status`) | Git de todos os repositórios (`aura-workspace` + `aura-estudos`) numa tela só — sujo/limpo, último commit, se o remoto tem algo que você não puxou ainda |
| Detecção de pasta órfã | Se você criar uma pasta de exercício nova em `aura-estudos` e esquecer de catalogar, ele avisa sozinho — não depende mais só da sua memória |
| Backup | Lê o log real do script de backup, alerta em vermelho se passou de 24h sem rodar |
| Catálogo | Conta quantas seções do `00-catalogo-progresso` ainda estão vazias |
| Dependabot | Lista PRs de segurança pendentes de revisão, via `gh pr list`, sem abrir o navegador |
| `aura-status timer start` / `timer stop` | Cronômetro do Protocolo de Fim de Bloco — resolve o "registre quanto tempo levou de verdade" que hoje é manual |
| `aura-status anki "frente" "verso"` | Manda cartão pro Anki direto do terminal, via AnkiConnect — sem abrir o programa |
| `aura-status zip-gabaritos` | Resolve a pendência real já registrada em `presenca-digital-empresas`: os 9 gabaritos nunca empacotados |

Código completo, pronto pra rodar: `aura-status-Program.cs` (anexo a este documento — copie pra `Program.cs` dentro de uma pasta `aura-status` com um `.csproj` de console). Roda com `dotnet run`.

---

## 3. Seu próprio setup — 100% conectado, o que der pra automatizar

A arquitetura física já existe em [[infraestrutura-fisica-10-anos]] e o setup de software em [[setup-ambiente-trabalho-final]] — o que falta é **ligar os dois**, pra você não precisar rodar nada manualmente:

| O que já existe solto | Como conectar |
|---|---|
| Script de backup (`backup.ps1`) | Agendar no Task Scheduler: `schtasks /create /tn "BackupNoturno" /tr "powershell.exe -File C:\dev\scripts\backup.ps1" /sc daily /st 23:00` |
| `aura-status` | Agendar rodada semanal que **escreve num arquivo de log**, em vez de só mostrar na tela — assim a rotina de segunda-feira já do [[ordem-e-sequencia-de-execucao-automacoes]] vira "abrir um arquivo", não "rodar um comando e lembrar de rodar" |
| Certbot (renovação de SSL) | `schtasks /create /tn "RenovarSSL" /tr "certbot renew --quiet" /sc weekly` |
| Gitleaks/Dependabot | Já são "automáticos por natureza" — disparam sozinhos no commit e no push, nada a agendar |
| Uptime Kuma | Fica rodando continuamente via Docker (`--restart=always`) — uma vez configurado, nunca precisa lembrar de novo |

**O resultado de "100% conectado":** depois de configurado, sua única ação manual vira abrir um arquivo de log (ou rodar `aura-status`) uma vez por semana — todo o resto (backup, scan de segurança, renovação de certificado, monitoramento) roda sozinho, sem depender da sua memória no dia a dia.

---

## 4. Práticas indispensáveis — sem exceção, custe o que custar

Resumo das que não têm meio-termo, detalhadas em [[por-que-automatizar-riscos-e-testes]]:

1. **Nunca** commit sem o hook de Gitleaks ativo — nem "só dessa vez"
2. **Nunca** `terraform apply` sem ler o `plan` antes
3. **Nunca** deploy sem um caminho de rollback já testado, não só teórico
4. **Nunca** confiar em backup que nunca foi restaurado de teste — uma vez por mês, sem exceção
5. **Nunca** automação financeira 100% sem revisão humana, mesmo depois de meses funcionando bem
6. **Nunca** IA aprovando o próprio código que ela mesma escreveu
7. **Sempre** log estruturado desde o primeiro deploy, não como correção depois de um incidente
8. **Sempre** limite de profundidade de query GraphQL configurado (relevante pro AM Taskoro) desde o primeiro deploy

---

## 🔗 Documentos relacionados
- [[automacao-total-ambiente-trabalho]] — cada ferramenta da seção 1, com config completa
- [[por-que-automatizar-riscos-e-testes]] — por que, vantagem, desvantagem, teste de validação de cada uma
- [[ordem-e-sequencia-de-execucao-automacoes]] — quando cada uma entra na sua sequência real de Passos
- [[mapa-automacao-por-contexto-profissional]] — a mesma automação, vista sozinho vs. freelance vs. empregado
- [[infraestrutura-fisica-10-anos]] e [[setup-ambiente-trabalho-final]] — o setup físico e de software que a seção 3 conecta
