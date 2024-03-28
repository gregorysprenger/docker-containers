# Set global variables
ARG FASTANI_VER="1.33"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG FASTANI_VER

LABEL base.image="ubuntu:focal"
LABEL description="Fast Whole-Genome Similarity (ANI) Estimation."
LABEL dockerfile.version="1.33"
LABEL license.url="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL software.version="${FASTANI_VER}"
LABEL software="fastANI"
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    build-essential \
    ca-certificates \
    zlib1g-dev \
    libgsl-dev \
    autoconf \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install fastANI
RUN wget -q "https://github.com/ParBLiSS/FastANI/archive/refs/tags/v${FASTANI_VER}.tar.gz" \
    && tar -xzf "v${FASTANI_VER}.tar.gz" \
    && rm "v${FASTANI_VER}.tar.gz" \
    && cd "FastANI-${FASTANI_VER}" \
    && ./bootstrap.sh \
    && ./configure \
    && make \
    && make install

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM builder as test

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python3 \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
