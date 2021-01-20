# Stage 1
FROM node:latest as stage-1
WORKDIR /usr/src/app
RUN npm install
RUN touch test
RUN echo "test data" >> test

# Stage 2 - the production environment
FROM nginx:1.17.1-alpine
COPY --from=stage-1 /usr/src/app/test /usr/share/nginx/html

