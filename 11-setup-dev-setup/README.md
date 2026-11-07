<!-- Arquivo GERADO por tools/gerar_docs.py. Edite os dados em data/ ou o gerador. -->

# dev-setup

[![docs](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml/badge.svg)](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml)

Arquitetura completa do meu ambiente de desenvolvimento e de trabalho: do hardware ao deploy na nuvem, da criação de conteúdo à venda de cursos. Cada ferramenta tem um motivo, um lugar e conexões definidas, e toda a documentação é gerada a partir de uma única fonte de dados.

| Camadas | Blocos | Conexões | Fluxos | Contas necessárias |
|---|---|---|---|---|
| 23 | 485 | 860 | 22 | 129 |

## Por onde começar

- **Continuar numa conversa nova com o Claude**: cole o [CONTINUAR.md](CONTINUAR.md) (ou `python3 tools/sessao/contexto.py --inicio | clip.exe`) e diga qual passo vai fazer. As decisões recentes ficam no [ESTADO.md](ESTADO.md).
- **Comece aqui, no Windows**: extraia o zip, entre na pasta que tem `RODAR-DIAGNOSTICO.cmd` e clique com o botão direito nele > Executar como administrador. Ele só lê o notebook e diz por qual passo do roteiro começar.
- **Montar tudo de uma vez**: `cd ~/dev/dev-setup && just instalar` (veja antes com `just instalar --simular`). O plano de autonomia está no [Núcleo AMtech](docs/nucleo/README.md).
- **No Ubuntu, um comando só**: `cd ~/dev/dev-setup && just` lista tudo; `just check` antes de cada commit e `just triagem "o que você quer"` antes de construir algo novo. Ver [Empresa solo](docs/empresa-solo.md).
- **[Arquitetura](docs/arquitetura.md)**: a pilha inteira, camada por camada, com o diagrama de cada uma.
- **[Fluxos de ponta a ponta](docs/fluxos.md)**: codar com agente e publicar, vender um curso, publicar automaticamente, medir uma campanha e outros.
- **[Editora AMS Silva](docs/editora/README.md)**: livros produzidos como software, com código testado, gabaritos conferidos e PDF, EPUB e impressão gerados da mesma fonte.
- **[Implantação](docs/implantacao/README.md)**: do planejamento ao setup funcionando, com scripts de instalação, verificadores e o roteiro passo a passo.
- **[Operação do grupo](docs/operacao/README.md)**: a esteira por onde passa toda oferta, o portfólio com 108 ofertas pontuadas e classificadas (arsenal de rendas), marca, conteúdo, automação, qualidade e a ordem de execução.
- **[Negócios do grupo](docs/negocios/README.md)**: software, loja, robótica, ponto de retirada, entregas, delivery, sushi, cafeteria e padaria, com números, ordem de abertura e mínimo legal de cada um.
- **[Marketing, vendas e automação](docs/marketing/README.md)**: funil, canais sem rosto com voz clonada, publicação no melhor horário, tráfego pago, parcerias, internacional e lucro por venda.
- **[Segurança](docs/seguranca/README.md)**: engenharia reversa com IA, AppSec nos seus sistemas, o caminho até a AMtech Segurança (pentest com guarda de escopo e relatório CVSS) e o Jarvis.
- **[Jarvis](docs/jarvis/README.md)**: comandos de voz para o PC, a casa (energia, água, câmeras, portas, janelas, eletrodomésticos) e os robôs, com política de risco.
- **[Construção civil e arquitetura](docs/construcao/README.md)**: BIM aberto (Bonsai, FreeCAD), Autodesk educacional, SINAPI, regras da IA para engenharia e a automação BIM como renda.
- **Diagrama interativo**: baixe [`docs/index.html`](docs/index.html) e abra no navegador. Toque em qualquer bloco para ver as conexões dele.
- **[Toda a documentação](docs/README.md)**

## A pilha

