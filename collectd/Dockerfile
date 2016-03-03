FROM debian:jessie-backports
MAINTAINER WOW! Group Development

RUN apt-get -y update \
 && apt-get -y dist-upgrade \
 && apt-get -y -t jessie-backports install collectd \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD collectd.conf /etc/collectd/

EXPOSE 8125/udp
ENTRYPOINT ["/usr/sbin/collectd", "-f"]
