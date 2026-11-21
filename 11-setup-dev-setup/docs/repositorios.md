<!-- Arquivo GERADO por tools/repos/repos.py a partir de repos.json. Não edite à mão. -->

# Repositórios do Alan Mateus

Tudo o que existe no GitHub e o que vai ser criado, por empresa, com o papel, o status e a visibilidade de cada repositório. Fonte: [`repos.json`](../repos.json); o plano em si está no `PLANO-UNICO-AMtech.md` do vault.

**Núcleo da stack:** TypeScript, Python, SQL. **Reserva:** Go, C#/.NET.

| Status | Quantos |
|---|---:|
| Planejados: criar quando a vez chegar | 10 |
| Ativos: em uso agora | 6 |
| Estudo: material e exercícios | 1 |
| A revisar: decidir se mantém ou funde | 3 |
| Arquivar: estudo concluído | 2 |

## Por empresa

| Empresa | Repositório | Para que serve | Status | Visibilidade |
|---|---|---|---|---|
| Grupo (operação e estudo) | [dev-setup](https://github.com/AlanMateus17/dev-setup) | Setup e operação (o cérebro): ferramentas, IAs, Professor, recrutador, rendas e ADRs | ativo | privado |
| Grupo (operação e estudo) | [Portfolio-AMS-Obsidian-Vault](https://github.com/AlanMateus17/Portfolio-AMS-Obsidian-Vault) | Vault de planejamento e estudo; fonte da verdade do plano (PLANO-UNICO) e da stack | ativo | privado |
| Grupo (operação e estudo) | [mapa-de-estudo](https://github.com/AlanMateus17/mapa-de-estudo) | Material de estudo: MAPA em etapas por pré-requisito e um arquivo conferido por assunto (o que estudar e em que ordem); o calendário fica no vault | ativo | privado |
| AMtech Software | [am-gestao](https://github.com/AlanMateus17/am-gestao) | O AM Gestão: um repositório, um módulo por componente (Caixa, Pedidos, Financeiro, Loja) | planejado | privado |
| AMtech Software | [amtech-software](https://github.com/AlanMateus17/amtech-software) | Vitrine para clientes da AMtech Software (README gerado de docs/vitrines/software.md) | planejado | público |
| Instituto AMS Silva | [ensino-ti](https://github.com/AlanMateus17/ensino-ti) | Material de ensino: cursos EMTI (Técnico em Informática e em Desenvolvimento de Sistemas) e a versão online | ativo | privado |
| Instituto AMS Silva | [catalogo-html](https://github.com/AlanMateus17/catalogo-html) | Site didático de HTML/CSS/JS para os alunos criarem e publicarem os próprios sites | ativo | público (GitHub Pages) |
| Instituto AMS Silva | [catalogo-plataforma](https://github.com/AlanMateus17/catalogo-plataforma) | Plataforma de contas, planos e vendas do curso do Catálogo do HTML (ASP.NET). Candidata a virar a plataforma de cursos do Instituto (AM Escola) ou ser reescrita em TypeScript | revisar | privado |
| Instituto AMS Silva | [codigo-c-](https://github.com/AlanMateus17/codigo-c-) | O nome diz C, mas hoje só tem 3 PDFs de aula (Aula 21 de Lógica e de SO, prática de sensores), sem código. Proposta: levar os PDFs para o ensino-ti e arquivar | revisar | privado |
| Instituto AMS Silva | [trilha-logica](https://github.com/AlanMateus17/trilha-logica) | O mini-curso de Lógica e os exercícios da Trilha Lógica | planejado | privado |
| Instituto AMS Silva | [instituto-ams-silva](https://github.com/AlanMateus17/instituto-ams-silva) | Vitrine para clientes do Instituto AMS Silva | planejado | público |
| AMtech Mídia | [ebooks_financas](https://github.com/AlanMateus17/ebooks_financas) | Material de finanças. Insumo para infoprodutos | estudo | privado |
| AMtech Mídia | [amtech-midia](https://github.com/AlanMateus17/amtech-midia) | Vitrine para clientes e patrocinadores da AMtech Mídia | planejado | público |
| AMtech Maker | [maker-automacoes](https://github.com/AlanMateus17/maker-automacoes) | Automações prontas e projetos de robótica do Maker Digital | planejado | privado |
| AMtech Maker | [amtech-maker](https://github.com/AlanMateus17/amtech-maker) | Vitrine para clientes da AMtech Maker | planejado | público |
| AM Logística | [am-logistica](https://github.com/AlanMateus17/am-logistica) | Vitrine para clientes da AM Logística | planejado | público |
| Editora AMS Silva | [logica-e-maquina](https://github.com/AlanMateus17/logica-e-maquina) | O livro Lógica e Máquina como repositório (texto, exercícios, figuras e pipeline) | planejado | privado |
| Editora AMS Silva | [editora-ams-silva](https://github.com/AlanMateus17/editora-ams-silva) | Vitrine da Editora AMS Silva | planejado | público |
| Pessoal | [AlanMateus17.github.io](https://github.com/AlanMateus17/AlanMateus17.github.io) | Site pessoal e portfólio. Migrar de Jekyll para a stack própria (Next.js) quando chegar a vez | ativo | público (GitHub Pages) |
| Pessoal | [instala-o-do-S.O-windows-pendrive](https://github.com/AlanMateus17/instala-o-do-S.O-windows-pendrive) | Repositório vazio, sem nenhum commit. Proposta: arquivar ou apagar (decisão do Alan) | revisar | privado |
| Pessoal | [desafio-cadastro-das-cartas-no-super-trunfo-AlanMateus17](https://github.com/Cursos-TI/desafio-cadastro-das-cartas-no-super-trunfo-AlanMateus17) | Fork de desafio de curso (C). Estudo concluído | arquivar | privado |
| Pessoal | [desafio-batalha-naval-AlanMateus17](https://github.com/Cursos-TI/desafio-batalha-naval-AlanMateus17) | Fork de desafio de curso (C). Estudo concluído | arquivar | privado |

## Produto único: AM Gestão

Ainda sem repositório próprio (nasce no trimestre 2 do plano).

- **Módulos:** Caixa/PDV (era Kaixara), Pedidos/Entrega (era Rotara), Financeiro (era Rendara), Loja online (Vendra)
- **MVP:** Caixa, Pedidos, Financeiro
- **Stack:** TypeScript (Next/NestJS), Python/FastAPI, PostgreSQL (Supabase), SQLite offline, Go/C# (agente fiscal)
