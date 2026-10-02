---
tags: [estudo, seguranca, recursos, links, ferramentas, certificacoes, portfolio-ams]
tipo: estudo
status: ativo
companion: "[[roadmap-seguranca-ofensiva-completo]]"
---

# 🔗 Recursos e Links — Segurança Ofensiva

> [!important] Companion do [[roadmap-seguranca-ofensiva-completo]]
> Todos os links foram verificados. Priorize sempre fonte oficial. Recurso gratuito marcado com 🆓, pago com 💲.

---

## 🎓 Plataformas de Prática (Labs)

| Plataforma | Foco | Custo | Nível |
|-----------|------|-------|-------|
| **TryHackMe** 🆓💲 | Guiado, iniciante | Free / ~$14/mês | 0-2 |
| **HackTheBox** 🆓💲 | Máquinas realistas | Free / ~$14/mês | 1-4 |
| **HTB Academy** 💲 | Teoria + prática modular | Cubes | 0-4 |
| **PortSwigger Web Academy** 🆓 | Web (o melhor gratuito) | Grátis | 1-3 |
| **Proving Grounds (OffSec)** 💲 | Prep OSCP | ~$19/mês | 2-3 |
| **VulnLab** 💲 | AD e Red Team | ~€8/mês | 3-4 |
| **Xillutec / Sacthreat / Zhero** 💲 | AD realista | Varia | 3-4 |
| **PentesterLab** 💲 | Web + code review | ~$20/mês | 1-3 |
| **Vulnhub** 🆓 | VMs para baixar | Grátis | 1-3 |
| **PwnCollege** 🆓 | Binário/exploit (ASU) | Grátis | 2-5 |
| **CryptoHack** 🆓 | Criptografia | Grátis | 1-4 |
| **OverTheWire** 🆓 | Wargames Linux | Grátis | 0-2 |
| **Root-Me** 🆓💲 | Desafios variados | Freemium | 1-4 |
| **CTFtime** 🆓 | Agenda de CTFs | Grátis | Todos |

> [!tip] Progressão ideal de labs
> TryHackMe (base) → HTB Academy (teoria) → HackTheBox (prática) → Proving Grounds (prep OSCP) → VulnLab (AD/Red Team). A mesma lógica de dificuldade crescente da [[metodo-de-estudo]].

---

## 📜 Certificações — Links Oficiais

