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

# Motor de decisão (ADR 0014): qual degrau da escada resolve o pedido, sem chamar IA: just motor "calcular o rateio"
motor pedido:
    python3 tools/motor/motor.py decidir "{{pedido}}"

# Registra o gasto de uma chamada de IA: just motor-custo claude sonnet --entrada 12000 --saida 1800 --usd 0.06
motor-custo ferramenta modelo *opcoes:
    python3 tools/motor/motor.py custo {{ferramenta}} {{modelo}} {{opcoes}}

# Marca se a decisão deu certo (alimenta a regra de três): just motor-ok 7   |   just motor-refazer 7
motor-ok id:
    python3 tools/motor/motor.py resultado {{id}} ok
motor-refazer id:
    python3 tools/motor/motor.py resultado {{id}} refazer

# Decisões por degrau, gasto e o que já pode virar script: just motor-relatorio
motor-relatorio:
    python3 tools/motor/motor.py relatorio

# Pacote de contexto para o Claude (só imprime, gasta zero token): just arquiteto "módulo de aporte do AM Gestão · Financeiro"
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
    python3 tools/editora/livros.py
    python3 tools/empresas/empresas.py
    python3 tools/kitsites/gerar.py
    python3 tools/custos/custos.py
    python3 tools/recursos/recursos.py
    python3 tools/investimentos/investimentos.py docs
    python3 tools/carreira/certificacoes.py
    python3 tools/negocios/gerar.py
    python3 tools/cockpit/gerar.py
    python3 tools/akita/akita.py docs
    python3 tools/biblioteca/biblioteca.py docs
    python3 tools/nucleo/agenda.py rapido --doc
    python3 tools/repos/repos.py
    python3 tools/vault/espelho.py --se-existir

