---
tags: [ferramenta-pessoal, portfolio-ams, produtizavel]
tipo: ferramenta-pessoal
status: completo
---

# aura-status — Documento de Projeto Final
### O único das 4 ferramentas de automação pessoal com potencial real de virar produto vendável — os outros 3 estão em [aura-queue](aura-queue-documento-projeto-final.md), [aura-secrets](aura-secrets-documento-projeto-final.md) e [aura-oncall](aura-oncall-documento-projeto-final.md), como peça de portfólio, não produto

---

## 1. Visão do produto

Painel de status pessoal, com arquitetura de fonte plugável (`IFonteDeStatus`), que agrega numa tela só sinais de várias ferramentas de automação — git, CI, backup, catálogo de estudo, Dependabot, monitoramento — sem precisar abrir cada uma separadamente.

**Diferencial real, calibrado contra concorrência que existe de verdade:** o **Backstage** (Spotify/CNCF, open source, maduro) já resolve isso pra empresa grande com time de plataforma dedicado — competir ali é terreno perdido. O espaço vazio de verdade é **freelancer e desenvolvedor solo/pequeno time**: gente que gerencia vários projetos de cliente ao mesmo tempo, sem infraestrutura própria de plataforma, e sem paciência (principalmente com TDAH) pra configurar algo pesado. É esse o público, não "empresa em geral".

**Público:** hoje, uso pessoal. Se virar produto: freelancer/dev solo multi-cliente, com developer TDAH como nicho mais fundo dentro desse público.

---

## 2. Funcionalidades completas

| Módulo | Funcionalidade | Origem |
|---|---|---|
| Núcleo de coleta | Roda todas as fontes ativas, exibe resumo | Novo |
| Fonte: Git local | Status de cada repositório (sujo/limpo, último commit, atraso do remoto) | Novo |
| Fonte: CI | Build passou/falhou no último push, por repositório | Novo |
| Fonte: Pull Request | Fila de PR esperando revisão do usuário, entre repositórios/organizações | Novo |
| Fonte: Backup | Última execução, alerta se > 24h | Novo |
| Fonte: Catálogo | Seções vazias no catálogo de progresso | Novo |
| Fonte: Dependabot | PRs de segurança pendentes, via `gh` CLI | Novo |
| Fonte: Uptime Kuma (futura) | Status de sistema em produção | Planejado |
| Fonte: Jira/GitHub corporativo (futura, plugin pago) | Tarefas/PRs atribuídos, só com autorização da empresa | Planejado |
| Higiene de repositório | Branch esquecida, repositório parado, segredo no histórico, licença incompatível, TODO/FIXME agregado | Novo |
| Painel multi-cliente | Projetos ativos, estagnados destacados, prazo com contagem regressiva, resumo "o que eu fiz ontem" | Novo |
| Infraestrutura pessoal | Espaço em disco, domínio expirando, certificado SSL expirando | Novo |
| Comunicação agregada | Menção não lida e issue atribuída, entre repositórios | Novo |
| **Próxima ação sugerida** | Uma linha priorizada no topo — não só lista, uma sugestão do que fazer primeiro | Novo — diferencial mais forte |
| Modo resumo vs. detalhe | 1 linha por fonte por padrão, `--detalhe` abre o resto | Novo |
| Resumo diário opcional | Arquivo local ou e-mail, **desligado por padrão** | Novo |
| Auto-detecção de repositório | Escaneia pasta em busca de `.git`, sem exigir configuração manual | Novo |
| Suporte multi-provedor | GitHub, GitLab, Bitbucket | Novo |
| Cronômetro de bloco de estudo | `timer start`/`timer stop` | Novo |
| Integração Anki | `anki "frente" "verso"`, via AnkiConnect | Novo |
| Empacotamento de material | `zip-gabaritos` | Novo |
| Configuração por perfil | Fontes ativas por fase de carreira (empresa própria/freelance/empregado) | Planejado |

**Fora de escopo, por decisão deliberada — nunca vira isso:** rastreamento de hora trabalhada/faturamento (Toggl/Harvest já resolvem, é categoria própria); qualquer recurso que exija o cliente instalar algo do lado dele (deixa de ser painel pessoal, vira ferramenta de colaboração); chat/comunicação embutida (escopo de outro produto inteiro). A régua: **é status de algo que já existe, ou é ferramenta de ação nova?** Status entra. Ação/colaboração multi-pessoa não — é onde a linha entre "painel enxuto" e "virar Jira sem querer" se desenha.

