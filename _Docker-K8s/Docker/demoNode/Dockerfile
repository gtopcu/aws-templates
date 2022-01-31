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

#Set hosts file
#RUN echo "127.0.0.1 localhost" >> /etc/hosts
#RUN cat /etc/hosts

#Set SSH access
#COPY ./ssh/id_rsa /root/.ssh/id_rsa
#RUN ssh-keyscan bitbucket.org > /root/.ssh/known_hosts
#RUN chmod 600 /root/.ssh/id_rsa

#Use docker image caching, complete rebuild only when package.json is changed
#ADD /app /app
COPY /app /app

#Do not run as sudo!
#RUN groupadd -r node && useradd -g node:node 
#RUN chown -R node:node /app 
#USER node
CMD [ "node", "index.js" ]