# Professores parceiros — o que falta para atender qualquer área

Oct 6, 2026 · @Alan Mateus

> **Substituído** por Plataforma de cursos — Especificação funcional v1, que junta este conteúdo aos dois modos (vitrine e escola própria).

## Resposta curta

**O site continua igual para o aluno?** Sim. Mesmo visual (o CSS é aproveitado), mesmas funções, mesmo login. Os endereços mudam de forma (`/cursos/html/1/introducao` no lugar de `aula-1-01-introducao.html`), mas os antigos redirecionam sozinhos. O aluno só percebe que ficou mais rápido.

**Hoje ele já atende qualquer área?** Não, e é melhor saber isso agora. O que é genérico (contas, planos, vídeo, texto, dúvidas, certificado) serve para qualquer curso. Mas 5 dos 6 tipos de exercício dependem de código, e o sistema supõe **um curso só, de um professor só**. Um curso de culinária, direito ou matemática hoje teria vídeo, texto e múltipla escolha, e mais nada.

Para qualquer professor de qualquer área faltam três coisas grandes: **atividades genéricas** (questões, entregas, materiais), **ferramentas do professor** (criar e vender o próprio curso) e **dinheiro dividido automaticamente** entre você e ele.

## O que hoje é só de programação

Nada disso sai: vira um **tipo de atividade opcional**, que o professor de programação liga e o de culinária nem vê.

| Recurso de hoje | Serve para outras áreas? | O que fazer |
| --- | --- | --- |
| Exercício **escolha** (múltipla escolha) | Sim | Vira o tipo básico de questão |
| Exercícios **preveja**, **ache-erro**, **codigo** | Não (exigem código) | Ficam no pacote "Programação" |
| Exercícios **complete** e **ordene** | A ideia sim; hoje exigem bloco de código | Aceitar texto comum (lacunas numa frase, ordenar etapas) |
| Laboratório, analisador, verificador, dicionário de códigos | Não | Pacote "Programação" |
| Trilha "Passo a passo" e capítulos `doc-*` | É conteúdo seu, não recurso | Viram o curso Catálogo do HTML |
| Checkpoint corrigido no servidor | Sim | Vira "Prova do módulo", com questões de qualquer tipo |
| Revisão espaçada | Sim | Vale para qualquer questão |
| Certificado | Sim, mas é "do curso" fixo | Por curso, com carga horária e nome do professor |
| Vídeo, texto, imagens, PDFs, dúvidas | Sim | Ficam como estão |

## Modelo: escola com convidados, não marketplace aberto

**Recomendação:** comece como escola com professores convidados (o Instituto AMS). Abra para qualquer professor só se a demanda aparecer.

|  | Escola com convidados | Marketplace aberto (estilo Udemy) |
| --- | --- | --- |
| Quem publica | Só quem você convida | Qualquer pessoa que se cadastra |
| Qualidade | Você garante, curso por curso | Precisa de avaliações, denúncias e moderação |
| Preço | Combinado com cada professor | Regras e faixas de preço da plataforma |
| Suporte e jurídico | Poucos contratos, conversados | Termos padrão, disputas, direitos autorais em escala |
| O que precisa construir | Menos (as seções abaixo, sem moderação em massa) | Tudo abaixo, mais moderação, denúncias e cadastro aberto |
| Concorrência | Sua marca e seu nicho | Udemy, Hotmart e Kiwify, de frente |

O diferencial real é o nicho: atividades corrigidas no servidor, provas por módulo e laboratório de código. Isso atrai **professores de cursos técnicos e de programação** primeiro. As outras áreas entram usando os tipos genéricos.

Antes de construir tudo: convide 1 ou 2 colegas, cadastre o curso deles você mesmo e veja se vende. Se não vender, você economizou meses.

## Tipos de conteúdo e atividade

Uma aula passa a ser uma **lista de blocos**: o professor monta escolhendo blocos, como num editor. Cada tipo é um componente, e um tipo novo não mexe nos outros.

