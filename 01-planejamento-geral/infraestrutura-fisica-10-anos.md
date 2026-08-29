---
tags: [planejamento, infraestrutura, portfolio-ams]
tipo: planejamento
status: completo
---

# Infraestrutura Física — Arquitetura de 10 Anos
### Trazido de uma conversa anterior (13/08/2026) — 11 camadas, cada uma só ativa quando a frente de renda correspondente começar de verdade

> **Critério geral por trás de tudo isso:** tecnologia madura e "chata" (boring tech) — LTS, padrões abertos, pouca dependência de vendor — porque é isso que sobrevive 10 anos só com manutenção, sem precisar reescrever nada. Diferente do [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]] (que é sobre o que estudar), este documento é sobre **o que comprar e configurar fisicamente**, e quando.

---

## As 11 camadas, o que cada uma resolve

| # | Camada | Resolve o quê |
|---|---|---|
| 1 | Estação de Trabalho | A máquina onde você programa e estuda |
| 2 | Rede | Separa e protege tudo (casa, clientes, servidores) |
| 3 | NAS e Backup | Memória permanente — nada se perde |
| 4 | Ambiente de Dev | Onde os sistemas são construídos e testados |
| 5 | Produção | Onde os SaaS ficam no ar gerando renda |
| 6 | Segurança | Protege senhas e acessos de tudo |
| 7 | Estudos | Matemática, idiomas, currículo pessoal |
| 8 | Assistência Técnica | Reparo de celular/computador (AuraFix) |
| 9 | Oficina Automotiva | Auto elétrica e som automotivo |
| 10 | Robótica e IoT | Robôs para casa, empresa e propriedades rurais |
| 11 | Infoprodutos | Cursos, ebooks, conteúdo pago |

---

## Camada 1 — Estação de trabalho principal

Precisa aguentar simultaneamente: .NET 10 + Docker + PostgreSQL + Next.js local, várias IDEs abertas, e futuramente um lab de pentest (OSCP).

| Item | Especificação |
|---|---|
| CPU | Ryzen 7/9 ou Intel i7/i9 (múltiplos núcleos > clock alto, por causa de containers) |
| RAM | 32GB mínimo, 64GB se o orçamento permitir |
| Disco | NVMe 1TB+ |
| GPU | **Revisado:** inicialmente marcada como dispensável — mas se você for produzir conteúdo/vídeo com regularidade (Camada 11), uma GPU de entrada (ex: RTX 4060) acelera renderização de forma real. Reconsiderar essa peça se Infoprodutos entrar no radar. |

## Camada 2 — Rede

- **Roteador/Firewall:** OPNsense/pfSense (mini-PC dedicado) ou Ubiquiti UniFi — firmware que você controla, sem ficar refém de fabricante
- **VLANs separadas:** rede doméstica | rede de dev/servidores | rede da assistência técnica (isola dispositivo de cliente por segurança e responsabilidade)
- **VPN (Wireguard):** acesso remoto seguro ao NAS/servidores de qualquer lugar

## Camada 3 — NAS e Backup

Espinha dorsal de tudo: apostilas, código-fonte, ISOs da assistência técnica, dados financeiros, gestão documental.

- RAID 1 (redundância local) + estratégia 3-2-1 (3 cópias, 2 mídias, 1 fora do local)
- Serve como Git self-hosted (Gitea) e registry Docker privado
- Se Infoprodutos (Camada 11) entrar: dimensionar pensando em vídeo bruto, que ocupa espaço numa escala totalmente diferente de código/PDF — a conta inicial de "2 discos de 4TB" pode ficar apertada rápido

## Camada 4 — Ambiente de desenvolvimento

Replica em local o que roda em produção, evitando "funciona na minha máquina":
- Docker Compose padronizado (mesma stack do AuraPOS: .NET 10, PostgreSQL, Next.js)
- CI/CD self-hosted (Gitea Actions) rodando testes a cada push

## Camada 5 — Produção (hospedagem dos SaaS)

Aqui não vale self-host total — é onde entra renda de verdade, precisa de uptime:
- VPS (Hetzner/DigitalOcean)
- Traefik/Nginx como reverse proxy + SSL automático (Let's Encrypt)
- Backup automatizado do banco de produção puxando pro NAS

## Camada 6 — Segurança (dobra como lab do OSCP)

- Vaultwarden (Bitwarden self-hosted) para senhas
- 2FA em tudo
- Uptime Kuma — monitoramento simples, saber se algo caiu antes do cliente reclamar

## Camada 7 — Estudos

- Obsidian + Anki, sincronizados via NAS
- O sistema de currículo (Topics/Subtopics/Exercises) pode rodar como mais um container na própria infra

## Camada 8 — Assistência Técnica (AuraFix)

- Repositório de ISOs no NAS
- Rede isolada (VLAN da Camada 2) — dispositivo de cliente nunca toca a rede de dev

## Camada 9 — Oficina Automotiva

Auto elétrica e som automotivo. Kit próprio, separado do resto — não compartilha ferramenta com as camadas de TI.

## Camada 10 — Robótica e IoT (casa, empresa, propriedade rural)

- **Conectividade:** Wi-Fi doméstico **não resolve** ambiente rural — é a causa nº1 de projeto de IoT agrícola que nunca sai do papel. 4G/LTE como fallback pra robôs que precisam de mais banda (câmeras)
- **Arquitetura offline-first:** o robô funciona sozinho no campo e sincroniza quando a conexão voltar, nunca depende de conexão constante
- **Dados:** banco de série temporal (InfluxDB ou TimescaleDB) — dado de sensor não cabe bem no modelo relacional já usado no resto do portfólio. Pode virar um sistema Aura novo (ex: "AuraAgro"), com dashboard/backend rodando na Camada 5 já existente — só a coleta de campo é nova
- **Problemas a evitar:** testar protótipo direto com animal real antes de validar em bancada; não ruggedizar (poeira/umidade/temperatura derruba eletrônica de prototipagem rápido); não prever autonomia de energia (bateria/solar); misturar firmware e software de aplicação no mesmo repositório

## Camada 11 — Produção de Conteúdo e Infoprodutos

- **Captação:** câmera/webcam boa, microfone dedicado (áudio importa mais que imagem em curso gravado), iluminação básica, espaço com tratamento acústico mínimo
- **Edição de vídeo:** GPU de entrada relevante aqui — ver revisão na Camada 1
- **Armazenamento:** dimensionar o NAS pra vídeo bruto, escala diferente de código/apostila

---

## Ordem de implementação no tempo

| Fase | Quando | O que construir |
|---|---|---|
| 1 | Mês 1–2 | Estação de trabalho + rede básica (Camadas 1 e 2) |
| 2 | Mês 2–4 | NAS + backup 3-2-1 + gestão documental (Camada 3) |
| 3 | Mês 3–6 | Ambiente de dev padronizado (Camada 4) |
| 4 | Mês 6+ | Produção — VPS, AuraPOS, AuraWealth (Camada 5) |
| Paralelo | Desde o início | Segurança (6) e Estudos (7) |
| Ao abrir assistência técnica | Sob demanda | VLAN dedicada + AuraFix (Camada 8) |
| Ao terminar curso de auto elétrica | Sob demanda | Oficina automotiva (Camada 9) |
| Ao iniciar projeto de robótica/agro | Sob demanda | Robótica e IoT (Camada 10) |
| Ao decidir gravar o 1º curso | Sob demanda | Infoprodutos (Camada 11) |
| Antes da 2ª/3ª fonte de renda | Urgente, transversal | Contador + gestão fiscal — ver [[estrutura-juridica-amtech]] |

**Por onde começar de verdade, se a pergunta for "o que eu faço amanhã":** só estação de trabalho (1) → roteador com VLANs básicas (2) → NAS com backup automático (3). As Camadas 9, 10 e 11 só entram quando a frente de renda correspondente estiver prestes a começar — montar bancada de auto elétrica hoje, sem cliente ainda, é dinheiro parado.

---

## Orçamento estimado

| Item | Custo aproximado | Tipo |
|---|---|---|
| Estação de trabalho (com GPU p/ vídeo) | R$ 7.500 – 11.000 | Único |
| Rede (roteador + switch + AP) | R$ 1.500 – 3.000 | Único |
| NAS + discos (considerando vídeo) | R$ 3.000 – 5.000 | Único |
| Nobreak | R$ 500 – 800 | Único |
| Kit oficina automotiva (Camada 9) | R$ 2.500 – 5.000 | Único — só na fase correspondente |
| Kit robótica/IoT inicial (Camada 10) | R$ 1.500 – 3.500 | Único — só na fase correspondente |
| Kit de gravação (Camada 11) | R$ 1.200 – 2.500 | Único — só na fase correspondente |
| VPS de produção | R$ 30 – 80 / mês | Recorrente |
| Backup em nuvem | R$ 20 – 50 / mês | Recorrente |
| Contador | R$ 150 – 400 / mês (varia por regime — ver [[estrutura-juridica-amtech]] pro valor atualizado com loja física) | Recorrente |

---

## Checklist de manutenção

**Mensal:** conferir se os backups automatizados rodaram · revisar alertas do Uptime Kuma
**Trimestral:** testar uma restauração de backup de verdade · atualizar dependências dos projetos
**Anual:** atualizar firmware de roteador/switch/NAS · revisar senhas e 2FA de todas as contas-mestre · conversar com o contador sobre enquadramento das atividades ativas no ano

---

## ⚠️ Sinal de alerta pra você mesmo — TDAH e hiperfoco em setup

Montar infraestrutura é divertido e vicia — mas infraestrutura não gera renda sozinha, só sustenta quem já está trabalhando. **Se você perceber que está há mais de 2 semanas seguidas mexendo em servidor/rede sem nenhuma entrega de cliente ou aula no meio, é sinal de estar fugindo da parte difícil (vender, entregar, aparecer) pela parte confortável (configurar).**

---

## 🔗 Documentos relacionados
- [[setup-ambiente-trabalho-final]] — a fatia de software desta arquitetura (Camada 4), já em execução no notebook atual
- [[estrutura-juridica-amtech]] — a gestão fiscal transversal citada na tabela de fases
- [[plano-mestre-frentes-alan]] — as frentes de renda que disparam cada camada sob demanda
