---
tags: [estudo, seguranca, pentest, red-team, roadmap, portfolio-ams]
tipo: estudo
status: ativo
companion: "[roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md)"
---

# 🛡️ Roadmap Completo — Segurança Ofensiva

> [!important] Como usar este documento
> Este é um mapa de conhecimento progressivo em **6 níveis**. Cada nível é pré-requisito do próximo. Os callouts indicam recursos prioritários e erros comuns a evitar.
>
> **Integração com o resto do vault:** este roadmap é a versão aprofundada da Fase 12 do [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md). O ponto de entrada real na sua sequência é depois do Bloco 8 (arquitetura consolidada), rodando em paralelo — mesma posição da [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md). Overlap já mapeado: rede/Linux (NetPractice e Born2beroot da 42), criptografia básica (episódios do Akitando em [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md)), OWASP defensivo (Fase 2.2). Não reestude o que essas trilhas já cobrem.

---

## 🗺️ Trilha de Certificações

```
eJPT → OSCP → CRTO → CRTP → CRTE → OSEP → OSED
                                          ├→ CARTP (Azure)
                                          ├→ CRTL (Lead)
                                          └→ GXPN (SANS)
OSCP → eMAPT (Mobile)
```

| Cert | Provedor | Foco Principal | Após |
|------|----------|----------------|------|
| **eJPT** | INE | Pentest básico, web, network | — |
| **OSCP** | OffSec | Metodologia completa, AD básico, BOF | eJPT |
| **CRTO** | Zero-Point | C2 operations, evasion, red team | OSCP |
| **CRTP** | Altered Security | AD kill chain completo | CRTO |
| **CRTE** | Altered Security | AD avançado, multi-forest, ADCS | CRTP |
| **OSEP** | OffSec PEN-300 | Hardened targets, evasion avançada | CRTE |
| **OSED** | OffSec EXP-301 | Exploit development, ROP, SEH | OSEP |
| **eMAPT** | INE | Mobile (Android/iOS) pentest | OSCP |
| **CARTP** | Altered Security | Azure red team completo | CRTE |
| **CRTL** | Zero-Point | Red Team Lead operations | OSED |
| **GICSP** | SANS | OT/ICS/SCADA security | OSED |

> [!note] Como isso se encaixa na sua trilha já decidida
> Sua trilha registrada no [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md) é `CompTIA A+/Network+ → Security+ → CCNA (opcional) → eJPT → OSCP`. As certificações acima (CRTO em diante) são a continuação natural além do OSCP, para quem vai a fundo em red team profissional — não precisa decidir sobre elas agora.

---

# NÍVEL 0 — Fundamentos Obrigatórios

> [!warning] Não pule esta etapa
> Profissionais que pulam fundamentos chegam ao OSCP e travam.

## 0.1 Redes e Protocolos
- Modelo OSI (7 camadas), TCP/IP (handshake, flags SYN/ACK/FIN/RST/PSH/URG), UDP
- **DNS** — zonas, registros (A, AAAA, MX, NS, PTR, TXT, CNAME, SRV), transferência de zona
- **HTTP/HTTPS** — métodos, headers, cookies, sessões, TLS handshake, SNI, HSTS, HTTP/2
- **SMB** — v1/v2/v3, autenticação NTLM, shares, null sessions
- **Kerberos** — AS-REQ/AS-REP, TGT, TGS, encryption types (RC4, AES128/256)
- **LDAP/LDAPS**, **NTLM** (Challenge/Response, NTLMv1 vs NTLMv2, relay), **RPC/DCOM/WMI**
- ARP, ICMP, DHCP, SNMP, SSH, FTP
- Ferramentas de análise: Wireshark, tcpdump, netstat/ss, ncat/nc

## 0.2 Sistemas Operacionais
**Windows (crítico):** registro (HKLM/HKCU/etc.), SIDs, permissões NTFS/ACL/DACL/SACL, serviços/processos/threads/tokens, UAC, PowerShell (execution policy, remoting, logging), Event IDs críticos (4624, 4625, 4648, 4662, 4672, 4688, 4697, 4720, 4728/4732/4756, 7045), AD (floresta, domínio, DC, OU, GPO, trusts), persistência.

**Linux:** filesystem hierarchy, permissões (rwx, SUID/SGID/Sticky), sudo/sudoers/shadow, processos/signals/namespaces/cgroups, cron/systemd, bash scripting, /proc, Linux Capabilities, LD_PRELOAD/LD_LIBRARY_PATH, PAM.