```mermaid
flowchart TB
  L_oper["23 · Operação do grupo (esteira, marca, qualidade)"]
  L_pub["22 · Público e canais"]
  L_mkt["21 · Marketing, automação e medição"]
  L_venda["20 · Plataformas de venda e recebimento"]
  L_emp["19 · Pessoa física: impostos e finanças"]
  L_web["18 · Vitrine web (sites e domínio)"]
  L_prod["17 · Produtos (o que você vende)"]
  L_neg["16 · Negócios do grupo (Barbacena)"]
  L_editora["15 · Editora AMS Silva (produção de livros)"]
  L_est["14 · Estudo e carreira"]
  L_cont["13 · Produção de conteúdo"]
  L_nuvem["12 · Nuvem, código e entrega"]
  L_app["11 · Aplicação: sistemas AM (Aura)"]
  L_obs["10 · Observabilidade"]
  L_cnt["09 · Containers, Kubernetes e infra como código"]
  L_clc["08 · Claude: recursos, conectores e plugins"]
  L_chat["07 · Assistentes de IA (chat, pesquisa e estudo)"]
  L_dados["06 · Dados e treino de IA"]
  L_ia["05 · Agentes de IA e sandbox"]
  L_lin["04 · Linux (Ubuntu no WSL2, Arch no 2º disco)"]
  L_win["03 · Windows 11, apps e máquinas virtuais"]
  L_seg["02 · Segurança e cofre"]
  L_hw["01 · Hardware"]
  L_oper --- L_pub
  L_pub --- L_mkt
  L_mkt --- L_venda
  L_venda --- L_emp
  L_emp --- L_web
  L_web --- L_prod
  L_prod --- L_neg
  L_neg --- L_editora
  L_editora --- L_est
  L_est --- L_cont
  L_cont --- L_nuvem
  L_nuvem --- L_app
  L_app --- L_obs
  L_obs --- L_cnt
  L_cnt --- L_clc
  L_clc --- L_chat
  L_chat --- L_dados
  L_dados --- L_ia
  L_ia --- L_lin
  L_lin --- L_win
  L_win --- L_seg
  L_seg --- L_hw
  classDef cam fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class L_oper,L_pub,L_mkt,L_venda,L_emp,L_web,L_prod,L_neg,L_editora,L_est,L_cont,L_nuvem,L_app,L_obs,L_cnt,L_clc,L_chat,L_dados,L_ia,L_lin,L_win,L_seg,L_hw cam
```

## A ideia em uma frase

O Windows cuida só do que precisa de janela, GPU e segurança; todo o trabalho de engenharia roda em Linux (Ubuntu no WSL2), em containers, e sai para a nuvem por CI/CD. Agentes de IA trabalham dentro de uma sandbox que só enxerga a pasta do projeto.

## Camadas

