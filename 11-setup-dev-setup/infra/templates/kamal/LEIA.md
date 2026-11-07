# Modelo de deploy com Kamal

Deploy sem queda de um sistema AM numa VM (Oracle grátis, VPS de cliente ou a sua), por SSH. Decisão no [ADR 0005](../../../docs/adr/0005-deploy-em-vm-com-kamal.md).

## Usar

1. Copie `config/deploy.yml` e `.kamal/secrets.example` para a raiz do sistema; renomeie o segundo para `.kamal/secrets` e ponha `.kamal/secrets` no `.gitignore`.
2. Troque os valores entre `<>`. A VM entra pelo IP do Tailscale; só as portas 80 e 443 ficam abertas para a internet.
3. Sem Ruby na máquina: use a imagem oficial. No Ubuntu do WSL, uma vez:

```bash
echo "alias kamal='docker run -it --rm -v \"\${PWD}:/workdir\" -v \"\${SSH_AUTH_SOCK}:/ssh-agent\" -v /var/run/docker.sock:/var/run/docker.sock -e SSH_AUTH_SOCK=/ssh-agent ghcr.io/basecamp/kamal:latest'" >> ~/.bashrc
```

4. `kamal setup` na primeira vez; depois `kamal deploy`. Para voltar: `kamal app versions` e `kamal rollback <versão>`.

## Regras

- O segredo nunca entra no repositório, nem cifrado: `.kamal/secrets` só chama o `keepassxc-cli` na hora.
- Banco na mesma VM só enquanto couber; o backup do PostgreSQL vai para o restic antes do primeiro cliente.
- O Azure (ADR 0003) continua sendo a trilha de estudo e de certificação, com Terraform. O Kamal é o caminho barato de produção.
