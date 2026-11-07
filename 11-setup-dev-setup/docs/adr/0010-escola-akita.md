# 0010 · Escola Akita: seguir o Fabio Akita a fundo, com notas próprias e aprovação por regra

- **Status:** aceita
- **Data:** 2026-11-06

## Contexto

O Alan quer seguir a fundo o que o Fabio Akita ensina: o setup deve ler todos os artigos e vídeos, criar notas e seguir as regras, dicas e alertas dele, sempre com a aprovação do Alan.

O blog (akitaonrails.com) tem 831 posts em português de 2006 a 2026, e o código-fonte dele está num repositório público no GitHub (akitaonrails/akitaonrails.github.io), em Markdown. Os vídeos do Akitando já estão lá também: 198 posts têm o vídeo e a transcrição. O rodapé diz "© 2006–2026 Fabio Akita" e o conteúdo não tem licença aberta.

## Decisão

1. **A fonte é o repositório público do blog, por git.** Nada de raspar o site ou baixar vídeo do YouTube: as transcrições do Akitando já vêm no blog.
2. **O texto dele fica só na máquina do Alan.** O clone fica em ~/dev/referencias/akitaonrails, fora do dev-setup, e uma cópia pesquisável fica no banco local do núcleo. No repositório entram só o índice (título, data, link, tags) e as regras escritas com outras palavras, cada uma com o link da fonte. O livro dele (Competent Enough) é pago e não entra.
3. **Nota não é regra.** Cada post vira uma nota no Obsidian. Só o que é acionável e técnico ou de negócio vira regra. Post de opinião, política ou off-topic vira nota sem regra.
4. **Toda regra nasce "nova" e só muda o setup com o ok do Alan.** O Alan escolhe aprovar, recusar, "já segue" ou "não se aplica". A aprovada vira tarefa no núcleo, e o Claude a aplica num PR, dentro do ai-jail e sem merge. Cada decisão fica na auditoria do núcleo.
5. **A mais nova vale.** Benchmark, modelo e preço ficam velhos rápido: essas regras são marcadas como "datado" e revistas toda semana. Quando uma regra nova contradiz uma antiga, a antiga vira "substituida".
6. **Seguir o Akita não passa por cima das regras do Alan.** Exemplo: o "faça mais deploy" do Akita convive com o "nada publicado sem aprovação" do Alan, e a aprovação passa a ser de um toque.

7. **Ligada ao Professor (ADR 0012).** Cada módulo indica até 2 posts escolhidos a dedo para ler antes da aula. Regra aprovada, aplicada ou "já segue" vira conhecimento no núcleo e entra no contexto das aulas. O texto original continua fora do pedido à IA: a aula recebe o link, não o post.
8. **Podcasts no Spotify:** o Akita tem dois. **The M.Akita Chronicles** é semanal, com as notícias da semana em tecnologia e IA (episódios de cerca de 30 minutos; o site é themakitachronicles.com). **Akitando** é o áudio dos vídeos do canal, cuja transcrição já está no blog. Os dois entram como escuta (ônibus, restaurante) seguida da nota de 3 ideias e 1 ação (`just professor escutei`). O Chronicles serve para acompanhar o que muda; o que for regra técnica vem pelo blog. Ele também aparece como convidado em podcasts de outras pessoas.

## Consequências

- Gerar as notas custa: perto de 1,8 milhão de palavras. Pelo Claude, são dias do plano; pelo Ollama na GTX 1650, são noites de processamento, com notas mais fracas. O Alan escolhe o motor por prioridade.
- Ordem: a era da IA (191 posts, 2025 e 2026), depois o Akitando, depois os técnicos, e o histórico da era Rails por último.
- Piloto: 2 posts lidos e 22 regras esperando decisão.
- Correção (2026-11-06): a leitura das tags ignorava as que vinham sem recuo, e por isso só 14 posts caíam em "opinião". Corrigido, o índice fica com 189 posts de opinião ou off-topic, que não viram regra.
