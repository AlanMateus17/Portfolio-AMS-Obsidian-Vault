# Regras extras para IA em projetos de construção, arquitetura e engenharia civil

Somam-se às regras gerais (`regras-ia.md`). Copie para o CLAUDE.md de cada repositório ou Project de construção.

## Quem assina
- Alan não é engenheiro civil nem arquiteto registrado. Nada sai como projeto pronto para obra, laudo, ART ou RRT.
- Todo dimensionamento (estrutura, fundação, instalações, incêndio) é estudo ou pré-dimensionamento e diz isso no topo:
  "Estudo, não é projeto: precisa de profissional habilitado (CREA/CAU) para revisão e assinatura".
- Trabalho para cliente só entra como apoio a um profissional responsável, que revisa e assina.

## Como calcular e citar
- Unidades do SI, com a unidade em cada número. Mostre a memória de cálculo passo a passo, nunca só o resultado.
- Norma citada com número e ano (ex.: ABNT NBR 6118:2023). Se não tiver certeza da versão em vigor, diga e mande conferir no catálogo da ABNT.
- Não invente coeficiente, tabela ou valor de norma: se não estiver na fonte que Alan forneceu, pergunte.
- Custos pelo SINAPI sempre com mês de referência, estado (MG) e se é desonerado ou não. Custo é estimativa até o orçamento do profissional.
- Confira cada resultado por um segundo caminho (ordem de grandeza, outro método, tabela prática) e diga se bateu.

## Material e dados
- Normas ABNT são pagas e protegidas: nada de PDF pirata em prompt, RAG ou treino. Use o texto que Alan comprou ou acessa pela escola, só para consulta.
- Pode usar livremente: NRs do Ministério do Trabalho, SINAPI, manuais da Caixa, documentos do governo (Estratégia BIM BR) e projetos com licença aberta.
- Planta, endereço, foto e documento de cliente são dados pessoais (LGPD): ficam fora da nuvem sem autorização.

## Arquivos
- Formato aberto primeiro: IFC para BIM, DXF para desenho 2D, CSV para planilhas. Formato proprietário só quando o profissional responsável pedir.
- Modelos e scripts versionados no Git; arquivos grandes (IFC, RVT) com Git LFS ou fora do repositório.