# O portão antes de cada commit: dados, documentação gerada, testes e segredos (o mesmo que o CI confere)
check:
    python3 tools/gerar_docs.py --check
    python3 tools/implantacao/gerar.py --check
    python3 tools/portfolio/portfolio.py --check
    python3 tools/softwares/softwares.py --check
    python3 tools/editora/livros.py --check
    python3 tools/empresas/empresas.py --check
    python3 tools/coerencia/coerencia.py
    python3 tools/kitsites/gerar.py --check
    python3 tools/custos/custos.py --check
    python3 tools/recursos/recursos.py --check
    python3 tools/investimentos/investimentos.py docs --check
    python3 tools/carreira/certificacoes.py --check
    python3 tools/negocios/gerar.py --check
    python3 tools/cockpit/gerar.py --check
    python3 tools/akita/akita.py docs --check
    python3 tools/biblioteca/biblioteca.py docs --check
    python3 tools/nucleo/agenda.py rapido --check
    python3 tools/repos/repos.py --check
    python3 -m unittest discover -s tools -p "test_gerar_docs.py" -q
    for d in tools/*/; do if ls "$d"test_*.py >/dev/null 2>&1; then python3 -m unittest discover -s "$d" -q; fi; done
    if command -v gitleaks >/dev/null; then gitleaks git --no-banner -v . >/dev/null; else echo "gitleaks ausente: rode o bootstrap"; fi
    if command -v shellcheck >/dev/null; then shellcheck -S warning scripts/wsl/*.sh infra/automacao/*.sh infra/automacao/sql/*.sh os/instalar.sh os/amtech; fi

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

# AMtech OS: mostra o que o instalador faria (rode numa VM ou no Linux nativo; veja os/README.md)
os-simular perfil="dev":
    bash os/instalar.sh --perfil {{perfil}} --simular

# AMtech OS: transforma este Ubuntu no AMtech OS: just os-instalar dev "Alan Mateus" voce@exemplo.com
os-instalar perfil="dev" nome="" email="":
    bash os/instalar.sh --perfil {{perfil}} {{ if nome != "" { "--nome '" + nome + "'" } else { "" } }} {{ if email != "" { "--email " + email } else { "" } }}

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

# O caminho mais curto: o setup funcionando e as 3 empresas prontas para vender, em 7 sessões: just rapido  ·  just rapido --todas
rapido *opcao:
    python3 tools/nucleo/agenda.py rapido {{opcao}}

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

# Professor × mapa-de-estudo: regrava o retrato do MAPA.md e confere (campo etapa de cada módulo)
professor-mapa md="~/dev/mapa-de-estudo/MAPA.md":
    python3 tools/professor/mapa.py atualizar {{md}} && python3 tools/professor/mapa.py conferir

# Caderno de erros e atritos do setup (uma linha, sem abrir arquivo): just erro 0.2 "o erro" --certo "o certo" | just atrito "o que travou" --area backup
[positional-arguments]
erro *args:
    python3 tools/registro/registro.py erro "$@"

[positional-arguments]
erros *args:
    python3 tools/registro/registro.py erros "$@"

[positional-arguments]
atrito *args:
    python3 tools/registro/registro.py atrito "$@"

atritos:
    python3 tools/registro/registro.py atritos

# Diagnóstico antes de cada assunto (certo/errado + certeza 1 a 3): just diag 0.1 c3 x2 c1 --min 4
[positional-arguments]
diag *args:
    python3 tools/registro/registro.py diag "$@"

# Ficha do assunto (escreva uma vez, depois de estudar): just ficha 0.2
ficha etapa:
    python3 tools/colher/colher.py ficha {{etapa}}

# Entrega a ficha: capítulo no pipeline, exercícios no banco e no Anki, plano de aula no ensino-ti: just colher 0.2 [--seco] [--forcar]
[positional-arguments]
colher *args:
    python3 tools/colher/colher.py colher "$@"

# Biblioteca: just livros lista | para ETAPA | comprar | ler LIVRO --trecho T --min N --assunto ETAPA --nota "..." | lidos | marcar LIVRO tenho
[positional-arguments]
livros *args:
    python3 tools/biblioteca/biblioteca.py "$@"

# Recrutador: just recrutador semana | entrevista FORMATO [--empresa X] [--vaga arq.txt] [--claude] | registrar FORMATO NOTA | progresso
recrutador *args:
    python3 tools/recrutador/recrutador.py {{args}}

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

# Liga o setup para o celular (Ollama, modelos, aider, LiteLLM, fila, bot, Remote Control): just ligar  ·  só ver: just ligar --simular
ligar *opcao:
    bash scripts/wsl/ligar-tudo.sh {{opcao}}

# O que está no ar agora (serviços, Ollama, LiteLLM, últimos pedidos)
ligado:
    bash scripts/wsl/ligar-tudo.sh --status

# Para os serviços do celular (não desinstala nada)
desligar:
    bash scripts/wsl/ligar-tudo.sh --desligar

# Manda um pedido para a fila (o mesmo do /pedir no Telegram): just pedir "@catalogo-html corrigir o menu"
pedir texto:
    python3 tools/remoto/fila.py adicionar "{{texto}}"

# Pedidos da fila e se o Claude está em pausa por limite
fila:
    python3 tools/remoto/fila.py listar

# Vitrine para clientes: copia docs/vitrines/EMPRESA.md como README do repositório público da empresa (ex.: just vitrine software ~/dev/amtech-software)
vitrine EMPRESA DESTINO:
    test -f docs/vitrines/{{EMPRESA}}.md && test -d {{DESTINO}}/.git && cp docs/vitrines/{{EMPRESA}}.md {{DESTINO}}/README.md && echo "README da vitrine copiado; revise, faça o commit e o push em {{DESTINO}}"

# Coerência com o plano (data/coerencia.json): confere o dev-setup e todos os repositórios em ~/dev e grava ~/dev/COERENCIA.md
# just coerencia            (só relatório)     just coerencia --corrigir     (troca sozinho o que tem troca segura)
coerencia *opcao:
    python3 tools/coerencia/coerencia.py . $(find ~/dev -maxdepth 2 -name .git -type d -printf '%h ' 2>/dev/null) --relatorio ~/dev/COERENCIA.md {{opcao}} || true
    @echo "Leia ~/dev/COERENCIA.md: arquivo por arquivo, o que atualizar"