| Bloco    | Exemplo de área | Correção | Hoje |
| --- | --- | --- | --- |
| Texto (Markdown) | Todas | — | Existe |
| Vídeo | Todas | Conclui com 90% assistido | Existe |
| Material para baixar (PDF, planilha, áudio) | Todas | — | Parcial (sem proteção) |
| Múltipla escolha / várias corretas | Todas | Automática | Parcial (só uma correta) |
| Verdadeiro ou falso | Direito, biologia | Automática | Novo |
| Lacunas em texto | Idiomas, contabilidade | Automática | Adaptar (hoje só código) |
| Ordenar etapas | Culinária, processos | Automática | Adaptar |
| Associar colunas | Idiomas, anatomia | Automática | Novo |
| Resposta numérica com tolerância | Matemática, física, finanças | Automática | Novo |
| Fórmulas (LaTeX) no texto e nas questões | Matemática, engenharia | — | Novo |
| Dissertativa | Redação, direito | Professor, com nota e comentário | Novo |
| Entrega de trabalho (arquivo, foto, vídeo) | Artes, culinária, projetos | Professor | Novo |
| Aula ao vivo (link + gravação depois) | Todas | Presença | Novo |
| Exercícios de código (preveja, ache-erro, codigo) | Programação | Automática | Existe |

**Prova do módulo** = qualquer conjunto desses blocos, com nota mínima, tentativas e tempo definidos pelo professor.

## Para o professor

O professor vê **só os próprios cursos, alunos e vendas**. O editor de hoje vira a base; o resto é novo.

| Código | Funcionalidade | Prioridade |
| --- | --- | --- |
| RF-P01 | Convite por e-mail → conta de professor com 2FA obrigatório | Primeiro professor |
| RF-P02 | Perfil público: foto, mini-biografia, formação, redes, lista de cursos | Primeiro professor |
| RF-P03 | Criar curso: título, categoria, capa, descrição, público, pré-requisitos, carga horária, o que o aluno aprende | Primeiro professor |
| RF-P04 | Editor de aulas por blocos, com rascunho, prévia e histórico (o de hoje, ampliado) | Primeiro professor |
| RF-P05 | Enviar vídeos (Bunny, por curso) e materiais | Primeiro professor |
| RF-P06 | Escolher aulas grátis de amostra | Primeiro professor |
| RF-P07 | Enviar para revisão → você aprova → publica | Primeiro professor |
| RF-P08 | Responder dúvidas e corrigir dissertativas e entregas do próprio curso | Primeiro professor |
| RF-P09 | Painel: vendas, alunos, conclusão por aula, onde os alunos param | Logo depois |
| RF-P10 | Ver quanto vai receber e quando (extrato) | Primeiro professor |
| RF-P11 | Cupons do próprio curso, dentro dos limites que você define | Logo depois |
| RF-P12 | Avisos para os alunos do curso (no site e por e-mail) | Logo depois |
| RF-P13 | Coprofessor / monitor no mesmo curso | Mais tarde |
| RF-P14 | Importar curso em .zip (Markdown + arquivos) | Mais tarde |

## Para o aluno

Com vários cursos e professores, o aluno precisa **achar, escolher e organizar**. Hoje ele só tem uma trilha.

| Código | Funcionalidade | Prioridade |
| --- | --- | --- |
| RF-A01 | Vitrine: categorias, busca, filtros (área, nível, preço, grátis) | Primeiro professor |
| RF-A02 | Página de venda de cada curso: vídeo de apresentação, ementa, professor, aulas de amostra, garantia | Primeiro professor |
| RF-A03 | "Meus cursos" com progresso de cada um e **Continuar de onde parei** | Primeiro professor |
| RF-A04 | Comprar curso avulso ou assinatura que libera vários | Primeiro professor |
| RF-A05 | Certificado por curso: carga horária, professor, código de verificação | Primeiro professor |
| RF-A06 | Avaliar o curso (nota + comentário), só quem comprou e assistiu parte dele | Logo depois |
| RF-A07 | Anotações e marcadores por aula, com o tempo do vídeo | Logo depois |
| RF-A08 | Pedir reembolso em até 7 dias pelo próprio site | Primeiro professor |
| RF-A09 | Lista de desejos e aviso de promoção | Mais tarde |
| RF-A10 | Comunidade ou fórum por curso | Mais tarde |
| RF-A11 | Legendas nos vídeos | Mais tarde |

## Para você: administração, financeiro e jurídico

A parte mais arriscada não é código: é dinheiro de terceiros passando pela sua plataforma.