**Entrada:** eJPT (INE/eLearnSecurity) — [ine.com](https://ine.com) 💲 | PNPT (TCM Security) — [certifications.tcm-sec.com](https://certifications.tcm-sec.com) 💲

**Core:** OSCP (PEN-200) — [offsec.com](https://www.offsec.com) 💲💲💲 | CRTO (Zero-Point Security) — [training.zeropointsecurity.co.uk](https://training.zeropointsecurity.co.uk) 💲💲

**Active Directory:** CRTP / CRTE / CARTP (Altered Security) — [alteredsecurity.com](https://www.alteredsecurity.com) 💲💲

**Avançado:** OSEP / OSED / OSEE (OffSec) 💲💲💲 | GXPN / GICSP (SANS/GIAC) — [giac.org](https://www.giac.org) 💲💲💲💲

**Mobile:** eMAPT (INE) 💲

> [!note] Sua trilha registrada
> No [[plano-estudos-basico-avancado-entrelacado]]: `CompTIA A+/Network+ → Security+ → CCNA (opcional) → eJPT → OSCP`. O resto é continuação além do OSCP.

---

## 🛠️ Ferramentas Essenciais por Categoria

**Distros:** Kali Linux, ParrotOS, BlackArch, Commando VM (Windows), Flare-VM (malware analysis).

**Recon/OSINT:** Nmap, Masscan, RustScan, Amass, Subfinder, theHarvester, Shodan, Censys, SpiderFoot, Recon-ng, Maltego, TruffleHog, gitleaks.

**Web:** Burp Suite, OWASP ZAP, sqlmap, ffuf, feroxbuster, Gobuster, Nikto, wpscan, XSStrike, commix, tplmap, jwt_tool, nuclei.

**AD/Windows:** BloodHound, SharpHound, PowerView, Impacket (suite completa), CrackMapExec/NetExec, Certipy, Rubeus, Mimikatz, Responder, ntlmrelayx, kerbrute, Coercer, Certify, Whisker.

**C2:** Sliver 🆓, Havoc 🆓, Mythic 🆓, Covenant 🆓, PoshC2 🆓, Merlin 🆓, Cobalt Strike 💲💲💲.

**Exploit Dev:** Immunity Debugger + Mona, x64dbg, WinDbg, GDB + GEF/pwndbg, pwntools, ROPgadget, ropper, Ghidra 🆓, IDA Free/Pro, Cutter.

**Password/Hash:** Hashcat, John the Ripper, Hydra, Medusa, CeWL, hcxtools.

**Pivoting:** ligolo-ng (padrão atual), chisel, socat, sshuttle, proxychains-ng.

**Cloud:** Pacu, ScoutSuite, Prowler, CloudFox (AWS), ROADtools, AADInternals, GraphRunner, TokenTactics (Azure), kube-hunter, peirates (K8s).

**Mobile:** apktool, jadx, MobSF, Frida, Objection, Drozer (Android), Ghidra, class-dump (iOS).

**Wireless:** Aircrack-ng suite, hostapd-wpe, Kismet, hcxdumptool, Bettercap.

**Detection/Blue (para entender defesa):** YARA, Sigma, Atomic Red Team, Caldera, Volatility 3, Chainsaw, Hayabusa, KAPE, Velociraptor.

---

## 📚 Livros Fundamentais

**Base:** *The Web Application Hacker's Handbook* (Stuttard/Pinto), *Penetration Testing* (Georgia Weidman), *The Hacker Playbook 3* (Kim), *RTFM: Red Team Field Manual*.

**Active Directory:** *The Dog Whisperer's Handbook* 🆓 (BloodHound), documentação ired.team 🆓, adsecurity.org 🆓.

**Exploit Dev:** *Hacking: The Art of Exploitation* (Erickson), *The Shellcoder's Handbook*, *Practical Malware Analysis* (Sikorski/Honig), *Windows Internals* (Russinovich).

**Evasão/Red Team:** *Evading EDR* (Matt Hand), *Antivirus Bypass Techniques*.

**Web moderno:** *Real-World Bug Hunting* (Yaworski), *Bug Bounty Bootcamp* (Vickie Li).

**Cloud:** *Hacking Kubernetes*, *Penetration Testing Azure for Ethical Hackers*.

---

## 🎥 Canais e Criadores

**YouTube:** IppSec (walkthroughs HTB — essencial), John Hammond, LiveOverflow, STÖK, NahamSec, The Cyber Mentor (TCM), Conda, David Bombal, Gynvael Coldwind, 13Cubed (DFIR).

**Blogs/Sites técnicos:** ired.team, adsecurity.org, harmj0y.net, thehackerrecipes.com, hausec.com, dirkjanm.io, specterops.io/blog, posts.specterops.io, PortSwigger Research, orange.tw.

**Newsletters:** tl;dr sec, Return on Security, Unsupervised Learning (Daniel Miessler), Cand.

---

## 🇧🇷 Recursos Brasileiros

**Comunidades:** Gurus of Information Security (GRIS), Mente Binária (mentebinaria.com.br 🆓 — reverse engineering em PT-BR), Papers We Love BR, DEF CON Group São Paulo.

**Eventos:** H2HC (Hackers to Hackers Conference), Roadsec, BSides (SP/BH/etc.), Cryptorave, Silver Bullet.

**Legislação (leitura obrigatória):** Lei 12.737/2012, Marco Civil (12.965/2014), LGPD (13.709/2018) — todas em planalto.gov.br 🆓.

> [!warning] Framework legal
> Ver seção 1.8 do [[roadmap-seguranca-ofensiva-completo]]. Sem autorização escrita e assinada, teste = crime no Brasil. Isso vale igual para o serviço de pentest como fonte de renda.

---

## 🧪 Ambientes de Lab Locais (montar em casa)

**AD para praticar:** GOAD (Game of Active Directory) 🆓, DetectionLab 🆓, vulnerable-AD scripts, Ludus (automação de lab).

**Web vulnerável:** DVWA, OWASP Juice Shop, WebGoat, bWAPP, VAmPI (API), crAPI (API).

**Malware/RE isolado:** Flare-VM + REMnux em rede isolada (host-only), snapshots sempre.

> [!warning] Isolamento obrigatório
> Malware analysis SEMPRE em VM isolada, rede host-only, snapshot antes. Nunca na máquina principal. Conecta com o `Born2beroot` da [[trilha-42-circles-oficial-verificado]] — a mesma disciplina de VM hardened.

---

## 🗓️ Rotina de Manutenção de Conhecimento

- **Diário:** 1 máquina/lab ou 1 lab PortSwigger
- **Semanal:** 1 walkthrough IppSec, ler 2-3 posts técnicos, acompanhar CVEs relevantes
- **Mensal:** 1 CTF, revisar notas (Obsidian/CherryTree), tentar 1 técnica nova
- **Anual:** revisar este roadmap, avaliar próxima certificação

> [!tip] Note-taking
> Mantenha suas próprias notas de técnica em formato consultável. Você já usa Obsidian — crie uma pasta dedicada de pentest com template por máquina (recon → enum → exploit → privesc → loot). Mesmo princípio da [[metodo-de-estudo]]: documentar para reter.

---

## 🔗 Documentos relacionados
- [[roadmap-seguranca-ofensiva-completo]] — o roadmap de 6 níveis que este companion suporta
- [[plano-estudos-basico-avancado-entrelacado]] — Fase 12
- [[biblioteca-recursos-por-passo]] — recursos gerais de todos os outros passos do plano
- [[mapa-mestre-prioridade-total]] — onde a segurança ofensiva entra na prioridade geral

---

*Companion do Roadmap v3.0 — Agosto/2026. Todos os links verificados na data de criação; revisar anualmente.*
