# Global ARG variables
ARG GUSTLE_VER="0.2.1"
ARG GO_VERSION="1.18.3"

# Build container
FROM ubuntu:focal as builder

ARG GUSTLE_VER
ARG GO_VERSION

ENV DEBIAN_FRONTEND noninteractive

LABEL base.image="ubuntu:focal"
LABEL software="gustle"
LABEL software.version=${GUSTLE_VER}
LABEL description="Performs genome wide MLST gentoyping."
LABEL website="https://github.com/supernifty/gustle"
LABEL license.url="https://github.com/supernifty/gustle/blob/master/LICENSE"

# Update and install packages
RUN apt-get update -y && apt-get install -y \
    curl \
    wget \
    zlib1g-dev \
    python3 \
    ca-certificates \
    build-essential \
    libssl-dev \
    uuid-dev \
    libgpgme11-dev \
    squashfs-tools \
    libseccomp-dev \
    pkg-config \
    build-essential \
    zlib1g-dev \
    python3

# Install Go 
# from https://github.com/shenwei356/seqkit/blob/master/Dockerfile
ENV GOLANG_VERSION ${GO_VERSION}
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_SHA256_CHECKSUM 956f8507b302ab0bb747613695cdae10af99bbd39a90cae522b7c0302cc27245
ENV GOPATH $HOME/go
ENV PATH $PATH:/usr/local/go/bin:$GOPATH/bin
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz && \
    echo "$GOLANG_SHA256_CHECKSUM golang.tar.gz" | sha256sum -c - && \
    tar -C /usr/local -xzf golang.tar.gz && \
    rm -r golang.tar.gz && \
    mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"


# Get gustle
# Waiting on newest release from supernifty 
RUN wget https://github.com/chrisgulvik/gustle/archive/refs/tags/v${GUSTLE_VER}.tar.gz && \
    tar -xzf v${GUSTLE_VER}.tar.gz && \
    rm -r v${GUSTLE_VER}.tar.gz && \
    cd gustle-${GUSTLE_VER} && \
    go build main/gustle.go 

ENV PATH="/gustle-${GUSTLE_VER}:$PATH"

# Create app image
FROM ubuntu:focal as app

ARG GUSTLE_VER

# Copy packages from build image
COPY --from=builder /gustle-${GUSTLE_VER}/ /gustle-${GUSTLE_VER}/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/local/go/ /go/
COPY --from=builder /usr/ /usr/

# Put gustle and Go in PATH
ENV PATH="/gustle-${GUSTLE_VER}/:$PATH"
ENV PATH="/go:$PATH"

RUN mkdir data/
WORKDIR data

# Create test image
FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget \
    curl

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests