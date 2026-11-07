<!-- Arquivo GERADO por tools/custos/custos.py a partir de data/custos.json. Não edite à mão. -->

# Custos: o que construir, o que pegar aberto e o que pagar

[← Índice da documentação](README.md)

Regra geral: **pague só pelo que custa menos que as suas horas ou exige confiança e legalidade.** O resto você constrói (se diferencia você) ou pega aberto (se é infraestrutura comum). Revisão a cada 3 meses (passo do roteiro).

## A regra

**Construir você mesmo**

- O que diferencia você e vira produto: sistemas AM, Fábrica de aulas, kit de sites, radar, agentes do grupo, MCP próprio
- Cola entre ferramentas: scripts, verificadores, geradores (pouco código, muito ganho)

**Pegar código aberto e hospedar**

- Infraestrutura que todo mundo precisa e ninguém paga por ela: n8n, Postiz, Cal.com, Umami, Uptime Kuma, Grafana, Paperless, Home Assistant, LiteLLM, Ollama, llama.cpp, Whisper, Listmonk, GlitchTip, Keycloak
- Modelos abertos com licença Apache 2.0 ou MIT para o que vira produto
- n8n: a licença permite uso interno e nos seus fluxos; não permite revender o próprio n8n como serviço

**Pagar**

- Só quando custa menos que as suas horas ou quando exige confiança/legalidade: Claude (uma IA só), domínio, Hostinger já pago, taxas por venda, contador e certificado quando houver CNPJ
- Toda assinatura passa pela auditoria trimestral e pela cascata

## Item por item

