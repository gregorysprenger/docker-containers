# Set global variables
ARG SKESA_VER="2.4.0"
ARG BOOST_VER="1.72.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SKESA_VER
ARG BOOST_VER

LABEL base.image="ubuntu:focal"
LABEL description="Strategic Kmer Extension for Scrupulous Assemblies"
LABEL dockerfile.version="1.0.0"
LABEL lisence="https://github.com/ncbi/SKESA/blob/master/LICENSE"
LABEL software.version="${SKESA_VER}"
LABEL software="SKESA"
LABEL website="https://github.com/ncbi/SKESA"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    build-essential \
    ca-certificates \
    autotools-dev \
    python3-dev \
    libbz2-dev \
    libicu-dev \
    cmake \
    wget \
    pigz \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install BOOST
RUN BOOST_REFORMAT_VER="${BOOST_VER//\./_}" \
    && wget -q "https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VER}/source/boost_${BOOST_REFORMAT_VER}.tar.gz" \
    && tar -xzf "boost_${BOOST_REFORMAT_VER}.tar.gz" \
    && rm "boost_${BOOST_REFORMAT_VER}.tar.gz" \
    && cd "boost_${BOOST_REFORMAT_VER}" \
    && ./bootstrap.sh --prefix=/usr/ \
    && ./b2 -j "$(nproc)" threading=multi \
    && ./b2 install -j "$(nproc)" threading=multi

# Install SKESA
RUN wget -q "https://github.com/ncbi/SKESA/archive/refs/tags/${SKESA_VER}.tar.gz" \
    && tar -xzf "${SKESA_VER}.tar.gz" \
    && rm "${SKESA_VER}.tar.gz" \
    && cd "SKESA-${SKESA_VER}" \
    && make -f Makefile.nongs \
    && mv skesa /usr/local/bin

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
    && rm -rf /var/lib/apt/lists/*

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
