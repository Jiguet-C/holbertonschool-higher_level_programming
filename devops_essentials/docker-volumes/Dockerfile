FROM alpine
RUN apk add --no-cache curl
COPY config.txt /app/config.txt
VOLUME /data
CMD sh -c "echo 'Hello, Docker Volumes!' > /data/hello.txt && cat /data/hello.txt"
