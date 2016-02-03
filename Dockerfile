FROM ubuntu:latest

MAINTAINER jiaju.chen@ele.com

RUN apt-get update
RUN apt-get install -y python2.7-dev
RUN apt-get install -y curl

WORKDIR /tmp
RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2.7
ADD requirements.txt /tmp/requirements.txt
RUN pip install -q -r  /tmp/requirements.txt

ADD notissue/ /data/notissue
ENV PYTHONPATH=/data
CMD ["/usr/local/bin/gunicorn", "-b :5000", "notissue:app"]
