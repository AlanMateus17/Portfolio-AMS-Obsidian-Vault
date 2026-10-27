# Plataforma de cursos — Especificação funcional v1

Oct 6, 2026 · @Alan Mateus

## Decisão

**Os dois modos cabem num sistema só, desde que tudo seja organizado em Escolas.** Uma Escola é um espaço separado: marca, cursos, alunos, vendas e configurações próprios. Nada de uma escola aparece na outra.

- **Modo vitrine (estilo Udemy/Rocketseat):** o **Instituto AMS** é a sua escola. Você convida professores para publicar dentro dela, com a sua marca, e divide a receita.
- **Modo escola própria:** o professor de artes cria a **Escola de Artes da Ana**, com logo, cores e endereço dela (`ana.suaplataforma.com.br` ou domínio próprio). Os alunos dela só veem aquela escola. A física básica de outro professor nunca se mistura.
- **Ponte entre os dois:** cada escola pode, se quiser, listar cursos na **Vitrine geral** da plataforma para ganhar alunos novos.

Esta especificação **substitui** o documento "Professores parceiros": tudo o que estava lá está aqui, reorganizado.

**Sendo honesto sobre o tamanho:** isto é um produto do porte de Hotmart Club ou Teachable. A base com Escolas entra no primeiro dia, porque acrescentá-la depois é reescrever o banco. As funcionalidades, em quatro entregas (R1 a R4). A R1 é só a sua escola, vendendo o Catálogo do HTML.

## Como se organiza

&#91;embedded content: organização · plataforma, escolas, vitrine e a hierarquia de um curso\]

A conta é da plataforma; cursos, alunos e vendas são da escola. A vitrine é uma janela opcional: a Ana pode deixar os cursos dela só no endereço dela.

## Organização dos cursos

**Cada curso tem um lugar fixo (área → categoria) e várias etiquetas (tecnologias e temas).** É isso que resolve "matéria" × "tecnologia": *Lógica de Programação* é uma matéria que pode ser ensinada com *JavaScript* ou *Java*, e o aluno acha o curso pelos dois caminhos.

| Nível | O que é | Exemplo | Quantos por curso | Quem define |
| --- | --- | --- | --- | --- |
| **Área** | Grande campo do conhecimento | Tecnologia, Exatas, Linguagens, Artes, Negócios | 1 | Plataforma (lista fixa) |
| **Categoria** | Matéria ou especialidade dentro da área | Tecnologia → Desenvolvimento Web, Banco de Dados, Hardware; Exatas → Matemática, Física | 1 | Plataforma; professor pede uma nova |
| **Tecnologias e temas** | Etiquetas para filtrar e buscar | HTML, CSS, JavaScript, C#, Java, SQL, ENEM, Álgebra | até 8 | Lista da plataforma com sinônimos ("JS" = JavaScript); professor sugere |
| **Nível** | Para quem é | Iniciante, Intermediário, Avançado | 1 | Professor |
| **Formato** | Como o curso funciona | Gravado, ao vivo, misto; com ou sem certificado | 1 | Professor |

Acima dos cursos ficam duas formas de agrupar:

- **Trilha (formação):** sequência ordenada de cursos para um objetivo, com etapas e **certificado final da trilha**. Ex.: *Técnico em Desenvolvimento de Sistemas* com as 13 matérias na ordem certa; *Desenvolvedor Web Fullstack .NET* com HTML → CSS → JavaScript → C# → SQL → ASP.NET. O aluno vê onde está e qual é o próximo passo.
- **Coleção:** vitrine editorial sem ordem nem certificado. Ex.: *Comece por aqui*, *Grátis*, *Para o ENEM*.

Por que a lista é fechada: se cada professor criar categorias, em seis meses existem "Programação", "programação web" e "Dev" separadas, e o aluno não acha nada. A escola própria pode criar **coleções e trilhas** livremente, mas usa as áreas e categorias da plataforma.

## Estrutura padrão de um curso

**A estrutura Trilha → Curso → Módulo → Aula → Blocos está correta e é a mesma das grandes plataformas.** Faltavam cinco peças que elas têm; agora entram como padrão.

| Nível | O que tem (padrão da plataforma) |
| --- | --- |
| **Trilha** | Objetivo de carreira, cursos em etapas, **projeto final da trilha**, certificado da trilha |
| **Curso** | Página de venda, boas-vindas, módulos, **projeto final do curso**, certificado |
| **Módulo** | **Objetivo do módulo** em uma frase, aulas, **prova do módulo** e/ou **projeto do módulo**, resumo |
| **Aula padrão** | 1. Objetivo → 2. Vídeo (com **capítulos** e **transcrição**) → 3. Texto de apoio → 4. **Pratique** (faça o que o vídeo fez) → 5. Exercícios → 6. Materiais → 7. **O que você aprendeu** (3 pontos) |
| **Projeto** | Enunciado, resultado esperado, **critérios de correção (rubrica)**, entrega, correção do professor por critério, refazer |

A aula padrão é um **modelo**, não uma obrigação: o editor já abre a aula nova com esses blocos vazios, e o professor apaga o que não usar.

**O que pegamos de cada uma** (pelo que conheço dessas plataformas; vale conferir as versões atuais):

| Ideia | De onde | Na nossa plataforma |
| --- | --- | --- |
| Formações com etapas e certificado próprio | Alura, Rocketseat | Trilha (CAT-07) |
| "Faça como eu fiz" depois do vídeo | Alura | Bloco **Pratique** na aula padrão |
| "O que aprendemos?" no fim da aula | Alura | **O que você aprendeu** (JOR-02) |
| Transcrição do vídeo | Alura | Novo: EST-03 |
| Projetos práticos e desafios no fim de cada etapa | Rocketseat | **Projeto do módulo** com rubrica (EST-04) |
| Recursos para baixar por aula | Udemy | Aba Materiais (ALU-02) |
| Perguntas e respostas por aula | Udemy | Dúvidas (COM-01) |
| Anotações com o tempo do vídeo | Udemy | ALU-05 |
| Simulados | Udemy | Prova do módulo + banco de questões (AVA-03, AVA-08) |
| Correção automática no servidor e revisão espaçada | **Nossa** (nenhuma das três faz igual) | Já existe |

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| EST-01 | Aula nova abre com os blocos da aula padrão | R1 |
| EST-02 | Objetivo do módulo e resumo do módulo | R1 |
| EST-03 | Capítulos no vídeo e transcrição (Bunny gera legenda automática; o professor revisa) | R2 |
| EST-04 | Projeto com rubrica: critérios, pontos por critério, correção e refazer | R2 |
| EST-05 | Projeto final do curso e da trilha | R2 |

## Jornada do aluno

**Fora do curso, o aluno explora; dentro do curso, só estuda.** A plataforma tem dois modos de tela, e a troca entre eles é clara.

