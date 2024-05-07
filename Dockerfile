FROM python:3.11

RUN mkdir -p /home/TelZone
RUN mkdir -p /home/static
RUN mkdir -p /home/media
WORKDIR /home/TelZone

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
