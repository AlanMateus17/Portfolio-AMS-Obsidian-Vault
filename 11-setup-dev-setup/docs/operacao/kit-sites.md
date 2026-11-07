<!-- Arquivo GERADO por tools/kitsites/gerar.py a partir de data/kitsites.json e data/softwares.json. Não edite à mão. -->

# Kit de sites com IA da Hostinger

[← Operação do grupo](README.md)

Tudo o que um site de cliente precisa para sair em poucas horas e virar mensalidade: 3 pacotes, a ficha do cliente, 26 prompts prontos (um por tipo de negócio), a conferência automática, o checklist de entrega e o relatório mensal. Contrato: [modelo](contrato-sites-modelo.md). Catálogo completo: [softwares](softwares.md).

## Fluxo

1. O cliente preenche a **ficha** (formulário).
2. Você cola o **prompt do tipo de negócio** no Website Builder ou no Horizons, trocando os campos entre colchetes.
3. `python tools/kitsites/conferir.py https://endereco-do-site --fotos` gera o laudo; corrija o que estiver em CORRIGIR.
4. Siga o **checklist de entrega** e cadastre o cliente no CRM e no monitoramento.
5. Todo mês o **relatório** sai sozinho; você só atende as mudanças do pacote.

## Regras

- Conta e domínio no nome do cliente
- Mudança fora do pacote é orçada à parte
- Site novo começa da ficha e da biblioteca de prompts, não do zero
- Nada de fotos ou textos de terceiros sem licença
- Clínica, odontologia e advocacia: seguir as regras de publicidade do conselho

## Pacotes

| Pacote | Inclui | Mudanças por mês | Meta de horas suas por mês |
|---|---|---:|---:|
| **Essencial** | Site institucional (Website Builder com IA); Google Perfil da Empresa configurado; Botão de WhatsApp e telefone clicável; Domínio e e-mail no nome do cliente; Monitoramento de site no ar | 1 | 1 h |
| **Negócio** | Tudo do Essencial; Pedido de avaliação no Google depois do atendimento; Relatório mensal automático de visitas e contatos; Até 3 mudanças de conteúdo por mês; Posts de novidade no Google Perfil | 3 | 2 h |
| **Vendas** | Tudo do Negócio; Função paga no Horizons: cardápio com pedido, agenda, catálogo ou área do cliente; Automação de atendimento no WhatsApp (perguntas frequentes); Captura de contatos com consentimento (LGPD) | 5 | 4 h |

Preço: taxa de criação + mensalidade. Defina os valores pela sua hora mínima e pelo tempo real medido nos 3 primeiros clientes.

## Ficha do cliente

| Campo | Tipo |
|---|---|
| Nome do negócio e CNPJ ou CPF do responsável | texto |
| Tipo de negócio (um dos 26 do catálogo) | lista |
| Endereço, horário de funcionamento e área atendida | texto |
| WhatsApp, telefone, e-mail e redes | texto |
| Logo (arquivo) e cores da marca | arquivo |
| Até 10 fotos boas do lugar, produtos ou trabalhos | arquivo |
| O que vende: serviços ou produtos com preço (se quiser mostrar) | texto |
| 3 diferenciais e o público principal | texto |
| Depoimentos ou link das avaliações do Google | texto |
| Domínio desejado (e se já tem) | texto |
| Pacote escolhido (Essencial, Negócio, Vendas) | lista |
| Autorização de uso das fotos e textos enviados | aceite |
| Consentimento para os dados de contato no CRM (LGPD) | aceite |

## Prompts por tipo de negócio

### Site de padaria e confeitaria

Ferramenta: **Website Builder com IA** · Para: padarias, confeitarias, docerias

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], padarias em [CIDADE]. Objetivo: vitrine, cardápio, encomenda de bolos e salgados. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, cardápio digital, pedido online, galeria e portfólio. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de restaurante, lanchonete e sushi

Ferramenta: **Horizons** · Para: restaurantes, lanchonetes, pizzarias, sushi

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], restaurantes em [CIDADE]. Objetivo: cardápio digital, pedido pelo whatsapp, reservas. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, cardápio digital, pedido online, agendamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de cafeteria

