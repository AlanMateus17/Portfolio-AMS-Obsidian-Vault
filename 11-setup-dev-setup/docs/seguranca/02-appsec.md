# AppSec nos seus sistemas

[← Segurança](README.md)

Software com zero erro não existe. O que existe é um processo que pega a maior parte dos erros antes do cliente e que, quando um escapa, mostra onde ele passou. Este é o processo para os sistemas AM, montado em camadas: cada uma pega o que a anterior deixou passar.

## As camadas

| # | Quando | O que pega | Peça do setup |
|---|---|---|---|
| 1 | Antes de codar | Falha de desenho (permissão errada, fluxo de dinheiro sem conferência) | Modelagem de ameaças STRIDE (`infra/templates/seguranca/modelagem-ameacas.md`) |
| 2 | Antes de codar | Requisito esquecido | Checklist ASVS nível 1, no mesmo arquivo |
| 3 | Ao escrever | Erro de lógica | Testes automatizados (xUnit) para cada mitigação da tabela STRIDE |
| 4 | No commit | Senha e chave no código | gitleaks (pre-commit e CI do repositório padrão) |
| 5 | No push | Padrão inseguro conhecido | Semgrep e CodeQL |
| 6 | No push | Biblioteca vulnerável | Trivy e Dependabot |
| 7 | Toda semana | Configuração exposta no ar (cabeçalho, cookie, versão) | ZAP passivo na homologação (`dast-zap.yml`) |
| 8 | Antes de vender | O que só um humano acha (IDOR, regra de negócio) | Você testando o próprio sistema com o Burp, como faria num cliente |
| 9 | Depois do ar | O que escapou de tudo | Sentry, logs (Seq) e o teste de restauração do backup |

As camadas 4 a 6 já estão no repositório padrão (`infra/templates/repo-padrao`). Esta frente acrescenta 1, 2, 7 e 8.

## O erro que nenhum scanner acha

A falha mais comum em sistema de pequena empresa não é técnica, é de autorização: a rota confere se a pessoa está logada, mas não se o dado é dela (IDOR). No AM Kaixara isso seria um caixa vendo o fechamento de outra loja. A defesa:

- Toda consulta filtra pelo dono (tenant, loja, usuário) no servidor, de preferência num filtro padrão do ORM (Prisma/Drizzle).
- Toda rota tem política de autorização explícita; rota sem política falha no teste.
- Um teste de integração por papel: "caixa da loja A não lê nada da loja B".

## Os repositórios de referência (passo sg-arquitetura)

Para ver onde a sua arquitetura erra, compare com projetos grandes e documentados. Não leia de cima a baixo:

1. Escolha uma funcionalidade (criar pedido).
2. Siga o caminho dela da API até o banco no projeto de referência.
3. Faça o mesmo no AM Kaixara.
4. Cada diferença vira uma ADR: adotar, adaptar ou manter o seu jeito, com o motivo.

| Repositório | O que observar |
|---|---|
| `dotnet/eShop` | Referência de arquitetura (.NET, carta de reserva): serviços, eventos, identidade |
| `kgrzybek/modular-monolith-with-ddd` | Monólito modular com DDD: padrões aplicáveis em qualquer stack, inclusive o AM Gestão |
| `jasontaylordev/CleanArchitecture` e `ardalis/CleanArchitecture` | Organização de camadas, validação e testes |
| `bitwarden/server` | Produto real em .NET com segurança como requisito central |
| `donnemartin/system-design-primer` | Teoria de escala para quando o Aura crescer |

## Checklist antes de publicar qualquer versão

- [ ] Tabela STRIDE atualizada para o que mudou, e cada mitigação nova com teste.
- [ ] CI verde: gitleaks, Semgrep, Trivy e testes.
- [ ] ZAP passivo sem alerta alto na homologação.
- [ ] Nenhum segredo no front ou na `.dll` (abra no ILSpy e confira).
- [ ] Backup restaurado de verdade na última semana.
