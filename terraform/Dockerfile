FROM alpine:3.3
MAINTAINER WOW! Group Development

RUN apk -Uv add ca-certificates \
 && update-ca-certificates \
 && wget -O /tmp/terraform.zip https://releases.hashicorp.com/terraform/0.6.11/terraform_0.6.11_linux_amd64.zip \
 && unzip /tmp/terraform.zip -d /usr/local/bin \
 && mkdir -p /workspace \
 && rm -rf /tmp/terraform.zip /var/cache/apk/*

ADD runner /
WORKDIR /workspace
ENTRYPOINT ["/runner"]
