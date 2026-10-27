# Catálogo do HTML — Avaliação da plataforma

Oct 6, 2026 · @Alan Mateus

A plataforma já tem tudo o que um curso online pago precisa para funcionar — contas, planos, vendas, painel, aulas com exercícios, checkpoint, certificado e videoaulas. O que falta é conteúdo (1 dos 18 módulos escrito) e colocar no ar com e-mail e pagamento reais.

## Como as peças se encaixam

&#91;embedded content: arquitetura · navegador, Caddy, sistema, banco e serviços externos\]

Tudo roda num único servidor com Docker. O site público gratuito é gerado à parte (gerar-site-publico.py) e vai para GitHub Pages ou Vercel, sem sistema por trás.

## O que foi criado

São 48 páginas, 82 endereços de API, 23 tabelas no banco e cerca de 5.200 linhas de C#. Os testes automáticos conferem 216 situações na API e 56 nas telas.

| Área | O que tem | Quem usa |
| --- | --- | --- |
| Site didático | Catálogo de códigos, Dicionário, Verificador, página de IA, Documentação com o mapa dos 18 módulos | Qualquer pessoa |
| Passo a passo | 10 passos, do preparar o computador ao publicar no GitHub Pages | Passos 1–4 livres; 5–10 com conta grátis |
| Projetos | 12 projetos especificados; páginas prontas dos Projetos 1 a 4, com vídeo do resultado esperado | Projeto 1 livre; os outros no plano |
| Aulas | Módulo 1 (Lógica com JavaScript): 10 lições, 6 tipos de exercício, editor de código isolado, visualizador passo a passo, analogias com limite, níveis 2 e 3 | Lição 1 livre, 2 com conta, 3–10 no plano |
| Estudo contínuo | Revisão espaçada (1, 3, 7, 21 e 60 dias), progresso salvo na conta, dúvidas por lição | Alunos |
| Avaliação | Checkpoint de 14 questões corrigido no servidor, 3 tentativas por dia, certificado com código de conferência | Alunos com plano |
| Videoaulas | Vídeo na própria plataforma ou no Bunny Stream, link que expira, continuar de onde parou, velocidade, conclusão em 90%, próxima aula | Alunos e professor |
| Contas | Cadastro com confirmação por e-mail, senha criada no link, esqueci a senha, 2 etapas, códigos de recuperação | Todos |
| Vendas | Kiwify, Hotmart e Mercado Pago por aviso automático; venda direta; cupons; códigos de acesso para escolas; teste grátis; reembolso tira o acesso | Equipe financeira |
| Painel | 12 abas: Painel, Usuários, Vendas, Produtos e preços, Cupons, Códigos de acesso, O que é pago, Aulas, Dúvidas, Estudos, Avisos das plataformas, Auditoria | Equipe, por papel |
| Editor de aulas | Módulos, lições, checkpoint, barra de blocos, pré-visualização, publicar, versões, imagens, PDFs e vídeos, baixar tudo em .zip | Professor e administrador |
| Privacidade | Baixar os próprios dados e excluir a conta (LGPD), Termos e Política de privacidade | Alunos |
| Operação | Docker Compose, HTTPS automático, scripts do servidor (preparar, criar .env, atualizar, backup) e guia da Hostinger | Você |
| Site público | Gerador da versão grátis para o GitHub Pages, sem nada pago | Alunos da escola |

## Requisitos funcionais

O que o sistema **faz hoje**. Tudo abaixo passa nos testes automáticos; a coluna Situação diz o que ainda falta testar no mundo real.

