FROM node:17-alpine3.14
#LABEL version="1.0"
#ARG testOutputDir=test
#ENV key=value
#EXPOSE 8080
#HEALTHCHECK --interval=10m --timeout=5s CMD curl -f http://localhost/ || exit 1
#VOLUME [ "/data" ]

WORKDIR /app
#COPY package.json package-lock.json .
#RUN npm install --production
#COPY yarn.lock .
#RUN yarn install --production

#ADD /app /app
COPY /app /app

#Do not run as sudo!
#RUN groupadd -r node && useradd -g node:node 
#RUN chown -R node:node /app 
#USER node
CMD [ "node", "index.js" ]