---
tags: [setup, dev-setup, indice, passo-a-passo, fluxogramas]
tipo: indice
atualizado: 2026-10-26
---

# 🖥️ Setup completo (dev-setup) dentro do vault

> **Em palavras simples:** esta pasta é o repositório `dev-setup` inteiro, copiado para dentro do vault. Nela estão os documentos, os 17 fluxogramas, o roteiro passo a passo de 34 fases e 253 passos, as páginas interativas, os dados e os scripts que instalam o notebook. Assim o estudo e o setup ficam no mesmo repositório e se ligam pelo [Plano Mestre](../00-PLANO-MESTRE-PASSO-A-PASSO.md), onde cada passo do setup aparece com o código `S-…`.
>
> **O que fazer primeiro:** siga o [Plano Mestre](../00-PLANO-MESTRE-PASSO-A-PASSO.md) a partir da Etapa 0. Ele manda abrir os documentos daqui quando for a hora.

## Se você não está vendo tudo

| O que acontece | Por quê | O que fazer |
|---|---|---|
| No GitHub não aparece esta pasta nem o Plano Mestre | Nada foi publicado ainda: as mudanças estão só no `vault-completo.zip` | Use o zip, ou peça para publicar |
| No Obsidian não aparecem os arquivos `.html`, `.json`, `.ps1` e `.sh` | O Obsidian só mostra notas, imagens e PDF | Configurações > Arquivos e links > ligue **Detectar todas as extensões de arquivo** |
| Clicar num `.html` no Obsidian não mostra a página | O Obsidian não abre página interativa | Botão direito > **Abrir no aplicativo padrão** (abre no navegador), ou use a versão publicada no claude.ai |
| A pasta `.github` não aparece | O Obsidian esconde pastas que começam com ponto | Normal: são só os testes automáticos |
| Um fluxograma aparece como texto | O modo de leitura não está ligado | Troque para **Modo de leitura** (Ctrl+E). Diagrama largo: role para o lado ou abra a página Fluxogramas |
| Os 326 blocos não aparecem num lugar só | Eles ficam na página interativa do ecossistema e nas 23 camadas | No [Plano Mestre](../00-PLANO-MESTRE-PASSO-A-PASSO.md), a seção **Todos os blocos do setup** lista os 326, camada por camada, com o passo em que cada um entra |

## Como usar esta pasta

1. **Para ler e planejar:** abra os documentos abaixo aqui mesmo no Obsidian. Os fluxogramas aparecem desenhados, porque são blocos Mermaid.
2. **Para marcar o que já fez:** use o [Plano Mestre](../00-PLANO-MESTRE-PASSO-A-PASSO.md) ou a página interativa do Plano Mestre. Ela fica no seu claude.ai e tem uma cópia em `ferramentas/plano-mestre-ams.html`.
3. **Para instalar o notebook:** os scripts precisam estar em `C:\Users\SEU_USUARIO\dev-setup`, porque todos os comandos do roteiro apontam para lá. Use o `dev-setup.zip`, ou copie esta pasta para esse lugar com o nome `dev-setup`. Depois clique com o botão direito em `RODAR-DIAGNOSTICO.cmd` > Executar como administrador.
4. **Para mudar alguma coisa:** os documentos com o aviso "Arquivo GERADO" saem dos arquivos de `data/`. Mude o dado e rode os geradores, senão a próxima geração desfaz a sua mudança. A lista dos geradores está no [README do setup](README.md).

## O passo a passo

| Documento | O que tem |
|---|---|
| [Roteiro de implantação](docs/implantacao/roteiro.md) | As 34 fases e os 253 passos, com comando, "pronto quando", quem faz e quanto tempo leva |
| [Implantação (explicação)](docs/implantacao/README.md) | Como o roteiro funciona, a fase de senhas, o caminho até a primeira venda e o que dá para fazer hoje |
| [Acompanhamento (página)](docs/implantacao/acompanhamento.html) | Caixinhas para marcar os passos do setup (abra no navegador) |
| [Roteiro de estudo do setup](docs/roteiro.md) | As etapas técnicas (Azure, dados, IA, Linux e segurança), com as datas presas aos Passos do vault |
| [Plano Mestre (vault)](../00-PLANO-MESTRE-PASSO-A-PASSO.md) | Os dois planejamentos juntos: setup, estudo, rendas, finanças, faculdade e certificações |

