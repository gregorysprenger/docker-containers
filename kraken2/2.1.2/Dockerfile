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
LABEL software.version="${KRAKEN2_VER}"
LABEL software="Kraken 2"
LABEL website="https://github.com/DerrickWood/kraken2"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    ca-certificates \
    build-essential \
    zlib1g-dev \
    rsync \
    wget \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install Kraken2
RUN wget -q "https://github.com/DerrickWood/kraken2/archive/refs/tags/v${KRAKEN2_VER}.tar.gz" \
    && tar -zxf "v${KRAKEN2_VER}.tar.gz" \
    && rm "v${KRAKEN2_VER}.tar.gz" \
    && cd "kraken2-${KRAKEN2_VER}" \
    && ./install_kraken2.sh /usr/local/bin/

# Download Kraken2 MiniKraken
RUN wget -q "https://genome-idx.s3.amazonaws.com/kraken/k2_standard_08gb_${MINIKRAKEN2_VER}.tar.gz" \
    && mkdir /kraken2-database \
    && tar -xzf "k2_standard_08gb_${MINIKRAKEN2_VER}.tar.gz" \
      -C /kraken2-database \
    && rm "k2_standard_08gb_${MINIKRAKEN2_VER}.tar.gz"

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/
COPY --from=builder /kraken2-database/ /kraken2-database/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python3 \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
