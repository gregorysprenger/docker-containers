# Set global variables
ARG KRAKEN_VER="1.1.1"
ARG JELLYFISH_VER="1.1.12"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KRAKEN_VER
ARG JELLYFISH_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version=${KRAKEN_VER}
LABEL software="Kraken"
LABEL software.version=${KRAKEN_VER}
LABEL description="Taxonomic sequence classifier"
LABEL website="https://github.com/DerrickWood/kraken"
LABEL license="https://github.com/DerrickWood/kraken/blob/master/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    ca-certificates \
    cpanminus \
    wget \
    curl \
    rsync \
    pigz

# Install Jellyfish
RUN wget https://github.com/gmarcais/Jellyfish/releases/download/v${JELLYFISH_VER}/jellyfish-${JELLYFISH_VER}.tar.gz && \
    tar -xzvf jellyfish-${JELLYFISH_VER}.tar.gz && \
    cd jellyfish-${JELLYFISH_VER} && \
    ./configure --prefix=/usr/ && \
    NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l) && \
    make -j ${NUM_CPUS} && \
    make install

# Install Kraken
RUN wget https://github.com/DerrickWood/kraken/archive/refs/tags/v${KRAKEN_VER}.tar.gz && \
    tar -xzvf v${KRAKEN_VER}.tar.gz && \
    cd kraken-${KRAKEN_VER} && \
    ./install_kraken.sh /usr/ && \
    cpanm Getopt::Std

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

# Copy certificates for wget
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

ENV PATH="${PATH}:/usr/:/usr/kraken"

RUN mkdir data/
WORKDIR /data

# Verify tools are working properly
FROM app as test

RUN apt-get update && \
    apt-get install -y python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
