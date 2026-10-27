"""Regras do acervo: o que é pessoal, de terceiros ou da escola, de que tema e tipo é cada documento,
e que produtos dá para tirar dele. Só biblioteca padrão, para ser testada no CI.

Os nomes de arquivo e trechos de texto aqui são exemplos genéricos; nada de dado real.
"""
from __future__ import annotations

import re
import unicodedata
from collections import defaultdict

# ---------------------------------------------------------------- normalização


def sem_acento(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def nome_base(nome: str) -> str:
    """'Aula-01 (2).docx' e 'Aula-01-3.docx' viram 'aula-01': para achar cópias com nomes parecidos."""
    n = sem_acento(nome.rsplit(".", 1)[0])
    n = re.sub(r"\s*\(\d+\)$", "", n)
    n = re.sub(r"[-_ ]\d{1,2}$", "", n)
    return re.sub(r"[\s_]+", "-", n).strip("-")


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", sem_acento(s)).strip("-")[:80] or "sem-nome"


# ---------------------------------------------------------------- privacidade e direitos

PESSOAL_NOME = re.compile(
    r"contracheque|holerite|nubank|extrato|irpf|declaracao|fatura|boleto|comprovante|sef[_ -]?mg|fazenda|"
    r"\bcpf\b|\brg\b|\bcnh\b|certidao|receita[_ -]federal|darf|carne[_ -]?leao|exame|laudo|receituario")
CPF = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
CNPJ = re.compile(r"\b\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}\b")
EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b")
TELEFONE = re.compile(r"\(?\b\d{2}\)?\s?9?\d{4}-?\d{4}\b")
ALUNO = re.compile(r"\b(aluno|aluna|estudante|nome do aluno|matr[ií]cula|respons[aá]vel)\s*:\s*\S+", re.I)
TERCEIROS_TEXTO = re.compile(
    r"todos os direitos reservados|all rights reserved|©|\bcopyright\b|\bisbn\b|casa do c[oó]digo|novatec|"
    r"o'?reilly|alta books|packt|manning|pearson", re.I)
TERCEIROS_NOME = re.compile(r"ebook|e-book|udemy|alura|rocketseat|vhslins|estacio|casa do codigo|\(casa|novatec|o'?reilly")
ESCOLA = re.compile(
    r"\bemti\b|escola estadual|e\.\s?e\.\s|see[-/ ]?mg|secretaria de estado de educa|curr[ií]culo refer[eê]ncia|"
    r"\bementa\b|plano de curso|superintend[eê]ncia regional", re.I)
EXT_PERMITIDAS = {".pdf", ".docx", ".pptx", ".xlsx", ".md", ".txt", ".html", ".htm", ".csv"}


def dados_pessoais(texto: str) -> dict[str, int]:
    achados = {"cpf": len(CPF.findall(texto)), "cnpj": len(CNPJ.findall(texto)), "email": len(EMAIL.findall(texto)),
               "telefone": len(TELEFONE.findall(texto)), "aluno": len(ALUNO.findall(texto))}
    return {k: v for k, v in achados.items() if v}


def classificar_direitos(nome: str, texto: str, autor: str = "alan") -> tuple[str, list[str]]:
    """Devolve (situação, motivos). Situações:
    pessoal  - documento pessoal: não converte, não copia, só aparece na lista para você guardar à parte
    terceiros- material de outra pessoa ou empresa: só estudo; não vende e não vai para treino de IA
    escola   - feito para a escola: confirmar direitos; o caminho seguro é reescrever do zero, fora do expediente
    proprio  - seu: pode virar produto (depois de limpar dados pessoais, se houver)
    """
    n, t = sem_acento(nome), texto[:20000]
    if PESSOAL_NOME.search(n):
        return "pessoal", ["nome indica documento pessoal ou financeiro"]
    dp = dados_pessoais(t)
    if dp.get("cpf", 0) >= 2 or dp.get("cnpj", 0) >= 3:
        return "pessoal", [f"contém documentos de pessoas ({dp})"]
    motivos = []
    terceiros = TERCEIROS_TEXTO.findall(t[:6000]) + TERCEIROS_NOME.findall(n)
    if terceiros and autor not in sem_acento(t[:3000]):
        return "terceiros", [f"marcas de obra de terceiros: {', '.join(sorted({x.lower() for x in terceiros})[:4])}"]
    if ESCOLA.search(t[:8000]) or ESCOLA.search(n):
        motivos.append("feito para a escola: confira os direitos antes de vender")
        situacao = "escola"
    else:
        situacao = "proprio"
    if dp:
        motivos.append(f"tem dados pessoais para apagar antes de usar: {', '.join(f'{k} ({v})' for k, v in dp.items())}")
    return situacao, motivos


# ---------------------------------------------------------------- tema e tipo

TEMAS: dict[str, tuple[str, list[str]]] = {
    "logica": ("Lógica de Programação", ["logica de programacao", "logicaprog", "algoritmo", "fluxograma", "pseudocodigo", "portugol", "visualg"]),
    "so": ("Sistemas Operacionais", ["sistemas operacionais", "sistema operacional", "so", "processos e threads", "escalonamento", "kernel"]),
    "hardware": ("Arquitetura e Manutenção de Computadores", ["arquitetura e manutencao", "hardware", "placa-mae", "placa mae", "processador", "memoria ram", "fonte atx", "manutencao de computadores"]),
    "htmlcss": ("HTML e CSS", ["htmlcss", "html", "css", "flexbox", "grid layout"]),
    "web": ("Programação Web", ["programacao web", "javascript", "dom", "http", "api rest", "node", "next.js", "react"]),
    "poo": ("POO e Java", ["poo", "orientacao a objetos", "orientada a objetos", "java", "heranca", "polimorfismo", "encapsulamento"]),
    "robotica": ("Robótica e Arduino", ["robotica", "arduino", "esp32", "raspberry", "sensor", "servo", "protoboard"]),
    "labsoft": ("Laboratório de Software", ["laboratorio de software", "lab software", "labsoftware", "lab-software"]),
    "labhard": ("Laboratório de Hardware", ["laboratorio de hardware", "lab hardware", "labhardware", "lab-hardware"]),
    "terminal": ("Terminal, Git, Docker e DevOps", ["terminal", "bash", "powershell", "git", "docker", "wsl", "devops", "linux", "comandos"]),
    "bd": ("Banco de Dados", ["banco de dados", "sql", "postgres", "mysql", "modelagem", "entidade relacionamento"]),
    "seguranca": ("Segurança da Informação", ["seguranca", "pentest", "kali", "owasp", "ciberseguranca", "ofensiva"]),
    "ia": ("Inteligência Artificial", ["inteligencia artificial", "machine learning", "llm", "rag", "prompt", "redes neurais"]),
    "dados": ("Engenharia e Análise de Dados", ["engenharia de dados", "dbt", "airflow", "spark", "pandas", "duckdb", "etl"]),
    "matematica": ("Matemática", ["matematica", "algebra", "calculo", "geometria", "probabilidade", "estatistica"]),
    "financas": ("Finanças e Investimentos", ["financas", "investimento", "b3", "renda fixa", "acoes", "orcamento"]),
    "sistemas": ("Sistemas e arquitetura de software (Aura)", ["aura", "especificacao", "requisitos", "documento-projeto", "arquitetura de software", "clean architecture", "ddd", "kaixara", "rendara", "rotara"]),
    "blockchain": ("Blockchain educacional (BSD)", ["bsd", "bytesdcoin", "blockchain", "provably fair"]),
    "carreira": ("Estudo e carreira", ["roadmap", "trilha", "plano de estudos", "metodo de estudo", "curriculo", "portfolio", "vaga", "akita", "42"]),
    "idiomas": ("Idiomas", ["ingles", "espanhol", "idioma"]),
    "projeto": ("Projeto integrador", ["projeto integrador", "projeto-integrador", "primeiros passos do projeto"]),
}

TIPOS: list[tuple[str, str, list[str]]] = [
    ("gabarito", "Prova ou gabarito", ["gabarito", "prova", "avaliacao", "simulado"]),
    ("exercicios", "Exercícios", ["exercicio", "lista de", "atividade", "desafio"]),
    ("apostila", "Apostila", ["apostila", "guia", "manual", "comandos"]),
    ("aula", "Aula ou slides", ["aula", "slide", "apresentacao", "conteudo-quadro", "quadro"]),
    ("plano", "Plano (aula, curso, projeto)", ["plano de aula", "plano-anual", "plano anual", "plano de ensino", "projeto-integrador", "projeto integrador", "entregaveis"]),
    ("especificacao", "Especificação de sistema", ["especificacao", "requisitos", "documento-projeto", "documento-unico", "stack", "decisao", "rnf", "arquitetura"]),
    ("estudo", "Plano ou método de estudo", ["roadmap", "trilha", "plano de estudos", "plano-estudos", "metodo", "sequencia", "sumario", "biblioteca-recursos"]),
    ("comercial", "Material comercial", ["proposta", "apresentacao comercial", "apresentacao-comercial", "orcamento"]),
]


def _conta(chave: str, alvo: str) -> int:
    return len(re.findall(r"(?<![a-z0-9])" + re.escape(chave) + r"(?![a-z0-9])", alvo))


def tema(nome: str, texto: str) -> str:
    alvo_nome = re.sub(r"[-_.]+", " ", sem_acento(nome))
    alvo_nome = re.sub(r"([a-z])(\d)", r"\1 \2", alvo_nome)
    alvo_texto = sem_acento(texto[:15000])
    pontos = defaultdict(int)
    for tid, (_, chaves) in TEMAS.items():
        for k in chaves:
            kk = re.sub(r"[-_]+", " ", k).strip()
            if not kk:
                continue
            if _conta(kk, alvo_nome) or (len(kk) > 4 and kk.replace(" ", "") in alvo_nome.replace(" ", "")):
                pontos[tid] += 5
            if len(kk) > 3:
                pontos[tid] += min(_conta(kk, alvo_texto), 6)
    if not pontos or max(pontos.values()) == 0:
        return "outros"
    return max(pontos, key=lambda k: (pontos[k], -list(TEMAS).index(k)))


def tipo(nome: str, texto: str = "") -> str:
    alvo = sem_acento(nome).replace("_", " ")
    for tid, _, chaves in TIPOS:
        if any(k in alvo for k in chaves):
            return tid
    inicio = sem_acento(texto[:400])
    for tid, _, chaves in TIPOS:
        if any(k in inicio for k in chaves):
            return tid
    return "outro"


# ---------------------------------------------------------------- produtos

VENDAVEIS = {"proprio", "escola"}


def q(n: int, um: str, varios: str) -> str:
    return f"{n} {um if n == 1 else varios}"


def sugerir_produtos(itens: list[dict]) -> list[dict]:
    """Agrupa o catálogo por tema e sugere produtos. Cada sugestão traz a base, o que bloqueia e o primeiro passo."""
    por_tema: dict[str, list[dict]] = defaultdict(list)
    for it in itens:
        if it.get("situacao") in VENDAVEIS and not it.get("duplicado_de") and not it.get("parecido_com"):
            por_tema[it["tema"]].append(it)
    out = []
    for tid, docs in sorted(por_tema.items(), key=lambda kv: -len(kv[1])):
        nome_tema = TEMAS.get(tid, ("Outros",))[0]
        n = defaultdict(int)
        for d in docs:
            n[d["tipo"]] += 1
        escola = sum(1 for d in docs if d["situacao"] == "escola")
        limpar = sum(1 for d in docs if any("dados pessoais" in m for m in d.get("motivos", [])))
        bloqueios = []
        if escola:
            bloqueios.append(f"{escola} de {len(docs)} feitos para a escola: reescreva do zero ou confirme os direitos")
        if limpar:
            bloqueios.append(f"{limpar} com dados pessoais para apagar")

        def add(produto, canal, base, passo):
            out.append({"tema": tid, "nome_tema": nome_tema, "produto": produto, "canal": canal, "base": base,
                        "documentos": len(docs), "bloqueios": bloqueios, "primeiro_passo": passo})

        aulas, exerc, provas, apost, planos = n["aula"], n["exercicios"], n["gabarito"], n["apostila"], n["plano"]
        if aulas + apost >= 3:
            add(f"Mini-curso de {nome_tema}", "Hotmart ou Kiwify, versão na Udemy",
                f"{q(aulas, 'aula', 'aulas')}, {q(apost, 'apostila', 'apostilas')}", "Gravar as 3 primeiras aulas a partir do material, com a sua voz e exemplos novos")
        if apost >= 1:
            add(f"Apostila de {nome_tema} (PDF)", "Hotmart, Kiwify e isca grátis de um capítulo",
                q(apost, "apostila", "apostilas"), "Juntar as apostilas num só PDF com a identidade da marca")
        if exerc + provas >= 3:
            add(f"Banco de questões de {nome_tema} com gabarito comentado", "Hotmart; amostra grátis no Instagram",
                f"{q(exerc, 'lista de exercícios', 'listas de exercícios')}, {q(provas, 'prova ou gabarito', 'provas ou gabaritos')}", "Passar as questões para YAML (exercícios do livro) e comentar o gabarito")
        if aulas + planos + provas >= 4:
            add(f"Kit do professor de {nome_tema} (slides, plano e avaliação)", "Hotmart para professores de cursos técnicos",
                f"{q(aulas, 'aula', 'aulas')}, {q(planos, 'plano', 'planos')}, {q(provas, 'avaliação', 'avaliações')}", "Montar um kit de 1 unidade e oferecer a 5 professores conhecidos")
        if n["especificacao"] >= 3:
            add("Estudo de caso: documentação completa de sistemas (requisitos, arquitetura e stack)", "Hotmart e portfólio",
                q(n["especificacao"], "especificação", "especificações"), "Escolher 1 sistema e transformar a especificação em ebook com templates editáveis")
        if n["estudo"] >= 3:
            add(f"Guia de estudos: {nome_tema}", "Ebook barato ou isca grátis da newsletter",
                q(n["estudo"], "plano ou roteiro", "planos e roteiros"), "Juntar os roteiros num guia único e testar como isca")
        if len(docs) >= 5:
            add(f"Série de conteúdo sobre {nome_tema}", "Instagram, YouTube e blog (atrai público para os produtos acima)",
                q(len(docs), "documento", "documentos"), "Colocar 1 documento por semana em ~/AMtech/entrada/ideias")
    return out
