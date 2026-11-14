---
tags: [glossario, ponto-de-entrada, portfolio-ams]
tipo: referencia
status: ativo
atualizado: 2026-10-26
---

# 📖 Glossário — Cada Palavra do Plano, Explicada do Zero

> Em ordem alfabética dentro de cada grupo. Se uma palavra do vault não estiver aqui, ela entra na próxima revisão.

## Programação e linguagens

| Termo | O que é |
|---|---|
| **Algoritmo** | Uma receita passo a passo para resolver um problema |
| **Big-O** | Jeito de dizer quanto um algoritmo fica mais lento quando os dados crescem |
| **C#** | Linguagem da Microsoft; era a base do portfólio, hoje é **carta de reserva** (vaga corporativa ou agente fiscal). O núcleo agora é TypeScript + Python + SQL |
| **C / C++** | Linguagens antigas e próximas da máquina; ensinam como a memória funciona (École 42) |
| **Clojure** | Era pensada para o `aura-historico`; **cortada** na nova realidade (sistema arquivado) |
| **Estrutura de dados** | Jeito de guardar dados na memória (lista, fila, árvore, tabela de busca) |
| **JavaScript** | A linguagem que roda no navegador |
| **TypeScript** | JavaScript com "tipos": avisa o erro antes de rodar |
| **Python** | Linguagem simples, padrão para dados e IA; roda em paralelo no seu plano |
| **SQL** | A linguagem para perguntar coisas ao banco de dados |
| **Bash / PowerShell** | Linguagens de comandos do terminal (Linux / Windows) |
| **.NET** | A plataforma onde o C# roda (hoje só na carta de reserva) |
| **Runtime / GC** | O "motor" que executa o programa / a parte que limpa a memória sozinha |

## Construção de sistemas

| Termo | O que é |
|---|---|
| **Backend** | A parte do sistema que fica no servidor: regras, banco, segurança |
| **Frontend** | A parte que a pessoa vê e clica (telas) |
| **Fullstack** | Quem faz backend e frontend |
| **API** | A "porta" pela qual o frontend (ou outro sistema) conversa com o backend |
| **REST** | O jeito mais comum de desenhar uma API, usando endereços e verbos (GET, POST…) |
| **GraphQL** | Outro jeito de API, em que quem pede escolhe os campos (opcional; o AM Taskoro foi arquivado) |
| **Next.js / NestJS** | Jeitos de criar o backend/API em TypeScript (o principal). ASP.NET Core faz o mesmo no .NET, hoje só na reserva |
| **HTML / CSS** | Estrutura da página / aparência da página |
| **React** | Biblioteca para montar telas em pedaços reutilizáveis (componentes) |
| **Next.js** | Ferramenta em cima do React que cuida de páginas, rotas e desempenho |
| **Tailwind** | Jeito rápido de estilizar com classes prontas |
| **Componente** | Um pedaço de tela reutilizável (botão, tabela, formulário) |
| **CRUD** | Criar, ler, atualizar e apagar registros — o básico de quase todo sistema |
| **Autenticação / Autorização** | Provar quem você é (login) / o que você pode fazer |
| **JWT** | Um "crachá" digital que o sistema dá depois do login |
| **OAuth / OIDC** | Padrões para login seguro, como "entrar com Google" |
| **Multi-tenant (`tenant_id`)** | Um sistema que atende várias empresas sem misturar os dados delas |
| **PWA** | Site que funciona como aplicativo no celular, até sem internet |
| **Agente local** | Programa que roda no computador do cliente (ex.: o módulo Caixa do AM Gestão, que imprime e funciona offline) |

## Dados

| Termo | O que é |
|---|---|
| **Banco de dados** | Onde o sistema guarda as informações |
| **PostgreSQL** | O banco de dados principal da sua stack |
| **SQLite** | Banco pequeno que mora num arquivo; usado no caixa offline |
| **Redis** | Memória super-rápida para guardar coisas temporárias (cache) e filas |
| **PostGIS** | Extensão do PostgreSQL para mapas e localização (módulo Pedidos do AM Gestão) |
| **Índice** | O "índice remissivo" do banco: deixa a busca rápida |
| **Transação** | Um conjunto de operações que acontece inteiro ou não acontece |
| **Prisma / Drizzle** | Ferramentas do TypeScript para falar com o banco sem escrever todo o SQL na mão (equivalem ao EF Core do .NET) |
| **Migração** | Mudança na estrutura do banco, feita de forma controlada |
| **Cache** | Guardar um resultado para não calcular de novo |

