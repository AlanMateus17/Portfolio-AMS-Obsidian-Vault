# Economia de tokens: produzir mais, gastar menos

[← Arquitetura de IA](README.md)

Token é o que o Claude cobra: cada palavra que entra (o que você manda) e que sai (o que ele responde) conta. Produzir mais gastando menos não é escrever menos; é **fazer o Claude trabalhar só no que é difícil** e deixar o resto com o seu computador, que é de graça.

## As cinco regras

1. **Peça um script, não o resultado.** O erro que mais gasta token é pedir ao Claude para "desenhar" ou "listar tudo". Peça o programa que faz isso. Um script de 40 linhas custa pouco token e gera a planta, as 500 linhas da tabela ou as 50 questões de graça, no seu PC, quantas vezes você quiser.
2. **Uma conversa por tarefa.** Conversa longa reenvia todo o histórico a cada mensagem: a quinta pergunta paga pelas quatro anteriores. Comece nova com o pacote de contexto (`contexto.py --inicio`), que é curto.
3. **A IA certa para cada tarefa.** O Claude é o caro. Rascunho, resumo, transcrição e tradução vão para o modelo local (Ollama) ou grátis. Pergunte ao roteador: `tools/ia/tokens.py rota "sua tarefa"`.
4. **Busca nas suas notas (RAG), não colar.** Em vez de colar um documento inteiro toda vez, o setup busca só o trecho que importa. Menos entra, menos custa.
5. **Deixe o resultado pronto antes de pedir revisão.** Mande o Claude revisar o que já está quase pronto (gasta pouco), não construir do zero numa conversa de ida e volta (gasta muito).

## Exemplo: a planta baixa de uma casa

**Jeito caro (não faça):** "Claude, desenhe a planta baixa da minha casa com sala, dois quartos, cozinha e banheiro, com todas as medidas." Ele responde com páginas de texto ou SVG, você pede ajuste, ele redesenha tudo de novo. Cada rodada paga o desenho inteiro.

**Jeito do setup (barato e melhor):**

1. Você fala (ou escreve): *"Jarvis, casa térrea, 7 por 10 metros: sala, 2 quartos, cozinha e banheiro."*
2. O Claude Code escreve **um script de FreeCAD ou Bonsai** com as paredes, portas e janelas como parâmetros (largura, altura, posição). Isso é pouco token.
3. O script roda no seu PC e gera o modelo em IFC. Zero token.
4. O `ifc_resumo.py` confere pavimentos, cômodos e áreas. Zero token.
5. Você diz *"o quarto 2 está pequeno, aumenta meio metro"*. O Claude muda **um número** no script, não a planta inteira. Quase zero token.

A planta fica melhor porque é paramétrica: muda um número e o desenho inteiro se ajusta, com as medidas certas. E "o mais perfeito possível" vem de rodar o script e conferir, não de o Claude acertar tudo de primeira no escuro.

> Lembre: uma planta para **construir** precisa de engenheiro ou arquiteto registrado (CREA/CAU). O que o setup faz é o estudo e o modelo; quem assina é o profissional.

## Qual parte o setup toma conta sozinho

| Você faz | O setup faz |
|---|---|
| Fala ou escreve o que quer | Ouve (Whisper local) e entende |
| — | Escolhe a IA certa pela regra do roteador |
| — | Roda os scripts, gera os arquivos, confere com os verificadores |
| Confirma o que muda algo (publicar, comprar, apagar) | Faz o resto e registra |
| Revisa o resultado na tela | Mostra pronto para aprovar |

O que **não** dá para largar 100% na mão do setup: a aprovação final. Um assistente que faz tudo sem conferir também faz besteira sem conferir. O setup foi montado para você só aprovar, não para você não olhar.

## Aplicar isso a tudo

A regra "peça o gerador, não o resultado" vale para quase tudo que você faz no setup. O que muda é o nome do gerador:

| Você quer | O caro (não faça) | O barato (o gerador) |
|---|---|---|
| Planta baixa | Claude desenhar em texto | Script de FreeCAD/Bonsai com medidas por parâmetro |
| Aula, prova, plano | Claude escrever tudo do zero toda vez | Fábrica de aulas a partir da ementa; Claude só revisa |
| Site de cliente | Claude gerar o site inteiro no chat | Kit de sites: modelo pronto, Claude ajusta o que muda |
| 50 questões, baralho Anki | Claude digitar uma a uma | Gerador a partir do YAML do livro |
| Orçamento, finanças | Claude somar no texto | Planilha ou `orcamento.py` que calcula sozinho |
| Documento repetido (contrato, laudo) | Reescrever cada vez | Modelo com campos; o script preenche |
| Resumo de aula gravada | Colar a transcrição toda no Claude | Whisper transcreve local; modelo local resume; Claude só a versão final |
| Dados de um app seu | Perguntar número por número | Script lê a API e devolve a tabela |

