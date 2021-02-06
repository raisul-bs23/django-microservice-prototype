FROM node:14
RUN mkdir /node-service
WORKDIR /node-service/help-app

COPY ["/node-service/help-app", "/node-service/help-app"]

USER node

RUN npm install
EXPOSE 8000

CMD [ "node", "server.js" ]