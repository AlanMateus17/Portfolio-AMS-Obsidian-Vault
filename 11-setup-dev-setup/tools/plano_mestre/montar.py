"""Monta o Plano Mestre único: setup (dev-setup) + estudo + rendas + finanças + formação + certificações.

Uso: python plano_mestre.py <repo dev-setup> <vault> <saida.json>
"""
import json, re, sys, pathlib, importlib.util

REPO, VAULT, OUT = map(pathlib.Path, sys.argv[1:4])

ETAPAS = [
    ("E0", "Etapa 0 · Arrumar a base", "out a início de nov/2026", "Arrumar a base: diagnóstico, senhas, Windows, finanças e o primeiro passo de estudo e de renda."),
    ("E1", "Etapa 1 · Primeiros clientes", "nov a dez/2026", "Montar o núcleo do setup, terminar os Passos 1 e 2 e fazer entrar o primeiro dinheiro extra."),
    ("E2", "Etapa 2 · Primeira venda de produto", "jan a fev/2027", "Vender no CPF com tudo medido, lançar o mini-curso e começar C#, TypeScript e Python."),
    ("E3", "Etapa 3 · Rendas crescendo", "mar a jun/2027", "API, frontend e testes do Kaixara; uma oferta nova por vez; contabilidade e matemática financeira."),
    ("E4", "Etapa 4 · Bater os R$ 7 mil", "jul a dez/2027", "Kaixara completo, arquitetura, candidaturas a vagas e a meta de renda."),
    ("E5", "Etapa 5 · Virar sênior e empresa", "2028", "Produção, plataforma interna, dados e IA, CNPJ, sistemas à venda e certificações."),
    ("E6", "Etapa 6 · Especialização e expansão", "2029 em diante", "Segundo e terceiro sistemas, fase sênior, 42, segurança, IA do zero, fundos e negócios físicos."),
    ("EC", "Sempre · Hábitos e rotinas", "contínuo", "O que roda toda semana, do início ao fim."),
]
TRILHAS = {"setup": "Setup", "estudo": "Estudo", "renda": "Renda", "financas": "Finanças pessoais",
           "formacao": "Formação e certificações", "decisao": "Decisões"}

itens = []
def add(id, trilha, etapa, titulo, pronto="", quando="", liga=(), nota="", gatilho="", fonte="", extra=None):
    d = dict(id=id, trilha=trilha, etapa=etapa, titulo=titulo, pronto=pronto, quando=quando,
             liga=list(liga), nota=nota, gatilho=gatilho, fonte=fonte)
    if extra: d.update(extra)
    itens.append(d)

# ------------------------------------------------------------------ setup (dev-setup)
im = json.loads((REPO / "data" / "implantacao.json").read_text(encoding="utf-8"))
FASE_ETAPA = {**{i: "E0" for i in range(0, 4)}, **{i: "E1" for i in range(4, 14)}, **{i: "E2" for i in range(14, 18)},
              18: "E3", 19: "E3", 20: "E3", 21: "E1", 22: "E3", 23: "E3", 24: "E4", 25: "E5", 26: "E5", 27: "E4",
              28: "E5", 29: "E6", 30: "E5", 31: "E5", 32: "E6", 33: "EC"}
POR_PASSO = {"vaga": ("E4", "Data ligada ao Passo 8 do estudo."),
             **{k: ("E5", "Junto do IA2 da Trilha de Dados e IA (depois do Passo 8 e das Finanças F4–F5).") for k in
                ["zoomcamp", "dbt-metricas", "airflow", "contas-ia"]},
             **{k: ("E6", "Junto do IA6 da Trilha de Dados e IA (treino e fine-tuning).") for k in
                ["dataset", "fine-tune", "modelo-no-ollama"]}}
QUEM = {"voce": "Você", "script": "Script", "claude": "Claude com você"}
setup_por_fase = {}
for i, f in enumerate(im["fases"]):
    for j, p in enumerate(f["passos"], 1):
        etapa, nota = POR_PASSO.get(p["id"], (FASE_ETAPA[i], ""))
        sid = f"S-{p['id']}"
        setup_por_fase.setdefault(i, []).append(sid)
        add(sid, "setup", etapa, p["titulo"], pronto=p.get("pronto", ""),
            quando=f"Setup {i}.{j} · {f['titulo']} · {f.get('quando','')}", gatilho=f.get("gatilho", ""),
            nota=" ".join(x for x in [nota, p.get("nota", "")] if x).strip(),
            fonte="dev-setup · docs/implantacao/roteiro.md",
            extra=dict(fase=i, passo=f"{i}.{j}", quem=QUEM[p["quem"]], comando=p.get("comando", ""),
                       min=p["tempo_min"], precisa=p.get("precisa", []), ofertas=p.get("ofertas", [])))

