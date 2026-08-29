---
tags: [execucao, automacao, portfolio-ams]
tipo: planejamento
status: novo
---

# Painel Central — Arquitetura para Todas as Fases da Carreira
### O `aura-status` de hoje, desenhado pra crescer sem reescrever — empresa própria, freelancer, empregado em empresa grande

> Este documento não repete "o que automatizar e quando" — isso já está resolvido em [[ordem-e-sequencia-de-execucao-automacoes]] (quando construir) e [[veredito-clonar-ou-nao-ferramenta-paga]] (construir vs. adotar). Aqui é só uma pergunta: **como desenhar o painel central hoje pra que, daqui a anos, numa empresa grande, ele ainda seja a mesma ferramenta — só com mais fontes de dado plugadas, não reescrita do zero.**

---

## O que você vai construir sozinho — lista final, e o tamanho real disso

São 4 ferramentas, nenhuma nova além do que já desenhamos nesta conversa, e nenhuma delas é grande o bastante pra competir com o resto do portfólio:

| Ferramenta | Tamanho estimado | Comparação com o que você já conhece | Quando |
|---|---|---|---|
| `aura-status` (núcleo) | ~170 linhas — **já escrito** | Menor que um único RF do AuraPOS | Já feito |
| Cada fonte nova do painel | 20-40 linhas cada | Fração de uma entidade de domínio | 1-2h, quando plugar |
| `aura-queue` | ~100-150 linhas | Bem menor que a lógica de venda do AuraPOS | Um fim de semana, quando 2+ sistemas precisarem conversar |
| `aura-vault-simples` | ~300-400 linhas | Do tamanho de um RF médio (login com JWT) | 2-3 dias, no Passo 10 (produção) |
| `aura-oncall` | ~100-150 linhas | Pequeno, é só temporizador + reenvio | Meio dia, só com mais de uma pessoa no time |

**Somando tudo: entre 700 e 900 linhas, espalhadas ao longo de anos — menor que um único sistema de negócio do seu portfólio.** O AuraPOS sozinho, com os 15 RF completos, já é maior que essas 4 ferramentas juntas. Não é um segundo portfólio competindo com os 23 sistemas — é uma camada fina, construída aos pedaços, cada pedaço nascendo só quando o problema que resolve existir de verdade.

**Documento de projeto completo, no mesmo padrão dos 23 sistemas, pra cada uma:**
- [[aura-status-documento-projeto-final]] — o único dos 4 com potencial real de virar produto vendável
- [[aura-queue-vault-oncall-documento-portfolio]] — os outros 3, documentados como peça de portfólio/aprendizado, não como produto — a razão de cada um estar nessa categoria, explicada dentro do próprio documento

---

## O problema de desenho, antes de qualquer código

Se você escrever o `aura-status` de hoje pensando só em "ler meus repositórios locais", ele quebra ou vira outro programa quando você precisar ler o Jira de um empregador, ou o status de três projetos de cliente diferente como freelancer. A solução não é escrever três programas — é escrever **um painel + várias fontes plugáveis**, onde adicionar uma fase nova da sua carreira é só adicionar uma fonte nova, nunca reescrever o núcleo.

Isso, por acaso, é o mesmo padrão que você já vai aprender no Passo 8 do seu próprio estudo (SOLID, Strategy Pattern) e já usa no resto do portfólio Aura — `IFonteDeEstoque`, `IEmissorFiscal`, interfaces trocáveis. O painel central usa exatamente a mesma ideia, com um nome novo: **`IFonteDeStatus`**.

```csharp
public interface IFonteDeStatus
{
    string Nome { get; }
    Task<ResultadoStatus> ColetarAsync();
}

public record ResultadoStatus(string Categoria, string Resumo, NivelUrgencia Nivel);
public enum NivelUrgencia { Ok, Atencao, Critico }
```

Cada fonte de dado (Git local, Dependabot, backup, Jira, GitHub de empregador) implementa essa interface, uma classe pequena e isolada. O painel central só sabe "chame `ColetarAsync()` de cada fonte ativa e mostre o resultado" — ele nunca precisa saber os detalhes de cada uma.

---

## As fontes, por fase — o que já existe e o que entra depois

