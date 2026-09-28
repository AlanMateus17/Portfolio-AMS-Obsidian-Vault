---
tags: [execucao, portfolio-ams]
tipo: execucao
status: completo
---

# GitHub — Estrutura Profissional e Autoridade Técnica
### Atualização do guia anterior (feito pra 3 sistemas) para a escala real de 21 sistemas + 10 serviços

---

## 1. A decisão mais importante: Organização, não conta pessoal

Com 3 sistemas, repositório pessoal fazia sentido. Com 21 sistemas + 10 serviços, isso vira ruído no seu perfil pessoal. Crie uma **GitHub Organization** — `grupo-amtech-digital` ou `aura-ecosystem` — e mova tudo pra lá. Isso sozinho já é um sinal de profissionalismo: recrutador e cliente enxergam "empresa", não "projeto de estudante".

**Seu perfil pessoal** continua existindo, mas vira mais enxuto: profile README curto, apresentando você, com link pra organização — não precisa (e não deveria) fixar 21 repositórios lá.

---

## 1.5 Estrutura de pasta local — antes de virar repositório

Tudo nasce local, em `C:\dev\`, organizado em três categorias que **nunca se misturam**:

```
C:\dev\
├── aura-workspace\              (sistemas reais — 1 pasta por repositório da Organization)
│   ├── kaixara-backend\
│   ├── kaixara-frontend\
│   └── ...                      (nasce só quando o sistema chegar no Passo correspondente)
│
├── aura-estudos\                (exercício e prática dos Passos — NÃO é produto)
│   ├── passo-01-logica\
│   ├── passo-02-git-sql-docker\
│   ├── passo-03-csharp-fundamentals\
│   └── ...                      (uma pasta por Passo, criada quando o Passo começa)
│
└── 42-cursus\                   (projetos da Trilha 42)
    ├── circle-00\
    └── ...                      (segue a convenção de repositório da própria 42 — confirme quando chegar lá, a escola às vezes exige um formato específico de submissão)
```

## 1.6 Exercício não vira repositório novo a cada vez

Diferente dos sistemas (1 repositório por sistema, seção 2), os exercícios de estudo (o que você resolve dentro de cada Passo, tipo "cálculo de carrinho com desconto" do Passo 1) vivem **num único repositório**, `aura-estudos`, na Organization — uma pasta por Passo dentro dele, não um repositório novo por exercício. Evita os 40+ repositórios vazios/triviais que a seção 2 já identificou como anti-padrão, e ainda fica público, versionado e visível pra quem for avaliar seu progresso.



Com 21 sistemas documentados mas só o AM Kaixara em código, criar 40+ repositórios vazios agora seria o oposto de profissional — pareceria abandono, não ambição. Regra simples: **repositório só nasce quando o primeiro commit real está pronto pra subir**, não quando o planejamento termina.

O que existe desde já, independente disso:

| Repositório | Conteúdo | Por quê já |
|---|---|---|
| `aura-ecosystem` | README com visão geral, arquitetura, roadmap dos 21 sistemas — **sem código** | É a vitrine. Fixado no topo da organização. Escalando o que o guia anterior já propunha pro `kaixara-ecosystem` |
| `aura-docs` (novo) | O conteúdo do seu vault do Obsidian, publicado como site (seção 5) | Documentação pública é diferencial real — poucos portfólios júnior/pleno mostram isso |
| `kaixara-backend`, `kaixara-frontend` | Já existe, já em código | — |

Os outros 19 sistemas e 9 serviços restantes (`aura-identity` já tem conteúdo suficiente pra nascer logo, dado que é Tier 1 da sua estratégia de extração) entram conforme a Fase 6D e os passos seguintes do `passo-a-passo-mestre-desde-o-inicio` forem sendo cumpridos.

---

## 3. Convenção de nome e descrição — mantendo o que já existia, escalado

Segue exatamente o padrão do guia anterior — `<sistema>-backend`, `<sistema>-frontend`, serviço compartilhado sem sufixo (`aura-identity`, `aura-vault`). Topics por repositório: `dotnet`, `aspnetcore`, `postgresql`, `clean-architecture`, `ddd`, `multi-tenant`, mais os específicos (`postgis`, `signalr`, `clojure`, `datomic`, `python`, `fastapi`).

---

## 4. O que muda de verdade — profissionalismo além de organização

### 4.1 Architecture Decision Records (ADR)
Isso é novo em relação ao guia anterior, e é a adição de maior valor real. Você já tem, em quase todo documento do portfólio, uma seção **"Pendências e decisões em aberto"** — cada decisão que você tomar a partir dali (ex: "escolhemos Stripe Billing, não Vindi, porque X") deveria virar um arquivo curto em `aura-ecosystem/docs/adr/0001-escolha-gateway-pagamento.md`. Formato padrão de mercado:

```
# ADR 0001: Escolha do gateway de pagamento

