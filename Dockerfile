FROM ubuntu:latest

MAINTAINER jiaju.chen@ele.me

RUN apt-get update
RUN apt-get install -y python2.7-dev
RUN apt-get install -y curl

WORKDIR /tmp
RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -q -r  /tmp/requirements.txt

ADD notissue/ /data/notissue
ENV PYTHONPATH=/data
RUN mkdir -p /data/logs/notissue
VOLUME /data/logs/notissue
CMD ["/usr/local/bin/gunicorn", "-b :5000", "--access-logfile=/data/logs/notissue/falcon.log", "notissue:app"]
