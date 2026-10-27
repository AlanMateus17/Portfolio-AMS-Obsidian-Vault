# 0002 · Agentes de IA só dentro de sandbox

- **Status:** aceita
- **Data:** 2026-10-19

## Contexto

Agentes de código (Claude Code, Codex) executam comandos e editam arquivos. Um agente com acesso à máquina inteira pode ler chaves SSH, senhas ou arquivos pessoais. Ferramentas de agente com histórico de instâncias expostas foram descartadas.

## Decisão

Os agentes rodam no Ubuntu do WSL2 dentro do ai-jail, que libera só `~/dev/<projeto>` e o vault de estudo em modo leitura. Regras fixas de cada repositório ficam no `CLAUDE.md`. Acesso a GitHub e banco de dados passa por servidores MCP com permissão limitada (banco só leitura). Segredos ficam no KeePassXC e nunca entram no repositório.

## Consequências

- O agente não enxerga `~/.ssh`, o Windows nem outros projetos.
- Toda mudança chega como diff para revisão antes do commit.
- O ai-jail é uma camada a mais de proteção, não uma blindagem total; a revisão humana continua obrigatória.