**macOS (base agora, aprofundar no Nível 5):** Gatekeeper, SIP, Notarization, TCC, LaunchDaemons/LaunchAgents, Keychain.

## 0.3 Programação e Scripting
Prioridade: Python ⭐⭐⭐⭐⭐, Bash ⭐⭐⭐⭐⭐, PowerShell ⭐⭐⭐⭐⭐, C ⭐⭐⭐⭐, C#/.NET ⭐⭐⭐⭐, Assembly x86/x64 ⭐⭐⭐, Go ⭐⭐⭐, JavaScript ⭐⭐⭐, C++ ⭐⭐, Rust ⭐⭐.

> [!warning] Sequência correta
> Python + Bash sólidos → antes do OSCP. C básico → antes do CRTO. Assembly → antes do OSED. Não inverta.
>
> **Nota de integração:** Python já está na sua trilha de dados/IA. C e C++ vêm da trilha de SO/robótica. C#/.NET é carta de reserva, mas segue útil em segurança ofensiva no mundo Windows. Ou seja: quase toda a base de linguagem deste nível você já cobre por outras trilhas — aqui é aplicá-las ao contexto ofensivo, não aprender do zero.

## 0.4 Criptografia Aplicada
Hashes (MD5, SHA-1/256, bcrypt, NTLM, LM, NetNTLMv1/v2), simétrica (AES CBC/CTR/GCM, DES, RC4, ChaCha20), assimétrica (RSA, ECDSA, DH), PKI/CAs/X.509/CRL/OCSP, TLS 1.2 vs 1.3, DPAPI.

**Cryptographic Attacks:** Padding Oracle (PadBuster), Hash Length Extension (HashPump), ECB Block Pattern Analysis, CBC Bit Flipping, Timing Attacks, TLS Downgrade (BEAST/DROWN/FREAK/LOGJAM), Broken Custom Crypto.

---

# NÍVEL 1 — Pentest Básico (→ eJPT)

## 1.1 Metodologias e Frameworks
**PTES — 7 fases:** Pre-engagement → Intelligence Gathering → Threat Modeling → Vulnerability Analysis → Exploitation → Post-Exploitation → Reporting.

**MITRE ATT&CK — 14 Táticas:** Reconnaissance (TA0043), Resource Development (TA0042), Initial Access (TA0001), Execution (TA0002), Persistence (TA0003), Privilege Escalation (TA0004), Defense Evasion (TA0005), Credential Access (TA0006), Discovery (TA0007), Lateral Movement (TA0008), Collection (TA0009), C2 (TA0011), Exfiltration (TA0010), Impact (TA0040).

**Cyber Kill Chain (Lockheed):** Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives. Use kill chain na narrativa do relatório, ATT&CK no mapeamento técnico.

## 1.2 Reconhecimento
**OSINT passivo:** theHarvester, Maltego, Shodan/Censys/FOFA, Amass/Subfinder/assetfinder, SpiderFoot, Recon-ng, crt.sh, WHOIS/DNS history, GitHub dorks (Gitrob/TruffleHog/gitleaks), Google Dorks.

**Reconhecimento ativo:** Nmap (SYN/UDP/Connect/FIN/Xmas/Null, -sV/-O/-A, timing T0-T5, scripts NSE), Masscan, Nikto, Gobuster/ffuf/feroxbuster, WhatWeb, SMBMap/enum4linux-ng, SNMP enumeration.

## 1.3 Web Security — OWASP Top 10
Injeção SQL (UNION/blind/time/error-based → sqlmap, Burp), XSS (Reflected/Stored/DOM → Burp, XSSer), SSRF (metadata 169.254.169.254 → Burp Collaborator), LFI/RFI (path traversal, wrappers PHP → dotdotpwn), XXE, Command Injection (commix), IDOR/BAC (Burp Autorize), Broken Auth (Hydra, Burp Intruder), SSTI (tplmap), Desserialização (ysoserial), File Upload, CSRF, Open Redirect, JWT Attacks (jwt_tool), OAuth 2.0.

> [!tip] Recurso definitivo
> **PortSwigger Web Academy** — gratuito, labs hands-on para CADA técnica. Resolva todos os labs antes do OSCP. (Já está na sua [biblioteca-recursos-por-passo](biblioteca-recursos-por-passo.md).)

**Burp Suite:** Proxy, Repeater, Intruder, Scanner (Pro), Decoder, Collaborator, Match and Replace, extensions (AuthMatrix, Autorize, Turbo Intruder, Logger++).

