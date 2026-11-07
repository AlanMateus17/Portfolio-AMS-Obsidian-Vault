<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 13 · Produção de conteúdo

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** Gravação e edição rodam no notebook; os arquivos finais sobem para as plataformas.

**8 blocos** · 2 precisam de conta · 0 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_cont["Produção de conteúdo"]
    n_obss["OBS Studio"]
    n_edit["DaVinci Resolve ou Kdenlive"]
    n_aud["Audacity"]
    n_img["Canva · Krita · Inkscape"]
    n_whis["Whisper (local)"]
    n_voz["Voz clonada (ElevenLabs)"]
    n_fabrica["Fábrica de aulas"]
    n_penpot["Penpot (design)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_oedit["Agente editor de conteúdo"]
    n_opipe["Pipeline de conteúdo"]
  end
  subgraph L_pub["Público e canais"]
    n_ig["Instagram"]
    n_yt["YouTube"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_dub["Dublagem (YouTube + ElevenLabs)"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_inst["Instituto AMS"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_aulas["Aulas particulares"]
    n_curso["Mini-curso Lógica de Programação"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_bcurso["Curso por seção"]
    n_licenca["Filtro de licença e fichas"]
    n_refs["Quadro de referências"]
  end
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_gpuh["GPU por hora (RunPod e afins)"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_front["Next.js + Aura Design System"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_ccan["Conectores Canva + Figma"]
    n_phst["Plugins: Hostinger · Adobe · Cloudinary"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_gpt["ChatGPT"]
  end
  subgraph L_dados["Dados e treino de IA"]
    n_dset["Seus datasets (só conteúdo seu)"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_jvoz["Voz local: Whisper, Piper, openWakeWord"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_hw["Hardware"]
    n_mic["Microfone + câmera"]
    n_ssdext["SSD externo (USB-C 10 Gbps)"]
    n_ws["Workstation com GPU"]
  end
  n_obss -->|"gravação"| n_edit
  n_obss -->|"áudio"| n_whis
  n_mic -->|"áudio e vídeo USB"| n_obss
  n_edit -->|"vídeo final"| n_yt
  n_edit -->|"aulas editadas"| n_curso
  n_edit -->|"aulas"| n_bcurso
  n_phst -->|"imagem e vídeo"| n_edit
  n_aud -->|"áudio limpo"| n_edit
  n_voz -->|"narração"| n_edit
  n_ssdext -->|"projetos de vídeo"| n_edit
  n_img -->|"posts"| n_ig
  n_img -->|"capas"| n_inst
  n_img -->|"rascunhos de ideia"| n_refs
  n_img -->|"ficha com prompt e ferramenta"| n_licenca
  n_gpt -->|"gera imagens"| n_img
  n_ccan -->|"posts e capas"| n_img
  n_whis -->|"transcrição"| n_obsd
  n_whis -->|"transcrição"| n_oedit
  n_whis -->|"transcreve"| n_opipe
  n_whis -->|"transcrições das suas aulas"| n_dset
  n_whis -->|"transcreve"| n_jvoz
  n_voz -->|"sua voz em outros idiomas"| n_dub
  n_voz -->|"narração"| n_bcurso
  n_ws -->|"voz e vídeo locais"| n_voz
  n_gpuh -->|"modelos abertos"| n_voz
  n_oedit -->|"narração"| n_voz
  n_fabrica -->|"material das aulas"| n_aulas
  n_penpot -->|"telas dos sistemas"| n_front
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_obss,n_edit,n_aud,n_img,n_whis,n_voz,n_fabrica,n_penpot desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [OBS Studio](#obss) | Local | Grava tela, câmera e áudio das aulas e vídeos. | passo 3.2 · Semana 1 · out/2026; passo 35.1 · Semana 5 · dez/2026; passo 40.2 · Semanas 12 a 15 · jan a fev/2027 |
| [DaVinci Resolve ou Kdenlive](#edit) | Local | Edição de vídeo. Os dois têm versão grátis. | passo 3.7 · Semana 1 · out/2026; passo 35.3 · Semana 5 · dez/2026; passo 40.2 · Semanas 12 a 15 · jan a fev/2027 |
| [Audacity](#aud) | Local | Limpa ruído e ajusta o áudio. | passo 3.2 · Semana 1 · out/2026; passo 35.2 · Semana 5 · dez/2026 |
| [Canva · Krita · Inkscape](#img) | Local · precisa de conta | Capas, posts e thumbnails. Canva precisa de conta; Krita e Inkscape são open source. | passo 3.2 · Semana 1 · out/2026; passo 28.8 · Semana 6 · nov/2026 a dez/2026; passo 35.4 · Semana 5 · dez/2026 |
| [Whisper (local)](#whis) | Local | Transcreve as aulas para legenda, artigo e capítulo. | passo 4.4 · Semana 2 · nov/2026; passo 34.6 · Semana 5 · nov/2026 |
| [Voz clonada (ElevenLabs)](#voz) | Remoto · precisa de conta | Clonagem profissional da sua própria voz (plano Creator em diante, uso comercial nos planos pagos). Treino com 30 minutos ou mais de áudio limpo. Avise o público que a voz é gerada por IA. | passo 35.5 · Semana 5 · dez/2026 |
| [Fábrica de aulas](#fabrica) | Local | Gera planejamentos e documentos da escola no modelo exigido, a partir da ementa e das suas regras. Sem dados de aluno. | passo 14.1 · Semanas 5 e 6 · nov/2026; passo 14.2 · Semanas 5 e 6 · nov/2026; passo 14.3 · Semanas 5 e 6 · nov/2026; passo 14.4 · Semanas 5 e 6 · nov/2026; passo 14.5 · Semanas 5 e 6 · nov/2026; passo 14.6 · Semanas 5 e 6 · nov/2026; passo 14.7 · Semanas 5 e 6 · nov/2026; passo 14.8 · Semanas 5 e 6 · nov/2026; passo 14.9 · Semanas 5 e 6 · nov/2026 |
| [Penpot (design)](#penpot) | Local | Design de telas e protótipos, aberto, alternativa ao Figma pago. | passo 33.8 · Com a primeira página de venda no ar (jan/2027) e por etapas |

<a id="obss"></a>

### OBS Studio

*Local*

Grava tela, câmera e áudio das aulas e vídeos.

**Quando entra:** passo 3.2 · Semana 1 · out/2026; passo 35.1 · Semana 5 · dez/2026; passo 40.2 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](13-cont.md#edit) | Produção de conteúdo | gravação |
| → envia para | [Whisper (local)](13-cont.md#whis) | Produção de conteúdo | áudio |
| ← recebe de | [Microfone + câmera](01-hw.md#mic) | Hardware | áudio e vídeo USB |

<a id="edit"></a>

### DaVinci Resolve ou Kdenlive

*Local*

Edição de vídeo. Os dois têm versão grátis.

**Quando entra:** passo 3.7 · Semana 1 · out/2026; passo 35.3 · Semana 5 · dez/2026; passo 40.2 · Semanas 12 a 15 · jan a fev/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [YouTube](22-pub.md#yt) | Público e canais | vídeo final |
| → envia para | [Mini-curso Lógica de Programação](17-prod.md#curso) | Produtos (o que você vende) | aulas editadas |
| → envia para | [Curso por seção](15-editora.md#bcurso) | Editora AMS Silva (produção de livros) | aulas |
| ← recebe de | [Plugins: Hostinger · Adobe · Cloudinary](08-clc.md#phst) | Claude: recursos, conectores e plugins | imagem e vídeo |
| ← recebe de | [OBS Studio](13-cont.md#obss) | Produção de conteúdo | gravação |
| ← recebe de | [Audacity](13-cont.md#aud) | Produção de conteúdo | áudio limpo |
| ← recebe de | [Voz clonada (ElevenLabs)](13-cont.md#voz) | Produção de conteúdo | narração |
| ← recebe de | [SSD externo (USB-C 10 Gbps)](01-hw.md#ssdext) | Hardware | projetos de vídeo |

<a id="aud"></a>

### Audacity

*Local*

Limpa ruído e ajusta o áudio.

**Quando entra:** passo 3.2 · Semana 1 · out/2026; passo 35.2 · Semana 5 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](13-cont.md#edit) | Produção de conteúdo | áudio limpo |

<a id="img"></a>

### Canva · Krita · Inkscape

*Local · precisa de conta*

Capas, posts e thumbnails. Canva precisa de conta; Krita e Inkscape são open source.

**Quando entra:** passo 3.2 · Semana 1 · out/2026; passo 28.8 · Semana 6 · nov/2026 a dez/2026; passo 35.4 · Semana 5 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Instagram](22-pub.md#ig) | Público e canais | posts |
| → envia para | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | capas |
| → envia para | [Quadro de referências](15-editora.md#refs) | Editora AMS Silva (produção de livros) | rascunhos de ideia |
| → envia para | [Filtro de licença e fichas](15-editora.md#licenca) | Editora AMS Silva (produção de livros) | ficha com prompt e ferramenta |
| ← recebe de | [ChatGPT](07-chat.md#gpt) | Assistentes de IA (chat, pesquisa e estudo) | gera imagens |
| ← recebe de | [Conectores Canva + Figma](08-clc.md#ccan) | Claude: recursos, conectores e plugins | posts e capas |

<a id="whis"></a>

### Whisper (local)

*Local*

Transcreve as aulas para legenda, artigo e capítulo.

**Quando entra:** passo 4.4 · Semana 2 · nov/2026; passo 34.6 · Semana 5 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | transcrição |
| → envia para | [Agente editor de conteúdo](23-oper.md#oedit) | Operação do grupo (esteira, marca, qualidade) | transcrição |
| → envia para | [Pipeline de conteúdo](23-oper.md#opipe) | Operação do grupo (esteira, marca, qualidade) | transcreve |
| → envia para | [Seus datasets (só conteúdo seu)](06-dados.md#dset) | Dados e treino de IA | transcrições das suas aulas |
| → envia para | [Voz local: Whisper, Piper, openWakeWord](05-ia.md#jvoz) | Agentes de IA e sandbox | transcreve |
| ← recebe de | [OBS Studio](13-cont.md#obss) | Produção de conteúdo | áudio |

<a id="voz"></a>

### Voz clonada (ElevenLabs)

*Remoto · precisa de conta*

Clonagem profissional da sua própria voz (plano Creator em diante, uso comercial nos planos pagos). Treino com 30 minutos ou mais de áudio limpo. Avise o público que a voz é gerada por IA.

**Quando entra:** passo 35.5 · Semana 5 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [DaVinci Resolve ou Kdenlive](13-cont.md#edit) | Produção de conteúdo | narração |
| → envia para | [Dublagem (YouTube + ElevenLabs)](21-mkt.md#dub) | Marketing, automação e medição | sua voz em outros idiomas |
| → envia para | [Curso por seção](15-editora.md#bcurso) | Editora AMS Silva (produção de livros) | narração |
| ← recebe de | [Workstation com GPU](01-hw.md#ws) | Hardware | voz e vídeo locais |
| ← recebe de | [GPU por hora (RunPod e afins)](12-nuvem.md#gpuh) | Nuvem, código e entrega | modelos abertos |
| ← recebe de | [Agente editor de conteúdo](23-oper.md#oedit) | Operação do grupo (esteira, marca, qualidade) | narração |

<a id="fabrica"></a>

### Fábrica de aulas

*Local*

Gera planejamentos e documentos da escola no modelo exigido, a partir da ementa e das suas regras. Sem dados de aluno.

**Quando entra:** passo 14.1 · Semanas 5 e 6 · nov/2026; passo 14.2 · Semanas 5 e 6 · nov/2026; passo 14.3 · Semanas 5 e 6 · nov/2026; passo 14.4 · Semanas 5 e 6 · nov/2026; passo 14.5 · Semanas 5 e 6 · nov/2026; passo 14.6 · Semanas 5 e 6 · nov/2026; passo 14.7 · Semanas 5 e 6 · nov/2026; passo 14.8 · Semanas 5 e 6 · nov/2026; passo 14.9 · Semanas 5 e 6 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Aulas particulares](17-prod.md#aulas) | Produtos (o que você vende) | material das aulas |

<a id="penpot"></a>

### Penpot (design)

*Local*

Design de telas e protótipos, aberto, alternativa ao Figma pago.

**Quando entra:** passo 33.8 · Com a primeira página de venda no ar (jan/2027) e por etapas ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Next.js + Aura Design System](11-app.md#front) | Aplicação: sistemas AM (Aura) | telas dos sistemas |

---

[↑ Camada 14 · Estudo e carreira](14-est.md) · [↓ Camada 12 · Nuvem, código e entrega](12-nuvem.md)