| Decisão | Item | Hoje | Alternativa | Por quê |
|---|---|---|---|---|
| **testar grátis** | ChatGPT pago | mensal | ChatGPT Go grátis pelo Nubank (1 mês; 3 meses no Nubank+; 1 ano no Ultravioleta), depois R$ 39,99 se for usado toda semana | Segunda IA para imagens, voz e quando o limite do Claude acabar. Plus (R$ 99,90) só se o Go não bastar. |
| **testar grátis** | Z.AI (GLM, plano de código) | mensal baixo | Usar como reserva do Claude Code quando o limite acabar | Plano de código barato que funciona em ferramentas compatíveis com o Claude Code; o próprio Akita monitora no ai-usagebar. Confira preço, limites e política de dados antes. |
| **usar barato** | DeepSeek | grátis / API muito barata | Chat grátis; API pelo gateway como 'barato' | Ótimo custo para rascunho em volume. Os dados ficam em servidores na China: nada sensível, nada de aluno, nada de cliente. |
| **cortar** | Agentes de código do Google | saiu do ar no grátis | Copilot Pro e Codex como reservas de código | O Gemini CLI parou para contas pessoais sem licença paga em 18/06/2026; o Antigravity tem acesso ampliado só no Pro. |
| **cortar** | Grok | pago | Grátis, se quiser ver o que está em alta no X | O diferencial é o X em tempo real; não resolve aula, código nem setup melhor que as outras. |
| **cortar uma** | Alura · Rocketseat · Udemy | mensal | Ficar com uma plataforma na renovação + Microsoft Learn, roadmap.sh e documentação oficial (grátis) | Regra já decidida: nenhum curso novo até o cartão zerar. |
| **trocar** | Gemini pago | mensal | Google AI Plus (R$ 24,99, com 200 GB) no lugar do Google One atual, se o seu plano for de até 200 GB | Quase sem custo extra: troca o armazenamento que você já paga por armazenamento + Gemini Pro + NotebookLM com mais uso. Melhor IA para rascunhar aulas a partir das fontes. |
| **trocar** | SonarQube Cloud | grátis só para público | Semgrep CE no CI (já no repositório padrão) | Repositório privado no Sonar é pago; o Semgrep cobre de graça. |
| **trocar para comercial** | Vercel | grátis (Hobby) | Cloudflare Pages ou GitHub Pages (grátis e permitem uso comercial) ou o Hostinger que você já paga | O plano Hobby da Vercel é para uso pessoal, não comercial: site de cliente ou de venda não pode ficar nele. |
| **adiar** | API de NFS-e | mensal | Emissor nacional da NFS-e (gov, grátis) enquanto for MEI | API só quando o volume de notas pedir. |
| **adiar** | Anúncios pagos | por uso | Conteúdo orgânico + SEO + indicação | Só depois de uma oferta vender sem anúncio; regras de corte já no setup. |
| **adiar** | Backblaze B2 | por TB | Disco externo + Google Drive que você já paga (restic via rclone) | Uma nuvem de backup só; use a que já está paga. |
| **adiar** | Certificado digital e-CNPJ | anual | — | Só quando houver CNPJ. |
| **adiar** | Chave física (YubiKey) | compra | App 2FA no celular + códigos de recuperação no cofre | Bom, mas não urgente. |
| **adiar** | Claude Max (5x) | US$ 100 por mês | Pro + Google AI Plus + ChatGPT Go grátis + modelos locais + Gemini API grátis no gateway | É a solução direta para o limite, mas custa caro hoje. Entra quando uma renda passar no portão e o limite ainda travar o trabalho. |
| **adiar** | Conector Upwork | créditos por proposta | — | Só com inglês B1. |
| **adiar** | Dublagem (ElevenLabs) | mensal | Dublagem automática do YouTube, quando disponível no canal | Só depois de um curso vender em português. |
| **adiar** | Influenciadores e newsletters | por uso | Parcerias por permuta | Só com oferta validada. |
| **adiar** | Servidor caseiro | compra | Um PC usado barato ou o notebook antigo como servidor | Servidor não precisa de máquina nova. |
| **adiar** | Voz clonada (ElevenLabs) | mensal | OpenVoice V2 (MIT) ou Piper (vozes prontas) locais | Pagar só no mês em que um curso pago estiver sendo gravado; testar antes o aberto. |
| **adiar** | Workstation com GPU | compra | Kaggle, Colab, GPU por hora, cluster na rede | Comprar só quando o aluguel passar do valor da parcela por 6 meses seguidos. |
| **adiar** | YouTube membros | por venda | — | Depende de canal monetizado. |
| **adiar** | vLLM em GPU alugada | por hora | Ollama local e gateway | Só quando um modelo seu tiver uso real. |
| **limitar** | Claude por API (agentes) | por uso | Modelos locais pelo gateway para tarefas simples | Teto mensal no LiteLLM; 'local' por padrão, 'rapido' só quando o eval mostrar que o local não basta. |
| **limitar** | GPU por hora | por hora | Kaggle e Colab grátis primeiro | Alugar só para o que não cabe no grátis, com teto e desligando ao terminar. |
| **usar grátis** | Gemini API (cota grátis do AI Studio) | grátis (cota) | — | Rascunhos em lote pelo gateway sem gastar o Claude. Na cota grátis o Google pode usar os dados para melhorar produtos: nada sensível, nada de aluno. |
| **usar grátis** | GitHub Copilot | mensal | GitHub Education como PROFESSOR (Copilot Pro), não como estudante | Professor verificado ganha o Pro grátis, com agente na nuvem e agentes de terceiros; o plano de estudante exclui os agentes de terceiros. Motor da esteira de sites. |
| **usar grátis** | OpenRouter | por uso (alguns modelos grátis) | — | Uma chave para dezenas de modelos, inclusive grátis com limite; bom reserva no gateway. Confira a política de dados de cada modelo. |
| **usar grátis** | Perplexity | grátis | — | Pesquisa com fontes citadas no plano grátis; Pro só se aparecer de graça por promoção. |
| **manter grátis** | Anki | grátis no PC | AnkiDroid (grátis) no celular | O app pago é só o de iPhone. |
| **manter grátis** | Cal.com | grátis | Auto-hospedar se precisar de mais | O plano individual grátis basta. |
| **manter grátis** | Canva | grátis | Krita e Inkscape | Pro só se um cliente pagar por isso. |
| **manter grátis** | DaVinci Resolve | grátis | Kdenlive | A versão grátis basta. |
| **manter grátis** | MailerLite | grátis (limite) | Listmonk auto-hospedado + envio barato (SES/Resend) | O plano grátis encolheu em 2025: confira o limite. Passou dele, Listmonk custa centavos. |
| **manter grátis** | Sentry | grátis (cota) | GlitchTip auto-hospedado se passar da cota | A cota grátis basta no começo. |
| **manter grátis** | Tailscale | grátis (pessoal) | Headscale auto-hospedado se um dia precisar | O plano pessoal grátis cobre todos os seus aparelhos. |
| **usar o que já paga** | Codex (OpenAI) | incluso em planos do ChatGPT | Usar só se vier junto com o plano do ChatGPT que você tiver | Bom como segunda opinião de código quando o limite do Claude acabar; não vale assinar à parte. |
| **usar o que já paga** | E-mail profissional | incluso | E-mail do plano Hostinger; Cloudflare Email Routing para encaminhar | Não contratar Google Workspace agora. |
| **manter** | ActivityWatch | grátis | — | Código aberto. |
| **manter** | Claude (assinatura) | mensal | — | A ferramenta que mais devolve hora sua: código, setup, conteúdo. A única IA paga. |
| **manter** | Domínio (Registro.br) | anual | — | Barato e necessário. |
| **manter** | Gateway Pix (Asaas) | por venda | Mercado Pago, que você já usa | Sem mensalidade; paga só quando vende. |
| **manter** | Google One | mensal | — | Já pago; vira o destino do backup criptografado. |
| **manter** | Hostinger | anual | — | Já pago; hospeda os sites dos clientes e o e-mail profissional sem custo extra. |
| **manter** | Hotmart / Kiwify | por venda | — | Sem mensalidade. |
| **manter** | Postiz | grátis (auto-hospedado) | Agendador nativo das redes | Código aberto no seu PC. |
| **manter** | Umami | grátis | — | Auto-hospedado ou plano grátis. |
| **manter** | Zoomcamp e cursos de IA | grátis | — | Os Zoomcamps são gratuitos. |
| **manter** | restic | grátis | — | Código aberto. |
| **regra** | Hardware novo em geral | compra | Comprar só o que um passo do roteiro bloqueia | Cada compra entra pelo Caixa da Casa e pela cascata. |

