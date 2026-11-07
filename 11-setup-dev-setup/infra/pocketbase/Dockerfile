# PocketBase + Litestream: backend de validação (MVP) num binário só, com o SQLite copiado em tempo real para o R2.
# Versões em build-arg (pegue as mais novas nas páginas de release):
#   docker build --build-arg PB_VERSAO=x.y.z --build-arg LS_VERSAO=x.y.z -t pocketbase-mvp infra/pocketbase
ARG LS_VERSAO
FROM litestream/litestream:${LS_VERSAO} AS litestream

FROM alpine:3.22
ARG PB_VERSAO
RUN test -n "$PB_VERSAO" \
 && apk add --no-cache ca-certificates unzip wget \
 && wget -q "https://github.com/pocketbase/pocketbase/releases/download/v${PB_VERSAO}/pocketbase_${PB_VERSAO}_linux_amd64.zip" -O /tmp/pb.zip \
 && unzip /tmp/pb.zip pocketbase -d /usr/local/bin && rm /tmp/pb.zip
COPY --from=litestream /usr/local/bin/litestream /usr/local/bin/litestream
COPY litestream.yml /etc/litestream.yml
COPY entrada.sh /usr/local/bin/entrada.sh
RUN chmod +x /usr/local/bin/entrada.sh
EXPOSE 8090
VOLUME /pb_data
ENTRYPOINT ["/usr/local/bin/entrada.sh"]
