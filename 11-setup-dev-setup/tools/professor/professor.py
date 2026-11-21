#!/usr/bin/env python3
"""O Professor do setup: aula, prática, prova e revisão espaçada de cada tópico de que você precisa para operar o setup e
subir no eixo (software e finanças).

O método completo está em docs/professor/metodo.md: as técnicas da ciência cognitiva (recuperação, espaçamento,
intercalação, dificuldade desejável, exemplos resolvidos, prática deliberada, Feynman) somadas ao que o Alan já tinha
decidido nos planos dele (Protocolo de fim de bloco, loop da mesma ideia de 4 jeitos, ficha dupla, registro de
entrevista, exercícios N1 a N4 do padrão do livro, 20/80, uma porta só). Domínio vai de 0 a 4: nada, viu a aula, fez a
prática, passou na prova, ensinou.

As aulas ficam no seu vault (~/dev/notas/07-estudo-e-carreira/professor) e são geradas uma vez só: reler não gasta token.
Quando o assunto do módulo já está escrito e conferido no mapa-de-estudo (📘), a aula É o arquivo do mapa: o Professor
abre esse arquivo em vez de pedir texto novo à IA (use --gerar só se quiser uma aula extra).

A ordem vem do mapa-de-estudo (ADR 0018): um módulo só é liberado quando o assunto dele está escrito e conferido e todos
os assuntos de que ele depende no mapa (direta ou indiretamente) já passaram na prova. O dia da semana só filtra as
trilhas; quando nenhuma trilha do dia tem módulo liberado, o `hoje` mostra o próximo da fila do mapa.

    python3 tools/professor/professor.py hoje                 # o que estudar hoje (revisões + próxima aula de cada trilha)
    python3 tools/professor/professor.py trilha               # o currículo com o seu nível em cada módulo
    python3 tools/professor/professor.py aula s-backup [--motor claude|ollama|imprimir] [--refazer] [--gerar]
    python3 tools/professor/professor.py ferramenta restic    # mini-aula sobre qualquer bloco do ecossistema
    python3 tools/professor/professor.py praticei s-backup    # nível 2
    python3 tools/professor/professor.py prova s-backup       # gera a prova; você responde no próprio arquivo
    python3 tools/professor/professor.py corrigir s-backup    # a IA corrige com rubrica, marca o nível e agenda a revisão
    python3 tools/professor/professor.py nota b-aprender 85   # sem IA: a nota que você tirou no gabarito do arquivo do mapa
    python3 tools/professor/professor.py ensinei s-backup     # nível 4: escreveu post ou deu a aula
    python3 tools/professor/professor.py fechar s-backup 80   # Protocolo de fim de bloco: ficha dupla, registro de entrevista, tempo real
    python3 tools/professor/professor.py escutei "Hipsters: carreira" "ideia 1; ideia 2; ideia 3" --acao "..."  # podcast vira nota
    python3 tools/professor/professor.py cartoes              # exporta todos os cartões para importar no Anki
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import nucleo as nuc  # noqa: E402

CURRICULO = RAIZ / "data" / "professor" / "curriculo.json"
RETRATO = RAIZ / "data" / "professor" / "mapa-assuntos.json"
# ids antigos (da época do C#) → ids novos; o progresso salvo é migrado na primeira execução
RENOMEADOS = {"o-csharp": "o-typescript", "o-dotnet": "o-ts-projeto"}
CONTEXTO = RAIZ / "docs" / "akita" / "contexto-setup.md"
INTERVALOS = (1, 3, 7, 21, 60, 120)
APROVA = 80
TRILHAS = {"oficio": "Ofício (âncora 6h-8h)", "setup": "Operar o setup (dentro do ofício)",
           "financas": "Domínio: finanças (bloco de quinta)", "matematica": "Matemática VHSlins (sexta de manhã)",
           "fisica": "Física (sábado)", "base": "Base do Akita (terça, 6h-7h)"}
# A semana fixa, sobre os horários reais (vault: 07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md, Parte 1):
# segunda e quarta âncora técnica; terça só o slot curto de leitura (base do Akita); quinta o bloco profundo;
# sexta matemática; sábado ofício leve + física; domingo é folga (só a revisão do Anki).
SEMANA = {0: ("oficio", "setup"), 1: ("base",), 2: ("oficio", "setup"),
          3: ("oficio", "setup", "financas"), 4: ("matematica",), 5: ("oficio", "fisica"), 6: ()}


def trilhas_do_dia(dia: date | None = None) -> tuple[str, ...]:
    return SEMANA[(dia or date.today()).weekday()]


AKITA_INDICE = RAIZ / "data" / "akita" / "indice.json"


def posts_akita(m: dict, limite: int = 2) -> list[dict]:
    """Os posts do Akita que mais combinam com o módulo (palavras do campo `akita` no título e nas tags), os mais
    recentes primeiro; opinião e histórico da era Rails ficam de fora."""
    if not AKITA_INDICE.exists():
        return []
    indice = json.loads(AKITA_INDICE.read_text(encoding="utf-8"))
    if m.get("akita_posts"):  # escolhidos a dedo para o módulo
        por_slug = {p["slug"]: p for p in indice}
        return [por_slug[s] for s in m["akita_posts"] if s in por_slug][:limite]
    chaves = [c.lower() for c in m.get("akita", [])]
    if not chaves:
        return []
    achados = []
    for p in indice:
        if p["categoria"] in ("opiniao", "historico"):
            continue
        alvo = (p["titulo"] + " " + " ".join(p["tags"])).lower()
        pontos = sum(1 for c in chaves if c in alvo)
        if pontos:
            achados.append((pontos, p["data"], p))
    achados.sort(key=lambda x: (x[0], x[1]), reverse=True)
    return [p for _, _, p in achados[:limite]]


def entrada(m: dict) -> list[str]:
    """O que assistir e ler ANTES da aula: o curso da Alura, o trecho do livro e os posts do Akita.
    A aula não resume nenhum deles."""
    linhas = [f"assistir: {a['titulo']} ({a['plataforma']})" for a in m.get("assistir", [])]
    linhas += [f"ler: {l['obra']}, {l['trecho']}" for l in m.get("ler", [])]
    linhas += [f"ler (Akita): {p['titulo']} · {p['url']}" for p in posts_akita(m)]
    return linhas


def vault() -> Path:
    return Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")


def pasta() -> Path:
    """Aulas, provas e cartões ficam no seu vault, ao lado do resto do estudo (07-estudo-e-carreira)."""
    return Path(os.environ.get("PROFESSOR_NOTAS") or vault() / "07-estudo-e-carreira" / "professor")


def pasta_fichas() -> Path:
    """Ficha dupla e registro de entrevista vão para a pasta de produção simultânea que o vault já tinha."""
    return Path(os.environ.get("PROFESSOR_FICHAS") or vault() / "09-material-producao-simultanea" / "fichas-duplas")


def etapa_do_modulo(mid: str) -> str | None:
    """A etapa do mapa-de-estudo ligada a este módulo em data/aulas.json (ADR 0021), se houver."""
    arq = RAIZ / "data" / "aulas.json"
    if not arq.exists():
        return None
    etapas = json.loads(arq.read_text(encoding="utf-8")).get("etapas", {})
    return next((e for e, info in etapas.items() if info.get("professor") == mid), None)


def curriculo() -> dict:
    return json.loads(CURRICULO.read_text(encoding="utf-8"))


def assuntos_mapa() -> dict[str, dict]:
    """O retrato do MAPA.md (tools/professor/mapa.py atualizar), na ordem do mapa. Vazio se ainda não existir."""
    if not RETRATO.exists():
        return {}
    return json.loads(RETRATO.read_text(encoding="utf-8")).get("assuntos", {})


def pasta_mapa() -> Path:
    return Path(os.environ.get("AMTECH_MAPA") or Path.home() / "dev" / "mapa-de-estudo")


def migrar_ids(con) -> None:
    """Leva o progresso dos ids antigos (o-csharp, o-dotnet) para os novos, sem apagar nada que já exista no novo."""
    for velho, novo in RENOMEADOS.items():
        con.execute("UPDATE dominio SET topico = ? WHERE topico = ? AND NOT EXISTS (SELECT 1 FROM dominio WHERE topico = ?)",
                    (novo, velho, novo))
        for sub in ("aulas", "provas"):
            for arq in (pasta() / sub).glob(f"{velho}*.md") if (pasta() / sub).exists() else []:
                alvo = arq.with_name(arq.name.replace(velho, novo, 1))
                if not alvo.exists():
                    arq.rename(alvo)
    con.commit()


def modulo(mid: str) -> dict:
    mid = RENOMEADOS.get(mid, mid)
    for m in curriculo()["modulos"]:
        if m["id"] == mid:
            return m
    raise ValueError(f"módulo {mid} não existe (veja: just professor trilha)")


# ---------- domínio e revisão espaçada ----------

def niveis(con) -> dict[str, dict]:
    return {r["topico"]: dict(r) for r in con.execute("SELECT * FROM dominio")}


def subir(con, topico: str, nivel: int) -> None:
    """Sobe o nível (nunca desce por aqui)."""
    con.execute("INSERT INTO dominio (topico, nivel) VALUES (?, ?) ON CONFLICT(topico) DO UPDATE SET "
                "nivel = max(nivel, excluded.nivel), atualizado = strftime('%Y-%m-%dT%H:%M:%S','now','localtime')",
                (topico, nivel))
    con.commit()


def registrar_prova(con, topico: str, nota: int, hoje: date | None = None) -> tuple[int, str]:
    """Aprovado: nível 3 e o próximo intervalo da escada. Reprovado: volta para 1 dia (o nível não sobe)."""
    hoje = hoje or date.today()
    atual = niveis(con).get(topico, {"intervalo_dias": 0, "nivel": 0})
    if nota >= APROVA:
        maiores = [i for i in INTERVALOS if i > atual["intervalo_dias"]]
        intervalo = maiores[0] if maiores else INTERVALOS[-1]
        nivel = max(3, atual["nivel"])
    else:
        intervalo, nivel = 1, min(atual["nivel"], 2)
    prox = (hoje + timedelta(days=intervalo)).isoformat()
    con.execute("INSERT INTO dominio (topico, nivel, ultima_nota, intervalo_dias, proxima_revisao) VALUES (?,?,?,?,?) "
                "ON CONFLICT(topico) DO UPDATE SET nivel=excluded.nivel, ultima_nota=excluded.ultima_nota, "
                "intervalo_dias=excluded.intervalo_dias, proxima_revisao=excluded.proxima_revisao, "
                "atualizado=strftime('%Y-%m-%dT%H:%M:%S','now','localtime')", (topico, nivel, nota, intervalo, prox))
    con.commit()
    return intervalo, prox


def _fecho(assuntos: dict[str, dict]) -> dict[str, set[str]]:
    """Para cada assunto do mapa, todos os assuntos de que ele depende, direta ou indiretamente."""
    memo: dict[str, set[str]] = {}

    def visita(a, pilha=()):
        if a in memo:
            return memo[a]
        if a in pilha:
            return set()
        tudo: set[str] = set()
        for d in assuntos.get(a, {}).get("depende", []):
            tudo |= {d} | visita(d, pilha + (a,))
        memo[a] = tudo
        return tudo
    for a in assuntos:
        visita(a)
    return memo


def bloqueio(m: dict, mods: list[dict], nv: dict[str, dict], assuntos: dict[str, dict],
             dep: dict[str, set[str]] | None = None) -> str | None:
    """Por que o módulo ainda não pode ser estudado (None = liberado).
    1) pré-requisitos do próprio módulo; 2) com o retrato do mapa: o assunto precisa estar escrito e conferido (📘),
    todo assunto de que ele depende no mapa também, e os módulos desses assuntos precisam ter passado na prova."""
    dom = lambda mid: nv.get(mid, {}).get("nivel", 0) >= 3  # noqa: E731
    falta = [p for p in m.get("prereq", []) if not dom(p)]
    if falta:
        return "falta passar na prova de " + ", ".join(falta)
    etapa = m.get("etapa")
    if not assuntos or etapa is None or etapa not in assuntos:
        return None
    if not assuntos[etapa].get("escrito"):
        return f"o assunto {etapa} ainda não foi escrito e conferido no mapa"
    dep = dep if dep is not None else _fecho(assuntos)
    nao_escritos = sorted(p for p in dep.get(etapa, set()) if not assuntos.get(p, {}).get("escrito"))
    if nao_escritos:
        return "o mapa pede antes: " + ", ".join(nao_escritos) + " (ainda não escritos)"
    pendentes = sorted(x["id"] for x in mods if x.get("etapa") in dep.get(etapa, set()) and not dom(x["id"]))
    if pendentes:
        return "o mapa pede antes: " + ", ".join(pendentes)
    return None


def plano_do_dia(mods: list[dict], nv: dict[str, dict], hoje: date | None = None,
                 assuntos: dict[str, dict] | None = None) -> dict:
    """Revisões vencidas; por trilha, o primeiro módulo liberado (ordem do mapa); a fila do mapa (todos os liberados,
    em qualquer trilha) e os próximos assuntos do mapa que precisam ser escritos antes de entrar."""
    hoje = (hoje or date.today()).isoformat()
    assuntos = assuntos or {}
    revisoes = sorted(t for t, r in nv.items() if r.get("proxima_revisao") and r["proxima_revisao"] <= hoje)
    ordem = {a: i for i, a in enumerate(assuntos)}
    dep = _fecho(assuntos) if assuntos else {}
    chave = lambda m: (m["trimestre"], ordem.get(m.get("etapa"), len(ordem)))  # noqa: E731
    proximos, fila = {}, []
    for m in sorted(mods, key=chave):
        if nv.get(m["id"], {}).get("nivel", 0) >= 3 or bloqueio(m, mods, nv, assuntos, dep):
            continue
        fila.append(m)
        proximos.setdefault(m["trilha"], m)
    a_escrever = [a for a, info in assuntos.items() if not info.get("escrito")
                  and all(assuntos.get(d, {}).get("escrito") for d in info.get("depende", []))][:3]
    return {"revisoes": revisoes, "proximos": proximos, "fila": fila, "a_escrever": a_escrever}


# ---------- pedidos à IA ----------

AULA = """Você é o professor particular do Alan: muito experiente, detalhista e didático. Ele é professor de TI,
dev em formação rumo a sênior (eixo: software e finanças) e tem TDAH. Escreva UMA aula em português do Brasil, em
Markdown, sobre o módulo abaixo. O método (docs/professor/metodo.md) é fixo; siga exatamente esta estrutura:

# {titulo}
> Profundidade: {profundidade} ("usar" = saber aplicar com segurança; "a fundo" = entender o porquê e os limites).
## Antes desta aula (ele já assistiu ou leu: {entrada}). Não resuma o curso nem o livro: comece com 3 perguntas
   sobre o que ele viu lá e diga o que esta aula acrescenta (o setup dele, a prática, os exercícios, o porquê)
## Por que isso importa (abra pela motivação, não pela definição: onde isso aparece no setup ou num sistema real dele)
## Objetivo (uma frase verificável)
## Antes de começar (3 perguntas diagnósticas, sem resposta: ele responde de cabeça antes de ler)
## Bloco 1 (25 min) · Intuição: uma analogia do dia a dia dele (escola, restaurante, a casa)
## Bloco 2 (25 min) · O modelo: como funciona por dentro, com um diagrama em texto ou Mermaid; 3 a 5 exemplos
   resolvidos embutidos na explicação; um quadro "> **Pare e responda:**" no meio
## Bloco 3 (25 min) · Os detalhes que pegam: casos de borda e diagnóstico, com quadros "> **Erro comum:**"
## A mesma ideia de 4 jeitos (quando fizer sentido): a ideia pura (matemática ou conceito) → em TypeScript → em Python →
   no sistema real (AM Gestão, o próprio setup). Se não fizer sentido para o tema, diga e pule.