| Etapa | O que o aluno vê | O que fica de fora |
| --- | --- | --- |
| **1. Primeira visita** | Promessa da escola em uma frase, busca em destaque, áreas em cards grandes, botão **"Por onde começar?"**: 3 perguntas (objetivo, nível, horas por semana) que indicam uma trilha ou um curso | Pop-up de cadastro antes de ver qualquer coisa; carrossel automático |
| **2. Explorar** | Área → categoria → lista de cursos; filtros à esquerda (nível, duração, preço, grátis, tecnologia, certificado); **card padrão**: capa, título, professor, nível, duração, nota, preço. Busca entende sinônimos e erros ("javascrip") | Mais de 7 informações por card; selos piscando |
| **3. Decidir** | Página do curso: o que vai conseguir fazer ao final, **para quem é e para quem não é**, pré-requisitos com link ("faça antes: Lógica"), ementa que abre por módulo, aulas de amostra, professor, avaliações, garantia de 7 dias, **um botão de compra** fixo no rodapé no celular | Contador de urgência falso, "só hoje" eterno |
| **4. Começar** | Boas-vindas do professor (vídeo curto), meta semanal escolhida pelo aluno (ex.: 3 aulas), lembrete opcional, **primeira aula a 1 clique** | Tour de 10 telas; formulário longo |
| **5. Estudar (modo foco)** | O cabeçalho troca: some a vitrine, ficam só o curso, o progresso e "Sair do curso". Cada aula abre com **o objetivo dela em uma frase**; aulas de 5 a 15 min; lateral do módulo recolhível; tela cheia com a tecla F; no fim, resumo em 3 pontos + botão da próxima | Recomendações de outros cursos, promoções, notificações em tempo real (ficam agrupadas no sino) |
| **6. Voltar** | A página inicial do aluno logado começa por **Continuar** (aula exata onde parou), depois Meus cursos, depois o próximo passo da trilha. A vitrine fica numa aba ao lado. E-mail de lembrete leva direto à aula | Vitrine como primeira tela para quem já é aluno |
| **7. Concluir** | Certificado, pedido de avaliação, **próximo curso da trilha** (só aqui entra recomendação) | Venda agressiva antes de mostrar o certificado |

O modo foco usa a marca da escola, mas o **layout é o mesmo em todas as escolas e cursos**: quem faz um curso de artes e um de física não precisa reaprender onde fica nada.

## Distrações proibidas

Estas regras valem para qualquer escola, inclusive as próprias. O sistema simplesmente não oferece o recurso.

1. **Nenhuma venda no modo foco:** sem banner, oferta ou "você também vai gostar" enquanto o aluno estuda.
2. **Nada toca sozinho fora do curso:** a próxima aula pode começar sozinha; outro curso, nunca.
3. **Sem truques de venda:** contagem regressiva falsa, "últimas vagas" inventadas, cancelamento escondido, caixa já marcada.
4. **Notificações em lote:** dentro do curso só aparece, discretamente, "sua dúvida foi respondida". O resto espera no sino.
5. **Gamificação sóbria:** progresso, meta semanal e sequência de dias. Ranking público só se a escola ligar, porque comparação desanima o iniciante.
6. **Movimento mínimo:** sem animações chamativas; o sistema respeita quem pede "reduzir movimento" no celular ou computador.
7. **Um objetivo por aula:** aula longa demais aparece como aviso para o professor no editor (sugestão de dividir acima de 20 min).

### Requisitos novos

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| CAT-01 | Áreas e categorias da plataforma, gerenciadas pelo admin | R1 |
| CAT-02 | Etiquetas de tecnologia e tema, com sinônimos | R1 |
| CAT-03 | Classificação obrigatória para publicar: área, categoria, etiquetas, nível, formato | R1 |
| CAT-04 | Catálogo por área e categoria, com filtros e card padrão | R1 |
| CAT-05 | Coleções editoriais (Comece por aqui, Grátis) | R1 |
| CAT-06 | Busca com sinônimos e tolerância a erros de digitação | R2 |
| CAT-07 | Trilhas: cursos em ordem, etapas, progresso e certificado da trilha | R2 |
| CAT-08 | Pré-requisitos entre cursos, com link para o curso anterior | R2 |
| CAT-09 | "Por onde começar?": 3 perguntas que recomendam trilha ou curso | R2 |
| CAT-10 | Professor pede categoria ou etiqueta nova; admin aprova | R2 |
| JOR-01 | Modo foco: cabeçalho do curso sem vitrine nem ofertas | R1 |
| JOR-02 | Objetivo da aula no topo e resumo no fim | R1 |
| JOR-03 | Página inicial do aluno logado começando por **Continuar** | R1 |
| JOR-04 | Tela cheia (tecla F) e lateral recolhível | R1 |
| JOR-05 | Respeitar "reduzir movimento" do aparelho | R1 |
| JOR-06 | Boas-vindas do curso com meta semanal | R2 |
| JOR-07 | Notificações agrupadas e silêncio no modo foco | R2 |
| JOR-08 | Lembretes por e-mail com link direto à aula; o aluno escolhe a frequência | R2 |
| JOR-09 | Recomendação de outro curso só ao concluir | R2 |

## Papéis

O papel vale **por escola** e, para quem ensina, **por curso**. A mesma pessoa pode ser aluna numa escola e professora em outra; um seletor no topo troca de escola, como no Slack.

| Papel | Quem é | O que vê e faz |
| --- | --- | --- |
| Visitante | Sem conta | Vitrine, páginas de venda, aulas de amostra |
| Aluno | Conta na plataforma, matriculado em cursos | Meus cursos, aulas, atividades, dúvidas, certificados, compras |
| Monitor | Ajudante indicado pelo professor, num curso | Dúvidas e correções daquele curso. Não edita conteúdo nem vê vendas |
| Professor | Autor de um ou mais cursos, numa escola | Editor dos próprios cursos, alunos deles, dúvidas, correções, extrato |
| Dono da escola | Quem criou a escola (no Instituto AMS, você) | Tudo da escola: marca, professores, planos, cupons, vendas, relatórios |
| Admin da plataforma | Você e sua equipe | Todas as escolas: aprovações, comissões, suporte, vitrine geral, auditoria |

Conta é **uma só por pessoa** (um e-mail, uma senha, um 2FA). O que muda de escola para escola são as matrículas e os papéis.

## Requisitos funcionais

82 requisitos em 10 módulos, mais 5 de estrutura (EST, na seção Estrutura padrão) e 19 de catálogo e jornada (CAT e JOR, na seção Distrações proibidas), 18 de venda (VND) e 8 de personalização (PER), nas seções próprias: 132 no total. **Entrega** diz quando cada um entra: R1 sua escola, R2 professores convidados, R3 escolas próprias, R4 crescimento. *(já existe)* marca o que o sistema atual faz e será portado.

### 1. Contas e segurança

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| CON-01 | Cadastro com confirmação de e-mail *(já existe)* | R1 |
| CON-02 | Login com bloqueio por tentativas, 2FA (TOTP) e códigos de recuperação *(já existe)* | R1 |
| CON-03 | Recuperar senha *(já existe)* | R1 |
| CON-04 | Perfil: nome, foto, tema claro/escuro, preferências de e-mail | R1 |
| CON-05 | LGPD: baixar meus dados e apagar conta *(já existe)* | R1 |
| CON-06 | Entrar com Google | R2 |
| CON-07 | Sessões ativas e "sair de todos os aparelhos" | R2 |
| CON-08 | Seletor de escola para quem participa de mais de uma | R3 |
| CON-09 | Passkeys (digital ou rosto) | R3 |