---

## 3. Requisitos Funcionais (RF)

| ID | Requisito | Para que serve |
|---|---|---|
| RF01 | Coleta de status de cada fonte ativa via interface comum `IFonteDeStatus` | Permite adicionar fonte nova sem alterar o núcleo |
| RF02 | Exibição resumida (1 linha por fonte) por padrão | Reduz carga cognitiva — mostra só o essencial primeiro |
| RF03 | Modo detalhado sob demanda (`--detalhe`) | Detalhe disponível sem forçar leitura constante |
| RF04 | Sinalização por cor (verde/amarelo/vermelho) como informação primária | Permite avaliar status "num olhar" |
| RF05 | Detecção de pasta de exercício sem entrada correspondente no catálogo | Evita esquecimento de atualizar o catálogo manualmente |
| RF06 | Leitura do log de backup, alerta se > 24h sem executar | Alerta automático sem checagem manual |
| RF07 | Listagem de Pull Requests abertos do Dependabot via `gh` CLI | Visibilidade de segurança sem abrir o navegador |
| RF08 | Cronômetro de sessão de estudo, com sugestão de linha pro catálogo | Resolve o "registre o tempo" hoje manual |
| RF09 | Envio de cartão ao Anki via AnkiConnect | Reduz fricção de trocar de ferramenta no meio do estudo |
| RF10 | Empacotamento de pasta em ZIP sob comando | Resolve tarefa pontual de organização |
| RF11 | Configuração de fontes ativas por arquivo, com perfil por fase de carreira | Alterna contexto sem recompilar |
| RF12 | Status de CI (build passou/falhou) do último push, por repositório | Responde "qual projeto está quebrado agora" |
| RF13 | Fila agregada de Pull Requests esperando revisão, entre múltiplos repositórios/organizações | Evita perder PR de vista trabalhando com vários clientes |
| RF14 | Suporte a GitLab e Bitbucket, além de GitHub | Freelancer usa o que o cliente já tem, não escolhe |
| RF15 | Auto-detecção de repositório (escaneia pasta em busca de `.git`) | Funciona quase sem configuração manual |
| RF16 | Resumo diário opcional, arquivo local ou e-mail, desligado por padrão | Atende quem prefere resumo passivo sem violar o princípio de zero notificação por push |
| RF17 | Alerta de branch esquecida (sem merge, antiga) | Evita acúmulo silencioso que vira bagunça |
| RF18 | Alerta de repositório parado (sem commit há muito tempo) | Sinaliza projeto abandonado ou cliente que sumiu |
| RF19 | Scan de segredo no histórico completo do repositório, não só commit novo | Gitleaks retroativo, não só o hook de pre-commit |
| RF20 | Alerta de licença de dependência incompatível com uso comercial | Evita problema jurídico que só aparece tarde |
| RF21 | Agregação de TODO/FIXME de todos os repositórios numa lista só | Elimina depender de lembrar onde ficou anotado |
| RF22 | Painel "projetos ativos agora", com estagnados destacados | Visão de carga de trabalho multi-cliente num relance |
| RF23 | Prazo de entrega por projeto, com contagem regressiva | Visibilidade de prazo sem virar ferramenta de faturamento |
| RF24 | Resumo automático "o que eu fiz ontem", a partir dos commits do dia anterior | Apoio pra daily standup e memória própria |
| RF25 | Alerta de espaço em disco baixo | Evita que backup/ambiente de dev pare sem aviso |
| RF26 | Alerta de domínio expirando em breve | Renovação esquecida é erro clássico evitável |
| RF27 | Alerta visível de certificado SSL prestes a expirar | Sinal complementar ao Certbot, caso a renovação falhe |
| RF28 | Agregação de menção não lida (@usuário) entre repositórios | Evita perder contexto espalhado |
| RF29 | Agregação de issue atribuída ao usuário, entre repositórios | Mesma lógica da fila de PR, aplicada a issue |
| RF30 | "Próxima ação sugerida" — uma linha priorizada no topo do painel | Remove a paralisia de "por onde começo" — nenhuma ferramenta genérica prioriza por você |

---

## 4. Sistemas e interfaces paralelas

| Perfil | Interface | Caminho |
|---|---|---|
| Você, hoje | Terminal | Roda `aura-status`, lê o resumo, decide se precisa de detalhe |
| Freelancer/dev solo multi-cliente (se virar produto) | Terminal + auto-detecção | Instala, aponta a pasta raiz de projetos, funciona quase sem configurar |
| Developer com TDAH (nicho dentro do público acima) | Mesmo terminal | Mesmo desenho, ênfase maior em "próxima ação" pra reduzir paralisia de decisão |
| Provedor de código (GitHub/GitLab/Bitbucket) | API de cada um | Fonte plugável por provedor, mesma interface `IFonteDeStatus` |