def fase_ids(*ix):
    return [x for i in ix for x in setup_por_fase[i]]

# ------------------------------------------------------------------ estudo (vault)
sumario = (VAULT / "00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md").read_text(encoding="utf-8")
passos = re.findall(r"^- \[ \] \*\*Passo (\d+)[^—]*— ([^*]+)\*\*([^\n]*)\n(.*?)(?=^- \[ \] \*\*Passo|\n---|\Z)", sumario, re.M | re.S)
P_ETAPA = {1: "E1", 2: "E1", 3: "E2", 4: "E3", 5: "E3", 6: "E3", 7: "E4", 8: "E4", 9: "E5", 10: "E5", 11: "E5", 12: "E5", 13: "E6", 14: "E6"}
P_LIGA = {2: fase_ids(4, 5), 3: ["E-py"], 4: ["S-template-aura", "S-auth", "F-f1"], 5: ["F-f1", "F-f2", "S-deploy-teste"], 6: ["S-sonar"],
          7: ["F-f1", "F-f3", "R-kaixara", "S-kaixara"], 8: ["S-vaga", "E-f4", "E-ia0"], 9: ["S-observabilidade-dev"],
          10: fase_ids(19), 11: [], 12: ["S-template-aura", "S-saas"], 13: ["S-rotara", "R-rotara"], 14: ["R-rendara", "S-servicos-aura"]}
for n, nome, dur, corpo in passos:
    n = int(n)
    pronto = re.search(r"\*\*✅ Pronto quando:\*\*\s*(.+)", corpo)
    add(f"E-P{n}", "estudo", P_ETAPA[n], f"Passo {n} — {nome.strip()}", pronto=pronto.group(1).strip() if pronto else "",
        quando=dur.strip(" *()"), liga=P_LIGA.get(n, []), fonte="vault · 00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO.md")
add("E-epic", "estudo", "E0", "Abrir o EPIC-01 e fazer a primeira User Story do Passo 1", pronto="Uma User Story marcada como feita",
    liga=["E-P1"], fonte="vault · 07-estudo-e-carreira/EPIC-01-backlog-passo1-fundamentos.md")
add("E-py", "estudo", "E2", "Começar o bloco paralelo de Python (1–2 h/semana, refazendo os exercícios de cada Passo)",
    pronto="Exercícios do Passo 3 refeitos em Python e testados com pytest", liga=["E-P3", "E-ia0"], fonte="vault · curriculo-dev-senior-completo.md §2.3")