## Os fluxogramas

Os 17 fluxos de ponta a ponta estão em [fluxos.md](docs/fluxos.md):

| Fluxo | Fluxo | Fluxo |
|---|---|---|
| Vender o mini-curso | Codar com agente e publicar | Conseguir a vaga de dev |
| Do livro ao leitor | Estudar e preparar aula com IA | Laboratório de segurança |
| Site para um cliente | Publicar automaticamente no melhor horário | Medir o lucro de uma campanha |
| Produzir um capítulo do livro | Ilustrar um capítulo | Abrir o próximo negócio |
| Do trabalho ao conteúdo | Treinar uma IA sua | Dados de venda viram decisão |
| Do documento antigo à venda | Do notebook à primeira venda | |

Também há um diagrama em cada uma das 23 camadas (abaixo), e diagramas na [arquitetura](docs/arquitetura.md), no [portfólio](docs/operacao/portfolio.md), nos [negócios](docs/negocios/README.md), na [editora](docs/editora/README.md), no [marketing](docs/marketing/README.md) e na [operação](docs/operacao/README.md).

## Os mapas e as páginas interativas

Abra os arquivos `.html` no navegador (botão direito > Abrir no aplicativo padrão), ou use as versões publicadas no seu claude.ai, que têm os mesmos nomes.

| Página | Versão publicada | O que mostra |
|---|---|---|
| [Diagrama do ecossistema](docs/index.html) | Ecossistema AMtech | Os 326 blocos e as 609 conexões, camada por camada |
| [Mapa do setup](docs/mapa.html) | Mapa do Setup AMtech | Sistemas operacionais, nuvens, ordem de estudo e mercado |
| [Acompanhamento](docs/implantacao/acompanhamento.html) | Implantação AMtech | O roteiro com caixinhas |
| [Portfólio](docs/operacao/portfolio.html) | Portfólio AMtech | As 47 ofertas pontuadas |
| [Planejador do grupo](docs/negocios/planejador.html) | Planejador do Grupo | Os números dos 9 negócios e os 5 portões |
| [Lucro por venda](ferramentas/lucro-por-venda.html) | Lucro por Venda | Quanto sobra em cada venda, por plataforma e canal |
| [Plano Mestre](ferramentas/plano-mestre-ams.html) | Plano Mestre AMS | Os 391 itens dos dois planejamentos, com caixinhas |
| [Fluxogramas](ferramentas/fluxogramas-setup.html) | Fluxogramas do Setup | Os 68 diagramas dos documentos numa página só |

## As 23 camadas do setup

Cada camada tem o diagrama dela e diz, bloco por bloco, em que passo do roteiro ele entra.

| Camada | Camada |
|---|---|
| [01 Hardware](docs/camadas/01-hw.md) | [02 Segurança e cofre](docs/camadas/02-seg.md) |
| [03 Windows 11, apps e máquinas virtuais](docs/camadas/03-win.md) | [04 Linux (Ubuntu no WSL2, Arch no 2º disco)](docs/camadas/04-lin.md) |
| [05 Agentes de IA e sandbox](docs/camadas/05-ia.md) | [06 Dados e treino de IA](docs/camadas/06-dados.md) |
| [07 Assistentes de IA (chat, pesquisa e estudo)](docs/camadas/07-chat.md) | [08 Claude: recursos, conectores e plugins](docs/camadas/08-clc.md) |
| [09 Containers, Kubernetes e infra como código](docs/camadas/09-cnt.md) | [10 Observabilidade](docs/camadas/10-obs.md) |
| [11 Aplicação: sistemas AM (Aura)](docs/camadas/11-app.md) | [12 Nuvem, código e entrega](docs/camadas/12-nuvem.md) |
| [13 Produção de conteúdo](docs/camadas/13-cont.md) | [14 Estudo e carreira](docs/camadas/14-est.md) |
| [15 Editora AMS Silva (produção de livros)](docs/camadas/15-editora.md) | [16 Negócios do grupo (Barbacena)](docs/camadas/16-neg.md) |
| [17 Produtos (o que você vende)](docs/camadas/17-prod.md) | [18 Vitrine web (sites e domínio)](docs/camadas/18-web.md) |
| [19 Pessoa física: impostos e finanças](docs/camadas/19-emp.md) | [20 Plataformas de venda e recebimento](docs/camadas/20-venda.md) |
| [21 Marketing, automação e medição](docs/camadas/21-mkt.md) | [22 Público e canais](docs/camadas/22-pub.md) |
| [23 Operação do grupo (esteira, marca, qualidade)](docs/camadas/23-oper.md) |  |

