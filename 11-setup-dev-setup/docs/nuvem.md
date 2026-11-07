<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Nuvem

[← Índice da documentação](README.md)

## Microsoft Azure

*1º · casa com sua stack · Próximos 3 meses*

- **Por quê:** A stack do Aura é .NET 10; o Azure tem a melhor integração (App Service, Azure SQL/PostgreSQL, Key Vault, Entra ID) e é forte em empresa brasileira que usa Microsoft.
- **Certificações:** AZ-900 (fundamentos) e depois AI-200 (desenvolvedor Azure com IA; substituiu o AZ-204 em 31/07/2026).
- **Prática:** Publicar um sistema AM no Azure com Terraform, Key Vault e deploy pelo GitHub Actions.

## Amazon Web Services

*2º · maior mercado · 3 a 12 meses*

- **Por quê:** Maior fatia do mercado e a nuvem mais usada pelos desenvolvedores. Muitas vagas pedem AWS mesmo em times .NET.
- **Certificações:** Cloud Practitioner e depois Developer Associate.
- **Prática:** Subir o mesmo sistema na AWS (ECS ou App Runner, RDS, S3) e comparar com o Azure. Isso vira post no blog e aula.

## Google Cloud

*3º · só o básico · Depois de 12 meses*

- **Por quê:** Cresce rápido, puxado por IA e dados, mas aparece menos em vaga .NET no Brasil.
- **Certificação:** Nenhuma por agora; só conhecer os serviços equivalentes.
- **Prática:** Usar quando um projeto de IA ou BigQuery pedir.

## Regra de ouro para as três

*Custo · Agora*

- **Conta:** Use os níveis gratuitos e crie alerta de orçamento (ex.: US$ 5) no primeiro dia.
- **Infra:** Tudo por código (Terraform/OpenTofu), para destruir com um comando e não esquecer nada ligado.
- **Local:** Azurite simula o Storage do Azure; emuladores evitam gastar enquanto aprende.
