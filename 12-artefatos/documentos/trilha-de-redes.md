# Trilha de Redes

Sep 27, 2026 · @Alan Mateus

Base de redes para segurança, servidores e deploy. Cada fase termina com algo testável na sua própria máquina ou laboratório.

## Como usar esta trilha

- **Por que redes é a base:** sem entender rede você não sabe como um ataque chega à máquina, como um servidor é exposto, nem por que o deploy do Aura funciona ou falha. Ela sustenta segurança, servidores e DevOps.
- **Ritmo:** 6 a 10 semanas no seu tempo livre chegam a um nível sólido para entrevista e para as outras trilhas.
- **Regra da evidência:** cada fase termina com algo testável na sua máquina (uma captura, uma varredura, um diagrama). Rede se aprende vendo o pacote, não decorando sigla.
- **Ferramentas, todas gratuitas e no Arch:** `ip`, `ping`, `traceroute`, `dig`, `ss`, `nmap`, `curl` e Wireshark. Você já tem quase tudo.
- **Postura:** monte cada conceito na prática. Toda vez que ler uma teoria, rode o comando que a mostra acontecendo.

## Fase R1: Camadas e o que é um pacote

A ideia central: a rede é organizada em camadas, cada uma cuidando de uma parte. Sua mensagem é embrulhada camada por camada (como envelopes dentro de envelopes) para viajar, e desembrulhada no destino.

- [ ] Modelo TCP/IP (4 camadas) e sua relação com o OSI (7 camadas): saber o que cada camada resolve
- [ ] O que é um pacote e o conceito de encapsulamento (cabeçalho + dados, camada sobre camada)
- [ ] Endereço MAC (camada de enlace) x endereço IP (camada de rede): quando cada um é usado
- [ ] TCP x UDP: conexão confiável com confirmação (TCP) x envio rápido sem garantia (UDP), e quando cada um serve
- [ ] O aperto de mão do TCP (SYN, SYN-ACK, ACK)
- [ ] **Prática:** abrir o Wireshark, acessar um site e achar o aperto de mão do TCP na captura
- [ ] **Evidência:** `notas/redes-01.md` explicando, com um print da captura, o que cada camada fez naquele acesso

## Fase R2: IP, sub-redes e portas

Como as máquinas se localizam e como um serviço é encontrado dentro da máquina.

- [ ] IPv4: estrutura do endereço, IP público x privado, o que é `localhost` (127.0.0.1)
- [ ] Noção de IPv6 (não precisa dominar agora, só reconhecer)
- [ ] Sub-redes e máscara (CIDR, tipo `/24`): entender o que é "minha rede local" x "fora"
- [ ] Gateway padrão: a porta de saída da sua rede para a internet
- [ ] **Portas:** o número que identifica o serviço dentro da máquina; portas conhecidas (22, 80, 443, 3306, 5432, 445)
- [ ] Estado de uma porta: aberta (serviço atende), fechada (nada atende), filtrada (firewall no meio)
- [ ] **Prática:** `ip a` para ver seu IP e máscara; `ss -tulpn` para ver quais portas a sua máquina está servindo; `nmap` numa VM do laboratório
- [ ] **Evidência:** varredura da sua VM com `nmap -sV`, explicando cada porta aberta e o serviço por trás

## Fase R3: Os protocolos principais na prática

Os protocolos que você vai encontrar todo dia, cada um numa porta conhecida.

- [ ] **DNS:** traduz nome (site.com) em IP; testar com `dig` e `nslookup`; entender registros A, CNAME, MX
- [ ] **HTTP/HTTPS:** métodos (GET, POST), códigos de status (200, 404, 500), cabeçalhos, cookies; inspecionar com `curl -v`
- [ ] **TLS:** o que a criptografia protege e o básico do certificado
- [ ] **SSH:** acesso remoto, chaves x senha (você já viu na trilha de segurança)
- [ ] **SMB:** compartilhamento de arquivos, muito comum em rede Windows
- [ ] **DHCP:** como sua máquina recebe IP automaticamente ao conectar
- [ ] **Prática:** `dig site.com`, depois `curl -v https://site.com`, lendo cada linha do que volta
- [ ] **Evidência:** `notas/redes-03.md` com a saída de um `dig` e de um `curl -v` explicadas linha a linha

## Fase R4: A jornada de uma requisição

A fase que amarra tudo: seguir o que acontece quando você digita um endereço e aperta Enter. Se você souber contar essa história inteira, dominou o essencial de redes.