ESTUDO_EXTRA = [
    ("E-ingles", "EC", "Inglês: Fase A → B → C (meta C1, essencial para o exterior)", "Conversa técnica fluente e entrevista em inglês", ["E-senior"], "ingles-espanhol-integrado.md"),
    ("E-matematica", "EC", "Matemática pelo livro do VHSlins, integrada aos Passos", "Capítulo do Passo atual resolvido", [], "matematica-e-desenvolvimento-integrado.md"),
    ("E-fisica", "E2", "Comprar o livro de Física básica e mandar o índice para montar a trilha", "Trilha de Física escrita no vault", [], "00-PLANO-UNIFICADO.md"),
    ("E-linux", "E3", "Trilha Linux/Arch até o nível que o dev usa (F1–F2)", "Fases F1 e F2 da trilha concluídas", ["S-pendrive-arch"], "trilha-linux-arch-profissional.md"),
    ("E-redes", "E3", "Trilha de Redes", "Fases da trilha concluídas com algo testável", [], "trilha-de-redes.md"),
    ("E-robotica-r1", "E1", "Robótica R1: Arduino Uno e Leonardo no projeto agro da escola", "Sensores da escola identificados e testados", [], "trilha-robotica-iot.md"),
    ("E-robotica-r2", "E3", "Robótica R2: ESP32, sensores e MQTT", "Coleta de dados do projeto agro funcionando", ["E-robotica-r1"], "trilha-robotica-iot.md"),
    ("E-robotica-r3", "E5", "Robótica R3: Raspberry Pi e Linux embarcado", "Central da casa inteligente rodando", ["E-linux"], "trilha-robotica-iot.md"),
    ("E-robotica-r45", "E6", "Robótica R4–R5: robôs e produto vendável (com homologação Anatel se tiver rádio)", "Primeiro produto pronto para vender", ["R-maker"], "trilha-robotica-iot.md"),
    ("E-f4", "E4", "Finanças F4: finanças corporativas e valuation (trilha paralela, depois do Passo 8)", "Preço-teto Bazin e Graham calculado pelo sistema e conferido à mão", ["R-rendara", "E-P8"], "trilha-financas-economia.md"),
    ("E-f5", "E5", "Finanças F5: mercado financeiro, regulação (CVM 19/20/21), Pix e Open Finance", "Cada tela do Rendara classificada como informação, educação ou recomendação", ["C-cpa"], "trilha-financas-economia.md"),
    ("E-f6", "E5", "Finanças F6: economia aplicada, indicadores e econometria em Python", "Painel de indicadores atualizando sozinho pelas APIs do BCB e IBGE", ["A-economia", "E-ia2"], "trilha-financas-economia.md"),
    ("E-f8", "E6", "Finanças F8: finanças quantitativas", "Backtest de uma estratégia com risco medido", ["A-economia"], "trilha-financas-economia.md"),
    ("E-ia0", "E5", "IA0: Python para IA e FastAPI (aura-analytics)", "Endpoint FastAPI testado com pytest", ["E-py", "S-lab-ia"], "trilha-dados-ia.md"),
    ("E-ia1", "E5", "IA1: matemática para IA (álgebra linear, cálculo, probabilidade)", "Gradiente e regressão feitos à mão", ["E-matematica"], "trilha-dados-ia.md"),
    ("E-ia2", "E5", "IA2: dados e engenharia de dados", "Pipeline BCB/IBGE gravando no PostgreSQL", ["S-zoomcamp", "S-dbt-metricas", "S-airflow"], "trilha-dados-ia.md"),
    ("E-ia3", "E5", "IA3: machine learning clássico", "Previsão de fluxo de caixa do Rendara melhor que a média simples", ["R-rendara"], "trilha-dados-ia.md"),
    ("E-ia4", "E6", "IA4: deep learning do zero (autograd sem biblioteca, depois PyTorch)", "Rede treinada com o seu próprio autograd", [], "trilha-dados-ia.md"),
    ("E-ia5", "E5", "IA5: LLMs aplicados (RAG, function calling, avaliação)", "Tutor do AM Mentor respondendo com citação do capítulo", ["S-rag-sistema", "R-ammentor"], "trilha-dados-ia.md"),
    ("E-ia6", "E6", "IA6: tokenizer e transformer do zero; modelo pequeno pré-treinado; fine-tuning de 8B", "Modelo próprio comparado contra o modelo base", ["S-dataset", "S-fine-tune", "S-modelo-no-ollama"], "trilha-dados-ia.md"),
    ("E-ia7", "E6", "IA7: MLOps (servir, versionar, monitorar)", "Modelo atrás do aura-analytics com observabilidade", [], "trilha-dados-ia.md"),
    ("E-42", "E6", "École 42: Circles 00–06, na sua stack e depois em C/C++", "25 entregáveis e 5 Exam Ranks", [], "trilha-42-circles-oficial-verificado.md"),
    ("E-seguranca", "E6", "Segurança ofensiva: laboratórios até eJPT e OSCP", "Writeups publicados", ["C-ejpt", "C-oscp", "S-pendrive-kali"], "roadmap-seguranca-ofensiva-completo.md"),
    ("E-espanhol", "E5", "Espanhol (começa no Passo 12)", "B1–B2", ["E-P12"], "ingles-espanhol-integrado.md"),
    ("E-senior", "E6", "Fase sênior: system design, SLO e postmortem, Kubernetes, entrevista em inglês", "Passa num system design de 45 minutos em inglês", ["E-P14"], "curriculo-dev-senior-completo.md §15"),
    ("E-horizonte", "E6", "Horizonte longo: Linux internals, reverse, kernel, AM-OS e AM Linux", "Gatilhos do mapa de horizonte longo", [], "mapa-horizonte-longo-sistemas.md"),
    ("E-mandarim", "E6", "Mandarim (depois do espanhol)", "—", ["E-espanhol"], "mapa-horizonte-longo-sistemas.md"),
]
for i, e, t, p, l, fo in ESTUDO_EXTRA:
    add(i, "estudo", e, t, pronto=p, liga=l, fonte="vault · 07-estudo-e-carreira/" + fo.split(" ")[0])

