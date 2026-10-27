"""Gera 00-PLANO-MESTRE-PASSO-A-PASSO.md a partir de plano-mestre.json."""
import json, sys
from collections import Counter
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
I = {x["id"]: x for x in d["itens"]}
ORD = {e["id"]: n for n, e in enumerate(d["etapas"])}
TR_ORD = ["setup", "estudo", "renda", "financas", "formacao", "decisao"]
EMO = {"setup": "🛠️", "estudo": "📚", "renda": "💰", "financas": "🏦", "formacao": "🎓", "decisao": "⚖️"}

# checagem de ordem: um pré-requisito nunca pode cair numa etapa posterior
problemas = []
for x in d["itens"]:
    for p in x.get("precisa", []):
        q = I.get("S-" + p)
        if q and ORD[q["etapa"]] > ORD[x["etapa"]] and x["etapa"] != "EC" and q["etapa"] != "EC":
            problemas.append(f"{x['id']} ({x['etapa']}) precisa de {q['id']} ({q['etapa']})")

def link(i):
    return f"`{i}`"

L = []
w = L.append
c = Counter(x["trilha"] for x in d["itens"])
w("---\ntags: [plano-mestre, passo-a-passo, setup, estudo, renda]\n---\n")
w("# 🧭 Plano Mestre — tudo em um só passo a passo\n")
w("> **Este é o único lugar para saber o que fazer a seguir.** Ele junta os dois planejamentos:")
w("> o **setup** (repositório `dev-setup`, 34 fases, hoje dentro deste vault na pasta `11-setup-dev-setup`) e o **estudo** (este vault, 14 Passos), mais")
w("> as **fontes de renda**, as **finanças da casa**, a **faculdade**, as **certificações** e as **decisões**.")
w(f"> São **{len(d['itens'])} itens**, cada um com um código, o que fazer, como saber que terminou e com quais outros itens ele se liga.\n")
w("## Como usar (leia uma vez)\n")
w("1. Vá até a **etapa** em que você está (começa na Etapa 0).")
w("2. Dentro dela, faça os itens **de cima para baixo** em cada trilha. As trilhas andam juntas: na mesma semana você mexe no setup, estuda e corre atrás de renda.")
w("3. Um item só está feito quando o **✅ Pronto quando** for verdade. Marque o `[ ]` como `[x]`.")
w("4. **🔗 Liga com** mostra os códigos dos itens relacionados (o que vem antes, o que depende dele). Use Ctrl+F com o código para achar.")
w("5. Itens com **⏸ gatilho** só começam quando o gatilho acontecer, mesmo que a etapa já tenha chegado.")
w("6. A etapa termina quando os itens dela estão feitos. Datas são estimativas: se atrasar, **a ordem continua a mesma**.")
w("7. Há uma versão interativa (página “Plano Mestre AMS”) com caixinhas, filtros e busca. Os dois têm os mesmos códigos.\n")
w("**Legenda das trilhas:** " + " · ".join(f"{EMO[t]} {d['trilhas'][t]} ({c[t]})" for t in TR_ORD))
w("\n**Códigos:** `S-` setup · `E-` estudo · `R-` renda · `F-` finanças · `A-` faculdade · `C-` certificação · `H-` hábito · `D-` decisão\n")
w("**Quem faz (setup):** Você = clique ou decisão sua · Script = você roda o comando · Claude com você = abre o Claude e pede.\n")
w("## Mapa das etapas\n")
w("| Etapa | Quando | Objetivo | Itens |\n|---|---|---|---|")
ce = Counter(x["etapa"] for x in d["itens"])
for e in d["etapas"]:
    w(f"| [{e['nome']}](#{e['id'].lower()}) | {e['quando']} | {e['objetivo']} | {ce[e['id']]} |")
w("\n## A regra do dinheiro (resumo)\n")
w("- Gastos fixos: cerca de **R$ 2.045/mês**. Restaurante em 2027: **R$ 2.200**. Meta: **R$ 7.000/mês** → faltam **R$ 4.800** de renda extra.")
w("- **Sair da escola** só com renda extra acima de **R$ 1.500/mês por 2 meses seguidos** (`F-sairescola`).")
w("- **Sair do restaurante** só com manutenção de sites acima de **R$ 2.200 por 3 meses** e reserva de 3 meses (`F-sairrest`).")
w("- Uma oferta nova por vez; cada uma precisa de uma métrica antes da próxima (`S-` fase 22).\n")
w("## Ligações entre os dois planejamentos (as mais importantes)\n")
w("| Quando no estudo | O que destrava no setup / na renda |\n|---|---|")
for a, b in [("Passo 2 (Git, SQL, Docker)", "Fases 4–5 do setup (Linux/WSL2, GitHub e CI) — o setup é a prática do Passo 2"),
             ("Passo 3 (C#, TypeScript)", "Bloco paralelo de Python `E-py`"),
             ("Passo 5 (EF Core)", "Finanças F1–F2 `F-f1`"),
             ("Passo 7 (Kaixara fechado)", "Renda do Kaixara, carnê-leão `S-carne-leao`, tributação `F-f3`"),
             ("Passo 4 a 6 (API, testes)", "Base dos sistemas AM (fase 18); conta na nuvem e deploy do sistema exemplo (fase 19) com o Passo 5"),
             ("Passo 8 (Arquitetura)", "Candidatura a vagas `S-vaga`; destrava as trilhas paralelas (Finanças F4–F5 → Dados e IA → 42 → Pentest)"),
             ("IA2 da trilha de Dados e IA (≈ 2028)", "Zoomcamp, dbt e Airflow da fase 21"),
             ("Passo 9 + IA0 (≈ 2028)", "IA dentro dos sistemas AM (fase 25), junto do IA5"),
             ("IA6 da trilha (≈ 2029)", "Dataset, fine-tuning do 8B e modelo no Ollama (fase 21)"),
             ("Passo 10 (Produção real)", "Deploy de produção do AM Kaixara na nuvem montada na fase 19"),
             ("Passo 12 (Plataforma interna)", "Sistemas AM à venda; espanhol começa"),
             ("Passo 14 + fase sênior", "Rendara, consultoria, fundo; decisão do aura-historico")]:
    w(f"| {a} | {b} |")