### 2. Escolas

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| ESC-01 | Escola com nome, endereço curto, logo, favicon, cor principal e fonte (de uma lista) | R1 (só a sua) |
| ESC-02 | Página inicial da escola montada com seções prontas: destaque, cursos, professores, depoimentos, perguntas | R1 fixa, R3 editável |
| ESC-03 | Páginas da escola: sobre, termos, privacidade, reembolso | R1 |
| ESC-04 | Convidar professores e monitores para a escola | R2 |
| ESC-05 | Liga/desliga de recursos por escola (ex.: fórum, certificado) | R2 |
| ESC-06 | Criar escola própria: assistente em 5 passos (nome, marca, primeiro curso, pagamento, publicar) | R3 |
| ESC-07 | Subdomínio (`ana.plataforma.com.br`) e domínio próprio com HTTPS automático | R3 |
| ESC-08 | E-mails da escola com nome e marca dela | R3 |
| ESC-09 | Assinatura da plataforma para donos de escola (mensal ou por venda) | R3 |
| ESC-10 | Listar cursos na Vitrine geral, por escolha da escola e com aprovação | R3 |

### 3. Cursos e conteúdo

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| CUR-01 | Curso: título, subtítulo, capa, categoria, nível, carga horária, pré-requisitos, objetivos, público | R1 |
| CUR-02 | Estrutura Curso → Módulo → Aula → Blocos, reordenar arrastando | R1 |
| CUR-03 | Editor de aula por blocos com rascunho, prévia "como aluno" e publicar *(base já existe)* | R1 |
| CUR-04 | Histórico de versões e restaurar *(já existe)* | R1 |
| CUR-05 | Aulas de amostra grátis | R1 |
| CUR-06 | Biblioteca de mídia do professor: vídeos, imagens, arquivos | R1 |
| CUR-07 | Envio de vídeo ao Bunny direto do editor, com barra de progresso | R1 |
| CUR-08 | Liberação programada: aula abre X dias após a matrícula ou numa data | R2 |
| CUR-09 | Módulo só abre após concluir o anterior ou passar na prova | R2 |
| CUR-10 | Modelos de curso por área | R2 |
| CUR-11 | Duplicar curso ou aula; exportar e importar .zip *(exportar já existe)* | R2 |
| CUR-12 | Enviar para revisão antes de publicar | R2 |
| CUR-13 | Vários professores no mesmo curso | R2 |

### 4. Atividades e avaliação

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| AVA-01 | Blocos com correção automática no servidor (ver Menu de blocos) *(parte já existe)* | R1 essenciais + programação, R2 o resto |
| AVA-02 | Explicação por alternativa: o aluno vê por que errou | R1 |
| AVA-03 | Prova do módulo: nota mínima, tentativas, tempo, embaralhar *(checkpoint já existe)* | R1 |
| AVA-04 | Revisão espaçada *(já existe)* | R1 |
| AVA-05 | Regra de conclusão do curso: % de aulas + nota mínima | R1 |
| AVA-06 | Certificado por curso, no modelo da escola, com verificação pública *(já existe, fixo)* | R1 |
| AVA-07 | Correção pelo professor (dissertativa, entrega): nota, comentário, devolver para refazer | R2 |
| AVA-08 | Banco de questões com sorteio na prova | R2 |

### 5. Experiência do aluno

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| ALU-01 | Meus cursos com progresso e **Continuar de onde parei** | R1 |
| ALU-02 | Tela da aula: vídeo grande, abas (Resumo, Atividades, Dúvidas, Materiais), lista lateral do módulo | R1 |
| ALU-03 | Player: velocidade, retomar, próxima aula, conclui com 90% *(já existe)* | R1 |
| ALU-04 | Modo escuro e tamanho de fonte | R1 |
| ALU-05 | Anotações e marcadores com tempo do vídeo | R2 |
| ALU-06 | Busca dentro do curso | R2 |
| ALU-07 | Avaliar o curso (nota + comentário) | R2 |
| ALU-08 | Legendas | R3 |
| ALU-09 | Metas semanais e sequência de dias | R4 |
| ALU-10 | Instalar no celular (PWA) e ler texto sem internet | R4 |

### 6. Comunicação

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| COM-01 | Dúvidas por aula, respondidas por professor ou monitor *(já existe)* | R1 |
| COM-02 | E-mails de transação: boas-vindas, compra, certificado | R1 |
| COM-03 | Central de notificações (sino) | R2 |
| COM-04 | Avisos do curso, no site e por e-mail | R2 |
| COM-05 | E-mails automáticos: aluno parado há 7 dias, carrinho abandonado | R2 |
| COM-06 | Aulas ao vivo (link + gravação depois) | R3 |
| COM-07 | Comunidade ou fórum por curso | R4 |

### 7. Vendas e financeiro

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| VEN-01 | Checkout com Pix, cartão parcelado e boleto | R1 |
| VEN-02 | Curso avulso e assinatura mensal/anual *(planos já existem)* | R1 |
| VEN-03 | Cupons, códigos de acesso e período de teste *(já existe)* | R1 |
| VEN-04 | Reembolso em até 7 dias pelo próprio site | R1 |
| VEN-05 | Pacote de cursos | R2 |
| VEN-06 | Divisão automática do pagamento (split) entre plataforma, escola e professor | R2 |
| VEN-07 | Comissão configurável por escola, professor ou curso | R2 |
| VEN-08 | Extrato do professor e do dono: vendas, taxas, comissão, repasses | R2 |
| VEN-09 | Conciliação diária com o gateway | R2 |
| VEN-10 | Recuperação de carrinho abandonado | R2 |
| VEN-11 | Afiliados com link e comissão | R4 |

### 8. Vitrine geral

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| VIT-01 | Página pública do professor com os cursos dele | R2 |
| VIT-02 | Catálogo com cursos de todas as escolas que optaram: categorias, busca, filtros | R3 |
| VIT-03 | Destaques editoriais e ordenação por avaliação | R3 |
| VIT-04 | Venda pela vitrine credita a escola de origem, com comissão de vitrine | R3 |

### 9. Painéis e relatórios

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| REL-01 | Relatório de estudos do aluno *(já existe)* | R1 |
| REL-02 | Painel do dono: receita, alunos ativos, vendas por curso | R1 básico, R2 completo |
| REL-03 | Painel do professor: vendas, alunos, conclusão por aula, onde os alunos param | R2 |
| REL-04 | Exportar relatórios em CSV | R2 |

### 10. Administração da plataforma

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| ADM-01 | Auditoria de ações *(já existe)* | R1 |
| ADM-02 | Aprovar professores e cursos | R2 |
| ADM-03 | Comissões e limites (armazenamento, minutos de vídeo) | R2 |
| ADM-04 | Entrar como usuário para dar suporte, registrado na auditoria | R2 |
| ADM-05 | Gerenciar escolas: aprovar, suspender, plano | R3 |
| ADM-06 | Denúncias e retirada por direito autoral | R3 |

## Menu de blocos

**Todos os blocos ficam disponíveis para todos os professores; o menu é que organiza.** Ninguém é bloqueado por área, e você programa cada bloco uma vez só.

| Grupo | Blocos | Correção | Entrega |
| --- | --- | --- | --- |
| **Essenciais** (sempre no topo) | Texto, vídeo, imagem, material para baixar, múltipla escolha (uma ou várias corretas), verdadeiro ou falso, destaque/aviso | Automática nas questões | R1 |
| **Programação** | Código com realce, preveja a saída, ache o erro, complete o código, ordene linhas, exercício de código com testes | Automática | R1 (já existem) |
| **Exatas** | Fórmula (LaTeX), resposta numérica com tolerância e unidade | Automática | R2 |
| **Linguagens** | Lacunas em texto, associar colunas, áudio | Automática | R2 |
| **Práticas** | Ordenar etapas, dissertativa, entrega de trabalho (arquivo, foto, vídeo) | Professor nas abertas | R2 |
| **Ao vivo e externos** | Aula ao vivo, incorporar (YouTube, Figma, GeoGebra, Google Slides) | — | R3 |

