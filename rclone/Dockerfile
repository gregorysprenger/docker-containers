ARG RCLONE_VERSION="1.70.1"

FROM ubuntu:noble AS builder
ARG RCLONE_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    ca-certificates \
    golang-go \
    wget \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN wget -q "https://github.com/rclone/rclone/releases/download/v1.70.1/rclone-v${RCLONE_VERSION}.tar.gz" \
    && tar -xzf "rclone-v${RCLONE_VERSION}.tar.gz" \
    && rm "rclone-v${RCLONE_VERSION}.tar.gz" \
    && cd "rclone-v${RCLONE_VERSION}" \
    && go build \
    && mv rclone /usr/local/bin

FROM ubuntu:noble

LABEL base.image="ubuntu:noble"
LABEL description="rclone with Ubuntu noble base image"
LABEL dockerfile.version="1.0.0"
LABEL software="rclone"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY --from=builder /usr/local/bin/rclone /usr/local/bin/rclone

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*