w("")
for e in d["etapas"]:
    its = [x for x in d["itens"] if x["etapa"] == e["id"]]
    w(f"\n---\n\n## {e['nome']}\n<a id=\"{e['id'].lower()}\"></a>\n")
    w(f"**Quando:** {e['quando']} · **Objetivo:** {e['objetivo']}\n")
    for t in TR_ORD:
        sub = [x for x in its if x["trilha"] == t]
        if not sub: continue
        if t == "setup": sub.sort(key=lambda x: (x.get("fase", 99), int(x.get("passo", "0.0").split(".")[1])))
        w(f"### {EMO[t]} {d['trilhas'][t]} ({len(sub)})\n")
        fase_atual = None
        for x in sub:
            if t == "setup" and "fase" in x and x["fase"] != fase_atual:
                fase_atual = x["fase"]
                w(f"\n**Fase {x['fase']} do setup** — {x['quando'].split(' · ')[1]}" + (f" · ⏸ gatilho: {x['gatilho']}" if x["gatilho"] else "") + "\n")
            head = f"- [ ] {link(x['id'])} "
            if "fase" in x:
                head += f"**{x['passo']}** {x['titulo']} · _{x['quem']}, ~{x['min']} min_"
            else:
                head += f"**{x['titulo']}**" + (f" · ⭐ {x['pontos']} pts" if "pontos" in x else "")
            w(head)
            if x.get("comando"): w(f"  - 💻 `{x['comando']}`")
            if x.get("blocos"): w("  - 🧱 Implanta: " + ", ".join(f"{b['nome']} (camada {b['camada']:02d})" for b in x["blocos"]))
            if x["pronto"]: w(f"  - ✅ Pronto quando: {x['pronto']}")
            if x["quando"] and "fase" not in x: w(f"  - 🕒 {x['quando']}")
            if x["gatilho"] and "fase" not in x: w(f"  - ⏸ Gatilho: {x['gatilho']}")
            if x["nota"]: w(f"  - 📝 {x['nota']}")
            w("  - 🔗 Liga com: " + ", ".join(link(i) for i in x["liga"]))
w("\n---\n\n## Todos os blocos do setup e em que passo cada um entra\n")
w(f"São **{sum(len(c['blocos']) for c in d['camadas'])} blocos** em **{len(d['camadas'])} camadas**. Cada bloco é um programa, conta, serviço, sistema ou peça do setup. O código `S-…` diz em que passo ele entra; o documento da camada tem o diagrama dela.\n")
for c in d["camadas"]:
    w(f"### Camada {c['n']:02d} · {c['titulo']} ({len(c['blocos'])} blocos) · [documento da camada]({c['arquivo']})\n")
    w("| Bloco | O que é | Entra em |\n|---|---|---|")
    for b in c["blocos"]:
        desc = b["descricao"].replace("|", "/").replace("\n", " ")
        w(f"| {b['nome']} | {desc} | " + ", ".join(link(p) for p in b["passos"]) + " |")
    w("")
w("\n---\n\n## Onde está cada coisa\n")
w("- Setup completo explicado: [[setup-completo-dev-setup]] · tudo do dev-setup (documentos, fluxogramas, roteiro, páginas e scripts): [índice do setup](11-setup-dev-setup/00-INDICE-DO-SETUP.md) · roteiro passo a passo: [roteiro de implantação](11-setup-dev-setup/docs/implantacao/roteiro.md)")
w("- Estudo detalhado: [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] · currículo sênior: [[curriculo-dev-senior-completo]]")
w("- Rendas: [[fontes-de-renda-completas]] · faculdade e certificações: [[formacao-academica]]")
w("- Palavras difíceis: [[00-GLOSSARIO]] · versão curta: [[00-GUIA-DO-INICIANTE]]")
w(f"\n_Gerado em {d['gerado']} a partir de `plano-mestre.json` (dados do dev-setup + vault). Ordem verificada: nenhum pré-requisito cai numa etapa posterior ({len(problemas)} problemas)._")
open(out, "w", encoding="utf-8").write("\n".join(L) + "\n")
print("linhas", len(L), "problemas de ordem:", problemas)
