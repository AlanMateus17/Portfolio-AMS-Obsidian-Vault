# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [1.16.0] - 2026-10-26

### Adicionado
- `tools/plano_mestre/`: junta este roteiro, o portfólio e o Sumário do vault de estudos num só passo a passo (`00-PLANO-MESTRE-PASSO-A-PASSO.md`, 391 itens com código, "pronto quando" e ligações).
- Documentação do setup copiada para o vault de estudos, na pasta `11-setup-dev-setup`.

### Mudado
- Datas ligadas à trilha de estudo do vault (Portfolio-AMS-Obsidian-Vault): dados e treino de IA depois do Passo 8, IA nos sistemas depois do Passo 9, candidatura às vagas quando o Passo 8 estiver feito.
- Concurso PF/PRF saiu do plano de estudo (baralhos do Anki sem concurso).

### Corrigido
- Os templates HTML (diagrama, mapa, portfólio, planejador e acompanhamento) foram recuperados dos artefatos publicados e voltam a gerar `docs/*.html`; todos os `--check` e testes passam.

## [1.15.1] - 2026-10-24

### Corrigido
- Os comandos do Windows usavam `.\scripts\windows\...` e falhavam quando o PowerShell de Administrador abria em System32. Agora apontam para `$HOME\dev-setup\scripts\windows\...`, e o primeiro passo deixa a pasta em `C:\Users\SEU_USUARIO\dev-setup`. O passo de copiar para o WSL usa essa mesma pasta.

## [1.15.0] - 2026-10-24

### Adicionado
- Fase "Senhas: recuperar, trocar e guardar" logo depois de Preparar (12 passos): cofre do KeePassXC com senha mestra de 6 palavras, kit de emergência em papel, o e-mail principal primeiro, importação das senhas do Chrome, Edge e Google com o CSV apagado na hora, relatório de senhas fracas, repetidas e vazadas, troca das contas críticas com verificação em duas etapas, recuperação das esquecidas, cofre no celular, preenchimento no navegador, backup e revisão a cada 3 meses. O passo do KeePassXC sai da fase Windows e abre essa fase.

## [1.14.1] - 2026-10-23

### Corrigido
- O diagnóstico agora roda com `RODAR-DIAGNOSTICO.cmd` na raiz (botão direito > Executar como administrador): ele entra sozinho na própria pasta, confere que `scripts\windows\diagnostico.ps1` está ali e não percorre nenhuma outra pasta. As instruções anteriores rodavam `Unblock-File` a partir da pasta onde o PowerShell abria (System32 ou a pasta do usuário).
- O plano B do passo (comando para colar) só aceita o arquivo dentro de `scripts\windows` e não usa `Unblock-File`: com `-ExecutionPolicy Bypass` ele não é necessário.

## [1.14.0] - 2026-10-23

### Adicionado
- Etapa 0 "Diagnóstico: o que você já tem" antes de tudo: `scripts/windows/diagnostico.ps1` (somente leitura) lê hardware, segurança, programas, WSL, Docker, Ollama e extensões, compara com o setup e diz em que passo do roteiro cada pendência se resolve; mais a lista das contas que você já tem e a contagem dos documentos. Roda no CI.
- Fase "Primeira venda: o mini-curso no ar" (8 passos, da gravação à primeira venda com acesso, suporte, painel e carnê-leão) e fase "Mais ofertas, uma por vez" (20 ofertas na ordem da pontuação).
- Cada uma das 47 ofertas do portfólio ligada ao passo em que entra à venda; o portfólio mostra "Quando entra"; o CI falha se uma oferta ficar sem passo.
- Passo que põe o banco de métricas e os fluxos do n8n no backup diário (eles ficavam em volumes do Docker, fora do restic).
- Bloco Diagnóstico do notebook e o fluxo "Do notebook à primeira venda".

## [1.13.0] - 2026-10-23

### Mudado
- Todo o planejamento entra no passo a passo: os 87 blocos que estavam como "para depois", "peça a construir" ou "não se instala" ganharam passo, e cada uma das 30 fases tem **quando** (semana e mês) e, quando depende de resultado, o **gatilho**. Fases novas: marketing pago, Linux nativo, IA nos sistemas AM, sistemas AM à venda, CNPJ, agentes do grupo, editora depois do primeiro livro, plataforma e segunda nuvem, infraestrutura própria e os 9 negócios pelos portões.
- O roteiro e o acompanhamento terminam com "Quando entra cada bloco", camada por camada; o diagrama, o mapa e os documentos de cada camada mostram o passo e a data de cada bloco.
- O CI falha se um bloco, mesmo futuro, não tiver passo, ou se uma fase não tiver data.
- "Fora do setup" vira "Decisões": dual boot, Kali, mobile e o treino do 8B entram por outro caminho, com passo; ficam de fora só OpenClaw (segurança) e o que você mesmo rejeitou.
- O diagrama volta a ter a seção de auditoria e a opção "Ver todas as conexões".

