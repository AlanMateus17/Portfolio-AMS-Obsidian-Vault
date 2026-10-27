---
name: livro-logica-e-maquina
description: Livro didático de TI que Alan está criando, "Lógica e Máquina", inspirado na arquitetura dos livros do VHSlins — estrutura em 5 volumes, identidade visual erudita definida, Capítulo 1 do Volume 1A já escrito
sources: [chat]
aliases: [Lógica e Máquina, livro de TI, livro fullstack]
---
- [stated] Título: "Lógica e Máquina", subtítulo "Do raciocínio lógico ao código — fundamentos de Tecnologia da Informação, da Matemática à Máquina", por Alan Mateus
- [stated] Livro didático de Tecnologia da Informação, inspirado na arquitetura dos livros do VHSlins (Matemática Básica, Física Básica, Cálculo), cobrindo tudo que estuda hoje e pretende estudar
- [stated] Público-alvo: adolescentes do ensino médio, alunos de faculdade e profissionais/professores da área
- [stated] Quer que o livro sirva a todo tipo de estudante e leitor, incluindo quem estuda para concursos com TI (ex.: área militar)
- [stated] Quer o livro autocontido: toda matemática e física ligada à TI explicada dentro dele, com livro e exercícios resolvíveis sem precisar estudar Matemática Básica, Física Básica ou Cálculo do VHSlins
- [stated] Concursos-alvo do livro: PF, PRF e áreas de TI das Forças Armadas
- [stated] Quer um único livro com um caminho só (sem trilhas por perfil): todos os leitores fazem todos os exercícios e a proposta, e ao terminar cada capítulo têm domínio total do assunto para qualquer prova/concurso e para trabalhar em TI como dev, engenheiro ou cientista
- [stated] Sem pressa para terminar — projeto de estudo e aprendizado de como desenvolver um livro didático, não uma corrida
- [stated] Estruturado em 5 volumes: Vol. 1A (Lógica + Arquitetura/POO), Vol. 1B (Estruturas de Dados e Algoritmos), Vol. 2 (Banco de Dados + Backend), Vol. 3 (Frontend + Infraestrutura), Vol. 4 (Grafos + Sistemas Distribuídos + Teoria dos Números + Segurança/Pentest), Vol. 5 (Estatística + Álgebra Linear + Cálculo + IA/Analytics)
- [stated] Identidade visual erudita/clássica: papel creme, tinta escura, cor verdigris e latão, tipografia Cormorant Garamond/EB Garamond/IBM Plex Mono; código e diagramas tratados como "pranchas técnicas" numeradas
- [stated] Está começando a criar o Volume 1A (Lógica + Arquitetura/POO); Capítulo 1 ("O que é uma Proposição") já escrito como piloto
- [stated] Pretende usar as ementas das disciplinas que leciona para organizar o conteúdo do livro
</content>
- [stated] Também criou um site interativo de exercícios (mesmo título, "Lógica e Máquina") cruzando o livro do VHSlins, os sistemas reais do Aura e a trilha École 42, com bloqueio de gabarito por tentativas e perguntas de compreensão profunda; pretende recriar esse site com um backend de verdade (usando as tecnologias que estuda) mantendo exatamente o mesmo design visual atual do site (paleta escura azul-marinho/dourado/rosa/azul-aço — diferente da identidade clássica papel-creme do livro)
- [stated] Quer expandir o site pra cobrir as 10 partes do livro (735 exercícios), com vídeo-aulas por seção e emissão de certificado ao final de cada trilha (livro/Aura/École 42); decidiu que o certificado deve existir tanto por Parte individual quanto um certificado consolidado cobrindo o livro inteiro por trilha
- [stated] Decidiu construir o site como sistema Aura: frontend primeiro (Next.js/TypeScript/Tailwind, nome de repo "am-mentor"), backend depois (C#/.NET); frontend já escaffoldado com o mesmo design visual do protótipo
- [stated] Decidiu que o site será construído primeiro só para uso próprio, já pensando em arquitetura que facilite disponibilizar depois para seus alunos (ex: multiusuário, turmas, dashboard de professor ficam para depois, não bloqueiam o uso pessoal agora)
- [stated] Projeto am-mentor já existe localmente em C:\Users\alanmateus\Desktop\am-mentor, com node_modules instalado; stack observada inclui Next.js, TypeScript, Tailwind, katex (renderização de matemática), jspdf (geração de PDF, provavelmente para os certificados), gray-matter (frontmatter markdown) e vitest (testes)