Como o menu evita bagunça:

1. **Atalho `/`** dentro do editor abre o menu com busca: digitou "fórmula", aparece o bloco.
2. **Essenciais abertos, demais grupos recolhidos.** O modelo de curso escolhido (Programação, Exatas, Linguagens, Práticas, Geral) só decide quais grupos começam abertos.
3. **Usados recentemente** aparecem primeiro, por professor.
4. Cada item mostra **ícone, nome e uma linha** do que faz; ao passar o mouse, uma prévia.
5. **Bloco novo em teste** liga primeiro para algumas escolas (ESC-05) e depois para todas.

No código, cada bloco é um componente com três partes: **editor** (o que o professor preenche), **exibição** (o que o aluno vê) e **correção** (no servidor, se houver). Um bloco novo não mexe nos outros.

## Experiência sem bagunça

Bagunça vem de mostrar tudo para todos. As regras abaixo valem para toda tela nova; uma tela que quebra uma delas não entra.

**Separação**

1. **Três áreas com cara própria:** *Estudar* (aluno), *Ensinar* (professor e monitor), *Administrar* (dono e admin). Cada pessoa só vê as áreas do seu papel.
2. **Uma escola por vez.** Tudo na tela pertence à escola aberta; trocar de escola é um clique no seletor, como no Slack.
3. **A marca da escola só aparece onde o aluno está.** Área do aluno e páginas de venda usam logo e cor da escola; as áreas *Ensinar* e *Administrar* usam o visual neutro da plataforma em todas as escolas.

**Simplicidade**

4. **Uma ação principal por tela**, em destaque; o resto em menus secundários.
5. **Mostrar aos poucos:** opções avançadas atrás de "Mais opções". O básico resolve 80% dos casos.
6. **Personalização por escolhas primeiro:** logo, uma cor (o contraste é conferido automaticamente), uma fonte de uma lista, seções prontas. Código próprio só nas páginas públicas e no plano mais alto (ver Personalização do site do cliente).
7. **Telas vazias ensinam:** "Você ainda não tem cursos" vem com o botão "Criar primeiro curso" e um exemplo.
8. **Lista de primeiros passos** para professor e dono novos, com progresso, que some quando termina.

**Consistência**

9. **Um sistema de design:** tokens (cores, espaços, fontes) e componentes únicos (botão, campo, card, tabela, aviso). Nenhuma tela inventa o próprio botão.
10. **Mesmas palavras em todo lugar:** curso, módulo, aula, bloco. Um glossário decide; nada de "lição" numa tela e "aula" em outra.
11. **Mesmos lugares em toda tela:** título e ação principal no topo, navegação à esquerda no computador e embaixo no celular.

**Confiança**

12. **Salvar sozinho** no editor, com "Salvo há 5 s". Publicar é sempre um passo separado e reversível.
13. **Desfazer em vez de "Tem certeza?"**, exceto para o que não volta (apagar conta, reembolsar).
14. **Mensagens de erro dizem o que fazer:** "O vídeo passou de 2 GB. Exporte em 1080p e envie de novo", nunca "Erro 413".
15. **Celular primeiro na área do aluno;** o editor do professor é pensado para computador, mas funciona no celular para responder dúvidas.
16. **Acessível:** teclado em tudo, foco visível, contraste AA, textos alternativos. Isso também deixa o site melhor para todos.

**Validar com gente de verdade:** antes de cada entrega, 3 a 5 pessoas (aluno, professor de outra área) fazem uma tarefa enquanto você observa sem ajudar. Onde elas travam é o que precisa mudar.

## Requisitos não funcionais

As tecnologias de cada item estão no documento "Stack profissional".

| Código | Categoria | Requisito | Como conferir |
| --- | --- | --- | --- |
| RNF-01 | Isolamento | Toda tabela de escola tem `escola_id`; o PostgreSQL bloqueia leitura entre escolas com Row-Level Security, mesmo se o código errar | Teste automático tenta ler dados de outra escola e precisa falhar |
| RNF-02 | Permissões | Papel por escola e por curso; o servidor confere em toda ação, a tela só esconde | Teste para cada papel × ação |
| RNF-03 | Segurança | CSP, anti-CSRF, cookies `__Host-`, HSTS, limites por rota, 2FA obrigatório para professor e dono; referência OWASP ASVS nível 2 | CodeQL, Dependabot, testes de segurança |
| RNF-04 | Conteúdo protegido | Gabaritos, vídeos e materiais pagos só com link assinado e de validade curta | Teste com link vencido e de outra pessoa |
| RNF-05 | Dinheiro | Webhook idempotente, conciliação diária, valores em centavos (inteiros), nunca `float` | Teste de webhook repetido e fora de ordem |
| RNF-06 | Desempenho | Página de aula abaixo de 1 s no servidor; LCP < 2,5 s, INP < 200 ms, CLS < 0,1 no celular em 4G | Lighthouse no CI |
| RNF-07 | Disponibilidade | Meta 99,5% ao mês; publicar não derruba quem está estudando | Uptime Kuma |
| RNF-08 | Recuperação | Backup diário fora do servidor; perder no máximo 24 h de dados; voltar em até 4 h | Restauração ensaiada todo mês |
| RNF-09 | Privacidade (LGPD) | Plataforma é controladora; professor vê só nome e progresso dos próprios alunos; exportar e apagar dados | Teste de exportação e exclusão |
| RNF-10 | Acessibilidade | WCAG 2.2 AA em todas as áreas, incluindo o editor | axe-core nos testes de tela |
| RNF-11 | Marca | Cor da escola só entra se tiver contraste AA com o texto; senão o sistema ajusta | Teste do cálculo de contraste |
| RNF-12 | Custos | Limite de armazenamento e minutos de vídeo por escola; aviso em 80% | Painel do admin |
| RNF-13 | Arquivos | Tipo conferido pelo conteúdo, tamanho máximo, antivírus antes de abrir para todos | Teste com arquivo disfarçado |
| RNF-14 | Observabilidade | Logs estruturados com escola, usuário e requisição; alerta quando o erro dispara | Seq |
| RNF-15 | Idioma | Textos da interface num arquivo de recursos (pt-BR), prontos para outros idiomas | Nenhum texto fixo no código das telas |
| RNF-16 | Manutenção | Cobertura de testes nas regras de domínio e dinheiro; CI verde para entrar na `main` | GitHub Actions |

## Modelo de dados essencial

Só `Usuario` e `Escola` são globais; **todo o resto carrega `escola_id`**, e é isso que impede artes e física de se misturarem.