---

## 5. Requisitos Não Funcionais (RNF)

| ID | Aplicação no aura-status | Para que serve |
|---|---|---|
| RNFT06 (LGPD) | Dado de ferramenta de terceiro (Jira, GitHub corporativo) fica só local, nunca enviado a servidor externo | Privacidade por padrão — roda 100% local, sem backend próprio coletando nada |
| Desempenho | Coleta de todas as fontes roda em poucos segundos; cada fonte tem timeout próprio | Fonte lenta nunca trava o painel inteiro |
| Segurança de credencial | Token de API de terceiro armazenado criptografado localmente, nunca texto puro | Evita vazamento de credencial de trabalho |
| Compatibilidade multi-provedor | Mesma interface `IFonteDeStatus` implementada por GitHub/GitLab/Bitbucket | Adicionar provedor novo não exige mudar o núcleo |

---

## 6. Segurança de nível profissional

Token de terceiro (Jira, GitHub corporativo, GitLab, Bitbucket) guardado via DPAPI do Windows ou reaproveitando o KeePassXC já no setup — nunca em arquivo de configuração em texto puro, mesmo em uso pessoal.

---

## 7. Hardware, instalador e distribuição

Hoje: executável .NET local, `dotnet run`. Se virar produto: `dotnet publish --self-contained` gera executável único por sistema operacional — instalador via `winget`/Chocolatey, sem infraestrutura própria de distribuição.

---

## 8. Deploy e CI/CD

Nenhum deploy de servidor no modo pessoal — roda 100% local. Se virar produto open-source: CI simples no GitHub (build + teste a cada push), releases via GitHub Releases.

---

## 9. Modelo de receita

| Camada | Conteúdo | Modelo |
|---|---|---|
| **Núcleo (grátis, open source)** | Git local, CI, backup, catálogo, Dependabot, higiene de repositório, auto-detecção, GitHub | Constrói reputação e portfólio — uso próprio já comprovado |
| **Pro (pago, foco freelancer multi-cliente)** | Painel multi-cliente, prazo/contagem regressiva, resumo "o que fiz ontem", GitLab/Bitbucket, menção/issue agregada, "próxima ação sugerida" | Assinatura pequena — é exatamente o conjunto de recursos que só quem gerencia vários clientes ao mesmo tempo sente falta |
| **Plugins avançados** | Fontes prontas de Jira/PagerDuty/GitHub corporativo, já configuradas | Venda avulsa ou incluída no Pro |
| **Sincronização entre dispositivos** | Se o conceito crescer além de uma máquina | Camada opcional, assinatura |

**Honestidade sobre escala:** ainda é produto de nicho, teto de receita bem menor que qualquer sistema de negócio do portfólio principal — mas agora com um recurso (RF30, próxima ação sugerida) que nenhuma ferramenta genérica de mercado tem, o que é a diferença entre "mais um dashboard" e um produto com razão de existir.

---

## 10. Status atual de desenvolvimento

Núcleo com ~170 linhas já escrito (RF01-RF11), funcionando localmente. RF12-RF30 especificados, não implementados ainda.

---

## 11. Pendências e decisões em aberto

1. Decidir se vira open source público desde já ou fica privado até mais maduro
2. Empacotamento como instalador ainda não feito
3. Ordem de implementação dos RF12-RF30 — não definida, deveria seguir o mesmo princípio de "só constrói quando o problema existir de verdade" já aplicado ao resto do portfólio
4. Interface gráfica leve — só considerar se o nicho freelancer validar que terminal é barreira de entrada

---

## 🔗 Documentos relacionados
- [painel-central-arquitetura-todas-fases](../06-execucao-e-desenvolvimento/painel-central-arquitetura-todas-fases.md) — a arquitetura de fonte plugável
- [aura-queue](aura-queue-documento-projeto-final.md), [aura-secrets](aura-secrets-documento-projeto-final.md) e [aura-oncall](aura-oncall-documento-projeto-final.md) — as outras 3 ferramentas, sem o mesmo potencial comercial
- [template-documento-projeto-final](../01-planejamento-geral/template-documento-projeto-final.md) — o padrão que este documento segue, igual aos 23 sistemas de negócio
