# Estudo, normas e dados

[← Construção](README.md)

## Trilha de conceitos, na ordem

O objetivo é você dominar os conceitos; o setup cuida de ferramenta, arquivo e conta.

| # | Bloco | O que dominar | Prática no setup |
|---|---|---|---|
| 1 | Desenho técnico e leitura de projeto | Escalas, vistas, cortes, cotas, convenções de arquitetura | Redesenhar uma planta pronta no FreeCAD |
| 2 | BIM e formato aberto | O que é IFC, níveis de informação, ISO 19650, classificação NBR 15965 | Casa térrea simples no Bonsai e o `ifc_resumo.py` |
| 3 | Materiais e técnicas construtivas | Concreto, alvenaria, aço, madeira, impermeabilização | Caderno no Obsidian com fotos de obra (só de obra sua ou com permissão) |
| 4 | Mecânica e estruturas | Estática, resistência dos materiais, análise matricial | PyNite e FreeCAD FEM numa viga e num pórtico; a sua Licenciatura ajuda aqui |
| 5 | Instalações | Elétrica de baixa tensão, água fria e quente, esgoto, incêndio | Modelar as instalações da casa do bloco 2 |
| 6 | Conforto e desempenho | Térmico, acústico, iluminação, desempenho habitacional | EnergyPlus numa sala |
| 7 | Orçamento e planejamento | Composições, SINAPI, BDI, cronograma físico-financeiro | Estimativa da casa com o SINAPI-MG do mês |
| 8 | Legislação e segurança | Código de obras e plano diretor de Barbacena, NR-18, responsabilidade técnica | Ficha de quem assina o quê |

## Normas que importam

As normas da ABNT são **pagas e protegidas por direito autoral**: compre as que usar ou acesse pelo convênio de uma instituição, e não ponha PDF pirata em lugar nenhum do setup. Confira sempre a versão em vigor no catálogo da ABNT antes de citar.

| Tema | Norma |
|---|---|
| Representação de projetos de arquitetura | ABNT NBR 6492 |
| Acessibilidade | ABNT NBR 9050 |
| Desempenho de edificações habitacionais | ABNT NBR 15575 |
| Concreto armado | ABNT NBR 6118 |
| Cargas | ABNT NBR 6120 |
| Fundações | ABNT NBR 6122 |
| Estruturas de aço | ABNT NBR 8800 |
| Instalações elétricas de baixa tensão | ABNT NBR 5410 |
| Água fria e quente | ABNT NBR 5626 |
| Esgoto sanitário | ABNT NBR 8160 |
| Custo unitário básico (CUB) | ABNT NBR 12721 |
| Classificação da informação da construção (BIM) | ABNT NBR 15965 |
| Gestão da informação em BIM | ISO 19650 |
| Segurança na construção | NR-18 (pública, do Ministério do Trabalho) |
| Trabalho em altura | NR-35 (pública) |

O governo federal tem a Estratégia BIM BR (Decreto 11.888/2024) e uma cartilha para implantar BIM na administração pública: ambos públicos e bons para estudo.

## Conteúdo para estudar (grátis e com licença)

- Documentação do FreeCAD e do Bonsai, e a comunidade OSArch (BIM aberto).
- buildingSMART: a especificação do IFC e arquivos de exemplo.
- Autodesk Education: cursos e projetos de exemplo junto da licença educacional.
- MIT OpenCourseWare: mecânica dos sólidos e análise estrutural.
- Caixa: manuais e cadernos técnicos do SINAPI.
- Cartilha de BIM na administração pública (gov.br) e o plano de trabalho da Estratégia BIM BR.

## O que pode alimentar a IA do setup

| Pode entrar no RAG e nos Projects | Não entra |
|---|---|
| Suas anotações e resumos com suas palavras | PDF de norma da ABNT, comprada ou não (consulta sim, base da IA não) |
| SINAPI, NRs, cartilhas e decretos públicos | Livros e cursos pagos |
| Modelos e scripts seus | Planta, endereço e foto de cliente sem autorização |
| Arquivos IFC de exemplo com licença aberta | Projeto de terceiro achado na internet |

As regras completas que a IA segue estão em [`infra/templates/regras-ia/construcao.md`](../../infra/templates/regras-ia/construcao.md).

## Fontes

- [Bonsai 0.8.5 (OSArch)](https://osarch.org/2026/04/17/bonsai-0-8-5-released/) · [FreeCAD 1.1 (OSArch)](https://osarch.org/2026/03/25/freecad-1-1-released/)
- [Autodesk Education](https://www.autodesk.com/education/home-ew-edu-home-b)
- [Tabela SINAPI 2025 (OrçaFascio)](https://www.orcafascio.com/papodeengenheiro/tabela-sinapi-2025)
- [Speckle (AEC Magazine)](https://aecmag.com/data-management/speckle-the-open-source-cloud-data-platform/)
- [Decreto 11.888/2024 (Câmara)](https://www2.camara.leg.br/legin/fed/decret/2024/decreto-11888-22-janeiro-2024-795274-norma-pe.html) · [Cartilha BIM na administração pública](https://bimforum.org.br/wp-content/uploads/2026/06/Cartilha-Orientacao-para-implementacao-BIM-na-administracao-publica.pdf) · [Plano de trabalho da Estratégia BIM BR 2025–2027](https://www.gov.br/obrasgov/pt-br/estrategia-bim-br/plano-de-trabalho-da-estrategia-bim-br-2025-2027)