## Arquitetura

| Termo | O que é |
|---|---|
| **Arquitetura** | A organização geral do sistema: quem fala com quem e por quê |
| **Clean Architecture** | Separar regras de negócio das ferramentas (banco, telas) para trocar uma sem quebrar a outra |
| **DDD** | Desenhar o código com as palavras e regras do negócio real |
| **SOLID** | Cinco princípios para código fácil de mudar |
| **Design pattern** | Solução conhecida para um problema comum de código |
| **Microsserviços / monolito modular** | Vários sistemas pequenos / um sistema só, bem dividido por dentro |
| **Mensageria / fila** | Sistemas mandando recados uns para os outros sem esperar resposta na hora |
| **Idempotência** | Fazer a mesma operação duas vezes dá o mesmo resultado (cobrar duas vezes não cobra em dobro) |
| **Ledger / partidas dobradas** | Livro-caixa em que todo valor sai de um lugar e entra em outro; o saldo sempre fecha |
| **ADR** | Registro escrito de uma decisão técnica e do motivo |
| **AM Gestão** | O seu produto único, com módulos (Caixa, Pedidos, Financeiro, Loja). O antigo ecossistema Aura de 23 sistemas foi arquivado em 99-arquivo |

## Qualidade, entrega e produção

| Termo | O que é |
|---|---|
| **Teste unitário / integração / E2E** | Testa um pedaço / testa pedaços juntos / testa o sistema inteiro como um usuário |
| **TDD** | Escrever o teste antes do código |
| **Vitest, Playwright, pytest** | Ferramentas de teste (TypeScript, navegador, Python) |
| **Git / GitHub** | Histórico de versões do código / site onde ele fica guardado |
| **Commit / push** | Salvar uma versão / mandar para o GitHub |
| **Docker / contêiner** | "Caixa" que leva o sistema com tudo o que ele precisa para rodar igual em qualquer lugar |
| **CI/CD** | Testes e publicação automáticos a cada mudança |
| **GitHub Actions** | A ferramenta de CI/CD do GitHub |
| **Deploy** | Colocar o sistema no ar |
| **Nuvem (Azure, AWS, Vercel, VPS)** | Computadores alugados na internet onde os sistemas rodam |
| **Terraform** | Descrever a infraestrutura em arquivos, para criar tudo de novo com um comando |
| **Kubernetes** | Sistema que gerencia muitos contêineres em muitos servidores |
| **Observabilidade (logs, métricas, traces)** | Enxergar o que o sistema está fazendo em produção |
| **OpenTelemetry** | Padrão para coletar logs, métricas e traces |
| **SLO** | A meta de quanto o sistema precisa funcionar (ex.: 99,9% do tempo) |
| **Performance / profiling** | Velocidade do sistema / medir onde ele está lento |

## Segurança

| Termo | O que é |
|---|---|
| **OWASP Top 10** | Lista das 10 falhas de segurança mais comuns em sites e APIs |
| **Criptografia** | Embaralhar dados para só quem tem a chave ler |
| **2FA** | Segundo fator de login (código no celular) |
| **Pentest** | Teste de invasão autorizado, para achar falhas antes dos outros |
| **eJPT, OSCP, Security+** | Certificações de segurança, da mais simples à mais difícil |
| **LGPD** | A lei brasileira de proteção de dados pessoais |
| **KeePassXC** | Cofre de senhas que fica no seu computador |

## IA e dados

| Termo | O que é |
|---|---|
| **IA / machine learning** | Programas que aprendem padrões a partir de exemplos |
| **Deep learning / rede neural** | Machine learning com muitas camadas de "neurônios" matemáticos |
| **LLM** | Modelo de linguagem grande (como o Claude) |
| **Transformer** | A arquitetura por trás dos LLMs |
| **Treinar do zero / fine-tuning** | Ensinar um modelo desde o começo / ajustar um modelo pronto com os seus dados |
| **8B** | Modelo com 8 bilhões de parâmetros (tamanho médio, dá para ajustar com GPU alugada) |
| **RAG** | A IA responde consultando os seus documentos |
| **GPU** | Placa de vídeo; faz as contas da IA muito mais rápido |
| **Kaggle** | Site com GPU grátis para treinar modelos |