Ferramenta: **Website Builder com IA** · Para: cafeterias

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], cafeterias em [CIDADE]. Objetivo: cardápio, fidelidade simples, eventos. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, cardápio digital, galeria e portfólio. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de imobiliária

Ferramenta: **Horizons** · Para: imobiliárias e corretores

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], imobiliárias e corretores em [CIDADE]. Objetivo: catálogo de imóveis com filtros, contato por imóvel, captação de proprietário. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, catálogo com filtros, galeria e portfólio, blog e notícias. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de construtora e empreiteira

Ferramenta: **Website Builder com IA** · Para: construtoras, empreiteiras, pedreiros

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], construtoras em [CIDADE]. Objetivo: portfólio de obras, empreendimentos, orçamento. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, galeria e portfólio, pedido de orçamento, catálogo com filtros. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de oficina mecânica e autopeças

Ferramenta: **Website Builder com IA** · Para: oficinas, funilarias, autopeças

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], oficinas em [CIDADE]. Objetivo: serviços, orçamento, agendamento de revisão. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, pedido de orçamento, agendamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de assistência técnica

Ferramenta: **Horizons** · Para: assistências de celular e informática

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], assistências de celular e informática em [CIDADE]. Objetivo: serviços, orçamento, status do conserto. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, pedido de orçamento, área do cliente. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de clínica e consultório

Ferramenta: **Horizons** · Para: clínicas, psicólogos, fisioterapeutas, nutricionistas

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], clínicas em [CIDADE]. Objetivo: especialidades, agendamento, conteúdo. respeitar as regras de publicidade de cada conselho. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento, blog e notícias. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de odontologia

Ferramenta: **Website Builder com IA** · Para: dentistas e clínicas odontológicas

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], dentistas e clínicas odontológicas em [CIDADE]. Objetivo: tratamentos, agendamento, depoimentos (regras do cro). Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento, galeria e portfólio. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de salão, barbearia e estética

Ferramenta: **Website Builder com IA** · Para: salões, barbearias, estética

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], salões em [CIDADE]. Objetivo: serviços, preços, agendamento. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento, galeria e portfólio. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de academia e personal

Ferramenta: **Website Builder com IA** · Para: academias, estúdios, personal trainers

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], academias em [CIDADE]. Objetivo: planos, aula experimental, agenda. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento, pagamento e assinatura. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de pet shop e veterinária

Ferramenta: **Website Builder com IA** · Para: pet shops, clínicas veterinárias

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], pet shops em [CIDADE]. Objetivo: banho e tosa com agenda, produtos, emergência. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento, catálogo com filtros. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de escola e curso livre

Ferramenta: **Website Builder com IA** · Para: escolas particulares, cursos de idioma e informática

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], escolas particulares em [CIDADE]. Objetivo: cursos, matrícula, eventos. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, blog e notícias, galeria e portfólio. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de advocacia

Ferramenta: **Website Builder com IA** · Para: advogados e escritórios

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], advogados e escritórios em [CIDADE]. Objetivo: áreas de atuação e conteúdo, dentro das regras da oab (sem captação). Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, blog e notícias. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de contabilidade

Ferramenta: **Horizons** · Para: escritórios de contabilidade

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], escritórios de contabilidade em [CIDADE]. Objetivo: serviços, abertura de empresa, portal de documentos. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, área do cliente, blog e notícias. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de loja (moda, presentes, variedades)

Ferramenta: **Horizons** · Para: lojas de roupa, calçados, presentes

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], lojas de roupa em [CIDADE]. Objetivo: catálogo com pedido pelo whatsapp ou loja virtual. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, catálogo com filtros, pedido online, pagamento e assinatura. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de mercado, hortifruti e açougue

Ferramenta: **Horizons** · Para: mercados de bairro, hortifrútis, açougues

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], mercados de bairro em [CIDADE]. Objetivo: ofertas da semana, lista de pedido, entrega. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, catálogo com filtros, pedido online. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de hotel e pousada