| Código | Requisito | Situação |
| --- | --- | --- |
| RF01 | Cadastro com confirmação de e-mail por link | Pronto (falta SMTP real) |
| RF02 | Login com senha, bloqueio após tentativas e verificação em duas etapas (TOTP) com códigos de recuperação | Pronto |
| RF03 | Recuperar senha por e-mail | Pronto (falta SMTP real) |
| RF04 | Papéis aluno, professor e admin, com permissões separadas | Pronto |
| RF05 | Portão de conteúdo por página: livre, conta, pago, equipe, bloqueado | Pronto |
| RF06 | Planos, webhook de venda, cupons, códigos de acesso, período de teste e reembolso | Pronto (falta teste com gateway real) |
| RF07 | Aulas com exercícios corrigidos no servidor, checkpoints e revisão espaçada | Pronto |
| RF08 | Progresso salvo na conta e sincronizado entre aparelhos | Pronto |
| RF09 | Dúvidas dos alunos respondidas pela equipe | Pronto |
| RF10 | Certificado ao concluir, com verificação pública | Pronto |
| RF11 | Editor de aulas no Painel: módulos, lições, rascunho × publicado, prévia | Pronto |
| RF12 | Publicação atômica e histórico de 30 versões por lição, com restauração | Pronto |
| RF13 | Envio de imagens e PDFs para as aulas | Pronto |
| RF14 | Videoaulas (local ou Bunny Stream): retomar de onde parou, velocidade, playlist, próxima aula automática | Pronto (Bunny sem teste com conta real) |
| RF15 | Aula concluída só ao assistir 90% do vídeo de verdade | Pronto |
| RF16 | Exportar módulo em .zip | Pronto (importar ainda não existe) |
| RF17 | LGPD: aluno baixa os próprios dados e apaga a conta | Pronto |
| RF18 | Auditoria das ações da equipe | Pronto |
| RF19 | Relatório de estudos do aluno | Pronto |
| RF20 | Gerador do site público gratuito (GitHub Pages / Vercel) | Pronto |

## Requisitos não funcionais

| Código | Categoria | Como está atendido |
| --- | --- | --- |
| RNF01 | Segurança | CSP rígida, cabeçalho anti-CSRF, cookies `__Host-`, HSTS, limites de requisição por rota, senhas com Identity, 2FA obrigatório para a equipe |
| RNF02 | Segurança do conteúdo | Gabaritos e vídeos nunca ficam no navegador; links de vídeo assinados (6 h local, 2 h Bunny) e presos ao usuário; arquivos conferidos pelo conteúdo, não pela extensão |
| RNF03 | Disponibilidade | Publicação troca a pasta inteira de uma vez; se o gerador falhar, a última versão boa continua no ar |
| RNF04 | Privacidade | LGPD: exportação e exclusão de dados; e-mails e IPs só onde necessários |
| RNF05 | Implantação | Docker Compose + Caddy com HTTPS automático; scripts de preparo, atualização e backup |
| RNF06 | Recuperação | Backup diário do banco (30 dias) e das pastas de mídia e vídeo |
| RNF07 | Evolução do banco | Migrações SQL numeradas, aplicadas na subida |
| RNF08 | Testabilidade | \~220 verificações de API e 56 de tela (navegador real) |
| RNF09 | Manutenção | Código e mensagens em português, sem ORM, SQL explícito, poucas dependências |
| RNF10 | Acessibilidade (básico) | HTML semântico, foco visível, `aria-live` nos avisos, funciona no celular |
| RNF11 | Desempenho | Site estático servido direto; só login, progresso e vídeo passam pela API |

## O que melhorar e organizar

Sendo direto: a parte técnica está à frente do conteúdo e da operação. O que mais pesa hoje:

**Conteúdo (o maior gargalo)**

- Só 1 dos 18 módulos está escrito no formato novo; os capítulos antigos `doc-*` seguem no formato antigo.
- Projetos 5 a 12 não têm página; a pasta de vídeos está vazia.
- Páginas legais (termos, privacidade, reembolso) ainda são modelos — precisam do texto real antes de vender.

**Ainda não provado no mundo real**

- E-mail: falta configurar SMTP de verdade (Resend, Brevo ou SES) e testar cadastro e senha esquecida.
- Pagamento: nenhum webhook real recebido ainda; faça uma compra de teste ponta a ponta.
- Bunny Stream: o código segue a documentação, mas nunca tocou um vídeo de uma conta real.
- Restauração: o backup existe, mas nunca foi restaurado. Backup não testado não é backup.

**Organização do projeto**

