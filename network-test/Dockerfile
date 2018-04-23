FROM alpine:3.6
RUN apk --update add docker
ENTRYPOINT ["docker", "run", "--network=docker-network-test", "curl-test"]