Ferramenta: **Horizons** · Para: hotéis e pousadas de Barbacena e região

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], hotéis e pousadas de Barbacena e região em [CIDADE]. Objetivo: quartos, galeria, reserva direta sem comissão. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, galeria e portfólio, agendamento, pagamento e assinatura. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de floricultura

Ferramenta: **Horizons** · Para: floriculturas e produtores de rosas (Barbacena)

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], floriculturas e produtores de rosas (Barbacena) em [CIDADE]. Objetivo: catálogo de buquês, pedido com data de entrega. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, catálogo com filtros, pedido online, pagamento e assinatura. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de buffet, eventos e fotógrafo

Ferramenta: **Website Builder com IA** · Para: buffets, decoradores, fotógrafos, DJs

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], buffets em [CIDADE]. Objetivo: portfólio, pacotes, orçamento de evento. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, galeria e portfólio, pedido de orçamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de arquitetura e interiores

Ferramenta: **Website Builder com IA** · Para: arquitetos, designers, marcenarias

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], arquitetos em [CIDADE]. Objetivo: portfólio de projetos, orçamento. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, galeria e portfólio, pedido de orçamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de autoescola

Ferramenta: **Website Builder com IA** · Para: autoescolas

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], autoescolas em [CIDADE]. Objetivo: categorias, preços, matrícula. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, agendamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de energia solar e elétrica

Ferramenta: **Horizons** · Para: integradores solares e eletricistas

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], integradores solares e eletricistas em [CIDADE]. Objetivo: simulador de economia, orçamento. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, pedido de orçamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de transporte e mudanças

Ferramenta: **Website Builder com IA** · Para: transportadoras, fretes, mudanças

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], transportadoras em [CIDADE]. Objetivo: orçamento por distância, áreas atendidas. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, pedido de orçamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de igreja e ONG

Ferramenta: **Website Builder com IA** · Para: igrejas, associações, ONGs

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], igrejas em [CIDADE]. Objetivo: agenda, transmissões, doações. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, blog e notícias, pagamento e assinatura. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

### Site de indústria e fornecedor B2B

Ferramenta: **Website Builder com IA** · Para: pequenas indústrias e distribuidores

```text
Crie um site em português do Brasil para [NOME DO NEGÓCIO], pequenas indústrias e distribuidores em [CIDADE]. Objetivo: catálogo técnico e pedido de cotação. Seções e funções: vitrine base, avaliações e depoimentos, captura de contatos, relatório mensal, catálogo com filtros, pedido de orçamento. Use as cores [CORES DA MARCA] e o logo enviado. Tom: próximo e profissional. Botão de WhatsApp fixo ([WHATSAPP]), telefone clicável, endereço com mapa, horário ([HORÁRIO]). Textos curtos, título claro em cada seção, fotos enviadas pelo cliente com descrição (alt). SEO: título da página e descrição com o tipo de negócio e a cidade. Funcionar perfeitamente no celular.
```

## Checklist de entrega

- [ ] Conta Hostinger e domínio no nome do cliente; você como colaborador (sem acesso a pagamentos)
- [ ] Laudo do conferir.py com nota 80 ou mais, e Lighthouse no celular conferido
- [ ] SSL ativo e endereço com https
- [ ] WhatsApp, telefone e mapa testados no celular
- [ ] Formulário de contato testado (mensagem chegou)
- [ ] Google Perfil da Empresa verificado e com link do site
- [ ] Monitoramento no Uptime Kuma e cliente cadastrado no CRM
- [ ] Relatório mensal agendado
- [ ] Contrato assinado e primeira mensalidade cobrada
- [ ] Senhas do cliente só no KeePassXC (grupo Clientes), nunca por WhatsApp

## Relatório mensal (modelo)

- Visitas do mês e comparação com o mês anterior
- Cliques em WhatsApp e telefone
- Mensagens do formulário
- Avaliações novas no Google
- Site no ar (% do tempo) e incidentes
- Mudanças feitas e quantas restam no pacote
- Uma sugestão de melhoria para o próximo mês
