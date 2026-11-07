# Dotfiles do setup (fonte do chezmoi)

Configuração de terminal, editor e ferramentas, aplicada pelo chezmoi. O chezmoi copia esta pasta para o seu repositório privado `dotfiles` (que vira a fonte dele) e aplica em `~/.config`.

```bash
# Ubuntu do WSL, uma vez:
chezmoi init && cp -rn ~/dev/dev-setup/infra/dotfiles/. ~/.local/share/chezmoi/ && chezmoi init && chezmoi diff && chezmoi apply
```

| Arquivo | O quê |
|---|---|
| `dot_config/mise/config.toml` | Runtimes (Node, Go, Rust) e as CLIs instaladas pelo `mise install` |
| `dot_config/zellij/` | Multiplexador e o layout `setup` (código, servidor, git) |
| `dot_config/starship.toml` | Prompt curto |
| `dot_config/ghostty/config` | Terminal do Arch nativo (o Ghostty não tem versão para Windows) |
| `dot_config/nvim/init.lua` | Neovim com lazy.nvim, snacks.nvim e tree-sitter |
| `dot_config/yazi/yazi.toml` | Gerenciador de arquivos no terminal |
| `dot_aider.conf.yml` | Aider com o modelo local do Ollama (custo zero) |
| `.chezmoi.toml.tmpl` | Liga o chezmoi ao KeePassXC: segredos vêm do cofre, nunca do repositório |

Segredo nunca entra aqui. Quando um arquivo precisar de um, use o modelo `.tmpl` com `{{ (keepassxc "AMtech/...").Password }}`.
