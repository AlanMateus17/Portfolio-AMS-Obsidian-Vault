-- Banco central do Núcleo AMtech na VM (PostgreSQL 17 + pgvector). Mesmo modelo do esquema.sql (SQLite).
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS unaccent;
CREATE SCHEMA IF NOT EXISTS nucleo;

CREATE TABLE IF NOT EXISTS nucleo.eventos (
  id bigserial PRIMARY KEY, quando timestamptz NOT NULL DEFAULT now(),
  tipo text NOT NULL, fonte text NOT NULL DEFAULT 'manual', dados jsonb NOT NULL DEFAULT '{}'
);
CREATE INDEX IF NOT EXISTS eventos_tipo ON nucleo.eventos (tipo, quando);

CREATE TABLE IF NOT EXISTS nucleo.conhecimento (
  id bigserial PRIMARY KEY, quando timestamptz NOT NULL DEFAULT now(),
  tipo text NOT NULL CHECK (tipo IN ('adr','triagem','garimpo','padrao','trecho','licao','recusa','nota','referencia')),
  titulo text NOT NULL, texto text NOT NULL, origem text NOT NULL DEFAULT '', tags text NOT NULL DEFAULT '',
  chave text UNIQUE,
  busca tsvector GENERATED ALWAYS AS (to_tsvector('portuguese', titulo || ' ' || texto || ' ' || tags)) STORED,
  embedding vector(768)   -- preenchido pelo modelo de embeddings local (fase 4)
);
CREATE INDEX IF NOT EXISTS conhecimento_busca ON nucleo.conhecimento USING gin (busca);

CREATE TABLE IF NOT EXISTS nucleo.tarefas (
  id bigserial PRIMARY KEY, criada timestamptz NOT NULL DEFAULT now(), titulo text NOT NULL,
  estado text NOT NULL DEFAULT 'aberta' CHECK (estado IN ('aberta','fazendo','esperando-ok','feita','cancelada')),
  responsavel text NOT NULL DEFAULT 'alan', evento_id bigint REFERENCES nucleo.eventos(id)
);

CREATE TABLE IF NOT EXISTS nucleo.auditoria (
  id bigserial PRIMARY KEY, quando timestamptz NOT NULL DEFAULT now(), agente text NOT NULL, acao text NOT NULL,
  nivel text NOT NULL CHECK (nivel IN ('automatico','avisa','pede-ok','proibido')),
  motivo text NOT NULL DEFAULT '', resultado text NOT NULL DEFAULT '', aprovado_por text
);

CREATE TABLE IF NOT EXISTS nucleo.passos_feitos (passo text PRIMARY KEY, quando timestamptz NOT NULL DEFAULT now());

CREATE TABLE IF NOT EXISTS nucleo.dominio (topico text PRIMARY KEY, nivel smallint NOT NULL DEFAULT 0 CHECK (nivel BETWEEN 0 AND 4),
  ultima_nota smallint, intervalo_dias integer NOT NULL DEFAULT 0, proxima_revisao date, atualizado timestamptz NOT NULL DEFAULT now());
