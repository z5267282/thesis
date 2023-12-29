FROM node:16

WORKDIR /frontend

COPY package*.json ./

RUN npm install

COPY public/ ./
COPY src/ ./
COPY start.js ./

ENV FE_PORT=3000

EXPOSE 3000 

CMD [ "npm", "start" ]
