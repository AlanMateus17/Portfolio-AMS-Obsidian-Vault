# CONTINUAR: contexto para qualquer conversa nova

> Instalação no notebook feita por outra conta ou conversa: use [docs/implantacao/INSTALACAO-AUTONOMA.md](docs/implantacao/INSTALACAO-AUTONOMA.md).

Cole este arquivo na primeira mensagem de uma conversa nova (ou rode `python3 ~/dev/dev-setup/tools/sessao/contexto.py --inicio | clip.exe`). Decisões do dia a dia vão para o ESTADO.md; este arquivo muda quando algo grande muda. Última revisão: 20/11/2026 (v2.35, realidade pós-13/11).

**Fonte da verdade:** `PLANO-UNICO-AMtech.md` no vault (`~/dev/notas`). Se este arquivo divergir dele, vale o PLANO-UNICO e este arquivo é corrigido. O que fazer hoje: `CARTAO-voce-esta-aqui.md` no vault, até o `just professor hoje` estar de pé.

## 1. Quem sou e como trabalhar comigo
- Alan Mateus, Barbacena-MG. Professor de informática (EMTI, Técnico em Informática e em Desenvolvimento de Sistemas), trabalha à noite num restaurante, cursa Licenciatura em Matemática. Fundador da Grupo AMtech.
- **Norte:** desenvolvedor sênior que cria IA e entende de dinheiro, com a Grupo AMtech como veículo. **Regra única:** todo estudo constrói um ativo que gera renda e vira portfólio. **Foco:** um ativo sendo construído + um sendo testado por vez.
- Seja direto e honesto: diga quando algo não é possível ou não vale a pena.
- Comandos de UMA linha, sempre dizendo ONDE rodar: PowerShell do Windows (PS C:\>) ou Ubuntu do WSL (alanmateus@...$).
- Nunca peça, leia ou guarde senhas, tokens, chaves, códigos de recuperação ou a chave do BitLocker. Segredos só no KeePassXC.
- Nada de dado de aluno (nome, nota, foto, voz) em IA. Nada publicado ou enviado em meu nome sem aprovação. Nenhuma conta nova sem mim.
- Não é assessoria financeira: aplique as MINHAS regras; a decisão é minha. Documentos financeiros pessoais não vão para o GitHub nem para IA na nuvem.
- Commits terminam com as linhas de coautoria do Claude e da sessão. Merge na `main` é meu: trabalhe em ramo e abra PR em rascunho.
- Uma conversa = uma tarefa. Termine me dando até 5 linhas para o ESTADO.md.

## 2. Onde está tudo
- **dev-setup** (este repositório, **público** desde nov/2026): github.com/AlanMateus17/dev-setup; no PC em `~/dev/dev-setup`. Por ser público: nada de segredo, dado pessoal, financeiro ou de aluno aqui; o que é privado fica em `~/.config/amtech`, `~/financas` e no KeePassXC.
- **Vault do Obsidian** (`~/dev/notas`, repositório Portfolio-AMS-Obsidian-Vault): PLANO-UNICO, CARTÃO, `07-estudo-e-carreira/PLANO-PASSO-A-PASSO.md` (o plano de estudo, ADR 0018). A pasta 11 é espelho do setup e **não se edita à mão** (`just vault-espelho`).
- **mapa-de-estudo** (público, `~/dev/mapa-de-estudo`): `MAPA.md` com tudo o que se estuda em etapas por pré-requisito (0 a 8 + horizonte H1–H7) e os arquivos de assunto conferidos. Cada módulo do Professor aponta para um assunto do mapa (campo `etapa`; `just professor-mapa` confere).
- Outros repositórios e o status de cada um (ativo, estudo, revisar, arquivar): `data/repos.json`.
- **Mudou uma decisão?** Primeiro edite `data/coerencia.json` (objetivo, decisões e termos velhos); depois `just coerencia` mostra, em todos os repositórios, o que ficou desatualizado, e `just coerencia --corrigir` troca o que é seguro. O CI do dev-setup falha se algum texto contradisser o plano.
- **Regra do repositório:** `data/*.json` → geradores → `docs/`. Nunca editar arquivo gerado. Toda mudança: dados ou ferramenta, geradores, testes, `just check` verde, CHANGELOG, linha no ESTADO.md, PR.