| Código | Funcionalidade | Prioridade |
| --- | --- | --- |
| RF-G01 | Convidar, aprovar, suspender professores | Primeiro professor |
| RF-G02 | Revisar e aprovar cursos e atualizações grandes antes de publicar | Primeiro professor |
| RF-G03 | **Divisão automática do pagamento** (split do Mercado Pago ou Asaas): o gateway paga o professor direto, e o dinheiro dele não passa pela sua conta | Primeiro professor |
| RF-G04 | Comissão por professor ou por curso (ex.: 20% a 30% para a plataforma) | Primeiro professor |
| RF-G05 | Reembolso devolve a parte de cada um; estorno e chargeback descontados do professor no extrato | Primeiro professor |
| RF-G06 | Relatório financeiro: vendas, comissões, reembolsos, por período | Logo depois |
| RF-G07 | Categorias e destaques da vitrine | Logo depois |
| RF-G08 | Denúncia de conteúdo e retirada por direito autoral | Antes de abrir para todos |
| RF-G09 | Auditoria das ações dos professores (já existe para a equipe) | Primeiro professor |

**Jurídico (antes do primeiro professor, não depois):**

- **Contrato com o professor:** comissão, prazo de repasse, quem é dono do conteúdo, o que acontece se ele sair.
- **Termos do aluno** atualizados: o professor responde pelo conteúdo, a plataforma pela entrega.
- **Arrependimento de 7 dias** (CDC, art. 49) vale para compra pela internet; o sistema precisa fazer isso funcionar.
- **LGPD:** você é o controlador dos dados dos alunos; o professor só vê o que precisa (nome, progresso) e nunca exporta a lista de e-mails sem base legal.
- **Impostos:** com split, cada professor emite a própria nota, e você fatura só a sua comissão. Confirme o enquadramento com um contador antes de começar; isso eu não substituo.

## Requisitos não funcionais novos

| Código | Requisito | Por quê |
| --- | --- | --- |
| RNF-P01 | **Isolamento por curso**: toda consulta filtra por `curso_id` e pelo dono; teste automático tenta acessar o curso de outro professor e precisa falhar | Um professor nunca vê alunos, vendas ou rascunhos de outro |
| RNF-P02 | Permissões por curso (professor, coprofessor, monitor), não só por papel global | Hoje "professor" edita tudo |
| RNF-P03 | Webhook de pagamento idempotente e conciliado todo dia com o extrato do gateway | Dinheiro de terceiros não pode sumir nem duplicar |
| RNF-P04 | Limite de armazenamento e minutos de vídeo por professor | O custo do Bunny e do R2 cresce com cada curso |
| RNF-P05 | Arquivos enviados conferidos pelo conteúdo, com tamanho máximo e, para abrir ao público, antivírus (ClamAV) | Entregas e materiais vêm de muita gente |
| RNF-P06 | Correção de questões sempre no servidor, com gabarito fora do navegador (como hoje) | Certificado precisa valer alguma coisa |
| RNF-P07 | Páginas de venda rápidas e indexáveis: dados de curso (schema.org `Course`), Open Graph, sitemap por curso | Cada professor traz tráfego do Google e das redes |
| RNF-P08 | Acessibilidade WCAG 2.2 AA também no editor do professor | Professores com deficiência também publicam |
| RNF-P09 | Modelo pronto para `tenant_id` + Row-Level Security, sem ativar | Se um dia virar SaaS para outras escolas, não reescreve |

## Ordem

Isto entra depois da Fase 3 (vários cursos) do plano de migração da stack. Sem vários cursos, não há onde o professor publicar.

**1. Validar sem construir**

- [ ] Convidar 1 ou 2 professores colegas
- [ ] Cadastrar o curso deles você mesmo, como curso seu, e combinar o repasse por fora
- [ ] Ver se vende e o que eles pedem

**2. Mínimo para o primeiro professor de verdade**

- [ ] Contrato com o professor e termos atualizados; conversa com o contador
- [ ] Conta de professor por convite, perfil público, permissões por curso e teste de isolamento
- [ ] Criar curso, editor por blocos, aulas de amostra, revisão e aprovação
- [ ] Blocos novos: várias corretas, verdadeiro ou falso, lacunas e ordenar em texto, numérica, material protegido
- [ ] Split no gateway, comissão, extrato do professor, reembolso de 7 dias
- [ ] Vitrine, página de venda, "Meus cursos" e certificado por curso

**3. Logo depois**

- [ ] Dissertativa e entrega de trabalho com correção pelo professor
- [ ] Painel do professor, cupons, avisos, avaliações, anotações
- [ ] Fórmulas (LaTeX), associar colunas, aula ao vivo

**4. Só antes de abrir para qualquer professor**

- [ ] Denúncia, retirada por direito autoral, antivírus nos envios
- [ ] Limites de armazenamento e vídeo por professor