| Decisão | Itens |
|---|---:|
| testar grátis | 2 |
| usar barato | 1 |
| cortar | 2 |
| cortar uma | 1 |
| trocar | 2 |
| trocar para comercial | 1 |
| adiar | 14 |
| limitar | 2 |
| usar grátis | 4 |
| manter grátis | 7 |
| usar o que já paga | 2 |
| manter | 11 |
| regra | 1 |

## Modelos abertos para cada tarefa

Para o que vira produto, prefira licença Apache 2.0 ou MIT e confira a licença do tamanho exato que baixar.

| Tarefa | Modelo | Licença | Onde roda |
|---|---|---|---|
| Chat e agentes locais | Qwen (maioria dos tamanhos), Mistral 7B, Phi | Apache 2.0 / MIT (confira cada tamanho) | Ollama no notebook (até ~14B com offload) |
| Código local | Qwen Coder | Apache 2.0 (confira o tamanho) | Ollama |
| Busca nas suas notas (embeddings para RAG) | bge-m3, nomic-embed-text | MIT / Apache 2.0 | Ollama, até em CPU |
| Transcrição de aulas e vídeos | Whisper (faster-whisper) | MIT | GPU 4 GB ou CPU |
| Voz | Piper (vozes prontas) · OpenVoice V2 (clonar a SUA voz) | MIT | CPU |
| OCR de documentos | Tesseract (dentro do Paperless) | Apache 2.0 | CPU |
| Imagens | FLUX.1 schnell | Apache 2.0 | GPU alugada ou Colab (pesado para 4 GB) |
| Modelos grandes para estudo | Llama, Gemma | Licenças próprias com restrições: leia antes de usar em produto | Quantizados ou alugados |

## Qual IA para cada tarefa