| Entidade | Pertence a | Campos principais |
| --- | --- | --- |
| Usuario | Plataforma | e-mail, nome, foto, senha, 2FA, preferências |
| Escola | Plataforma | nome, endereço curto, domínio, logo, cor, fonte, plano, situação |
| Membro | Escola + Usuario | papel (aluno, professor, dono), desde quando |
| Curso | Escola | título, capa, categoria, nível, carga horária, modelo, situação (rascunho, em revisão, publicado), na vitrine? |
| EquipeCurso | Curso + Usuario | papel no curso (professor, coprofessor, monitor), % da receita |
| Modulo | Curso | título, ordem, regra de liberação |
| Aula | Modulo | título, ordem, amostra grátis?, duração, versão publicada |
| Bloco | Aula | tipo, ordem, conteúdo (JSON validado por tipo) |
| Gabarito | Bloco | resposta certa e explicações; nunca vai ao navegador |
| VersaoAula | Aula | blocos daquela versão, autor, data |
| Midia | Escola | tipo, onde está (Bunny ou R2), tamanho, dono |
| Produto | Escola | curso avulso, assinatura ou pacote; preço em centavos; cursos incluídos |
| Pedido | Escola + Usuario | produto, valor, cupom, situação, id no gateway |
| Repasse | Pedido | quem recebe (plataforma, escola, professor), valor, situação |
| Matricula | Curso + Usuario | origem (compra, assinatura, código), validade |
| Progresso | Matricula + Aula | concluída?, posição do vídeo, último acesso |
| Resposta | Matricula + Bloco | resposta, nota, tentativa, corrigida por |
| Duvida | Aula + Usuario | texto, respostas, situação |
| Certificado | Matricula | código de verificação, data, carga horária |
| Avaliacao | Curso + Usuario | nota, comentário |
| Notificacao | Usuario | tipo, texto, lida? |
| Auditoria | Escola | quem, o quê, quando, de onde |
| Area, Categoria | Plataforma | nome, endereço curto, ordem, ícone; categoria pertence a uma área |
| Etiqueta | Plataforma | nome, tipo (tecnologia ou tema), sinônimos |
| Trilha | Escola | título, objetivo, cursos em ordem por etapa, certificado da trilha |
| Colecao | Escola | título, cursos, ordem na vitrine |
| MetaSemanal | Matricula | aulas por semana, lembrete, frequência dos e-mails |

## Entregas

Cada entrega termina **no ar e vendendo**; a próxima só começa com a anterior validada por gente de verdade.

**R1 — Sua escola** (vender o Catálogo do HTML)

- [ ] Fase 0 da stack: solução, CI, Aspire + Mailpit, ADRs
- [ ] Banco com `escola_id` e Row-Level Security desde já (uma escola: Instituto AMS)
- [ ] Contas, perfil e LGPD portados (CON-01 a 05)
- [ ] Cursos, editor por blocos, mídia e vídeo (CUR-01 a 07)
- [ ] Blocos essenciais + programação, prova do módulo, certificado (AVA-01 a 06)
- [ ] Tela da aula nova, Meus cursos, Continuar de onde parei (ALU-01 a 04)
- [ ] Checkout real, assinatura, cupons, reembolso de 7 dias (VEN-01 a 04)
- [ ] E-mails de transação, painel básico, auditoria
- [ ] Módulos 2 e 3 do Catálogo escritos; teste com 3 a 5 alunos
- [ ] Áreas, categorias, etiquetas, coleções, catálogo com filtros e modo foco (CAT-01 a 05, JOR-01 a 05)
- [ ] Aula padrão no editor, objetivo e resumo do módulo, guia de qualidade (EST-01, EST-02)

**R2 — Professores convidados** (estilo Udemy, dentro do Instituto AMS)

- [ ] Contrato com professor, conversa com contador
- [ ] Convite, equipe do curso, revisão e aprovação
- [ ] Split, comissão, extrato, conciliação
- [ ] Blocos de exatas, linguagens e práticas; correção pelo professor
- [ ] Painel do professor, notificações, avisos, e-mails automáticos
- [ ] Página do professor, avaliações, anotações, busca no curso
- [ ] Validar com 1 ou 2 professores colegas

**R3 — Escolas próprias** (cada professor com a sua marca)

- [ ] Assistente para criar escola, marca, página inicial editável
- [ ] Subdomínio e domínio próprio com HTTPS automático
- [ ] Assinatura da plataforma para donos; limites de armazenamento e vídeo
- [ ] Vitrine geral com cursos das escolas que optarem
- [ ] Seletor de escola, passkeys, legendas, aulas ao vivo
- [ ] Denúncias, direito autoral, antivírus
- [ ] Venda da plataforma: planos e recursos, cobrança recorrente, licença e implantação de servidor exclusivo (VND-01 a 09)
- [ ] Personalização: construtor de páginas, 3 temas, código próprio nas páginas públicas (PER-01 a 08)

**R4 — Crescimento**

- [ ] Comunidade por curso, metas e sequência de dias
- [ ] PWA, afiliados

## Mapa de telas da R1

**29 telas em três áreas.** Nenhuma tela nova entra sem estar aqui; se precisar, primeiro atualiza o mapa.

Navegação fixa: **Estudar** tem cabeçalho no topo (logo, Catálogo, Meus cursos, busca, avatar) e troca para o cabeçalho do curso no modo foco. **Ensinar** e **Administrar** têm menu lateral à esquerda (embaixo no celular).

### Estudar (visitante e aluno)

| Tela | Endereço | Mostra | Leva para |
| --- | --- | --- | --- |
| Início da escola | `/` | Promessa, busca, áreas, coleções | Catálogo, curso |
| Catálogo | `/cursos`, `/cursos/{area}/{categoria}` | Filtros e cards | Curso |
| Página do curso | `/curso/{curso}` | Venda, ementa, amostras, professor | Aula de amostra, checkout |
| Checkout | `/comprar/{produto}` | Resumo, cupom, pagamento | Boas-vindas do curso |
| Entrar · Cadastrar · Recuperar senha · Confirmar e-mail · 2FA | `/entrar` ... | Formulário único por tela | Volta para onde estava |
| Início do aluno | `/inicio` | **Continuar**, Meus cursos, próximo passo | Aula |
| Aula (modo foco) | `/curso/{curso}/{modulo}/{aula}` | Aula padrão + lateral do módulo | Próxima aula, prova |
| Prova do módulo | `.../{modulo}/prova` | Questões, tempo, resultado | Próximo módulo |
| Certificados | `/certificados` | Lista e PDF | Verificação pública |
| Verificar certificado | `/certificado/{codigo}` | Nome, curso, data, carga horária | — |
| Minha conta | `/conta` | Perfil, segurança, compras, reembolso, meus dados | — |

### Ensinar (professor)

| Tela | Endereço | Mostra | Leva para |
| --- | --- | --- | --- |
| Meus cursos | `/ensinar` | Cursos com situação e lista de primeiros passos | Curso |
| Curso: informações | `/ensinar/{curso}` | Dados, classificação, guia de qualidade | Estrutura |
| Estrutura | `/ensinar/{curso}/estrutura` | Módulos e aulas, arrastar | Editor |
| Editor de aula | `/ensinar/{curso}/aula/{aula}` | Blocos, salvar sozinho, prévia, publicar | Estrutura |
| Biblioteca de mídia | `/ensinar/midia` | Vídeos, imagens, arquivos, uso | — |
| Dúvidas | `/ensinar/duvidas` | Sem resposta primeiro | Aula da dúvida |

### Administrar (dono e admin)

| Tela | Endereço | Mostra | Leva para |
| --- | --- | --- | --- |
| Painel | `/admin` | Receita, alunos ativos, vendas por curso | Detalhes |
| Produtos e planos | `/admin/produtos` | Preços, cursos incluídos | — |
| Cupons e códigos | `/admin/cupons` | Validade, usos | — |
| Pedidos e reembolsos | `/admin/pedidos` | Situação, estorno | Usuário |
| Usuários e papéis | `/admin/usuarios` | Busca, papel, matrículas | — |
| Catálogo | `/admin/catalogo` | Áreas, categorias, etiquetas, coleções | — |
| Escola | `/admin/escola` | Marca, páginas (sobre, termos, privacidade) | — |
| Auditoria | `/admin/auditoria` | Quem fez o quê e quando | — |

