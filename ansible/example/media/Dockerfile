FROM ubuntu:latest
MAINTAINER Matt Pinner "dev@touchtech.io"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
# todo: try a git checkout... one-day
# RUN git clone https://github.com/Runscope/healthcheck.git
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]
