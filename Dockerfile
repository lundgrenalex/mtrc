FROM python:3.8-slim-buster
RUN groupadd deploy && useradd -g deploy deploy

COPY . /mtrc

RUN apt-get update -qq && apt-get install gcc openssh-client git -y

WORKDIR /mtrc
ENV PYTHONPATH /mtrc
RUN pip3 install --upgrade pip && pip3 install flake8
#RUN flake8 .
RUN pip3 install -r requirements.txt

ENTRYPOINT ["gunicorn", "application:app", "--bind", "0.0.0.0:8087", "--workers", "1", "--worker-connections=1000", "--backlog=1000", "--timeout", "60", "--log-level=info", "--pid", "./run/events_handler.pid", "--log-file=./logs/mrtc.log"]
