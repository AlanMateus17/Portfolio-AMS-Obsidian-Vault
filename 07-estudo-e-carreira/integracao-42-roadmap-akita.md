---
tags: [estudo, portfolio-ams]
tipo: estudo
status: completo
---

# Integrando École 42, roadmap.sh e Fábio Akita ao Plano
### Aplicando a mesma régua de sempre: o que entra, entra no lugar certo — o resto fica de fora, com o motivo explícito

---

## Parte 1 — École 42: currículo real, mas em C/C++

### O que a 42 realmente é
Escola sem professor, aprendizado peer-to-peer, currículo em árvore de projetos. O Common Core confirmado (pesquisado agora, não de memória): `libft` (reimplementar função da biblioteca C padrão) → `born2beroot` (VM Linux hardened) → `ft_printf` → `get_next_line` → `push_swap`/`so_long`/`fract-ol` (algoritmo/gráfico) → `pipex`/`minitalk` (processo Unix) → `philosophers` (concorrência com mutex/semáforo) → `minishell` (shell próprio) → `cub3d`/`net_practice` → módulos de C++ → `webserv` (servidor HTTP do zero) → `ft_transcendence` (projeto final full stack).

### A honestidade que precisa vir primeiro
Adotar esse currículo inteiro significa **aprender C e C++ do zero**, como trilha completa — não é adicionar um projeto, é adicionar uma segunda linguagem de sistemas com peso comparável ao próprio C#/.NET. Aplicando a mesma régua de 3 perguntas já usada nesta conversa (resolve problema real agora? existe forma mais simples? vai reaparecer ou é uso único?), a maior parte do currículo **não passa** — seria o mesmo erro de proporção já corrigido com Clojure/Datomic, agora em escala maior.

### O que entra — critério de valor real, baixo custo de linguagem nova

| Projeto 42 | Entra? | Por quê |
|---|---|---|
| **`born2beroot`** (VM Linux, SSH, hardening, política de senha) | ✅ Entra | Não exige C — é Linux/ops puro, e conecta direto com a Fase 6 (deploy) já existente. Fazer esse projeto de verdade antes do primeiro deploy real do AuraPOS é preparo genuíno, não currículo por currículo |
| **`net_practice`** (configuração de rede/IP) | ✅ Entra | Mesma lógica — sem custo de linguagem nova, fortalece exatamente o tipo de conhecimento de infraestrutura que a Fase 6 e a Fase 12 (pentest) já exigem |
| **Conceito de `webserv`** (construir servidor HTTP do zero) | ⚠️ Entra, mas **não em C++** | O valor real é entender o que o ASP.NET Core abstrai por baixo — isso dá pra fazer em C# mesmo (um servidor HTTP mínimo usando só `Socket`/`TcpListener`, sem framework), sem pagar o custo de aprender C++ só pra isso |
| `libft`, `ft_printf`, `get_next_line`, `minishell`, `philosophers`, `cub3d`, módulos C++ | ❌ Não entram | Alto custo de linguagem nova (C/C++), baixo retorno incremental dado que você já vai aprender concorrência, algoritmo e manipulação de string dentro do próprio C#/.NET nas fases já planejadas |

### Onde isso entra no plano
- `born2beroot`: antes do **Passo 10** (Produção real) do `passo-a-passo-mestre-desde-o-inicio` — fazer esse projeto como preparo direto pro primeiro deploy
- `net_practice`: mesma janela, complementar
- Servidor HTTP mínimo em C#: como exercício de aprofundamento dentro da **Fase 2.2** (ASP.NET Core) — construir o mínimo antes de usar o framework completo, pra sentir na pele o que ele resolve

---

## Parte 2 — roadmap.sh: checklist visual de lacuna, não currículo à parte

