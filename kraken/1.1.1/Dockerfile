# Set global variables
ARG KRAKEN_VER="1.1.1"
ARG JELLYFISH_VER="1.1.12"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KRAKEN_VER
ARG JELLYFISH_VER

LABEL base.image="ubuntu:focal"
LABEL description="Taxonomic sequence classifier"
LABEL dockerfile.version="${KRAKEN_VER}"
LABEL license="https://github.com/DerrickWood/kraken/blob/master/LICENSE"
LABEL software.version="${KRAKEN_VER}"
LABEL software="Kraken"
LABEL website="https://github.com/DerrickWood/kraken"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    build-essential \
    ca-certificates \
    cpanminus \
    rsync \
    wget \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install Jellyfish
RUN wget -q "https://github.com/gmarcais/Jellyfish/releases/download/v${JELLYFISH_VER}/jellyfish-${JELLYFISH_VER}.tar.gz" \
    && tar -xzf "jellyfish-${JELLYFISH_VER}.tar.gz" \
    && rm "jellyfish-${JELLYFISH_VER}.tar.gz" \
    && cd "jellyfish-${JELLYFISH_VER}" \
    && ./configure --prefix=/usr/ \
    && make -j "$(nproc)" \
    && make install

# Install Kraken
RUN wget -q "https://github.com/DerrickWood/kraken/archive/refs/tags/v${KRAKEN_VER}.tar.gz" \
    && tar -xzf "v${KRAKEN_VER}.tar.gz" \
    && rm "v${KRAKEN_VER}.tar.gz" \
    && cd "kraken-${KRAKEN_VER}" \
    && ./install_kraken.sh /usr/local/bin/ \
    && cpanm Getopt::Std

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
# FROM app as test

# RUN apt-get update \
#     && apt-get install --no-install-recommends -y \
#     python3 \
#     && rm -rf /var/lib/apt/lists/*

# RUN mkdir ../tests/
# COPY tests/ ../tests/
# RUN python3 -m unittest discover -v -s ../tests
