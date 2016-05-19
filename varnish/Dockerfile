FROM alpine:edge
MAINTAINER WOW! Group Development

RUN apk -Uv add varnish su-exec openssl \
 && apk add -UvX http://dl-cdn.alpinelinux.org/alpine/edge/community/ tini \
 && wget -O /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip \
 && unzip /tmp/cnsltmpl.zip -d /usr/local/bin \
 && chmod +x /usr/local/bin/consul-template \
 && touch /etc/varnish/default.vcl \
 && apk --purge -v del openssl \
 && rm -rf /tmp/* /var/cache/apk/*

ADD runner reload /
ADD default.vcl default.vcl.tmpl /etc/varnish/
EXPOSE 8080
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/runner"]
