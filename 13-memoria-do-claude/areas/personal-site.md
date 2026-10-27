---
name: personal-site
description: Migração do site pessoal (alanmateus17.github.io, hoje em Jekyll) para a stack própria de Alan
sources: [chat]
aliases: [alanmateus17.github.io, site pessoal]
---
- [stated] Decidiu migrar o site pessoal (hoje Jekyll/GitHub Pages) para sua própria stack: frontend em Next.js/TypeScript/Tailwind (hospedado na Vercel) + backend em ASP.NET Core com Clean Architecture (Docker num VPS) + PostgreSQL + Redis
- [stated] Quer que toda a lógica do sistema seja desenvolvida por ele mesmo, sem serviços terceirizados (substituindo Formspree, CounterAPI, Decap CMS, GoatCounter e MailerLite por lógica própria)
- [stated] A hospedagem em nuvem (Vercel/VPS alugado) é aceitável — a exigência de "nada terceirizado" é sobre a lógica das funcionalidades, não sobre a infraestrutura de hospedagem em si
- [stated] Fechou a lista de conteúdo novo a adicionar ao portfólio: página "Agora" (o que está construindo no momento), página "Setup" (hardware/ferramentas), estudo de caso por sistema (problema, arquitetura, decisões), painel de atividade do GitHub ao vivo, diagrama do ecossistema Aura, writeups de segurança (eJPT/OSCP), e página "como este site funciona" pós-migração
- [stated] Direção visual da migração fechada: estética terminal/futurista escura, com fundo de partículas ("aura") que reage ao cursor, efeito de decodificação no título e paleta de comando (Cmd+K) para navegação
- [stated] Antes planejava remover o blog deste site (separado, possivelmente no Instituto AMS); em out/2026 decidiu manter o blog junto na migração "por enquanto"; escopo do portfólio: o que está estudando, projetos pessoais e currículo pra download
- [stated] Currículo terá download em PDF, Word e Markdown, mantidos como arquivos separados por ele mesmo (não gerados automaticamente de uma fonte única)
- [stated] Na rodada atual de atualização dos sites, apenas o blog e o portfólio serão modificados; o sistema AM Mentor (Lógica e Máquina) não precisa de nenhuma alteração
- [stated] (out/2026) Escolheu o template Magic UI Portfolio (Next.js) no tema escuro do Aura Design System para migrar o site inteiro; quer o site com a identidade visual da Grupo AMtech Digital, não as cores antigas do site
