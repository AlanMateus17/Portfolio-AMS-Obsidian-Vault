# CONTINUAR: contexto completo para qualquer conversa nova

Cole este arquivo na primeira mensagem de uma conversa nova (ou rode `python3 ~/dev/dev-setup/tools/sessao/contexto.py --inicio | clip.exe`). Decisões do dia a dia vão para o ESTADO.md; este arquivo muda quando algo grande muda. Última revisão: 06/11/2026 (v2.16). Escola Akita: `just akita pendentes`. Para saber o que é seu: `just agora` e `just decisoes software`.

## 1. Quem sou e como trabalhar comigo
- Alan Mateus, Barbacena-MG. Professor de informática numa escola EMTI (9 disciplinas, Técnico em Informática e em Desenvolvimento de Sistemas), trabalho também num restaurante (terça a domingo à noite), fundador da Grupo AMtech Digital. Formado em ADS, cursando Licenciatura em Matemática. Tenho TDAH.
- Seja direto e honesto: diga quando algo não é possível ou não vale a pena. Sem enrolação.
- Comandos de UMA linha, sempre dizendo ONDE rodar: PowerShell do Windows (PS C:\>) ou Ubuntu do WSL (alanmateus@...$). Já errei muito rodando comando no terminal errado.
- Não sugerir Ctrl+C para copiar dentro do terminal (cancela). Senhas são digitadas à mão, nunca coladas.
- Nunca peça, leia ou guarde minhas senhas, códigos de recuperação ou chave do BitLocker. Segredos só no KeePassXC.
- Nada de dado de aluno (nome, nota, foto, voz) em IA. Não vender para alunos menores. Nada publicado ou enviado em meu nome sem aprovação.
- Não é assessoria financeira: aplique as MINHAS regras (cascata, ARCA, Barsi, Bazin, Graham, Buffett); a decisão é minha.
- Documentos financeiros pessoais (contracheques, extratos, IRPF) não vão para o GitHub nem para IA na nuvem.
- Não copiar conteúdo de VHSlins, livros ou cursos pagos (Udemy, DIO, Alura) para treinar IA ou produtos.
- Mudar configurações do GitHub (ex.: Dependabot) só com o meu "pode ligar".
- Commits terminam com as linhas de coautoria do Claude e da sessão.
- Uma conversa = uma tarefa. Termine me dando 5 linhas para o ESTADO.md.

