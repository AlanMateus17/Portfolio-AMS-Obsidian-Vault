# 7 · O que vai para a nuvem gastando pouco

[← Motor de decisão](README.md) · Base existente: [docs/nuvem.md](../../nuvem.md) e [operação 24 horas](../../operacao/24-horas.md)

Online só o que precisa ficar ligado 24 horas ou ser acessado de fora. IA pesada fica no notebook (GPU) e nas assinaturas; servidor barato sem GPU roda modelo devagar demais.

## Na nuvem

- **n8n** (webhooks de Hotmart, pagamentos e formulários com o notebook desligado).
- **PostgreSQL do Núcleo AMtech** (registro, catálogo, lições).
- **LiteLLM** para os agentes que rodam sozinhos.
- **Monitoramento** (Uptime Kuma).
- **Backup fora de casa** (a cópia "1" da regra 3-2-1).
- **Sites e páginas estáticas.**

## No notebook

Ollama e modelos locais, laboratório de dissecação e garimpo, desenvolvimento, dados sensíveis sem criptografia.

## Fase 0: grátis

- **GitHub Actions:** CI, checagens de segurança, tarefas agendadas (dentro da cota).
- **Cloudflare:** sites estáticos, funções pequenas, armazenamento de backup na camada gratuita.
- **Oracle Cloud Always Free:** a cota Ampere A1 caiu pela metade em 2026, de 4 OCPU/24 GB para 2 OCPU/12 GB ([fonte](https://terminalbytes.com/oracle-cloud-free-tier-changes-2026)). Basta para n8n, PostgreSQL, LiteLLM e monitoramento. Cuidados: capacidade não garantida, arquitetura ARM (não roda binário x86 direto) e risco de recolhimento de máquina parada. Tratar como descartável, com tudo declarado no repositório para recriar em minutos.
- **Rede privada** (Tailscale ou equivalente) ligando notebook e VM sem abrir portas.

## Fase 1: quando uma renda pagar

**Hostinger KVM 2:** 2 vCPU, 8 GB RAM, 100 GB NVMe, 8 TB de banda, servidor em São Paulo. Promoção R$ 35,09/mês com renovação a R$ 69,99/mês em contrato longo ([fonte](https://horadecodar.com.br/valor-vps/)); usar o valor de renovação nas contas. Vira a máquina principal; a Oracle vira reserva.

## Performance

A nuvem orquestra, o notebook faz o pesado. Notebook desligado → modo degradado: o roteador usa assinaturas e camadas gratuitas até ele voltar.

Preços e cotas conferidos em 11/11/2026; mudam com frequência.