## Status: Aceito
## Contexto: [o problema, copiado da seção de pendência do documento original]
## Decisão: [o que foi escolhido]
## Consequências: [o que isso implica pros outros sistemas]
```

Isso é prática real de empresa madura — e você já tem a matéria-prima pronta, só precisa formalizar cada decisão conforme ela for tomada.

### 4.2 GitHub Projects (quadro Kanban) espelhando o EPIC-01
Seu `EPIC-01-backlog-passo1-fundamentos.md` já está estruturado como Sprint/User Story/Task. Isso se converte quase 1:1 em **GitHub Issues** (uma issue por User Story, checklist de Task dentro da descrição) organizadas num **GitHub Project** (quadro Kanban nativo, gratuito). Vantagem real: histórico público e datado de progresso — evidência concreta de disciplina de execução pra quem for avaliar seu perfil depois.

### 4.3 Template de Issue e Pull Request
Arquivo `.github/ISSUE_TEMPLATE.md` e `.github/PULL_REQUEST_TEMPLATE.md` na raiz de cada repositório — força você (e qualquer futuro colaborador) a preencher contexto, critério de aceite, o que foi testado. Mesmo sozinho, isso instala o hábito antes de precisar dele em equipe.

### 4.4 Conventional Commits + Changelog automático
Já mencionado no guia anterior — reforçando aqui porque, com pacote NuGet privado entrando na Fase 6D (extração da plataforma interna), commit padronizado (`feat:`, `fix:`, `docs:`) permite gerar `CHANGELOG.md` automaticamente por ferramenta gratuita (`semantic-release` via GitHub Actions), sem trabalho manual.

### 4.5 Branch protection na `main`
Configuração gratuita do GitHub: exigir que toda mudança passe pelo pipeline de CI (já planejado) antes de poder ser mesclada. Sinaliza disciplina de engenharia mesmo em repositório de uma pessoa só.

---

## 5. A inovação real: publicar a documentação, não só o código

Isso é o que dá autoridade de verdade, mais do que qualquer configuração de repositório. A maioria dos portfólios mostra código. **Poucos mostram o raciocínio de arquitetura por trás — que é exatamente o que você já tem, em 41 documentos.**

**Como fazer, gratuito:** publicar uma versão curada do seu vault do Obsidian como site via **GitHub Pages + MkDocs Material** (ferramenta gratuita, gera site de documentação bonito a partir de Markdown puro — seus arquivos já estão prontos, quase sem edição). Isso vira `docs.grupo-amtech-digital.com.br` ou `seu-usuario.github.io/aura-docs`.

**O que publicar (curado, não tudo):**
- A visão geral do ecossistema e a arquitetura reaproveitável (RNFT-E, RNFT-S, RNFT-D)
- Os ADRs conforme forem nascendo
- O padrão de Clean Architecture + multi-tenant que você usa
- **Não publicar:** dado financeiro específico de precificação, informação de cliente real, qualquer coisa da AM Canteira/AM Horaria com risco jurídico se mal interpretada fora de contexto

**Por que isso constrói autoridade de verdade:** um recrutador ou cliente que lê "aqui está como decidimos proteger dado sensível de forma centralizada em vez de reimplementar 4 vezes" enxerga pensamento de arquiteto sênior — isso é raro em portfólio de quem está começando, e é exatamente o que você já documentou no `aura-vault`.

---

## 6. Coisa que o guia anterior já tinha certo, sem mudar

- Profile README (`seu-usuario/seu-usuario`) — mantém, só atualiza pra linkar pra organização, não pros repositórios individuais
- README por repositório na ordem: frase → problema → stack → como rodar → arquitetura → link pros sistemas irmãos
- Badges de tecnologia no README

---

## 7. Ordem prática de execução, sem sobrecarregar

1. Criar a organização e mover o `kaixara-backend`/`kaixara-frontend` existentes pra dentro dela
2. Criar `aura-ecosystem` com o README de visão geral (reaproveitando o `00-INICIO` do Obsidian como base)
3. Publicar `aura-docs` via GitHub Pages — pode ser feito com o material que já existe, sem esperar mais nenhum sistema avançar
4. A partir da próxima decisão real tomada (ex: gateway de pagamento), já registrar como ADR — hábito novo, começa no próximo, não precisa retroagir todas as pendências antigas de uma vez
5. GitHub Project só quando o EPIC-01 estiver ativo — não vale montar quadro Kanban antes de ter tarefa rodando nele