## 1.4 OWASP API Security Top 10
API1 BOLA, API2 Broken Authentication, API3 Broken Object Property Level Auth, API4 Unrestricted Resource Consumption, API5 BFLA, API6 Unrestricted Access to Sensitive Business Flows, API7 SSRF, API8 Security Misconfiguration, API9 Improper Inventory Management, API10 Unsafe Consumption of APIs.

Técnicas específicas: Mass Assignment, Parameter Pollution, GraphQL introspection/batching/field suggestions, Verb tampering, Content-type confusion, Swagger/OpenAPI exposure. Ferramentas: Postman/Insomnia, Kiterunner, Arjun, ffuf, GraphQL Playground, jwt_tool.

> [!note] Conexão com seu portfólio
> Você constrói APIs REST (Next.js/FastAPI) no AM Gestão. Esta seção é o lado ofensivo exato do que você já projeta defensivamente nos seus RNFTs de segurança. Estude os dois lados juntos.

## 1.5 WAF Evasion
Fingerprinting (wafw00f), encoding bypass (URL simples/duplo, Unicode, HTML entities, Base64), case manipulation, comentários SQL, whitespace alternatives, HTTP Parameter Pollution, Chunked Transfer Encoding, bypass de WAF cloud via origin direct (Shodan p/ IP real), header manipulation (X-Forwarded-For, X-Real-IP).

## 1.6 e 1.7 Escalada de Privilégios
**Linux:** SUID/SGID (GTFOBins), sudo misconfigs, cron jobs (pspy), world-writable scripts, capabilities, Docker socket, NFS no_root_squash, PATH hijacking, kernel exploits (linux-exploit-suggester), LD_PRELOAD. Enumeração: LinPEAS, lse.sh, pspy.

**Windows:** AlwaysInstallElevated, unquoted service paths, weak service permissions, DLL hijacking, stored credentials, token impersonation (Potato attacks), scheduled tasks, autologon, Pass-the-Hash, UAC bypass, SeDebugPrivilege. Enumeração: WinPEAS, Seatbelt, PowerUp, SharpUp, PEASS-ng, accesschk.

## 1.8 Framework Legal Brasileiro
> [!warning] Leia antes de qualquer teste
> Sem autorização formal por escrito, qualquer teste é crime no Brasil, mesmo com autorização verbal.

- **Lei 12.737/2012 (Carolina Dieckmann)** — Art. 154-A: invadir dispositivo sem autorização (detenção 3 meses-1 ano + multa)
- **Marco Civil (12.965/2014)** — responsabilidade civil, retenção de logs
- **LGPD (13.709/2018)** — cuidado com PII em relatórios; anonimizar evidências; multa até 2% do faturamento / R$ 50M

**Contrato mínimo de autorização:** identificação das partes, escopo explícito (IPs/domínios/sistemas), período, tipo de teste, pessoas autorizadas, exclusões, tratamento de dados, responsabilidade, assinaturas.

> [!important] Regra de ouro
> Autorização verbal não tem valor legal no Brasil. Sempre escrito, sempre assinado, sempre guardado.
>
> **Conexão:** isso se conecta com a Fase 0 jurídica que o [projeta-documento-projeto-final](../99-arquivo/sistemas-antigos/projeta-documento-projeto-final.md) e o AM Canteira/AM Saberia já preveem — a mesma disciplina de contrato e LGPD vale para prestar serviço de pentest.

## 1.9 Relatório de Pentest
Executive Summary (linguagem de negócio), Escopo/Metodologia, Sumário de Risco (CVSS v3.1), Findings (título, severidade, evidência, impacto, recomendação, referências), Narrativa de Ataque, Roadmap de Remediação, Apêndices. Ferramentas: Sysreptor, Ghostwriter, Dradis, PlexTrac.

---

# NÍVEL 2 — Pentest Avançado (→ OSCP)

## 2.1 Buffer Overflow
**Stack-based x86 (base do OSCP):** Fuzzing → Offset (pattern_create/offset) → Bad characters → JMP ESP (mona) → Shellcode (msfvenom) → NOPs + exploit.

**Avançado:** SEH overflow (POP POP RET), Egghunter, ROP (ROPgadget/ropper/mona), ASLR bypass, heap spraying, UAF, format string. Ferramentas: Immunity Debugger + Mona.py, x64dbg, pwntools, GDB + peda/gef/pwndbg.