## Os outros documentos

- **Visão geral:** [Documentação](docs/README.md) · [Arquitetura](docs/arquitetura.md) · [Auditoria](docs/auditoria.md) · [Contas e conexões](docs/contas.md) · [Decisões](docs/fora-do-setup.md) · [Peças autorais](docs/pecas-autorais.md)
- **Técnico:** [Sistemas operacionais](docs/sistemas-operacionais.md) · [Nuvem](docs/nuvem.md) · [Mercado](docs/mercado.md) · [Vários computadores, SSD e NAS](docs/infra/README.md) · decisões de arquitetura: [WSL2](docs/adr/0001-wsl2-em-vez-de-dual-boot.md), [agentes em sandbox](docs/adr/0002-agentes-de-ia-em-sandbox.md), [Azure primeiro](docs/adr/0003-azure-primeiro.md)
- **Dinheiro e operação:** [Operação do grupo](docs/operacao/README.md) (esteira de ofertas, marca, conteúdo, automação, qualidade, clientes, ordem de execução) · [Portfólio de ofertas](docs/operacao/portfolio.md)
- **Marketing:** [Marketing, vendas e automação](docs/marketing/README.md) (funil, canais sem rosto, publicação automática, anúncios, parcerias, internacional, medição, custos, riscos, 90 dias, canais de anúncio)
- **Negócios em Barbacena:** [Negócios do grupo](docs/negocios/README.md) · [Números de cada negócio](docs/negocios/numeros.md) · os 9 negócios, cardápios, mínimo legal para abrir e sistemas do grupo
- **Editora AMS Silva:** [Editora](docs/editora/README.md) (estrutura legal, produção, rigor, identidade visual, avaliação, produtos, lançamento, roteiro, nível e concursos, imagens, automação)
- **Marca:** [Guia de marca](config/marca.md)
- **Ferramentas:** [Acervo](tools/acervo/README.md) · [Pipeline de conteúdo](tools/conteudo/README.md) · [Postiz](infra/postiz/README.md) · [Plano Mestre](tools/plano_mestre/README.md)
- **Histórico:** [CHANGELOG](CHANGELOG.md) (o que mudou em cada versão, até a 1.16.0)

## O que tem em cada pasta

| Pasta | O que tem |
|---|---|
| `data/` | Os dados de onde tudo é gerado: ecossistema, roteiro, mapa, portfólio e negócios |
| `docs/` | Os documentos e as páginas geradas |
| `scripts/windows/` | Diagnóstico, inventário, instalador, verificador e extensões do VS Code |
| `scripts/wsl/` | Bootstrap do Ubuntu, cofre do Obsidian, laboratório de IA, nuvem, pipeline e verificador |
| `infra/` | n8n, banco de métricas, Grafana e Uptime Kuma (Docker Compose); Postiz |
| `tools/` | Os geradores dos documentos, o acervo, o pipeline de conteúdo, o planejador financeiro e o Plano Mestre, cada um com testes |
| `ferramentas/` | Cópias das páginas Lucro por Venda e Plano Mestre, que não saem dos geradores |
| `.github/workflows/` | Os testes automáticos. Dentro do vault eles não rodam sozinhos: só rodam quando o `dev-setup` está no próprio repositório dele |
