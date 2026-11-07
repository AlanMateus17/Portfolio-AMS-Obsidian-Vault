#!/bin/sh
# Restaura do R2 se o disco estiver vazio e sobe o PocketBase com o Litestream replicando.
set -eu
if [ ! -f /pb_data/data.db ]; then litestream restore -if-replica-exists -config /etc/litestream.yml /pb_data/data.db; fi
exec litestream replicate -config /etc/litestream.yml -exec "pocketbase serve --http=0.0.0.0:8090 --dir=/pb_data"
