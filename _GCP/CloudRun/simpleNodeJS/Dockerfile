# Use the official lightweight Node.js 12 image.
# https://hub.docker.com/_/node

# gcloud auth login
# gcloud services enable cloudbuild.googleapis.com
# gcloud services enable run.googleapis.com
# gcloud config set compute/region "us-east1"
# gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/helloworld
# docker run -d -p 8080:8080 gcr.io/$GOOGLE_CLOUD_PROJECT/helloworld
# web preview / curl localhost:8080
# gcloud run deploy --image gcr.io/$GOOGLE_CLOUD_PROJECT/helloworld --allow-unauthenticated --region=$LOCATION
# gcloud container images delete gcr.io/$GOOGLE_CLOUD_PROJECT/helloworld
# gcloud run services delete helloworld --region="REGION"

FROM node:12-slim

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy application dependency manifests to the container image.
# A wildcard is used to ensure copying both package.json AND package-lock.json (when available).
# Copying this first prevents re-running npm install on every code change.
COPY package*.json ./

# Install production dependencies.
# If you add a package-lock.json, speed your build by switching to 'npm ci'.
# RUN npm ci --only=production
RUN npm install --only=production

# Copy local code to the container image.
COPY . ./

# Run the web service on container startup.
CMD [ "npm", "start" ]