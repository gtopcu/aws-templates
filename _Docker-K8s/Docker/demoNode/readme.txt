
docker --version
docker pull node:17-alpine3.14

docker build -t node-demo .
docker tag node-demo node-demo:latest
docker run -d -p 8080:8080 node-demo