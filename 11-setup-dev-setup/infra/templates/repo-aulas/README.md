# aulas (repositório PRIVADO)

Esqueleto da Fábrica de aulas. Copiado do dev-setup (infra/templates/repo-aulas).

| Pasta | O que vai |
|---|---|
| `regras/` | `alan.toml`: suas regras (máximo de objetivos, fontes permitidas, o que é proibido). Cada correção sua vira uma linha |
| `ementas/` | Uma ementa por disciplina e turma (`.toml`, modelo em tools/fabrica/modelos) |
| `modelos-escola/` | Os modelos .docx que a escola exige, com campos `{{assim}}` |
| `aulas/` | Aulas geradas e revisadas, por disciplina e semana |
| `documentos/` | Planejamentos e guias preenchidos |

**Nunca entram aqui:** nomes, notas, fotos, vozes ou qualquer dado de aluno. Material de livros e cursos pagos também não.

Gerar o planejamento da semana 12:

```bash
python ~/dev/dev-setup/tools/fabrica/plano_semanal.py ementas/logica-1tec.toml regras/alan.toml 12 > /tmp/ctx.toml
python ~/dev/dev-setup/tools/fabrica/preencher.py modelos-escola/planejamento-semanal.docx /tmp/ctx.toml documentos/planejamento-s12.docx
```