**Correção: você tinha razão em corrigir — não é Stack Overflow, é [roadmap.sh](https://roadmap.sh/roadmaps), um site diferente e mais adequado.** É um projeto open source (6º mais estrelado do GitHub) com roadmap visual, gratuito, por tecnologia/carreira — cada nó do mapa linka pra recurso curado. Confirmei a existência real e atual antes de integrar.

Diferente de currículo com progressão própria, o uso certo de roadmap.sh é como **auditoria cruzada** — verificar se o seu próprio plano já construído tem lacuna que o roadmap da comunidade aponta e você não tinha visto.

### Roadmaps diretamente relevantes ao seu plano, confirmados
| Roadmap | Link | Cruza com |
|---|---|---|
| Backend | [roadmap.sh/backend](https://roadmap.sh/backend) | Passos 3-8 (fundamento geral de backend) |
| ASP.NET Core | [roadmap.sh/aspnet-core](https://roadmap.sh/aspnet-core) | Passos 3-5 — específico do seu framework |
| Índice geral (todos os roadmaps: PostgreSQL, Docker, System Design, C, C++, Git/GitHub, SQL, DevOps, Kubernetes) | [roadmap.sh/roadmaps](https://roadmap.sh/roadmaps) | Praticamente todo o plano — use pra achar o roadmap certo de cada tecnologia específica na hora de cada Passo |

### Como usar sem virar mais uma trilha
No início de cada bloco grande (Passo 3, Passo 8, Passo 8B, Passo 10), abrir o roadmap correspondente e comparar 2 minutos contra o que já está no seu plano — se aparecer um nó que você nunca ouviu falar, essa é a lacuna real; se for tudo familiar, seguir sem desviar. Não é pra seguir o roadmap do zero, é conferência rápida contra o que você já construiu.

---

## Parte 3 — Fábio Akita: hábito de consumo contínuo, com trilha real por tema (correção: episódios específicos, não mais "1 vídeo por semana" genérico)

Canal chamado **"Akitando"**, blog **"AkitaOnRails"** (`akitaonrails.com`) — mesmo autor, conteúdo complementar (vídeo dá contexto, post costuma ter mais profundidade técnica e código).

### Playlist de início (fundamentos, sequência oficial dele)
`#36` a `#49`, mais `#54` e `#76` — playlist "Programação para Iniciantes" (começou com o nome "Começando aos 40"), cada vídeo tem post correspondente no blog.

### Trilhas temáticas, pra depois do início — episódio real, não estimativa
| Trilha | Episódios |
|---|---|
| Carreira/trajetória pessoal | `#61`, `#64`, `#83`, `#138` |
| Estrutura de Dados & Algoritmos | `#95`, `#118`, `#143`, `#144` |
| Infra/Redes/Homelab | `#98`, `#99`, `#126`, `#139`, `#146` |
| Segurança/Criptografia | `#67`, `#131`, `#147` |
| Linguagens & Comparações | `#136`, `#145` |
| IA aplicada (mais recente) | `#142`, `#148`, `#149` |

O canal tem 150+ episódios ao todo — esta lista é o recorte que cruza direto com o que você já estuda (não é o canal inteiro).

**Como encaixar sem virar mais uma trilha:** bloco fixo pequeno e recorrente, não meta de "terminar". Sugestão: 1 vídeo ou 1 post de blog por semana, no tempo de deslocamento ou pausa — mesmo princípio de "reaproveitar tempo que já existe" já usado com o inglês (ouvir em vez de ler, se for vídeo longo). Escolha a trilha temática por prioridade de fase (ex: Segurança/Criptografia quando chegar no `aura-vault` ou no Pentest, Infra/Redes quando chegar no `Born2beroot`/`NetPractice`).

**Por que vale, mesmo sem estrutura formal:** o conteúdo dele é majoritariamente sobre **contexto de carreira e indústria**, não sobre sintaxe de linguagem — complementa exatamente a lacuna de "entendimento de mercado" que apareceu antes (ex: quando expliquei as áreas de uma empresa grande). Não substitui nenhuma fase técnica, é pano de fundo cultural.

---

## Resumo — o que muda de verdade no plano

1. **Duas adições concretas de baixo custo:** `Born2beroot` e `NetPractice`, antes da Fase 6 (Produção)
2. **Um exercício adaptado, não importado:** servidor HTTP mínimo em C#, dentro da Fase 2.2, em vez do `webserv` em C++
3. **roadmap.sh:** checklist de auditoria cruzada no início de cada bloco grande, não currículo próprio
4. **Fábio Akita:** consumo semanal leve, contínuo, sem fase nem critério de conclusão — cultura de indústria, não currículo técnico
5. **O resto do currículo da 42** (a maior parte, em C/C++ puro) fica de fora — não por falta de qualidade, mas porque o custo de abrir uma segunda linguagem de sistemas inteira não se paga dado o que você já tem pela frente

---

## 🔗 Documentos relacionados
