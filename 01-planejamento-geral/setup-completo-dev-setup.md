---
tags: [setup, infraestrutura, implantacao, portfolio-ams]
tipo: plano
status: ativo
atualizado: 2026-10-26
---

# 🖥️ O Setup Completo — Projeto e Planejamento

> Todos os passos do setup estão no [Plano Mestre](../00-PLANO-MESTRE-PASSO-A-PASSO.md) com códigos `S-…`, distribuídos nas mesmas etapas do estudo.

> **Em palavras simples:** "setup" é tudo o que você usa para trabalhar: o notebook, os programas, as contas, as automações e os sistemas que fazem o trabalho repetitivo por você. O seu setup foi planejado para **três coisas ao mesmo tempo**: estudar para ser dev sênior, produzir conteúdo e aulas, e **vender** (cursos, sites, serviços). Ele está documentado num repositório privado chamado **`dev-setup`**, com scripts que instalam e conferem tudo.
>
> **De onde veio este resumo:** da conversa "Arquitetura e ferramentas do setup" (até 24/10/2026). O `dev-setup` é privado e não pôde ser aberto nesta revisão; **ele é a fonte oficial** — quando os números divergirem, vale o repositório.

---

## 1. O que existe no repositório `dev-setup`

> **Agora está tudo dentro deste vault**, na pasta [11-setup-dev-setup](../11-setup-dev-setup/00-INDICE-DO-SETUP.md): os documentos, os 17 fluxogramas, o roteiro passo a passo, as páginas interativas, os dados e os scripts. As datas das fases seguem a trilha de estudo (ver a coluna "Quando").

| Peça | O que é, em palavras simples |
|---|---|
| **Mapa do ecossistema** (`ecossistema.json`) | Desenho de tudo: **326 blocos** (cada programa, conta, serviço ou sistema) ligados por **609 conexões**, em **23 camadas** |
| **Roteiro de implantação** (`implantacao.json`) | A receita, em ordem: **34 fases e 253 passos**, cada passo com "pronto quando" e "quem faz" |
| **Acompanhamento** (`acompanhamento.html`) | A página onde você marca o que já fez. Tem o filtro **"Só o que dá para fazer hoje"** (168 passos só com o notebook e contas grátis) |
| **Portfólio** (`portfolio.json`) | As **47 ofertas** de renda, pontuadas — detalhadas em [fontes-de-renda-completas](fontes-de-renda-completas.md) |
| **Negócios** (`negocios.json`) | Os números dos **9 negócios de Barbacena**, com simulador |
| **Scripts do Windows** | `diagnostico.ps1` (só lê o notebook), instalador, verificador, e o atalho `RODAR-DIAGNOSTICO.cmd` (duplo clique) |
| **Scripts do Linux (WSL)** | `bootstrap.sh` (instala linguagens e ferramentas), cofre, laboratório de IA, nuvem, verificador |
| **Pipeline de conteúdo** (`tools/conteudo/processar.py`) | Você grava → o Whisper transcreve → a IA monta as peças (cortes, carrossel, newsletter, post) → você aprova no celular → publica sozinho |
| **Acervo** (`tools/acervo/acervo.py`) | Transforma os seus documentos antigos em notas do Obsidian, filtrando material pessoal, de terceiros e da escola |
| **CI no GitHub** | Testes automáticos que falham se algum bloco, oferta ou fase ficar sem passo ou sem data |

**Regra do repositório:** nada é retirado do plano sem você confirmar; o que fica para depois recebe **passo e data** (ou gatilho).

---

## 2. O hardware

**Notebook Acer Nitro AN515-45:** Ryzen 7 5800H, 32 GB de RAM, placa de vídeo GTX 1650 (4 GB), SSD de 1 TB, dois slots M.2 e uma baia de 2,5" livres, segundo monitor. Configurado **só para trabalho** (sem jogos, sem programas inúteis).

**Limite honesto:** 4 GB de vídeo não bastam para treinar ou ajustar um modelo de IA de 8B (precisa de 6 GB ou mais). Por isso o ajuste fino vai para a **GPU grátis do Kaggle** ou GPU alugada na nuvem.

---

## 3. As fases do roteiro, em ordem

