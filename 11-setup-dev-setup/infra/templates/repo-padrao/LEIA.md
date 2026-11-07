# Repositório padrão AMtech

Copiado por `scripts/wsl/padronizar-repo.sh` (só cria o que falta, nunca sobrescreve).

- `.pre-commit-config.yaml`: higiene, segredos (gitleaks) e mensagem de commit no padrão Conventional Commits.
- `.github/workflows/qualidade.yml`: gitleaks, Trivy, Semgrep e testes em todo push.
- `.github/pull_request_template.md`: a Definition of Done.
- `docs/adr/`: decisões de arquitetura.
- `.editorconfig` e `CHANGELOG.md`.
- `.claude/settings.json`: o que o agente não pode ler (segredos, `node_modules`, `bin/obj`, logs, lockfiles, `~/.ssh`). O Claude Code não lê `.claudeignore`; quem vale são as regras `permissions.deny`. Economiza token e fecha a porta para o agente ver segredo.
