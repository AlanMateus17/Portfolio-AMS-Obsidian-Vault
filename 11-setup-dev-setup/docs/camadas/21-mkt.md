<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 21 · Marketing, automação e medição

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** O que é publicado e anunciado aqui leva às plataformas de venda; cada venda volta como dado para o banco de métricas.

**30 blocos** · 13 precisam de conta · 14 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_mkt["Marketing, automação e medição"]
    n_ads["Meta Ads (Instagram, Facebook)"]
    n_isca["Isca grátis + sequência de e-mails"]
    n_mailer["MailerLite"]
    n_postiz["Postiz (agendador)"]
    n_aprov["Aprovação no celular"]
    n_tg["Telegram (avisos)"]
    n_n8n["n8n"]
    n_horario["Algoritmo de horário"]
    n_pixel["Tags de conversão (Pixel, Google…)"]
    n_utm["Padrão de UTM"]
    n_gads["Google e YouTube Ads"]
    n_ttads["TikTok Ads"]
    n_regras["Regras de corte"]
    n_calc["Lucro por Venda (calculadora)"]
    n_hooks["Webhooks de venda"]
    n_metrics["Banco de métricas (PostgreSQL)"]
    n_painel["Painel de lucro (Grafana)"]
    n_afprog["Programa de afiliados"]
    n_prosp["Prospecção de parceiros"]
    n_dub["Dublagem (YouTube + ElevenLabs)"]
    n_spotads["Spotify Ad Studio"]
    n_kwaiads["Kwai Ads"]
    n_pinads["Pinterest Ads"]
    n_liads["LinkedIn Ads"]
    n_nativo["Mídia nativa (Taboola, Outbrain)"]
    n_infl["Influenciadores e newsletters"]
    n_posthog["PostHog (funil e gravações)"]
    n_growthbook["GrowthBook (testes A/B)"]
    n_formbricks["Formbricks (NPS e pesquisas)"]
    n_adaptadores["Adaptadores do núcleo"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_nucleo["Núcleo AMtech (banco central)"]
    n_oanal["Analista semanal"]
    n_oatend["Agente atendente (WhatsApp)"]
    n_oaval["NPS e avaliações"]
    n_ocob["Agente cobrador"]
    n_ocrm["CRM único + LGPD"]
    n_oedit["Agente editor de conteúdo"]
    n_opipe["Pipeline de conteúdo"]
    n_opos["Agente pós-venda"]
    n_overif["Verificadores"]
    n_roi["Lucro por ferramenta"]
    n_simulacao["Simulação noturna de ponta a ponta"]
  end
  subgraph L_pub["Público e canais"]
    n_facebook["Facebook"]
    n_ig["Instagram"]
    n_li["LinkedIn"]
    n_tiktok["TikTok"]
    n_yt["YouTube"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_eduzz["Eduzz"]
    n_hotm["Hotmart"]
    n_kiwi["Kiwify"]
  end
  subgraph L_emp["Pessoa física: impostos e finanças"]
    n_financas["Financeiro local"]
    n_invoiceninja["Invoice Ninja (orçamentos)"]
    n_nfse["Carnê-leão (Receita Federal)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
    n_klaro["Klaro! (consentimento LGPD)"]
    n_mail["E-mail profissional (enviar e receber)"]
    n_site["Site pessoal + blog (Jekyll)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_livro["Livro Lógica e Máquina"]
  end
  subgraph L_neg["Negócios do grupo (Barbacena)"]
    n_radar["Radar de revenda"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bcurso["Curso por seção"]
    n_bkit["Kit edição especial"]
    n_trad["Traduções (espanhol, inglês)"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_voz["Voz clonada (ElevenLabs)"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_cf["Cloudflare (DNS, Pages, e-mail)"]
    n_stripecli["Stripe CLI (testar pagamentos)"]
    n_vm247["VM sempre ligada (Oracle grátis)"]
  end
  subgraph L_obs["Observabilidade"]
    n_graf["Grafana"]
    n_kuma["Uptime Kuma"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_docker["Docker + Compose"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_cml["Conector MailerLite"]
    n_cvid["Conector vidIQ"]
    n_pbiz["Plugins: small- business + marketing"]
  end
  subgraph L_dados["Dados e treino de IA"]
    n_dbt["dbt Core"]
    n_grocy["Grocy"]
    n_metabase["Metabase (painéis)"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_jarvis["Jarvis (porta única dos agentes)"]
    n_litellm["Gateway de modelos (LiteLLM)"]
    n_mcp["Servidores MCP"]
    n_oll["Ollama"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_rotinas["Rotinas agendadas"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_aw["ActivityWatch"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_politicaaut["Política de autonomia"]
    n_restauracao["Teste de restauração"]
  end
  subgraph L_hw["Hardware"]
    n_cel["Celular"]
    n_nas["Servidor caseiro (NAS + serviços)"]
  end
  n_ads -->|"alcance pago"| n_ig
  n_ads -->|"gasto por campanha"| n_metrics
  n_ads -->|"leva à isca grátis"| n_isca
  n_pixel -->|"otimiza para venda"| n_ads
  n_utm -->|"marca os links"| n_ads
  n_regras -->|"pausa ou escala"| n_ads
  n_calc -->|"custo máximo por clique"| n_ads
  n_isca -->|"sequência"| n_mailer
  n_inst -->|"captura o e-mail"| n_isca
  n_gads -->|"leva à isca grátis"| n_isca
  n_ttads -->|"leva à isca grátis"| n_isca
  n_kwaiads -->|"leva à isca grátis"| n_isca
  n_spotads -->|"leva à isca grátis"| n_isca
  n_pinads -->|"leva à isca grátis"| n_isca
  n_liads -->|"leva à isca grátis"| n_isca
  n_nativo -->|"leva à isca grátis"| n_isca
  n_infl -->|"leva à isca grátis"| n_isca
  n_livro -->|"capítulo grátis"| n_isca
  n_mailer -->|"leva à página de venda"| n_inst
  n_mailer -->|"lançamento"| n_hotm
  n_mail -->|"remetente"| n_mailer
  n_cml -->|"campanhas"| n_mailer
  n_n8n -->|"novo aluno → e-mail"| n_mailer
  n_site -->|"formulário da newsletter"| n_mailer
  n_ocrm -->|"etiquetas"| n_mailer
  n_postiz -->|"publica"| n_yt
  n_postiz -->|"publica"| n_ig
  n_postiz -->|"publica"| n_tiktok
  n_postiz -->|"publica"| n_facebook
  n_postiz -->|"publica"| n_li
  n_n8n -->|"manda o post aprovado"| n_postiz
  n_utm -->|"marca os links"| n_postiz
  n_nas -->|"roda 24 h"| n_postiz
  n_aprov -->|"libera"| n_n8n
  n_oedit -->|"fila de aprovação"| n_aprov
  n_tg -->|"aprovar ou recusar"| n_aprov
  n_jarvis -->|"ação pede o seu ok"| n_aprov
  n_tg -->|"notificação"| n_cel
  n_opipe -->|"aviso de peça pronta"| n_tg
  n_kuma -->|"alerta"| n_tg
  n_rotinas -->|"resumo da manhã"| n_tg
  n_grocy -->|"avisa ração e remédios"| n_tg
  n_jarvis -->|"conversa por"| n_tg
  n_politicaaut -->|"ok no celular"| n_tg
  n_simulacao -->|"relatório da manhã"| n_tg
  n_n8n -->|"grava"| n_metrics
  n_n8n -->|"roda"| n_ocob
  n_n8n -->|"roda"| n_opos
  n_n8n -->|"roda"| n_oatend
  n_n8n -->|"agentes do n8n usam"| n_litellm
  n_oll -->|"IA local nas automações"| n_n8n
  n_docker -->|"container"| n_n8n
  n_horario -->|"escolhe o horário"| n_n8n
  n_hooks -->|"dispara"| n_n8n
  n_nas -->|"roda 24 h"| n_n8n
  n_overif -->|"confere"| n_n8n
  n_kuma -->|"está no ar?"| n_n8n
  n_cf -->|"túnel dos webhooks"| n_n8n
  n_vm247 -->|"roda 24 h"| n_n8n
  n_adaptadores -->|"fluxos simples"| n_n8n
  n_metrics -->|"desempenho por horário"| n_horario
  n_pixel -->|"eventos de compra"| n_inst
  n_pixel -->|"otimiza para venda"| n_gads
  n_pixel -->|"otimiza para venda"| n_ttads
  n_pixel -->|"otimiza para venda"| n_kwaiads
  n_pixel -->|"otimiza para venda"| n_pinads
  n_pixel -->|"otimiza para venda"| n_liads
  n_pixel -->|"otimiza para venda"| n_nativo
  n_klaro -->|"libera as tags com aceite"| n_pixel
  n_utm -->|"marca os links"| n_gads
  n_utm -->|"marca os links"| n_ttads
  n_utm -->|"marca os links"| n_kwaiads
  n_utm -->|"marca os links"| n_spotads
  n_utm -->|"marca os links"| n_pinads
  n_utm -->|"marca os links"| n_liads
  n_utm -->|"marca os links"| n_nativo
  n_utm -->|"marca os links"| n_infl
  n_gads -->|"gasto"| n_metrics
  n_regras -->|"pausa ou escala"| n_gads
  n_calc -->|"custo máximo por clique"| n_gads
  n_ttads -->|"gasto"| n_metrics
  n_regras -->|"pausa ou escala"| n_ttads
  n_calc -->|"custo máximo por clique"| n_ttads
  n_regras -->|"pausa ou escala"| n_spotads
  n_regras -->|"pausa ou escala"| n_kwaiads
  n_regras -->|"pausa ou escala"| n_pinads
  n_regras -->|"pausa ou escala"| n_liads
  n_regras -->|"pausa ou escala"| n_nativo
  n_regras -->|"renova ou encerra parceria"| n_infl
  n_calc -->|"CPA e ROAS de empate"| n_regras
  n_painel -->|"dispara alertas"| n_regras
  n_calc -->|"comissão máxima"| n_afprog
  n_calc -->|"valor máximo do post"| n_infl
  n_calc -->|"custo máximo por clique"| n_kwaiads
  n_calc -->|"custo máximo por clique"| n_spotads
  n_calc -->|"custo máximo por clique"| n_pinads
  n_calc -->|"custo máximo por clique"| n_liads
  n_calc -->|"custo máximo por clique"| n_nativo
  n_calc -->|"preço e margem"| n_bkit
  n_calc -->|"preço e margem"| n_bcurso
  n_hotm -->|"venda e reembolso"| n_hooks
  n_kiwi -->|"venda e reembolso"| n_hooks
  n_eduzz -->|"venda e reembolso"| n_hooks
  n_invoiceninja -->|"avisa pagamentos"| n_hooks
  n_stripecli -->|"simula webhooks"| n_hooks
  n_metrics -->|"consultas"| n_painel
  n_metrics -->|"base do carnê-leão"| n_nfse
  n_metrics -->|"dados da semana"| n_oanal
  n_metrics -->|"tabelas brutas"| n_dbt
  n_spotads -->|"gasto"| n_metrics
  n_kwaiads -->|"gasto"| n_metrics
  n_pinads -->|"gasto"| n_metrics
  n_liads -->|"gasto"| n_metrics
  n_nativo -->|"gasto"| n_metrics
  n_infl -->|"custo do post"| n_metrics
  n_nas -->|"roda 24 h"| n_metrics
  n_mcp -->|"leitura (usuário do Grafana)"| n_metrics
  n_docker -->|"container"| n_metrics
  n_metabase -->|"lê"| n_metrics
  n_painel -->|"roda no Grafana"| n_graf
  n_dbt -->|"modelos limpos"| n_painel
  n_radar -->|"lucro por hora"| n_painel
  n_aw -->|"horas por renda"| n_painel
  n_financas -->|"sobra do mês"| n_painel
  n_restauracao -->|"resultado do teste"| n_painel
  n_roi -->|"resultado por ferramenta"| n_painel
  n_posthog -->|"conversão por página"| n_painel
  n_afprog -->|"afiliados cadastrados"| n_hotm
  n_prosp -->|"novos afiliados"| n_afprog
  n_cvid -->|"canais semelhantes"| n_prosp
  n_pbiz -->|"rascunho de propostas"| n_prosp
  n_dub -->|"faixas de áudio"| n_yt
  n_voz -->|"sua voz em outros idiomas"| n_dub
  n_trad -->|"voz em outros idiomas"| n_dub
  n_spotads -->|"lembrança da marca"| n_yt
  n_nativo -->|"leva aos artigos"| n_site
  n_infl -->|"link com cupom"| n_inst
  n_growthbook -->|"mede os testes"| n_posthog
  n_formbricks -->|"alimenta o NPS"| n_oaval
  n_adaptadores -->|"eventos"| n_nucleo
  n_simulacao -->|"testa a cadeia"| n_adaptadores
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_ads,n_isca,n_mailer,n_postiz,n_aprov,n_tg,n_n8n,n_horario,n_pixel,n_utm,n_gads,n_ttads,n_regras,n_calc,n_hooks,n_metrics,n_painel,n_afprog,n_prosp,n_dub,n_spotads,n_kwaiads,n_pinads,n_liads,n_nativo,n_infl,n_posthog,n_growthbook,n_formbricks,n_adaptadores desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Meta Ads (Instagram, Facebook)](#ads) | Remoto · precisa de conta · futuro | Primeiro canal pago: anúncios da isca grátis e remarketing do mini-curso. Desde jan/2026 a fatura tem +12,15% de impostos sobre a mídia. | passo 47.1 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Isca grátis + sequência de e-mails](#isca) | Local | Aula ou PDF grátis que captura o e-mail e abre uma sequência de 5 a 7 e-mails até o mini-curso. | passo 36.6 · Semanas 6 e 7 · dez/2026; passo 40.8 · Semanas 12 a 15 · jan a fev/2027 |
| [MailerLite](#mailer) | Remoto · precisa de conta | Newsletter do blog com grupos por tema e funil de lançamento. Você já escolheu o plano grátis. | passo 36.6 · Semanas 6 e 7 · dez/2026; passo 40.8 · Semanas 12 a 15 · jan a fev/2027; passo 46.8 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Postiz (agendador)](#postiz) | Local · futuro | Agendador open source (AGPL-3.0) que publica em mais de 28 redes. Roda no seu Docker com PostgreSQL e Redis; integra com o n8n. | passo 10.8 · Semana 4 · nov/2026 |
| [Aprovação no celular](#aprov) | Local | Nenhum post sai sem o seu ok: a peça chega pelo Telegram e você aprova no celular. Protege o canal de erro da IA. | passo 34.3 · Semana 5 · nov/2026 |
| [Telegram (avisos)](#tg) | Remoto · precisa de conta | Bot que avisa no celular: peça pronta para aprovar, serviço fora do ar. Grátis. | passo 18.1 · Semana 5 · nov/2026; passo 18.2 · Semana 5 · nov/2026; passo 18.3 · Semana 5 · nov/2026; passo 18.4 · Semana 5 · nov/2026; passo 18.5 · Semana 5 · nov/2026; passo 31.5 · Dez/2026 a jan/2027; passo 34.3 · Semana 5 · nov/2026 |
| [n8n](#n8n) | Local | Automação: novo aluno → e-mail, post agendado, aviso. | passo 10.1 · Semana 4 · nov/2026; passo 10.2 · Semana 4 · nov/2026; passo 10.5 · Semana 4 · nov/2026; passo 10.7 · Semana 4 · nov/2026; passo 12.1 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.4 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.6 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.7 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.9 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.10 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.12 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 27.7 · Semana 6 · nov/2026 a dez/2026; passo 31.5 · Dez/2026 a jan/2027; passo 46.5 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Algoritmo de horário](#horario) | Local · futuro | Calcula o desempenho por rede, dia e hora com os seus dados; 80% dos posts nas melhores faixas, 20% testando faixas novas. | passo 47.6 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Tags de conversão (Pixel, Google…)](#pixel) | Remoto · precisa de conta | Pixel + API de Conversões da Meta, tag do Google Ads, pixel do TikTok e as tags de Kwai, Pinterest, LinkedIn e nativos. Sem a tag, o canal não aprende quem compra e a venda não chega ao painel. | passo 36.5 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 |
| [Padrão de UTM](#utm) | Local | Todo link marcado com fonte, meio, campanha e criativo, para ligar cada venda ao anúncio ou post que a trouxe. | passo 37.12 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 |
| [Google e YouTube Ads](#gads) | Remoto · precisa de conta · futuro | Para vídeos longos que já convertem e buscas com intenção de compra. | passo 47.2 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [TikTok Ads](#ttads) | Remoto · precisa de conta · futuro | Depois que os cortes orgânicos mostrarem tração. | passo 47.2 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Regras de corte](#regras) | Local | Pausa criativo ou conjunto quando o CPA passa do de empate; sobe 15% do orçamento quando fica abaixo do CPA da margem. | passo 37.13 · Semanas 8 a 10 · dez/2026 a jan/2027 |
| [Lucro por Venda (calculadora)](#calc) | Remoto | Artefato com taxas das plataformas, imposto, CPA e ROAS de empate, simulador e o lucro real de cada campanha. | passo 37.13 · Semanas 8 a 10 · dez/2026 a jan/2027 |
| [Webhooks de venda](#hooks) | Remoto | Hotmart, Kiwify e Eduzz avisam cada venda e reembolso; o n8n grava no banco. | passo 38.1 · Semana 11 · jan/2027; passo 38.2 · Semana 11 · jan/2027; passo 39.3 · Semana 11 · jan/2027; passo 40.10 · Semanas 12 a 15 · jan a fev/2027 |
| [Banco de métricas (PostgreSQL)](#metrics) | Local | Tabelas de produtos, vendas, gastos, ferramentas e impostos. | passo 10.2 · Semana 4 · nov/2026; passo 10.7 · Semana 4 · nov/2026; passo 38.3 · Semana 11 · jan/2027 |
| [Painel de lucro (Grafana)](#painel) | Local | Lucro por produto, canal, campanha e país, atualizado sozinho. | passo 11.6 · Semana 4 · nov/2026; passo 12.11 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 38.4 · Semana 11 · jan/2027; passo 39.3 · Semana 11 · jan/2027 |
| [Programa de afiliados](#afprog) | Remoto · futuro | Comissão definida pela calculadora, aberta depois de 20 vendas próprias. | passo 47.5 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Prospecção de parceiros](#prosp) | Local | Busca e qualificação de parceiros com IA; mensagem revisada e enviada por você. | passo 37.16 · Semanas 8 a 10 · dez/2026 a jan/2027 |
| [Dublagem (YouTube + ElevenLabs)](#dub) | Remoto · futuro | Dublagem automática do YouTube para vídeos; ElevenLabs para cursos fora do YouTube. Espanhol primeiro. | passo 47.8 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Spotify Ad Studio](#spotads) | Remoto · precisa de conta · futuro | Anúncios em áudio e podcast, abertos a anunciantes no Brasil. Clique baixo: serve para marca, não para venda direta. | passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Kwai Ads](#kwaiads) | Remoto · precisa de conta · futuro | Plataforma de anúncios do Kwai no Brasil; teste depois de Meta e TikTok. | passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Pinterest Ads](#pinads) | Remoto · precisa de conta · futuro | Para templates e material visual; confira se a conta aceita o Brasil. | passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [LinkedIn Ads](#liads) | Remoto · precisa de conta · futuro | Caro; só para B2B (sistemas AM e consultoria). | passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Mídia nativa (Taboola, Outbrain)](#nativo) | Remoto · precisa de conta · futuro | Clique barato e conversão baixa; leva leitores a artigos do blog que vendem. | passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [Influenciadores e newsletters](#infl) | Remoto · futuro | Post pago ou por desempenho no nicho de TI e educação; peça números reais e use cupom. | passo 47.4 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) |
| [PostHog (funil e gravações)](#posthog) | Remoto · precisa de conta | Funis, gravação de sessões e testes nas páginas de venda: mostra onde o visitante desiste. Plano de nuvem com cota grátis; código aberto. | passo 33.2 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 33.3 · Com a primeira página de venda no ar (jan/2027) e por etapas |
| [GrowthBook (testes A/B)](#growthbook) | Local | Testes A/B e liberação gradual de funções com estatística correta. Código aberto. | passo 33.3 · Com a primeira página de venda no ar (jan/2027) e por etapas |
| [Formbricks (NPS e pesquisas)](#formbricks) | Remoto · precisa de conta | Principal de pesquisas (ADR 0008): NPS e pesquisa dentro do produto e por link, com histórico por cliente. | passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.10 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 45.6 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão) |
| [Adaptadores do núcleo](#adaptadores) | Remoto · futuro | Um conector por ferramenta (n8n para os simples, código para os complexos): traduz webhooks em eventos do núcleo e executa as ações que ele manda. | passo 22.9 · Nov/2026 a abr/2027, uma fase por vez, dentro das 7 h extras por semana; fases 0 e 1 primeiro, o garimpo logo depois; passo 22.10 · Nov/2026 a abr/2027, uma fase por vez, dentro das 7 h extras por semana; fases 0 e 1 primeiro, o garimpo logo depois; passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada |

<a id="ads"></a>

### Meta Ads (Instagram, Facebook)

*Remoto · precisa de conta · futuro*

Primeiro canal pago: anúncios da isca grátis e remarketing do mini-curso. Desde jan/2026 a fatura tem +12,15% de impostos sobre a mídia.

**Quando entra:** passo 47.1 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](22-pub.md#ig) | Público e canais | alcance pago |
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto por campanha |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="isca"></a>

### Isca grátis + sequência de e-mails

*Local*

Aula ou PDF grátis que captura o e-mail e abre uma sequência de 5 a 7 e-mails até o mini-curso.

**Quando entra:** passo 36.6 · Semanas 6 e 7 · dez/2026; passo 40.8 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MailerLite](21-mkt.md#mailer) | Marketing, automação e medição | sequência |
| ← recebe de | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | captura o e-mail |
| ← recebe de | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Influenciadores e newsletters](21-mkt.md#infl) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Livro Lógica e Máquina](17-prod.md#livro) | Produtos (o que você vende) | capítulo grátis |

<a id="mailer"></a>

### MailerLite

*Remoto · precisa de conta*

Newsletter do blog com grupos por tema e funil de lançamento. Você já escolheu o plano grátis.

**Quando entra:** passo 36.6 · Semanas 6 e 7 · dez/2026; passo 40.8 · Semanas 12 a 15 · jan a fev/2027; passo 46.8 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | leva à página de venda |
| → envia para | [Hotmart](20-venda.md#hotm) | Plataformas de venda e recebimento | lançamento |
| ← recebe de | [E-mail profissional (enviar e receber)](18-web.md#mail) | Vitrine web (sites e domínio) | remetente |
| ← recebe de | [Conector MailerLite](08-clc.md#cml) | Claude: recursos, conectores e plugins | campanhas |
| ← recebe de | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | novo aluno → e-mail |
| ← recebe de | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | formulário da newsletter |
| ← recebe de | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | sequência |
| ← recebe de | [CRM único + LGPD](23-oper.md#ocrm) | Operação do grupo (esteira, marca, qualidade) | etiquetas |

<a id="postiz"></a>

### Postiz (agendador)

*Local · futuro*

Agendador open source (AGPL-3.0) que publica em mais de 28 redes. Roda no seu Docker com PostgreSQL e Redis; integra com o n8n.

**Quando entra:** passo 10.8 · Semana 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](22-pub.md#yt) | Público e canais | publica |
| → envia para | [Instagram](22-pub.md#ig) | Público e canais | publica |
| → envia para | [TikTok](22-pub.md#tiktok) | Público e canais | publica |
| → envia para | [Facebook](22-pub.md#facebook) | Público e canais | publica |
| → envia para | [LinkedIn](22-pub.md#li) | Público e canais | publica |
| ← recebe de | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | manda o post aprovado |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | roda 24 h |

<a id="aprov"></a>

### Aprovação no celular

*Local*

Nenhum post sai sem o seu ok: a peça chega pelo Telegram e você aprova no celular. Protege o canal de erro da IA.

**Quando entra:** passo 34.3 · Semana 5 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | libera |
| ← recebe de | [Agente editor de conteúdo](23-oper.md#oedit) | Operação do grupo (esteira, marca, qualidade) | fila de aprovação |
| ← recebe de | [Telegram (avisos)](21-mkt.md#tg) | Marketing, automação e medição | aprovar ou recusar |
| ← recebe de | [Jarvis (porta única dos agentes)](05-ia.md#jarvis) | Agentes de IA e sandbox | ação pede o seu ok |

<a id="tg"></a>

### Telegram (avisos)

*Remoto · precisa de conta*

Bot que avisa no celular: peça pronta para aprovar, serviço fora do ar. Grátis.

**Quando entra:** passo 18.1 · Semana 5 · nov/2026; passo 18.2 · Semana 5 · nov/2026; passo 18.3 · Semana 5 · nov/2026; passo 18.4 · Semana 5 · nov/2026; passo 18.5 · Semana 5 · nov/2026; passo 31.5 · Dez/2026 a jan/2027; passo 34.3 · Semana 5 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aprovação no celular](21-mkt.md#aprov) | Marketing, automação e medição | aprovar ou recusar |
| → envia para | [Celular](01-hw.md#cel) | Hardware | notificação |
| ← recebe de | [Pipeline de conteúdo](23-oper.md#opipe) | Operação do grupo (esteira, marca, qualidade) | aviso de peça pronta |
| ← recebe de | [Uptime Kuma](10-obs.md#kuma) | Observabilidade | alerta |
| ← recebe de | [Rotinas agendadas](04-lin.md#rotinas) | Linux (Ubuntu no WSL2, Arch no 2º disco) | resumo da manhã |
| ← recebe de | [Grocy](06-dados.md#grocy) | Dados e treino de IA | avisa ração e remédios |
| ← recebe de | [Jarvis (porta única dos agentes)](05-ia.md#jarvis) | Agentes de IA e sandbox | conversa por |
| ← recebe de | [Política de autonomia](02-seg.md#politicaaut) | Segurança e cofre | ok no celular |
| ← recebe de | [Simulação noturna de ponta a ponta](23-oper.md#simulacao) | Operação do grupo (esteira, marca, qualidade) | relatório da manhã |

<a id="n8n"></a>

### n8n

*Local*

Automação: novo aluno → e-mail, post agendado, aviso.

**Quando entra:** passo 10.1 · Semana 4 · nov/2026; passo 10.2 · Semana 4 · nov/2026; passo 10.5 · Semana 4 · nov/2026; passo 10.7 · Semana 4 · nov/2026; passo 12.1 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.4 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.6 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.7 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.9 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.10 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 12.12 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 27.7 · Semana 6 · nov/2026 a dez/2026; passo 31.5 · Dez/2026 a jan/2027; passo 46.5 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [MailerLite](21-mkt.md#mailer) | Marketing, automação e medição | novo aluno → e-mail |
| → envia para | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | manda o post aprovado |
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | grava |
| → envia para | [Agente cobrador](23-oper.md#ocob) | Operação do grupo (esteira, marca, qualidade) | roda |
| → envia para | [Agente pós-venda](23-oper.md#opos) | Operação do grupo (esteira, marca, qualidade) | roda |
| → envia para | [Agente atendente (WhatsApp)](23-oper.md#oatend) | Operação do grupo (esteira, marca, qualidade) | roda |
| → envia para | [Gateway de modelos (LiteLLM)](05-ia.md#litellm) | Agentes de IA e sandbox | agentes do n8n usam |
| ← recebe de | [Ollama](05-ia.md#oll) | Agentes de IA e sandbox | IA local nas automações |
| ← recebe de | [Docker + Compose](09-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [Aprovação no celular](21-mkt.md#aprov) | Marketing, automação e medição | libera |
| ← recebe de | [Algoritmo de horário](21-mkt.md#horario) | Marketing, automação e medição | escolhe o horário |
| ← recebe de | [Webhooks de venda](21-mkt.md#hooks) | Marketing, automação e medição | dispara |
| ← recebe de | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | roda 24 h |
| ← recebe de | [Verificadores](23-oper.md#overif) | Operação do grupo (esteira, marca, qualidade) | confere |
| ← recebe de | [Uptime Kuma](10-obs.md#kuma) | Observabilidade | está no ar? |
| ← recebe de | [Cloudflare (DNS, Pages, e-mail)](12-nuvem.md#cf) | Nuvem, código e entrega | túnel dos webhooks |
| ← recebe de | [VM sempre ligada (Oracle grátis)](12-nuvem.md#vm247) | Nuvem, código e entrega | roda 24 h |
| ← recebe de | [Adaptadores do núcleo](21-mkt.md#adaptadores) | Marketing, automação e medição | fluxos simples |

<a id="horario"></a>

### Algoritmo de horário

*Local · futuro*

Calcula o desempenho por rede, dia e hora com os seus dados; 80% dos posts nas melhores faixas, 20% testando faixas novas.

**Quando entra:** passo 47.6 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | escolhe o horário |
| ← recebe de | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | desempenho por horário |

<a id="pixel"></a>

### Tags de conversão (Pixel, Google…)

*Remoto · precisa de conta*

Pixel + API de Conversões da Meta, tag do Google Ads, pixel do TikTok e as tags de Kwai, Pinterest, LinkedIn e nativos. Sem a tag, o canal não aprende quem compra e a venda não chega ao painel.

**Quando entra:** passo 36.5 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | eventos de compra |
| → envia para | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | otimiza para venda |
| → envia para | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Klaro! (consentimento LGPD)](18-web.md#klaro) | Vitrine web (sites e domínio) | libera as tags com aceite |

<a id="utm"></a>

### Padrão de UTM

*Local*

Todo link marcado com fonte, meio, campanha e criativo, para ligar cada venda ao anúncio ou post que a trouxe.

**Quando entra:** passo 37.12 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | marca os links |
| → envia para | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | marca os links |
| → envia para | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | marca os links |
| → envia para | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | marca os links |
| → envia para | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | marca os links |
| → envia para | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | marca os links |
| → envia para | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | marca os links |
| → envia para | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | marca os links |
| → envia para | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | marca os links |
| → envia para | [Influenciadores e newsletters](21-mkt.md#infl) | Marketing, automação e medição | marca os links |

<a id="gads"></a>

### Google e YouTube Ads

*Remoto · precisa de conta · futuro*

Para vídeos longos que já convertem e buscas com intenção de compra.

**Quando entra:** passo 47.2 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="ttads"></a>

### TikTok Ads

*Remoto · precisa de conta · futuro*

Depois que os cortes orgânicos mostrarem tração.

**Quando entra:** passo 47.2 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="regras"></a>

### Regras de corte

*Local*

Pausa criativo ou conjunto quando o CPA passa do de empate; sobe 15% do orçamento quando fica abaixo do CPA da margem.

**Quando entra:** passo 37.13 · Semanas 8 a 10 · dez/2026 a jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | pausa ou escala |
| → envia para | [Influenciadores e newsletters](21-mkt.md#infl) | Marketing, automação e medição | renova ou encerra parceria |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | CPA e ROAS de empate |
| ← recebe de | [Painel de lucro (Grafana)](21-mkt.md#painel) | Marketing, automação e medição | dispara alertas |

<a id="calc"></a>

### Lucro por Venda (calculadora)

*Remoto*

Artefato com taxas das plataformas, imposto, CPA e ROAS de empate, simulador e o lucro real de cada campanha.

**Quando entra:** passo 37.13 · Semanas 8 a 10 · dez/2026 a jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | CPA e ROAS de empate |
| → envia para | [Programa de afiliados](21-mkt.md#afprog) | Marketing, automação e medição | comissão máxima |
| → envia para | [Influenciadores e newsletters](21-mkt.md#infl) | Marketing, automação e medição | valor máximo do post |
| → envia para | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | custo máximo por clique |
| → envia para | [Kit edição especial](15-editora.md#bkit) | Editora AMS Silva (produção de livros) | preço e margem |
| → envia para | [Curso por seção](15-editora.md#bcurso) | Editora AMS Silva (produção de livros) | preço e margem |

<a id="hooks"></a>

### Webhooks de venda

*Remoto*

Hotmart, Kiwify e Eduzz avisam cada venda e reembolso; o n8n grava no banco.

**Quando entra:** passo 38.1 · Semana 11 · jan/2027; passo 38.2 · Semana 11 · jan/2027; passo 39.3 · Semana 11 · jan/2027; passo 40.10 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | dispara |
| ← recebe de | [Hotmart](20-venda.md#hotm) | Plataformas de venda e recebimento | venda e reembolso |
| ← recebe de | [Kiwify](20-venda.md#kiwi) | Plataformas de venda e recebimento | venda e reembolso |
| ← recebe de | [Eduzz](20-venda.md#eduzz) | Plataformas de venda e recebimento | venda e reembolso |
| ← recebe de | [Invoice Ninja (orçamentos)](19-emp.md#invoiceninja) | Pessoa física: impostos e finanças | avisa pagamentos |
| ← recebe de | [Stripe CLI (testar pagamentos)](12-nuvem.md#stripecli) | Nuvem, código e entrega | simula webhooks |

<a id="metrics"></a>

### Banco de métricas (PostgreSQL)

*Local*

Tabelas de produtos, vendas, gastos, ferramentas e impostos.

**Quando entra:** passo 10.2 · Semana 4 · nov/2026; passo 10.7 · Semana 4 · nov/2026; passo 38.3 · Semana 11 · jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Painel de lucro (Grafana)](21-mkt.md#painel) | Marketing, automação e medição | consultas |
| → envia para | [Algoritmo de horário](21-mkt.md#horario) | Marketing, automação e medição | desempenho por horário |
| → envia para | [Carnê-leão (Receita Federal)](19-emp.md#nfse) | Pessoa física: impostos e finanças | base do carnê-leão |
| → envia para | [Analista semanal](23-oper.md#oanal) | Operação do grupo (esteira, marca, qualidade) | dados da semana |
| → envia para | [dbt Core](06-dados.md#dbt) | Dados e treino de IA | tabelas brutas |
| ← recebe de | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | grava |
| ← recebe de | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | gasto por campanha |
| ← recebe de | [Google e YouTube Ads](21-mkt.md#gads) | Marketing, automação e medição | gasto |
| ← recebe de | [TikTok Ads](21-mkt.md#ttads) | Marketing, automação e medição | gasto |
| ← recebe de | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | gasto |
| ← recebe de | [Kwai Ads](21-mkt.md#kwaiads) | Marketing, automação e medição | gasto |
| ← recebe de | [Pinterest Ads](21-mkt.md#pinads) | Marketing, automação e medição | gasto |
| ← recebe de | [LinkedIn Ads](21-mkt.md#liads) | Marketing, automação e medição | gasto |
| ← recebe de | [Mídia nativa (Taboola, Outbrain)](21-mkt.md#nativo) | Marketing, automação e medição | gasto |
| ← recebe de | [Influenciadores e newsletters](21-mkt.md#infl) | Marketing, automação e medição | custo do post |
| ← recebe de | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | roda 24 h |
| ← recebe de | [Servidores MCP](05-ia.md#mcp) | Agentes de IA e sandbox | leitura (usuário do Grafana) |
| ← recebe de | [Docker + Compose](09-cnt.md#docker) | Containers, Kubernetes e infra como código | container |
| ← recebe de | [Metabase (painéis)](06-dados.md#metabase) | Dados e treino de IA | lê |

<a id="painel"></a>

### Painel de lucro (Grafana)

*Local*

Lucro por produto, canal, campanha e país, atualizado sozinho.

**Quando entra:** passo 11.6 · Semana 4 · nov/2026; passo 12.11 · Nov/2026 em diante, uma por vez, na ordem de desbloqueio; passo 38.4 · Semana 11 · jan/2027; passo 39.3 · Semana 11 · jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | dispara alertas |
| → envia para | [Grafana](10-obs.md#graf) | Observabilidade | roda no Grafana |
| ← recebe de | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | consultas |
| ← recebe de | [dbt Core](06-dados.md#dbt) | Dados e treino de IA | modelos limpos |
| ← recebe de | [Radar de revenda](16-neg.md#radar) | Negócios do grupo (Barbacena) | lucro por hora |
| ← recebe de | [ActivityWatch](03-win.md#aw) | Windows 11, apps e máquinas virtuais | horas por renda |
| ← recebe de | [Financeiro local](19-emp.md#financas) | Pessoa física: impostos e finanças | sobra do mês |
| ← recebe de | [Teste de restauração](02-seg.md#restauracao) | Segurança e cofre | resultado do teste |
| ← recebe de | [Lucro por ferramenta](23-oper.md#roi) | Operação do grupo (esteira, marca, qualidade) | resultado por ferramenta |
| ← recebe de | [PostHog (funil e gravações)](21-mkt.md#posthog) | Marketing, automação e medição | conversão por página |

<a id="afprog"></a>

### Programa de afiliados

*Remoto · futuro*

Comissão definida pela calculadora, aberta depois de 20 vendas próprias.

**Quando entra:** passo 47.5 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Hotmart](20-venda.md#hotm) | Plataformas de venda e recebimento | afiliados cadastrados |
| ← recebe de | [Prospecção de parceiros](21-mkt.md#prosp) | Marketing, automação e medição | novos afiliados |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | comissão máxima |

<a id="prosp"></a>

### Prospecção de parceiros

*Local*

Busca e qualificação de parceiros com IA; mensagem revisada e enviada por você.

**Quando entra:** passo 37.16 · Semanas 8 a 10 · dez/2026 a jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Programa de afiliados](21-mkt.md#afprog) | Marketing, automação e medição | novos afiliados |
| ← recebe de | [Conector vidIQ](08-clc.md#cvid) | Claude: recursos, conectores e plugins | canais semelhantes |
| ← recebe de | [Plugins: small- business + marketing](08-clc.md#pbiz) | Claude: recursos, conectores e plugins | rascunho de propostas |

<a id="dub"></a>

### Dublagem (YouTube + ElevenLabs)

*Remoto · futuro*

Dublagem automática do YouTube para vídeos; ElevenLabs para cursos fora do YouTube. Espanhol primeiro.

**Quando entra:** passo 47.8 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](22-pub.md#yt) | Público e canais | faixas de áudio |
| ← recebe de | [Voz clonada (ElevenLabs)](13-cont.md#voz) | Produção de conteúdo | sua voz em outros idiomas |
| ← recebe de | [Traduções (espanhol, inglês)](15-editora.md#trad) | Editora AMS Silva (produção de livros) | voz em outros idiomas |

<a id="spotads"></a>

### Spotify Ad Studio

*Remoto · precisa de conta · futuro*

Anúncios em áudio e podcast, abertos a anunciantes no Brasil. Clique baixo: serve para marca, não para venda direta.

**Quando entra:** passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| → envia para | [YouTube](22-pub.md#yt) | Público e canais | lembrança da marca |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="kwaiads"></a>

### Kwai Ads

*Remoto · precisa de conta · futuro*

Plataforma de anúncios do Kwai no Brasil; teste depois de Meta e TikTok.

**Quando entra:** passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="pinads"></a>

### Pinterest Ads

*Remoto · precisa de conta · futuro*

Para templates e material visual; confira se a conta aceita o Brasil.

**Quando entra:** passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="liads"></a>

### LinkedIn Ads

*Remoto · precisa de conta · futuro*

Caro; só para B2B (sistemas AM e consultoria).

**Quando entra:** passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="nativo"></a>

### Mídia nativa (Taboola, Outbrain)

*Remoto · precisa de conta · futuro*

Clique barato e conversão baixa; leva leitores a artigos do blog que vendem.

**Quando entra:** passo 47.3 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | gasto |
| → envia para | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | leva aos artigos |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | pausa ou escala |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Tags de conversão (Pixel, Google…)](21-mkt.md#pixel) | Marketing, automação e medição | otimiza para venda |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | custo máximo por clique |

<a id="infl"></a>

### Influenciadores e newsletters

*Remoto · futuro*

Post pago ou por desempenho no nicho de TI e educação; peça números reais e use cupom.

**Quando entra:** passo 47.4 · A partir de fev/2027 (começa quando: o mini-curso vendeu sem anúncio (por exemplo, 10 vendas) e o painel de lucro está no ar) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Banco de métricas (PostgreSQL)](21-mkt.md#metrics) | Marketing, automação e medição | custo do post |
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | link com cupom |
| → envia para | [Isca grátis + sequência de e-mails](21-mkt.md#isca) | Marketing, automação e medição | leva à isca grátis |
| ← recebe de | [Lucro por Venda (calculadora)](21-mkt.md#calc) | Marketing, automação e medição | valor máximo do post |
| ← recebe de | [Padrão de UTM](21-mkt.md#utm) | Marketing, automação e medição | marca os links |
| ← recebe de | [Regras de corte](21-mkt.md#regras) | Marketing, automação e medição | renova ou encerra parceria |

<a id="posthog"></a>

### PostHog (funil e gravações)

*Remoto · precisa de conta*

Funis, gravação de sessões e testes nas páginas de venda: mostra onde o visitante desiste. Plano de nuvem com cota grátis; código aberto.

**Quando entra:** passo 33.2 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 33.3 · Com a primeira página de venda no ar (jan/2027) e por etapas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Painel de lucro (Grafana)](21-mkt.md#painel) | Marketing, automação e medição | conversão por página |
| ← recebe de | [GrowthBook (testes A/B)](21-mkt.md#growthbook) | Marketing, automação e medição | mede os testes |

<a id="growthbook"></a>

### GrowthBook (testes A/B)

*Local*

Testes A/B e liberação gradual de funções com estatística correta. Código aberto.

**Quando entra:** passo 33.3 · Com a primeira página de venda no ar (jan/2027) e por etapas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [PostHog (funil e gravações)](21-mkt.md#posthog) | Marketing, automação e medição | mede os testes |

<a id="formbricks"></a>

### Formbricks (NPS e pesquisas)

*Remoto · precisa de conta*

Principal de pesquisas (ADR 0008): NPS e pesquisa dentro do produto e por link, com histórico por cliente.

**Quando entra:** passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada; passo 33.10 · Com a primeira página de venda no ar (jan/2027) e por etapas; passo 45.6 · Recesso escolar de jan/2027 (14 dias seguidos, de dia; o restaurante segue à noite) (começa quando: o recesso começou e uma das 3 rendas de agora já passou no portão) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [NPS e avaliações](23-oper.md#oaval) | Operação do grupo (esteira, marca, qualidade) | alimenta o NPS |

<a id="adaptadores"></a>

### Adaptadores do núcleo

*Remoto · futuro*

Um conector por ferramenta (n8n para os simples, código para os complexos): traduz webhooks em eventos do núcleo e executa as ações que ele manda.

**Quando entra:** passo 22.9 · Nov/2026 a abr/2027, uma fase por vez, dentro das 7 h extras por semana; fases 0 e 1 primeiro, o garimpo logo depois; passo 22.10 · Nov/2026 a abr/2027, uma fase por vez, dentro das 7 h extras por semana; fases 0 e 1 primeiro, o garimpo logo depois; passo 23.8 · Nov/2026 a jan/2027 (no CPF); o CNPJ quando a renda de software passar do ponto de virada ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Núcleo AMtech (banco central)](23-oper.md#nucleo) | Operação do grupo (esteira, marca, qualidade) | eventos |
| → envia para | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | fluxos simples |
| ← recebe de | [Simulação noturna de ponta a ponta](23-oper.md#simulacao) | Operação do grupo (esteira, marca, qualidade) | testa a cadeia |

---

[↑ Camada 22 · Público e canais](22-pub.md) · [↓ Camada 20 · Plataformas de venda e recebimento](20-venda.md)