> **Em palavras simples:** é a lista do que montar primeiro. As primeiras 15 fases (umas 51 horas) usam só o que você já tem. Até a primeira venda do curso são cerca de **75 horas**, umas **15 semanas a 5 horas por semana** (quinta e sexta de manhã).

| Fase | Nome | O que você ganha com ela | Quando | Primeiro item no Plano Mestre |
|---|---|---|---|---|
| 0 | Diagnóstico: o que você já tem | Saber exatamente o que o notebook já tem de hardware, segurança, programas, contas e documentos, e começar o roteiro a partir daí. | Antes de tudo · semana 1 (out/2026) | `S-diag-pasta` |
| 1 | Preparar | Nada se perde, o hardware está no lugar e as contas estão protegidas antes de mexer na máquina. | Semana 1 · out/2026 | `S-backup-inicial` |
| 2 | Senhas: recuperar, trocar e guardar | Toda conta com senha única guardada no KeePassXC, verificação em duas etapas nas críticas e um jeito de recuperar tudo se perder o notebook ou o celular. | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 | `S-keepass` |
| 3 | Windows | Os programas do setup instalados, o navegador com o Claude e o WSL2 pronto. | Semana 1 · out/2026 | `S-win-simular` |
| 4 | Linux (WSL2) | O Ubuntu com tudo o que o código precisa, commits assinados e o ambiente versionado. | Semana 2 · nov/2026 | `S-ubuntu-usuario` |
| 5 | GitHub e CI | O repositório no ar, com testes automáticos verdes a cada envio e o trabalho organizado. | Semana 2 · nov/2026 | `S-repo-criar` |
| 6 | Agentes de IA | O Claude Code trabalhando dentro da sandbox, com as suas regras, ferramentas e memória. | Semana 2 · nov/2026 | `S-claude-login` |
| 7 | Backup e segurança | Perder o notebook não faz você perder nada. | Semana 3 · nov/2026 | `S-restic-local` |
| 8 | Acervo: tudo o que você já tem | Todos os seus documentos convertidos em conhecimento organizado no Obsidian, os pessoais separados e a lista do que dá para vender. | Semanas 3 e 4 · nov/2026 | `S-acervo-copia` |
| 9 | Claude e assistentes | Cada recurso do Claude e cada assistente com um papel definido no setup. | Semana 4 · nov/2026 | `S-claude-app` |
| 10 | Automação e medição | n8n, banco de métricas, Grafana e Uptime Kuma rodando. | Semana 4 · nov/2026 | `S-senhas` |
| 11 | Pipeline de conteúdo | Gravou ou escreveu, as peças aparecem na fila de aprovação. | Semana 5 · nov/2026 | `S-marca` |
| 12 | Estúdio de conteúdo | Gravar, editar e montar imagens no mesmo padrão toda semana, sem pensar. | Semana 5 · dez/2026 | `S-obs-cenas` |
| 13 | Contas, canais e sites | Perfis, domínio, e-mail e sites prontos para receber o que o pipeline produz. | Semanas 6 e 7 · dez/2026 | `S-perfis` |
| 14 | Vendas e finanças no CPF | Cada oferta pode ser vendida, recebida e declarada do jeito certo. | Semanas 8 a 10 · dez/2026 a jan/2027 | `S-govbr` |
| 15 | Vendas medidas | Cada venda chega sozinha ao banco e aparece no painel de lucro. | Semana 11 · jan/2027 | `S-tunel` |
| 16 | Teste do núcleo | Os três testes de ponta a ponta passam: daqui em diante, alimentar o sistema já faz tudo sozinho. | Semana 11 · jan/2027 | `S-teste-dev` |
| 17 | Primeira venda: o mini-curso no ar | A primeira venda real pela internet, com entrega, suporte, imposto e números no painel. | Semanas 12 a 15 · jan a fev/2027 | `S-mc-roteiro` |
| 18 | Base dos sistemas AM | Um sistema novo nasce pronto: arquitetura, testes, login, observabilidade e deploy. | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 | `S-template-aura` |
| 19 | Nuvem e deploy | As contas de nuvem criadas por código, com custo sob controle. | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) | `S-nuvem-clis` |
| 20 | Editora | O livro sai de um repositório com CI, pronto para virar PDF, EPUB e impressão. | Quando o capítulo 1 estiver pronto · ⏸ espera: O capítulo 1 e o seu modelo de criação prontos | `S-modelo-metodo` |
| 21 | Dados, IA e pendrives | O laboratório de dados e de treino no ar, um modelo seu rodando no Ollama e os pendrives de Kali e Arch dando boot. | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) | `S-pendrive-kali` |
| 22 | Mais ofertas, uma por vez | Cada oferta do portfólio entra na esteira na ordem da pontuação: uma em construção e uma em validação por vez. | Fev a dez/2027, uma oferta por vez · ⏸ espera: A primeira venda do mini-curso aconteceu | `S-of-meu-setup` |
| 23 | Marketing pago e crescimento | Pôr dinheiro em anúncio só quando a venda orgânica provou a oferta. | A partir de fev/2027 · ⏸ espera: O mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar | `S-ads-meta` |
| 24 | Linux nativo e laboratório completo | Arch com boot próprio, VMs de laboratório e a segurança física em dia. | 2027, conforme cada compra | `S-nvme-arch` |
| 25 | IA dentro dos sistemas AM | Busca e assistente com os seus dados dentro de um sistema AM. | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 | `S-rag-sistema` |
| 26 | Sistemas AM à venda | Os sistemas viram produto por assinatura. | 2027 · ⏸ espera: O primeiro sistema AM pronto e testado com um cliente | `S-saas` |
| 27 | CNPJ e formalização | Sair do CPF na hora certa, com nota fiscal e cobrança automáticas. | Quando a renda pedir · ⏸ espera: A renda passou do valor de virada definido com o contador | `S-cnpj` |
| 28 | Agentes do grupo | Atendimento, orçamento, cobrança e análise rodando com a sua aprovação. | Junto com o primeiro CNPJ · ⏸ espera: Clientes e vendas recorrentes | `S-ag-analista` |
| 29 | Editora: depois do primeiro livro | O mesmo livro em mais formatos, públicos e idiomas. | Depois do primeiro livro · ⏸ espera: O primeiro livro publicado | `S-grafica` |
| 30 | Distribuído, plataforma e segunda nuvem | O que pesa em vaga pleno e sênior. | 2028 | `S-mensageria` |
| 31 | Infraestrutura própria | Servidor em casa e máquina de IA quando o grupo pedir. | 2028, quando o grupo pedir | `S-nas` |
| 32 | Negócios do grupo em Barbacena | Um negócio por vez, cada um só depois que o anterior passa no portão. | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano · ⏸ espera: Os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta | `S-planejador-real` |
| 33 | Estudo contínuo | As trilhas de estudo ligadas ao setup, sem copiar conteúdo de ninguém. | Contínuo, desde a semana 2 | `S-github-education` |

