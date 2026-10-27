# /// script
# requires-python = ">=3.11"
# dependencies = ["markitdown[pdf,docx,pptx,xlsx]>=0.1.7"]
# ///
"""Acervo: transforma todos os seus documentos em conhecimento organizado e em produtos candidatos.

Lê uma pasta (a cópia do Google Drive pelo Takeout, um HD, um pendrive) SEM alterar nada nela e:
  1. acha cópias repetidas (mesmo conteúdo ou mesmo nome com (1), -2...)
  2. separa o que é pessoal (contracheque, extrato, IRPF...): não converte nem copia
  3. marca o que é de terceiros (livros, cursos) e o que foi feito para a escola
  4. converte o resto para Markdown, com tema e tipo, dentro do seu cofre do Obsidian
  5. escreve o catálogo e o relatório "Produtos do acervo" com o que dá para vender

Tudo roda no notebook; nada é enviado para fora.

    uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular
    uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import sys
import tempfile
import zipfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regras  # noqa: E402

HOME = Path.home()
VAULT_PADRAO = HOME / "dev" / "notas"
DADOS_PADRAO = HOME / "AMtech" / "acervo"
LIMITE_ZIP = 300 * 1024 * 1024  # não abre zip maior que 300 MB


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloco in iter(lambda: f.read(1 << 20), b""):
            h.update(bloco)
    return h.hexdigest()


def arquivos(origem: Path, tmp: Path):
    """Percorre a origem e o conteúdo dos .zip (extraídos numa pasta temporária, protegida contra zip-slip)."""
    for p in sorted(origem.rglob("*")):
        if not p.is_file() or any(parte.startswith(".") for parte in p.relative_to(origem).parts):
            continue
        rel = str(p.relative_to(origem))
        if p.suffix.lower() == ".zip":
            if p.stat().st_size > LIMITE_ZIP:
                yield p, rel, "zip grande demais (abra à mão)"
                continue
            destino = tmp / regras.slug(rel)
            try:
                with zipfile.ZipFile(p) as z:
                    for info in z.infolist():
                        alvo = (destino / info.filename).resolve()
                        if info.is_dir() or not str(alvo).startswith(str(destino.resolve())):
                            continue
                        if Path(info.filename).suffix.lower() not in regras.EXT_PERMITIDAS:
                            continue
                        alvo.parent.mkdir(parents=True, exist_ok=True)
                        with z.open(info) as src, alvo.open("wb") as dst:
                            shutil.copyfileobj(src, dst)
                        yield alvo, f"{rel}!{info.filename}", None
            except zipfile.BadZipFile:
                yield p, rel, "zip corrompido"
            continue
        if p.suffix.lower() not in regras.EXT_PERMITIDAS:
            yield p, rel, f"formato {p.suffix or 'sem extensão'} não é documento"
            continue
        yield p, rel, None


def converter(p: Path, md_conv) -> str:
    if p.suffix.lower() in {".md", ".txt"}:
        return p.read_text(encoding="utf-8", errors="replace")
    return md_conv.convert(str(p)).text_content or ""


def frontmatter(it: dict) -> str:
    linhas = ["---", f"titulo: {json.dumps(it['nome'], ensure_ascii=False)}", f"origem: {json.dumps(it['origem'], ensure_ascii=False)}",
              f"sha256: {it['sha256']}", f"tema: {it['tema']}", f"tipo: {it['tipo']}", f"situacao: {it['situacao']}",
              f"alertas: {json.dumps(it['motivos'], ensure_ascii=False)}", f"importado: {date.today().isoformat()}",
              "tags: [acervo]", "---", ""]
    return "\n".join(linhas)


def relatorio(itens: list[dict], produtos: list[dict], ignorados: list[dict]) -> str:
    total = len(itens) + len(ignorados)
    dup = sum(1 for i in itens if i.get("duplicado_de"))
    por = lambda s: sum(1 for i in itens if i["situacao"] == s and not i.get("duplicado_de"))  # noqa: E731
    o = [f"# Produtos do acervo\n", f"Gerado em {date.today().isoformat()} por tools/acervo/acervo.py. Revise antes de vender: é uma sugestão por regras, não uma decisão.\n",
         "## Resumo\n", "| | Arquivos |", "|---|---:|", f"| Lidos | {total} |", f"| Cópias repetidas (ignoradas) | {dup} |",
         f"| Seus (podem virar produto) | {por('proprio')} |", f"| Feitos para a escola (reescrever ou confirmar direitos) | {por('escola')} |",
         f"| De terceiros (só estudo, não vende nem treina IA) | {por('terceiros')} |", f"| Pessoais (fora do acervo) | {por('pessoal')} |",
         f"| Não são documentos ou deram erro | {len(ignorados)} |", ""]
    o += ["## Produtos candidatos\n"]
    if not produtos:
        o.append("Nenhum ainda: o acervo tem pouco material vendável por tema.\n")
    for p in produtos:
        o.append(f"### {p['produto']}\n")
        o.append(f"- **Onde vender:** {p['canal']}")
        o.append(f"- **Base:** {p['base']} ({regras.q(p['documentos'], 'documento', 'documentos')} do tema)")
        o.append(f"- **Primeiro passo:** {p['primeiro_passo']}")
        for b in p["bloqueios"]:
            o.append(f"- **Antes de vender:** {b}")
        o.append("")
    alertas = [i for i in itens if i["situacao"] in ("escola", "terceiros") or i["motivos"]]
    alertas = [i for i in alertas if i["situacao"] != "pessoal" and not i.get("duplicado_de")]
    o += ["## Alertas para revisar\n", "| Documento | Situação | Motivo |", "|---|---|---|"]
    o += [f"| {i['nome']} | {i['situacao']} | {'; '.join(i['motivos']) or '-'} |" for i in alertas]
    pess = [i for i in itens if i["situacao"] == "pessoal"]
    if pess:
        o += ["", "## Pessoais: guarde fora do acervo\n",
              "Não foram convertidos nem copiados. Mova para uma pasta só sua, coberta pelo backup criptografado.\n"]
        o += [f"- {i['origem']}" for i in pess]
    return "\n".join(o) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--origem", required=True, type=Path, help="pasta com os seus documentos (não é alterada)")
    ap.add_argument("--vault", type=Path, default=VAULT_PADRAO, help="cofre do Obsidian (padrão: ~/dev/notas)")
    ap.add_argument("--dados", type=Path, default=DADOS_PADRAO, help="onde ficam catálogo e relatório (padrão: ~/AMtech/acervo)")
    ap.add_argument("--autor", default="alan", help="seu nome como aparece nos seus documentos")
    ap.add_argument("--simular", action="store_true", help="classifica e mostra o resumo sem escrever nada")
    a = ap.parse_args()
    if not a.origem.is_dir():
        print(f"Pasta não encontrada: {a.origem}", file=sys.stderr)
        return 2

    catalogo_arq = a.dados / "catalogo.json"
    anterior = {i["sha256"]: i for i in json.loads(catalogo_arq.read_text(encoding="utf-8"))} if catalogo_arq.exists() else {}
    md_conv = None
    itens, ignorados, por_sha, por_nome = [], [], {}, {}
    destino_md = a.vault / "30-Acervo"

    with tempfile.TemporaryDirectory(prefix="acervo-") as tmpd:
        for p, rel, problema in arquivos(a.origem, Path(tmpd)):
            if problema:
                ignorados.append({"origem": rel, "motivo": problema})
                continue
            nome = rel.split("!")[-1].split("/")[-1]
            h = sha256(p)
            it = {"nome": nome, "origem": rel, "sha256": h}
            base = regras.nome_base(nome)
            if h in por_sha:
                it.update({k: por_sha[h][k] for k in ("tema", "tipo", "situacao", "motivos")}, duplicado_de=por_sha[h]["origem"])
                itens.append(it)
                continue
            if regras.PESSOAL_NOME.search(regras.sem_acento(nome)):
                it.update(tema="pessoal", tipo="pessoal", situacao="pessoal", motivos=["nome indica documento pessoal ou financeiro"])
            elif h in anterior and anterior[h].get("arquivo_md") and (a.vault / anterior[h]["arquivo_md"]).exists():
                it.update({k: anterior[h][k] for k in ("tema", "tipo", "situacao", "motivos", "arquivo_md")}, reaproveitado=True)
            else:
                if md_conv is None and p.suffix.lower() not in {".md", ".txt"}:
                    try:
                        from markitdown import MarkItDown
                    except ImportError:
                        print("Falta o markitdown. Rode com: uv run tools/acervo/acervo.py ...", file=sys.stderr)
                        return 2
                    md_conv = MarkItDown()
                try:
                    texto = converter(p, md_conv)
                except Exception as e:  # um arquivo ruim não para o acervo
                    ignorados.append({"origem": rel, "motivo": f"erro ao converter: {type(e).__name__}"})
                    continue
                situacao, motivos = regras.classificar_direitos(nome, texto, a.autor)
                it.update(tema=regras.tema(nome, texto) if situacao != "pessoal" else "pessoal",
                          tipo=regras.tipo(nome, texto) if situacao != "pessoal" else "pessoal",
                          situacao=situacao, motivos=motivos, caracteres=len(texto))
                if situacao != "pessoal" and not a.simular:
                    pasta = destino_md / ("_terceiros" if situacao == "terceiros" else it["tema"])
                    pasta.mkdir(parents=True, exist_ok=True)
                    arq = pasta / f"{regras.slug(base)}-{h[:6]}.md"
                    arq.write_text(frontmatter(it) + texto, encoding="utf-8")
                    it["arquivo_md"] = str(arq.relative_to(a.vault))
            if base in por_nome and por_nome[base]["situacao"] == it["situacao"] and it["situacao"] != "pessoal":
                it["parecido_com"] = por_nome[base]["origem"]
            por_nome.setdefault(base, it)
            por_sha[h] = it
            itens.append(it)

    produtos = regras.sugerir_produtos(itens)
    rel_md = relatorio(itens, produtos, ignorados)
    unicos = [i for i in itens if not i.get("duplicado_de")]
    print(f"{len(itens) + len(ignorados)} arquivos lidos · {len(itens) - len(unicos)} cópias repetidas · "
          + " · ".join(f"{s}: {sum(1 for i in unicos if i['situacao'] == s)}" for s in ("proprio", "escola", "terceiros", "pessoal"))
          + f" · {len(ignorados)} fora · {len(produtos)} produtos candidatos")
    if a.simular:
        print("\n".join(rel_md.splitlines()[:40]))
        print("\nSimulação: nada foi escrito.")
        return 0
    a.dados.mkdir(parents=True, exist_ok=True)
    catalogo_arq.write_text(json.dumps(itens, ensure_ascii=False, indent=1), encoding="utf-8")
    with (a.dados / "catalogo.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nome", "origem", "tema", "tipo", "situacao", "duplicado_de", "alertas", "arquivo_md"])
        for i in itens:
            w.writerow([i["nome"], i["origem"], i["tema"], i["tipo"], i["situacao"], i.get("duplicado_de", ""), "; ".join(i["motivos"]), i.get("arquivo_md", "")])
    (a.dados / "fora.json").write_text(json.dumps(ignorados, ensure_ascii=False, indent=1), encoding="utf-8")
    (a.dados / "produtos.json").write_text(json.dumps(produtos, ensure_ascii=False, indent=1), encoding="utf-8")
    pasta_prod = a.vault / "40-Produtos"
    pasta_prod.mkdir(parents=True, exist_ok=True)
    (pasta_prod / "Produtos do acervo.md").write_text(rel_md, encoding="utf-8")
    print(f"Markdown em {destino_md}; relatório em {pasta_prod / 'Produtos do acervo.md'}; catálogo em {catalogo_arq}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
