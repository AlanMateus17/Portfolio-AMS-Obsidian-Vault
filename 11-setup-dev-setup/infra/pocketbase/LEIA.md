# PocketBase + Litestream: validar antes de construir

Para um MVP (o AM Rendara, um protótipo para cliente) antes de gastar semanas no Aura: banco, login, arquivos, tempo real e painel num binário só. O Litestream copia o SQLite para o R2 a cada segundo, e o `entrada.sh` restaura sozinho se a VM for recriada.

Se o MVP vender, o sistema de verdade nasce no Aura (.NET + PostgreSQL) e os dados migram. Se não vender, você perdeu dias, não meses.

Sem Docker, no Ubuntu: `mise install` já traz os dois binários; `litestream replicate -exec "pocketbase serve"` faz o mesmo.

Na primeira subida, confira no log que a réplica começou (`docker compose logs pocketbase`). O formato do `litestream.yml` é o das versões 0.3 a 0.5; se uma versão nova mudar, ajuste pela documentação do Litestream.
