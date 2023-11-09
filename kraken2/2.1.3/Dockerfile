# Set global variables
ARG KRAKEN2_VER="2.1.3"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KRAKEN2_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.1.3"
LABEL software="Kraken 2"
LABEL software.version=${KRAKEN2_VER}
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    wget \
    curl \
    rsync \
    pigz

# Install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN2_VER}.tar.gz && \
    tar -zxvf v${KRAKEN2_VER}.tar.gz && \
    rm -rf v${KRAKEN2_VER}.tar.gz && \
    cd kraken2-${KRAKEN2_VER} && \
    ./install_kraken2.sh /usr/

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

# Copy certificates for wget
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

ENV PATH="${PATH}:/usr/:/usr/kraken2"

RUN mkdir data/
WORKDIR /data

# Verify tools are working properly
FROM app as test

RUN apt-get update && \
    apt-get install -y python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
