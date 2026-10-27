# Gabarito — Lab. Software e Lab. Hardware (Professor)

Oct 27, 2026 · @Alan Mateus

Documento do professor. As respostas seguem os blocos do quadro de cada aula; o bloco de origem aparece entre parênteses.

## Laboratório de Software

### Exercícios (1 a 18)

1. **pwd** mostra a pasta atual. **ls -la** lista os arquivos com as permissões. (A)
2. **mkdir -p bsd-cassino/src bsd-cassino/docs bsd-cassino/scripts** (A)
3. **>** grava a saída no arquivo apagando o que tinha. **>>** acrescenta no final, sem apagar. (B)
4. Passa a saída de um comando como entrada para o próximo. (B)
5. **grep "PERDEU" apostas.log** (B)
6. **grep "PERDEU" apostas.log | wc -l** (B)
7. **tail -3 apostas.log** (B)
8. r = 4, w = 2, x = 1. O 6 = 4 + 2 = ler e escrever. (C)
9. Só o dono lê e escreve; grupo e outros não têm nenhuma permissão. Precisa disso porque quem lê a chave privada consegue gastar os PRIMEs da carteira. (C)
10. (D)
    - \#!/bin/bash: indica que o script roda no bash.
    - # Backup do banco...: comentário, não executa.
    - DATA=$(date +%Y-%m-%d): guarda a data de hoje na variável DATA.
    - mkdir -p backup: cria a pasta backup, se não existir.
    - cp banco.db backup/banco\_$DATA.db: copia o banco com a data no nome.
    - echo ... >> backup.log: registra no fim do backup.log que o backup foi feito.
11. **chmod +x backup.sh** e **./backup.sh** (D)
12. **cp backup/banco\_2026-10-21.db banco.db** (D)
13. 3 cópias, em 2 mídias diferentes, com 1 fora do local. (D)
14. Git é o programa instalado no computador, que funciona sem internet. GitHub é o site que guarda o repositório na nuvem para a equipe. (E)
15. Trabalho → **git add** → Staging → **git commit** → Repositório (→ **git push** → GitHub). (E)
16. Lista o que o Git não deve enviar. Arquivos: chave\_privada.pem, banco.db e a pasta backup/. (F)
17. Backup é cópia dos dados; commit é cópia (versão) do código. Um não substitui o outro. (G)
18. **Desafio** (C e F): a chave privada ficou pública no GitHub, e qualquer pessoa pode gastar os PRIMEs da carteira. Antes, ele deveria ter colocado a chave no .gitignore (e mantido com chmod 600), e não dar git add nela.
    - Resposta completa: cita o risco (gastar os PRIMEs) **e** a prevenção (.gitignore). Se o aluno disser também que a chave exposta deve ser trocada por uma nova, vale como resposta excelente, mas não é obrigatório porque não está no quadro.

### Avaliação

| Questão | Resposta | Bloco |
| --- | --- | --- |
| 1 | a) pwd | A |
| 2 | c) Acrescenta a saída no final do arquivo | B |
| 3 | b) grep "PERDEU" apostas.log \| wc -l | B |
| 4 | d) Só o dono pode ler e escrever | C |
| 5 | c) Rodar chmod +x backup.sh | D |
| 6 | a) 3 cópias, 2 mídias diferentes, 1 fora do local | D |
| 7 | d) .gitignore | F |
| 8 | b) Uma "fotografia" do estado completo da VM | I |
| 9 | b) Criar uma imagem, cópia exata do disco | J |
| 10 | d) O Editor de Política de Grupo Local | K |
| 11 | a) fsck | L |
| 12 | c) sudo apt purge nome | H |
| Extra | b) grep Failed /var/log/auth.log | K |

**Desafio — resposta esperada** (Blocos L, D e J), nesta ordem:

1. Verificar e corrigir o sistema de arquivos com o **fsck**, com a partição desmontada. (L)
2. Se o banco continuar com defeito, **restaurar o último backup**: cp backup/banco\_DATA.db banco.db. Os saldos voltam como estavam no último backup. (D)
3. Se o sistema inteiro estiver comprometido, **restaurar a imagem de sistema** da máquina de validação (ex.: Clonezilla). (J)

Sugestão de correção: cita o fsck = 1/3; cita a restauração do backup = 1/3; cita a imagem de sistema ou a regra 3-2-1 = 1/3.

## Laboratório de Hardware

### Exercícios (1 a 18)

1. (A)
   1. Desligar e tirar da tomada.
   2. Tirar anéis, relógios e correntes.
   3. Colocar a pulseira e usar a manta, as duas ligadas ao aterramento.
   4. Usar ferramentas com isolamento.
   5. Separar os parafusos em um recipiente.
   6. Bancada limpa, seca e sem poeira.
2. NR-12: a máquina deve estar parada, desenergizada e bloqueada durante a manutenção. NR-10: a prioridade é a prevenção. (A)
3. Por causa do risco de choque e de curto-circuito. (A)
4. Iguala a carga elétrica do corpo com a do equipamento. Deve estar ligada ao aterramento. (A e H)
5. 10 V já podem danificar um chip; o ser humano só sente acima de 3.000 V. (A)
6. Tensão contínua: **VDC** (V⎓). (B)
7. Amarelo +12 V; vermelho +5 V; laranja +3,3 V; preto 0 V (GND). (B)
8. P = 12 × 8 = **96 W**. (C)
9. 250 × 1,2 = **300 W**. (C)
10. Porque a máquina do projeto trabalha sob carga, e é sob estresse que ela consome mais e exige mais da fonte e do cooler. A medição em repouso serve de comparação. (C e G)
11. Power-On Self Test (autoteste ao ligar), feito pela BIOS/UEFI. (D)
12. Bipes curtos repetidos: memória RAM. 1 longo + 3 curtos: placa de vídeo. (D)
13. Porque os códigos de bipe mudam de fabricante para fabricante. (D)
14. (E)
    1. Entrevista.
    2. Verificação visual.
    3. Boot mínimo.
    4. Testar componentes, um por vez.
    5. Ferramentas de software.
    6. Confirmar e reparar.
    7. Documentar.
15. Ligar só o mínimo para testar. Ficam conectadas: placa-mãe, CPU e 1 pente de RAM. (E)
16. A poeira funciona como isolante térmico e a temperatura sobe. Thermal throttling = o processador reduz o desempenho para não superaquecer. (F)
17. Faz o sistema conversar com a placa de vídeo para ela processar o hash. Deve ser baixado do site do fabricante. (F)
18. **Desafio** (E, C e F), ordem esperada:
    1. Entrevista e verificação visual: poeira, cabos soltos, cooler girando.
    2. Acompanhar a temperatura no HWMonitor durante o estresse.
    3. Se a temperatura subir: limpar a poeira, conferir o cooler e reaplicar a pasta térmica.
    4. Se a temperatura estiver normal: conferir a potência da fonte (consumo sob estresse + 20%) e medir as tensões com o multímetro.
    5. Trocar uma peça por vez e documentar.
    - Sugestão de correção: superaquecimento/cooler = 1/3; fonte/potência = 1/3; seguir a ordem (uma peça por vez, documentar) = 1/3.

### Avaliação

| Questão | Resposta | Bloco |
| --- | --- | --- |
| 1 | a) Desligar e tirar da tomada | A |
| 2 | c) Igualar a carga elétrica do corpo com a do equipamento | A |
| 3 | b) O terra | H |
| 4 | d) +12 V | B |
| 5 | c) VDC | B |
| 6 | a) 300 W | C |
| 7 | d) Memória RAM | D |
| 8 | b) Placa-mãe, CPU e 1 pente de RAM | E |
| 9 | b) Superaquecimento e thermal throttling | F |
| 10 | d) Evitar que a placa-mãe encoste no metal e cause curto | I |
| 11 | a) SSD M.2 NVMe | J |
| 12 | c) Instalar a CPU na placa-mãe, fora do gabinete | I |
| Extra | b) 22 mm de largura e 80 mm de comprimento | J |

**Desafio — resposta esperada** (Blocos A, H, I e C):

1. **Bancada:** desligado da tomada, sem anéis e relógio, pulseira e manta ligadas ao terra, ferramentas isoladas, parafusos separados, bancada limpa. (A e H)
2. **Montagem:** CPU, cooler, RAM e SSD M.2 fora do gabinete; espaçadores; placa-mãe; fonte; drives SATA; cabos; GPU por último; testar antes de fechar. (I)
3. **Medições:** tensões da fonte com o multímetro em VDC; consumo com wattímetro em repouso e sob estresse; conferir se a fonte suporta o consumo + 20%; anotar em docs/HARDWARE\_SETUP.md. (B e C)

Sugestão de correção: bancada segura = 1/3; sequência de montagem (pelo menos CPU primeiro, espaçadores e GPU por último) = 1/3; medições em repouso e sob estresse = 1/3.
