FROM openjdk:17-jdk-slim

LABEL maintainer="prasannapujitha03@gmail.com"

WORKDIR /app

COPY target/hello-pujitha-1.0.0.jar hello-pujitha-1.0.0.jar

EXPOSE 8080

ENTRYPOINT [ "java", "-jar", "hello-pujitha-1.0.0.jar" ]
