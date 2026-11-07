# Sala limpa: estudar um binário e reimplementar do zero

Três pastas, uma regra: o que está em `alvos/` nunca é copiado para `src/`.

1. `alvos/` binários brutos e dumps (.bin, .hex). Fora do Git (`.gitignore`) e dentro da pasta cifrada do gocryptfs.
2. `specs/` o protocolo e o comportamento descritos em Markdown, com as suas palavras: mensagens, campos, ordem, temporização.
3. `src/` a reimplementação limpa, escrita só a partir de `specs/`, na linguagem que a triagem escolher (C#, TypeScript, Go ou Rust).

Só com binário seu, de aluno em aula, crackme ou com autorização escrita no `escopo.py`. Binário de cliente só com modelo local.

    gocryptfs -init ~/dev/lab-cifrado && mkdir -p ~/dev/lab && gocryptfs ~/dev/lab-cifrado ~/dev/lab
