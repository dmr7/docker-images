FROM rancher/debianconsole:v0.3.1
MAINTAINER WOW! Group Development

RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/backports.list \
 && apt-get update \
 && apt-get upgrade --no-install-recommends -y \
 && apt-get install -y --no-install-recommends openjdk-8-jdk subversion git curl uuid-runtime \
 && mkdir -p /usr/local/bin \
 && curl -L https://github.com/remind101/emp/releases/download/v0.9.2/emp-linux-amd64-0.9.2.tgz | tar -C /usr/local/bin -xzf - \
 && chmod +x /usr/local/bin/emp \
 && locale-gen --purge en_US.UTF-8 \
 && echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY bin/* /usr/local/bin/
