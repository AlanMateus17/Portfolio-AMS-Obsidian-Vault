<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 22 · Público e canais

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Link na bio, vídeo, post, busca e indicação levam a pessoa até o site ou o WhatsApp.

**12 blocos** · 9 precisam de conta · 1 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_pub["Público e canais"]
    n_mbs["Meta Business Suite"]
    n_ig["Instagram"]
    n_yt["YouTube"]
    n_li["LinkedIn"]
    n_wa["WhatsApp Business"]
    n_ogbp["Google Perfil da Empresa"]
    n_comu["Comunidade (Discord ou grupo)"]
    n_seo["Busca Google (SEO)"]
    n_alunos["Alunos e ex-alunos"]
    n_recr["Recrutadores"]
    n_tiktok["TikTok"]
    n_facebook["Facebook"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_oatend["Agente atendente (WhatsApp)"]
    n_obuild["Canal build in public"]
    n_omarca["Marca pessoal Alan Mateus"]
    n_opos["Agente pós-venda"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_ads["Meta Ads (Instagram, Facebook)"]
    n_dub["Dublagem (YouTube + ElevenLabs)"]
    n_postiz["Postiz (agendador)"]
    n_spotads["Spotify Ad Studio"]
  end
  subgraph L_venda["Plataformas de venda e recebimento"]
    n_afil["Afiliados (Amazon, Hotmart…)"]
    n_hotm["Hotmart"]
    n_ytm["YouTube (membros)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_catal["Catálogo do HTML"]
    n_gsc["Google Search Console"]
    n_inst["Instituto AMS"]
    n_site["Site pessoal + blog (Jekyll)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_aulas["Aulas particulares"]
    n_curso["Mini-curso Lógica de Programação"]
    n_sites["Sites para pequenas empresas"]
  end
  subgraph L_neg["Negócios do grupo (Barbacena)"]
    n_nloja["Loja AMtech (assistência)"]
    n_npad["Padaria + café da manhã + almoço"]
    n_nsushi["Sushi (delivery)"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_edit["DaVinci Resolve ou Kdenlive"]
    n_img["Canva · Krita · Inkscape"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gh["GitHub"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_cvid["Conector vidIQ"]
    n_pbiz["Plugins: small- business + marketing"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_gem["Gemini (pago)"]
    n_grok["Grok"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_sharex["ShareX"]
  end
  subgraph L_hw["Hardware"]
    n_cel["Celular"]
  end
  n_mbs -->|"agenda posts"| n_ig
  n_mbs -->|"agenda posts"| n_facebook
  n_ig -->|"link na bio"| n_inst
  n_ig -->|"contato direto"| n_wa
  n_cel -->|"posta reels"| n_ig
  n_sharex -->|"GIFs e prints"| n_ig
  n_ads -->|"alcance pago"| n_ig
  n_pbiz -->|"conteúdo"| n_ig
  n_img -->|"posts"| n_ig
  n_alunos -->|"seguem"| n_ig
  n_postiz -->|"publica"| n_ig
  n_omarca -->|"perfil"| n_ig
  n_yt -->|"membros"| n_ytm
  n_yt -->|"link na descrição"| n_inst
  n_yt -->|"links na descrição"| n_afil
  n_gem -->|"resume vídeos"| n_yt
  n_cvid -->|"tendências"| n_yt
  n_edit -->|"vídeo final"| n_yt
  n_postiz -->|"publica"| n_yt
  n_dub -->|"faixas de áudio"| n_yt
  n_spotads -->|"lembrança da marca"| n_yt
  n_obuild -->|"vídeo semanal"| n_yt
  n_omarca -->|"canal"| n_yt
  n_li -->|"perfil e posts"| n_recr
  n_li -->|"link"| n_site
  n_grok -->|"tendências do setor"| n_li
  n_postiz -->|"publica"| n_li
  n_omarca -->|"carreira e B2B"| n_li
  n_wa -->|"agenda"| n_aulas
  n_wa -->|"pedido de orçamento"| n_sites
  n_cel -->|"atendimento"| n_wa
  n_oatend -->|"responde"| n_wa
  n_ogbp -->|"presença local"| n_nloja
  n_ogbp -->|"presença local"| n_nsushi
  n_ogbp -->|"presença local"| n_npad
  n_opos -->|"pede avaliação"| n_ogbp
  n_comu -->|"suporte aos alunos"| n_curso
  n_hotm -->|"convite na compra"| n_comu
  n_seo -->|"visitas"| n_site
  n_seo -->|"visitas"| n_inst
  n_gsc -->|"indexação"| n_seo
  n_alunos -->|"usam o site"| n_catal
  n_gh -->|"portfólio"| n_recr
  n_site -->|"currículo"| n_recr
  n_tiktok -->|"link na bio"| n_inst
  n_postiz -->|"publica"| n_tiktok
  n_facebook -->|"link"| n_inst
  n_postiz -->|"publica"| n_facebook
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_mbs,n_ig,n_yt,n_li,n_wa,n_ogbp,n_comu,n_seo,n_alunos,n_recr,n_tiktok,n_facebook desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Meta Business Suite](#mbs) | Remoto · precisa de conta | Agenda posts e reels do Instagram com antecedência e mostra as métricas. Grátis. | passo 36.5 · Semanas 6 e 7 · dez/2026 |
| [Instagram](#ig) | Remoto · precisa de conta | Canal principal de venda: posts, reels e link na bio para o Instituto AMS. | passo 36.1 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 |
| [YouTube](#yt) | Remoto · precisa de conta | Aulas e vídeos de vendas. Gera público para os cursos e para o livro. | passo 36.1 · Semanas 6 e 7 · dez/2026; passo 46.14 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [LinkedIn](#li) | Remoto · precisa de conta | Vitrine para a vaga de dev: projetos, posts técnicos e certificações. | passo 36.1 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 |
| [WhatsApp Business](#wa) | Remoto · precisa de conta | Atendimento de alunos particulares e clientes de sites. | passo 36.2 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 |
| [Google Perfil da Empresa](#ogbp) | Remoto · precisa de conta · futuro | O canal local mais importante: loja, assistência e restaurantes. Post semanal, fotos, horários e resposta a avaliações em 24 h. | passo 46.9 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 56.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) |
| [Comunidade (Discord ou grupo)](#comu) | Remoto · precisa de conta | Alunos do curso juntos: tira-dúvidas, retenção e indicação. | passo 37.10 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.15 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) |
| [Busca Google (SEO)](#seo) | Remoto | Pessoas chegando ao blog e aos sites pelos artigos. | passo 36.12 · Semanas 6 e 7 · dez/2026 |
| [Alunos e ex-alunos](#alunos) | Físico | Seu público inicial: alunos do EMTI, ex-alunos e contatos. | passo 36.10 · Semanas 6 e 7 · dez/2026 |
| [Recrutadores](#recr) | Físico | Quem decide a vaga de dev. Olham GitHub, LinkedIn e o site. | passo 41.8 · Trimestre 2 do eixo (fev a abr/2027): o modelo nasce no esqueleto do AM Rendara (módulo o-dotnet do Professor) e ganha testes e qualidade até o MVP |
| [TikTok](#tiktok) | Remoto · precisa de conta | Cortes verticais diários. Conteúdo realista de IA precisa do rótulo de IA. | passo 36.1 · Semanas 6 e 7 · dez/2026 |
| [Facebook](#facebook) | Remoto · precisa de conta | Reels e posts da página da marca; mesma conta de anúncios do Instagram. | passo 36.1 · Semanas 6 e 7 · dez/2026 |

<a id="mbs"></a>

### Meta Business Suite

*Remoto · precisa de conta*

Agenda posts e reels do Instagram com antecedência e mostra as métricas. Grátis.

**Quando entra:** passo 36.5 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](22-pub.md#ig) | Público e canais | agenda posts |
| → envia para | [Facebook](22-pub.md#facebook) | Público e canais | agenda posts |

<a id="ig"></a>

### Instagram

*Remoto · precisa de conta*

Canal principal de venda: posts, reels e link na bio para o Instituto AMS.

**Quando entra:** passo 36.1 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | link na bio |
| → envia para | [WhatsApp Business](22-pub.md#wa) | Público e canais | contato direto |
| ← recebe de | [Celular](01-hw.md#cel) | Hardware | posta reels |
| ← recebe de | [ShareX](03-win.md#sharex) | Windows 11, apps e máquinas virtuais | GIFs e prints |
| ← recebe de | [Meta Business Suite](22-pub.md#mbs) | Público e canais | agenda posts |
| ← recebe de | [Meta Ads (Instagram, Facebook)](21-mkt.md#ads) | Marketing, automação e medição | alcance pago |
| ← recebe de | [Plugins: small- business + marketing](08-clc.md#pbiz) | Claude: recursos, conectores e plugins | conteúdo |
| ← recebe de | [Canva · Krita · Inkscape](13-cont.md#img) | Produção de conteúdo | posts |
| ← recebe de | [Alunos e ex-alunos](22-pub.md#alunos) | Público e canais | seguem |
| ← recebe de | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | publica |
| ← recebe de | [Marca pessoal Alan Mateus](23-oper.md#omarca) | Operação do grupo (esteira, marca, qualidade) | perfil |

<a id="yt"></a>

### YouTube

*Remoto · precisa de conta*

Aulas e vídeos de vendas. Gera público para os cursos e para o livro.

**Quando entra:** passo 36.1 · Semanas 6 e 7 · dez/2026; passo 46.14 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube (membros)](20-venda.md#ytm) | Plataformas de venda e recebimento | membros |
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | link na descrição |
| → envia para | [Afiliados (Amazon, Hotmart…)](20-venda.md#afil) | Plataformas de venda e recebimento | links na descrição |
| ← recebe de | [Gemini (pago)](07-chat.md#gem) | Assistentes de IA (chat, pesquisa e estudo) | resume vídeos |
| ← recebe de | [Conector vidIQ](08-clc.md#cvid) | Claude: recursos, conectores e plugins | tendências |
| ← recebe de | [DaVinci Resolve ou Kdenlive](13-cont.md#edit) | Produção de conteúdo | vídeo final |
| ← recebe de | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | publica |
| ← recebe de | [Dublagem (YouTube + ElevenLabs)](21-mkt.md#dub) | Marketing, automação e medição | faixas de áudio |
| ← recebe de | [Spotify Ad Studio](21-mkt.md#spotads) | Marketing, automação e medição | lembrança da marca |
| ← recebe de | [Canal build in public](23-oper.md#obuild) | Operação do grupo (esteira, marca, qualidade) | vídeo semanal |
| ← recebe de | [Marca pessoal Alan Mateus](23-oper.md#omarca) | Operação do grupo (esteira, marca, qualidade) | canal |

<a id="li"></a>

### LinkedIn

*Remoto · precisa de conta*

Vitrine para a vaga de dev: projetos, posts técnicos e certificações.

**Quando entra:** passo 36.1 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Recrutadores](22-pub.md#recr) | Público e canais | perfil e posts |
| → envia para | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | link |
| ← recebe de | [Grok](07-chat.md#grok) | Assistentes de IA (chat, pesquisa e estudo) | tendências do setor |
| ← recebe de | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | publica |
| ← recebe de | [Marca pessoal Alan Mateus](23-oper.md#omarca) | Operação do grupo (esteira, marca, qualidade) | carreira e B2B |

<a id="wa"></a>

### WhatsApp Business

*Remoto · precisa de conta*

Atendimento de alunos particulares e clientes de sites.

**Quando entra:** passo 36.2 · Semanas 6 e 7 · dez/2026; passo 40.7 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aulas particulares](17-prod.md#aulas) | Produtos (o que você vende) | agenda |
| → envia para | [Sites para pequenas empresas](17-prod.md#sites) | Produtos (o que você vende) | pedido de orçamento |
| ← recebe de | [Celular](01-hw.md#cel) | Hardware | atendimento |
| ← recebe de | [Instagram](22-pub.md#ig) | Público e canais | contato direto |
| ← recebe de | [Agente atendente (WhatsApp)](23-oper.md#oatend) | Operação do grupo (esteira, marca, qualidade) | responde |

<a id="ogbp"></a>

### Google Perfil da Empresa

*Remoto · precisa de conta · futuro*

O canal local mais importante: loja, assistência e restaurantes. Post semanal, fotos, horários e resposta a avaliações em 24 h.

**Quando entra:** passo 46.9 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu); passo 56.3 · Fase A: 12 a 18 meses; B: mais 12 a 18; C: a partir do 3º ou 4º ano (começa quando: os 5 portões do planejador: negócio anterior se pagando há 3 meses, capital em caixa, alguém de confiança tocando, sistema AM rodando e a sua reserva intacta) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Loja AMtech (assistência)](16-neg.md#nloja) | Negócios do grupo (Barbacena) | presença local |
| → envia para | [Sushi (delivery)](16-neg.md#nsushi) | Negócios do grupo (Barbacena) | presença local |
| → envia para | [Padaria + café da manhã + almoço](16-neg.md#npad) | Negócios do grupo (Barbacena) | presença local |
| ← recebe de | [Agente pós-venda](23-oper.md#opos) | Operação do grupo (esteira, marca, qualidade) | pede avaliação |

<a id="comu"></a>

### Comunidade (Discord ou grupo)

*Remoto · precisa de conta*

Alunos do curso juntos: tira-dúvidas, retenção e indicação.

**Quando entra:** passo 37.10 · Semanas 8 a 10 · dez/2026 a jan/2027; passo 46.15 · Fev a dez/2027, uma oferta por vez (começa quando: a primeira venda do mini-curso aconteceu) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | suporte aos alunos |
| ← recebe de | [Hotmart](20-venda.md#hotm) | Plataformas de venda e recebimento | convite na compra |

<a id="seo"></a>

### Busca Google (SEO)

*Remoto*

Pessoas chegando ao blog e aos sites pelos artigos.

**Quando entra:** passo 36.12 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | visitas |
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | visitas |
| ← recebe de | [Google Search Console](18-web.md#gsc) | Vitrine web (sites e domínio) | indexação |

<a id="alunos"></a>

### Alunos e ex-alunos

*Físico*

Seu público inicial: alunos do EMTI, ex-alunos e contatos.

**Quando entra:** passo 36.10 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Catálogo do HTML](18-web.md#catal) | Vitrine web (sites e domínio) | usam o site |
| → envia para | [Instagram](22-pub.md#ig) | Público e canais | seguem |

<a id="recr"></a>

### Recrutadores

*Físico*

Quem decide a vaga de dev. Olham GitHub, LinkedIn e o site.

**Quando entra:** passo 41.8 · Trimestre 2 do eixo (fev a abr/2027): o modelo nasce no esqueleto do AM Rendara (módulo o-dotnet do Professor) e ganha testes e qualidade até o MVP ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [LinkedIn](22-pub.md#li) | Público e canais | perfil e posts |
| ← recebe de | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | portfólio |
| ← recebe de | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | currículo |

<a id="tiktok"></a>

### TikTok

*Remoto · precisa de conta*

Cortes verticais diários. Conteúdo realista de IA precisa do rótulo de IA.

**Quando entra:** passo 36.1 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | link na bio |
| ← recebe de | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | publica |

<a id="facebook"></a>

### Facebook

*Remoto · precisa de conta*

Reels e posts da página da marca; mesma conta de anúncios do Instagram.

**Quando entra:** passo 36.1 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | link |
| ← recebe de | [Postiz (agendador)](21-mkt.md#postiz) | Marketing, automação e medição | publica |
| ← recebe de | [Meta Business Suite](22-pub.md#mbs) | Público e canais | agenda posts |

---

[↑ Camada 23 · Operação do grupo (esteira, marca, qualidade)](23-oper.md) · [↓ Camada 21 · Marketing, automação e medição](21-mkt.md)
