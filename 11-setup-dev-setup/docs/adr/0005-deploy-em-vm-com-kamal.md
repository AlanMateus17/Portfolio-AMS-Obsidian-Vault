# 0005 · Deploy em VM pelo Kamal; Coolify e Dokploy ficam de fora

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O contexto mestre da empresa solo pede soberania: código, dados e binários sob controle do Alan, sem plataforma intermediária. Ele lista três formas de deploy ao mesmo tempo (Kamal, Coolify e Dokploy) e duas nuvens pagas (AWS e Azure), além da Hetzner. Três ferramentas para a mesma função é o Frankenstein que o próprio documento condena.

O setup já tem: a VM grátis da Oracle (2 núcleos, 12 GB) ligada 24 horas, o Tailscale, o GHCR para as imagens, o KeePassXC para segredos e o ADR 0003 (Azure como nuvem de estudo, por Terraform).

## Decisão

1. **Produção barata dos sistemas AM e de clientes:** Kamal 2, por SSH, numa VM (a da Oracle primeiro; VPS do cliente ou paga quando a renda pedir). Imagem no GHCR, HTTPS pelo kamal-proxy, rollback por versão.
2. **Sem Ruby na máquina:** o Kamal roda pela imagem Docker oficial (`ghcr.io/basecamp/kamal`).
3. **Segredos:** `.kamal/secrets` só chama o `keepassxc-cli` na hora do deploy. Nada de `.env` cifrado no Git (sops/age): segredo fica só no KeePassXC.
4. **Azure continua** como trilha de estudo, certificação e deploy do sistema exemplo por Terraform (ADR 0003). AWS depois.
5. **Coolify e Dokploy ficam de fora.** O painel visual que eles dão não paga a segunda superfície de ataque e de manutenção.

## Alternativas avaliadas

- **Coolify ou Dokploy:** mais fáceis de clicar, mas são mais um serviço web com acesso root à VM para manter atualizado.
- **Só Azure App Service/Container Apps:** bom para estudo; caro para cada cliente pequeno de Barbacena.
- **docker compose por SSH na mão:** funciona, mas sem troca sem queda nem rollback.

## Consequências

- Um caminho só para pôr qualquer sistema no ar: `kamal deploy`. Modelo em `infra/templates/kamal`.
- A VM da Oracle passa a ter dois papéis (automação 24 h e produção pequena); quando um cliente pagar, a produção dele ganha VM própria.
- Aprender Kamal não substitui Terraform e Azure no currículo: os dois continuam na trilha.