- Duas cópias do site (`pagina-completa` e `plataforma/site`): escolha uma só e faça a outra ser gerada ou ligada.
- Páginas geradas (`aula-*.html`) estão no repositório: deveriam ser geradas no build, não versionadas.
- Sem CI: os testes só rodam quando alguém lembra.
- Teste local tem atrito (e-mail vira arquivo, admin inicial fixo no compose): um script `iniciar-local` resolveria.
- Comentários desatualizados em pontos isolados (ex.: `video.js` diz 6 h para o Bunny, que é 2 h).

**Limites da arquitetura atual**

- Um servidor só: se ele cair, tudo cai. Aceitável no lançamento, mas tenha monitoramento.
- Imagens enviadas pelo Painel são públicas por endereço (vídeos não). Ok para ilustrações; não suba material pago como PDF ali.
- Sem `sitemap.xml`, `robots.txt`, metadados de compartilhamento nem analytics: o site público ainda não trabalha para ser encontrado.

## O que acrescentar

**Novos requisitos funcionais**

| Código | Recurso | Por quê |
| --- | --- | --- |
| RF21 | Importar módulo (.zip) | Escrever no computador e subir de uma vez; par do exportar |
| RF22 | Layout de aula estilo Udemy (vídeo grande, abas Resumo/Exercícios/Dúvidas/Materiais, lateral fixa) | Experiência que o aluno já conhece |
| RF23 | "Continuar de onde parei" na página de aulas | Maior motivo de retorno do aluno |
| RF24 | Anotações e marcadores com tempo do vídeo | Estudo ativo |
| RF25 | Materiais para baixar por aula (protegidos) | Hoje mídia é pública por endereço |
| RF26 | Legendas (VTT) | Acessibilidade e estudo sem som |
| RF27 | Busca nas aulas | Com 18 módulos, achar algo vira problema |
| RF28 | E-mails automáticos: boas-vindas, carrinho abandonado, aluno parado | Venda e retenção |
| RF29 | Sequência de dias estudando e metas | Hábito |
| RF30 | Turmas para escolas com painel do professor | Abre venda B2B |
| RF31 | Comunidade ou fórum entre alunos | Reduz dúvidas repetidas |
| RF32 | Envio de vídeo para o Bunny direto do Painel | Hoje é preciso colar o ID |
| RF33 | Painel de métricas: vendas, conclusão, onde os alunos param | Decidir com dados |

**Novos requisitos não funcionais**

| Código | Requisito |
| --- | --- |
| RNF12 | CI no GitHub Actions: rodar os testes a cada push e publicar automaticamente |
| RNF13 | Monitoramento de disponibilidade e alerta de erro (UptimeRobot + logs) |
| RNF14 | Restauração de backup ensaiada a cada mês, com cópia fora do servidor |
| RNF15 | SEO: sitemap, robots, Open Graph, dados estruturados de curso |
| RNF16 | Auditoria de acessibilidade WCAG 2.2 AA |
| RNF17 | Marca d'água com e-mail do aluno nos vídeos (contra pirataria) |
| RNF18 | PWA / leitura offline das aulas de texto |
| RNF19 | Preparar para mais de uma instância (chaves e arquivos fora do contêiner) |

## Ordem sugerida

Vender antes de enfeitar: primeiro o que bloqueia o lançamento, depois o que melhora a experiência.

- [ ] Escrever os módulos 2 e 3 (o produto é o conteúdo)
- [ ] Criar o importar módulo (.zip) para acelerar a escrita
- [ ] Configurar SMTP real e testar cadastro e senha esquecida
- [ ] Trocar as páginas legais pelo texto real
- [ ] Fazer uma compra de teste ponta a ponta no gateway
- [ ] Colocar no ar na Hostinger e ensaiar uma restauração de backup
- [ ] Ligar CI e monitoramento
- [ ] Unificar as duas cópias do site e tirar páginas geradas do repositório
- [ ] Layout estilo Udemy + "continuar de onde parei"
- [ ] Testar o Bunny com conta real e gravar os vídeos do módulo 1
- [ ] SEO e sitemap no site público
- [ ] E-mails automáticos e painel de métricas