### Adicionado
- Bloco App mobile (.NET MAUI), em 2028.

## [1.12.0] - 2026-10-23

### Adicionado
- `tools/acervo/acervo.py`: lê todos os seus documentos sem alterar a origem, acha cópias, separa os pessoais, marca material de terceiros e da escola e dados de alunos, converte o resto para Markdown no Obsidian e escreve o relatório de produtos candidatos. Regras em `regras.py`, 9 testes no CI e teste de verdade com .docx, .pptx e .pdf.
- `scripts/wsl/vault.sh`: cofre do Obsidian em `~/dev/notas` com pastas de estudo, aulas, acervo, produtos e conteúdo, e modelos de nota.
- Fase "Acervo: tudo o que você já tem" no roteiro (7 passos), blocos Google Drive e Acervo e o fluxo "Do documento antigo à venda".
- Campo `precisa` nos passos (compra, pagamento, conteúdo) e o filtro "Só o que dá para fazer hoje" no acompanhamento: 135 dos 148 passos só precisam do notebook e de contas grátis.

## [1.11.0] - 2026-10-23

### Adicionado
- Camada nova "Dados e treino de IA" com 13 blocos: Python de dados, DuckDB, dbt, Airflow, PySpark, PyTorch com CUDA no WSL2, Hugging Face, Unsloth, Kaggle e Colab, MLflow, avaliação, GGUF e os seus datasets (só conteúdo seu). Fluxos "Treinar uma IA sua" e "Dados de venda viram decisão".
- Pendrives de Kali (persistência criptografada) e de Arch (instalação portátil), Rufus no winget e o cuidado com Secure Boot e BitLocker no mapa.
- `scripts/wsl/lab-ia.sh`: laboratório de dados e de IA em `~/dev/lab-ia` (opção `--so-dados`); `verificar.sh` confere a GPU e o laboratório.
- Fase "Dados, IA e pendrives" no roteiro (12 passos, do pendrive ao seu modelo no Ollama) e duas etapas novas na ordem de estudo: engenharia de dados e IA profunda.

### Mudado
- "LLM 8B na GPU / fine-tuning" e "Engenharia de dados" saem de "cortado". Fica cortado só treinar um 8B na GTX 1650 (pede 6 GB de VRAM, a placa tem 4): o 8B roda no notebook dividido entre GPU e RAM, e o treino vai para a nuvem.
- Os botões de fluxo do diagrama saem dos dados, não do HTML.

## [1.10.0] - 2026-10-23

### Corrigido
- Diagrama do ecossistema: as 529 linhas apareciam todas juntas, atravessando o desenho; no celular os blocos ficavam cortados e o painel do bloco aparecia lá embaixo da página. Agora os blocos se reorganizam na largura da tela, as linhas aparecem só para o bloco ou o fluxo escolhido (com seta) e o painel fica fixo na tela.
- Os 13 fluxos tinham 37 passos sem conexão entre si, então o destaque mostrava blocos soltos. Todos refeitos sobre conexões reais.
- Conexões com o sentido trocado (Sentry, Seq, Mailpit, Kafka, Terraform → Google Cloud, Obsidian → Anki, livro → isca, flywheel → pipeline) e conexões erradas ou duplicadas (n8n → Hotmart, Obsidian → livro, TeX → livro, Arduino nos dois sentidos, 7-Zip → backup, edição do professor → sites).
- Blocos na camada errada: n8n e MailerLite (marketing), comunidade e Google Perfil da Empresa (público), Syncthing (Windows), assinatura e API do Claude (Claude).
- Mapa do setup: células vazias cinza no fim de cada camada, cartões de mercado com o texto empurrado para baixo e a lista de cortes desalinhada.
- Roteiro: a página de vendas do Instituto AMS ia para o Vercel, cujo plano grátis não permite uso comercial; agora vai para a Cloudflare Pages, como o mapa já indicava.
- Contas: a lista agora sai dos próprios blocos marcados com conta; Umami e Anki passam a pedir conta; Cloudflare e vidIQ saem de "sugeridos" (já estão conectados).

