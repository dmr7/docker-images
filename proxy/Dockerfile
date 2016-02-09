FROM nginx
MAINTAINER WOW! Group Development

RUN apt-get -y update \
 && apt-get -y install curl unzip \
 && curl -sSL -o /usr/local/bin/forego https://godist.herokuapp.com/projects/ddollar/forego/releases/current/linux-amd64/forego \
 && curl -sSL -o /tmp/cnsltmpl.zip https://releases.hashicorp.com/consul-template/0.12.2/consul-template_0.12.2_linux_amd64.zip \
 && unzip /tmp/cnsltmpl.zip -d /usr/local/bin \
 && chmod +x /usr/local/bin/forego /usr/local/bin/consul-template \
 && apt-get -y remove --purge curl unzip \
 && apt-get -y autoremove --purge \
 && apt-get -y clean \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/nginx/conf.d/*

ADD Procfile /
ADD app.conf.tmpl /etc/

CMD ["forego", "start", "-f", "/Procfile"]