## 2. Onde está tudo
- Repositório privado: github.com/AlanMateus17/dev-setup (branch main, CI verde). No PC: ~/dev/dev-setup (Ubuntu/WSL) e C:\Users\alanmateus\dev-setup (Windows).
- Regra do repositório: data/*.json → geradores → docs/. Nunca editar arquivo gerado. Toda mudança: dados ou ferramenta, geradores, testes, CHANGELOG, commit, push, CI verde.
- Números agora: 58 fases, 533 passos, 483 blocos, 108 rendas, 71 softwares, 27 metodologias de investimento. O CI recusa passo sem comando ou motivo, bloco fora do roteiro e renda sem passo.
- Artefatos: Painel do Núcleo (constelação do setup, o que já roda sozinho, principal e reserva, o que falta) https://claude.ai/artifact/Frwo8DGEdifkeVcCKdtTAo · Acompanhamento (progresso marcado) https://claude.ai/artifact/CJ27fg9sycvhqZ2s9GSbjd · Portfólio de rendas https://claude.ai/artifact/Mbj1yj6LRmUnf3SJLrTfaB · Mapa https://claude.ai/artifact/BTUyCQfojw6cngvR5W5oAB · Ecossistema https://claude.ai/artifact/4Ze2J4Y1oKgAkjuQmbAAG1 · Plano de automação (documento) https://claude.ai/artifact/XCzSQNb28yFgPCymRV9wrL · Posts do setup (design) https://claude.ai/artifact/V8826RzNePgWKuy6GuYPvd
- Guias no repositório: docs/implantacao/roteiro.md (passo a passo), docs/operacao/portfolio.md (rendas e automações), docs/operacao/softwares.md, docs/operacao/kit-sites.md, docs/custos.md (o que pagar, rotas de IA), docs/recursos.md (a melhor ferramenta para cada tarefa: primária, reserva e portão), docs/investimentos.md (as 27 metodologias nas 4 classes do ARCA), docs/certificacoes.md (o que cada certificação habilita e a ordem), docs/seguranca/README.md (engenharia reversa, AppSec e empresa de pentest), docs/jarvis/README.md (voz, casa, câmeras, energia, água, robótica e PC por comando de voz), docs/ia/hugging-face.md (modelos do Hub que cabem na GTX 1650 e as compras em ordem), docs/construcao/README.md (construção civil, arquitetura e engenharia pela TI), docs/operacao/24-horas.md, docs/operacao/sessoes-curtas.md, docs/ia/README.md, docs/rede/README.md.

## 3. Já feito no meu notebook (Acer Nitro, 32 GB, GTX 1650)
Fases 0, 3, 4 e 5 completas: diagnóstico, Windows (winget, BitLocker, Defender, extensões do VS Code), Ubuntu no WSL com Docker, gh e SSH, repositório no GitHub com CI. Também: backup inicial, Windows Update, 2FA do GitHub, KeePassXC instalado com os cofres copiados para o pendrive D:\Cofre. Falta: senhas (2.2 a 2.4), mesa (1.2), e todas as fases a partir da 6.

## 4. Decisões principais
- Arsenal de 108 rendas, cada uma com veredito (agora, próxima, fila, 2027, decidir, descartar), % automático e motivo.
- AGORA (máximo 3): Mini-curso Lógica de Programação, Sites e lojas para pequenas empresas, Avaliação de respostas de IA (DataAnnotation, Outlier).
- PRÓXIMAS, em ordem: 1. AM Mentor: banco de exercícios com correção; 2. Aulas particulares; 3. Notebooks e PCs: comprar, consertar e revender; 4. Fábrica de documentos para professores de MG (assinatura); 5. Setup profissional (curso, template e configuração remota); 6. Plano de negócios e viabilidade financeira para quem vai abrir empresa; 7. Verificador e formatador ABNT automático (TCC, artigos, relatórios).
- Regras: hora mínima R$ 45 por hora minha (a confirmar), teto de 7 h extras por semana (quinta 13h–16h30 negócio, sábado 9h30–12h30 produção), portão = 3 meses se pagando, corte = abaixo da hora mínima por 2 meses. Domingo, sono e cães são intocáveis.
- Marcas: AMtech Educação, Software, Digital, Campo (presencial por parceiros), Mídia, Economia, Patrimônio; Editora AMS Silva à parte.
- Harumakis/congelados: RETIRADOS do plano.
- Documentos da escola e TCC: Fábrica de documentos para professores (assinatura), verificador e formatador ABNT online (por documento) e conferência para coordenações. Só formatar e conferir; nunca escrever trabalho por aluno.
- IAs: Claude Pro principal; Google AI Plus (R$ 24,99, 200 GB) no lugar do Google One; ChatGPT Go grátis pelo Nubank; NotebookLM para rascunho de aulas; DeepSeek, OpenRouter e Gemini API grátis só para rascunho sem dado sensível; Z.AI GLM para testar como reserva de código; Perplexity grátis; Grok cortado; Claude Max só quando uma renda passar no portão.
- Custos: construir o que me diferencia, código aberto para infraestrutura, pagar só o que vale mais que minhas horas. Cortar IAs pagas repetidas; Vercel não serve para projeto comercial (usar Cloudflare Pages, GitHub Pages ou Hostinger); GitHub Education (estudante) para Copilot grátis.
- 24 horas sem pagar: GitHub Actions (vigia semanal já ativo), VM grátis da Oracle (2 núcleos, 12 GB desde jun/2026) para n8n, bot, Uptime Kuma e gateway; notebook para estudo e modelos locais.
- Modelos grandes sem PC maior: quantização, MoE, cluster na rede (llama.cpp RPC), QLoRA no Kaggle ou GPU alugada com teto, destilação; Strata (do Akita) só com GPU de 12 GB+.
- Setup 2.x (nov/2026): toda tarefa tem ferramenta primária, reserva e portão humano; nenhuma depende dos créditos de uma ferramenta só. Copilot Pro grátis como PROFESSOR é o motor da esteira de sites (issue → PR → CI → revisão do Claude → prévia → minha aprovação → Hostinger). Codex do ChatGPT Go como reserva. Gemini CLI e v0 fora. OpenClaw só isolado na VM, depois da esteira entregar um site.
- Investimentos: todas as metodologias ao mesmo tempo nas 4 classes do ARCA (ações 9, FIIs 7, renda fixa 4, internacional 7), consenso por ativo (forte, médio, fraco), aporte em dois níveis (classe → metodologia) com mínimo de R$ 100 por compra, uma carteira por metodologia contra o índice. As perguntas do Raul Sena ficam só nas minhas anotações em ~/financas.
- Certificações: CNPI primeiro (para poder recomendar ativos), depois registro de consultor na CVM, CGE/CGA, CFP, CFA. CPA e C-PRO só se for trabalhar em banco. AZ-204 saiu; o caminho Azure é AZ-900 → AI-200.
- Regra de "parar de adicionar áreas até a primeira venda" retirada a meu pedido: ideias novas entram no setup; a execução segue a ordem do roteiro.
- Prospecção: lista semanal de dados públicos com aprovação minha; nunca disparo em massa no WhatsApp. "Procurar buracos" só nos meus sistemas e de clientes com contrato.
- Segurança (nov/2026): engenharia reversa só em binário meu, de aluno em aula ou crackme; defesa dos meus sistemas antes de vender teste; ordem dos serviços: laudo dos sites → bug bounty → pentest web → rede/AD → red team; certificações eJPT → BSCP → OSCP → OSWE/OSEP. Nenhum teste sem termo assinado passando no escopo.py. Binário de cliente só com modelo local.
- Construção (v2.6): estudo com Bonsai, FreeCAD, QGIS e Autodesk educacional (só estudo); renda pela TI (automação BIM para escritórios, AM Obra em 2027). Alan não assina projeto, laudo, ART nem RRT; decisão de cursar Edificações ou Engenharia fica em aberto.
- Foco (nov/2026): TI em primeiro lugar, depois casa inteligente e agropecuária (pecuária, lavoura e horta, e o negócio AMtech Campo). O modelo de doença de folha saiu do plano.
- Hugging Face e robótica (v2.5): LeRobot com o par SO-101 como primeira compra de robótica, Reachy Mini como corpo do Jarvis depois, LeKiwi por último; Whisper large-v3-turbo, Qwen3-VL 2B local para a câmera que descreve, Docling para documentos, Prompt Guard só se acertar em português. Treino com bf16 (SmolVLA) vai para GPU alugada: a GTX 1650 e o T4 não têm bf16. GPU de 12 GB só depois do portão.
- Jarvis (v2.4): Home Assistant Assist com voz local (Whisper na GPU do notebook, Piper pt_BR, "hey jarvis") e o Claude como agente de conversa; Claude Code por voz no PC (/voice + falar.py). Casa num servidor próprio sempre ligado (ADR 0004), Zigbee e MQTT, Frigate local, leitor do hidrômetro, robôs pelo ESPHome e ROS 2. Política: destrancar, abrir janela/porta/portão e desligar geladeira só com toque no celular (geladeira religa sozinha); desarmar alarme, desligar câmera e apagar gravação proibidos por voz; no máximo 25 entidades expostas.
- Núcleo AMtech (v2.13, nov/2026, ADR 0009): o setup vira um sistema conectado e autônomo sem reescrever as ferramentas. Banco central (tools/nucleo: eventos, conhecimento, tarefas, auditoria; SQLite no notebook, PostgreSQL na VM) que a triagem e o arquiteto já leem e gravam. Tokens mínimos cifrados com sops/age na VM (exceção aceita), teto de IA dos agentes US$ 20/mês, garimpo adiantado para a fase 2. Objetivo: máximo de renda com menos horas e a base das empresas do grupo; o núcleo também é o produto de automação da empresa de TI.
- Empresa solo (v2.12, nov/2026): todas as ferramentas do contexto mestre estão no setup, cada função com principal e reserva (ADR 0008; docs/empresa-solo.md). Nenhuma linguagem é proibida (ADR 0007): Aura em .NET 10 + Next.js, Astro para sites, SvelteKit + PocketBase para MVP, Go para CLIs, Rust para firmware. Trocas: mise no lugar do fnm, Zellij no lugar do tmux, chezmoi nos dotfiles, GlitchTip e SigNoz na observabilidade, Astro nos sites, HeyForm e Formbricks no comercial, Beancount e Portfolio Performance nas finanças. Kamal em VM (ADR 0005); segredo só no KeePassXC (age e sops só para arquivo que sai da máquina); um repositório por sistema com apps/ e packages/; o que é pago liga quando uma renda pagar. Sprint de 14 dias no recesso de jan/2027.

## 5. Ferramentas prontas no repositório (comandos no Ubuntu)
- Montar tudo: just instalar (scripts/wsl/instalar-tudo.sh). Base do núcleo: just lembrar "..." TIPO, just buscar "...", just tarefas. Backup: just backup (agendado às 22h30).
- Porta única: just (na raiz do repositório): just check antes de todo commit, just triagem "pedido", just arquiteto "pedido", just docs, just ci-local, just contexto-ia PASTA, just medir "comando", just menu, just diagrama ARQ.d2, just servico PERFIL, just lab-abrir
- Complementares: scripts/wsl/extras.sh (CLIs do mise, uv, Podman, Git LFS); dotfiles do chezmoi em infra/dotfiles; serviços próprios por perfil em infra/soberania; MVP em infra/pocketbase; modelos go-cli, rust-cli e sala-limpa em infra/templates
- Triagem e arquiteto: tools/triagem/triagem.py triar | arquitetar
- Deploy em VM: infra/templates/kamal (Kamal pela imagem Docker, segredos pelo keepassxc-cli)
- Pacote de contexto: tools/sessao/contexto.py (--inicio, --resumo, --passo ID)
- Kit de sites: tools/kitsites/conferir.py URL (laudo); prompts e pacotes em docs/operacao/kit-sites.md; contrato em docs/operacao/contrato-sites-modelo.md
- Avaliador de templates: tools/avaliador/avaliar.py ~/templates (não roda código de terceiros)
- Verificador de documentos: tools/documentos/verificar.py arquivo.docx [--corrigir] [--perfil escola]
- Fábrica de aulas: tools/fabrica/plano_semanal.py e preencher.py; esqueleto do repositório privado "aulas" em infra/templates/repo-aulas
- Radar de revenda: tools/radar/radar.py anuncios.csv (preços em ~/.config/amtech/radar.toml)
- Organizadores: tools/organizar/downloads.py e senhas_csv.py (prepara o CSV do Chrome para o KeePassXC sem mostrar senhas)
- Bot do Telegram: tools/remoto/bot.py (só o meu chat, comandos fixos)
- Financeiro local: tools/financeiro/financeiro.py iniciar | importar | mes (dados em ~/financas)
- Investimentos: tools/investimentos/investimentos.py iniciar | avaliar CLASSE CSV | aporte carteira.csv 800 | comparar carteiras.csv
- Certificações e recursos: tools/carreira/certificacoes.py e tools/recursos/recursos.py (geram os docs)
- Esteira de sites: infra/templates/esteira-site (ficha como issue, workflow qualidade, LEIA.md)
- Lucro por ferramenta: tools/roi/roi.py (dados em ~/financas/roi.toml)
- Jarvis: tools/jarvis/politica.py (validar | decidir | expor | ha-yaml) com modelo em politica.example.toml; tools/jarvis/falar.py (hook Stop do Claude Code); infra/jarvis (voz, MQTT e perfis zigbee e cameras)
- Construção: tools/construcao/ifc_resumo.py ARQUIVO.ifc [--json]; regras da IA em infra/templates/regras-ia/construcao.md
- Orçamento: tools/custos/orcamento.py ~/financas/orcamento.toml (só dev/protótipo, por etapa); economia de tokens: tools/ia/tokens.py rota "tarefa" e docs/ia/tokens.md
- Versões/tags: tools/git/taguear.py --criar --push (no notebook, após git fetch --unshallow); boas práticas em docs/boas-praticas.md
- Segurança: tools/seguranca/escopo.py (validar | checar | rodar), cvss.py VETOR, relatorio.py ESCOPO ACHADOS; modelos em infra/templates/seguranca; lab em infra/lab-seguranca; scripts/wsl/ferramentas-re.sh (Ghidra, GhidraMCP, ILSpy)
- Calculadora de modelos: tools/ia/cabe.py 32 ou cabe.py --hf DONO/MODELO (lê o tamanho no Hugging Face)
- Rotinas: scripts/wsl/resumo-manha.sh, manutencao-semanal.sh, agendar.sh --aplicar
- Padrão de elite: scripts/wsl/padronizar-repo.sh --todos, segredos.sh, teste-restauracao.sh, regras-ia.sh
- Serviços Docker: infra/automacao (n8n, Grafana...), infra/ia (gateway LiteLLM), infra/casa (Home Assistant, Paperless, Grocy), infra/rede (AdGuard), infra/dados (Metabase)

## 6. Fases do roteiro
| # | Fase | Quando | Passos |
|---:|---|---|---:|
| 0 | Diagnóstico: o que você já tem | Antes de tudo · semana 1 (out/2026) | 6 |
| 1 | Preparar | Semana 1 · out/2026 | 4 |
| 2 | Senhas: recuperar, trocar e guardar | Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026 | 16 |
| 3 | Windows | Semana 1 · out/2026 | 9 |
| 4 | Linux (WSL2) | Semana 2 · nov/2026 | 10 |
| 5 | GitHub e CI | Semana 2 · nov/2026 | 5 |
| 6 | Agentes de IA | Semana 2 · nov/2026 | 7 |
| 7 | Backup e segurança | Semana 3 · nov/2026 | 4 |
| 8 | Acervo: tudo o que você já tem | Semanas 3 e 4 · nov/2026 | 7 |
| 9 | Claude e assistentes | Semana 4 · nov/2026 | 4 |
| 10 | Automação e medição | Semana 4 · nov/2026 | 8 |
| 11 | Arsenal de rendas: regras e as 3 de agora | Semana 4 · nov/2026 | 8 |
| 12 | Automações do arsenal | Nov/2026 em diante, uma por vez, na ordem de desbloqueio | 12 |
| 13 | Kit de sites com IA da Hostinger | Semanas 4 e 5 · nov/2026 | 5 |
| 14 | Escola: Fábrica de aulas e documentos | Semanas 5 e 6 · nov/2026 | 9 |
| 15 | Departamento financeiro pessoal | Dez/2026 | 8 |
| 16 | Investimentos com as suas metodologias | Dez/2026 | 11 |
| 17 | Rotina automatizada | Semana 4 · nov/2026 | 5 |
| 18 | Comandos remotos pelo Telegram | Semana 5 · nov/2026 | 5 |
| 19 | Casa e vida | Dez/2026 | 6 |
| 20 | Padrão de elite em todo repositório | Semana 5 · nov/2026 | 10 |
| 21 | Empresa solo: o contexto mestre no setup | Semana 5 · nov/2026 (tudo grátis, em sessões curtas); o analisador lógico entra com a primeira compra de robótica | 18 |
| 22 | Núcleo AMtech: o setup conectado e autônomo | Nov/2026 a abr/2027, uma fase por vez, dentro das 7 h extras por semana; fases 0 e 1 primeiro, o garimpo logo depois | 12 |
| 23 | Agentes e IA com qualidade medida | Semana 6 · nov/2026 a dez/2026 | 15 |
| 24 | Roteador de agentes e esteira de sites | Semana 6 · nov/2026 a dez/2026 | 9 |
| 25 | Modelos grandes sem computador maior | 2027, depois do primeiro fine-tuning de 8B | 6 |
| 26 | Rede própria entre os seus computadores | Semana 6 · nov/2026 | 6 |
| 27 | Operação 24 horas | Dez/2026 a jan/2027 | 8 |
| 28 | Soberania: serviços próprios na VM | Dez/2026 a jan/2027 na VM grátis da Oracle, depois da Operação 24 horas; VPS e VM paga quando uma renda pagar | 13 |
| 29 | Dados e crescimento: medir, testar e vender mais | Com a primeira página de venda no ar (jan/2027) e por etapas | 13 |
| 30 | Pipeline de conteúdo | Semana 5 · nov/2026 | 7 |
| 31 | Estúdio de conteúdo | Semana 5 · dez/2026 | 5 |
| 32 | Contas, canais e sites | Semanas 6 e 7 · dez/2026 | 14 |
| 33 | Vendas e finanças no CPF | Semanas 8 a 10 · dez/2026 a jan/2027 | 20 |
| 34 | Vendas medidas | Semana 11 · jan/2027 | 4 |
| 35 | Teste do núcleo | Semana 11 · jan/2027 | 4 |
| 36 | Primeira venda: o mini-curso no ar | Semanas 12 a 15 · jan a fev/2027 | 9 |
| 37 | Base dos sistemas AM | Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 | 9 |
| 38 | Nuvem e deploy | Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) | 8 |
| 39 | Editora | Quando o capítulo 1 estiver pronto | 11 |
| 40 | Dados, IA e pendrives | Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) | 12 |
| 41 | Sprint de 14 dias (Estratégia do Halter) | Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) | 10 |
| 42 | Mais ofertas, uma por vez | Fev a dez/2027, uma oferta por vez | 23 |
| 43 | Marketing pago e crescimento | A partir de fev/2027 | 11 |
| 44 | Linux nativo e laboratório completo | 2027, conforme cada compra | 7 |
| 45 | IA dentro dos sistemas AM | Depois do Passo 9 e do IA0 da Trilha de Dados e IA (≈ 2028), junto do IA5 | 1 |
| 46 | Sistemas AM à venda | 2027 | 5 |
| 47 | CNPJ e formalização | Quando a renda pedir | 5 |
| 48 | Agentes do grupo | Junto com o primeiro CNPJ | 7 |
| 49 | Editora: depois do primeiro livro | Depois do primeiro livro | 5 |
| 50 | Distribuído, plataforma e segunda nuvem | 2028 | 6 |
| 51 | Infraestrutura própria | 2028, quando o grupo pedir | 3 |
| 52 | Negócios do grupo em Barbacena | Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano | 11 |
| 53 | Estudo contínuo | Contínuo, desde a semana 2 | 14 |
| 54 | Engenharia reversa, AppSec e pentest | Dez/2026 em diante: 1 bloco de 1 h por semana dentro do estudo da manhã; serviços pagos só depois dos portões (eJPT, ensaio, OSCP) | 21 |
| 55 | Jarvis: o setup e a casa por comando de voz | Voz no PC e política em dez/2026; servidor da casa e cada aparelho conforme a compra (2027); orquestrador depois da Operação 24 horas | 13 |
| 56 | Hugging Face e IA física: TI, casa inteligente e agropecuária | Modelos em dez/2026 (nada a comprar); SO-101 na primeira compra de robótica de 2027; Reachy Mini e LeKiwi depois do primeiro treino | 16 |
| 57 | Construção civil, arquitetura e engenharia civil (pela TI) | Ferramentas grátis no estudo da manhã a partir de jan/2027; serviços e o AM Obra só depois das rendas de agora passarem no portão | 13 |

## 7. Minhas pendências (ver também ESTADO.md)
1. Senhas: passo kp-organizar, depois 2.4 (exportar do Chrome, importar no KeePassXC, apagar os CSVs, copiar o cofre para o pendrive).
2. ActivityWatch (PowerShell: winget install --id ActivityWatch.ActivityWatch -e) e cadastro na avaliação de IA (passo ar-ia).
3. Confirmar hora mínima R$ 45 e teto de 7 h.
4. Templates do Rei dos Sites: comprei? onde estão os arquivos? (repositório só privado e só se a licença permitir).
5. Modelos .docx da escola e uma ementa para a Fábrica.
6. Mesa (passo 1.2) e trocas de assinatura (ct-cortes, ia-segunda).
7. GitHub Education como professor (ag-ghed) e token da Hostinger (ag-hostinger-mcp): destravam a esteira de sites.
8. investimentos.toml e os 4 CSVs de indicadores (inv-politica, inv-indicadores, inv-sena).

## 8. Como pedir ajuda numa conversa nova
1. Cole este arquivo e o pacote do passo: `python3 ~/dev/dev-setup/tools/sessao/contexto.py --passo ID | clip.exe`.
2. Peça ao Claude para abrir o repositório AlanMateus17/dev-setup (GitHub conectado) e, ao terminar, marcar o passo no Acompanhamento.
3. Foco: executar o roteiro na ordem. Ideias novas podem entrar no setup a qualquer momento (dados, gerador, teste, CHANGELOG, CI).
