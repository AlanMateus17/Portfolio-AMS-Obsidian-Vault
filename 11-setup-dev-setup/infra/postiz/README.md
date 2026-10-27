# Postiz (agendador de posts)

[← Implantação](../../docs/implantacao/README.md)

O Postiz agenda e publica nas redes a partir de uma fila. Ele é open source (AGPL-3.0), mas a instalação atual é pesada: além do próprio app, o compose oficial sobe PostgreSQL, Redis, **Temporal** (orquestrador de tarefas) e **Elasticsearch**. Conferido no repositório oficial `gitroomhq/postiz-docker-compose` em 21/10/2026.

## Quando subir

| Situação | O que fazer |
|---|---|
| Só o notebook, com o WSL limitado a 12 GB | Comece agendando direto no **Meta Business Suite** (Instagram e Facebook), no **YouTube Studio** e no **TikTok Studio**. O pipeline já entrega as peças prontas; o agendamento leva poucos minutos por semana |
| Servidor 24 horas (mini PC ou PC antigo com 16 GB) | Suba o Postiz lá, junto da stack de automação |

O agendador nativo de cada rede não escolhe o melhor horário sozinho, mas o painel de métricas mostra os melhores horários para você escolher.

## Como subir

```bash
mkdir -p ~/servicos/postiz && cd ~/servicos/postiz
curl -fsSLO https://raw.githubusercontent.com/gitroomhq/postiz-docker-compose/main/docker-compose.yaml
# Edite o arquivo: troque JWT_SECRET por um valor aleatório e as senhas do PostgreSQL.
# Guarde tudo no KeePassXC.
docker compose up -d
```

Depois abra `http://localhost:4007`, crie sua conta e, em seguida, mude `DISABLE_REGISTRATION` para `'true'` e rode `docker compose up -d` de novo para fechar o cadastro.

Cada rede pede um app de desenvolvedor próprio (chaves `*_CLIENT_ID` e `*_CLIENT_SECRET` no compose). Lembre dos limites já documentados em [Publicação autônoma](../../docs/marketing/03-publicacao-autonoma.md): um app do TikTok que não passou pela auditoria só publica como privado.
