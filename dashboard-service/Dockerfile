FROM python:3.8 AS base
# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Export application port
EXPOSE 8000

FROM base AS build

RUN mkdir /dashboard-service
WORKDIR /dashboard-service/dashboard

# Copy source code & libraries
COPY ["/dashboard-service/dashboard", "/dashboard-service/dashboard"]

# Copy dependencies file to container working directory
COPY ["./dashboard-service/requirements.txt", "/dashboard-service/dashboard"]

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ARG COLLECT_STATIC
RUN mkdir /dashboard-service/api-static
RUN python manage.py collectstatic --no-input
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000
