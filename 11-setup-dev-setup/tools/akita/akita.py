#!/usr/bin/env python3
"""Escola Akita: o blog e os episódios do Akitando viram notas, e as notas viram regras que o setup segue com o seu ok.

O conteúdo é do Fabio Akita (© 2006-2026, sem licença aberta). Por isso:
  - o texto original fica só na sua máquina: um clone do repositório público do blog em ~/dev/referencias/akitaonrails
    (fora do dev-setup, nunca vai para o GitHub) e uma cópia pesquisável no banco local do núcleo;
  - no repositório entram só o índice (título, data, link, tags) e as regras escritas com outras palavras, cada uma
    com o link da fonte;
  - o livro dele (Competent Enough) é pago e não entra; post de opinião ou off-topic vira nota, não regra.

Nada muda no setup sem você: toda regra nasce "nova", você decide (aprovar, recusar, já segue, não se aplica)
e só a aprovada vira tarefa para o Claude, que abre PR para você revisar.

    python3 tools/akita/akita.py sincronizar            # clona ou atualiza o blog (git, repositório público)
    python3 tools/akita/akita.py indexar                # índice + texto no núcleo local
    python3 tools/akita/akita.py fila -n 10             # próximos posts sem nota, por prioridade
    python3 tools/akita/akita.py pacote SLUG            # o pedido de extração, para colar ou mandar a uma IA
    python3 tools/akita/akita.py notar SLUG --motor claude|ollama
    python3 tools/akita/akita.py lote -n 5 --motor ollama
    python3 tools/akita/akita.py pendentes              # regras esperando a sua decisão
    python3 tools/akita/akita.py aprovar AK-0003        |  recusar AK-0004 "motivo"  |  ja-segue AK-0001 "onde"
    python3 tools/akita/akita.py aplicar AK-0003        # o comando para o Claude aplicar (PR, sem merge)
    python3 tools/akita/akita.py docs [--check]         # docs/akita/README.md a partir de data/akita/regras.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "tools" / "nucleo"))
import nucleo as nuc  # noqa: E402

REPO_URL = "https://github.com/akitaonrails/akitaonrails.github.io.git"
SITE = "https://akitaonrails.com"
DADOS = RAIZ / "data" / "akita"
REGRAS = DADOS / "regras.json"
INDICE = DADOS / "indice.json"
CONTEXTO = RAIZ / "docs" / "akita" / "contexto-setup.md"
DOC = RAIZ / "docs" / "akita" / "README.md"
TIPOS = ("regra", "dica", "alerta", "pratica", "ferramenta")
AREAS = ("ia", "dev", "infra", "seguranca", "negocio", "carreira", "hardware", "dados")
ESTADOS = ("nova", "aprovada", "aplicada", "ja-segue", "recusada", "nao-se-aplica", "substituida")
DECIDIDOS = ("aprovada", "aplicada", "ja-segue", "recusada", "nao-se-aplica", "substituida")
OPINIAO = {"off-topic", "politica", "politics", "economia", "pessoal", "censura", "eleicoes", "clima"}
TECNICO = {"ia", "llm", "claude", "agentes", "vibe-coding", "devops", "linux", "seguranca", "programacao", "docker",
           "rust", "ruby", "rails", "arquitetura", "carreira", "backup", "homelab", "open-source", "benchmark"}


def repo_local() -> Path:
    return Path(os.environ.get("AKITA_REPO") or Path.home() / "dev" / "referencias" / "akitaonrails")


def cofre_notas() -> Path:
    vault = Path(os.environ.get("AMTECH_VAULT") or Path.home() / "dev" / "notas")
    return Path(os.environ.get("AKITA_NOTAS") or vault / "07-estudo-e-carreira" / "akita")


# ---------- leitura do blog ----------

def frontmatter(texto: str) -> tuple[dict, str]:
    """Front matter YAML simples do Hugo (title, date, slug, tags, description) e o corpo."""
    if not texto.startswith("---"):
        return {}, texto
    fim = texto.find("\n---", 3)
    cab, corpo = texto[3:fim], texto[fim + 4:]
    meta: dict = {"tags": []}
    chave = None
    for ln in cab.splitlines():
        if re.match(r"^\s*-\s", ln) and chave == "tags":
            meta["tags"].append(ln.split("-", 1)[1].strip().strip("'\""))
        elif re.match(r"^\S[^:]*:", ln):
            chave, _, valor = ln.partition(":")
            chave, valor = chave.strip(), valor.strip().strip("'\"")
            if chave != "tags":
                meta[chave] = valor
        elif chave in ("title", "description") and ln.startswith("  "):
            meta[chave] = (meta.get(chave, "") + " " + ln.strip().strip("'\"")).strip()
    return meta, corpo


def corpo_limpo(corpo: str) -> str:
    """Tira blocos de código, imagens e shortcodes: sobra o raciocínio, que é o que vira nota."""
    saida, codigo = [], False
    for ln in corpo.splitlines():
        if ln.strip().startswith("```"):
            codigo = not codigo
            continue
        if codigo or ln.startswith("![") or ln.strip().startswith("{{"):
            continue
        if ln.strip():
            saida.append(ln)
    return "\n".join(saida)


def _sem_acento(t: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFKD", t.lower()) if not unicodedata.combining(c))


def classificar(meta: dict, ano: int, video: bool) -> tuple[str, int]:
    """Categoria e prioridade (1 = primeiro). A era da IA (2025+) primeiro, depois os episódios do Akitando,
    depois o resto; os posts da era Rails (até 2013) por último, como histórico."""
    tags = {_sem_acento(t) for t in meta.get("tags", [])}
    titulo = _sem_acento(meta.get("title", ""))
    if tags & OPINIAO or titulo.startswith("off-topic"):
        return "opiniao", 9
    if ano >= 2025:
        return "ia-e-dev-atual", 1
    if video or "akitando" in tags:
        return "akitando", 2
    if ano >= 2014:
        return "tecnico", 3
    return "historico", 4


def ler_posts(repo: Path) -> list[dict]:
    posts = []
    for arq in sorted((repo / "content").glob("[12][0-9][0-9][0-9]/**/index.md")):
        meta, corpo = frontmatter(arq.read_text(encoding="utf-8", errors="replace"))
        if meta.get("draft") == "true" or not meta.get("title"):
            continue
        partes = arq.relative_to(repo / "content").parts
        ano = int(partes[0])
        slug = meta.get("slug") or partes[-2]
        caminho = "/".join(partes[:-1])
        video = "{{< youtube" in corpo
        cat, prio = classificar(meta, ano, video)
        texto = corpo_limpo(corpo)
        posts.append({"slug": slug, "titulo": meta["title"], "data": meta.get("date", "")[:10], "url": f"{SITE}/{caminho}/",
                      "tags": meta.get("tags", []), "video": video, "categoria": cat, "prioridade": prio,
                      "palavras": len(texto.split()), "_texto": texto, "_arquivo": str(arq)})
    return posts


# ---------- regras ----------

def carregar_regras() -> dict:
    if REGRAS.exists():
        return json.loads(REGRAS.read_text(encoding="utf-8"))
    return {"notas": {}, "regras": []}


def salvar_regras(d: dict) -> None:
    DADOS.mkdir(parents=True, exist_ok=True)
    REGRAS.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def proximo_id(d: dict) -> str:
    n = max((int(r["id"][3:]) for r in d["regras"]), default=0)
    return f"AK-{n + 1:04d}"


def validar_extracao(x: dict) -> dict:
    """Confere o JSON que a IA devolveu antes de gravar qualquer coisa."""
    if not isinstance(x, dict) or "resumo" not in x or not isinstance(x.get("itens", []), list):
        raise ValueError("a extração precisa de 'resumo' e 'itens'")
    for i in x.get("itens", []):
        if i.get("tipo") not in TIPOS or i.get("area") not in AREAS or len(i.get("texto", "")) < 15:
            raise ValueError(f"item inválido: {i}")
    return x


def registrar(d: dict, post: dict, extracao: dict) -> list[str]:
    """Grava a nota do post e as regras novas (sem repetir texto igual). Devolve os ids criados."""
    extracao = validar_extracao(extracao)
    existentes = {_sem_acento(r["texto"]) for r in d["regras"]}
    novos = []
    if not extracao.get("opiniao"):
        for it in extracao.get("itens", []):
            if _sem_acento(it["texto"]) in existentes:
                continue
            rid = proximo_id(d)
            d["regras"].append({"id": rid, "tipo": it["tipo"], "area": it["area"], "texto": it["texto"],
                                "no_setup": it.get("aplica_ao_setup", ""), "sugestao": it.get("estado_sugerido", ""),
                                "validade": extracao.get("validade", "perene"),
                                "fonte": {"titulo": post["titulo"], "url": post["url"], "data": post["data"]},
                                "estado": "nova", "decisao": ""})
            existentes.add(_sem_acento(it["texto"]))
            novos.append(rid)
    d["notas"][post["slug"]] = {"data": str(date.today()), "regras": novos, "opiniao": bool(extracao.get("opiniao"))}
    return novos


def decidir(d: dict, rid: str, estado: str, motivo: str = "") -> dict:
    if estado not in ESTADOS:
        raise ValueError(f"estado inválido: {estado}")
    for r in d["regras"]:
        if r["id"] == rid:
            r["estado"], r["decisao"] = estado, motivo
            return r
    raise ValueError(f"regra {rid} não existe")


def nota_markdown(post: dict, extracao: dict, ids: list[str]) -> str:
    linhas = ["---", f"titulo: \"{post['titulo']}\"", f"fonte: {post['url']}", f"data: {post['data']}",
              f"categoria: {post['categoria']}", f"validade: {extracao.get('validade', 'perene')}", "autor: Fabio Akita",
              "tags: [akita]", "---", "", f"# {post['titulo']}", "", f"Fonte: [{post['url']}]({post['url']})", "",
              "## Resumo (com as minhas palavras)", "", extracao["resumo"], ""]
    if extracao.get("itens"):
        linhas += ["## Regras, dicas e alertas", ""]
        for i, it in enumerate(extracao["itens"]):
            rid = ids[i] if i < len(ids) else ""
            linhas.append(f"- **{it['tipo']}** ({it['area']}) {rid}: {it['texto']}")
            if it.get("aplica_ao_setup"):
                linhas.append(f"  - No meu setup: {it['aplica_ao_setup']}")
    return "\n".join(linhas) + "\n"


# ---------- pedido à IA ----------

PEDIDO = """Você vai ler um post do blog do Fabio Akita (akitaonrails.com) e extrair o que um desenvolvedor solo deve
seguir. Escreva TUDO com as suas palavras, em português do Brasil: nunca copie frases do texto (no máximo uma citação
de até 15 palavras entre aspas). Responda só com um JSON válido, sem nada antes ou depois, neste formato:

