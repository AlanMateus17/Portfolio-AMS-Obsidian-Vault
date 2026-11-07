# As empresas do grupo: o que está pronto e o que só você faz

Três frentes estão configuradas no setup, cada uma com site, roteiro e decisões próprias:

| Empresa | O que vende | Site | Seu roteiro |
|---|---|---|---|
| **Grupo AMtech Digital** | Sites, sistemas e automação para pequenas empresas (pacotes Essencial, Negócio e Vendas) | `just site amtech` | `just agora software` · `just decisoes software` |
| **Instituto AMS Silva** | Cursos de TI, Matemática e Finanças; o primeiro é o mini-curso de Lógica | `just site instituto` | `just agora instituto` · `just decisoes instituto` |
| **Editora AMS Silva** | Livros didáticos; o primeiro é Lógica e Máquina | `just site editora` | `just agora editora` · `just decisoes editora` |

As três vendem no seu CPF até o ponto de virada combinado com o contador (passo `sw-formalizar`). O carnê-leão vale para todas.

## O que já está pronto (você não precisa montar)

- **Os três sites**, gerados do mesmo modelo Astro (`infra/templates/site-marca`): início, ofertas, como funciona, sobre, dúvidas, contato, política de privacidade e termos de uso da LGPD, versão clara e escura, celular, sitemap. Textos, ofertas e cores ficam em `data/marcas/<marca>.json`. Testados: compilam e não estouram a largura no celular.
- **O roteiro de cada empresa**, com cada passo marcado por empresa (62 da AMtech, 23 do Instituto, 17 da Editora), o comando, onde rodar e o critério de pronto.
- **As decisões listadas**, com os fatos para decidir (CPF ou SLU, marca no INPI, preços, contrato, hospedagem, autonomia, plataforma de cursos, ISBN).
- **O contrato de sites** (`docs/operacao/contrato-sites-modelo.md`), o kit de sites com 26 prompts por tipo de negócio, a esteira issue → PR → prévia → aprovação, o checklist de entrega e o relatório mensal.
- **A operação por trás:** backup, cofre de senhas, CI com testes, o Professor para aprender o que você opera e a Escola Akita.

## O que só você pode fazer

Ninguém pode fazer isto por você, nem deve: são suas contas, seu dinheiro, sua assinatura e sua voz.

1. **Decidir:** `just decisoes software`, `just decisoes instituto` e `just decisoes editora`. Os preços, por exemplo, ficam em branco até você decidir, e o site mostra "Sob orçamento" ou "Preço no lançamento".
2. **Criar as contas e pôr os dados no site.** `just site <marca> --checar` lista exatamente o que falta:
   - domínio (Registro.br);
   - pelo menos um canal de contato (WhatsApp Business, formulário ou e-mail do domínio);
   - o e-mail para pedidos da LGPD;
   - o link de venda dos cursos (Hotmart ou Kiwify);
   - o Umami, para medir visitas.
3. **Gravar as aulas** do mini-curso e **escrever o livro**.
4. **Aprovar** cada proposta, contrato, cobrança e publicação. Isso sempre para no seu ok, pela sua regra.

## O que ainda não é automático (com franqueza)

- **O funil que roda sozinho** (formulário → agenda → CRM → proposta → contrato → fatura) depende das fases 6 e 7 do Núcleo, que ainda não foram construídas. Hoje o setup prepara cada documento e você envia.
- **Publicar posts sozinho** nos melhores horários depende do Postiz configurado e da sua aprovação de cada post.
- **Atender no WhatsApp sozinho** depende do pacote Vendas de cada cliente e do Chatwoot ou do n8n ligados ao número dele.

Quando essas peças existirem, cada uma entra no roteiro da empresa como passo novo, e esta página muda.