## 3. Decisões que valem hoje
- **Stack (ADR 0017, 13/11):** núcleo **TypeScript + Python + SQL**. TypeScript + Next.js + PostgreSQL (Supabase) para web, SaaS e sites; Python para dados, IA e finanças; Go para CLIs e o agente fiscal do PDV; C/C++ e Rust pela trilha de SO e robótica. **.NET sai do centro** e vira carta de reserva (só se um emprego ou cliente pagar).
- **Produto único: AM Gestão** (ADR 0017): uma suíte que junta 3 ou mais sistemas no lugar dos 23 sistemas soltos. MVP = PDV (vem do Kaixara) + Pedidos (do Rotara) + Financeiro (do Rendara); loja online depois. Começa pela **planilha do financeiro**. Com o MVP pronto, é vendido em **pacotes** (Caixa, Caixa + Financeiro, Integrado, Integrado + Loja). "AM Gestão · Financeiro" como produto separado não existe mais.
- **Os outros sistemas também viram suítes** (20/11), cada uma com 3 ou mais sistemas e vendida em pacotes, uma por vez, só depois da anterior vender: AM Serviços (agenda, assistência, veterinária), AM Escola (educacional, AM Mentor, plataforma do Instituto, fábrica de documentos), AM Projetos (Kanban, obras, diagnóstico por IA). Condomínios e o app de casais ficam fora, para decidir. Tudo em [docs/operacao/softwares.md](docs/operacao/softwares.md).
- **Plano de estudo único (ADR 0018, 17/11):** a fonte é o PLANO-PASSO-A-PASSO do vault; o Professor segue a rotina real (seg/qua ofício e setup, ter base do Akita, qui bloco profundo, sex matemática, sáb ofício leve e física, domingo folga), ~20 h por semana; 4 h por dia é bônus, nunca dívida. O calendário começou em 17/11/2026 e anda ~2 semanas.
- **Mapa de estudo:** o que estudar e em que ordem está no `MAPA.md`; o calendário (quando) está no vault. Um assunto só entra quando o arquivo dele estiver escrito e conferido.
- **Trilhas ativas** (PLANO-UNICO §3): fundamentos e engenharia, web TS, Python/dados/IA (T3–T4), finanças F0–F3, matemática, física leve, inglês, robótica/IoT, sistema operacional (Linux, AMtech OS), Go, baixo nível leve. Na fila: redes, finanças F4–F8, segurança, economia, agro e construção.
- **Seis empresas no Grupo AMtech Digital** (marcas no plano; CNPJ só quando cada uma faturar), cada uma com produtos principais que juntam componentes e são vendidos em pacotes, como o AM Gestão: AMtech Software, Instituto AMS Silva e AMtech Mídia ativas; Editora AMS Silva pausada; **AMtech Maker** (robótica, automação, serviços presenciais e a loja, juntando o antigo Campo) e **AM Logística** como software primeiro, empresa depois. Patrimônio é finança pessoal. Tudo em [docs/empresas.md](docs/empresas.md); o que mostrar ao cliente, em [docs/vitrines](docs/vitrines/README.md).
- **Sequência:** 1) mini-curso de Lógica, planilha do AM Gestão e Primer Code; 2) MVP do AM Gestão em 1 restaurante, Anki e AM Mentor, Bancada Dev; 3) pacotes do AM Gestão, Udemy, canal de finanças (a AM Logística fase 1 já é o Pedidos); 4) AM Serviços e Maker Digital; depois Editora e as fases físicas, só no gatilho.
- **Restaurantes próprios saíram do plano (20/11):** sushi, cafeteria, padaria e aula de sushi; também mercadinho autônomo, máquina de lanches e revenda de veículos. Ficam Loja (assistência e ponto de retirada), AM Entregas e AM Delivery ([docs/negocios](docs/negocios/README.md)).
- **Editora pausada, livros em estruturação:** *Lógica e Máquina* em 6 volumes, cada capítulo ligado a um assunto do mapa-de-estudo e **escrito por mim a partir das minhas notas** (a ficha do assunto); o mapa é referência, não texto ([docs/editora/livros.md](docs/editora/livros.md)).

## 4. Rendas: passivas × ativas (decisão de 18/11)
Só **rendas passivas** entram no plano, em ondas; a onda seguinte entra quando uma da atual passar no portão (3 meses se pagando). Rendas **ativas** ficam fora das ondas (atendem o que chegar, sem prospectar). Tudo em `data/portfolio.json` (campos `tipo` e `onda`) e em [docs/operacao/portfolio.md](docs/operacao/portfolio.md).
- **Onda 0 (agora, máximo 4):** mini-curso de Lógica, canais sem rosto, planilha do AM Gestão, catálogo do HTML.
- **Os 3 canais sem rosto:** **Primer Code** (lógica e programação), **Bancada Dev** (setup e ferramentas) e um canal de finanças com **nome a definir** (Bolso Exato está ocupado).
- **Onda 1:** Anki, templates, modelos financeiros, calculadoras, Udemy, afiliados.
- **Onda 2:** monetização das plataformas, newsletter, AM Mentor, simulados, aulas prontas para professores, fábrica de documentos para professores, dublagem, templates em inglês, UI kits, canal em público.
- **Onda 3:** AM Gestão SaaS (Kaixara e Rotara), formação técnica, comunidade, livro, camisetas, dividendos.
- **Ativas, fora das ondas:** sites, aulas particulares, sistemas sob encomenda, laudo de segurança de sites, entre outras. **Descartada:** avaliação de respostas de IA (só rendas passivas).

## 5. Comandos do dia a dia (Ubuntu, em `~/dev/dev-setup`)
- `just` lista tudo; `just check` antes de todo commit; `just verificar` confere a instalação; `just ligado` mostra o que está no ar.
- Estudo: `just professor hoje`, `just diag ETAPA ...`, `just ficha ETAPA`, `just colher ETAPA`, `just livros ...`, `just erro ETAPA "..." --certo "..."`, `just atrito "..."`.
- Progresso: `just rapido` (trilha rápida da instalação), `just agora` (o que é seu agora), `just feito ID`.
- Contexto para outra conversa: `python3 tools/sessao/contexto.py --inicio | clip.exe` ou `--passo ID`.

## 6. Como pedir ajuda numa conversa nova
1. Cole este arquivo e, se for um passo do roteiro, o pacote dele (`contexto.py --passo ID`).
2. Peça ao Claude para abrir os repositórios dev-setup, mapa-de-estudo e o vault (GitHub conectado).
3. Se algo daqui contradisser o PLANO-UNICO, o CARTÃO ou o PLANO-PASSO-A-PASSO, vale o vault: corrija aqui por PR.