## Critérios de aceite da R1

Cada linha vira um teste automático. Um requisito só está pronto quando todos os critérios dele passam no CI.

| Requisito | Pronto quando |
| --- | --- |
| Isolamento por escola (RNF-01) | Uma consulta sem `escola_id` não retorna nada, mesmo escrita errada de propósito. Usuário da escola A recebe 404 ao abrir curso, aluno ou pedido da escola B |
| Cadastro e login (CON-01 a 03) | Conta só entra depois do e-mail confirmado. 5 senhas erradas bloqueiam por 15 min. Professor e dono não entram sem 2FA. O e-mail chega em menos de 1 min (Mailpit no teste) |
| Classificação (CAT-03) | "Publicar" fica desativado e diz o que falta enquanto área, categoria, nível ou capa estiverem vazios |
| Catálogo (CAT-04) | Filtro por nível + tecnologia mostra só os cursos certos. Endereço com filtros pode ser copiado e reabre igual. Sem cursos, aparece mensagem com link para limpar filtros |
| Editor (CUR-03, EST-01) | Aula nova abre com os blocos da aula padrão. Texto digitado aparece salvo em até 5 s. Fechar a aba e voltar não perde nada. Prévia mostra exatamente o que o aluno verá. Aluno nunca vê rascunho |
| Histórico (CUR-04) | Restaurar uma versão antiga cria uma versão nova; nada é apagado |
| Vídeo (CUR-07, ALU-03) | Envio mostra progresso e continua após queda de internet. Aluno sem matrícula recebe 403 no link do vídeo. Pular para o fim não conclui a aula; 90% assistido conclui |
| Correção (AVA-01, AVA-02) | Gabarito nunca aparece no HTML nem nas respostas da API. Resposta errada mostra a explicação daquela alternativa |
| Prova do módulo (AVA-03) | Tempo acaba e a prova é entregue sozinha. Tentativas esgotadas bloqueiam com a data da próxima. Nota abaixo do mínimo não libera o próximo módulo (quando a regra estiver ligada) |
| Certificado (AVA-06) | Só é emitido com a regra de conclusão cumprida. O código abre a verificação pública sem login. Mudar o curso depois não altera o certificado |
| Continuar (ALU-01, JOR-03) | Aluno que parou no minuto 7:30 da aula 3 em um aparelho cai na aula 3, minuto 7:30, em outro aparelho |
| Modo foco (JOR-01, JOR-04) | Dentro do curso não existe link para a vitrine nem oferta na tela. Tecla F entra e sai da tela cheia. Lateral recolhida continua recolhida na próxima aula |
| Checkout (VEN-01, VEN-02) | Pix aprovado libera o curso em até 30 s. O mesmo aviso do gateway chegando duas vezes gera uma matrícula só. Preços guardados em centavos |
| Reembolso (VEN-04) | Botão aparece só nos 7 primeiros dias. Pedir reembolso tira o acesso e gera o estorno no gateway na hora |
| LGPD (CON-05) | "Baixar meus dados" entrega um arquivo com tudo do aluno. "Apagar conta" remove os dados pessoais e mantém só o que a lei fiscal exige, sem nome |
| Acessibilidade (RNF-10) | axe-core sem erros nas 29 telas. Todas as telas funcionam só com teclado |
| Desempenho (RNF-06) | Lighthouse no celular: aula, catálogo e página do curso com nota 90+ em desempenho |

## Guia de qualidade do curso

Aparece na tela "Curso: informações" como uma lista com ✓. **Obrigatório** impede publicar; **recomendado** só avisa. É o que faz cursos de professores diferentes parecerem da mesma plataforma.

| Item | Regra | Tipo | Quem confere |
| --- | --- | --- | --- |
| Classificação | Área, categoria, nível e pelo menos 1 etiqueta | Obrigatório | Sistema |
| Capa | 1280 × 720 px, sem texto pequeno | Obrigatório | Sistema (tamanho) |
| Página de venda | O que o aluno vai conseguir fazer (3 a 6 itens), para quem é, pré-requisitos | Obrigatório | Sistema |
| Objetivos | Cada módulo e cada aula com objetivo escrito | Obrigatório | Sistema |
| Aulas de amostra | Pelo menos 1 | Obrigatório | Sistema |
| Atividade | Pelo menos 1 por módulo | Obrigatório | Sistema |
| Duração da aula | Até 20 min; acima disso, sugestão de dividir | Recomendado | Sistema |
| Vídeo | 1080p, áudio sem eco nem ruído de fundo, volume constante | Recomendado | Revisão (você, na R2) |
| Textos alternativos | Toda imagem com descrição | Recomendado | Sistema |
| Transcrição | Revisada pelo professor | Recomendado | Professor |
| Materiais | Em PDF ou formato aberto, com nome claro | Recomendado | Sistema (formato) |

No Instituto AMS, a revisão humana da R2 usa esta mesma lista; nas escolas próprias (R3), só os itens do sistema valem.

## Mudanças em curso com alunos

**Regra geral: o professor melhora o curso à vontade, e o aluno nunca perde o que já conquistou.**

| Mudança | O que acontece com quem já está matriculado |
| --- | --- |
| Corrigir texto, trocar vídeo de uma aula | Aula continua concluída. Mudança grande pode ser marcada como "atualizada", com selo na lista |
| Aula nova | Aparece com selo "nova". Não tira o certificado de quem já concluiu; o progresso passa a mostrar a aula a mais |
| Apagar aula | Vai para a lixeira por 30 dias. O progresso de quem a concluiu não diminui |
| Mudar questão já respondida | A nota antiga fica. A nova versão vale para novas tentativas |
| Mudar a regra de conclusão ou a nota mínima | Vale só para quem ainda não concluiu |
| Certificado emitido | Nunca muda; guarda os dados do momento da emissão |
| Mudar o preço | Não afeta quem já comprou; assinante mantém o valor até cancelar |
| Despublicar o curso | Some da vitrine; quem comprou continua com acesso pelo prazo da compra |

O professor vê um aviso antes de publicar uma mudança que afeta alunos ativos ("42 alunos estão neste módulo") e pode avisá-los com um clique.

## Glossário

Telas, e-mails, código e documentação usam **só estas palavras**. As da coluna "Não usar" ficam proibidas na interface.

| Termo | Significa | Não usar |
| --- | --- | --- |
| Plataforma | O sistema inteiro, com todas as escolas | Site, portal |
| Escola | Espaço separado com marca, cursos e alunos próprios | Tenant, instância |
| Vitrine | Catálogo geral com cursos de várias escolas | Marketplace, loja |
| Área | Grande campo do conhecimento (Tecnologia, Exatas) | Departamento |
| Categoria | Matéria ou especialidade dentro da área | Subcategoria, assunto |
| Etiqueta | Tecnologia ou tema para filtrar (JavaScript, ENEM) | Tag, palavra-chave |
| Trilha | Cursos em ordem para um objetivo, com certificado próprio | Formação, carreira, jornada |
| Coleção | Grupo de cursos sem ordem, para a vitrine | Lista, playlist |
| Curso | Conjunto de módulos vendido ou liberado de uma vez | Treinamento, produto |
| Módulo | Parte do curso com objetivo e prova próprios | Seção, capítulo, unidade |
| Aula | Uma unidade de estudo de 5 a 20 min | Lição, vídeo, conteúdo |
| Bloco | Peça da aula: texto, vídeo, questão, material | Componente, elemento |
| Atividade | Bloco que o aluno responde ou entrega | Exercício (só nos nomes dos blocos), tarefa |
| Prova do módulo | Avaliação no fim do módulo | Checkpoint, teste |
| Projeto | Trabalho prático com critérios de correção | Desafio |
| Matrícula | Acesso de um aluno a um curso | Inscrição |
| Produto | O que se compra: curso, assinatura ou pacote | Oferta |
| Professor | Quem cria e ensina um curso | Instrutor, autor, tutor |
| Monitor | Quem ajuda o professor nas dúvidas e correções | Tutor, assistente |
| Dono da escola | Quem administra uma escola | Admin (fica só para a plataforma) |

