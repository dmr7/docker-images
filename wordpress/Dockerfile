FROM wordpress
MAINTAINER WOW! Group Development

RUN apt-get -y update \
 && apt-get -y install unzip \
 && curl -sSL -o /tmp/rest-api.zip https://downloads.wordpress.org/plugin/rest-api.2.0-beta13.1.zip \
 && unzip -d /usr/src/wordpress/wp-content/plugins /tmp/rest-api.zip \
 && sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf \
 && apt-get -y purge --auto-remove unzip \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 8080