## Exemplo resolvido completo (passo a passo, explicando cada decisão)
## Agora você tenta (o mesmo tipo de exemplo com lacunas ___)
## Exercícios em 4 níveis (N1 reconhecimento; N2 aplicação direta; N3 aplicação combinada e "encontre o erro";
   N4 desafio ou mini-projeto real), 3 a 4 por nível
## Prática no seu setup (comandos de UMA linha, dizendo ONDE rodar: Ubuntu do WSL ou PowerShell; nada destrutivo
   sem cópia antes; critério de pronto verificável)
## Perguntas de recuperação (5, de lembrar a aplicar)
## Gabarito comentado (exercícios e perguntas, num bloco recolhido <details>, explicando o porquê de cada resposta)
## Cartões (8 linhas no formato "- pergunta :: resposta", curtas, uma ideia cada, conceito e não só termo)
## Como você ensinaria isso (ele também quer dar esta aula): roteiro de quadro para 50 min, com o que escrever no
   quadro, a analogia, a pergunta para a turma, o erro que os alunos mais cometem e uma atividade sem gabarito
## Fechamento do bloco (lembre o Protocolo: fechar o material, reconstruir de cabeça, explicar em 3 a 5 frases sem
   jargão, cartões, tempo real; rodar: just professor fechar {id} MINUTOS)
