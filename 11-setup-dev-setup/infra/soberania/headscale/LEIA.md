O Headscale lê `config.yaml` desta pasta. Baixe o modelo oficial e troque `server_url` pelo endereço da VM:

    curl -fsSL https://raw.githubusercontent.com/juanfont/headscale/main/config-example.yaml -o infra/soberania/headscale/config.yaml

O `config.yaml` não vai para o Git (tem a chave privada do servidor).
