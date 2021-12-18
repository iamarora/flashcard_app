FROM node:16.11
USER root

# Install global NPM dependencies in non-root user directory
# https://github.com/nodejs/docker-node/blob/main/docs/BestPractices.md#global-npm-dependencies
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global
ENV PATH=$PATH:/home/node/.npm-global/bin
RUN npm config set unsafe-perm true

WORKDIR /frontend