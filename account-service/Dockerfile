FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Export application port
EXPOSE 8000

FROM base AS build

RUN mkdir /account-service
WORKDIR /account-service/account

# Copy source code & libraries
COPY ["/account-service/account", "/account-service/account"]

COPY ["/account-service/account/run.sh", "/account-service"]
RUN ["chmod", "+x", "/account-service/run.sh"]
# Copy dependencies file to container working directory
COPY ["./account-service/requirements.txt", "/account-service/account"]


# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT . ../run.sh