## Se quiser ir além (as fontes oficiais abaixo, dizendo o que ler em cada uma)

Regras: explique com as suas palavras; nada copiado de curso pago ou livro; quando não tiver certeza de um detalhe,
diga "confira na fonte oficial" em vez de inventar; aplique tudo ao setup dele (contexto abaixo); 20/80: o que resolve
a maior parte dos casos vem primeiro e marcado; fundamentos antes de framework; nada de dado de aluno, senha ou
documento pessoal nos exemplos.

MÓDULO: {titulo}
Objetivos: {objetivos}
Prática pedida: {pratica}
Fontes oficiais: {fontes}

O SETUP DELE:
{contexto}

O QUE O SETUP JÁ SABE SOBRE O ASSUNTO (decisões, regras do Akita aprovadas, lições):
{nucleo}
"""

FICHA = """# Ficha dupla · {titulo}

1. **A ideia** (pura, sem código): definição com as suas palavras + um exemplo + um exercício
2. **A mesma ideia, em código**: o trecho + por que é a MESMA coisa + um exercício
3. **Por que importa**: onde aparece num sistema real (AM Gestão, o setup) + a motivação em uma frase
4. **Conexão com o próximo tópico**: uma linha

---

# Registro de entrevista · {titulo}

- **Contexto:** o que precisava ser resolvido, em qual sistema
- **Decisão:** o que escolheu, a alternativa descartada e por quê
- **Resultado:** o que aconteceu, com número real se tiver
- **Pergunta que responde:** a pergunta de entrevista que este registro cobre
"""

PROTOCOLO = """Protocolo de fim de bloco ({titulo}):
  1. FECHE o material.
  2. RECONSTRUA de cabeça: o que o bloco resolveu e por quê.
  3. ENSINE em 3 a 5 frases sem jargão: preencha a ficha dupla e o registro de entrevista em {ficha}
  4. ANKI: 1 a 3 cartões de conceito (just professor cartoes junta os da aula).
  5. TEMPO: {minutos} min reais contra {estimado} min estimados.
  6. Só então avance: just professor praticei {id} (se fez a prática) e a prova: just professor prova {id}
     (corrigida pela IA) ou, sem IA, os exercícios e o gabarito do arquivo do mapa e just professor nota {id} NOTA."""

PROVA = """Monte uma prova em português do Brasil sobre o módulo "{titulo}" (objetivos: {objetivos}). 8 questões: 3 de
explicar com as próprias palavras, 3 de aplicar no setup dele (comando ou decisão), 2 de diagnosticar um erro. Nada de
múltipla escolha. Depois de cada questão deixe a linha "Resposta:" vazia. Não dê as respostas. Só a prova, em Markdown."""

CORRECAO = """Corrija a prova abaixo como um professor exigente e justo. Para cada questão: certo, parcial ou errado,
e o porquê em uma ou duas frases, com a correção. No fim, uma linha só com o JSON {{"nota": 0 a 100, "revisar": ["tópico
fraco", ...]}}. Módulo: "{titulo}". Objetivos: {objetivos}.

{prova}"""


def pedido_aula(m: dict, contexto_nucleo: str = "") -> str:
    ctx = CONTEXTO.read_text(encoding="utf-8") if CONTEXTO.exists() else ""
    ent = "; ".join(entrada(m)) or "nada antes; a aula é a primeira exposição"
    return (AULA.replace("{entrada}", ent).replace("{titulo}", m["titulo"]).replace("{id}", m["id"])
            .replace("{profundidade}", "a fundo" if m.get("profundidade") == "a-fundo" else "usar").replace("{objetivos}", "; ".join(m["objetivos"]))
            .replace("{pratica}", m["pratica"]).replace("{fontes}", ", ".join(m["fontes"]))
            .replace("{contexto}", ctx).replace("{nucleo}", contexto_nucleo or "(nada ainda)"))


class MotorAusente(ValueError):
    """O programa do motor (claude ou ollama) não está instalado neste Linux."""


def rodar(motor: str, pedido: str) -> str:
    if motor == "imprimir":
        return pedido
    cmd = {"claude": ["claude", "-p", "--output-format", "text"],
           "ollama": ["ollama", "run", os.environ.get("PROFESSOR_MODELO", "qwen2.5:7b")]}.get(motor)
    if not cmd:
        raise ValueError("motor: claude, ollama ou imprimir")
    try:
        return subprocess.run(cmd, input=pedido, capture_output=True, text=True, check=True, timeout=1800).stdout
    except FileNotFoundError:
        raise MotorAusente(f"O motor '{motor}' não está instalado neste Linux (o comando '{cmd[0]}' não existe). "
                           f"Use --motor imprimir (mostra o pedido para colar numa conversa) ou --motor ollama, "
                           f"ou instale o Claude Code no Ubuntu e faça login.") from None
    except subprocess.CalledProcessError as erro:
        detalhe = (erro.stderr or erro.stdout or "").strip()[-400:] or "sem mensagem"
        raise ValueError(f"O motor '{motor}' falhou (código {erro.returncode}): {detalhe}. "
                         f"Confira o login (claude) ou o modelo (ollama list), ou use --motor imprimir.") from None


def cartoes_de(texto: str) -> list[tuple[str, str]]:
    """Linhas '- pergunta :: resposta' da seção Cartões."""
    i = texto.find("## Cartões")
    if i < 0:
        return []
    saida = []
    for ln in texto[i:].splitlines()[1:]:
        if ln.startswith("## "):
            break
        m = re.match(r"^\s*[-*]\s*(.+?)\s*::\s*(.+)$", ln)
        if m:
            saida.append((m.group(1), m.group(2)))
    return saida


def fracos_da_correcao(texto: str) -> list[str]:
    achado = re.findall(r"\{[^{}]*\"nota\"[^{}]*\}", texto)
    try:
        return [str(x) for x in json.loads(achado[-1]).get("revisar", [])] if achado else []
    except json.JSONDecodeError:
        return []


def pontos_fracos(con) -> dict[str, list[str]]:
    """O que a última correção de cada módulo mandou revisar: é ali que vai a prática deliberada."""
    saida: dict[str, list[str]] = {}
    for r in con.execute("SELECT dados FROM eventos WHERE tipo = 'professor.prova' ORDER BY id"):
        d = json.loads(r["dados"])
        saida[d["modulo"]] = d.get("revisar", []) if d.get("nota", 0) < 100 else []
    return {k: v for k, v in saida.items() if v}


def nota_da_correcao(texto: str) -> int:
    achado = re.findall(r"\{[^{}]*\"nota\"\s*:\s*(\d{1,3})[^{}]*\}", texto)
    if not achado:
        raise ValueError("a correção não trouxe a nota em JSON")
    return max(0, min(100, int(achado[-1])))


# ---------- CLI ----------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("hoje")
    s.add_parser("trilha")
    a = s.add_parser("aula"); a.add_argument("id"); a.add_argument("--motor", default="claude"); a.add_argument("--refazer", action="store_true")
    a.add_argument("--gerar", action="store_true", help="gera uma aula por IA mesmo com o arquivo do mapa pronto")
    f = s.add_parser("ferramenta"); f.add_argument("bloco"); f.add_argument("--motor", default="claude")
    for nome in ("praticei", "ensinei"):
        s.add_parser(nome).add_argument("id")
    p = s.add_parser("prova"); p.add_argument("id"); p.add_argument("--motor", default="claude")
    c = s.add_parser("corrigir"); c.add_argument("id"); c.add_argument("--motor", default="claude")
    n = s.add_parser("nota"); n.add_argument("id"); n.add_argument("valor", type=int)
    s.add_parser("cartoes")
    z = s.add_parser("fechar"); z.add_argument("id"); z.add_argument("minutos", type=int)
    y = s.add_parser("escutei"); y.add_argument("titulo"); y.add_argument("ideias"); y.add_argument("--acao", default="")
    args = ap.parse_args(argv)
    con = nuc.abrir()
    try:
        migrar_ids(con)
        cur = curriculo()
        assuntos = assuntos_mapa()
        if args.cmd == "hoje":
            pl = plano_do_dia(cur["modulos"], niveis(con), assuntos=assuntos)
            if pl["revisoes"]:
                print("Revisar primeiro (prova curta de novo): " + ", ".join(pl["revisoes"]))
            hoje_trilhas = trilhas_do_dia()
            if not hoje_trilhas:
                print("Domingo é folga. O descanso faz parte do plano.")

            def mostrar(m, rotulo):
                etapa = m.get("etapa")
                info = assuntos.get(etapa, {}) if etapa else {}
                print(f"{rotulo}: {m['id']} · {m['titulo']}" + (f"  (mapa {etapa})" if etapa else ""))
                for ln in entrada(m):
                    print(f"   antes, {ln}")
                if info.get("escrito"):
                    print(f"   estude pelo arquivo do mapa: {pasta_mapa() / info['arquivo']}  (just professor aula {m['id']} abre)")
                else:
                    print(f"   depois: just professor aula {m['id']}")
            mostrados = set()
            for trilha in hoje_trilhas:
                m = pl["proximos"].get(trilha)
                if m:
                    mostrar(m, TRILHAS[trilha])
                    mostrados.add(m["id"])
            if hoje_trilhas:
                extra = next((m for m in pl["fila"] if m["id"] not in mostrados and m.get("etapa")), None)
                if extra:
                    mostrar(extra, "Próximo da fila do mapa (fora das trilhas de hoje)")
            for mid, fracos in pontos_fracos(con).items():
                print(f"Prática deliberada em {mid}: {', '.join(fracos)}")
            if pl["a_escrever"]:
                nomes = ", ".join(f"{a} {assuntos[a]['titulo']}" for a in pl["a_escrever"])
                print(f"Próximos assuntos do mapa a escrever e conferir antes de entrar: {nomes}")
            if not pl["fila"] and not pl["revisoes"] and not pl["a_escrever"]:
                print("Currículo do trimestre dominado. Hora de acrescentar módulos (data/professor/curriculo.json).")
        elif args.cmd == "trilha":
            nv, nomes = niveis(con), cur["niveis"]
            for m in sorted(cur["modulos"], key=lambda m: (m["trimestre"], m["trilha"])):
                n = nv.get(m["id"], {}).get("nivel", 0)
                print(f"T{m['trimestre']} {m['trilha']:<10} {'●' * n}{'○' * (4 - n)} {m['id']:<20} {m['titulo']}  ({nomes[n]})")
        elif args.cmd in ("aula", "ferramenta"):
            if args.cmd == "ferramenta":
                eco = json.loads((RAIZ / "data" / "ecossistema.json").read_text(encoding="utf-8"))
                b = next((x for x in eco["blocos"] if x["id"] == args.bloco), None)
                if not b:
                    raise ValueError(f"bloco {args.bloco} não existe no ecossistema")
                m = {"id": f"ferramenta-{b['id']}", "titulo": f"Conhecer: {b['rotulo'].replace('|', ' ')}",
                     "objetivos": [b["descricao"], "saber quando usar e quando não usar", "usar o básico no setup"],
                     "pratica": "o primeiro uso real dessa ferramenta no setup dele", "fontes": ["a documentação oficial da ferramenta"]}
                refazer = False
            else:
                m, refazer = modulo(args.id), args.refazer
                motivo = bloqueio(m, cur["modulos"], niveis(con), assuntos)
                if motivo:
                    print(f"Aviso: {m['id']} ainda não está liberado ({motivo}). Siga o just professor hoje.", file=sys.stderr)
            info = assuntos.get(m.get("etapa") or "", {})
            destino = pasta() / "aulas" / f"{m['id']}.md"
            if args.cmd == "aula" and info.get("escrito") and not args.gerar:
                arq = pasta_mapa() / info["arquivo"]
                print(f"A aula deste módulo é o arquivo conferido do mapa ({m['etapa']} {info['titulo']}):\n  {arq}")
                if not arq.exists():
                    print("  O mapa-de-estudo não está nesse caminho. No Ubuntu: "
                          "git clone https://github.com/AlanMateus17/mapa-de-estudo.git ~/dev/mapa-de-estudo")
                print("  Comece pela seção 0 (diagnóstico). Quer uma aula extra gerada por IA? Use --gerar.")
            elif destino.exists() and not refazer:
                print(f"A aula já existe (reler não gasta token): {destino}")
            else:
                pedido = pedido_aula(m, nuc.contexto(con, m["titulo"], excluir=("referencia",)))
                try:
                    texto = rodar(args.motor, pedido)
                except MotorAusente as erro:
                    print(f"{erro}\nMostrando o pedido (motor imprimir):\n", file=sys.stderr)
                    args.motor, texto = "imprimir", pedido
                if args.motor == "imprimir":
                    print(texto)
                    return 0
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_text(texto, encoding="utf-8")
                print(f"Aula salva: {destino}")
            subir(con, m["id"], 1)
            nuc.evento(con, "professor.aula", {"modulo": m["id"]}, fonte="professor")
        elif args.cmd == "praticei":
            modulo(args.id); subir(con, args.id, 2); print(f"{args.id}: nível 2 (fez a prática). Próximo: just professor prova {args.id}")
        elif args.cmd == "ensinei":
            modulo(args.id); subir(con, args.id, 4); print(f"{args.id}: nível 4 (ensinou). É assim que o assunto fica de vez.")
        elif args.cmd == "prova":
            m = modulo(args.id)
            motivo = bloqueio(m, cur["modulos"], niveis(con), assuntos)
            if motivo:
                print(f"Aviso: {m['id']} ainda não está liberado ({motivo}).", file=sys.stderr)
            texto = rodar(args.motor, PROVA.replace("{titulo}", m["titulo"]).replace("{objetivos}", "; ".join(m["objetivos"])))
            destino = pasta() / "provas" / f"{m['id']}-{date.today().isoformat()}.md"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text(texto, encoding="utf-8")
            print(f"Prova em {destino}. Responda sem consultar e depois: just professor corrigir {m['id']}")
        elif args.cmd == "corrigir":
            m = modulo(args.id)
            provas = sorted((pasta() / "provas").glob(f"{m['id']}-*.md"))
            provas = [p for p in provas if not p.stem.endswith("-correcao")]
            if not provas:
                raise ValueError(f"nenhuma prova de {m['id']} (rode: just professor prova {m['id']})")
            texto = rodar(args.motor, CORRECAO.replace("{titulo}", m["titulo"]).replace("{objetivos}", "; ".join(m["objetivos"]))
                          .replace("{prova}", provas[-1].read_text(encoding="utf-8")))
            provas[-1].with_name(provas[-1].stem + "-correcao.md").write_text(texto, encoding="utf-8")
            nota = nota_da_correcao(texto)
            intervalo, prox = registrar_prova(con, m["id"], nota)
            nuc.evento(con, "professor.prova", {"modulo": m["id"], "nota": nota, "revisar": fracos_da_correcao(texto)},
                       fonte="professor")
            veredito = "aprovado" if nota >= APROVA else f"abaixo de {APROVA}: releia o Bloco 3 e refaça"
            print(f"Nota {nota} ({veredito}). Próxima revisão em {intervalo} dia(s): {prox}.")
        elif args.cmd == "nota":
            # Para quando a prova é feita sem IA: os exercícios e o gabarito comentado do arquivo do mapa (seções 12, 13
            # e 17). A nota entra na mesma escada de revisão da prova corrigida pela IA.
            m = modulo(args.id)
            if not 0 <= args.valor <= 100:
                raise ValueError("a nota vai de 0 a 100")
            intervalo, prox = registrar_prova(con, m["id"], args.valor)
            nuc.evento(con, "professor.prova", {"modulo": m["id"], "nota": args.valor, "revisar": [], "origem": "gabarito"},
                       fonte="professor")
            veredito = "aprovado" if args.valor >= APROVA else f"abaixo de {APROVA}: revise e refaça"
            print(f"{m['id']}: nota {args.valor} ({veredito}). Próxima revisão em {intervalo} dia(s): {prox}.")
        elif args.cmd == "fechar":
            m = modulo(args.id)
            etapa = etapa_do_modulo(m["id"])
            if etapa:  # módulo ligado a uma etapa do mapa: a ficha única do assunto substitui a ficha dupla
                ficha = f"a ficha do assunto (just ficha {etapa}; no fim, just colher {etapa})"
            else:
                ficha = pasta_fichas() / f"{m['id']}.md"
                if not ficha.exists():
                    ficha.parent.mkdir(parents=True, exist_ok=True)
                    ficha.write_text(FICHA.replace("{titulo}", m["titulo"]), encoding="utf-8")
            estimado = m.get("estimado_min", 75)
            nuc.evento(con, "professor.bloco", {"modulo": m["id"], "minutos": args.minutos, "estimado": estimado}, fonte="professor")
            print(PROTOCOLO.replace("{titulo}", m["titulo"]).replace("{ficha}", str(ficha)).replace("{id}", m["id"])
                  .replace("{minutos}", str(args.minutos)).replace("{estimado}", str(estimado)))
        elif args.cmd == "escutei":
            # Podcast e vídeo são passivos; a nota de escuta (3 ideias e 1 ação, de cabeça) é o que transforma em estudo.
            texto = f"Ideias: {args.ideias}" + (f"\nAção: {args.acao}" if args.acao else "")
            rid = nuc.lembrar(con, texto, tipo="nota", titulo=f"Escutei: {args.titulo}", tags="escuta podcast")
            if args.acao:
                nuc.tarefa_nova(con, f"Da escuta '{args.titulo}': {args.acao}")
            print(f"Nota de escuta #{rid} guardada{' e a ação virou tarefa' if args.acao else ''}. Ache depois com: just buscar \"{args.titulo}\"")
        elif args.cmd == "cartoes":
            linhas = []
            for arq in sorted((pasta() / "aulas").glob("*.md")):
                for p, r in cartoes_de(arq.read_text(encoding="utf-8")):
                    linhas.append(f"{p}\t{r}\t{arq.stem}")
            destino = pasta() / "cartoes-anki.tsv"
            destino.parent.mkdir(parents=True, exist_ok=True)
            destino.write_text("\n".join(linhas) + "\n", encoding="utf-8")
            print(f"{len(linhas)} cartões em {destino}. No Anki: Arquivo > Importar, separado por tabulação, 3º campo como etiqueta.")
    except (ValueError, subprocess.CalledProcessError) as erro:
        print(erro, file=sys.stderr)
        return 2
    finally:
        con.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
