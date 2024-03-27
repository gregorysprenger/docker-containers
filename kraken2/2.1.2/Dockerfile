# Set global variables
ARG KRAKEN2_VER="2.1.2"
ARG MINIKRAKEN2_VER="20230314"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KRAKEN2_VER
ARG MINIKRAKEN2_VER

LABEL base.image="ubuntu:focal"
LABEL description="Taxonomic sequence classifier"
LABEL dockerfile.version="1.0.0"
LABEL license="https://github.com/DerrickWood/kraken2/blob/master/LICENSE"
LABEL software.version=${KRAKEN2_VER}
LABEL software="Kraken 2"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    rsync \
    wget \
    curl \
    pigz

# Install Kraken2
RUN wget https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN2_VER}.tar.gz \
    && tar -zxf v${KRAKEN2_VER}.tar.gz \
    && rm v${KRAKEN2_VER}.tar.gz \
    && cd kraken2-${KRAKEN2_VER} \
    && ./install_kraken2.sh /usr/local/bin/

# Download Kraken2 MiniKraken
RUN wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_08gb_${MINIKRAKEN2_VER}.tar.gz \
    && mkdir /kraken2-database \
    && tar -xzf k2_standard_08gb_${MINIKRAKEN2_VER}.tar.gz \
      -C /kraken2-database \
    && rm k2_standard_08gb_${MINIKRAKEN2_VER}

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /kraken2-database/ /kraken2-database/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN apt-get update && apt-get install -y python3 wget

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
