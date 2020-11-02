FROM python:3-alpine
MAINTAINER Tegshbayar Pujii <tegshbayar.p@gmail.com>

RUN mkdir -p /usr/srcs/app
WORKDIR /usr/srcs/app

COPY requirements.txt /usr/srcs/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/srcs/app

EXPOSE 5000

CMD [ "python", "/usr/srcs/app/app_rotas.py" ]