> Os nomes e datas das fases vêm da conversa; a coluna "o que você ganha" é um resumo em linguagem simples feito a partir do nome de cada fase. A numeração exata pode variar em uma posição por causa da fase de senhas, que foi inserida depois. O detalhe de cada passo está no `roteiro.md` e no `acompanhamento.html` do `dev-setup`.

---

## 4. Como o setup vira dinheiro (a "esteira")

> **Em palavras simples:** tudo o que você faz uma vez vira várias coisas. Uma aula vira vídeo, corte, carrossel, newsletter, questão de concurso e post no Google. Um cliente vira dado. Um processo repetido vira automação.

1. **Catálogo único:** as 47 ofertas, pontuadas.
2. **Esteira:** ideia → validação → construção → lançamento → escala. Só passa de etapa com prova real (uma venda, um checklist cumprido).
3. **Padrão de qualidade** por tipo de oferta (o que é "pronto").
4. **Venda e entrega**, com cadastro único de clientes e consentimento (LGPD).
5. **Flywheel de conteúdo:** cada trabalho vira peças que trazem novos clientes.
6. **Marca:** **você** é o guarda-chuva de confiança; Instituto AMS, Editora, AMtech e os negócios locais apontam para você. Nos negócios locais, o **Google Perfil da Empresa** é o canal mais forte, com pedido automático de avaliação (nunca comprada).
7. **Painel do grupo:** números por oferta, que decidem o que cresce e o que sai.

