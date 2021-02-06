FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Export application port
EXPOSE 8000

FROM base AS build

RUN mkdir /product-service
WORKDIR /product-service/product

# Copy source code & libraries
COPY ["/product-service/product", "/product-service/product"]

# Copy dependencies file to container working directory
COPY ["./product-service/requirements.txt", "/product-service/product"]

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG COLLECT_STATIC
RUN mkdir /product-service/api-static
RUN python manage.py collectstatic --no-input
CMD python manage.py runserver 0.0.0.0:8000
