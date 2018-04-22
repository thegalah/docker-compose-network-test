FROM node:alpine
RUN apk add --update yarn
RUN yarn add express
COPY . /app
WORKDIR app
ENTRYPOINT ["node", "api.js"]