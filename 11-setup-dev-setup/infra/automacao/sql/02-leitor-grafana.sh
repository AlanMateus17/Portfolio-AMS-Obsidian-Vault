#!/bin/sh
# Cria o usuário só de leitura que o Grafana usa. A senha vem de GRAFANA_DB_SENHA (no .env).
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<SQL
CREATE ROLE grafana_leitor LOGIN PASSWORD '${GRAFANA_DB_SENHA}';
GRANT CONNECT ON DATABASE ${POSTGRES_DB} TO grafana_leitor;
GRANT USAGE ON SCHEMA public TO grafana_leitor;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO grafana_leitor;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO grafana_leitor;
SQL
