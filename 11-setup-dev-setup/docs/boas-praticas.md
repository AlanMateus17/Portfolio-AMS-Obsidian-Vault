<!-- Escrito à mão. Guia de boas práticas que vale para TODOS os repositórios do grupo. -->

# Boas práticas em todo repositório, versão e arquivo

[← Índice da documentação](README.md)

O que fazer em qualquer repositório seu para o setup se manter profissional. Muito já está pronto no repositório padrão (`infra/templates/repo-padrao`) e na fase "Padrão de elite" do roteiro; isto reúne tudo num lugar e completa o que falta.

## Git e versões

- **Um commit por mudança, com mensagem no padrão Conventional Commits:** `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`. A mensagem diz o *porquê*, não só o *o quê*.
- **Versão semântica (SemVer) `x.y.z`:** `z` para correção, `y` para novidade compatível, `x` para mudança que quebra. Cada versão vira uma seção no `CHANGELOG.md`.
- **Tags marcam cada versão:** `tools/git/taguear.py --criar --push` cria as tags de todas as versões do CHANGELOG de uma vez (precisa do histórico completo e da sua máquina).
- **Tag automática a cada push:** o hook `scripts/git-hooks/pre-push` cria e envia a tag da versão atual sozinho (ligue com `git config core.hooksPath scripts/git-hooks`). Backfill das versões antigas, uma vez: `tools/git/taguear.py --criar --push` após `git fetch --unshallow`.
- **Branch `main` sempre verde:** nada entra sem o CI passar. Trabalho novo em branch próprio, juntado por Pull Request.
- **Proteja a `main` no GitHub:** exigir CI verde e revisão antes de juntar (já é o passo `protecao-main`).
- **Histórico limpo:** nada de arquivo gerado, binário grande ou segredo no commit. Arquivo grande vai para o Git LFS ou fica fora.

## Segredos e segurança

- **Nenhum segredo no repositório, nunca.** Senha, token e chave ficam no KeePassXC e entram por variável de ambiente.
- **gitleaks no pre-commit e no CI:** barra segredo antes de virar commit (já no repo-padrão).
- **Dependabot e CodeQL ligados:** atualizam pacote vulnerável e procuram falha no código.
- **`.gitignore` e `.env.example`:** o `.env` real nunca sobe; o exemplo sim, para quem for rodar.

## Qualidade do código

- **Testes automatizados** para toda ferramenta, e o CI roda a cada push (o seu repositório já faz isso).
- **Uma fonte da verdade:** dados em `data/`, a documentação é gerada; nunca edite o arquivo gerado.
- **Análise estática no CI:** Semgrep (código), ShellCheck (scripts) e PSScriptAnalyzer (PowerShell), que você já usa.
- **`.editorconfig`** para o mesmo estilo em qualquer editor.
- **Formato aberto primeiro:** JSON, CSV, Markdown, IFC, DXF — nada preso a um programa só.

## Documentação e organização

- **README em todo repositório:** o que é, como rodar, como testar.
- **ADR para decisão importante** (`docs/adr`): o que foi decidido e por quê, para o "eu do futuro" entender.
- **CHANGELOG sempre atualizado** na mesma mudança que alterou o código.
- **Nomes e pastas consistentes** entre os repositórios, saindo do repo-padrão.

## Backup e continuidade

- **Backup 3-2-1, testado:** 3 cópias, 2 mídias, 1 fora de casa — e a restauração conferida todo mês (`el-restauracao`). Backup não testado não conta.
- **O dev-setup é a memória:** o pacote de contexto e o ESTADO.md mantêm o fio entre as conversas.

## Dados pessoais e licenças

- **LGPD:** dado de aluno e de cliente não vão para IA na nuvem nem para repositório público.
- **Licença em todo repositório** (um `LICENSE`): decide o que os outros podem fazer com o seu código.
- **Respeite a licença dos outros:** nada de norma da ABNT, curso pago ou código de terceiro sem licença no setup.

## O mínimo para um repositório novo começar certo

1. `bash scripts/wsl/padronizar-repo.sh` aplica o repo-padrão (CI, pre-commit, .gitignore, .editorconfig, templates).
2. Primeiro commit com `chore: setup inicial` e a `main` protegida no GitHub.
3. README, LICENSE e CHANGELOG na raiz.
4. Segredos no KeePassXC, `.env.example` no repositório.
