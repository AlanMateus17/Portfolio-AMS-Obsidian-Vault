# Atacante do laboratório: as ferramentas entram na hora do build (com internet); depois o container
# roda só na rede interna, sem saída. Ferramentas com janela (Burp, ZAP desktop) ficam na VM Kali.
FROM kalilinux/kali-rolling
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      nmap sqlmap nikto ffuf gobuster whatweb curl wget netcat-openbsd dnsutils iputils-ping \
      python3 python3-requests jq seclists ca-certificates \
 && rm -rf /var/lib/apt/lists/*
WORKDIR /trabalho