O padrão é sempre o mesmo: o Claude escreve **uma vez** a ferramenta que faz; a ferramenta roda **mil vezes** de graça. Quando algo vira repetição, isso é sinal de que falta um gerador — peça o gerador.

## Preciso dar todas as informações?

Não. Dar tudo de antemão gasta token (entra texto) e cansa você. O setup trabalha assim:

1. **Você dá o essencial** e o resto a IA **assume por padrão**, dizendo o que assumiu: *"assumi pé-direito 2,70 m, parede 15 cm, porta 80 cm — mude se quiser"*.
2. **Você corrige só o que está errado.** Uma frase de correção custa quase nada; a descrição completa custaria muito.
3. **A IA reúsa o que já sabe de você:** preferências salvas, a stack por problema (.NET, PostgreSQL), as regras do repositório e os seus projetos. Ela não pergunta de novo o que já está escrito no setup.

Então "criar da forma mais perfeita possível" não vem de você descrever tudo; vem de um primeiro rascunho com padrões sensatos, que você corrige em uma ou duas frases, rodando o gerador a cada ajuste. Isso é mais rápido, mais barato e dá um resultado melhor do que tentar acertar tudo na primeira descrição.

Quando um padrão se repete (sempre a mesma parede de 15 cm, sempre a mesma stack), peça para salvar nas suas preferências: a IA passa a assumir aquilo sozinha, e você nem precisa mais dizer.

## Por voz, por escrito ou de qualquer forma

A economia é a mesma nos três casos, porque o que conta é o texto que chega ao Claude, não como você falou:

- **Voz:** o Whisper transcreve local (zero token) e manda ao Claude só o texto curto do seu pedido.
- **Escrito:** frases curtas e diretas; o pacote de contexto entra no lugar de colar histórico.
- **Arquivo (foto, PDF, planta):** o setup extrai local (Docling, Whisper, `ifc_resumo.py`) e manda ao Claude só o resumo, não o arquivo inteiro.

## Contexto enxuto: o que o agente lê

A regra nº 4 (buscar, não colar) também vale para o próprio repositório. Quatro travas, todas grátis:

1. **O agente não lê lixo nem segredo.** Em todo repositório, `.claude/settings.json` com `permissions.deny` (modelo em `infra/templates/repo-padrao`): `node_modules`, `bin/obj`, lockfiles, logs, `.env` e `~/.ssh`. O Claude Code não usa arquivo `.claudeignore`; é essa regra que vale.
2. **Pacote de arquitetura em vez de "leia o repositório".** `just arquiteto "o pedido"` monta em cerca de 400 tokens a stack por problema, as regras, o que já existe e o que foi recusado. O Claude não precisa descobrir isso lendo tudo.
3. **Só a pasta que importa, comprimida.** Para colar no Claude do app: `just contexto-ia caminho/da/pasta` (Repomix com `--compress`, que guarda só assinaturas e tipos).
4. **Resposta seca.** O pacote já pede a resposta sem saudação nem resumo; token de saída custa mais que o de entrada.

Versão de modelo não se escreve em documento: fica no gateway LiteLLM e em [custos.md](../custos.md), porque muda a cada poucos meses.

## Ferramentas

```bash
python3 ~/dev/dev-setup/tools/ia/tokens.py rota "revisar a arquitetura do AM Kaixara"   # qual IA usar
python3 ~/dev/dev-setup/tools/ia/tokens.py tamanho aula.md                               # estima os tokens
python3 ~/dev/dev-setup/tools/ia/cabe.py 32                                              # cabe um modelo local?
just arquiteto "módulo de aporte do AM Rendara"                                          # pacote curto para o Claude
```

O teto de gasto real fica no gateway LiteLLM (`infra/ia`) e no ai-usagebar; a tabela de rotas por tarefa está em [recursos.md](../recursos.md) e em [custos.md](../custos.md). A regra nº 1 — pedir o script, não o resultado — vale para todo agente do setup e está nas regras da IA.
