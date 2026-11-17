# Recrutador: simulações de entrevista nacionais e internacionais

O setup treina você para entrevistas do mesmo jeito que o Professor ensina: um formato por vez, com nota, histórico e o próximo treino escolhido pelo seu ponto fraco. Liga direto ao critério do trimestre 4 do [plano do eixo](../plano-eixo.md): "entrevista em inglês simulada sem travar".

## Como funciona

1. `just recrutador semana` diz qual simulação fazer agora: só entram os formatos do seu trimestre, e ganha o que você ainda não fez ou em que foi pior.
2. `just recrutador entrevista FORMATO` monta o entrevistador e imprime o texto. Você cola no app do Claude e responde. As entrevistas em **inglês** são feitas com o **modo de voz**: falar é o que a entrevista real cobra. Com `--claude`, ela abre no terminal.
3. No fim, você diz "fim da entrevista" e o Claude dá a nota de 1 a 4 (escala de contratação), a nota de cada competência com a evidência, o que um entrevistador exigente anotaria, a pergunta para refazer e, em inglês, as frases que você disse com a versão natural.
4. `just recrutador registrar FORMATO NOTA --melhorar "..."` guarda a nota no Núcleo. O que melhorar vira lição pesquisável (`just buscar entrevista`).
5. `just recrutador progresso` mostra a evolução. Um formato fica **pronto** quando as 3 últimas notas dele são 3 ou 4.

Opções úteis: `--empresa "Nubank"` (usa só o que é público sobre o processo dela) e `--vaga arquivo.txt` (o entrevistador escolhe as perguntas pelos requisitos de uma vaga real que você colou).

## Os formatos

| Formato | Mercado | Idioma | Entra no trimestre |
|---|---|---|---|
| `ingles-conversa`: primeira ligação com recrutador estrangeiro | internacional | inglês | 1 |
| `br-triagem`: triagem de RH | nacional | português | 1 |
| `br-tecnica-dotnet`: técnica .NET com tech lead | nacional | português | 1 |
| `br-case`: defesa de desafio para casa | nacional | português | 2 |
| `fintech-dominio`: dinheiro em software, Pix, conciliação | nacional | português | 2 |
| `bigtech-coding`: algoritmos, estilo big tech | internacional | inglês | 3 |
| `remoto-intl`: seleção para trabalho remoto no exterior | internacional | inglês | 3 |
| `bigtech-design`: system design | internacional | inglês | 4 |
| `amazon-lp`: comportamental com Leadership Principles | internacional | inglês | 4 |

Os formatos ficam em `data/recrutador/formatos.json`. Para acrescentar um (por exemplo, o de uma empresa-alvo), copie um bloco, ajuste as etapas e rode `just check`.

## As suas histórias

Entrevista comportamental é feita de histórias reais. Escreva as suas em `07-estudo-e-carreira/recrutador/historias.md` no vault, a partir do [modelo](historias-modelo.md). O entrevistador lê esse arquivo para aprofundar, e nunca inventa experiência por você. Elas ficam no vault, fora do GitHub.

## Ritmo

Uma simulação por semana, 45 minutos, no lugar de um bloco de Ofício (veja a semana no plano do eixo). Na semana em que houver uma entrevista real marcada, faça duas, no formato dela.

## Limites, com franqueza

- **Não existe acesso ao processo interno de nenhuma empresa.** Os formatos vêm do que as empresas e guias públicos descrevem (as fontes estão em cada formato). "Estilo Amazon" é o formato público dos Leadership Principles, não a entrevista secreta da Amazon.
- **A IA não substitui gente.** A partir do trimestre 3, faça uma simulação por mês com uma pessoa: um dev mais experiente, uma comunidade, ou plataformas de mock interview entre pares. A IA treina volume; a pessoa calibra a nota.
- **A nota da IA é uma estimativa.** Ela tende a ser gentil: o prompt pede um entrevistador exigente, mas confira se a evidência que ela cita justifica a nota.
- **Nada de aluno nas histórias.** Fale de turmas e resultados em geral, sem nomes.
