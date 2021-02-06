FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Export application port
EXPOSE 8000

FROM base AS build

RUN mkdir /order-service
WORKDIR /order-service/order

# Copy source code & libraries
COPY ["/order-service/order", "/order-service/order"]

# Copy dependencies file to container working directory
COPY ["./order-service/requirements.txt", "/order-service/order"]

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG COLLECT_STATIC
RUN mkdir /order-service/api-static
RUN python manage.py collectstatic --no-input
CMD python manage.py runserver 0.0.0.0:8000
