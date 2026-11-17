# 5 · Qualidade, erros e segurança

[← Motor de decisão](README.md)

Nenhum sistema zera erros e alucinações. O objetivo é pegar o erro antes de chegar ao Alan.

## As 6 peças anti-erro e anti-desperdício

1. **Catálogo único de capacidades** (evolução de `data/recursos.json`): cada ferramenta, agente, script e modelo com função, custo, limites e confiabilidade. A escada consulta; o garimpo procura nele e no GitHub antes de construir (contra reinventar a roda).
2. **Barreiras contra alucinação:** resposta só com o contexto recebido, citando arquivo, linha ou link; saída em schema; verificador independente (código ou outro modelo); "não sei" é válido; ação passa por simulação (`--simular`), é idempotente e tem volta.
3. **Limites para agentes e n8n:** permissão mínima, orçamento por tarefa (tokens, tempo, dinheiro), limite de tentativas, tempo máximo, botão de parar, execução isolada, portão humano para publicar, pagar ou falar com cliente.
4. **Ciclo de aprendizado:** todo erro vira teste ou regra no Núcleo (análise de 3 linhas); regra de três; consultar lições antes de cada tarefa.
5. **Registro de tudo:** cada decisão da escada (por que, custo, falha) e revisão semanal de 15 minutos.
6. **Mesma régua em todas as áreas:** "pronto para começar" e "pronto para entregar" com a mesma estrutura.

| Área | Checagem de pronto |
|---|---|
| Programação | Testes e CI passando |
| Sistemas | Arquitetura em ADR e revisada |
| Empreendedorismo | Validado com cliente real e uma métrica |
| Finanças | Cálculo em código testado e fonte do dado registrada |
| Aulas | Alinhada à ementa e à apostila |

Contra atraso: limite de frentes ativas, fila priorizada pela VEH, prazos com data. Nada é congelado: ideias novas entram a qualquer hora, e a ordem de execução respeita o limite de 3 frentes "agora".

## As 7 lacunas de sênior e a técnica de cada uma

| # | Lacuna | Técnicas e ferramentas (gratuitas) |
|---|---|---|
| 1 | Classificação dos dados | Rótulo público/interno/sensível; sensível só vai para IA local ou código; minimização; pseudonimização antes de IA online; detector por regex (CPF, e-mail, telefone) que bloqueia o envio. Proteção para LGPD |
| 2 | Injeção de prompt | Conteúdo externo é dado, nunca ordem; agente que lê conteúdo de fora não age; lista fixa de ferramentas por agente; saída em schema; aprovação humana |
| 3 | Código garimpado | SBOM com **Syft**; licenças com **ScanCode** (GPL pode obrigar a abrir o código do produto); vulnerabilidades com **Trivy** ou **OSV-Scanner**; análise estática com **Semgrep**; segredos com **gitleaks**; tudo em container antes de entrar |
| 4 | Pontos de falha | Tabela "se X cair, então Y"; plano B e modo degradado por peça; saída de fornecedor por adaptador; backup com teste de restauração periódico; desligar uma peça de propósito |
| 5 | Versões | Lock em tudo; **Renovate** ou Dependabot abrindo PRs; testes de regressão e modo sombra antes de trocar modelo ou prompt |
| 6 | Custo total real | **ActivityWatch** mede as horas; orçamento de manutenção dentro das 7 h semanais; automação que não se paga em 60 dias é desligada |
| 7 | Documentação para outra pessoa operar | ADRs, runbook por serviço (ligar, saber se quebrou, consertar), diagramas C4, docs versionadas junto do código |

Os itens 3 e 5 viram etapas do CI que bloqueiam o merge: ninguém, nem a IA, pula a checagem.