### Adicionado
- Blocos Wireshark e Telegram (avisos); 38 conexões que faltavam (pipeline → API do Claude e Telegram, túnel da Cloudflare → n8n, MCP → banco de métricas, Uptime Kuma → n8n e Telegram, entre outras).
- `gerar_docs.py` falha com bloco sem conexão, conexão nos dois sentidos, conexão sem rótulo e fluxo com passo sem conexão; `tools/test_gerar_docs.py` no CI.

## [1.9.0] - 2026-10-23

### Corrigido
- O roteiro de implantação cobria só parte do setup (cerca de 176 dos 303 blocos). Agora cada passo diz quais blocos implanta e todos os 303 têm lugar: 214 em passos, 9 peças a construir, 3 que não se instalam e 77 para depois.
- Blocos n8n, banco de métricas, painel de lucro, webhooks de venda e aprovação no celular deixam de ser "futuro": a implantação já os coloca no ar.

### Adicionado
- Roteiro com 18 fases e 129 passos: hardware, Defender, Claude in Chrome, extensões do VS Code, dotfiles, Obsidian Git, Syncthing, ADRs, MCP, ai-memory, RAG, recursos do Claude, conectores e plugins, outros assistentes, estúdio de conteúdo, WhatsApp Business, sites, Umami, Hostinger, vendas e finanças no CPF (gov.br, banco, contador, LGPD, plataformas, Mercado Pago, agenda, CRM, comunidade, afiliados, UTM, ofertas, avaliações, prospecção, INPI, carnê-leão, IRPF, Caixa da Casa), base dos sistemas AM, nuvem e deploy, editora e estudo.
- `tools/implantacao/gerar.py` falha se um bloco do setup ficar fora do roteiro, se um passo citar bloco que não existe ou se um bloco estiver em dois lugares; roteiro e acompanhamento mostram o que cada passo implanta e a cobertura completa. 5 testes novos.
- `scripts/wsl/nuvem.sh`: Azure CLI, Terraform, Vercel CLI e Wrangler.
- `scripts/windows/extensoes-vscode.ps1` com `vscode-extensoes.txt` e `.vscode/extensions.json`.
- Wireshark no winget (o Unity Hub só pelo passo de decisão); nmap e dnsutils no `bootstrap.sh`; `verificar.sh` confere as ferramentas novas como opcionais.

## [1.8.0] - 2026-10-21

### Adicionado
- Implantação: `data/implantacao.json` com 11 fases e 58 passos, gerando `docs/implantacao/roteiro.md` e `acompanhamento.html`.
- `scripts/windows/instalar.ps1` e `verificar.ps1` (winget com IDs conferidos, WSL2, .wslconfig, segurança).
- `scripts/wsl/bootstrap.sh`, `verificar.sh` e `ativar-pipeline.sh` (ferramentas, .NET 10, Node, uv, gitleaks, trivy, Claude Code, ai-jail, Git assinado, pastas, timer).
- `infra/automacao/`: Docker Compose com n8n, banco de métricas (esquema, views de lucro e de melhor horário, usuário só de leitura), Grafana e Uptime Kuma; `infra/postiz/README.md`.
- `tools/conteudo/processar.py`: pipeline de conteúdo com transcrição local, guia de marca, fila de aprovação e aviso no Telegram, com 10 testes.
- `config/marca.md`: guia de marca para preencher.
- CI: job novo com ShellCheck, PSScriptAnalyzer e validação do Docker Compose.

## [1.7.1] - 2026-10-21

### Corrigido
- `docs/mapa.html` estava escrito à mão e mostrava 10 camadas e 5 fluxos antigos. Agora é gerado de `tools/mapa.template.html` com `data/ecossistema.json` e `data/mapa.json`: as 22 camadas, os 299 blocos com conexões e os 13 fluxos, conferido no CI.
- Receita do ponto de retirada corrigida de R$ 1.150 para R$ 1.140, como dá o motor financeiro.
- Os dados embutidos no planejador e no portfólio escapam `</` para não quebrar a página.

### Adicionado
- `tools/negocios/test_coerencia.py`: confere se os números escritos nos documentos batem com o motor financeiro e com o portfólio.

## [1.7.0] - 2026-10-21

### Adicionado
- `docs/operacao/`: esteira de ofertas, marca e presença, flywheel de conteúdo, automação e escala, padrão de qualidade, clientes e dados, ordem de execução.
- `data/portfolio.json` com 47 ofertas (14 fontes de renda novas) e `tools/portfolio/portfolio.py`, que valida, pontua e gera `docs/operacao/portfolio.md` e `portfolio.html`, com testes no CI.
- Camada "Operação do grupo", 18 blocos (incluindo os agentes do grupo) e o fluxo "Do trabalho ao conteúdo".

