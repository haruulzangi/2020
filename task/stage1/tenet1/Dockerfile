FROM node:12-alpine

WORKDIR /app/

COPY package.json /app/
COPY package-lock.json /app/

RUN npm install

COPY . /app/

ENTRYPOINT ["node", "index.js"]