## 2.2 MSSQL — Lateral Movement
Enumeração (PowerUpSQL), xp_cmdshell, Linked Servers, CLR Assemblies, Impersonation (EXECUTE AS), UNC Path Injection (capturar NTLMv2 com Responder), Trustworthy Database, credential exfiltration. Ferramentas: PowerUpSQL, SQLRecon.

## 2.3 Web Avançado
Code Review (source-to-sink), Business Logic Flaws (race conditions), HTTP Request Smuggling (CL.TE/TE.CL/TE.TE), Cache Poisoning, Prototype Pollution, GraphQL, WebSocket hijacking, CORS misconfiguration, Clickjacking.

## 2.4 Pivoting e Tunneling
> [!important] Toda operação com mais de um host exige pivoting. Obrigatório antes do OSCP.

SSH port forwarding (Local -L, Remote -R, Dynamic -D), Double Pivot, ProxyJump -J. Ferramentas modernas: **ligolo-ng** (padrão atual da indústria), chisel, socat, rpivot, Metasploit routes. DNS tunneling (dnscat2, iodine), ICMP tunneling (ptunnel-ng). Proxychains config.

---

# NÍVEL 3 — Red Team (→ CRTO / CRTP)

## 3.1 Active Directory — Kill Chain Completa
**Enumeração:** BloodHound + SharpHound (Shortest Path to DA, Kerberoastable, ASREProastable, ACL abuse), PowerView, ADRecon, ldapdomaindump, adidnsdump.

**Acesso inicial:** LLMNR/NBT-NS Poisoning (Responder), IPv6 DNS takeover (mitm6), Password Spraying (CrackMapExec/kerbrute/Spray), NTLM Relay (ntlmrelayx + Coercer/PetitPotam/PrinterBug).

**Escalada:** Kerberoasting (GetUserSPNs → hashcat -m 13100), AS-REP Roasting (GetNPUsers → hashcat -m 18200), abuso de ACLs (GenericAll, GenericWrite, WriteOwner, WriteDACL, ForceChangePassword), abuso de Delegation (Unconstrained/Constrained/RBCD), Shadow Credentials (Whisker/Certipy), BadSuccessor (2025, dMSA).

**ADCS — ESC1 a ESC15** (Certipy): SAN arbitrário, EKU abuse, NTLM relay para HTTP endpoint, weak certificate mapping, etc.

**Domain Compromise:** DCSync (secretsdump -just-dc), NTDS.dit dump, Golden/Silver/Diamond/Sapphire Ticket, Skeleton Key.

**Multi-Forest Trust:** trust tickets, SID History injection, ExtraSID attack, cross-forest exploitation.

## 3.2 C2 Framework — Operação Profissional
Infraestrutura em camadas (redirectors por função → teamserver nunca exposto), Domain Fronting e alternativas (Cloudflare Workers, DNS C2), frameworks (Sliver/Havoc/Mythic/Covenant/PoshC2/Merlin; Cobalt Strike comercial), Malleable C2 Profiles (customizar tráfego, sleep obfuscation, jitter).

## 3.3 OPSEC
Blast radius containment, infraestrutura efêmera (Terraform), separação por função/tempo de vida, conteúdo legítimo sempre. Em host: execução in-memory, process injection em processos whitelisted, sacrificial processes, evitar binários com assinaturas conhecidas, LOLBins.

## 3.4 Wireless
WPA2 handshake capture + cracking (aireplay-ng + aircrack-ng/hashcat -m 22000), PMKID attack, WPS (Reaver), Evil Twin (hostapd-wpe/mana), RADIUS attacks, captive portal bypass, deauth, Bluetooth BLE, RF (SDR: HackRF/RTL-SDR). Ferramentas: Aircrack-ng, hostapd-wpe, Kismet, hcxtools, hcxdumptool, Flipper Zero.

---

# NÍVEL 4 — Red Team Avançado (→ OSEP / OSED)

## 4.1 Windows Internals Profundo
PE format (DOS/NT headers, sections, IAT/Export, relocations), gerenciamento de memória (Virtual Address Space, pages, VirtualAlloc/Ex, VAD), process/thread internals (EPROCESS, PEB, TEB, handles, tokens).

**Mecanismos de segurança e bypasses:** AMSI (patch AmsiScanBuffer), ETW (patch EtwEventWrite), PPL (BYOVD), Credential Guard, WDAC/AppLocker (LOLBins, DLL sideloading).

