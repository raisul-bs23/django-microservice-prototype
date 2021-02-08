FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


EXPOSE 8000

FROM base as build

RUN mkdir /account-service
WORKDIR /account-service/account

COPY ["/account-service/account", "/account-service/account"]

COPY ["/account-service/account/run.sh", "/account-service"]
RUN ["chmod", "+x", "/account-service/run.sh"]

COPY ["./account-service/requirements.txt", "/account-service/account"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT . ../run.sh