{"resumo": "3 a 5 frases com a ideia central",
 "opiniao": false,
 "validade": "perene" ou "datado" (datado = benchmark, modelo da semana, preço, versão),
 "itens": [{"tipo": "regra|dica|alerta|pratica|ferramenta", "area": "ia|dev|infra|seguranca|negocio|carreira|hardware|dados",
            "texto": "uma frase acionável",
            "aplica_ao_setup": "o que isso mudaria no setup descrito abaixo, ou onde o setup já faz isso",
            "estado_sugerido": "ja-segue|proposta|nao-se-aplica"}]}

Regras da extração: só o que é acionável; 3 a 12 itens; se o post for opinião, política ou off-topic, "opiniao": true
e "itens": []; nada sobre alunos, senhas ou dados pessoais.

O SETUP DO ALAN (para comparar):
{contexto}

O POST: "{titulo}" ({data}) {url}
{texto}
"""


def pacote(post: dict, limite: int = 60000) -> str:
    contexto = CONTEXTO.read_text(encoding="utf-8") if CONTEXTO.exists() else "(sem resumo do setup)"
    return (PEDIDO.replace("{contexto}", contexto).replace("{titulo}", post["titulo"]).replace("{data}", post["data"])
            .replace("{url}", post["url"]).replace("{texto}", post["_texto"][:limite]))


def extrair_json(saida: str) -> dict:
    ini, fim = saida.find("{"), saida.rfind("}")
    if ini < 0 or fim < ini:
        raise ValueError("a IA não devolveu JSON")
    return json.loads(saida[ini:fim + 1])


def rodar_motor(motor: str, pedido: str) -> str:
    if motor == "claude":
        cmd = ["claude", "-p", "--output-format", "text"]
    elif motor == "ollama":
        cmd = ["ollama", "run", os.environ.get("AKITA_MODELO", "qwen2.5:7b")]
    else:
        raise ValueError("motor: claude ou ollama")
    return subprocess.run(cmd, input=pedido, capture_output=True, text=True, check=True, timeout=1800).stdout


# ---------- documento ----------

def gerar_doc(d: dict) -> str:
    rs = d["regras"]
    cont = {e: sum(1 for r in rs if r["estado"] == e) for e in ESTADOS}
    o = ["# Escola Akita: regras que o setup segue com o seu ok", "",
         "Gerado por tools/akita/akita.py a partir de data/akita/regras.json. Cada regra está escrita com outras palavras",
         "e aponta para o post original do Fabio Akita. O texto dele fica só na sua máquina.", "",
         f"Posts com nota: **{len(d['notas'])}** · regras: **{len(rs)}** · " +
         " · ".join(f"{e}: {n}" for e, n in cont.items() if n), "",
         "Decidir: `just akita pendentes`, depois `just akita aprovar AK-0001` (ou recusar, ja-segue, nao-se-aplica).", ""]
    for estado, titulo in (("nova", "Esperando a sua decisão"), ("aprovada", "Aprovadas, para aplicar"),
                           ("aplicada", "Aplicadas"), ("ja-segue", "O setup já segue"),
                           ("nao-se-aplica", "Não se aplicam"), ("recusada", "Recusadas")):
        grupo = [r for r in rs if r["estado"] == estado]
        if not grupo:
            continue
        o += [f"## {titulo} ({len(grupo)})", "", "| Id | Tipo | Área | Regra | No setup | Fonte |", "|---|---|---|---|---|---|"]
        for r in grupo:
            extra = r["decisao"] or r["no_setup"]
            o.append(f"| {r['id']} | {r['tipo']} | {r['area']} | {r['texto']} | {extra} | "
                     f"[{r['fonte']['data']}]({r['fonte']['url']}) |")
        o.append("")
    return "\n".join(o)


# ---------- CLI ----------

def _post(slug: str) -> dict:
    for p in ler_posts(repo_local()):
        if p["slug"] == slug:
            return p
    raise ValueError(f"post {slug} não encontrado (rode: just akita sincronizar && just akita indexar)")


def fila(posts: list[dict], d: dict, n: int) -> list[dict]:
    feitos = set(d["notas"])
    resto = [p for p in posts if p["slug"] not in feitos and p["categoria"] != "opiniao"]
    return sorted(resto, key=lambda p: (p["prioridade"], _inverso(p["data"])))[:n]


def _inverso(data: str) -> str:
    """Mais novo primeiro dentro da mesma prioridade."""
    return "".join(chr(255 - ord(c)) for c in data)


def notar(slug: str, motor: str, d: dict) -> list[str]:
    post = _post(slug)
    extracao = validar_extracao(extrair_json(rodar_motor(motor, pacote(post))))
    ids = registrar(d, post, extracao)
    destino = cofre_notas() / f"{post['data']}-{slug[:60]}.md"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(nota_markdown(post, extracao, ids), encoding="utf-8")
    salvar_regras(d)
    return ids


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    s = ap.add_subparsers(dest="cmd", required=True)
    s.add_parser("sincronizar")
    s.add_parser("indexar")
    s.add_parser("fila").add_argument("-n", type=int, default=10)
    s.add_parser("pacote").add_argument("slug")
    a = s.add_parser("notar"); a.add_argument("slug"); a.add_argument("--motor", default="claude")
    b = s.add_parser("lote"); b.add_argument("-n", type=int, default=5); b.add_argument("--motor", default="ollama")
    s.add_parser("pendentes")
    for nome in ("aprovar", "recusar", "ja-segue", "nao-se-aplica", "aplicada"):
        c = s.add_parser(nome); c.add_argument("id"); c.add_argument("motivo", nargs="?", default="")
    s.add_parser("aplicar").add_argument("id")
    s.add_parser("docs").add_argument("--check", action="store_true")
    args = ap.parse_args(argv)
    d = carregar_regras()
    try:
        if args.cmd == "sincronizar":
            r = repo_local()
            if (r / ".git").exists():
                subprocess.run(["git", "-C", str(r), "pull", "-q", "--ff-only"], check=True)
            else:
                r.parent.mkdir(parents=True, exist_ok=True)
                subprocess.run(["git", "clone", "-q", "--depth", "1", "--filter=blob:limit=2m", REPO_URL, str(r)], check=True)
            print(f"Blog do Akita em {r} (só na sua máquina; não vai para o GitHub).")
        elif args.cmd == "indexar":
            posts = ler_posts(repo_local())
            DADOS.mkdir(parents=True, exist_ok=True)
            indice = [{k: v for k, v in p.items() if not k.startswith("_")} for p in posts]
            INDICE.write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            con = nuc.abrir()
            for p in posts:
                nuc.lembrar(con, p["_texto"], tipo="referencia", titulo=f"Akita: {p['titulo']}", origem=p["url"],
                            tags="akita " + " ".join(p["tags"]), chave=f"akita:{p['slug']}")
            con.close()
            por = {}
            for p in posts:
                por[p["categoria"]] = por.get(p["categoria"], 0) + 1
            print(f"{len(posts)} posts indexados ({', '.join(f'{k}: {v}' for k, v in sorted(por.items()))}). "
                  f"Texto pesquisável no núcleo local: just buscar \"backup btrfs\".")
        elif args.cmd == "fila":
            for p in fila(ler_posts(repo_local()), d, args.n):
                print(f"[{p['prioridade']}] {p['data']} {p['slug']}  ({p['palavras']} palavras{', vídeo' if p['video'] else ''})")
        elif args.cmd == "pacote":
            print(pacote(_post(args.slug)))
        elif args.cmd == "notar":
            ids = notar(args.slug, args.motor, d)
            print(f"Nota salva no Obsidian; {len(ids)} regra(s) nova(s): {' '.join(ids) or '-'}. Decida com: just akita pendentes")
        elif args.cmd == "lote":
            for p in fila(ler_posts(repo_local()), d, args.n):
                try:
                    ids = notar(p["slug"], args.motor, d)
                    print(f"ok {p['slug']}: {len(ids)} regra(s)")
                except (ValueError, subprocess.SubprocessError, json.JSONDecodeError) as erro:
                    print(f"pulei {p['slug']}: {erro}", file=sys.stderr)
            DOC.write_text(gerar_doc(d), encoding="utf-8")
        elif args.cmd == "pendentes":
            novas = [r for r in d["regras"] if r["estado"] == "nova"]
            for r in novas:
                print(f"{r['id']} [{r['tipo']}/{r['area']}] {r['texto']}\n   no setup: {r['no_setup']}\n   sugestão: {r['sugestao']} · fonte: {r['fonte']['url']}\n")
            print(f"{len(novas)} esperando você. Decida: just akita aprovar ID | recusar ID \"motivo\" | ja-segue ID \"onde\" | nao-se-aplica ID \"por quê\"")
        elif args.cmd in ("aprovar", "recusar", "ja-segue", "nao-se-aplica", "aplicada"):
            estado = {"aprovar": "aprovada", "recusar": "recusada"}.get(args.cmd, args.cmd)
            r = decidir(d, args.id, estado, args.motivo)
            salvar_regras(d)
            DOC.write_text(gerar_doc(d), encoding="utf-8")
            con = nuc.abrir()
            nuc.auditar(con, "alan", f"{estado} {r['id']}: {r['texto'][:120]}", "pede-ok", args.motivo, aprovado_por="alan")
            if estado in ("aprovada", "aplicada", "ja-segue"):
                # Regra aceita vira conhecimento do núcleo: a triagem, o arquiteto e as aulas do Professor passam a vê-la.
                nuc.lembrar(con, f"{r['texto']} No setup: {r['no_setup']} Fonte: {r['fonte']['url']}", tipo="padrao",
                            titulo=f"Akita {r['id']}: {r['texto'][:80]}", origem=r["fonte"]["url"], tags="akita regra",
                            chave=f"akita-regra:{r['id']}")
            if estado == "aprovada":
                tid = nuc.tarefa_nova(con, f"Aplicar {r['id']} (Akita): {r['texto'][:150]}", responsavel="claude")
                print(f"{r['id']} aprovada; tarefa #{tid} no núcleo. Para aplicar: just akita aplicar {r['id']}")
            else:
                print(f"{r['id']}: {estado}.")
            con.close()
        elif args.cmd == "aplicar":
            r = next((x for x in d["regras"] if x["id"] == args.id), None)
            if not r or r["estado"] != "aprovada":
                raise ValueError(f"{args.id} não está aprovada; só regra aprovada vira mudança no setup")
            pedido = (f"Aplicar no dev-setup a regra {r['id']} (do Fabio Akita, {r['fonte']['url']}): {r['texto']} "
                      f"O que muda no setup: {r['no_setup']} Siga o CLAUDE.md, rode just check, abra um PR e NÃO faça merge.")
            print("Ubuntu do WSL, na pasta do setup:")
            print(f"cd ~/dev/dev-setup && ai-jail claude {json.dumps(pedido, ensure_ascii=False)}")
        elif args.cmd == "docs":
            texto = gerar_doc(d)
            if args.check:
                if not DOC.exists() or DOC.read_text(encoding="utf-8") != texto:
                    print("docs/akita/README.md desatualizado. Rode: python3 tools/akita/akita.py docs", file=sys.stderr)
                    return 1
                print("Escola Akita em dia.")
            else:
                DOC.parent.mkdir(parents=True, exist_ok=True)
                DOC.write_text(texto, encoding="utf-8")
                print(f"Gerado {DOC.relative_to(RAIZ)}")
    except (ValueError, subprocess.CalledProcessError) as erro:
        print(erro, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
