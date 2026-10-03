---
tags: [estudo, horizonte-longo, mapa-mestre, sistemas]
tipo: trilha
status: estacionado
atualizado: 2026-10-02
---

# 🌌 Mapa de Horizonte Longo — Sistemas, Baixo Nível e SO Próprio

> **Camada D do [00-PLANO-UNIFICADO](../00-PLANO-UNIFICADO.md).** Tudo aqui está **estacionado de propósito**: é o arco de ~10 anos, da base de sistemas até criar seu próprio SO e sua própria distro. Nenhum bloco compete pelas horas de 2026-2027. Ver tudo documentado aqui é o que te deixa tranquilo pra **não** tocar nisso agora.
>
> A parte ofensiva (reverse, exploit, kernel exploitation) é só **nomeada** aqui — o detalhe vive em [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md), não é duplicado.

---

## 🧭 Ordem de dependência (cada nível precisa do anterior)

```
MATEMÁTICA  (já corre na licenciatura + livro do Lins)
   ▼
LÓGICA · ALGORITMOS · ESTRUTURAS DE DADOS        → já no núcleo (Camada A)
   ▼
C · C++ · Python · JS/TS · C#                    → C/C++ vem pela École 42
   ▼
LINUX + WINDOWS (internals)                      → Linux já começa na Camada C
   ▼
REDES → SERVIDORES → WEB/APIs/DATABASES          → núcleo + Trilha de Redes
   ▼
CYBERSECURITY (web + Active Directory)           → trilha de segurança
   ▼
REVERSE ENGINEERING → ASSEMBLY → EXPLOIT DEV     → ponta avançada da segurança
   ▼
KERNEL (Linux · Windows NT · XNU/Apple)
   ▼
OS RESEARCH → AM-OS (SO próprio) · AM Linux (distro própria)
```

> macOS/iOS e Windows **não precisam esperar** terminar todo o Linux: depois dos fundamentos de redes, programação e SO, podem entrar em paralelo. Só o conteúdo realmente avançado (kernel, reverse profundo, pesquisa de vulnerabilidade) é que espera.

---

## 📚 Blocos por área (nível de currículo — o QUE estudar, não o passo a passo)

### Fundamentos de estudo
Terminal Linux/Windows · Git/GitHub · Markdown · leitura de RFC/manual/código-fonte · debugging · método científico · laboratório (virtualização, snapshots, redes isoladas) · escrita técnica · inglês técnico. → já coberto por [metodo-de-estudo](metodo-de-estudo.md).

### Matemática (profunda)
Básica → Álgebra → Geometria/Trigonometria → Discreta → Teoria dos Números → Cálculo → Álgebra Linear → Probabilidade/Estatística → (depois) Análise Real, Álgebra Abstrata, Topologia, Análise Complexa, EDO, Teoria da Informação, Teoria da Computação. → [matematica-e-desenvolvimento-integrado](matematica-e-desenvolvimento-integrado.md).

### Ciência da Computação
Algoritmos, complexidade (Big-O), recursão, concorrência/paralelismo · estruturas de dados (array, lista, pilha, fila, árvore, heap, hash, grafo, trie) · algoritmos (ordenação, busca, DP, greedy, backtracking, grafos, caminho mínimo, árvore geradora, fluxo).

### Programação (baixo nível)
C, C++, Rust, Assembly x86-64/ARM64 · memória, ponteiros, stack/heap, gerência de memória, threads/processos, IPC, sockets, concorrência, async, generics, metaprogramação, FFI. → C/C++ pela [trilha-42-circles-oficial-verificado](trilha-42-circles-oficial-verificado.md).

### Linux (profundo)
Fundamentos (FHS, terminal, permissões, processos, shell, Vim) → Arch manual → desktop (Wayland/Hyprland) → server → internals (kernel, syscalls, VFS, memória virtual, drivers) → LFS/BLFS → kernel development. → base prática em [trilha-linux-arch-profissional](trilha-linux-arch-profissional.md).

### Windows / macOS / iOS
Windows: arquitetura NT, Win32/NT API, registro, NTFS, ACL/SID/tokens, UAC, PowerShell/WMI · Windows Internals · Active Directory.
macOS: Darwin/XNU/Mach/BSD, launchd, APFS, Keychain, SIP, Gatekeeper, TCC, sandbox, code signing.
iOS: iBoot, Secure Enclave, entitlements, provisioning, Data Protection, Mach-O, dyld, XPC.

### Segurança (web · redes · AD · ofensiva)
Escopo e trilha completos em [roadmap-seguranca-ofensiva-completo](roadmap-seguranca-ofensiva-completo.md) e [recursos-links-seguranca-ofensiva](recursos-links-seguranca-ofensiva.md). Áreas: segurança web (OWASP), pentest, wireless, AD security, reverse engineering, exploit development, kernel exploitation, malware analysis, forense digital, blue team, cloud security, segurança de containers/k8s, criptografia aplicada, segurança de hardware, IoT/embedded. **Regra permanente:** só em ambientes próprios ou autorizados.

### Sistemas Operacionais (juntar tudo)
boot/bootloader · kernel · memória virtual · processos/scheduling · interrupts · syscalls · IPC · filesystems · drivers · networking · segurança · userland. Comparar **Linux × Windows NT × XNU**.

---

## 🏗️ Projetos de coroação
- **AM-OS** — SO próprio: boot → GDT/IDT/interrupts → memória/paging → processos/scheduler → syscalls/user mode → filesystem/VFS → networking → shell → modelo de segurança.
- **AM Linux** — distro própria, depois do LFS: kernel + bootloader + glibc + systemd + coreutils + stack de rede + gerenciador de pacotes + instalador + ISO.
- **Homelab físico** — laboratório permanente (Linux/Windows/Apple, AD, Docker, monitoramento), expandindo com Raspberry Pi, mini-PC, switch, NAS, WireGuard. → [infraestrutura-fisica-10-anos](../01-planejamento-geral/infraestrutura-fisica-10-anos.md).

Progressão de identidade: **usuário Linux → administrador → desenvolvedor de sistemas → kernel developer → criador de distribuição.**

---

## 🔓 Gatilhos de ativação

| Bloco | Só ativa quando… |
|---|---|
| Linux internals, LFS/BLFS, Arch avançado | empregado como dev **E** Trilha Linux básica fechada |
| Windows internals, AD, macOS/iOS internals | a trilha de segurança (Camada C) chegar lá naturalmente |
| Reverse, exploit dev, kernel exploitation | pós-OSCP — ponta avançada da segurança |
| Criptografia avançada, hardware, IoT/embedded | quando um projeto real seu pedir |
| Linux kernel development | depois de C/C++ nativo (42) + Linux internals |
| **AM-OS** e **AM Linux** | só com kernel + C + Linux internals dominados |
| Homelab físico | quando houver renda extra pra hardware |

> **Padrão de toda a Camada D:** cada bloco termina em **laboratório + projeto + documentação + evidência**, igual aos sistemas Aura — nunca em "assisti a um curso".
