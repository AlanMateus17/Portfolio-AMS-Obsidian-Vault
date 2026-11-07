-- Banco central do Núcleo AMtech (ADR 0009), versão SQLite: o mesmo modelo do PostgreSQL da VM (esquema-postgres.sql).
PRAGMA journal_mode = WAL;

CREATE TABLE IF NOT EXISTS eventos (
  id      INTEGER PRIMARY KEY,
  quando  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime')),
  tipo    TEXT NOT NULL,            -- ex.: venda.aprovada, erro.producao, backup.concluido, triagem.feita
  fonte   TEXT NOT NULL DEFAULT 'manual',
  dados   TEXT NOT NULL DEFAULT '{}' -- JSON
);
CREATE INDEX IF NOT EXISTS eventos_tipo ON eventos (tipo, quando);

CREATE TABLE IF NOT EXISTS conhecimento (
  id      INTEGER PRIMARY KEY,
  quando  TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime')),
  tipo    TEXT NOT NULL CHECK (tipo IN ('adr','triagem','garimpo','padrao','trecho','licao','recusa','nota','referencia')),
  titulo  TEXT NOT NULL,
  texto   TEXT NOT NULL,
  origem  TEXT NOT NULL DEFAULT '',  -- arquivo, URL ou repositório de onde veio
  tags    TEXT NOT NULL DEFAULT '',
  chave   TEXT UNIQUE                -- evita duplicar o que é importado de novo (ex.: adr:0005)
);
CREATE VIRTUAL TABLE IF NOT EXISTS conhecimento_fts USING fts5(
  titulo, texto, tags, content='conhecimento', content_rowid='id', tokenize='unicode61 remove_diacritics 2'
);
CREATE TRIGGER IF NOT EXISTS conhecimento_ai AFTER INSERT ON conhecimento BEGIN
  INSERT INTO conhecimento_fts(rowid, titulo, texto, tags) VALUES (new.id, new.titulo, new.texto, new.tags);
END;
CREATE TRIGGER IF NOT EXISTS conhecimento_ad AFTER DELETE ON conhecimento BEGIN
  INSERT INTO conhecimento_fts(conhecimento_fts, rowid, titulo, texto, tags) VALUES ('delete', old.id, old.titulo, old.texto, old.tags);
END;
CREATE TRIGGER IF NOT EXISTS conhecimento_au AFTER UPDATE ON conhecimento BEGIN
  INSERT INTO conhecimento_fts(conhecimento_fts, rowid, titulo, texto, tags) VALUES ('delete', old.id, old.titulo, old.texto, old.tags);
  INSERT INTO conhecimento_fts(rowid, titulo, texto, tags) VALUES (new.id, new.titulo, new.texto, new.tags);
END;

CREATE TABLE IF NOT EXISTS tarefas (
  id          INTEGER PRIMARY KEY,
  criada      TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime')),
  titulo      TEXT NOT NULL,
  estado      TEXT NOT NULL DEFAULT 'aberta' CHECK (estado IN ('aberta','fazendo','esperando-ok','feita','cancelada')),
  responsavel TEXT NOT NULL DEFAULT 'alan',
  evento_id   INTEGER REFERENCES eventos(id)
);

CREATE TABLE IF NOT EXISTS auditoria (
  id           INTEGER PRIMARY KEY,
  quando       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime')),
  agente       TEXT NOT NULL,
  acao         TEXT NOT NULL,
  nivel        TEXT NOT NULL CHECK (nivel IN ('automatico','avisa','pede-ok','proibido')),
  motivo       TEXT NOT NULL DEFAULT '',
  resultado    TEXT NOT NULL DEFAULT '',
  aprovado_por TEXT
);

-- Passos do roteiro que você já terminou (just feito ID). O Acompanhamento no navegador guarda o dele à parte.
CREATE TABLE IF NOT EXISTS passos_feitos (
  passo  TEXT PRIMARY KEY,
  quando TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime'))
);

-- Domínio de cada tópico do Professor: nível 0 (nada) a 4 (ensinou) e a próxima revisão espaçada.
CREATE TABLE IF NOT EXISTS dominio (
  topico          TEXT PRIMARY KEY,
  nivel           INTEGER NOT NULL DEFAULT 0 CHECK (nivel BETWEEN 0 AND 4),
  ultima_nota     INTEGER,
  intervalo_dias  INTEGER NOT NULL DEFAULT 0,
  proxima_revisao TEXT,
  atualizado      TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%S', 'now', 'localtime'))
);