## 4.2 Evasão AV/EDR
**Estática:** obfuscação de strings, polimorfismo, packing/encryption, PE stomping, resource manipulation, signed binary, threshold evasion.

**Comportamental/memória:** API Unhooking, Direct Syscalls (SysWhispers2/3), Indirect Syscalls, Sleep Obfuscation (Ekko/Foliage/Cronos), Stack Spoofing, Heaven's Gate.

**Process Injection:** classic, hollowing, doppelgänging, thread hijacking, APC (Early Bird), module stomping, transacted hollowing, ghost writing, DLL sideloading, COM hijacking, reflective DLL loading.

**BOF (Beacon Object Files):** COFF compilado de C, executa in-process, Beacon API, compilação MinGW/MSVC, testing harness.

## 4.3 Exploit Development Avançado (→ OSED)
ROP/JOP/COP, heap exploitation (UAF, spray, grooming), BYOVD, kernel exploitation (Windows), browser exploitation (JIT abuse, type confusion, sandbox escape).

## 4.4 Engenharia Social
Phishing (spoofing, DKIM bypass, HTML harvesting), spear phishing, Evilginx2 (session cookie + MFA bypass), vishing, smishing, physical access, GoPhish, lure creation (macros VBA/DDE/OLE, LNK, ISO/ZIP, HTA, OneNote).

## 4.5 Anti-Forensics
> [!warning] Em operações autorizadas é legítimo; em crime real, é agravante. Contexto importa.

Timestomping, seletividade na limpeza de logs (evitar Event ID 1102), Alternate Data Streams, slack space, LOLBin chains, memory-only execution, Volume Shadow Copy management.

## 4.6 Deception Technology (perspectiva ofensiva)
Canary Tokens, HoneyAD, honeypot fingerprinting (T-Pot/OpenCanary), breadcrumbs falsos, deception na rede. Estratégia: validar antes de usar credenciais/hosts suspeitos, movimentar-se com cautela.

---

# NÍVEL 5 — Especialização

## 5.1 Cloud Security
**AWS:** IAM priv esc, S3 misconfig, EC2 IMDS (169.254.169.254), Lambda, SSM, Secrets Manager, CloudTrail gaps, ECS/EKS. Ferramentas: Pacu, ScoutSuite, Prowler, CloudMapper, CloudFox.

**Azure/Entra ID:** password spray, device code phishing, Pass-the-PRT, Pass-the-Certificate, app registrations, managed identities, Azure RBAC, Key Vaults, hybrid identity, cross-tenant. Ferramentas: ROADtools, AADInternals, BloodHound (Azure), GraphRunner, TokenTactics, PowerZure.

**Kubernetes:** pod escape, Docker socket abuse, RBAC misconfig, API server exposto, etcd exposure, supply chain de imagem. Ferramentas: kube-hunter, kube-bench, peirates, CDK.

## 5.2 Mobile Security
**Android:** ADB, emuladores, Magisk, análise estática (apktool, jadx, MobSF), análise dinâmica (Frida, Objection, Drozer), SSL pinning bypass, vulns comuns (storage inseguro, intent hijacking, deep link, backup, exported components, WebView).

**iOS:** jailbreak, class-dump/otool/nm, Frida, SSL Kill Switch 2, Keychain extraction. Cert: eMAPT.

## 5.3 Reverse Engineering
Estática (Ghidra, IDA, Cutter, CFF Explorer, DIE, strings, binwalk), dinâmica (x64dbg, WinDbg, Process Monitor/Hacker, API Monitor, Wireshark), sandboxes (ANY.RUN, Cuckoo, Hybrid Analysis, VirusTotal, Flare-VM), análise de malware (IoCs, evasão de sandbox, desofuscação, C2 reconstruction, JA3/JA3S).

## 5.4 Detection Engineering
YARA rules, SIGMA rules (Uncoder.IO), Atomic Red Team + Caldera, ATT&CK Navigator, Threat Hunting (hypothesis/analytics/intel-driven), SIEM (Elastic/Splunk/Sentinel/Velociraptor).

## 5.5 DFIR
> [!tip] Sendo red teamer, entender o que o blue team encontrará guia decisões de OPSEC.

Windows forensics (Volatility 3, registry, event logs, prefetch, LNK, VSS, $MFT, ADS), ferramentas (Autopsy, FTK Imager, Chainsaw, Hayabusa, Eric Zimmermann Tools, KAPE), network forensics (PCAPs, beacon detection, JA3, Suricata/Zeek).

