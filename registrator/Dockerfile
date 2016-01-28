FROM gliderlabs/registrator:master
MAINTAINER WOW! Group Development

RUN apk -Uv add curl \
 && rm -rf /var/cache/apk/*
ADD ./runner /runner

ENTRYPOINT ["/runner"]
