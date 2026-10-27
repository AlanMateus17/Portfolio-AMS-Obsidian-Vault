# Acervo

[← Implantação](../../docs/implantacao/README.md)

Transforma todos os documentos que você já tem em conhecimento organizado no Obsidian e numa lista do que dá para vender. Roda no notebook; nada é enviado para fora. A pasta de origem nunca é alterada.

```bash
bash scripts/wsl/vault.sh                                              # cofre em ~/dev/notas (uma vez)
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout --simular
uv run tools/acervo/acervo.py --origem /mnt/c/Users/SEU_USUARIO/Downloads/Takeout
```

## O que ele faz com cada arquivo

| Situação | Como reconhece | O que acontece |
|---|---|---|
| Cópia repetida | Mesmo conteúdo (SHA-256) | Fica no catálogo como cópia e não é convertida de novo |
| Versão parecida | Mesmo nome com (1), -2... | Convertida, mas conta uma vez só nos produtos |
| Pessoal | Nome (contracheque, extrato, IRPF, fatura...) ou vários CPFs no texto | Não é convertida nem copiada; aparece numa lista para você guardar à parte |
| De terceiros | Direitos reservados, ISBN, editora, ebook, plataforma de curso no nome | Vai para 30-Acervo/_terceiros só como referência de estudo; não vira produto nem treino de IA |
| Feita para a escola | EMTI, escola estadual, SEE-MG, ementa | Convertida, com alerta: confira os direitos ou reescreva do zero antes de vender |
| Sua | O resto | Convertida em 30-Acervo/tema, pronta para virar produto |

Dados de alunos (CPF, e-mail, telefone, "Aluno: ...") geram alerta em qualquer situação.

## Saídas

- `~/dev/notas/30-Acervo/<tema>/*.md`: cada documento em Markdown, com tema, tipo, situação e alertas no cabeçalho
- `~/dev/notas/40-Produtos/Produtos do acervo.md`: resumo, produtos candidatos (mini-curso, apostila, banco de questões, kit do professor, estudo de caso, guia de estudos, série de conteúdo) e alertas
- `~/AMtech/acervo/catalogo.json` e `.csv`, `produtos.json` e `fora.json` (o que não é documento ou deu erro)

As regras ficam em `regras.py` (temas, tipos, produtos). As sugestões são por regra, não uma decisão: revise antes de vender.

Testes: `python -m unittest discover -s tools/acervo -v` (só biblioteca padrão; o teste de ponta a ponta usa arquivos Markdown).