## 5.6 Supply Chain Security
> SolarWinds, XZ Utils, Log4Shell, event-stream. Um dos vetores mais eficientes.

Dependency Confusion, Typosquatting, Compromised Maintainer Account, Build Pipeline Poisoning, Malicious PR, Container Image Poisoning. Análise: SBOM, SLSA Framework, Sigstore/Cosign.

## 5.7 CI/CD Pipeline Security
Secrets em env vars, misconfigured `pull_request_target`, artifact poisoning, self-hosted runners sem isolamento, pipeline injection, permissões excessivas de GITHUB_TOKEN, cache poisoning. Ferramentas: Semgrep, actionlint, truffleHog, Gato-X.

> [!note] Conexão direta com seu plano
> Você vai configurar GitHub Actions (Passo 10-12 e o [github-estrutura-profissional-autoridade](../06-execucao-e-desenvolvimento/github-estrutura-profissional-autoridade.md)). Esta seção é como um atacante ataca exatamente esse pipeline — estude junto, é o lado ofensivo do que você constrói.

## 5.8 macOS Offensive
Gatekeeper/SIP/TCC/Notarization/XProtect bypass, persistência (LaunchDaemons/Agents, Login Items), TCC bypass, Keychain extraction, LOLBins macOS (osascript, curl, python3, ditto, screencapture), Dylib hijacking, DYLD_INSERT_LIBRARIES.

## 5.9 DPAPI
> Mecanismo que o Windows usa para proteger credenciais de browsers, WiFi, RDP, centenas de apps. Comprometer DPAPI = comprometer todos os segredos do usuário.

MasterKey, DPAPI blob, backup no DC. Exploração: SharpDPAPI (chrome/unprotect, masterkeys/pvk), Mimikatz DPAPI, Domain DPAPI Backup Key. Integração com BloodHound para achar alvos de alto valor.

## 5.10 OT/ICS/SCADA
Protocolos (Modbus 502, DNP3 20000, Profinet, EtherNet/IP 44818, Siemens S7 102, IEC 61850, BACnet 47808), ferramentas (PLCScan, s7scan, ModbusPal, Shodan, GRASSMARLIN). Cert: GICSP.

> [!warning] Scanners agressivos podem crashar PLCs e causar acidentes reais. Em OT, sempre varredura passiva ou com o fabricante presente.

---

# NÍVEL 6 — Elite

## 6.1 AI/LLM Security
Prompt injection (direct/indirect), jailbreaking, tool call hijacking, adversarial ML (evasão de detectores, model extraction, training data poisoning), LLM como ferramenta ofensiva, testes em sistemas com LLM. Recurso: OWASP Top 10 for LLM Applications.

> [!note] Conexão direta com seu portfólio
> Você planeja recursos de IA no AM Gestão (busca semântica, geração assistida). A série [rnft-ia-governanca-geracao-ia](../04-documentos-transversais/rnft-ia-governanca-geracao-ia.md) que você já criou é justamente a defesa contra parte disto. Esta seção é o ataque correspondente — os dois lados da mesma moeda.

## 6.2 APT Emulation
Simular threat actor específico com TTPs documentadas. APTs para estudo: APT29 (Midnight Blizzard), APT41, Lazarus, FIN7/CARBANAK, ALPHV/BlackCat. Plataformas: SCYTHE, Vectr.

## 6.3 Malware Development Avançado
Shellcode (PIC, API resolution por hash, staged, egghunter), custom C2 (protocolo próprio, mTLS, sleep obfuscation), BOF development.

## 6.4 Vulnerability Research
Fuzzing (AFL++, LibFuzzer, WinAFL), source code auditing, binary diffing (BinDiff, Diaphora), Responsible Disclosure (CVD), bug bounty.

## 6.5 Bug Bounty
Seleção de programa, metodologia de recon (amass/subfinder → httpx/naabu → gowitness → priorização), mindset (pentest vs bug bounty), relatório que converte. Plataformas: HackerOne, Bugcrowd, Intigriti, YesWeHack.

> [!note] Fonte de renda paralela
> Bug bounty conecta com a lógica de fontes de renda que você já tem no plano (e-commerce/afiliados, freelance). É renda variável que também treina habilidade real.

## 6.6 DevSecOps — Perspectiva do Atacante
SAST (Semgrep, SonarQube), DAST (OWASP ZAP, Burp Enterprise), SCA (Snyk, Dependabot), IaC Security (Checkov, tfsec, trivy), secret scanning (TruffleHog, GitLeaks). Entender como cada defesa falha.

