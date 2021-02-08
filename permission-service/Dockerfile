FROM golang:alpine

RUN mkdir /permission-service
WORKDIR /permission-service/permission

COPY ["/permission-service/permission", "/permission-service/permission"]

EXPOSE 8000
CMD ["go", "run", "main.go"]


