# 4 · Automação e escala

[← Operação do grupo](README.md)

Automatizar não é tirar você de tudo. É tirar você do que se repete, para sobrar tempo para o que só você faz: ensinar, escrever, decidir e criar a primeira versão.

## Os quatro níveis

| Nível | O que é | Exemplo |
|---|---|---|
| **0 · Manual** | Você faz | Gravar a aula, primeira conversa com um cliente B2B |
| **1 · Padronizado** | Você faz seguindo modelo ou checklist | Proposta a partir dos pacotes, POP de abertura da loja |
| **2 · Assistido** | Um agente prepara, você aprova | Cortes e legendas, resposta a avaliação, rascunho de orçamento |
| **3 · Automático com alerta** | Roda sozinho e avisa quando algo sai do normal | Entrega do curso após o pagamento, lembrete de cobrança, backup, relatório semanal |

Regra: **tudo passa por 1 antes de ir para 2 ou 3.** Automatizar um processo que nem você faz sempre igual só automatiza a bagunça.

## O que nunca fica no nível 3

- Prometer preço, prazo ou desconto fora da tabela.
- Publicar em seu nome sem aprovação.
- Mexer em dinheiro (estorno, pagamento a fornecedor, repasse) sem confirmação.
- Responder reclamação séria ou qualquer coisa jurídica.
- Decidir sobre dados pessoais de clientes e alunos.

## Os agentes do grupo

Agentes do Claude Code e fluxos do n8n, cada um com um papel estreito, as permissões mínimas e registro de tudo o que fez.

| Agente | Faz | Nível | Liga com |
|---|---|---|---|
| `atendente` | Responde perguntas frequentes no WhatsApp de cada negócio, mostra catálogo e horários, agenda; passa para você o que não souber | 2, depois 3 nas perguntas frequentes | WhatsApp Business, catálogo, agenda |
| `orcamentista` | Monta proposta a partir dos pacotes e do histórico | 2 | Sites, automação, assistência, eventos |
| `cobrador` | Lembra vencimentos e envia Pix; avisa você nos atrasos | 3 | Mercado Pago, Asaas, AM Rendara |
| `pos-venda` | Pergunta a nota (NPS), pede avaliação no Google, oferece o próximo produto da jornada | 3 | CRM, Google Perfil, MailerLite |
| `editor-de-conteudo` | Transforma gravações e textos em peças para cada rede | 2 | Whisper, Postiz, Telegram |
| `analista-semanal` | Lê o painel toda segunda e manda 3 fatos e 1 sugestão de decisão | 3 (só leitura) | Painel do grupo |
| `comprador` | Sugere a lista de compras pelo estoque mínimo e pela previsão | 2 | AM Kaixara |
| `organizador-fiscal` | Junta notas, extratos e vendas do mês para o contador e para o carnê-leão | 2 | Bancos, plataformas, AM Rendara |
| `revisor-de-oferta` | Confere cada lançamento contra o padrão de qualidade | 2 | Repositório da oferta |

Os agentes da editora (revisor técnico, verificador de gabarito e os demais) seguem em [Editora AMS Silva](../editora/02-arquitetura-de-producao.md).

## A alavanca de escala de cada tipo

| Tipo de oferta | O que limita | Como escala |
|---|---|---|
| **Infoproduto e livro** | Alcance | Tráfego, afiliados, Udemy, tradução e dublagem; custo por cliente perto de zero |
| **SaaS** | Onboarding e suporte | Autoatendimento, base de ajuda, white-label, licença para outras cidades |
| **Serviço produtizado** (sites, automação, presença digital) | Suas horas | Pacotes fixos, modelos reaproveitados, depois um freelancer treinado no seu padrão |
| **Serviço local** (assistência, aulas, eventos) | Gente e lugar | Planos mensais, POPs, técnico contratado, agenda cheia antes de crescer |
| **Negócio físico** (restaurantes, entregas) | Capital e gestão | Processos escritos, gerente, sistemas AM, depois réplica ou licença do modelo |
| **Mídia** | Constância | Flywheel, agendamento, dublagem para outros idiomas |

## Por onde começar a automatizar

Na ordem do que mais devolve horas para você:

1. **Entrega automática** dos infoprodutos após o pagamento (as plataformas já fazem; só configurar).
2. **Agenda com pagamento antecipado** para aulas e eventos.
3. **Editor-de-conteudo + aprovação no celular + Postiz**.
4. **Pós-venda com pedido de avaliação.**
5. **Relatório semanal do painel.**
6. **Atendente de WhatsApp** só quando houver volume de perguntas repetidas para treinar.
