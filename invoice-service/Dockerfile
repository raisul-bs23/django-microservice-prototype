FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Export application port
EXPOSE 8000

FROM base AS build

RUN mkdir /invoice-service
WORKDIR /invoice-service/invoice

# Copy source code & libraries
COPY ["/invoice-service/invoice", "/invoice-service/invoice"]

# Copy dependencies file to container working directory
COPY ["./invoice-service/requirements.txt", "/invoice-service/invoice"]

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG COLLECT_STATIC
RUN mkdir /invoice-service/api-static
RUN python manage.py collectstatic --no-input
CMD python manage.py runserver 0.0.0.0:8000