---

# DOMÍNIOS TRANSVERSAIS

**Threat Intelligence:** tipos (strategic/operational/tactical/technical), fontes (VirusTotal, MalwareBazaar, Shodan, Censys), plataformas (MISP, OpenCTI), Pyramid of Pain, Diamond Model.

**Purple Team — processo formal:** Planning → Notification → Execution → Detection Validation → Gap Analysis → Detection Development → Retest. Ferramentas: VECTR, PlexTrac, ATT&CK Navigator, Atomic Red Team, Caldera.

**Hardware/IoT:** Flipper Zero, HackRF One, Proxmark3, Rubber Ducky/O.MG Cable, Bus Pirate, Binwalk, JTAG/UART.

**Soft Skills e Comunicação Executiva:** apresentar para C-Level (risco financeiro, não CVSS), executive summary, debrief, negociação de escopo, risk quantification (FAIR model).

> [!important] O gargalo real após o nível intermediário
> Sem soft skills, o profissional fica preso como operador. Isso conecta com o [curriculo-dev-senior-completo](curriculo-dev-senior-completo.md) — a mesma comunicação executiva que pesa em qualquer carreira sênior de tecnologia.

---

# SEQUÊNCIA DE ESTUDO RECOMENDADA

```
FASE 1 — BASE (3-6 meses): Redes + Linux + Windows + Python/Bash + TryHackMe + PortSwigger → eJPT
FASE 2 — PENTEST PRO (6-12 meses): BOF x86 + AD básico + MSSQL + HackTheBox + Proving Grounds + PEN-200 → OSCP
FASE 3 — RED TEAM OPS (3-6 meses): Sliver/CS + C2 infra + OPSEC + CRTO labs → CRTO
FASE 4 — AD ESPECIALIZAÇÃO (6-12 meses): BloodHound + ACLs + Delegation + ADCS + CRTP/CRTE labs → CRTP + CRTE
FASE 5 — EVASION + EXPLOIT DEV (6-12 meses): Windows Internals + AV/EDR evasion + BOF + BOF avançado + OSEP/OSED → OSEP + OSED
FASE 6 — ESPECIALIZAÇÃO (ongoing): Cloud (CARTP/AWS) + Mobile (eMAPT) + Malware dev + Vuln research + Bug bounty + APT emulation + AI/LLM
```

> [!tip] Regra de ouro
> Cada técnica aprendida teoricamente deve ser praticada em lab antes de avançar. Plano sem horas de hands-on não forma profissional. Isso é a mesma lógica de prática deliberada da [metodo-de-estudo](metodo-de-estudo.md).

---

## 🔗 Documentos relacionados
- [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md) — companion com todos os links, ferramentas, cursos e certificações verificados
- [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md) — a Fase 12 é a versão resumida deste roadmap
- [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md) — cobre a base de C/C++, rede (NetPractice) e Linux (Born2beroot)
- [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md) — episódios de criptografia/segurança do Akitando
- [sequencia-mestra-completa-desde-o-inicio](../99-arquivo/sequencia-mestra-completa-desde-o-inicio.md) — onde a segurança ofensiva entra na ordem geral

---

*Versão 3.0 — Agosto/2026. Revisão recomendada: anual. Fontes: MITRE ATT&CK, OffSec, SANS, ired.team, adsecurity.org, PortSwigger, OWASP.*

---

## 🔗 Gates com as trilhas Linux e Redes

Este roadmap (os 6 níveis acima) roda entrelaçado com [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md) e [trilha-de-redes](trilha-de-redes.md). Cada nível só abre com a fase de Linux correspondente concluída — a base sustenta o ataque.

- Fundamentos Linux + primeiro contato (Bandit) andam juntos; [trilha-de-redes](trilha-de-redes.md) vem cedo, porque destrava tudo
- Linux F2 → redes para pentest · F3–4 → testar o próprio Aura (OWASP, maior retorno) · F5–6 → escalada de privilégio · F8 → laboratório Kali (Distrobox)
- Depois: Windows/Active Directory → baixo nível/exploit → metodologia e relatório

