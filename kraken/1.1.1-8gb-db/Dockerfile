# Set global variables
ARG KRAKEN_VER="1.1.1"
ARG JELLYFISH_VER="1.1.12"
ARG MINIKRAKEN_VER="20171019"
ARG MINIKRAKEN_SIZE="8GB"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KRAKEN_VER
ARG JELLYFISH_VER
ARG MINIKRAKEN_VER
ARG MINIKRAKEN_SIZE

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1.0.0"
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

# Download and configure 4gb database
RUN wget http://ccb.jhu.edu/software/kraken/dl/minikraken_${MINIKRAKEN_VER}_${MINIKRAKEN_SIZE}.tgz && \
    mkdir /kraken-database && \
    tar -xzvf minikraken_${MINIKRAKEN_VER}_${MINIKRAKEN_SIZE}.tgz \
    -C /kraken-database --strip-components 1 && \
    rm -rf minikraken_${MINIKRAKEN_VER}_${MINIKRAKEN_SIZE}.tgz

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /kraken-database/ /kraken-database/

ENV PATH="${PATH}:/usr/:/usr/kraken"

RUN mkdir data/
WORKDIR /data

# Make sure Kraken is working properly
FROM app as test

RUN apt-get update && apt-get install -y wget python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests