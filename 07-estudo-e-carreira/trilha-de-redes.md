---
tags: [estudo, redes, infraestrutura, seguranca, portfolio-ams]
tipo: trilha
status: novo
data: 2026-09-28
---

# 🌐 Trilha de Redes

> Base de redes para segurança, servidores e deploy. Pré-requisito da parte de segurança ([[roadmap-seguranca-ofensiva-completo]]) e do homelab ([[trilha-linux-arch-profissional]] Fase 8). Ponto de entrada do dia a dia: [[00-SUMARIO-UNICO-SEQUENCIA-DE-ESTUDO]].

**Ritmo:** 6 a 10 semanas em horas livres chegam a um nível sólido. Cada fase termina com algo testável na própria máquina. Ferramentas (todas no Arch): `ip`, `ping`, `traceroute`, `dig`, `ss`, `nmap`, `curl`, Wireshark.

---

## Fase R1 — Camadas e o que é um pacote
- [ ] Modelo TCP/IP (4 camadas) e relação com o OSI (7)
- [ ] Pacote e encapsulamento (cabeçalho + dados, camada sobre camada)
- [ ] MAC (enlace) vs IP (rede): quando cada um é usado
- [ ] TCP vs UDP: confiável com confirmação vs rápido sem garantia
- [ ] Aperto de mão do TCP (SYN, SYN-ACK, ACK)
- [ ] **Prática:** achar o aperto de mão do TCP numa captura do Wireshark
- [ ] **Evidência:** `notas/redes-01.md` com print e explicação por camada

## Fase R2 — IP, sub-redes e portas
- [ ] IPv4: público vs privado, `localhost` (127.0.0.1); noção de IPv6
- [ ] Sub-redes e máscara (CIDR, `/24`): "minha rede" vs "fora"
- [ ] Gateway padrão
- [ ] **Portas lógicas:** número que identifica o serviço na máquina; portas conhecidas (22, 80, 443, 3306, 5432, 445)
- [ ] Estado da porta: aberta (serviço atende), fechada, filtrada (firewall)
- [ ] **Prática:** `ip a`, `ss -tulpn`, `nmap` numa VM
- [ ] **Evidência:** varredura com `nmap -sV`, explicando cada porta e o serviço por trás

## Fase R3 — Protocolos principais na prática
- [ ] DNS: nome → IP; `dig`, `nslookup`; registros A, CNAME, MX
- [ ] HTTP/HTTPS: métodos, status (200/404/500), cabeçalhos, cookies; `curl -v`
- [ ] TLS: o que a criptografia protege; noção de certificado
- [ ] SSH: chaves vs senha
- [ ] SMB: compartilhamento em rede Windows
- [ ] DHCP: como a máquina recebe IP automático
- [ ] **Evidência:** `notas/redes-03.md` com `dig` e `curl -v` explicados linha a linha

## Fase R4 — A jornada de uma requisição
Amarra tudo: o que acontece do Enter até a página carregar. Saber contar isso = dominar o essencial de redes.

- [ ] Resolução DNS → IP
- [ ] Rota até o destino (`traceroute`)
- [ ] Conexão TCP + aperto de mão na porta 443
- [ ] Negociação TLS
- [ ] Requisição HTTP e resposta
- [ ] NAT, firewall e roteadores no caminho
- [ ] **Prática:** `traceroute` + captura inteira no Wireshark identificando cada etapa
- [ ] **Evidência:** a jornada escrita nas suas palavras (resposta pronta de entrevista)

## Fase R5 — Infraestrutura de rede
- [ ] Switch vs roteador (e em que camada operam)
- [ ] NAT: rede inteira saindo com um IP público
- [ ] Firewall: regras por porta e origem; praticar `ufw`/`nftables`
- [ ] VPN: WireGuard entre duas VMs
- [ ] Proxy reverso: por que um servidor web usa (liga no deploy do Aura)
- [ ] VLAN e segmentação
- [ ] **Evidência:** `homelab/rede.md` com diagrama e regras de firewall comentadas

## Fase R6 — Redes aplicadas ao Aura
- [ ] Rede de containers Docker: bridge, portas publicadas, redes do Compose
- [ ] Por que Postgres, Redis e API se enxergam por nome no Compose
- [ ] Proxy reverso (Nginx/Caddy) na frente; onde o TLS termina
- [ ] Expor serviço com segurança: só portas certas, atrás de firewall, com HTTPS
- [ ] Diagnóstico em container: porta não publicada, serviço em `localhost` vs `0.0.0.0`, DNS interno
- [ ] **Evidência:** README de deploy com o caminho da requisição até o container

## Recursos
- Kurose & Ross (livro) / material do curso de redes de Stanford
- Practical Networking; Professor Messer (trilha Network+)
- Wireshark com capturas próprias
- Certificação opcional: CompTIA Network+ (confira preço e formato atuais)
