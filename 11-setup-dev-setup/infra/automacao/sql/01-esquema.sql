-- Banco de métricas do Grupo AMtech: vendas, gastos com anúncio, ferramentas, impostos e publicações.
-- Roda sozinho na primeira subida do container (docker-entrypoint-initdb.d).

CREATE TABLE produtos (
    id              text PRIMARY KEY,                 -- ex.: minicurso-logica
    nome            text NOT NULL,
    plataforma      text NOT NULL,                    -- hotmart, kiwify, eduzz, udemy, proprio...
    preco           numeric(10,2) NOT NULL CHECK (preco >= 0),
    taxa_percentual numeric(6,4) NOT NULL DEFAULT 0,   -- 0.0990 = 9,9%
    taxa_fixa       numeric(10,2) NOT NULL DEFAULT 0,
    custo_variavel  numeric(10,2) NOT NULL DEFAULT 0,
    ativo           boolean NOT NULL DEFAULT true
);

CREATE TABLE vendas (
    id              bigserial PRIMARY KEY,
    id_externo      text NOT NULL,                    -- id da transação na plataforma
    plataforma      text NOT NULL,
    produto_id      text REFERENCES produtos(id),
    data            timestamptz NOT NULL,
    valor           numeric(10,2) NOT NULL,
    taxa_cobrada    numeric(10,2) NOT NULL DEFAULT 0,
    comissao        numeric(10,2) NOT NULL DEFAULT 0, -- afiliado
    status          text NOT NULL CHECK (status IN ('paga', 'reembolsada', 'chargeback', 'pendente')),
    pais            char(2),
    utm_source      text,
    utm_medium      text,
    utm_campaign    text,
    utm_content     text,
    recebido_em     timestamptz NOT NULL DEFAULT now(),
    UNIQUE (plataforma, id_externo)                   -- webhook repetido não duplica venda
);

CREATE TABLE gastos (
    id              bigserial PRIMARY KEY,
    data            date NOT NULL,
    canal           text NOT NULL,                    -- meta, google, tiktok, kwai, spotify...
    campanha        text NOT NULL,
    criativo        text,
    valor           numeric(10,2) NOT NULL CHECK (valor >= 0),
    UNIQUE (data, canal, campanha, criativo)
);

CREATE TABLE ferramentas (
    id              text PRIMARY KEY,
    nome            text NOT NULL,
    valor_mensal    numeric(10,2) NOT NULL,
    moeda           char(3) NOT NULL DEFAULT 'BRL',
    produtos        text[] NOT NULL DEFAULT '{}'      -- produtos que a ferramenta atende
);

CREATE TABLE impostos (
    mes             date PRIMARY KEY,                 -- primeiro dia do mês
    base            numeric(12,2) NOT NULL,
    imposto_pago    numeric(12,2) NOT NULL
);

CREATE TABLE publicacoes (
    id              bigserial PRIMARY KEY,
    rede            text NOT NULL,                    -- youtube, instagram, tiktok, linkedin...
    publicado_em    timestamptz NOT NULL,
    oferta_id       text,                             -- id do data/portfolio.json
    titulo          text,
    url             text,
    alcance         integer,
    retencao_media  numeric(5,2),                     -- % assistido
    cliques         integer,
    atualizado_em   timestamptz NOT NULL DEFAULT now()
);

-- Lucro por produto e mês: receita líquida − anúncio da campanha do produto (pela UTM).
-- Regra: cada campanha de anúncio divulga um produto só (utm_campaign única por produto).
CREATE VIEW lucro_por_produto_mes AS
WITH v AS (
    SELECT date_trunc('month', data)::date AS mes, produto_id, utm_campaign,
           sum(valor) FILTER (WHERE status = 'paga') AS receita,
           sum(valor - taxa_cobrada - comissao) FILTER (WHERE status = 'paga') AS liquido,
           count(*) FILTER (WHERE status = 'paga') AS vendas,
           count(*) FILTER (WHERE status IN ('reembolsada', 'chargeback')) AS devolucoes
    FROM vendas GROUP BY 1, 2, 3
), g AS (
    SELECT date_trunc('month', data)::date AS mes, campanha, sum(valor) AS anuncio
    FROM gastos GROUP BY 1, 2
)
SELECT v.mes, v.produto_id, v.utm_campaign,
       coalesce(v.receita, 0) AS receita, coalesce(v.liquido, 0) AS liquido,
       coalesce(g.anuncio, 0) AS anuncio,
       coalesce(v.liquido, 0) - coalesce(g.anuncio, 0) AS lucro_antes_imposto,
       v.vendas, v.devolucoes,
       CASE WHEN v.vendas > 0 THEN round(coalesce(g.anuncio, 0) / v.vendas, 2) END AS cpa
FROM v LEFT JOIN g ON g.mes = v.mes AND g.campanha = v.utm_campaign;

-- Desempenho por rede, dia da semana e hora (base do algoritmo de melhor horário).
CREATE VIEW desempenho_por_horario AS
SELECT rede,
       extract(isodow FROM publicado_em AT TIME ZONE 'America/Sao_Paulo')::int AS dia_semana,
       extract(hour FROM publicado_em AT TIME ZONE 'America/Sao_Paulo')::int AS hora,
       count(*) AS publicacoes,
       round(avg(alcance)) AS alcance_medio,
       round(avg(retencao_media), 1) AS retencao_media,
       round(avg(cliques), 1) AS cliques_medios
FROM publicacoes
GROUP BY 1, 2, 3;
