FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.2
MAINTAINER Simon Meoni

## Dependencies
RUN yum -y update && yum -y install epel-release
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm yum -y install yum-utils
RUN yum -y install python36u python36u-pip curl
RUN pip3.6 install --upgrade pip
# copy needed files
COPY deploy.py .
COPY requirements.txt .
COPY header.csv .
COPY header.csv .
COPY demonette-1.2.csv .
COPY fields-to-mapped.txt .
COPY license.json .

RUN pip3.6 install -r requirements.txt
RUN su elasticsearch -c "elasticsearch -d && sleep 30 && curl -XPUT 'http://localhost:9200/_xpack/license' -H 'Content-Type: application/json' -d @license.json"
RUN su elasticsearch -c "elasticsearch -d && sleep 30 && python3.6 deploy.py"
