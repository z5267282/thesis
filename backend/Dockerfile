FROM python:3.13-alpine
WORKDIR /app
COPY . /app
EXPOSE 5005
RUN ["./setup"]
ENTRYPOINT ["./start"]
