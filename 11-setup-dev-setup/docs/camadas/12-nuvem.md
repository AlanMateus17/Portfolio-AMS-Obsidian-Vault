<!-- Arquivo GERADO por tools/gerar_docs.py a partir de data/. Edite os dados, não este arquivo. -->


# Camada 12 · Nuvem, código e entrega

[← Arquitetura](../arquitetura.md) · [Índice da documentação](../README.md)

> **Ligação com a camada de baixo:** git push via SSH leva o código ao GitHub; o Actions testa e publica.

**17 blocos** · 12 precisam de conta · 3 marcados como futuro

## Mapa de conexões

```mermaid
flowchart LR
  subgraph L_nuvem["Nuvem, código e entrega"]
    n_blob["Armazenamento de arquivos (Blob/R2)"]
    n_tmail["E-mail transacional (Resend, SES…)"]
    n_sonar["SonarQube Cloud"]
    n_ghproj["Projects · ADRs · MkDocs"]
    n_dbot["Dependabot + CodeQL"]
    n_gcp["Google Cloud"]
    n_gh["GitHub"]
    n_gha["GitHub Actions"]
    n_ghcr["GHCR (imagens)"]
    n_ghp["GitHub Pages"]
    n_cf["Cloudflare (DNS, Pages, e-mail)"]
    n_vercel["Vercel"]
    n_azure["Azure"]
    n_aws["AWS"]
    n_b2["Backblaze B2 (backup)"]
    n_gpuh["GPU por hora (RunPod e afins)"]
    n_gdrv["Google Drive (seus documentos)"]
  end
  subgraph L_oper["Operação do grupo (esteira, marca, qualidade)"]
    n_acv["Acervo (seus documentos)"]
  end
  subgraph L_pub["Público e canais"]
    n_recr["Recrutadores"]
  end
  subgraph L_mkt["Marketing, automação e medição"]
    n_n8n["n8n"]
  end
  subgraph L_web["Vitrine web (sites e domínio)"]
    n_amsite["Site Grupo AMtech"]
    n_catal["Catálogo do HTML"]
    n_dom["Domínio (Registro.br)"]
    n_inst["Instituto AMS"]
    n_site["Site pessoal + blog (Jekyll)"]
  end
  subgraph L_prod["Produtos (o que você vende)"]
    n_saas["Sistemas AM (SaaS)"]
    n_tmpl["Templates e código-fonte"]
  end
  subgraph L_editora["Editora AMS Silva (produção de livros)"]
    n_brepo["Repositório do livro"]
    n_projcap["Projeto do capítulo"]
  end
  subgraph L_est["Estudo e carreira"]
    n_learn["Microsoft Learn + AWS Skill Builder"]
  end
  subgraph L_cont["Produção de conteúdo"]
    n_voz["Voz clonada (ElevenLabs)"]
  end
  subgraph L_app["Aplicação: sistemas AM (Aura)"]
    n_api["API ASP.NET Core"]
    n_status["aura-status"]
    n_tests["Testes: xUnit, Playwright, k6"]
  end
  subgraph L_cnt["Containers, Kubernetes e infra como código"]
    n_clis["Azure CLI · AWS CLI"]
    n_tf["Terraform"]
  end
  subgraph L_clc["Claude: recursos, conectores e plugins"]
    n_ccf["Conector Cloudflare"]
    n_cdev["Vercel · AWS · Microsoft Learn"]
    n_cgws["Conector Google (Gmail, Drive…)"]
  end
  subgraph L_chat["Assistentes de IA (chat, pesquisa e estudo)"]
    n_codex["Codex (OpenAI)"]
    n_gcode["Agentes de código do Google"]
  end
  subgraph L_dados["Dados e treino de IA"]
    n_unsl["Unsloth (QLoRA)"]
  end
  subgraph L_ia["Agentes de IA e sandbox"]
    n_mcp["Servidores MCP"]
  end
  subgraph L_lin["Linux (Ubuntu no WSL2, Arch no 2º disco)"]
    n_dot["dotfiles"]
    n_git["Git + SSH + gh"]
  end
  subgraph L_win["Windows 11, apps e máquinas virtuais"]
    n_obsd["Obsidian + Git"]
  end
  subgraph L_seg["Segurança e cofre"]
    n_kee["KeePassXC"]
    n_restic["restic (backup criptografado)"]
    n_sign["Commits assinados (chave SSH)"]
    n_ykey["Chave física (YubiKey)"]
  end
  subgraph L_hw["Hardware"]
    n_nas["Servidor caseiro (NAS + serviços)"]
    n_ws["Workstation com GPU"]
  end
  n_blob -->|"arquivos"| n_api
  n_tmail -->|"e-mails do sistema"| n_api
  n_sonar -->|"análise no PR"| n_gha
  n_ghproj -->|"issues e board"| n_gh
  n_dbot -->|"PRs de segurança"| n_gh
  n_dbot -->|"alertas"| n_status
  n_tf -->|"cria recursos"| n_gcp
  n_gh -->|"dispara a cada push"| n_gha
  n_gh -->|"portfólio"| n_recr
  n_kee -->|"senhas e tokens"| n_gh
  n_obsd -->|"Obsidian Git"| n_gh
  n_git -->|"push via SSH"| n_gh
  n_dot -->|"versionado"| n_gh
  n_mcp -->|"issues e PRs"| n_gh
  n_sign -->|"Verified"| n_gh
  n_ykey -->|"2FA"| n_gh
  n_codex -->|"mesmos repos"| n_gh
  n_gcode -->|"mesmos repos"| n_gh
  n_status -->|"Dependabot e repos"| n_gh
  n_tmpl -->|"demo pública"| n_gh
  n_ws -->|"mesmos repositórios"| n_gh
  n_brepo -->|"hospedado"| n_gh
  n_projcap -->|"portfólio do aluno"| n_gh
  n_gha -->|"publica imagem"| n_ghcr
  n_gha -->|"deploy OIDC"| n_azure
  n_gha -->|"deploy front"| n_vercel
  n_gha -->|"publica sites"| n_ghp
  n_gha -->|"publica Pages"| n_cf
  n_tests -->|"roda no CI"| n_gha
  n_ghcr -->|"imagem"| n_azure
  n_ghcr -->|"imagem"| n_aws
  n_site -->|"hospedado"| n_ghp
  n_catal -->|"hospedado"| n_ghp
  n_cf -->|"túnel dos webhooks"| n_n8n
  n_ccf -->|"DNS e Pages"| n_cf
  n_tf -->|"DNS por código"| n_cf
  n_dom -->|"nameservers"| n_cf
  n_inst -->|"hospedado (Pages)"| n_cf
  n_amsite -->|"hospedado (Pages)"| n_cf
  n_cdev -->|"deploy e logs"| n_vercel
  n_kee -->|"senhas"| n_azure
  n_clis -->|"comandos"| n_azure
  n_learn -->|"certificação"| n_azure
  n_cdev -->|"documentação"| n_azure
  n_tf -->|"cria recursos"| n_azure
  n_saas -->|"roda na nuvem"| n_azure
  n_clis -->|"comandos"| n_aws
  n_cdev -->|"documentação"| n_aws
  n_tf -->|"cria recursos"| n_aws
  n_learn -->|"Skill Builder"| n_aws
  n_nas -->|"restic diário"| n_b2
  n_restic -->|"criptografado"| n_b2
  n_gpuh -->|"modelos abertos"| n_voz
  n_gpuh -->|"GPU de 24 GB"| n_unsl
  n_gdrv -->|"cópia pelo Takeout"| n_acv
  n_cgws -->|"o Claude lê o Drive"| n_gdrv
  classDef desta fill:#e2ecec,stroke:#0e3a45,color:#13262b
  class n_blob,n_tmail,n_sonar,n_ghproj,n_dbot,n_gcp,n_gh,n_gha,n_ghcr,n_ghp,n_cf,n_vercel,n_azure,n_aws,n_b2,n_gpuh,n_gdrv desta
```

