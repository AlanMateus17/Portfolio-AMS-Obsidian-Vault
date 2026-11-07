# Porta única de comandos do setup (just: https://just.systems). Rode no Ubuntu do WSL, na pasta do repositório:
#   alanmateus@...$ cd ~/dev/dev-setup && just            # lista as receitas
# Cada receita só chama os scripts que já existem; nada aqui tem lógica própria.

set shell := ["bash", "-euo", "pipefail", "-c"]

# Lista as receitas
default:
    @just --list --unsorted

# Montar, colar ou construir: just triagem "atendimento no WhatsApp com fila"
triagem pedido *opcoes:
    python3 tools/triagem/triagem.py triar "{{pedido}}" {{opcoes}}

# Pacote de contexto para o Claude (só imprime, gasta zero token): just arquiteto "módulo de aporte do AM Rendara"
arquiteto pedido:
    python3 tools/triagem/triagem.py arquitetar "{{pedido}}"

# O mesmo pacote enviado ao Claude Code dentro da sandbox (gasta token do seu plano)
arquiteto-claude pedido:
    python3 tools/triagem/triagem.py arquitetar "{{pedido}}" | ai-jail claude -p

# Regenera toda a documentação a partir de data/
docs:
    python3 tools/gerar_docs.py
    python3 tools/implantacao/gerar.py
    python3 tools/portfolio/portfolio.py
    python3 tools/softwares/softwares.py
    python3 tools/kitsites/gerar.py
    python3 tools/custos/custos.py
    python3 tools/recursos/recursos.py
    python3 tools/investimentos/investimentos.py docs
    python3 tools/carreira/certificacoes.py
    python3 tools/negocios/gerar.py
    python3 tools/cockpit/gerar.py
    python3 tools/akita/akita.py docs
    python3 tools/vault/espelho.py --se-existir

# O portão antes de cada commit: dados, documentação gerada, testes e segredos (o mesmo que o CI confere)
check:
    python3 tools/gerar_docs.py --check
    python3 tools/implantacao/gerar.py --check
    python3 tools/portfolio/portfolio.py --check
    python3 tools/softwares/softwares.py --check
    python3 tools/kitsites/gerar.py --check
    python3 tools/custos/custos.py --check
    python3 tools/recursos/recursos.py --check
    python3 tools/investimentos/investimentos.py docs --check
    python3 tools/carreira/certificacoes.py --check
    python3 tools/negocios/gerar.py --check
    python3 tools/cockpit/gerar.py --check
    python3 tools/akita/akita.py docs --check
    python3 -m unittest discover -s tools -p "test_gerar_docs.py" -q
    for d in tools/*/; do if ls "$d"test_*.py >/dev/null 2>&1; then python3 -m unittest discover -s "$d" -q; fi; done
    if command -v gitleaks >/dev/null; then gitleaks git --no-banner -v . >/dev/null; else echo "gitleaks ausente: rode o bootstrap"; fi
    if command -v shellcheck >/dev/null; then shellcheck -S warning scripts/wsl/*.sh infra/automacao/*.sh infra/automacao/sql/*.sh; fi

# Roda o CI do GitHub Actions na sua máquina, sem push (precisa do Docker): just ci-local
ci-local:
    gh act -j check

# Contexto enxuto de uma pasta para colar numa IA: just contexto-ia tools/triagem
contexto-ia pasta:
    npx --yes repomix@latest --compress --include "{{pasta}}/**" --ignore "**/*.lock,**/node_modules/**" -o /tmp/contexto-ia.xml
    @echo "Pacote em /tmp/contexto-ia.xml"

# Pacote de contexto para começar uma conversa nova (cole no Claude)
conversa:
    python3 tools/sessao/contexto.py --inicio

# Mede antes de mudar de stack: just medir "python3 tools/gerar_docs.py --check"
medir comando:
    hyperfine --warmup 2 "{{comando}}"

# Confere o que está instalado no Ubuntu
verificar:
    bash scripts/wsl/verificar.sh

# Mostra o que o bootstrap instalaria, sem mudar nada
bootstrap-simular:
    bash scripts/wsl/bootstrap.sh --simular

# Escolhe a receita num menu com setas (gum)
menu:
    just "$(just --summary | tr ' ' '\n' | gum choose --header 'Qual receita?')"

# Desenha um diagrama D2 em SVG ao lado do arquivo: just diagrama docs/arquitetura-exemplo.d2
diagrama arquivo:
    d2 --layout elk "{{arquivo}}" "{{without_extension(arquivo)}}.svg"

# Monta a pasta cifrada da sala limpa (pede a senha do gocryptfs) e desmonta com just lab-fechar
lab-abrir:
    mkdir -p ~/dev/lab && gocryptfs ~/dev/lab-cifrado ~/dev/lab

lab-fechar:
    fusermount -u ~/dev/lab

# Sobe um serviço próprio pelo perfil: just servico forgejo
servico perfil:
    cd infra/soberania && docker compose --profile "{{perfil}}" up -d

# Monta o setup inteiro de uma vez (fase 0 do Núcleo): just instalar  ·  só ver: just instalar --simular
instalar *opcao:
    bash scripts/wsl/instalar-tudo.sh {{opcao}}

# Guarda algo na base do núcleo: just lembrar "Kamal na t4g precisa de arm64" licao
lembrar texto tipo="nota":
    python3 tools/nucleo/nucleo.py lembrar "{{texto}}" --tipo {{tipo}}

# Procura na base do núcleo (decisões, lições, triagens, garimpos): just buscar "deploy"
buscar texto:
    python3 tools/nucleo/nucleo.py buscar "{{texto}}"

# Tarefas abertas do núcleo
tarefas:
    python3 tools/nucleo/nucleo.py tarefa listar

# O que depende de você agora (passos manuais e decisões, na ordem): just agora  ·  just agora software
agora empresa="":
    python3 tools/nucleo/agenda.py agora {{ if empresa != "" { "--empresa " + empresa } else { "" } }}

# Só as decisões que são suas: just decisoes software
decisoes empresa="":
    python3 tools/nucleo/agenda.py decisoes {{ if empresa != "" { "--empresa " + empresa } else { "" } }}

# Marca passos ou fases inteiras como feitos: just feito kp-chave  ·  just feito f0
feito +ids:
    python3 tools/nucleo/agenda.py feito {{ids}}

# Quanto do roteiro já foi feito: just progresso  ·  just progresso software
progresso empresa="":
    python3 tools/nucleo/agenda.py progresso {{ if empresa != "" { "--empresa " + empresa } else { "" } }}

# Professor: just professor hoje | trilha | aula ID | praticei ID | prova ID | corrigir ID | ensinei ID | cartoes | ferramenta BLOCO
professor *args:
    python3 tools/professor/professor.py {{args}}

# Escola Akita: just akita sincronizar | indexar | fila | notar SLUG | lote | pendentes | aprovar ID | aplicar ID
akita *args:
    python3 tools/akita/akita.py {{args}}

# Site de uma marca (amtech, instituto, editora): just site amtech  ·  só pendências: just site instituto --checar
site *args:
    python3 tools/sites/novo_site.py {{args}}

# Copia o dev-setup para a pasta 11 do seu vault (o just docs já faz isso quando o vault existe)
vault-espelho *opcao:
    python3 tools/vault/espelho.py {{opcao}}

# Backup agora (o mesmo do agendamento das 22h30)
backup:
    bash scripts/wsl/backup.sh