# ------------------------------------------------------------------ rendas (portfólio + catálogo)
spec = importlib.util.spec_from_file_location("portfolio", REPO / "tools" / "portfolio" / "portfolio.py")
pm = importlib.util.module_from_spec(spec); sys.path.insert(0, str(REPO / "tools" / "portfolio")); spec.loader.exec_module(pm)
dados = pm.carregar() if hasattr(pm, "carregar") else json.loads((REPO / "data" / "portfolio.json").read_text())
rk = pm.ranking(dados)
oferta_passo = {}
for i, f in enumerate(im["fases"]):
    for j, p in enumerate(f["passos"], 1):
        for o in p.get("ofertas", []):
            oferta_passo.setdefault(o, f"S-{p['id']}")
etapa_de = {x["id"]: x["etapa"] for x in itens}
for o in rk:
    sid = oferta_passo.get(o["id"])
    add(f"R-{o['id']}", "renda", etapa_de.get(sid, "E5"), f"{o['nome']} — {o['proximo_passo']}",
        pronto=f"Métrica: {o['metrica']}", quando=o.get("quando", ""), liga=[sid] if sid else [],
        fonte="dev-setup · data/portfolio.json", extra=dict(pontos=o["pontos"], nova=o["nova"]))
RENDA_EXTRA = [
    ("R-msg", "E0", "Mandar mensagem a contatos e pais de alunos oferecendo aulas particulares e manutenção de computador", "Mensagem enviada", ["R-aulas"]),
    ("R-manutpc", "E1", "Primeiro cliente de manutenção de PC/notebook (formatação, limpeza, troca por SSD)", "Primeiro serviço pago", ["R-assist"]),
    ("R-sitemodelo", "E1", "Montar 1 site modelo de restaurante para mostrar aos clientes", "Site publicado e no portfólio", ["R-sites"]),
    ("R-sites3", "E3", "Sites com manutenção mensal: 3 a 4 clientes", "3 contratos de manutenção ativos", ["R-sites"]),
    ("R-sites7", "E4", "Sites com manutenção mensal: 7 clientes (pagam o salário do restaurante)", "Manutenção líquida acima de R$ 2.200 por 3 meses", ["R-sites", "F-sairrest"]),
    ("R-aulasmeta", "E4", "Aulas particulares: 8 alunos individuais + 2 turmas online", "R$ 2.800/mês em aulas", ["R-aulas"]),
    ("R-meta7k", "E4", "Meta: R$ 7.000 líquidos por mês", "3 meses seguidos acima de R$ 7.000", ["R-sites7", "R-aulasmeta", "R-minicurso"]),
    ("R-congelados", "E6", "Congelados (harumakis): só com licença sanitária e cozinha adequada", "Licença e primeiro lote vendido", []),
    ("R-consultoria", "E6", "Consultoria de investimentos do Rendara (com certificação e registro na CVM)", "Primeiro cliente de consultoria", ["C-cnpi", "R-rendara"]),
    ("R-fundo", "E6", "Gestora e fundo próprio (gestora na CVM, diretor de compliance, administrador e custodiante)", "Fundo registrado", ["C-cga", "C-cfa"]),
    ("R-status", "E6", "aura-status como produto (dev solo e freelancer)", "Primeira venda", []),
]
for i, e, t, p, l in RENDA_EXTRA:
    add(i, "renda", e, t, pronto=p, liga=l, fonte="vault · 01-planejamento-geral/fontes-de-renda-completas.md")

