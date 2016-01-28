FROM gliderlabs/consul:0.6
MAINTAINER WOW! Group Development

RUN apk --update add jq && rm -rf /var/cache/apk/*
ADD ./runner /runner
ADD ./config /config/
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp

ENTRYPOINT ["/runner"]