**Limites que o setup não resolve:** ele não grava a sua aula, não escreve o seu livro e não atende o primeiro cliente. **Dinheiro, preço, publicação em seu nome e reclamação séria nunca rodam sem você.**

---

## 5. Decisões já tomadas

| Decisão | Motivo |
|---|---|
| Vender no **CPF**, com carnê-leão mensal (sem MEI por enquanto) | Menos custo enquanto valida; programação geralmente não cabe no MEI |
| Hotmart, Kiwify, Eduzz, Udemy e DIO para cursos | Custo zero antecipado |
| **Obsidian** em vez de Notion | Arquivos seus, no seu disco e no GitHub |
| **Azure** antes da AWS | Combina com .NET |
| **Arch e Kali em pendrive**, nunca dual boot | Já houve perda de dados antes; procedimento de Secure Boot/BitLocker documentado |
| Ajuste fino de IA 8B no **Kaggle** ou GPU alugada | A GTX 1650 tem só 4 GB |
| Livro autocontido (ensina toda a matemática e física necessárias) | Leitor não precisa de outro livro antes |
| Nenhuma senha compartilhada com o Claude | Segurança |
| Fora do setup: OpenClaw (segurança) e o que você mesmo rejeitou (Bun, Hono, Rust, Tauri, gRPC) | Registrado em "Decisões" no `dev-setup` |

---

## 6. Documentos do vault ligados ao setup

- [setup-ambiente-trabalho-final](../06-execucao-e-desenvolvimento/setup-ambiente-trabalho-final.md) — o notebook reconstruído
- [infraestrutura-fisica-10-anos](infraestrutura-fisica-10-anos.md) — as 11 camadas físicas de 10 anos (estação, rede, NAS, oficina, robótica, estúdio)
- [seguranca-e-ferramentas-todas-as-frentes](seguranca-e-ferramentas-todas-as-frentes.md)
- [automacao-ordem-de-execucao](../06-execucao-e-desenvolvimento/automacao-ordem-de-execucao.md) e [automacao-o-que-e-por-que](../06-execucao-e-desenvolvimento/automacao-o-que-e-por-que.md)
- [aura-status](../10-ferramentas-pessoais/aura-status-documento-projeto-final.md) — o painel que mostra o estado de tudo
- [fontes-de-renda-completas](fontes-de-renda-completas.md) — o que o setup vende
- [trilha-robotica-iot](../07-estudo-e-carreira/trilha-robotica-iot.md) — casa inteligente e bancada maker (lista de 98 itens, de R$ 16,5 mil a R$ 39 mil, em 5 fases)

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Fluxogramas do Setup](../12-artefatos/paginas/fluxogramas-do-setup-vbdz/index.html) · página interativa · [sobre](../12-artefatos/paginas/fluxogramas-do-setup-vbdz/LEIA-ME.md)
- [Mapa do Setup AMtech](../12-artefatos/paginas/mapa-do-setup-amtech-btuy/index.html) · página interativa · [sobre](../12-artefatos/paginas/mapa-do-setup-amtech-btuy/LEIA-ME.md)
- [Implantação AMtech](../12-artefatos/paginas/implantacao-amtech-cj27/index.html) · página interativa · [sobre](../12-artefatos/paginas/implantacao-amtech-cj27/LEIA-ME.md)
- [Repositório dev-setup (versão de 23/10)](../12-artefatos/paginas/repositorio-dev-setup-k9wt/index.html) · página interativa · [sobre](../12-artefatos/paginas/repositorio-dev-setup-k9wt/LEIA-ME.md)
- [Repositório dev-setup (versão de 21/10)](../12-artefatos/paginas/repositorio-dev-setup-ria4/index.html) · página interativa · [sobre](../12-artefatos/paginas/repositorio-dev-setup-ria4/LEIA-ME.md)
- [Casa Inteligente e Setup Automatizado](../12-artefatos/documentos/casa-inteligente-e-setup-automatizado.md)
- [Guia de Terminal: Git, GitHub, PowerShell e Git Bash](../12-artefatos/documentos/guia-de-terminal-git-github-powershell-e-git-bash.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
