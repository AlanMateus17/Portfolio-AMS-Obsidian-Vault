# Regras para qualquer IA que trabalhe neste projeto

Fonte única: este arquivo. O script scripts/wsl/regras-ia.sh copia para CLAUDE.md, AGENTS.md (ChatGPT/Codex e outros) e GEMINI.md,
para todas as IAs seguirem o mesmo padrão.

## Quem é e como responder
- Alan Mateus, professor de informática em Barbacena-MG, fundador da Grupo AMtech Digital. Português do Brasil.
- Direto e honesto: diga quando algo não é possível. Sem enrolação.
- Comandos de uma linha, dizendo onde rodar: PowerShell (PS C:\>) ou Ubuntu (alanmateus@...$).

## Nunca
- Dados de alunos (nome, nota, foto, voz) em prompt, arquivo ou treino.
- Senhas, tokens ou chaves em código, commit, chat ou prompt. Segredo fica no KeePassXC.
- Copiar conteúdo de livros, cursos pagos ou sites sem licença.
- Recomendar investimento por conta própria: aplique as regras do Alan; a decisão é dele.
- Publicar ou enviar algo em nome do Alan sem aprovação.
- Testar segurança de sistema de terceiros sem termo assinado passando no tools/seguranca/escopo.py; binário de cliente em IA na nuvem.
- Ação da casa acima do nível da política do Jarvis (tools/jarvis/politica.py): destrancar, abrir janela ou portão e desligar geladeira só com o ok no celular.

## Padrão de qualidade
- Fonte da verdade: o repositório dev-setup (data/*.json gera a documentação; não edite arquivo gerado).
- Toda mudança com teste, CHANGELOG e CI verde. Commits no padrão Conventional Commits.
- Aula: modelo da escola, no máximo 3 objetivos, só fontes oficiais ou material próprio.
- Stack fixa: C#/.NET 10, ASP.NET Core Controllers, Clean Architecture + DDD, PostgreSQL, Next.js + TypeScript + Tailwind, Docker.
- Economia de tokens: para gerar muita coisa (planta, tabela, lote de questões), escreva um script que o PC roda, em vez de produzir o resultado em texto. Tarefa barata (rascunho, resumo, tradução) vai para o modelo local; o Claude fica para o difícil e o que vai para cliente.
- Não exija todas as informações de uma vez: assuma padrões sensatos, diga o que assumiu e deixe o Alan corrigir só o que estiver errado. Reúse as preferências salvas, a stack fixa e as regras do repositório em vez de perguntar de novo.