## [1.6.0] - 2026-10-21

### Adicionado
- `docs/negocios/`: os nove negócios do grupo em Barbacena (software, loja, peças, Maker, ponto de retirada, entregas e Flex, delivery, sushi, cafeteria, padaria), estrutura de CNPJs, ordem com portões, cardápios e desperdício, mínimo legal e sistemas.
- `data/negocios.json` e `tools/negocios/financas.py`: motor financeiro com Simples por anexo, ponto de equilíbrio, rampa, retorno e capital mínimo, com testes no CI.
- `docs/negocios/numeros.md` e `docs/negocios/planejador.html` (planejador interativo), gerados e conferidos no CI.
- Camada "Negócios do grupo", 18 blocos, 34 conexões e o fluxo "Abrir o próximo negócio".

## [1.5.0] - 2026-10-21

### Adicionado
- `docs/editora/10-imagens-e-figuras.md`: acervos, regras de licença, busca automática e figuras geradas por código.
- `docs/editora/11-automacao-e-metodo.md`: o método de criação dentro do pipeline e o que é automático.
- `tools/editora/tabela_verdade.py` com testes, rodando no CI.
- 11 blocos e o fluxo "Ilustrar um capítulo".

## [1.4.0] - 2026-10-21

### Adicionado
- `docs/editora/09-nivel-e-concursos.md`: caminho único, livro autocontido, matemática e física da TI, concursos PF, PRF e Forças Armadas, critério de domínio.
- Blocos Matriz de editais, Projeto do capítulo e Mapa de pré-requisitos.
- Critérios 11 a 13 na avaliação do livro; itens novos no checklist de rigor.

## [1.3.0] - 2026-10-21

### Adicionado
- Camada "Editora AMS Silva (produção de livros)" com 22 blocos: selo, repositório do livro, modelo de criação, fonte única, exercícios em YAML, pranchas TikZ, classe LaTeX, pipeline do livro, revisão automática, agentes, leitores beta, errata, ISBN, ficha catalográfica, depósito legal, KDP, gráfica sob demanda, kit, curso, edição do professor, traduções e quadro de referências.
- Fluxo "Produzir um capítulo do livro".
- Plano da editora em `docs/editora/` (8 documentos).

## [1.2.0] - 2026-10-20

### Adicionado
- `docs/marketing/11-canais-de-anuncio.md`: todos os canais de anúncio com o limite de custo de cada um.
- `docs/infra/`: vários computadores, SSD externo, NAS local e armazenamento em nuvem.
- Blocos de Spotify, Kwai, Pinterest, LinkedIn, mídia nativa e influenciadores; SSD externo, workstation, Syncthing, Backblaze B2 e GPU por hora.

### Alterado
- Servidor caseiro detalhado (NAS + serviços 24 h).

## [1.1.0] - 2026-10-20

### Adicionado
- Camada 18 "Marketing, automação e medição" (Postiz, aprovação no celular, algoritmo de horário, Pixel + CAPI, UTM, regras de corte, webhooks, banco de métricas, painel de lucro, afiliados, prospecção, dublagem).
- TikTok e Facebook na camada de público; voz clonada com ElevenLabs.
- Fluxos "Publicar automaticamente no melhor horário" e "Medir o lucro de uma campanha".
- Plano de marketing, vendas e automação em `docs/marketing/` (10 documentos).

### Alterado
- O gerador remove páginas de camada que deixaram de existir.
- Diagramas Mermaid sem cliques (o GitHub não os abre); a navegação fica nas tabelas.

## [1.0.0] - 2026-10-20

### Adicionado
- Fonte única de dados em `data/` (18 camadas, blocos, conexões, fluxos, contas, auditoria e plano de estudo).
- Gerador `tools/gerar_docs.py` com validação dos dados.
- Uma página por camada em `docs/camadas/`, com diagrama Mermaid e tabela de conexões de cada bloco.
- Arquitetura, fluxos de ponta a ponta, contas, auditoria, sistemas operacionais, nuvem, mercado, roteiro, peças autorais e cortes.
- Diagrama interativo `docs/index.html`, gerado a partir dos mesmos dados.
- ADRs 0001 a 0003.
- Script de inventário somente leitura do Windows.
- Workflow do GitHub Actions que valida os dados e confere os arquivos gerados.
