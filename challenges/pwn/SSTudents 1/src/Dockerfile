FROM pwn.red/jail
COPY --from=ubuntu:22.04 / /srv

COPY ./server /srv/app/run

RUN chmod +x /srv/app/run