FROM nginx
MAINTAINER WOW! Group Development

RUN apt-get -y update \
 && apt-get -y install curl unzip \
 && curl -sSL -o /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-template/0.14.0/consul-template_0.14.0_linux_amd64.zip \
 && unzip /tmp/cnsltmpl.zip -d /usr/local/bin \
 && chmod +x /usr/local/bin/consul-template \
 && apt-get -y remove --purge curl unzip \
 && apt-get -y autoremove --purge \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/nginx/conf.d/*

ADD forego /usr/local/bin/
ADD Procfile /
ADD nginx.conf.tmpl /etc/nginx/

EXPOSE 8080 8081
CMD ["forego", "start", "-f", "/Procfile"]
