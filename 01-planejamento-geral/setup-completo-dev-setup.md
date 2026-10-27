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

| Peça | O que é, em palavras simples |
|---|---|
| **Mapa do ecossistema** (`ecossistema.json`) | Desenho de tudo: **326 blocos** (cada programa, conta, serviço ou sistema) ligados por **609 conexões**, em **23 camadas** |
| **Roteiro de implantação** (`implantacao.json`) | A receita, em ordem: **cerca de 34 fases e mais de 240 passos**, cada passo com "pronto quando" e "quem faz" |
| **Acompanhamento** (`acompanhamento.html`) | A página onde você marca o que já fez. Tem o filtro **"Só o que dá para fazer hoje"** (cerca de 157 passos só com o notebook e contas grátis) |
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

| Fase | Nome | O que você ganha com ela | Quando |
|---:|---|---|---|
| 0 | Diagnóstico | Saber o que o notebook já tem e o que falta (sem instalar nada) | Semana 1 |
| — | Senhas e contas | Cofre de senhas (KeePassXC), 2FA, recuperação de contas — **nenhuma senha passa pelo Claude** | Semana 1; 5 contas por semana até dez/2026 |
| 1 | Preparar | Pastas, disco, Windows Update, pontos de restauração | Semana 1 |
| 2 | Windows | Programas de trabalho instalados pelo script | Semana 1 |
| 3 | Linux (WSL2) | Ubuntu dentro do Windows, linguagens e ferramentas | Semana 2 |
| 4 | GitHub e CI | Repositórios, commits assinados, testes automáticos | Semana 2 |
| 5 | Agentes de IA | Claude Code e assistentes rodando com segurança | Semana 2 |
| 6 | Backup e segurança | Cópia automática (regra 3-2-1), Defender, criptografia | Semana 3 |
| 7 | Acervo | Todos os seus documentos organizados no Obsidian | Semanas 3–4 |
| 8 | Claude e assistentes | Conectores (Drive, Gmail, Agenda) e rotinas | Semana 4 |
| 9 | Automação e medição | n8n, painel de métricas (Grafana) | Semana 4 |
| 10 | Pipeline de conteúdo | Gravação → transcrição → peças → aprovação | Semana 5 |
| 11 | Estúdio | Áudio, câmera, luz, voz clonada (com consentimento seu) | Semana 5 |
| 12 | Contas, canais e sites | Instagram, YouTube, newsletter, página com afiliados | Semanas 6–7 |
| 13 | Vendas e finanças no CPF | Agenda com Pix, carnê-leão, Hotmart/Kiwify — **aulas, sites e afiliados já vendem aqui** | Semanas 8–10 |
| 14 | Vendas medidas | Cada venda cai no painel | Semana 11 |
| 15 | Teste do núcleo | Conferir tudo de ponta a ponta | Semana 11 |
| 16 | **Primeira venda** | Mini-curso no ar: gravar 5 aulas, página, isca grátis, pré-venda, venda real | Semanas 12–15 (jan–fev/2027) |
| 17 | Base dos sistemas AM | Fundação do Kaixara e dos outros | Jan–abr/2027 |
| 18 | Nuvem e deploy | Azure (antes da AWS), Vercel, VPS | Jan–abr/2027 |
| 19 | Editora | Produção do livro | Quando o capítulo 1 ficar pronto |
| 20 | Dados, IA e pendrives | Laboratório de IA; **Arch e Kali em pendrive** (sem dual boot) | Semana 2 em diante e 2027 |
| 21 | Mais ofertas, uma por vez | As 20 ofertas seguintes, pela pontuação | Fev–dez/2027 |
| 22 | Marketing pago | Anúncios, só com oferta que já vende | 2027 |
| 23 | Linux nativo | Arch + Omarchy no dia a dia | 2027, por gatilho |
| 24 | IA nos sistemas AM | aura-copilot e analytics de verdade | 2027 |
| 25 | Sistemas AM à venda | Kaixara, Rotara e outros com cliente pagante | 2027, por gatilho |
| 26 | CNPJ | Abrir a empresa quando a renda justificar | 2027, por gatilho |
| 27 | Agentes do grupo | Atendente de WhatsApp, orçamentista, cobrador, pós-venda, editor, analista semanal, organizador fiscal, comprador, revisor de oferta | 2027 |
| 28 | Editora depois do primeiro livro | Kit do professor, adoção por escolas, traduções | Depois do livro |
| 29 | Distribuído, plataforma e 2ª nuvem | Kubernetes, AWS | 2028 |
| 30 | Infraestrutura própria | NAS, homelab, servidor (ver [infraestrutura de 10 anos](infraestrutura-fisica-10-anos.md)) | 2028 |
| 31 | Negócios de Barbacena | Um por vez, pelos 5 portões | Ondas A, B e C |
| 32 | Estudo contínuo | A [Trilha Principal](../00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md) roda o tempo todo | Sempre |

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
