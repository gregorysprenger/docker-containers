# Set global variables
ARG GUSTLE_VER="0.2.1"
ARG GOLANG_VERSION="1.18.3"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG GUSTLE_VER
ARG GOLANG_VERSION

LABEL base.image="ubuntu:focal"
LABEL description="Performs genome wide MLST gentoyping."
LABEL docker.version="1.0.0"
LABEL license.url="https://github.com/supernifty/gustle/blob/master/LICENSE"
LABEL software.version="${GUSTLE_VER}"
LABEL software="gustle"
LABEL website="https://github.com/supernifty/gustle"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    ca-certificates \
    build-essential \
    build-essential \
    libgpgme11-dev \
    squashfs-tools \
    libseccomp-dev \
    zlib1g-dev \
    libssl-dev \
    pkg-config \
    zlib1g-dev \
    uuid-dev \
    python3 \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Golang
ENV GOLANG_SHA256_CHECKSUM="956f8507b302ab0bb747613695cdae10af99bbd39a90cae522b7c0302cc27245"

RUN wget -q "https://golang.org/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz" -O golang.tar.gz \
    && echo "${GOLANG_SHA256_CHECKSUM} golang.tar.gz" | sha256sum -c - \
    && tar -C /usr/local/ -xzf golang.tar.gz \
    && rm golang.tar.gz \
    && chmod -R 777 /usr/local/go/ \
    && ln -s /usr/local/go/bin/go /usr/local/bin/go

# Install gustle
RUN wget -q "https://github.com/chrisgulvik/gustle/archive/refs/tags/v${GUSTLE_VER}.tar.gz" \
    && tar -xzf "v${GUSTLE_VER}.tar.gz" \
    && rm "v${GUSTLE_VER}.tar.gz" \
    && cd "gustle-${GUSTLE_VER}" \
    && go build main/gustle.go \
    && mv gustle /usr/local/bin

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python3 \
    python3-pip \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install pytest

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m pytest ../tests