| Fase | Fonte | Mecanismo | Status |
|---|---|---|---|
| **Empresa própria** (hoje) | Git de cada repositório (`aura-workspace`, `aura-estudos`) | `git status`, `git log` via processo local | ✅ já construído |
| **Empresa própria** | Backup | Leitura do arquivo de log | ✅ já construído |
| **Empresa própria** | Catálogo de progresso | Leitura do `.md` | ✅ já construído |
| **Empresa própria** | Dependabot | `gh pr list` | ✅ já construído |
| **Empresa própria**, quando sistema estiver no ar | Uptime Kuma | API HTTP local do próprio Uptime Kuma (`/api/status-page/...`) | 🟡 fonte nova, simples de adicionar — só um `HttpClient` a mais |
| **Freelancer** | Status de projeto de cliente | Mesma lógica de Git, só apontando pra uma pasta `aura-freelance\cliente-x\` em vez de `aura-workspace` | 🟡 fonte nova, reaproveita o código que já existe, só muda o caminho |
| **Freelancer** | Prazo de entrega/fatura pendente | Arquivo `.md` simples por cliente, com data — o painel só lê e avisa se está perto do prazo | 🟡 fonte nova, bem pequena |
| **Empregado em empresa grande** | Tarefas atribuídas a você (Jira) | API oficial do Jira (`GET /rest/api/2/search?jql=assignee=currentUser()`), com seu próprio token | 🔴 só quando chegar lá — **e só depois de confirmar com a política de TI da empresa que conectar uma ferramenta pessoal é permitido** |
| **Empregado em empresa grande** | Pull Requests seus, ou esperando sua revisão | API do GitHub/GitLab da empresa | 🔴 mesma cautela da linha acima |
| **Empregado em empresa grande** | Alerta de incidente/on-call | API do PagerDuty/Opsgenie, se a empresa usar e permitir | 🔴 mesma cautela |

**A cautela em vermelho não é burocracia — é a mesma que já registramos no `mapa-automacao-por-contexto-profissional`:** ferramenta pessoal puxando dado de sistema interno de empregador precisa de autorização explícita, sempre, antes de conectar qualquer coisa. O painel funciona sem essas fontes perfeitamente bem — elas são plugadas só quando (e se) fizer sentido.

---

## Desenho pensado pro seu TDAH, não só "funcional"

Um painel que mostra 40 linhas de texto é tão inútil pro seu caso quanto nenhum painel — a informação existe, mas exige esforço de atenção pra extrair o que importa. Regras de desenho, não só de dado:

1. **Cor é a primeira informação, texto é a segunda.** Você deveria saber se está tudo bem só pela quantidade de vermelho/amarelo na tela, antes de ler uma palavra.
2. **Resumo primeiro, detalhe só se pedir.** Rodar `aura-status` mostra 1 linha por fonte (ex: "Git: 2 repositórios com pendência"), não a lista inteira — um argumento (`aura-status --detalhe`) abre o resto, só quando você decidir que quer.
3. **Nunca mais que uma tela, sem rolagem.** Se o número de fontes crescer a ponto de não caber, agrupa por fase (Empresa | Freelance | Emprego), não empilha tudo solto.
4. **Zero notificação por push.** O painel é consultado, não interrompe — evita exatamente a fadiga de alerta já documentada em `por-que-automatizar-riscos-e-testes`. Você decide quando olhar, ele nunca decide por você.
5. **Nunca mistura urgência real com ruído.** Um Pull Request esperando revisão há 2 dias é 🟡; um site fora do ar é 🔴 — o painel nunca trata os dois com o mesmo peso visual.

---

## Como isso cresce, concretamente, sem reescrever

```csharp
// Núcleo do painel — nunca muda quando uma fase nova entra
var fontes = new List<IFonteDeStatus>
{
    new FonteGitLocal(caminhoRepositorios),
    new FonteBackup(caminhoLog),
    new FonteCatalogo(caminhoVault),
    new FonteDependabot(),
};

// No dia em que você virar freelancer, só adiciona:
// fontes.Add(new FonteProjetoCliente(caminhoClientes));

// No dia em que entrar numa empresa grande, e a política permitir:
// fontes.Add(new FonteJira(tokenPessoal));

foreach (var fonte in fontes)
{
    var resultado = await fonte.ColetarAsync();
    Exibir(resultado); // mesma função de exibição, sempre
}
```

Cada fase da sua carreira não é um programa novo — é uma ou duas classes novas, seguindo o mesmo contrato (`IFonteDeStatus`), sem tocar em nada que já funciona.

---

## 🔗 Documentos relacionados
- [[automacao-total-ambiente-trabalho]] e o código já existente do `aura-status` — o núcleo que este documento estende
- [[mapa-automacao-por-contexto-profissional]] — o detalhe de cada fase (o que você controla, o que precisa seguir)
- [[veredito-clonar-ou-nao-ferramenta-paga]] — por que Jira/PagerDuty não precisam ser clonados, só ter uma fonte de leitura no painel
- [[ordem-e-sequencia-de-execucao-automacoes]] — quando cada fonte da tabela acima realmente entra
