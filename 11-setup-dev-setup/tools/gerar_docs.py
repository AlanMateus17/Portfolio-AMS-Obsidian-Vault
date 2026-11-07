#!/usr/bin/env python3
"""Gera toda a documentação do setup a partir de data/*.json.

Fonte única da verdade: data/ecossistema.json (camadas, blocos, conexões, fluxos,
contas, auditoria) e data/mapa.json (sistemas operacionais, nuvens, mercado,
roteiro, peças autorais, cortes).

Uso:
    python tools/gerar_docs.py          # valida os dados e regenera os arquivos
    python tools/gerar_docs.py --check  # valida e falha se algo gerado estiver desatualizado (CI)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"
DOCS = RAIZ / "docs"
TEMPLATE_HTML = RAIZ / "tools" / "diagrama.template.html"
TEMPLATE_MAPA = RAIZ / "tools" / "mapa.template.html"

TIPO = {"local": "Local", "remoto": "Remoto", "fisico": "Físico"}
FASE = {"ok": "Instalado", "f1": "Agora", "f2": "Próximos 3 meses", "f3": "3 a 12 meses", "fut": "Depois de 12 meses", "dec": "Decisão sua"}
ID_RE = re.compile(r"^[a-z0-9]+$")


# ---------------------------------------------------------------- carga e validação

def carregar() -> tuple[dict, dict]:
    eco = json.loads((DADOS / "ecossistema.json").read_text(encoding="utf-8"))
    mapa = json.loads((DADOS / "mapa.json").read_text(encoding="utf-8"))
    return eco, mapa


def validar(eco: dict) -> list[str]:
    erros: list[str] = []
    camadas = {c["id"] for c in eco["camadas"]}
    if len(camadas) != len(eco["camadas"]):
        erros.append("Há camadas com id repetido.")
    ids: set[str] = set()
    for b in eco["blocos"]:
        if b["id"] in ids:
            erros.append(f"Bloco com id repetido: {b['id']}")
        ids.add(b["id"])
        if not ID_RE.match(b["id"]):
            erros.append(f"Id inválido (use a-z e 0-9): {b['id']}")
        if b["camada"] not in camadas:
            erros.append(f"Bloco {b['id']} aponta para camada inexistente: {b['camada']}")
        if b["tipo"] not in TIPO:
            erros.append(f"Bloco {b['id']} com tipo inválido: {b['tipo']}")
        for linha in b["rotulo"].split("|"):
            if len(linha) > 21:
                erros.append(f"Rótulo longo demais no bloco {b['id']} (máx. 21 por linha): {linha!r}")
        if not b["descricao"].strip():
            erros.append(f"Bloco {b['id']} sem descrição.")
    vistos: set[tuple[str, str]] = set()
    for c in eco["conexoes"]:
        for ponta in (c["de"], c["para"]):
            if ponta not in ids:
                erros.append(f"Conexão {c['de']} → {c['para']} usa bloco inexistente: {ponta}")
        par = (c["de"], c["para"])
        if par in vistos:
            erros.append(f"Conexão repetida: {c['de']} → {c['para']}")
        if (c["para"], c["de"]) in vistos:
            erros.append(f"Conexão nos dois sentidos (deixe uma só): {c['de']} ↔ {c['para']}")
        if c["de"] == c["para"]:
            erros.append(f"Conexão de um bloco com ele mesmo: {c['de']}")
        if not c["rotulo"].strip():
            erros.append(f"Conexão {c['de']} → {c['para']} sem rótulo")
        vistos.add(par)
    ligados = {p for par in vistos for p in par}
    for b in eco["blocos"]:
        if b["id"] not in ligados:
            erros.append(f"Bloco {b['id']} sem nenhuma conexão: ligue ao que ele alimenta ou de que depende")
    for f in eco["fluxos"]:
        for p in f["passos"]:
            if p["bloco"] not in ids:
                erros.append(f"Fluxo {f['id']} usa bloco inexistente: {p['bloco']}")
        s = [p["bloco"] for p in f["passos"]]
        for a, b in zip(s, s[1:]):
            if (a, b) not in vistos and (b, a) not in vistos:
                erros.append(f"Fluxo {f['id']}: o passo {a} → {b} não tem conexão no desenho")
    return erros


# ---------------------------------------------------------------- utilidades

def nome(b: dict) -> str:
    return b["rotulo"].replace("|", " ")


def num(eco: dict, camada_id: str) -> int:
    ordem = [c["id"] for c in eco["camadas"]]
    return len(ordem) - ordem.index(camada_id)


def arquivo_camada(eco: dict, camada_id: str) -> str:
    return f"{num(eco, camada_id):02d}-{camada_id}.md"


def mm(texto: str) -> str:
    """Escapa texto para rótulos do Mermaid."""
    return (texto.replace('"', "#quot;").replace("<", "#lt;").replace(">", "#gt;")
            .replace("|", " "))


def selos(b: dict) -> str:
    partes = [TIPO[b["tipo"]]]
    if b["conta"]:
        partes.append("precisa de conta")
    if b["futuro"]:
        partes.append("futuro")
    return " · ".join(partes)


AVISO = "<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->\n\n"


# ---------------------------------------------------------------- geradores

def gerar_camada(eco: dict, camada: dict, por_id: dict, saidas: dict, entradas: dict) -> str:
    cid = camada["id"]
    n = num(eco, cid)
    blocos = [b for b in eco["blocos"] if b["camada"] == cid]
    ordem = [c["id"] for c in eco["camadas"]]
    idx = ordem.index(cid)
    titulo_por_id = {c["id"]: c["titulo"] for c in eco["camadas"]}

    out = [AVISO, f"# Camada {n:02d} · {camada['titulo']}\n"]
    out.append(f"[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)\n")
    if camada["ponte"]:
        out.append(f"> **Ligação com a camada de baixo:** {camada['ponte']}\n")
    contas = sum(1 for b in blocos if b["conta"])
    futuros = sum(1 for b in blocos if b["futuro"])
    out.append(f"**{len(blocos)} blocos** · {contas} precisam de conta · {futuros} marcados como futuro\n")

    # diagrama da camada com vizinhos agrupados por camada
    linhas = ["```mermaid", "flowchart LR"]
    vizinhos: dict[str, set[str]] = defaultdict(set)
    arestas: list[tuple[str, str, str]] = []
    for b in blocos:
        for c in saidas[b["id"]] + entradas[b["id"]]:
            if (c["de"], c["para"], c["rotulo"]) in arestas:
                continue
            arestas.append((c["de"], c["para"], c["rotulo"]))
            for ponta in (c["de"], c["para"]):
                if por_id[ponta]["camada"] != cid:
                    vizinhos[por_id[ponta]["camada"]].add(ponta)
    linhas.append(f'  subgraph L_{cid}["{mm(camada["titulo"])}"]')
    for b in blocos:
        linhas.append(f'    n_{b["id"]}["{mm(nome(b))}"]')
    linhas.append("  end")
    for outra in ordem:
        if outra in vizinhos:
            linhas.append(f'  subgraph L_{outra}["{mm(titulo_por_id[outra])}"]')
            for bid in sorted(vizinhos[outra]):
                linhas.append(f'    n_{bid}["{mm(nome(por_id[bid]))}"]')
            linhas.append("  end")
    for de, para, rot in arestas:
        linhas.append(f'  n_{de} -->|"{mm(rot)}"| n_{para}')
    linhas.append(f"  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b")
    if blocos:
        linhas.append("  class " + ",".join(f"n_{b['id']}" for b in blocos) + " desta")
    linhas.append("```\n")
    out.append("## Mapa de conexões\n")
    out.append("\n".join(linhas))

    out.append("## Blocos\n")
    out.append("| Bloco | Tipo | O que faz | Quando entra |\n|---|---|---|---|")
    for b in blocos:
        out.append(f"| [{nome(b)}](#{b['id']}) | {selos(b)} | {b['descricao']} | {b.get('quando', '')} |")
    out.append("")

    for b in blocos:
        out.append(f'<a id="{b["id"]}"></a>\n')
        out.append(f"### {nome(b)}\n")
        out.append(f"*{selos(b)}*\n")
        out.append(f"{b['descricao']}\n")
        if b.get("quando"):
            out.append(f"**Quando entra:** {b['quando']} ([roteiro](../implantacao/roteiro.md))\n")
        if saidas[b["id"]] or entradas[b["id"]]:
            out.append("| Direção | Bloco | Camada | O que passa |\n|---|---|---|---|")
            for c in saidas[b["id"]]:
                d = por_id[c["para"]]
                out.append(f"| → envia para | [{nome(d)}]({arquivo_camada(eco, d['camada'])}#{d['id']}) | {titulo_por_id[d['camada']]} | {c['rotulo']} |")
            for c in entradas[b["id"]]:
                o = por_id[c["de"]]
                out.append(f"| ← recebe de | [{nome(o)}]({arquivo_camada(eco, o['camada'])}#{o['id']}) | {titulo_por_id[o['camada']]} | {c['rotulo']} |")
            out.append("")
        else:
            out.append("_Sem conexões registradas._\n")

    nav = []
    if idx > 0:
        cima = ordem[idx - 1]
        nav.append(f"[↑ Camada {num(eco, cima):02d} · {titulo_por_id[cima]}]({arquivo_camada(eco, cima)})")
    if idx < len(ordem) - 1:
        baixo = ordem[idx + 1]
        nav.append(f"[↓ Camada {num(eco, baixo):02d} · {titulo_por_id[baixo]}]({arquivo_camada(eco, baixo)})")
    out.append("---\n\n" + " · ".join(nav) + "\n")
    return "\n".join(out)


def gerar_arquitetura(eco: dict, por_camada: dict) -> str:
    out = [AVISO, "# Arquitetura do setup\n", "[← Índice da documentação](README.md)\n"]
    out.append("A pilha vai do público (topo) ao hardware (base). Cada linha é a ligação entre uma camada e a de baixo; o detalhe de cada ligação está na tabela abaixo e em cada página de camada.\n")
    linhas = ["```mermaid", "flowchart TB"]
    for c in eco["camadas"]:
        n = num(eco, c["id"])
        linhas.append(f'  L_{c["id"]}["{n:02d} · {mm(c["titulo"])}<br/>{len(por_camada[c["id"]])} blocos"]')
    ids = [c["id"] for c in eco["camadas"]]
    for a, b in zip(ids, ids[1:]):
        linhas.append(f"  L_{a} --- L_{b}")
    linhas.append("  classDef cam fill:#e2ecec,stroke:#0e3a45,color:#13262b")
    linhas.append("  class " + ",".join(f"L_{i}" for i in ids) + " cam")
    linhas.append("```\n")
    out.append("\n".join(linhas))
    out.append("## Camadas e ligações\n")
    out.append("| # | Camada | Blocos | Como se liga à camada de baixo |\n|---|---|---|---|")
    for c in eco["camadas"]:
        out.append(f"| {num(eco, c['id']):02d} | [{c['titulo']}](camadas/{arquivo_camada(eco, c['id'])}) | {len(por_camada[c['id']])} | {c['ponte'] or '—'} |")
    out.append("")
    out.append("## Princípios\n")
    out.append("- O Windows cuida só do que precisa de janela, GPU e segurança; o código vive e roda no Linux (Ubuntu no WSL2). Ver [ADR 0001](adr/0001-wsl2-em-vez-de-dual-boot.md).")
    out.append("- Agentes de IA trabalham dentro de sandbox e só enxergam a pasta do projeto. Ver [ADR 0002](adr/0002-agentes-de-ia-em-sandbox.md).")
    out.append("- Infraestrutura por código, Azure primeiro e AWS depois. Ver [ADR 0003](adr/0003-azure-primeiro.md).")
    out.append("- Produção barata em VM pelo Kamal, um deploy só. Ver [ADR 0005](adr/0005-deploy-em-vm-com-kamal.md). Contrato no OpenAPI e Zod só no front. Ver [ADR 0006](adr/0006-contratos-na-borda.md).")
    out.append("- Antes de construir, a triagem: subir pronto, colar ou construir (`just triagem`). Ver [Empresa solo](empresa-solo.md).")
    out.append("- Tudo conectado pelo Núcleo AMtech: as ferramentas falam com um banco central e os agentes agem pela política de autonomia. Ver [ADR 0009](adr/0009-nucleo-amtech.md).")
    out.append("- A melhor ferramenta para cada trabalho, sem linguagem proibida. Ver [ADR 0007](adr/0007-poliglota-por-funcao.md); principal e reserva de cada função no [ADR 0008](adr/0008-trocas-de-ferramenta-principal.md).")
    out.append("- Uma ferramenta por função: o que repete outra fica de fora ([decisões](fora-do-setup.md)).")
    out.append("- Segredos só no KeePassXC; nunca no repositório.\n")
    return "\n".join(out)


def gerar_fluxos(eco: dict, por_id: dict) -> str:
    out = [AVISO, "# Fluxos de ponta a ponta\n", "[← Índice da documentação](README.md)\n"]
    out.append("Cada fluxo mostra o caminho real que o trabalho percorre pelas camadas.\n")
    for f in eco["fluxos"]:
        out.append(f"## {f['titulo']}\n")
        linhas = ["```mermaid", "flowchart LR"]
        for i, p in enumerate(f["passos"]):
            linhas.append(f'  s{i}["{i + 1}. {mm(nome(por_id[p["bloco"]]))}"]')
        for i in range(len(f["passos"]) - 1):
            linhas.append(f"  s{i} --> s{i + 1}")
        linhas.append("```\n")
        out.append("\n".join(linhas))
        for i, p in enumerate(f["passos"]):
            b = por_id[p["bloco"]]
            out.append(f"{i + 1}. **[{nome(b)}](camadas/{arquivo_camada(eco, b['camada'])}#{b['id']})**: {p['descricao']}")
        out.append("")
    return "\n".join(out)


def gerar_lista(titulo: str, intro: str, grupos: list[dict]) -> str:
    out = [AVISO, f"# {titulo}\n", "[← Índice da documentação](README.md)\n", f"{intro}\n"]
    for g in grupos:
        out.append(f"## {g['grupo']}\n")
        out.append("| Item | Observação |\n|---|---|")
        for it in g["itens"]:
            out.append(f"| **{it['nome']}** | {it['obs']} |")
        out.append("")
    return "\n".join(out)


def gerar_planejamento(mapa: dict) -> dict[str, str]:
    arq: dict[str, str] = {}
    o = [AVISO, "# Sistemas operacionais\n", "[← Índice da documentação](README.md)\n"]
    o.append("Arch e Kali entram, mas sem dual boot no disco atual: Arch no segundo NVMe, o resto em VMs.\n")
    o.append("| Sistema | Origem | Fase | Onde roda | Por quê |\n|---|---|---|---|---|")
    for s in mapa["sistemas"]:
        o.append(f"| **{s['nome']}** | {s['origem']} | {FASE[s['fase']]} | {s['onde']} | {s['porque']} |")
    arq["sistemas-operacionais.md"] = "\n".join(o) + "\n"

    o = [AVISO, "# Nuvem\n", "[← Índice da documentação](README.md)\n"]
    for n in mapa["nuvens"]:
        o.append(f"## {n['nome']}\n")
        o.append(f"*{n['papel']} · {FASE[n['fase']]}*\n")
        for d in n["detalhes"]:
            o.append(f"- **{d['k']}:** {d['v']}")
        o.append("")
    arq["nuvem.md"] = "\n".join(o)

    m = mapa["mercado"]
    o = [AVISO, "# Mercado\n", "[← Índice da documentação](README.md)\n"]
    for chave, titulo in (("nuvem", "Fatia do mercado de nuvem (receita)"), ("uso", "Uso entre desenvolvedores")):
        o.append(f"## {titulo}\n")
        o.append(f"Fonte: {m[chave]['fonte']}\n")
        o.append("```mermaid")
        o.append("xychart-beta")
        o.append(f'  x-axis [{", ".join(chr(34) + mm(d["n"]) + chr(34) for d in m[chave]["dados"])}]')
        o.append('  y-axis "%" 0 --> 100')
        o.append(f'  bar [{", ".join(str(d["v"]) for d in m[chave]["dados"])}]')
        o.append("```\n")
        o.append("| Item | % |\n|---|---|")
        for d in m[chave]["dados"]:
            o.append(f"| {d['n']} | {str(d['v']).replace('.', ',')} |")
        o.append("")
    o.append("## Tendências\n")
    for t in m["tendencias"]:
        o.append(f"- **{t['t']}:** {t['d']}")
    arq["mercado.md"] = "\n".join(o) + "\n"

    o = [AVISO, "# Roteiro de estudo\n", "[← Índice da documentação](README.md)\n"]
    o.append("Do que aparece em quase toda vaga .NET para o que só pesa em vagas avançadas. Cada etapa termina com algo publicado.\n")
    for i, r in enumerate(mapa["roteiro"], 1):
        o.append(f"{i}. **{r['etapa']}** ({r['quando']}): {r['o_que']}")
    arq["roteiro.md"] = "\n".join(o) + "\n"

    o = [AVISO, "# Peças autorais\n", "[← Índice da documentação](README.md)\n"]
    o.append("Agentes, skills, hooks e ferramentas que fazem parte do setup e são construídos por mim.\n")
    o.append("| Peça | Tipo | Fase | O que faz |\n|---|---|---|---|")
    for p in mapa["pecas"]:
        o.append(f"| **{p['nome']}** | {p['tipo']} | {FASE[p['fase']]} | {p['descricao']} |")
    arq["pecas-autorais.md"] = "\n".join(o) + "\n"

    o = [AVISO, "# Decisões: o que entra de outro jeito e o que fica de fora\n", "[← Índice da documentação](README.md)\n",
         "Nada do planejamento foi retirado. Os quatro primeiros entram por outro caminho, com passo e data no "
         "[roteiro](implantacao/roteiro.md); os outros são decisões suas ou de segurança, e voltam se você mudar de ideia.\n"]
    o.append("| Item | Decisão |\n|---|---|")
    for c in mapa["fora"]:
        o.append(f"| {c['item']} | {c['motivo']} |")
    arq["fora-do-setup.md"] = "\n".join(o) + "\n"
    return arq


def gerar_indice_docs(eco: dict, por_camada: dict) -> str:
    out = [AVISO, "# Documentação\n", "[← README](../README.md)\n"]
    out.append("- [Arquitetura](arquitetura.md): a pilha completa e como as camadas se ligam")
    out.append("- [Fluxos de ponta a ponta](fluxos.md)")
    out.append("- [Contas e conexões](contas.md)")
    out.append("- [Auditoria: o que faltava](auditoria.md)")
    out.append("- [Sistemas operacionais](sistemas-operacionais.md) · [Nuvem](nuvem.md) · [Mercado](mercado.md) · [Roteiro de estudo](roteiro.md)")
    out.append("- [Peças autorais](pecas-autorais.md) · [Decisões](fora-do-setup.md)")
    out.append("- [Arquitetura de IA: modelos grandes sem computador maior](ia/README.md) · [Hugging Face: o que usar e o que comprar](ia/hugging-face.md) · [Rede própria entre os seus computadores](rede/README.md) · [Custos: construir, abrir ou pagar](custos.md) · [Recursos: a melhor ferramenta para cada tarefa](recursos.md) · [Investimentos: as suas metodologias](investimentos.md) · [Certificações](certificacoes.md)")
    out.append("- [Marketing, vendas e automação](marketing/README.md): funil, canais sem rosto com voz clonada, publicação automática, tráfego, parcerias, internacional e medição de lucro")
    out.append("- [Editora AMS Silva](editora/README.md): estrutura legal, pipeline de produção dos livros, rigor editorial, identidade visual, avaliação, produtos, lançamento e roteiro")
    out.append("- [Implantação](implantacao/README.md): roteiro que cobre todos os blocos do setup, scripts que instalam e verificadores que conferem; pipeline de conteúdo e stack de automação")
    out.append("- [Operação do grupo](operacao/README.md): esteira de ofertas, portfólio pontuado, marca e presença, flywheel de conteúdo, automação, qualidade, clientes e ordem de execução")
    out.append("- [Negócios do grupo](negocios/README.md): os nove negócios em Barbacena, estrutura de CNPJs, ordem de abertura, números, cardápios e mínimo legal")
    out.append("- [Segurança](seguranca/README.md): engenharia reversa com IA, AppSec nos seus sistemas, empresa de pentest com guarda de escopo e relatório CVSS, e o Jarvis")
    out.append("- [Jarvis](jarvis/README.md): o setup e a casa por comando de voz: voz local, casa, câmeras, energia, água, robótica, PC e open source, com política de risco")
    out.append("- [Construção civil, arquitetura e engenharia civil](construcao/README.md): BIM aberto e Autodesk educacional, estudo e normas, regras da IA e as rendas pela TI")
    out.append("- [Vários computadores, SSD externo e NAS](infra/README.md): como crescer o setup para mais máquinas e armazenamento local e em nuvem")
    out.append("- [Boas práticas em todo repositório](boas-praticas.md): git, versões, tags, segurança, qualidade, backup e licenças")
    out.append("- [Painel do Núcleo](cockpit.html): a constelação do setup inteiro, o que já roda sozinho, principal e reserva, autonomia, roteiro e o que falta (abra no navegador)")
    out.append("- [Núcleo AMtech](nucleo/README.md): o setup conectado e autônomo, com banco central, garimpo de código, política de autonomia, agentes 24 horas e o teste do sistema inteiro")
    out.append("- [Empresa solo: o contexto mestre dentro do setup](empresa-solo.md): o que entrou, o que ficou de fora, as 88 ferramentas uma por uma, o cronograma de 14 dias reescrito e os comandos `just`")
    out.append("- [Decisões de arquitetura (ADRs)](adr/)")
    out.append("- Versões interativas, geradas dos mesmos dados: [`index.html`](index.html) (diagrama) e [`mapa.html`](mapa.html) (mapa do setup), para abrir no navegador\n")
    out.append("## Camadas\n")
    for c in eco["camadas"]:
        out.append(f"- [{num(eco, c['id']):02d} · {c['titulo']}](camadas/{arquivo_camada(eco, c['id'])}) ({len(por_camada[c['id']])} blocos)")
    return "\n".join(out) + "\n"


def gerar_readme(eco: dict, por_camada: dict) -> str:
    total_b = len(eco["blocos"])
    total_c = len(eco["conexoes"])
    contas = sum(1 for b in eco["blocos"] if b["conta"])
    out = ["<!-- Arquivo GERADO por tools/gerar_docs.py. Edite os dados em data/ ou o gerador. -->\n",
           "# dev-setup\n",
           "[![docs](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml/badge.svg)](https://github.com/AlanMateus17/dev-setup/actions/workflows/docs.yml)\n",
           "Arquitetura completa do meu ambiente de desenvolvimento e de trabalho: do hardware ao deploy na nuvem, da criação de conteúdo à venda de cursos. Cada ferramenta tem um motivo, um lugar e conexões definidas, e toda a documentação é gerada a partir de uma única fonte de dados.\n",
           f"| Camadas | Blocos | Conexões | Fluxos | Contas necessárias |\n|---|---|---|---|---|\n| {len(eco['camadas'])} | {total_b} | {total_c} | {len(eco['fluxos'])} | {contas} |\n",
           "## Por onde começar\n",
           "- **Continuar numa conversa nova com o Claude**: cole o [CONTINUAR.md](CONTINUAR.md) (ou `python3 tools/sessao/contexto.py --inicio | clip.exe`) e diga qual passo vai fazer. As decisões recentes ficam no [ESTADO.md](ESTADO.md).",
           "- **Comece aqui, no Windows**: extraia o zip, entre na pasta que tem `RODAR-DIAGNOSTICO.cmd` e clique com o botão direito nele > Executar como administrador. Ele só lê o notebook e diz por qual passo do roteiro começar.",
           "- **Montar tudo de uma vez**: `cd ~/dev/dev-setup && just instalar` (veja antes com `just instalar --simular`). O plano de autonomia está no [Núcleo AMtech](docs/nucleo/README.md).",
           "- **No Ubuntu, um comando só**: `cd ~/dev/dev-setup && just` lista tudo; `just check` antes de cada commit e `just triagem \"o que você quer\"` antes de construir algo novo. Ver [Empresa solo](docs/empresa-solo.md).",
           "- **[Arquitetura](docs/arquitetura.md)**: a pilha inteira, camada por camada, com o diagrama de cada uma.",
           "- **[Fluxos de ponta a ponta](docs/fluxos.md)**: codar com agente e publicar, vender um curso, publicar automaticamente, medir uma campanha e outros.",
           "- **[Editora AMS Silva](docs/editora/README.md)**: livros produzidos como software, com código testado, gabaritos conferidos e PDF, EPUB e impressão gerados da mesma fonte.",
           "- **[Implantação](docs/implantacao/README.md)**: do planejamento ao setup funcionando, com scripts de instalação, verificadores e o roteiro passo a passo.",
           "- **[Operação do grupo](docs/operacao/README.md)**: a esteira por onde passa toda oferta, o portfólio com " + str(len(json.loads((RAIZ / "data" / "portfolio.json").read_text(encoding="utf-8"))["ofertas"])) + " ofertas pontuadas e classificadas (arsenal de rendas), marca, conteúdo, automação, qualidade e a ordem de execução.",
           "- **[Negócios do grupo](docs/negocios/README.md)**: software, loja, robótica, ponto de retirada, entregas, delivery, sushi, cafeteria e padaria, com números, ordem de abertura e mínimo legal de cada um.",
           "- **[Marketing, vendas e automação](docs/marketing/README.md)**: funil, canais sem rosto com voz clonada, publicação no melhor horário, tráfego pago, parcerias, internacional e lucro por venda.",
           "- **[Segurança](docs/seguranca/README.md)**: engenharia reversa com IA, AppSec nos seus sistemas, o caminho até a AMtech Segurança (pentest com guarda de escopo e relatório CVSS) e o Jarvis.",
           "- **[Jarvis](docs/jarvis/README.md)**: comandos de voz para o PC, a casa (energia, água, câmeras, portas, janelas, eletrodomésticos) e os robôs, com política de risco.",
           "- **[Construção civil e arquitetura](docs/construcao/README.md)**: BIM aberto (Bonsai, FreeCAD), Autodesk educacional, SINAPI, regras da IA para engenharia e a automação BIM como renda.",
           "- **Diagrama interativo**: baixe [`docs/index.html`](docs/index.html) e abra no navegador. Toque em qualquer bloco para ver as conexões dele.",
           "- **[Toda a documentação](docs/README.md)**\n",
           "## A pilha\n",
           "```mermaid", "flowchart TB"]
    ids = [c["id"] for c in eco["camadas"]]
    for c in eco["camadas"]:
        out.append(f'  L_{c["id"]}["{num(eco, c["id"]):02d} · {mm(c["titulo"])}"]')
    for a, b in zip(ids, ids[1:]):
        out.append(f"  L_{a} --- L_{b}")
    out.append("  classDef cam fill:#e2ecec,stroke:#0e3a45,color:#13262b")
    out.append("  class " + ",".join(f"L_{i}" for i in ids) + " cam")
    out += ["```\n",
            "## A ideia em uma frase\n",
            "O Windows cuida só do que precisa de janela, GPU e segurança; todo o trabalho de engenharia roda em Linux (Ubuntu no WSL2), em containers, e sai para a nuvem por CI/CD. Agentes de IA trabalham dentro de uma sandbox que só enxerga a pasta do projeto.\n",
            "## Camadas\n",
            "| # | Camada | Blocos | Destaques |\n|---|---|---|---|"]
    for c in eco["camadas"]:
        bl = por_camada[c["id"]]
        destaque = ", ".join(nome(b) for b in bl[:4]) + ("…" if len(bl) > 4 else "")
        out.append(f"| {num(eco, c['id']):02d} | [{c['titulo']}](docs/camadas/{arquivo_camada(eco, c['id'])}) | {len(bl)} | {destaque} |")
    out += ["",
            "## Stack\n",
            "Sistemas AM: C#/.NET 10 · ASP.NET Core (Controllers) · Clean Architecture + DDD · PostgreSQL · Redis · SignalR · Next.js, TypeScript, Tailwind e Zod · Docker · GitHub Actions · Kamal. Fora deles, a melhor ferramenta para cada trabalho ([ADR 0007](docs/adr/0007-poliglota-por-funcao.md)): Astro para sites, SvelteKit e PocketBase para MVPs, Go para CLIs, Rust para firmware, Python para dados e IA. Principal e reserva de cada função no [ADR 0008](docs/adr/0008-trocas-de-ferramenta-principal.md).\n",
            "## Como este repositório funciona\n",
            "```mermaid", "flowchart LR",
            '  D["data/ecossistema.json<br/>data/mapa.json"] --> G["tools/gerar_docs.py"]',
            f'  G --> M["docs/*.md<br/>{len(eco["camadas"])} páginas de camada"]',
            '  G --> H["docs/index.html<br/>diagrama interativo"]',
            '  G --> R["README.md"]',
            '  CI["GitHub Actions"] -->|"valida e confere"| G',
            "```\n",
            "1. Tudo nasce em [`data/`](data): camadas, blocos, conexões, fluxos, contas e o plano.",
            "2. `python tools/gerar_docs.py` valida os dados (ids, conexões quebradas, rótulos) e regenera as páginas, o diagrama e este README.",
            "3. O GitHub Actions roda `python tools/gerar_docs.py --check` a cada push: se os dados tiverem erro ou os arquivos gerados estiverem desatualizados, o build falha.\n",
            "## Estrutura\n",
            "```",
            "data/                 fonte única: ecossistema, mapa, negócios, portfólio e implantação",
            "docs/",
            "  arquitetura.md      a pilha e as ligações entre camadas",
            "  camadas/            uma página por camada, com diagrama e conexões de cada bloco",
            "  fluxos.md           fluxos de ponta a ponta",
            "  marketing/          funil, IA, publicação, tráfego, canais, parcerias, internacional, lucro",
            "  infra/              vários computadores, SSD externo, NAS local e em nuvem",
            "  editora/            Editora AMS Silva: pipeline dos livros, rigor, produtos e lançamento",
            "  implantacao/        roteiro de implantação e acompanhamento (gerados)",
            "  operacao/           esteira, portfólio, marca, conteúdo, automação, qualidade, execução",
            "  negocios/           os nove negócios do grupo: estrutura, ordem, números, cardápios, licenças",
            "  seguranca/          engenharia reversa, AppSec e empresa de pentest",
            "  jarvis/             voz, casa, câmeras, energia, água, robótica e PC por comando de voz",
            "  construcao/         construção civil, arquitetura e engenharia civil pela TI",
            "  contas.md, auditoria.md, nuvem.md, roteiro.md, ...",
            "  adr/                decisões de arquitetura",
            "  index.html          diagrama interativo (gerado)",
            "  mapa.html           sistemas, nuvens, pilha, mercado e ordem de estudo (gerado)",
            "scripts/windows/      instalar.ps1, verificar.ps1, extensões do VS Code e o inventário do Windows",
            "scripts/wsl/          bootstrap.sh, nuvem.sh, verificar.sh e ativar-pipeline.sh",
            "infra/automacao/      n8n, banco de métricas, Grafana e Uptime Kuma (Docker Compose)",
            "infra/lab-seguranca/  laboratório de ataque local (Juice Shop, WebGoat) presos em 127.0.0.1",
            "infra/lab-alvo/       alvo isolado sem internet: o software que você estudou contra o atacante",
            "infra/jarvis/         voz local (Whisper, Piper, openWakeWord), MQTT, Zigbee2MQTT e Frigate",
            "config/marca.md       guia de marca usado pelo pipeline de conteúdo",
            "infra/templates/     repositório padrão, deploy com Kamal, esteira de sites, regras da IA e segurança",
            "tools/                geradores, motor financeiro, pipeline de conteúdo e templates",
            "justfile              porta única de comandos (check, triagem, arquiteto, docs, ci-local)",
            "```\n",
            "## Status\n",
            "Em construção por fases. A fase 1 (Windows, WSL2, Docker e .NET) está em andamento; o restante segue o [roteiro de estudo](docs/roteiro.md).\n",
            "## Licença\n",
            "[MIT](LICENSE)\n"]
    return "\n".join(out)


def gerar_html(eco: dict) -> str:
    tpl = TEMPLATE_HTML.read_text(encoding="utf-8")
    dados = json.dumps(eco, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return tpl.replace("__DATA__", dados)


def gerar_mapa_html(eco: dict, mapa: dict) -> str:
    tpl = TEMPLATE_MAPA.read_text(encoding="utf-8")
    eco_min = {k: eco[k] for k in ("camadas", "blocos", "conexoes", "fluxos")}
    dados = json.dumps({"eco": eco_min, "mapa": mapa}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return tpl.replace("__DATA__", dados)


# ---------------------------------------------------------------- principal

def quando_no_roteiro() -> dict[str, str]:
    """'6.7 · Semanas 3 e 4 · nov/2026' para cada bloco, a partir de data/implantacao.json."""
    arq = DADOS / "implantacao.json"
    if not arq.exists():
        return {}
    im = json.loads(arq.read_text(encoding="utf-8"))
    out: dict[str, list[str]] = defaultdict(list)
    for i, f in enumerate(im["fases"]):
        for j, p in enumerate(f["passos"], 1):
            for b in p.get("blocos", []):
                q = f.get("quando", "")
                if f.get("gatilho"):
                    q += f" (começa quando: {f['gatilho'][0].lower() + f['gatilho'][1:]})"
                out[b].append(f"passo {i}.{j} · {q}")
    return {b: "; ".join(dict.fromkeys(v)) for b, v in out.items()}


def gerar_tudo(eco: dict, mapa: dict) -> dict[Path, str]:
    qr = quando_no_roteiro()
    eco = {**eco, "blocos": [{**b, "quando": qr.get(b["id"], "")} for b in eco["blocos"]]}
    por_id = {b["id"]: b for b in eco["blocos"]}
    por_camada: dict[str, list] = defaultdict(list)
    for b in eco["blocos"]:
        por_camada[b["camada"]].append(b)
    saidas: dict[str, list] = defaultdict(list)
    entradas: dict[str, list] = defaultdict(list)
    for c in eco["conexoes"]:
        saidas[c["de"]].append(c)
        entradas[c["para"]].append(c)

    arquivos: dict[Path, str] = {}
    for camada in eco["camadas"]:
        arquivos[DOCS / "camadas" / arquivo_camada(eco, camada["id"])] = gerar_camada(eco, camada, por_id, saidas, entradas)
    arquivos[DOCS / "arquitetura.md"] = gerar_arquitetura(eco, por_camada)
    arquivos[DOCS / "fluxos.md"] = gerar_fluxos(eco, por_id)
    arquivos[DOCS / "contas.md"] = gerar_lista("Contas e conexões", "Contas que o setup exige. Senhas no KeePassXC, 2FA no app autenticador e códigos de recuperação impressos.", eco["contas"])
    arquivos[DOCS / "auditoria.md"] = gerar_lista("Auditoria: o que faltava", "Itens adicionados na revisão de 20/10/2026, por urgência.", eco["auditoria"])
    for nome_arq, texto in gerar_planejamento(mapa).items():
        arquivos[DOCS / nome_arq] = texto
    arquivos[DOCS / "README.md"] = gerar_indice_docs(eco, por_camada)
    arquivos[RAIZ / "README.md"] = gerar_readme(eco, por_camada)
    arquivos[DOCS / "index.html"] = gerar_html(eco)
    arquivos[DOCS / "mapa.html"] = gerar_mapa_html(eco, mapa)
    return arquivos


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true", help="não escreve; falha se algo estiver desatualizado")
    args = ap.parse_args()

    eco, mapa = carregar()
    erros = validar(eco)
    if erros:
        print("Erros nos dados:", *erros, sep="\n  ")
        return 1

    arquivos = gerar_tudo(eco, mapa)
    desatualizados = []
    for caminho, texto in arquivos.items():
        atual = caminho.read_text(encoding="utf-8") if caminho.exists() else None
        if atual != texto:
            desatualizados.append(caminho.relative_to(RAIZ))
            if not args.check:
                caminho.parent.mkdir(parents=True, exist_ok=True)
                caminho.write_text(texto, encoding="utf-8")

    pasta = DOCS / "camadas"
    sobrando = [f for f in pasta.glob("*.md") if f not in arquivos]
    for f in sobrando:
        desatualizados.append(f.relative_to(RAIZ))
        if not args.check:
            f.unlink()

    sem_conexao = [b["id"] for b in eco["blocos"]
                   if not any(c["de"] == b["id"] or c["para"] == b["id"] for c in eco["conexoes"])]
    print(f"{len(eco['camadas'])} camadas, {len(eco['blocos'])} blocos, {len(eco['conexoes'])} conexões, {len(eco['fluxos'])} fluxos.")
    if sem_conexao:
        print(f"Aviso: {len(sem_conexao)} bloco(s) sem conexão: {', '.join(sem_conexao)}")
    if args.check:
        if desatualizados:
            print("Arquivos gerados desatualizados. Rode: python tools/gerar_docs.py", *desatualizados, sep="\n  ")
            return 1
        print("Tudo em dia.")
    else:
        print(f"{len(desatualizados)} arquivo(s) atualizado(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
