# ESTADO do setup (memória curta entre conversas)

Cada conversa termina com até 5 linhas aqui: o que foi decidido, o que ficou pendente. Mais recentes no fim.
O pacote de contexto (tools/sessao/contexto.py --resumo) lê as últimas linhas daqui.

- 2026-11-01: arsenal de 100 rendas, 20 automações, 69 softwares, kit de sites, ferramentas do dia a dia, padrão de elite, IA medida, rede própria, operação 24 h e custos no repositório.
- 2026-11-01: pendente do Alan: senhas (passo 2.4), ActivityWatch, cadastro na avaliação de IA, Rei dos Sites (comprou? onde estão?), modelos .docx da escola, confirmar R$ 45 e 7 h.
- 2026-11-01: regra nova: uma conversa por tarefa, começando com o pacote de contexto.
- 2026-11-01: segunda IA barata decidida: Google AI Plus no lugar do Google One, ChatGPT Go grátis pelo Nubank, DeepSeek/OpenRouter só para rascunho sem dado sensível; Grok cortado; Claude Max só quando uma renda passar no portão.
- 2026-11-01: dados e crescimento, ferramentas do Akita (ai-memory 2.0, ai-usagebar, Strata para o futuro) e operação 24 h no roteiro. Regra: parar de adicionar áreas e executar até a primeira venda.
- 2026-11-01: harumakis/congelados retirados do plano. Documentos da escola e TCC: verificador ABNT automático (próxima renda, 7ª) e conferência para escolas (fila).
- 2026-11-01: passos que faltavam adicionados (revisão de fim de ano, robótica 41+, posts do setup, EBTT, Licenciatura). CONTINUAR.md completo. Próxima conversa começa pelo kp-organizar (senhas).
- 2026-11-01: v2.0: roteador de agentes (primária, reserva e portão por tarefa) e esteira de sites (issue → Copilot → PR → prévia → aprovação → Hostinger). Auditoria em docs/recursos.md. OpenClaw só isolado na VM e depois da esteira entregar um site. Maior lacuna: verificação de professor no GitHub Education (ag-ghed).
- 2026-11-01: v2.1: investimentos (metodologias por script, ARCA dentro de ações, carteira por metodologia contra o índice) e certificações (CNPI primeiro para recomendar; AZ-204 → AI-200). Alan pediu para não travar ideias novas: a regra de parar de adicionar áreas saiu.
- 2026-11-01: v2.2: todas as metodologias ao mesmo tempo nas 4 classes do ARCA (27 metodologias), consenso por ativo e aporte em dois níveis com mínimo de R$ 100 por compra. Pendente do Alan: preencher investimentos.toml (portão, ARCA, NTN-B do mês) e os 4 CSVs de indicadores.
- 2026-11-02: v2.3 a v2.5.1: segurança (engenharia reversa, AppSec, pentest com escopo.py, cvss.py, relatorio.py), Jarvis por voz (politica.py, falar.py, infra/jarvis, ADR 0004) e catálogo do Hugging Face com foco em TI, casa inteligente e agropecuária (cabe.py --hf).
- 2026-11-02: v2.6: construção civil pela TI (docs/construcao, regras da IA para engenharia, ifc_resumo.py, fase 53); auditoria: regras "Nunca" do pacote de contexto corrigidas e artefatos sincronizados.
- 2026-11-02: regras novas: nenhum teste sem termo no escopo.py; destrancar, abrir janela e desligar geladeira só com ok no celular; nada de projeto, laudo, ART ou RRT assinado por IA ou por Alan.
- 2026-11-02: compras em ordem: servidor da casa → kit de campo e Zigbee → SO-101 + 2 câmeras → satélite ESP32-S3 → câmeras → Reachy Mini → LeKiwi; GPU de 12 GB só depois do portão.
- 2026-11-02: próximo sem comprar nada: jv-claude-voz, jv-voz, hf-coder e sg-ferramentas. Pendente do Alan: termo de autorização com advogado antes do 1º laudo pago; licença educacional da Autodesk.
- 2026-11-02: v2.7: lab de alvo isolado (containers e VMs) para estudar e atacar software só na própria máquina; orçamento (orcamento.py, só dev/protótipo); economia de tokens (tokens.py + docs/ia/tokens.md: peça o script, não o resultado).
- 2026-11-02: v2.7.1: economia de tokens generalizada (docs/ia/tokens.md: tabela por tipo de saída, por voz/escrito/arquivo) e regra "assuma padrões, o Alan corrige o que estiver errado" nas regras da IA.
- 2026-11-02: v2.8: plano de financiamento (docs/operacao/08-financiar-o-setup.md): renda de TI primeiro (sem compra), cada marco de renda libera uma compra pela cascata; hardware caro (robótica, casa, GPU) é desejo e só entra com sobra. Versões no CHANGELOG; push de tag não é aceito por esta sessão.
- 2026-11-02: v2.9: tools/git/taguear.py (tag de todas as versões do CHANGELOG de uma vez, no notebook) e docs/boas-praticas.md (git, versões, tags, segurança, qualidade, backup, licenças); passo el-tags. Tags não enviam por esta sessão: rodar no notebook com git fetch --unshallow.
- 2026-11-02: v2.10: tag automática no push (hook scripts/git-hooks/pre-push + taguear.py --ultima); ligar com git config core.hooksPath scripts/git-hooks. Daqui ainda não envia tag; no notebook, sim.
- 2026-11-06: v2.11: contexto mestre da empresa solo integrado (docs/empresa-solo.md): justfile como porta única, tools/triagem (montar, colar ou construir; pacote do arquiteto), ADR 0005 Kamal em VM e ADR 0006 Zod só no front; 17 decisões novas em fora-do-setup.
- 2026-11-06: stack fixa mantida (.NET 10); o cronograma de 14 dias virou as ofertas automacaoia (Chatwoot) e rendara (planilha primeiro), ambas na fila; venda segue no CPF. .claudeignore não existe: vale permissions.deny no .claude/settings.json.
- 2026-11-06: próximo: fase Empresa solo (rodar o bootstrap, just check, triagem antes de qualquer ideia nova). Pendências do Alan continuam as mesmas (senhas, ActivityWatch, R$ 45 e 7 h).
- 2026-11-06: v2.11.1: delta dos 5 módulos absorvido (sala limpa no lab, link do grep.app no arquiteto); Soft Serve, monorepo, VM paga na AWS/Azure agora, Astro, Plausible, Plunk, Akaunting e HeyForm ficaram de fora com motivo.
- 2026-11-06: v2.12: TODAS as ferramentas do contexto mestre entraram, cada função com principal e reserva (ADR 0008); nenhuma linguagem proibida (ADR 0007). Fases novas: Soberania (VM, dez/2026) e Sprint de 14 dias (recesso de jan/2027).
- 2026-11-06: trocas: mise no lugar do fnm, Zellij do tmux, chezmoi nos dotfiles, GlitchTip e SigNoz, Astro nos sites, HeyForm, Formbricks, Beancount e Portfolio Performance. Pago liga com renda. Próximo: bootstrap.sh, extras.sh e chezmoi (passos solo-*).
- 2026-11-06: v2.13: Núcleo AMtech decidido (ADR 0009): conectar as ferramentas, não reescrever; tokens mínimos com sops/age na VM; IA dos agentes até US$ 20/mês; garimpo como fase 2. Fase 0 pronta (just instalar, backup diário, manutenção real) e fase 1 começada (tools/nucleo, triagem gravando na base).
- 2026-11-06: próximo: no notebook, just instalar --simular → just instalar → nuc-backup; depois a fase 2 (garimpo) numa conversa nova. Objetivo do Alan: máximo de renda com menos horas e as empresas do grupo.
- 2026-11-06: v2.14: Painel do Núcleo publicado (https://claude.ai/artifact/Frwo8DGEdifkeVcCKdtTAo), gerado dos dados; Implantação, Mapa, Portfólio e Ecossistema republicados. O Plano de automação (documento de 31/10) ficou antigo: o Núcleo o substitui.
- 2026-11-06: v2.15: começa a instalação. Primeira empresa: AMtech Software (desenvolvimento), no CPF até o ponto de virada combinado com o contador (MEI impossível no CNAE 6201-5/01).
- 2026-11-06: o setup diz o que é manual: just agora software (próximos passos), just decisoes software (10 decisões), just feito ID, just progresso software.
- 2026-11-06: pendente do Alan: rodar just instalar --simular e depois just instalar; marcar com just feito as fases já feitas; tomar as 10 decisões da empresa.
- 2026-11-06: v2.16: Escola Akita. O blog do Akita (831 posts, 198 Akitando com transcrição) vem por git, fica só local; notas no Obsidian, regras com outras palavras e link; nada muda sem aprovação (just akita pendentes).
- 2026-11-06: pendente do Alan: decidir as 22 regras do piloto e o motor (Claude ou Ollama) para gerar as notas dos outros 829 posts.
- 2026-11-06: v2.17: eixo profundo = software + finanças, pelo Grupo AMtech Digital (ADR 0011). Plano de 12 meses em docs/plano-eixo.md; o resto pausado até o fim do trimestre 4.
- 2026-11-06: v2.18: Professor do setup (ADR 0012): just professor hoje | aula | prova | corrigir; 19 módulos do T1; aula-modelo em docs/professor/exemplo-aula-s-backup.md.
- 2026-11-06: v2.19: método do Professor em docs/professor/metodo.md (ciência + metodologias das conversas: protocolo de fim de bloco, ficha dupla, N1-N4, 20/80); just professor fechar ID MINUTOS.
- 2026-11-06: v2.20: Alura (assistir antes) e VHSlins (ler antes) ligados aos módulos; trilhas de matemática e física; semana fixa no just professor hoje; aula termina com roteiro para dar a aula.
- 2026-11-06: v2.21: posts do Akita escolhidos por módulo no Professor; regras aprovadas entram no núcleo; podcasts viram nota de escuta (just professor escutei); bug das tags do índice do Akita corrigido.
- 2026-11-06: v2.22: um vault só (ADR 0013): o seu Portfolio-AMS-Obsidian-Vault em ~/dev/notas, com o dev-setup espelhado na pasta 11 (just vault-espelho); plano mestre = eixo + Professor.
- 2026-11-07: v2.23: sites das 3 empresas prontos pelo modelo Astro (just site amtech|instituto|editora; --checar mostra o que falta); roteiro por empresa (just agora instituto|editora); docs/empresas/README.md.