| # | Camada | Blocos | Destaques |
|---|---|---|---|
| 23 | [Operação do grupo (esteira, marca, qualidade)](docs/camadas/23-oper.md) | 32 | Portfólio de ofertas, Esteira de ofertas, Padrão de qualidade, Marca pessoal Alan Mateus… |
| 22 | [Público e canais](docs/camadas/22-pub.md) | 12 | Meta Business Suite, Instagram, YouTube, LinkedIn… |
| 21 | [Marketing, automação e medição](docs/camadas/21-mkt.md) | 30 | Meta Ads (Instagram, Facebook), Isca grátis + sequência de e-mails, MailerLite, Postiz (agendador)… |
| 20 | [Plataformas de venda e recebimento](docs/camadas/20-venda.md) | 15 | Pix Automático + gateway (ex.: Asaas), Agenda online (Cal.com), CRM simples (planilha), Hotmart… |
| 19 | [Pessoa física: impostos e finanças](docs/camadas/19-emp.md) | 21 | Registro de marca (INPI), Termos, privacidade (LGPD) e contratos, Certificado digital (e-CNPJ), API de NFS-e (ex.: Focus NFe)… |
| 18 | [Vitrine web (sites e domínio)](docs/camadas/18-web.md) | 15 | E-mail profissional (enviar e receber), Domínio (Registro.br), Site pessoal + blog (Jekyll), Instituto AMS… |
| 17 | [Produtos (o que você vende)](docs/camadas/17-prod.md) | 8 | Mini-curso Lógica de Programação, Formações (TI, Matemática, Finanças), Templates e código-fonte, Livro Lógica e Máquina… |
| 16 | [Negócios do grupo (Barbacena)](docs/camadas/16-neg.md) | 19 | AMtech Software (projetos e SaaS), Loja AMtech (assistência), Peças sem estoque (sob encomenda), Ponto de retirada (Shopee e ML)… |
| 15 | [Editora AMS Silva (produção de livros)](docs/camadas/15-editora.md) | 36 | Selo Editora AMS Silva, Repositório do livro, Seu modelo de criação, Fonte única (Markdown + Pandoc)… |
| 14 | [Estudo e carreira](docs/camadas/14-est.md) | 16 | Microsoft Learn + AWS Skill Builder, TryHackMe / Hack The Box, Alura · Rocketseat · DIO · Udemy, Anki… |
| 13 | [Produção de conteúdo](docs/camadas/13-cont.md) | 8 | OBS Studio, DaVinci Resolve ou Kdenlive, Audacity, Canva · Krita · Inkscape… |
| 12 | [Nuvem, código e entrega](docs/camadas/12-nuvem.md) | 32 | Armazenamento de arquivos (Blob/R2), E-mail transacional (Resend, SES…), SonarQube Cloud, Projects · ADRs · MkDocs… |
| 11 | [Aplicação: sistemas AM (Aura)](docs/camadas/11-app.md) | 26 | OpenAPI + Scalar, PostGIS + MapLibre, Storybook, Clean Arch + DDD… |
| 10 | [Observabilidade](docs/camadas/10-obs.md) | 10 | Sentry (erros), Uptime Kuma, Seq (logs), Loki + Tempo… |
| 09 | [Containers, Kubernetes e infra como código](docs/camadas/09-cnt.md) | 16 | Caddy (proxy + HTTPS), Mailpit, Kafka, kubectl · Helm · k9s… |
| 08 | [Claude: recursos, conectores e plugins](docs/camadas/08-clc.md) | 19 | Projects + memória, Artifacts (Docs, Slides, Sheets…), Pesquisa aprofundada, Tarefas agendadas… |
| 07 | [Assistentes de IA (chat, pesquisa e estudo)](docs/camadas/07-chat.md) | 10 | Claude (app), ChatGPT, Gemini (pago), NotebookLM… |
| 06 | [Dados e treino de IA](docs/camadas/06-dados.md) | 22 | Python de dados (Polars, Jupyter), DuckDB + Parquet, dbt Core, Airflow (orquestração)… |
| 05 | [Agentes de IA e sandbox](docs/camadas/05-ia.md) | 26 | Modelos locais: Qwen · Gemma · Llama, Base de conhecimento (RAG) das suas notas, Claude Code, ai-jail… |
| 04 | [Linux (Ubuntu no WSL2, Arch no 2º disco)](docs/camadas/04-lin.md) | 29 | Neovim, nmap · dig · curl, Ubuntu (WSL2), Git + SSH + gh… |
| 03 | [Windows 11, apps e máquinas virtuais](docs/camadas/03-win.md) | 32 | Tailscale (VPN), .wslconfig + localhost, Terminal · PowerShell · winget, Excalidraw / draw.io… |
| 02 | [Segurança e cofre](docs/camadas/02-seg.md) | 25 | Commits assinados (chave SSH), restic (backup criptografado), Chave física (YubiKey), TPM + Secure Boot… |
| 01 | [Hardware](docs/camadas/01-hw.md) | 26 | Nobreak, Base com cooler, SSD SATA 2,5", Acer Nitro (32 GB, GTX 1650)… |

## Stack

