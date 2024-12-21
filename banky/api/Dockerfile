FROM golang:1.23

WORKDIR /usr/src/banky

# pre-copy/cache go.mod for pre-downloading dependencies and only redownloading them in subsequent builds if they change
COPY go.mod ./
RUN go mod download && go mod verify

COPY .. .
RUN go build -v -o /usr/local/bin/banky ./...

# Once using docker compose (or any other orchestrator), this last command needs to be removed.
# The orchestrator will start the service once other conditions are met, i.e: database is up.
#CMD ["banky"]
