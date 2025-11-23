# all node official images after 22 seem to have security vulnerabilities
FROM node:24.11-slim
WORKDIR /frontend
COPY . /frontend
RUN npm install
EXPOSE 3000
# can't use nvm without installing it, so we just leave it on v24.11 from the base image
CMD ["npm", "run", "start"]
