FROM elasticsearch:1.7
MAINTAINER WOW! Group Development

RUN plugin install srv-discovery --url https://github.com/github/elasticsearch-srv-discovery/releases/download/1.5.0/elasticsearch-srv-discovery-1.5.0.zip
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.7.1
ADD ./runner /runner

ENTRYPOINT ["/runner"]