## Blocos

| Bloco | Tipo | O que faz | Quando entra |
|---|---|---|---|
| [Armazenamento de arquivos (Blob/R2)](#blob) | Remoto · precisa de conta | Fotos de produtos, anexos e PDFs dos sistemas AM fora do banco de dados. | passo 19.4 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| [E-mail transacional (Resend, SES…)](#tmail) | Remoto · precisa de conta | E-mails automáticos dos sistemas: confirmação de conta, senha, recibo. | passo 19.5 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| [SonarQube Cloud](#sonar) | Remoto · precisa de conta | Nota de qualidade e segurança do código a cada PR. Grátis para repositório público; recrutador vê o selo. | passo 18.5 · Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| [Projects · ADRs · MkDocs](#ghproj) | Remoto | GitHub Projects espelhando o EPIC-01, decisões de arquitetura registradas e documentação publicada no Pages. | passo 5.5 · Semana 2 · nov/2026 |
| [Dependabot + CodeQL](#dbot) | Remoto | Dependabot atualiza pacotes vulneráveis; CodeQL procura falhas no seu código. Grátis em repositório público. | passo 5.3 · Semana 2 · nov/2026 |
| [Google Cloud](#gcp) | Remoto · precisa de conta · futuro | Terceira nuvem: só o básico, quando um projeto de IA ou dados pedir. | passo 30.5 · 2028 |
| [GitHub](#gh) | Remoto · precisa de conta | Código, vault, ensino-ti e a org grupo-amtech-digital. É também o seu portfólio. | passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 5.1 · Semana 2 · nov/2026; passo 5.4 · Semana 2 · nov/2026 |
| [GitHub Actions](#gha) | Remoto | CI/CD: build, testes, segurança e deploy. | passo 5.2 · Semana 2 · nov/2026; passo 16.1 · Semana 11 · jan/2027 |
| [GHCR (imagens)](#ghcr) | Remoto | Registro das imagens Docker das APIs. | passo 18.6 · Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 |
| [GitHub Pages](#ghp) | Remoto | Hospeda site pessoal, blog e Catálogo do HTML. | passo 13.7 · Semanas 6 e 7 · dez/2026 |
| [Cloudflare (DNS, Pages, e-mail)](#cf) | Remoto · precisa de conta | DNS, HTTPS, proteção, hospedagem estática dos sites comerciais e redirecionamento de e-mail do domínio. O Cloudflare Tunnel leva os webhooks de venda até o n8n sem abrir portas em casa. | passo 13.3 · Semanas 6 e 7 · dez/2026; passo 13.8 · Semanas 6 e 7 · dez/2026; passo 15.1 · Semana 11 · jan/2027; passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| [Vercel](#vercel) | Remoto · precisa de conta | Frontends Next.js. O plano grátis é para uso pessoal e não comercial; confira os termos antes de pôr venda nele. | passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| [Azure](#azure) | Remoto · precisa de conta | Primeira nuvem para as APIs AM: App Service/Container Apps, PostgreSQL, Key Vault. | passo 19.2 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028); passo 19.3 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028); passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) |
| [AWS](#aws) | Remoto · precisa de conta · futuro | Segunda nuvem, para o mercado maior. | passo 30.4 · 2028 |
| [Backblaze B2 (backup)](#b2) | Remoto · precisa de conta · futuro | Cópia fora de casa do backup, criptografada pelo restic. US$ 6,95 por TB/mês. | passo 7.2 · Semana 3 · nov/2026 |
| [GPU por hora (RunPod e afins)](#gpuh) | Remoto · precisa de conta | Quando o Kaggle não bastar: GPU de 24 GB a partir de cerca de US$ 0,27 a 0,90 por hora no RunPod (out/2026). Um fine-tuning QLoRA de 8B costuma levar poucas horas. Use crédito pré-pago, sem cartão em débito automático. | passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) |
| [Google Drive (seus documentos)](#gdrv) | Remoto · precisa de conta | Onde estão hoje as suas aulas, apostilas, provas, especificações e planos, misturados com cópias repetidas e documentos pessoais. O Google Takeout tira uma cópia completa para o acervo. | passo 0.5 · Antes de tudo · semana 1 (out/2026); passo 8.1 · Semanas 3 e 4 · nov/2026 |

<a id="blob"></a>

### Armazenamento de arquivos (Blob/R2)

*Remoto · precisa de conta*

Fotos de produtos, anexos e PDFs dos sistemas AM fora do banco de dados.

**Quando entra:** passo 19.4 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](11-app.md#api) | Aplicação: sistemas AM (Aura) | arquivos |

<a id="tmail"></a>

### E-mail transacional (Resend, SES…)

*Remoto · precisa de conta*

E-mails automáticos dos sistemas: confirmação de conta, senha, recibo.

**Quando entra:** passo 19.5 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [API ASP.NET Core](11-app.md#api) | Aplicação: sistemas AM (Aura) | e-mails do sistema |

<a id="sonar"></a>

### SonarQube Cloud

*Remoto · precisa de conta*

Nota de qualidade e segurança do código a cada PR. Grátis para repositório público; recrutador vê o selo.

**Quando entra:** passo 18.5 · Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | análise no PR |

<a id="ghproj"></a>

### Projects · ADRs · MkDocs

*Remoto*

GitHub Projects espelhando o EPIC-01, decisões de arquitetura registradas e documentação publicada no Pages.

**Quando entra:** passo 5.5 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | issues e board |

<a id="dbot"></a>

### Dependabot + CodeQL

*Remoto*

Dependabot atualiza pacotes vulneráveis; CodeQL procura falhas no seu código. Grátis em repositório público.

**Quando entra:** passo 5.3 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | PRs de segurança |
| → envia para | [aura-status](11-app.md#status) | Aplicação: sistemas AM (Aura) | alertas |

<a id="gcp"></a>

### Google Cloud

*Remoto · precisa de conta · futuro*

Terceira nuvem: só o básico, quando um projeto de IA ou dados pedir.

**Quando entra:** passo 30.5 · 2028 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Terraform](09-cnt.md#tf) | Containers, Kubernetes e infra como código | cria recursos |

<a id="gh"></a>

### GitHub

*Remoto · precisa de conta*

Código, vault, ensino-ti e a org grupo-amtech-digital. É também o seu portfólio.

**Quando entra:** passo 2.6 · Semana 1 · out/2026 (o e-mail e as críticas); o resto, 5 contas por semana até dez/2026; passo 5.1 · Semana 2 · nov/2026; passo 5.4 · Semana 2 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | dispara a cada push |
| → envia para | [Recrutadores](22-pub.md#recr) | Público e canais | portfólio |
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senhas e tokens |
| ← recebe de | [Obsidian + Git](03-win.md#obsd) | Windows 11, apps e máquinas virtuais | Obsidian Git |
| ← recebe de | [Git + SSH + gh](04-lin.md#git) | Linux (Ubuntu no WSL2, Arch no 2º disco) | push via SSH |
| ← recebe de | [dotfiles](04-lin.md#dot) | Linux (Ubuntu no WSL2, Arch no 2º disco) | versionado |
| ← recebe de | [Servidores MCP](05-ia.md#mcp) | Agentes de IA e sandbox | issues e PRs |
| ← recebe de | [Projects · ADRs · MkDocs](12-nuvem.md#ghproj) | Nuvem, código e entrega | issues e board |
| ← recebe de | [Dependabot + CodeQL](12-nuvem.md#dbot) | Nuvem, código e entrega | PRs de segurança |
| ← recebe de | [Commits assinados (chave SSH)](02-seg.md#sign) | Segurança e cofre | Verified |
| ← recebe de | [Chave física (YubiKey)](02-seg.md#ykey) | Segurança e cofre | 2FA |
| ← recebe de | [Codex (OpenAI)](07-chat.md#codex) | Assistentes de IA (chat, pesquisa e estudo) | mesmos repos |
| ← recebe de | [Agentes de código do Google](07-chat.md#gcode) | Assistentes de IA (chat, pesquisa e estudo) | mesmos repos |
| ← recebe de | [aura-status](11-app.md#status) | Aplicação: sistemas AM (Aura) | Dependabot e repos |
| ← recebe de | [Templates e código-fonte](17-prod.md#tmpl) | Produtos (o que você vende) | demo pública |
| ← recebe de | [Workstation com GPU](01-hw.md#ws) | Hardware | mesmos repositórios |
| ← recebe de | [Repositório do livro](15-editora.md#brepo) | Editora AMS Silva (produção de livros) | hospedado |
| ← recebe de | [Projeto do capítulo](15-editora.md#projcap) | Editora AMS Silva (produção de livros) | portfólio do aluno |

<a id="gha"></a>

### GitHub Actions

*Remoto*

CI/CD: build, testes, segurança e deploy.

**Quando entra:** passo 5.2 · Semana 2 · nov/2026; passo 16.1 · Semana 11 · jan/2027 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [GHCR (imagens)](12-nuvem.md#ghcr) | Nuvem, código e entrega | publica imagem |
| → envia para | [Azure](12-nuvem.md#azure) | Nuvem, código e entrega | deploy OIDC |
| → envia para | [Vercel](12-nuvem.md#vercel) | Nuvem, código e entrega | deploy front |
| → envia para | [GitHub Pages](12-nuvem.md#ghp) | Nuvem, código e entrega | publica sites |
| → envia para | [Cloudflare (DNS, Pages, e-mail)](12-nuvem.md#cf) | Nuvem, código e entrega | publica Pages |
| ← recebe de | [Testes: xUnit, Playwright, k6](11-app.md#tests) | Aplicação: sistemas AM (Aura) | roda no CI |
| ← recebe de | [SonarQube Cloud](12-nuvem.md#sonar) | Nuvem, código e entrega | análise no PR |
| ← recebe de | [GitHub](12-nuvem.md#gh) | Nuvem, código e entrega | dispara a cada push |

<a id="ghcr"></a>

### GHCR (imagens)

*Remoto*

Registro das imagens Docker das APIs.

**Quando entra:** passo 18.6 · Junto dos Passos 4 a 6 da trilha de estudo (≈ mar a jun/2027): o modelo nasce no Passo 4 (API e login) e ganha testes e qualidade no Passo 6 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Azure](12-nuvem.md#azure) | Nuvem, código e entrega | imagem |
| → envia para | [AWS](12-nuvem.md#aws) | Nuvem, código e entrega | imagem |
| ← recebe de | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | publica imagem |

<a id="ghp"></a>

### GitHub Pages

*Remoto*

Hospeda site pessoal, blog e Catálogo do HTML.

**Quando entra:** passo 13.7 · Semanas 6 e 7 · dez/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | publica sites |
| ← recebe de | [Site pessoal + blog (Jekyll)](18-web.md#site) | Vitrine web (sites e domínio) | hospedado |
| ← recebe de | [Catálogo do HTML](18-web.md#catal) | Vitrine web (sites e domínio) | hospedado |

<a id="cf"></a>

### Cloudflare (DNS, Pages, e-mail)

*Remoto · precisa de conta*

DNS, HTTPS, proteção, hospedagem estática dos sites comerciais e redirecionamento de e-mail do domínio. O Cloudflare Tunnel leva os webhooks de venda até o n8n sem abrir portas em casa.

**Quando entra:** passo 13.3 · Semanas 6 e 7 · dez/2026; passo 13.8 · Semanas 6 e 7 · dez/2026; passo 15.1 · Semana 11 · jan/2027; passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [n8n](21-mkt.md#n8n) | Marketing, automação e medição | túnel dos webhooks |
| ← recebe de | [Conector Cloudflare](08-clc.md#ccf) | Claude: recursos, conectores e plugins | DNS e Pages |
| ← recebe de | [Terraform](09-cnt.md#tf) | Containers, Kubernetes e infra como código | DNS por código |
| ← recebe de | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | publica Pages |
| ← recebe de | [Domínio (Registro.br)](18-web.md#dom) | Vitrine web (sites e domínio) | nameservers |
| ← recebe de | [Instituto AMS](18-web.md#inst) | Vitrine web (sites e domínio) | hospedado (Pages) |
| ← recebe de | [Site Grupo AMtech](18-web.md#amsite) | Vitrine web (sites e domínio) | hospedado (Pages) |

<a id="vercel"></a>

### Vercel

*Remoto · precisa de conta*

Frontends Next.js. O plano grátis é para uso pessoal e não comercial; confira os termos antes de pôr venda nele.

**Quando entra:** passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Vercel · AWS · Microsoft Learn](08-clc.md#cdev) | Claude: recursos, conectores e plugins | deploy e logs |
| ← recebe de | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | deploy front |

<a id="azure"></a>

### Azure

*Remoto · precisa de conta*

Primeira nuvem para as APIs AM: App Service/Container Apps, PostgreSQL, Key Vault.

**Quando entra:** passo 19.2 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028); passo 19.3 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028); passo 19.6 · Com o Passo 5 da trilha de estudo (≈ abr a jun/2027) para a conta e o deploy do sistema exemplo; o deploy de produção do AM Kaixara é o Passo 10 (≈ 2028) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [KeePassXC](02-seg.md#kee) | Segurança e cofre | senhas |
| ← recebe de | [Azure CLI · AWS CLI](09-cnt.md#clis) | Containers, Kubernetes e infra como código | comandos |
| ← recebe de | [Microsoft Learn + AWS Skill Builder](14-est.md#learn) | Estudo e carreira | certificação |
| ← recebe de | [Vercel · AWS · Microsoft Learn](08-clc.md#cdev) | Claude: recursos, conectores e plugins | documentação |
| ← recebe de | [Terraform](09-cnt.md#tf) | Containers, Kubernetes e infra como código | cria recursos |
| ← recebe de | [GitHub Actions](12-nuvem.md#gha) | Nuvem, código e entrega | deploy OIDC |
| ← recebe de | [GHCR (imagens)](12-nuvem.md#ghcr) | Nuvem, código e entrega | imagem |
| ← recebe de | [Sistemas AM (SaaS)](17-prod.md#saas) | Produtos (o que você vende) | roda na nuvem |

<a id="aws"></a>

### AWS

*Remoto · precisa de conta · futuro*

Segunda nuvem, para o mercado maior.

**Quando entra:** passo 30.4 · 2028 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Azure CLI · AWS CLI](09-cnt.md#clis) | Containers, Kubernetes e infra como código | comandos |
| ← recebe de | [Vercel · AWS · Microsoft Learn](08-clc.md#cdev) | Claude: recursos, conectores e plugins | documentação |
| ← recebe de | [Terraform](09-cnt.md#tf) | Containers, Kubernetes e infra como código | cria recursos |
| ← recebe de | [GHCR (imagens)](12-nuvem.md#ghcr) | Nuvem, código e entrega | imagem |
| ← recebe de | [Microsoft Learn + AWS Skill Builder](14-est.md#learn) | Estudo e carreira | Skill Builder |

<a id="b2"></a>

### Backblaze B2 (backup)

*Remoto · precisa de conta · futuro*

Cópia fora de casa do backup, criptografada pelo restic. US$ 6,95 por TB/mês.

**Quando entra:** passo 7.2 · Semana 3 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| ← recebe de | [Servidor caseiro (NAS + serviços)](01-hw.md#nas) | Hardware | restic diário |
| ← recebe de | [restic (backup criptografado)](02-seg.md#restic) | Segurança e cofre | criptografado |

<a id="gpuh"></a>

### GPU por hora (RunPod e afins)

*Remoto · precisa de conta*

Quando o Kaggle não bastar: GPU de 24 GB a partir de cerca de US$ 0,27 a 0,90 por hora no RunPod (out/2026). Um fine-tuning QLoRA de 8B costuma levar poucas horas. Use crédito pré-pago, sem cartão em débito automático.

**Quando entra:** passo 21.9 · Pendrives, GPU e laboratório a partir da semana 2; Zoomcamp, dbt e Airflow junto do IA2 da Trilha de Dados e IA do vault (depois do Passo 8, ≈ 2028); dataset e treino do 8B junto do IA6 (≈ 2029) ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Voz clonada (ElevenLabs)](13-cont.md#voz) | Produção de conteúdo | modelos abertos |
| → envia para | [Unsloth (QLoRA)](06-dados.md#unsl) | Dados e treino de IA | GPU de 24 GB |

<a id="gdrv"></a>

### Google Drive (seus documentos)

*Remoto · precisa de conta*

Onde estão hoje as suas aulas, apostilas, provas, especificações e planos, misturados com cópias repetidas e documentos pessoais. O Google Takeout tira uma cópia completa para o acervo.

**Quando entra:** passo 0.5 · Antes de tudo · semana 1 (out/2026); passo 8.1 · Semanas 3 e 4 · nov/2026 ([roteiro](../implantacao/roteiro.md))

| Direção | Bloco | Camada | O que passa |
|---|---|---|---|
| → envia para | [Acervo (seus documentos)](23-oper.md#acv) | Operação do grupo (esteira, marca, qualidade) | cópia pelo Takeout |
| ← recebe de | [Conector Google (Gmail, Drive…)](08-clc.md#cgws) | Claude: recursos, conectores e plugins | o Claude lê o Drive |

---

[↑ Camada 13 · Produção de conteúdo](13-cont.md) · [↓ Camada 11 · Aplicação: sistemas AM (Aura)](11-app.md)
