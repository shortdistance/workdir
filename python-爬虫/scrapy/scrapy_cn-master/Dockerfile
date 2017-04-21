FROM ubuntu:14.04

RUN sed -i.bal 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update

ADD http://archive.scrapy.org/ubuntu/archive.key /tmp/scrapy.key
RUN apt-key add /tmp/scrapy.key
RUN echo "deb http://archive.scrapy.org/ubuntu precise main" > /etc/apt/sources.list.d/scrapy.list
RUN apt-get update -qq
RUN apt-get install -y scrapy-0.24
RUN apt-get install -y git
RUN apt-get install -y python-pip

RUN mkdir /opt/qfbot
RUN cd /opt/qfbot && \
    git clone https://github.com/qfboys/qfbot.git

EXPOSE 80,
RUN (cd /home/web && git clone https://github.com/addwork/scrapy_cn.git)
RUN (cd /home/web/scrapy_cn && pip install -r requirements.txt)

