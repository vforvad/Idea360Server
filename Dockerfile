FROM python:3.6.2

ARG DEFAULT_REQUIREMENTS
ENV REQUIREMENTS $DEFAULT_REQUIREMENTS

RUN mkdir /idea360
WORKDIR /idea360

ADD ./requirements /idea360/requirements
RUN pip install -r ./requirements/$REQUIREMENTS

ADD . /idea360
