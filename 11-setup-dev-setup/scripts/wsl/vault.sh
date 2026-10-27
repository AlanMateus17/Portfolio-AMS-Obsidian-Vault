#!/usr/bin/env bash
# Cria o cofre do Obsidian em ~/dev/notas, organizado para estudar, guardar conhecimento e transformar em produto.
# Seguro para rodar várias vezes: não apaga nem sobrescreve nota sua.
#   bash scripts/wsl/vault.sh             # cria ou completa
#   bash scripts/wsl/vault.sh --simular   # mostra o que faria
#   bash scripts/wsl/vault.sh --pasta DIR
# No Windows, abra no Obsidian a pasta \\wsl.localhost\Ubuntu-24.04\home\SEU_USUARIO\dev\notas
set -euo pipefail

SIMULAR=0; V="$HOME/dev/notas"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --simular) SIMULAR=1 ;;
    --pasta) V="${2:?informe a pasta}"; shift ;;
    -h|--help) sed -n '2,8p' "$0"; exit 0 ;;
    *) echo "Opção desconhecida: $1" >&2; exit 64 ;;
  esac
  shift
done

feito=0
linha() { printf '%-10s %-42s %s\n' "$1" "$2" "$3"; }
pasta() {
  if [[ -d "$V/$1" ]]; then linha pasta "$1" "JA TEM"
  elif [[ $SIMULAR -eq 1 ]]; then linha pasta "$1" "CRIARIA"
  else mkdir -p "$V/$1"; linha pasta "$1" "CRIADA"; feito=$((feito + 1)); fi
}
arquivo() {  # arquivo <caminho> ; conteúdo pela entrada padrão. Nunca sobrescreve.
  local alvo="$V/$1" conteudo; conteudo="$(cat)"
  if [[ -e "$alvo" ]]; then linha arquivo "$1" "JA TEM"
  elif [[ $SIMULAR -eq 1 ]]; then linha arquivo "$1" "CRIARIA"
  else mkdir -p "$(dirname "$alvo")"; printf '%s\n' "$conteudo" > "$alvo"; linha arquivo "$1" "CRIADO"; feito=$((feito + 1)); fi
}

for p in "00-Entrada" "10-Estudos" "20-Aulas" "30-Acervo" "40-Produtos" "50-Projetos" "60-Conteudo" "90-Modelos" "99-Arquivo" "anexos"; do pasta "$p"; done

arquivo "00-INICIO.md" <<'EOF'
# Início

Como este cofre funciona, em uma frase por pasta:

- **00-Entrada**: tudo que chega sem pensar (ideia, link, anotação rápida). Esvazie uma vez por semana.
- **10-Estudos**: o que você aprendeu, com as suas palavras. Uma nota por conceito.
- **20-Aulas**: as aulas que você dá ou vai gravar.
- **30-Acervo**: os seus documentos antigos convertidos em Markdown pelo `acervo.py`. Não edite aqui; copie para 10 ou 20.
- **40-Produtos**: cada coisa que pode ser vendida, com o que falta para ir ao ar.
- **50-Projetos**: sistemas, livro e negócios.
- **60-Conteudo**: posts, roteiros e cortes antes de ir para a fila do pipeline.
- **90-Modelos**: modelos de nota (use Ctrl+P > "Inserir modelo").
- **99-Arquivo**: o que terminou.

Regra de ouro: o que você estuda vira nota em 10; a nota boa vira aula em 20; a aula vira produto em 40 e conteúdo em 60.
Tudo aqui é seu e pode alimentar a sua IA. Material de cursos e livros de terceiros fica só como referência (link e resumo com suas palavras).
EOF

arquivo "90-Modelos/Nota de estudo.md" <<'EOF'
---
tipo: estudo
tema:
fonte:
data: {{date}}
vira: [aula, post, questao]
---
# {{title}}

## Com as minhas palavras

## Exemplo que eu mesmo fiz

## Onde isso aparece (vaga, concurso, sistema AM)

## Perguntas para revisar (vão para o Anki)
- P:
  R:
EOF

arquivo "90-Modelos/Aula.md" <<'EOF'
---
tipo: aula
disciplina:
serie:
duracao: 50 min
data: {{date}}
---
# {{title}}

## Objetivo

## Roteiro (o que eu falo e mostro)

## Atividade

## Avaliação (questões com gabarito)

## O que dá para reaproveitar
- [ ] corte de vídeo
- [ ] carrossel
- [ ] questão para o banco de questões
- [ ] trecho do livro
EOF

arquivo "90-Modelos/Produto.md" <<'EOF'
---
tipo: produto
estagio: ideia   # ideia, validacao, construcao, lancamento, escala
preco:
canal:
origem:          # notas e documentos do acervo usados
---
# {{title}}

## Para quem é e que problema resolve

## O que já existe (links para 10, 20 e 30)

## O que falta para ir ao ar
- [ ] material revisado e sem dados de alunos
- [ ] direitos conferidos (nada de terceiros; material da escola reescrito)
- [ ] página de venda
- [ ] produto cadastrado na plataforma

## Próximo passo
EOF

arquivo ".gitignore" <<'EOF'
.obsidian/workspace*.json
.obsidian/cache
.trash/
.DS_Store
EOF

if [[ -d "$V/.git" ]]; then linha git "repositório" "JA TEM"
elif [[ $SIMULAR -eq 1 ]]; then linha git "repositório" "CRIARIA"
else git -C "$V" init -q && git -C "$V" add -A && git -C "$V" commit -qm "chore: estrutura do cofre" && linha git "repositório" "CRIADO"; feito=$((feito + 1)); fi

echo
if [[ $SIMULAR -eq 1 ]]; then echo "Simulação pronta."
else echo "Pronto ($feito item(ns) novos). Abra no Obsidian: \\\\wsl.localhost\\Ubuntu-24.04$(echo "$V" | tr '/' '\\')"; fi
