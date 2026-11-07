# Software e ferramentas

[← Construção](README.md)

Regra do setup: formato aberto (IFC) no centro, software aberto onde ele já é bom, e o software comercial dos escritórios pela licença educacional, para estudar no mesmo programa que o mercado usa.

## Modelagem e BIM

| Ferramenta | Para quê | Licença e custo | No seu notebook |
|---|---|---|---|
| **Bonsai** (Blender) + **IfcOpenShell** | Modelar em BIM direto no formato aberto IFC, gerar plantas, cortes e quantitativos | Aberto e grátis | Roda bem (32 GB, GTX 1650) |
| **FreeCAD 1.1** (bancadas BIM, Desenho 2D e FEM) | BIM, desenho técnico e análise por elementos finitos no mesmo programa | Aberto e grátis | Roda bem |
| **Revit, AutoCAD, Civil 3D, Robot Structural** (Autodesk Education) | O que os escritórios usam; currículo e aula | Grátis para professor de instituição qualificada, renovável por ano; **só para estudo e ensino, nunca para trabalho pago** | Revit é só Windows e pesado, mas roda |
| LibreCAD | Desenho 2D simples em DXF | Aberto e grátis | Leve |
| QGIS | Topografia, mapa do terreno, dados do IBGE e da prefeitura | Aberto e grátis | Roda bem |
| Eberick, TQS, CYPE (estrutura, mercado brasileiro) | Cálculo estrutural com as normas da ABNT | Comerciais; alguns têm versão estudantil: confira | — |

O Bonsai 0.8.5 (abr/2026) trouxe ferramentas novas do IfcOpenShell que interessam ao seu lado de TI: `ifcquery` (perguntar ao modelo), `ifcedit` (mudar por script), **`ifcopenshell-mcp`** (o Claude consulta e edita o modelo IFC por MCP) e `ifcchat`.

## Análise, conforto e energia

| Ferramenta | Para quê |
|---|---|
| FreeCAD FEM | Elementos finitos para estudar como uma viga ou laje se deforma |
| PyNite (Python) | Análise de pórticos e vigas por código; casa com a sua Licenciatura (álgebra linear e cálculo) |
| EnergyPlus e Ladybug Tools | Simulação térmica e de energia, base para estudar o desempenho da NBR 15575 |

Tudo isso é estudo: o dimensionamento de verdade é do profissional habilitado, com o software que ele assina.

## Dados, colaboração e web

| Ferramenta | Para quê |
|---|---|
| **Speckle** | Plataforma aberta que leva modelos de Revit, Rhino, Blender e outros para a web, com versões e API; há servidores MCP da comunidade |
| That Open Engine | Bibliotecas abertas para ver e editar IFC no navegador: base para um visualizador dentro do sistema AM |
| SINAPI (Caixa) | Custos de referência por estado, todo mês, em Excel e PDF, de graça |

## O que o setup já traz

```bash
python3 ~/dev/dev-setup/tools/construcao/ifc_resumo.py casa.ifc          # pavimentos, elementos e quantidades
python3 ~/dev/dev-setup/tools/construcao/ifc_resumo.py casa.ifc --json   # para o orçamento ou um painel
```

Lê qualquer IFC (Bonsai, FreeCAD, Revit, Archicad) sem instalar nada. Não mede geometria: usa as quantidades que o modelo exportou.

## Hardware

O notebook atual dá conta de estudar e modelar casas e prédios pequenos. Renderização pesada e modelos grandes pedem a GPU de 12 GB que já está no plano, só depois do portão de renda.