- [ ] O navegador resolve o nome via DNS e obtém o IP
- [ ] Descobre o gateway e a rota até o destino (`traceroute`)
- [ ] Abre conexão TCP com o aperto de mão na porta 443
- [ ] Negocia o TLS e monta o canal criptografado
- [ ] Envia a requisição HTTP e recebe a resposta
- [ ] O pacote passou por NAT, firewall e vários roteadores no caminho
- [ ] **Prática:** `traceroute site.com` para ver os saltos; capturar o acesso inteiro no Wireshark e identificar cada etapa acima
- [ ] **Evidência:** escrever a jornada completa nas suas palavras — este texto é praticamente a resposta pronta para a pergunta clássica de entrevista

## Fase R5: Infraestrutura de rede

Os equipamentos e mecanismos que fazem a rede existir. Aqui a rede vira algo que você administra, não só usa.

- [ ] Switch x roteador: o que cada um faz e em que camada opera
- [ ] **NAT:** por que sua rede inteira sai para a internet com um IP público só, e o que isso esconde
- [ ] **Firewall:** regras que liberam ou bloqueiam por porta e origem; praticar com `ufw` ou `nftables` no seu Linux
- [ ] **VPN:** túnel criptografado entre redes; montar um WireGuard entre duas máquinas do laboratório
- [ ] **Proxy e proxy reverso:** o que é e por que um servidor web usa (liga direto no deploy do Aura)
- [ ] VLAN e segmentação de rede: separar o que não precisa se enxergar (base de defesa)
- [ ] **Prática:** configurar o firewall numa VM liberando só as portas necessárias; subir um WireGuard
- [ ] **Evidência:** `homelab/rede.md` com um diagrama da sua rede de laboratório e as regras de firewall comentadas

## Fase R6: Redes aplicadas a servidores e ao Aura

Fechar o ciclo aplicando tudo no que você já constrói.

- [ ] Como um container Docker recebe rede: bridge, portas publicadas, redes internas do Compose
- [ ] Por que os serviços do Aura (Postgres, Redis, API) se enxergam por nome dentro do Compose
- [ ] Proxy reverso na frente da aplicação (Nginx ou Caddy) e onde o TLS é terminado
- [ ] Expor um serviço com segurança: só as portas certas, atrás de firewall, com HTTPS
- [ ] Diagnosticar problema de rede em container: porta não publicada, serviço em `localhost` em vez de `0.0.0.0`, DNS interno
- [ ] **Prática:** subir um sistema do Aura atrás de proxy reverso com HTTPS numa VM, acessível só pelas portas que você liberou
- [ ] **Evidência:** README do deploy explicando o caminho da requisição até o container e as regras de firewall

## Recursos e currículo

**Para estudar (gratuitos, salvo indicação):**

- Curso *Computer Networking* da Stanford / o clássico livro de Kurose & Ross (há material do curso online)
- Practical Networking (canal e site) para explicações visuais
- Professor Messer, trilha Network+ (vídeos gratuitos), boa para cobrir a teoria de ponta a ponta
- Wireshark: praticar com capturas próprias, o melhor professor de rede que existe

**Certificação (opcional, confira preço e formato atuais):** CompTIA Network+ é a de entrada mais reconhecida; ajuda em filtro de RH, mas os laboratórios e write-ups pesam mais.

**Linhas para o currículo (cada uma com evidência):**

- **Redes:** TCP/IP, DNS, HTTP/TLS, sub-redes, NAT, firewall e VPN, com laboratório próprio de VMs e análise de tráfego em Wireshark.
- **Diagnóstico:** identifico e resolvo problemas de conectividade com `nmap`, `ss`, `dig`, `traceroute` e Wireshark.
- **Rede de aplicações:** configuro rede de containers Docker e proxy reverso com HTTPS para deploy seguro.

**Onde encaixa:** esta trilha é pré-requisito da Fase S2 (segurança) e da Fase 8 (homelab) da Trilha Linux. Faça-a cedo; ela destrava as outras duas.

---

<!-- conexoes:inicio -->
## 🔗 Onde isto entra no plano

- [🎯 Sumário Único de Estudo — O Único Arquivo Que Você Abre](../PLANO-UNICO-AMtech.md)
- [Método de Estudo — Documento Único](../../07-estudo-e-carreira/metodo-de-estudo.md)
- [🌐 Trilha de Redes](../../07-estudo-e-carreira/trilha-de-redes.md)

🗂️ Voltar ao [índice dos artefatos](../00-INDICE-DOS-ARTEFATOS.md) · [mapa de conexões](../01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
