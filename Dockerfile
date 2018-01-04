FROM python:3.6.2
RUN mkdir /idea360
WORKDIR /idea360
ADD requirements.txt /idea360/
RUN pip install -r requirements.txt
ADD . /idea360
