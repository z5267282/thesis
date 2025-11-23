FROM python:3.13-alpine
WORKDIR /backend
COPY . /backend
ENV IN_DOCKER=yes
EXPOSE 5005
# need ps with -p flag - default busybox binary does not have -p
RUN apk --no-cache add procps
RUN ./setup
ENTRYPOINT ["./start"]