No código, as classes e tabelas usam os mesmos nomes (`Escola`, `Trilha`, `Matricula`), sem tradução para o inglês.

## Venda da plataforma

**Decisão: vender de duas formas, com o mesmo código.** Assinatura é o produto principal; servidor exclusivo é a versão para cliente grande. Os dois rodam a mesma imagem Docker, e o que muda é só configuração.

|  | Assinatura | Servidor exclusivo |
| --- | --- | --- |
| Para quem | Professor, escola pequena ou média | Rede de escolas, prefeitura, empresa com exigência de dados separados |
| Onde roda | Na sua plataforma, como uma escola | Num servidor só do cliente (contratado por você ou por ele) |
| Marca e domínio | Do cliente | Do cliente |
| Cobrança | Mensal ou anual pelo plano + adicionais | **Implantação** (uma vez) + **mensalidade de manutenção** + recursos contratados |
| Atualizações | Automáticas, no mesmo dia para todos | Automáticas, 7 dias depois da assinatura (já testadas em produção) |
| Backup e monitoramento | O seu, central | Feito por você, com a mesma ferramenta, com os alertas no seu painel |
| Contratação | Pelo próprio site | Proposta e contrato assinado |

**Pacotes de recursos.** A base é completa para ensinar; os adicionais são módulos grandes, nunca um tipo de questão isolado.

- **Base (todo plano):** cursos, aulas, vídeo, blocos essenciais, prova do módulo, certificado, checkout, marca e subdomínio.
- **Adicionais:** trilhas · pacote de programação · projetos com rubrica · domínio próprio · remover "feito com" · aulas ao vivo · comunidade · relatórios avançados · professores extras · mais armazenamento e vídeo.

**Regras que protegem os dois lados:**

1. **Nunca uma cópia alterada.** Pedido especial de um cliente vira recurso liga/desliga para todos, ou não é feito. Uma versão por cliente é o que quebra empresas pequenas de software.
2. **Servidor exclusivo aceita atualizações.** O contrato diz que ele sempre roda a versão atual (ou no máximo a anterior). Quem recusar atualização perde o suporte.
3. **Licença assinada.** O servidor exclusivo lê um arquivo de licença assinado por você, com recursos e validade. Ele confere a assinatura sem precisar da internet, e ninguém liga um recurso sem pagar.
4. **Falta de pagamento nunca prende os dados.** 7 dias de tolerância, depois só leitura: a escola ainda exporta tudo, alunos ainda baixam certificados.
5. **Rebaixar o plano não apaga nada.** O recurso fica só leitura até voltar a pagar.

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| VND-01 | Catálogo de recursos e planos; recursos ligados por escola, conferidos no servidor | R3 |
| VND-02 | Página de planos e contratação pelo próprio cliente | R3 |
| VND-03 | Cobrança recorrente pelo gateway; pagamento liga, atraso bloqueia após 7 dias | R3 |
| VND-04 | Painel do cliente: plano, uso, faturas, mudar de plano | R3 |
| VND-05 | Modo só leitura com exportação liberada | R3 |
| VND-06 | Licença assinada para servidor exclusivo (recursos + validade), conferida sem internet | R3 |
| VND-07 | Implantação de servidor exclusivo por script: mesma imagem, configuração e licença por cliente | R3 |
| VND-08 | Pipeline de atualização: assinatura primeiro, servidores exclusivos 7 dias depois, com volta automática se falhar | R3 |
| VND-09 | Painel central: versão, saúde, backup e licença de cada servidor exclusivo | R3 |

### Recursos para vender

O que o plano comercial precisa do sistema para vender sem depender de você a cada cliente.

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| VND-10 | Site da plataforma: o que faz, planos, perguntas frequentes, casos de sucesso, SEO | R3 |
| VND-11 | Escola de demonstração com dados de exemplo, recriada toda noite | R3 |
| VND-12 | Teste grátis de 14 dias sem cartão; aviso 3 dias antes de acabar; vira só leitura se não assinar | R3 |
| VND-13 | Sequência de e-mails do teste (dias 1, 3, 7 e 12), parando quando o cliente já fez o passo | R3 |
| VND-14 | Lista de primeiros passos do dono com progresso; o assistente cria um curso de exemplo | R3 |
| VND-15 | Programa de indicação: link próprio, crédito de 1 mês lançado sozinho após o 1º pagamento do indicado | R3 |
| VND-16 | Painel de negócio do admin: MRR, pagantes, conversão do teste, ativação, cancelamento, custo e chamados por cliente | R3 |
| VND-17 | Chamados de suporte no painel do cliente: abrir, acompanhar, prazo por plano, histórico | R3 |
| VND-18 | Central de ajuda pública com busca, artigos e vídeos curtos; link contextual em cada tela ("Como faço isso?") | R3 |

**Contratos:** contrato de software por assinatura (prazo, disponibilidade, suporte, cancelamento); no servidor exclusivo, também implantação e política de atualização. Nos dois, **acordo de tratamento de dados (LGPD)**: a escola cliente é controladora dos dados dos alunos, você é operador. Nota fiscal como serviço de software, enquadramento confirmado com o contador.

**Antes da R3 estar pronta:** uma escola parceira com preço de cliente fundador, configurada à mão, valida preço e pacotes.

## Personalização do site do cliente

**O cliente monta o site do jeito que quiser nas páginas públicas; a área de estudo e o editor ficam padrão, só com a marca dele.** É essa divisão que deixa você atualizar todos os clientes sem quebrar o site de nenhum.

| Nível | O que o cliente faz | Onde vale | Plano |
| --- | --- | --- | --- |
| **1. Marca** | Logo, cores, fontes, favicon, e-mails com a marca. O contraste é conferido sozinho | Todo o site | Todos |
| **2. Construtor de páginas** | Monta início, sobre, páginas de venda e páginas livres arrastando seções: destaque, cursos, vídeo, texto, imagem, depoimentos, professores, perguntas, preços, formulário, contador de alunos. Cria menus e rodapé | Páginas públicas | Todos |
| **3. Temas** | Escolhe entre temas prontos (layouts diferentes, não só cores). Cliente de servidor exclusivo pode encomendar um **tema exclusivo**, feito por você e cobrado como projeto | Páginas públicas + moldura da área do aluno | Temas prontos: todos. Tema exclusivo: projeto pago |
| **4. Código próprio** | CSS próprio e trechos de HTML nas páginas públicas; scripts aprovados (Google Analytics, Meta Pixel) por campo próprio, sem JavaScript livre | Páginas públicas | Plano mais alto e servidor exclusivo |

