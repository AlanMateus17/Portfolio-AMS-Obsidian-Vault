# 0003 · Azure como primeira nuvem, AWS como segunda

- **Status:** aceita, atualizada pela [0017](0017-nucleo-ts-python-dotnet-reserva.md)
- **Data:** 2026-10-20

> **Atualização (13/11, ADR 0017):** com o núcleo em TS/Python (não mais .NET), o deploy primário passou a ser **Vercel + VPS**. Azure/AWS viram estudo e portfólio, não a primeira nuvem padrão.

## Contexto

A stack dos sistemas é .NET 10. No 2º trimestre de 2026, a AWS tinha 28% do mercado de infraestrutura em nuvem, a Microsoft 20% e o Google 15% (Synergy Research). Na pesquisa do Stack Overflow de 2026, 41,8% dos desenvolvedores usaram AWS, 25,1% Azure e 24,5% Google Cloud.

## Decisão

Primeiro deploy real no Azure (App Service ou Container Apps, PostgreSQL, Key Vault), com certificações AZ-900 e AZ-204. Depois, o mesmo sistema na AWS para comparar. Google Cloud só no básico. Toda infraestrutura criada por Terraform, com alerta de orçamento desde o primeiro dia.

## Consequências

- Melhor integração com .NET e com empresas que usam o ecossistema Microsoft.
- A AWS entra em seguida para cobrir o mercado maior.
- Infra por código permite destruir e recriar tudo, e vira material de portfólio e de aula.

> Atualização (2026-11-01): o AZ-204 deixou de ser agendável em 31/07/2026; o caminho de desenvolvedor passa a ser o AI-200. Ver docs/certificacoes.md.