Sistemas AM: C#/.NET 10 · ASP.NET Core (Controllers) · Clean Architecture + DDD · PostgreSQL · Redis · SignalR · Next.js, TypeScript, Tailwind e Zod · Docker · GitHub Actions · Kamal. Fora deles, a melhor ferramenta para cada trabalho ([ADR 0007](docs/adr/0007-poliglota-por-funcao.md)): Astro para sites, SvelteKit e PocketBase para MVPs, Go para CLIs, Rust para firmware, Python para dados e IA. Principal e reserva de cada função no [ADR 0008](docs/adr/0008-trocas-de-ferramenta-principal.md).

## Como este repositório funciona

```mermaid
flowchart LR
  D["data/ecossistema.json<br/>data/mapa.json"] --> G["tools/gerar_docs.py"]
  G --> M["docs/*.md<br/>23 páginas de camada"]
  G --> H["docs/index.html<br/>diagrama interativo"]
  G --> R["README.md"]
  CI["GitHub Actions"] -->|"valida e confere"| G
```

1. Tudo nasce em [`data/`](data): camadas, blocos, conexões, fluxos, contas e o plano.
2. `python tools/gerar_docs.py` valida os dados (ids, conexões quebradas, rótulos) e regenera as páginas, o diagrama e este README.
3. O GitHub Actions roda `python tools/gerar_docs.py --check` a cada push: se os dados tiverem erro ou os arquivos gerados estiverem desatualizados, o build falha.

## Estrutura

```
data/                 fonte única: ecossistema, mapa, negócios, portfólio e implantação
docs/
  arquitetura.md      a pilha e as ligações entre camadas
  camadas/            uma página por camada, com diagrama e conexões de cada bloco
  fluxos.md           fluxos de ponta a ponta
  marketing/          funil, IA, publicação, tráfego, canais, parcerias, internacional, lucro
  infra/              vários computadores, SSD externo, NAS local e em nuvem
  editora/            Editora AMS Silva: pipeline dos livros, rigor, produtos e lançamento
  implantacao/        roteiro de implantação e acompanhamento (gerados)
  operacao/           esteira, portfólio, marca, conteúdo, automação, qualidade, execução
  negocios/           os nove negócios do grupo: estrutura, ordem, números, cardápios, licenças
  seguranca/          engenharia reversa, AppSec e empresa de pentest
  jarvis/             voz, casa, câmeras, energia, água, robótica e PC por comando de voz
  construcao/         construção civil, arquitetura e engenharia civil pela TI
  contas.md, auditoria.md, nuvem.md, roteiro.md, ...
  adr/                decisões de arquitetura
  index.html          diagrama interativo (gerado)
  mapa.html           sistemas, nuvens, pilha, mercado e ordem de estudo (gerado)
scripts/windows/      instalar.ps1, verificar.ps1, extensões do VS Code e o inventário do Windows
scripts/wsl/          bootstrap.sh, nuvem.sh, verificar.sh e ativar-pipeline.sh
infra/automacao/      n8n, banco de métricas, Grafana e Uptime Kuma (Docker Compose)
infra/lab-seguranca/  laboratório de ataque local (Juice Shop, WebGoat) presos em 127.0.0.1
infra/lab-alvo/       alvo isolado sem internet: o software que você estudou contra o atacante
infra/jarvis/         voz local (Whisper, Piper, openWakeWord), MQTT, Zigbee2MQTT e Frigate
config/marca.md       guia de marca usado pelo pipeline de conteúdo
infra/templates/     repositório padrão, deploy com Kamal, esteira de sites, regras da IA e segurança
tools/                geradores, motor financeiro, pipeline de conteúdo e templates
justfile              porta única de comandos (check, triagem, arquiteto, docs, ci-local)
```

## Status

Em construção por fases. A fase 1 (Windows, WSL2, Docker e .NET) está em andamento; o restante segue o [roteiro de estudo](docs/roteiro.md).

## Licença

[MIT](LICENSE)
