# Operação do grupo

[← Índice da documentação](../README.md)

O sistema que faz **toda** oferta do Grupo AMtech Digital passar pela mesma engenharia: infoprodutos, livros, software, serviços, negócios físicos e canais. Uma esteira só, um catálogo só, um jeito só de medir, divulgar, automatizar e escalar.

## A ideia em uma frase

Nada é vendido sem ter passado pela esteira; nada é feito uma vez só: cada trabalho vira conteúdo, cada cliente vira dado, cada processo repetido vira automação, e cada oferta nova nasce do que já existe.

```mermaid
flowchart LR
  C["Catálogo único<br/>108 ofertas pontuadas<br/>arsenal com vereditos"] --> E["Esteira<br/>ideia → validação → construção<br/>→ lançamento → escala"]
  E --> Q["Padrão de qualidade<br/>por tipo de oferta"]
  Q --> V["Venda e entrega"]
  V --> D["Clientes e dados<br/>CRM único, LGPD"]
  V --> F["Flywheel de conteúdo<br/>cada trabalho vira peças"]
  F --> M["Marca e presença<br/>redes, Google, newsletter"]
  M --> V
  D --> P["Painel do grupo<br/>números por oferta"]
  P -->|"novas ideias e cortes"| C
  A["Automação e agentes<br/>n8n, Claude, sistemas AM"] -.-> V
  A -.-> F
  A -.-> D
```

## Documentos

1. [Esteira de ofertas](01-esteira-de-ofertas.md): os estágios, os portões entre eles e o que o setup faz em cada um
2. [Marca e presença](02-marca-e-presenca.md): arquitetura de marcas, papel de cada rede, Google Perfil da Empresa, avaliações e uma rotina que cabe na sua semana
3. [Flywheel de conteúdo](03-flywheel-de-conteudo.md): como uma aula, um reparo, um capítulo ou um prato viram dez peças de conteúdo
4. [Automação e escala](04-automacao-e-escala.md): os níveis de automação, os agentes do grupo e a alavanca de escala de cada tipo de oferta
5. [Padrão de qualidade](05-padrao-de-qualidade.md): o que é "pronto" para cada tipo de oferta e o ciclo de melhoria
6. [Clientes e dados](06-clientes-e-dados.md): CRM único, consentimento, jornadas entre ofertas e os números de cada uma
7. [Ordem de execução](07-ordem-de-execucao.md): o que fazer nos próximos 90 dias e 12 meses, dentro das horas que você tem
8. [Financiar o setup](08-financiar-o-setup.md): a renda paga o setup, nessa ordem — cada marco de renda libera uma compra, pela cascata
- [Portfólio de ofertas](portfolio.md): o catálogo completo, o arsenal de rendas (o que entra agora, a fila, o que fica para 2027, o que exige capital e o que foi descartado), as regras de hora mínima e teto de horas, e o ranking (gerado)
- [Kit de sites com IA da Hostinger](kit-sites.md): pacotes, ficha do cliente, um prompt por tipo de negócio, conferência automática, checklist de entrega, relatório mensal e o [modelo de contrato](contrato-sites-modelo.md) (gerado)
- [Conversas curtas](sessoes-curtas.md): o protocolo para o limite das IAs durar (pacote de contexto, ESTADO.md, ai-memory, ai-usagebar)
- [Operação 24 horas](24-horas.md): o que roda no notebook, no GitHub e na VM grátis, e o que o setup faz sozinho o tempo todo
- [Catálogo de softwares](softwares.md): todos os sites por tipo de negócio, sistemas AM, micro-SaaS e produtos que você pode criar e vender, montados com módulos reaproveitáveis e ligados às ofertas (gerado)
- [`portfolio.html`](portfolio.html): o mesmo catálogo com filtros, para abrir no navegador

## Antes de tudo: o limite real

Você trabalha cerca de 63 horas por semana entre escola e restaurante, faz licenciatura e estuda para a vaga de dev. O setup automatiza muito, mas não grava a sua aula, não escreve o seu livro e não atende o primeiro cliente por você. Por isso a regra que segura tudo é a do [documento de execução](07-ordem-de-execucao.md): **uma oferta em construção e uma em validação por vez.** O resto espera na fila do catálogo, pontuado e com o próximo passo escrito, sem ocupar a sua cabeça.

## Como os dados funcionam

- `data/portfolio.json` é a fonte de todas as ofertas. `python tools/portfolio/portfolio.py` valida e gera o [portfólio](portfolio.md) e o `portfolio.html`, com testes em `tools/portfolio/test_portfolio.py`.
- Os números dos negócios físicos vêm de `data/negocios.json` ([Negócios do grupo](../negocios/README.md)).
- O CI confere tudo a cada push.