# ------------------------------------------------------------------ finanças pessoais
FIN = [
    ("F-gastos", "E0", "Lançar no Caixa da Casa os gastos fixos (R$ 2.045) e as parcelas do cartão", "Você sabe quanto sobra por mês", []),
    ("F-cartao", "E1", "Zerar o cartão de crédito", "Fatura sem parcelas antigas", []),
    ("F-reserva3", "E2", "Reserva de emergência de 3 meses de gastos fixos", "Valor guardado em caixa separado", ["F-cartao"]),
    ("F-sairescola", "E2", "Decisão: sair da escola só se a renda extra passou de R$ 1.500/mês por 2 meses seguidos", "Decisão tomada com os números", ["R-meta7k"]),
    ("F-consorcio", "E2", "Decidir o lance de R$ 14 mil no consórcio da moto sem furar a reserva", "Decisão anotada", ["F-reserva3"]),
    ("F-acoes", "E3", "Próximo pilar do ARCA: ações escolhidas por Barsi e Bazin", "Primeira compra justificada pelo método", ["F-reserva3"]),
    ("F-f1", "E3", "Finanças F1–F2: contabilidade (partidas dobradas, DRE) e matemática financeira", "Simulador de financiamento bate com o banco", ["E-P5", "E-P7"]),
    ("F-f2", "E3", "Simulador de financiamento do apartamento e de aportes", "Simulador conferido", ["F-apto"]),
    ("F-f3", "E4", "Finanças F3: tributação (carnê-leão, IRPF, Simples, notas fiscais)", "Declaração de IR feita com os dados do seu sistema", ["S-carne-leao", "E-P7"]),
    ("F-reserva6", "E4", "Reserva de 6 meses", "Valor guardado", ["F-reserva3"]),
    ("F-sairrest", "E5", "Sair do restaurante: manutenção de sites acima de R$ 2.200 por 3 meses + reserva de 3 meses", "Gatilho cumprido", ["R-sites7"]),
    ("F-reserva12", "E6", "Reserva de 12 meses", "Valor guardado", ["F-reserva6"]),
    ("F-apto", "E6", "Financiar o apartamento (entrada, parcela até 30% da renda)", "Financiamento aprovado", ["F-reserva12"]),
]
for i, e, t, p, l in FIN:
    add(i, "financas", e, t, pronto=p, liga=l, fonte="vault · trilha-financas-economia.md · memória")

# ------------------------------------------------------------------ formação e certificações
FORM = [
    ("A-licenciatura", "EC", "Licenciatura em Matemática (em curso)", "Diploma", []),
    ("A-decidir", "E4", "Decidir a ordem entre Economia e a faculdade para IA (regra: Economia primeiro se os sistemas precisarem dela)", "Decisão anotada em formacao-academica.md", ["E-f4"]),
    ("A-economia", "E5", "Ciências Econômicas (bacharelado EAD, MEC 4 ou 5)", "Matrícula feita; depois, diploma", ["A-decidir"]),
    ("A-ia", "E6", "Faculdade para IA: Ciência da Computação EAD ou bacharelado presencial em IA (UFU, UFG, UFMS)", "Matrícula feita", ["A-decidir"]),
    ("C-cpa", "E5", "Certificação CPA (ANBIMA)", "Aprovado", ["E-f5"]),
    ("C-cnpi", "E5", "Certificação CNPI (APIMEC) — consultor e relatórios de análise", "Aprovado", ["C-cpa", "R-consultoria"]),
    ("C-cga", "E6", "Certificação CGA (ANBIMA) — gestor de carteiras e fundos", "Aprovado", ["R-fundo"]),
    ("C-cfa", "E6", "CFA (3 níveis, em inglês) — exterior e gestão", "Nível III", ["E-ingles", "R-fundo"]),
    ("C-comptia", "E5", "CompTIA A+ e Network+", "Aprovado", ["E-redes"]),
    ("C-security", "E6", "CompTIA Security+ (CCNA opcional)", "Aprovado", ["C-comptia"]),
    ("C-ejpt", "E6", "eJPT", "Aprovado", ["E-seguranca"]),
    ("C-oscp", "E6", "OSCP", "Aprovado", ["C-ejpt"]),
]
for i, e, t, p, l in FORM:
    add(i, "formacao", e, t, pronto=p, liga=l, fonte="vault · 07-estudo-e-carreira/formacao-academica.md")

