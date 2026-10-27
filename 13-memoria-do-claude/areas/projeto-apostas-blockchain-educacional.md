---
name: projeto-apostas-blockchain-educacional
description: ByteSDCoin (Escola Senhora das Dores) — blockchain educacional para escolas e outros públicos, tabuleiro robótico, rede pública com moeda de mercado
sources: [chat]
aliases: [ByteSDCoin, BSD, BetSim Educacional]
---
- [stated] Escola: Escola Estadual Senhora das Dores
- [stated] Projeto: equipes de alunos desenvolvem, cada uma, um sistema completo de "casa de apostas" simulada (sem dinheiro real), com explicação de como garantem lucro e como evitam enganar usuários
- [stated] Todas as equipes compartilham uma moeda/token comum e uma blockchain própria e comum entre elas
- [stated] Nome da moeda escolhido: ByteSDCoin, símbolo BSD
- [stated] Quer que a mineração de BSD funcione como no Bitcoin: teto de 21 milhões de moedas, com subunidade própria (tipo "satoshi") baseada em um número com curiosidade matemática (ex: número primo)
- [stated] Quer que a mineração seja um "jogo": alunos jogam xadrez/dama/dominó/quebra-cabeça enquanto respondem perguntas de TI, matemática, física e química; quem vence o jogo e as perguntas leva o bloco inteiro, tudo registrado na blockchain
- [stated] Quer incluir perguntas em modo "quem responde primeiro" (estilo buzzer) na mineração
- [stated] Quer que o projeto seja contínuo/sem fim, para que mais pessoas possam usá-lo no futuro, sempre validado pela mesma rede blockchain
- [stated] Pretende usar este projeto (ByteSDCoin) em seu blog e em seu currículo
- [stated] Subunidade: 1 BSD = 100.000.000 PRIMEs (antes havia decidido 1.000.000.007)
- [stated] Emissão: 50.000 BSD por semana (época), halving a cada 210 semanas, teto de 21.000.000 BSD, limite de 5% do pote por conta (antes era 50.000 BSD por bloco, halving a cada 210 blocos)
- [stated] Em 23/09/2026 aprovou todas as decisões de arquitetura (ADRs 0000–0018): consenso Proof of Authority com validadores institucionais (4 no piloto), rede de produção sobre Hyperledger Besu, núcleo atual vira "BSD Didático", dados pessoais fora da cadeia (só hashes), log de auditoria ancorado em todos os sistemas escolares, blockchain não substitui segurança operacional, licença MIT + CC BY 4.0
- [stated] Quer manter a blockchain/núcleo sob seu próprio controle (professor); os alunos só minerariam (via o jogo definido) e usariam a moeda (comércio entre alunos, plataformas de apostas), sem acesso direto ao núcleo da rede
- [stated] Quer que eventos decisivos do jogo (ex: xeque-mate) disparem uma pergunta transmitida simultaneamente a todos que estiverem minerando; quem responder primeiro ganha bonificação em moedas, com perguntas classificadas por níveis de dificuldade
- [stated] Quer que a moeda seja sempre uma única rede/cadeia, exatamente como o Bitcoin (nunca fragmentada em cadeias paralelas), mesmo se o projeto crescer para outras escolas no futuro
- [stated] Quer começar já com a arquitetura final de validação descentralizada (múltiplos nós validadores com quórum), mesmo operando sozinho no início do projeto
- [stated] Ideia inicial de registrar fotos das jogadas foi substituída: decidiu que os jogos de mineração serão totalmente virtuais (não físicos/presenciais), com jogadas registradas diretamente como dados pelo motor de jogo
- [stated] BSD nunca será conversível em dinheiro real; usar cotação simulada entre alunos (antes queria conversão em moeda fiduciária)
- [stated] Quer aplicar métodos de educação financeira ao projeto: método ARCA, método BEST (Barsi), e um terceiro método complementar, para que os alunos aprendam fundamentos de investimento
- [stated] Quer que a mineração seja individual (não por equipe) e aberta a qualquer pessoa que fizer login, não só alunos
- [stated] Quer uma segunda arquitetura de blockchain que torne a criação de novas moedas realmente impossível, não apenas detectável
- [stated] Quer que os jogos de mineração (xadrez, damas, dominó etc.) sejam jogados normalmente, com regras oficiais e frontend jogável de verdade, como em qualquer outro lugar — o motor do jogo não deve saber que está sendo minerado; a camada de mineração só reage a eventos do jogo (ex: xeque-mate) por fora, sem alterar as regras
- [stated] Quer usar WSL2 + Docker em vez de VirtualBox/VM tradicional como ambiente de desenvolvimento do projeto (mais leve, mais próximo da prática de mercado)
- [stated] Quer que a blockchain ByteSDCoin seja universal: fazer tudo o que o Bitcoin e o Ethereum fazem hoje, além das funcionalidades próprias adicionadas no projeto
- [stated] Quer as mesmas propriedades do Bitcoin/Ethereum, com as funcionalidades do projeto em paralelo, e usar os computadores dos usuários para ajudar na mineração/segurança da rede
- [stated] A casa de apostas é só uma ideia de jogo para o trabalho em sala; a versão pública não terá apostas, e sim jogos educacionais, realização de provas, registro de notas e histórico de alunos (ainda decidindo o que incluir)
- [stated] Quer que os jogos sirvam só para bonificações/recompensas, com a segurança da rede garantida por outro mecanismo que não seja prejudicado pelos jogos
- [stated] Quer colocar o projeto no portfólio e dar continuidade a ele junto com os alunos, para fortalecer os currículos dele e dos alunos perante recrutadores
- [stated] Pretende criar uma terceira criptomoeda que siga as regras do Bitcoin/Ethereum, reúna o melhor das duas e tenha identidade própria, atraindo força computacional e valor; aceitou separá-la da rede escolar (mesma tecnologia, redes diferentes), e quer que o público escolar use a blockchain e as tecnologias do projeto para resolver problemas da escola
- [stated] O projeto não será só para escolas: deve atender também universidades, cursos e empresas (certificados, treinamentos), clubes, olimpíadas e competições, o público geral sem moeda de valor real e o público geral com a criptomoeda de mercado
- [stated] Quer partidas e provas em ambientes controlados (anti-cola) e uma parte de robótica: tabuleiro de xadrez robótico construído com os alunos, aberto a jogos adicionados pela comunidade