**Por que a área de estudo não é livre:** é nela que ficam o player, a correção, o progresso e o modo foco. Se cada cliente mudar o HTML dali, a próxima atualização quebra o curso de alguém, e a acessibilidade deixa de ser garantida. Plataformas como Kajabi e Teachable seguem a mesma divisão.

**Como funciona por dentro:** o construtor de páginas usa o **mesmo motor de blocos das aulas**: uma página é uma lista de seções salva em JSON, renderizada pelo Razor. Um tema é um pacote de layouts + tokens de cor, espaço e fonte, sem código de regra. O CSS próprio passa por um filtro e fica restrito às páginas públicas.

| Código | Funcionalidade | Entrega |
| --- | --- | --- |
| PER-01 | Marca completa: logo, cores, fontes, favicon, e-mails | R3 (R1 só para a sua escola) |
| PER-02 | Construtor de páginas com seções arrastáveis, rascunho e prévia | R3 |
| PER-03 | Menus e rodapé editáveis; páginas livres com endereço próprio | R3 |
| PER-04 | Galeria de temas prontos (começar com 3) | R3 |
| PER-05 | Tema exclusivo por cliente, como pacote separado (sem alterar o código do sistema) | R3 |
| PER-06 | CSS e HTML próprios nas páginas públicas, com filtro de segurança | R3 |
| PER-07 | Campos para Google Analytics, Meta Pixel e Google Tag Manager | R3 |
| PER-08 | Histórico de versões das páginas e voltar para a anterior | R3 |

## Mapa para o backend

**Cada módulo de requisitos já tem a peça da stack que o atende**; nada aqui pede tecnologia fora de Plataforma de cursos — Stack profissional, exceto as bibliotecas marcadas *(nova)*, que entram lá também. Use esta tabela para abrir as tarefas do backend.

### Peças que valem para tudo

| Peça | Como fazer na stack |
| --- | --- |
| Descobrir a escola da requisição | Middleware no ASP.NET Core que lê o domínio ou subdomínio e carrega a escola (com HybridCache) |
| Isolamento por escola | Filtro global do EF Core por `escola_id` **e** Row-Level Security no PostgreSQL 18, com a escola passada a cada conexão (`SET app.escola_id`) por um interceptor do EF Core; Dapper usa a mesma conexão |
| Permissões | Políticas de autorização do ASP.NET Core + handlers por recurso (curso, escola); atributo `[RequerRecurso]` para o plano contratado |
| Regras e validação | Casos de uso em `Plataforma.Aplicacao`, validação com FluentValidation, entidades sem dependência de infraestrutura |
| Banco | EF Core 10 + Migrations para escrita; Dapper para relatórios; dinheiro em `bigint` (centavos) |
| Tarefas em segundo plano | Hangfire guardado no PostgreSQL, com nova tentativa e painel restrito ao admin |
| Integrações externas | `HttpClient` tipado + `Microsoft.Extensions.Http.Resilience` *(nova)* para repetir e cortar chamadas lentas |
| Logs | Serilog + OpenTelemetry → Seq, sempre com escola, usuário e requisição |
| Telas | Razor Pages + htmx; JavaScript em módulos com `@ts-check` |

### Por módulo

| Módulo | Peças da stack | Tarefas (Hangfire) | Teste-chave |
| --- | --- | --- | --- |
| Contas (CON) | ASP.NET Core Identity, TOTP, passkeys, MailKit + modelos Razor de e-mail | Envio de e-mails | Conta sem e-mail confirmado não entra |
| Escolas (ESC) | Middleware de escola; domínios próprios com **Caddy on-demand TLS** *(nova configuração)* consultando uma rota que confirma o domínio | Verificar DNS do domínio novo | Domínio não cadastrado não recebe certificado |
| Cursos e blocos (CUR, EST) | Blocos em JSON tipado (`System.Text.Json` com tipos polimórficos), um validador por tipo; Markdig para texto; SortableJS *(nova)* para arrastar | Gerar versão publicada | Aluno nunca recebe rascunho |
| Atividades (AVA) | Correção por tipo no servidor; gabarito em tabela separada; KaTeX *(nova)* para fórmulas; certificado em PDF com QuestPDF *(nova, conferir licença)* | Revisão espaçada diária | Gabarito ausente de HTML e JSON |
| Vídeo e arquivos | Bunny Stream (API + token); envio retomável com tus-js-client *(nova)*; R2 por AWSSDK.S3 *(nova)* com links assinados; ClamAV *(nova, contêiner)* para arquivos enviados | Conferir vídeo pronto, limpar arquivos órfãos | Link vencido ou de outra pessoa recusado |
| Catálogo e jornada (CAT, JOR) | Full-text do PostgreSQL em português + `unaccent` + `pg_trgm` para erros de digitação | Lembretes de estudo | Filtro com etiqueta e nível traz só os cursos certos |
| Comunicação (COM) | Tabela de notificações + htmx para o sino; MailKit | E-mails automáticos, aluno parado | Modo foco não mostra notificação fora de dúvida respondida |
| Vendas (VEN) | Cliente Asaas atrás de `IGatewayPagamento`; webhook grava o evento antes de processar (idempotência); split por carteira | Conciliação diária, carrinho abandonado | Mesmo webhook duas vezes = uma matrícula |
| Venda da plataforma (VND) | Assinatura da escola no Asaas; recursos ligados por escola; licença assinada com ECDSA (`System.Security.Cryptography`) para servidor exclusivo | Bloqueio após 7 dias de atraso, fim do teste, crédito de indicação | Licença alterada à mão é recusada |
| Personalização (PER) | Mesmo motor de blocos das aulas para páginas; temas = layouts Razor + tokens CSS; CSS próprio filtrado e servido só nas páginas públicas | — | CSS com `url(javascript:)` ou `@import` externo é recusado |
| Relatórios (REL) | Consultas Dapper; exportação CSV | Relatórios pesados | Professor só vê os próprios cursos |
| Administração (ADM) | Auditoria em tabela própria; "entrar como" com registro | — | Toda ação do admin aparece na auditoria |

**Testes:** xUnit v3 para regras, WebApplicationFactory + Testcontainers (PostgreSQL 18 real) para integração e isolamento, Playwright .NET + axe-core para os critérios de aceite das telas.

## Decisões em aberto

Duas travam a R1: o nome e o gateway. As demais precisam estar decididas antes da entrega indicada.

| Decisão | Opções | Minha sugestão | Antes de |
| --- | --- | --- | --- |
| Nome e domínio da plataforma | Instituto AMS como marca da plataforma, ou plataforma com nome neutro e o Instituto AMS como uma escola dentro dela | Família "AM" do portfólio, com um nome que não soe como verbo; o cliente final vê a marca da escola, não a da plataforma | R1 |
| Gateway | Mercado Pago ou Asaas | Decidido: Asaas (divide entre várias partes e também nas assinaturas) | R1 |
| Comissão do Instituto AMS sobre convidados | Ex.: 20%, 30%, 50% | Combinar com os primeiros professores e só depois fixar | R2 |
| Cobrança das escolas próprias | Mensalidade fixa, % por venda, ou os dois | % por venda sem mensalidade no início: tira a barreira de entrada | R3 |
| Quem paga o vídeo da escola própria | Incluído até um limite, ou a escola conecta a própria conta Bunny | Incluído até um limite, excedente cobrado | R3 |
| Aluno compartilhado entre escolas | O aluno de uma escola aparece como "já tem conta" em outra | Sim (uma conta por pessoa), mas cada escola só vê os próprios alunos | R3 |
|  |  |  |  |
