FROM alpine:3.3
MAINTAINER WOW! Group Development

RUN apk -Uv add curl \
 && rm -rf /var/cache/apk/*

ENTRYPOINT ["/usr/bin/curl"]
