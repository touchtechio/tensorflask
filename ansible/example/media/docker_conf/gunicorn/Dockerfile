#FROM ubuntu:latest
#FROM python:3
FROM ubuntu:16.04
MAINTAINER Matt Pinner "dev@touchtech.io"
#RUN add-apt-repository universe
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# todo: try a git checkout... one-day
# RUN git clone https://github.com/Runscope/healthcheck.git
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn"]
#CMD ["server.py"]
CMD ["-b", ":5000", "wsgi"]

