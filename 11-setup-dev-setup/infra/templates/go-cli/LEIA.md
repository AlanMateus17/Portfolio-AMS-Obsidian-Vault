# Modelo de CLI em Go

Para ferramentas do setup e produtos que precisam ser um binário único (rodar no cliente sem instalar nada). Tela interativa com bubbletea; release com GoReleaser. `go` vem do mise.

    cp -r ~/dev/dev-setup/infra/templates/go-cli ~/dev/minha-cli && cd ~/dev/minha-cli && go mod tidy && go run ./cmd/ferramenta