# ------------------------------------------------------------------ hábitos e decisões
HAB = [
    ("H-anki", "Anki todo dia, 10–20 min", ["S-anki"]), ("H-fimbloco", "Protocolo de fim de bloco a cada sessão de estudo", []),
    ("H-ensina", "Estuda → ensina → grava: cada tópico vira aula paga e conteúdo", ["R-aulas", "S-ativar-pipeline"]),
    ("H-caixa", "Revisão mensal do Caixa da Casa", ["F-gastos"]), ("H-status", "aura-status toda segunda-feira", []),
    ("H-akita", "1 conteúdo do Fábio Akita por semana", []), ("H-posts", "3 posts por semana tirados das aulas", ["S-perfis"]),
    ("H-senhas", "5 contas por semana no cofre até dez/2026; revisão do cofre a cada 3 meses", ["S-senhas-resto", "S-senhas-revisao"]),
]
for i, t, l in HAB:
    add(i, "estudo" if i in ("H-anki", "H-fimbloco", "H-akita") else ("financas" if i == "H-caixa" else "setup"), "EC", t, liga=l, fonte="vault · 00-GUIA-DO-INICIANTE.md")
DEC = [
    ("D-paralelas", "E4", "Confirmar a ordem das trilhas paralelas (Finanças → IA → 42 → Pentest)", ["E-f4", "E-ia0", "E-42", "E-seguranca"]),
    ("D-clojure", "E6", "aura-historico: Clojure/Datomic ou Event Sourcing com Marten em .NET", ["E-P14"]),
    ("D-socia", "E3", "Sócia do Rendara: trocar o alvo de CEA (extinta) para CPA + C-Pro I ou CFP", ["R-consultoria"]),
    ("D-devsetup", "E0", "Publicar o dev-setup no GitHub (passo de criar o repositório privado)", ["S-repo-criar"]),
]
for i, e, t, l in DEC:
    add(i, "decisao", e, t, liga=l, fonte="vault · 00-PLANO-UNIFICADO.md")

# ------------------------------------------------------------------ conexões nos dois sentidos + checagem
ids = {x["id"] for x in itens}
for i, lista in setup_por_fase.items():          # passo anterior na mesma fase e pré-requisitos
    for a, b in zip(lista, lista[1:]):
        next(x for x in itens if x["id"] == b)["liga"].insert(0, a)
for x in itens:
    for pr in x.get("precisa", []):
        if "S-" + pr in ids: x["liga"].append("S-" + pr)
EXTRA_LIGA = {"E-P11": ["E-P10"], "E-fisica": ["E-matematica"], "E-ia4": ["E-ia3"], "E-ia7": ["E-ia6"],
    "E-horizonte": ["E-linux", "E-42"], "R-congelados": ["S-neg-c1"], "R-status": ["H-status"],
    "A-licenciatura": ["E-matematica", "A-decidir"], "H-fimbloco": ["E-P1"], "H-akita": ["E-P1"]}
for x in itens:
    x["liga"] += EXTRA_LIGA.get(x["id"], [])
    m = re.match(r"E-P(\d+)$", x["id"])
    if m and int(m.group(1)) > 1: x["liga"].insert(0, f"E-P{int(m.group(1))-1}")
    if x["id"] == "E-P1": x["liga"].append("E-epic")
primeiro = {i: l[0] for i, l in setup_por_fase.items()}
for i in range(1, len(primeiro)):                # cada fase liga à anterior
    next(x for x in itens if x["id"] == primeiro[i])["liga"].append(setup_por_fase[i - 1][-1])
assert len(ids) == len(itens), "id repetido"
quebrados = [(x["id"], l) for x in itens for l in x["liga"] if l not in ids]
for x in itens:
    x["liga"] = [l for l in x["liga"] if l in ids]
volta = {}
for x in itens:
    for l in x["liga"]:
        volta.setdefault(l, []).append(x["id"])
for x in itens:
    x["liga"] = list(dict.fromkeys(x["liga"] + volta.get(x["id"], [])))
ordem = {e[0]: n for n, e in enumerate(ETAPAS)}
json.dump(dict(etapas=[dict(id=a, nome=b, quando=c, objetivo=d) for a, b, c, d in ETAPAS], trilhas=TRILHAS, itens=itens,
               gerado="2026-10-26"), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
from collections import Counter
print(len(itens), "itens", Counter(x["trilha"] for x in itens), Counter(x["etapa"] for x in itens))
print("conexões quebradas:", quebrados)
print("sem conexão:", sum(1 for x in itens if not x["liga"]))