## Finanças, economia e investimentos

| Termo | O que é |
|---|---|
| **Fluxo de caixa** | O dinheiro que entra e sai, mês a mês |
| **DRE** | Relatório que mostra se a empresa teve lucro ou prejuízo |
| **Balanço patrimonial** | Foto do que a empresa tem e do que ela deve |
| **Regime de caixa / competência** | Contar a venda quando o dinheiro entra / quando a venda acontece |
| **Margem de contribuição** | Quanto sobra de cada venda para pagar os custos fixos |
| **Juros compostos** | Juros sobre juros |
| **VPL / TIR** | Contas para saber se um investimento vale a pena |
| **Valuation** | Calcular quanto uma empresa vale |
| **ARCA** | Método de dividir a carteira: Ações, Real estate (FIIs), Caixa e Ativos internacionais |
| **Barsi / Bazin / Graham / Buffett** | Métodos de escolher ações (dividendos, preço-teto, margem de segurança, vantagem competitiva) |
| **FII** | Fundo imobiliário |
| **Renda fixa** | Investimento com regra de rendimento conhecida (Tesouro, CDB) |
| **Carnê-leão** | Imposto mensal de quem recebe de pessoa física no CPF (aulas, freelas) |
| **MEI / Simples Nacional / CNPJ** | Tipos de empresa e de imposto no Brasil |
| **NF-e / NFC-e / NFS-e** | Notas fiscais de produto / do consumidor (caixa) / de serviço |
| **Pix / Open Finance** | Pagamento instantâneo / compartilhamento de dados bancários com autorização |
| **CVM** | O órgão que fiscaliza o mercado de investimentos |
| **BACEN** | O Banco Central |
| **ANBIMA / APIMEC** | Entidades que aplicam provas de certificação do mercado |
| **CPA / C-Pro I / C-Pro R** | Certificações da ANBIMA para trabalhar com investimentos (substituíram CPA-10, CPA-20 e CEA em 2026) |
| **CNPI** | Certificação de analista de investimentos (APIMEC) |
| **CGA / CGE** | Certificações de gestor de fundos (ANBIMA) |
| **CFA** | Certificação internacional de análise de investimentos, em inglês, com 3 níveis |
| **CFP** | Certificação de planejador financeiro pessoal |
| **Consultor / gestor de carteiras** | Quem recomenda investimentos / quem administra o dinheiro dos outros |
| **Gestora / administrador fiduciário / custodiante** | Empresa que decide os investimentos do fundo / empresa que responde legalmente pelo fundo / empresa que guarda os ativos |
| **Econometria** | Estatística aplicada à economia |
| **Selic / IPCA** | Taxa básica de juros / índice oficial de inflação |

## Plano, método e ferramentas suas

| Termo | O que é |
|---|---|
| **Vault** | A pasta do Obsidian com todos os seus documentos de plano |
| **Obsidian** | O programa onde você lê e liga as notas |
| **Passo** | Cada etapa da trilha de estudo (são 14) |
| **EPIC-01** | As tarefas detalhadas do Passo 1 |
| **Trilha paralela** | Estudo que roda junto da trilha principal, uma por vez |
| **Gatilho** | O acontecimento que libera uma etapa (ex.: "primeira venda feita") |
| **Portão** | Condição para abrir um negócio físico (são 5) |
| **Validar antes de construir** | Vender a versão mais simples antes de fazer a completa |
| **Setup / `dev-setup`** | Tudo o que você usa para trabalhar / o repositório que documenta e instala isso |
| **Pipeline de conteúdo** | A esteira que transforma uma gravação sua em várias postagens |
| **n8n** | Ferramenta de automação ("quando acontecer X, faça Y") |
| **Caixa da Casa** | O seu sistema de finanças pessoais e da família |
| **Ferramenta de status** | Painel (Go/Python) que mostra o estado de todos os projetos (substitui o antigo aura-status em C#) |
| **Anki** | Aplicativo de revisão com cartões, que lembra você na hora certa |
| **École 42** | Escola de programação sem professor; você segue o currículo dela em C/C++ |
| **roadmap.sh** | Site com mapas do que estudar em cada área |