| Tarefa | IA | Por quê |
|---|---|---|
| Planejar o setup, arquitetura, revisão de código e do que vai para cliente | Claude (Pro) | Melhor raciocínio longo e coerência com o repositório |
| Código no setup e nos sistemas | Claude Code; Copilot (agente na nuvem) para issues pequenas | Lê e muda o repositório com testes |
| Rascunho de aulas e documentos a partir das ementas e fontes oficiais | NotebookLM / Gemini (AI Plus) | Responde preso às fontes que você carrega; economiza o limite do Claude |
| Revisar a aula pronta contra as suas regras | Claude | Uma revisão curta gasta pouco limite |
| Pesquisa com fontes | Perplexity (grátis) ou Gemini; Claude para fechar a decisão | Busca barata, decisão no Claude |
| Imagens, capas e voz de conversa | ChatGPT Go | Ponto forte dele |
| Rascunho em volume pela API (descrições, variações, resumos) | DeepSeek ou OpenRouter grátis pelo gateway | Custo perto de zero; nada sensível |
| Código quando o limite do Claude acabar | Copilot Pro (grátis para professor) ou Codex do ChatGPT Go | Créditos de outra empresa; revisão final no Claude. Detalhes em docs/recursos.md |
| Transcrever, resumir e rascunhar em volume | Modelos locais (Ollama) ou Gemini API grátis pelo gateway | Sem custo e sem gastar limite |
| Tudo que tem dado sensível (aluno, finanças, senha) | Nenhuma IA na nuvem; modelo local ou à mão | Segurança acima de conveniência |

## Outras ferramentas de IA: o que acrescentam e quando

| Categoria | Exemplos | Como gera renda | Decisão | Quando |
|---|---|---|---|---|
| Vídeo curto a partir dos seus vídeos longos | Ferramentas de cortes automáticos; aberto: Whisper + FFmpeg + script seu | Mais alcance no Reels/Shorts → isca do mini-curso e dos sites | construir aberto | Quando o canal tiver 10 vídeos longos |
| Avatar e vídeo falado | Avatares de IA (só com o SEU rosto e a SUA voz) | Vídeos de venda e aulas sem gravar tudo de novo | adiar | Depois que um curso vender; nunca rosto ou voz de aluno |
| Imagens e capas | ChatGPT Go (imagens), FLUX.1 schnell (aberto) | Capas de curso, posts, mockups de sites para proposta | usar o que já tem | Agora |
| Apresentações e propostas | Geradores de slides com IA; Claude Slides que você já tem | Proposta bonita em minutos → fecha mais sites | usar o que já tem | Agora |
| Música e trilha | Geradores de música com IA (confira a licença comercial do plano) | Trilha própria nos vídeos, sem direito autoral de terceiros | adiar | Quando o canal monetizar |
| Prospecção e enriquecimento de leads | Ferramentas de lista e enriquecimento B2B; aberto: o seu prospector com dados públicos | Mais conversas com comércio local | construir aberto | Fase 24 horas (prospector) |
| Atendimento omnicanal com IA | Chatwoot (aberto) + agente atendente pelo gateway | Responde WhatsApp/Instagram/site rápido, com passagem para você | construir aberto | Com 3 clientes de sites ou o primeiro curso |
| SEO e conteúdo com IA | Search Console + Umami + agente de pauta pelo gateway | Tráfego orgânico para o blog e as páginas de venda | construir aberto | Quando o site novo for ao ar |
| Agente no navegador | Claude in Chrome (você já tem) | Tarefas repetitivas em sites sem API | usar o que já tem | Agora, com aprovação nas ações |
| Transcrição e notas de reuniões e aulas | Whisper local; NotebookLM | Cada aula vira resumo, exercícios e post | usar o que já tem | Agora |

## Fazer o limite do Claude durar

- Uma conversa por tarefa: conversa longa relê tudo a cada mensagem e consome o limite muito mais rápido.
- Projects com os arquivos fixos (regras, ementas, setup) em vez de colar tudo de novo.
- Modelo mais leve do Claude para tarefas simples; o mais forte só para planejar e revisar.
- Rascunho na IA mais barata, revisão final no Claude.
- Peça o resultado em arquivo ou no repositório, não em textos longos repetidos no chat.

Coerência entre IAs: as mesmas regras em CLAUDE.md, AGENTS.md e GEMINI.md (scripts/wsl/regras-ia.sh).

Assinaturas pessoais (streaming, apps) ficam fora do repositório: confira no Caixa da Casa.