**Regra de ouro:** nunca abrir uma fase de segurança sem o gate de Linux fechado. Só teste o que é seu ou o que você tem autorização por escrito para testar (Lei 12.737/2012).

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Trilha de Cibersegurança e Pentest](../12-artefatos/documentos/trilha-de-ciberseguranca-e-pentest.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->


---

## Recursos e links de segurança ofensiva

> [!important] Companion do [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md)
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
> TryHackMe (base) → HTB Academy (teoria) → HackTheBox (prática) → Proving Grounds (prep OSCP) → VulnLab (AD/Red Team). A mesma lógica de dificuldade crescente da [metodo-de-estudo](metodo-de-estudo.md).

---

## 📜 Certificações — Links Oficiais

**Entrada:** eJPT (INE/eLearnSecurity) — [ine.com](https://ine.com) 💲 | PNPT (TCM Security) — [certifications.tcm-sec.com](https://certifications.tcm-sec.com) 💲

**Core:** OSCP (PEN-200) — [offsec.com](https://www.offsec.com) 💲💲💲 | CRTO (Zero-Point Security) — [training.zeropointsecurity.co.uk](https://training.zeropointsecurity.co.uk) 💲💲

**Active Directory:** CRTP / CRTE / CARTP (Altered Security) — [alteredsecurity.com](https://www.alteredsecurity.com) 💲💲

**Avançado:** OSEP / OSED / OSEE (OffSec) 💲💲💲 | GXPN / GICSP (SANS/GIAC) — [giac.org](https://www.giac.org) 💲💲💲💲

**Mobile:** eMAPT (INE) 💲

> [!note] Sua trilha registrada
> No [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md): `CompTIA A+/Network+ → Security+ → CCNA (opcional) → eJPT → OSCP`. O resto é continuação além do OSCP.

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
> Ver seção 1.8 do [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md). Sem autorização escrita e assinada, teste = crime no Brasil. Isso vale igual para o serviço de pentest como fonte de renda.

---

## 🧪 Ambientes de Lab Locais (montar em casa)

**AD para praticar:** GOAD (Game of Active Directory) 🆓, DetectionLab 🆓, vulnerable-AD scripts, Ludus (automação de lab).

**Web vulnerável:** DVWA, OWASP Juice Shop, WebGoat, bWAPP, VAmPI (API), crAPI (API).

**Malware/RE isolado:** Flare-VM + REMnux em rede isolada (host-only), snapshots sempre.

> [!warning] Isolamento obrigatório
> Malware analysis SEMPRE em VM isolada, rede host-only, snapshot antes. Nunca na máquina principal. Conecta com o `Born2beroot` da [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md) — a mesma disciplina de VM hardened.

---

## 🗓️ Rotina de Manutenção de Conhecimento

- **Diário:** 1 máquina/lab ou 1 lab PortSwigger
- **Semanal:** 1 walkthrough IppSec, ler 2-3 posts técnicos, acompanhar CVEs relevantes
- **Mensal:** 1 CTF, revisar notas (Obsidian/CherryTree), tentar 1 técnica nova
- **Anual:** revisar este roadmap, avaliar próxima certificação

> [!tip] Note-taking
> Mantenha suas próprias notas de técnica em formato consultável. Você já usa Obsidian — crie uma pasta dedicada de pentest com template por máquina (recon → enum → exploit → privesc → loot). Mesmo princípio da [metodo-de-estudo](metodo-de-estudo.md): documentar para reter.

---

## 🔗 Documentos relacionados
- [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md) — o roadmap de 6 níveis que este companion suporta
- [plano-estudos-basico-avancado-entrelacado](../99-arquivo/plano-estudos-basico-avancado-entrelacado.md) — Fase 12
- [biblioteca-recursos-por-passo](biblioteca-recursos-por-passo.md) — recursos gerais de todos os outros passos do plano
- [mapa-mestre-prioridade-total](../99-arquivo/mapa-mestre-prioridade-total.md) — onde a segurança ofensiva entra na prioridade geral

---

*Companion do Roadmap v3.0 — Agosto/2026. Todos os links verificados na data de criação; revisar anualmente.*

---

<!-- conexoes:inicio -->
## 🗂️ Artefatos do claude.ai sobre este assunto

> Documentos e páginas que você criou no claude.ai e que detalham esta parte do plano. Todos estão copiados na pasta `12-artefatos`.

- [Trilha de Cibersegurança e Pentest](../12-artefatos/documentos/trilha-de-ciberseguranca-e-pentest.md)

🗺️ Mapa completo de quais artefatos entram em cada parte do plano: [mapa de conexões](../12-artefatos/01-MAPA-DE-CONEXOES.md)
<!-- conexoes:fim -->
