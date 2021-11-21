FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /CSElite
WORKDIR /CSElite
COPY . /CSElite
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc g++ libc-dev linux-headers postgresql-dev
RUN apk add --update --no-cache postgresql-client postgresql jpeg-dev zlib-dev libjpeg
RUN pip3 install -r /CSElite/requirements.txt
RUN apk del .tmp-build-deps
RUN adduser -D CSElite
USER CSElite
