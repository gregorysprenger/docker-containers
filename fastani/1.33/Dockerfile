# Set global variables
ARG FASTANI_VER="1.33"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG FASTANI_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1.33"
LABEL software="fastANI"
LABEL software.version=${FASTANI_VER}
LABEL description="Fast Whole-Genome Similarity (ANI) Estimation."
LABEL website="https://github.com/ParBLiSS/FastANI"
LABEL license.url="https://github.com/ParBLiSS/FastANI/blob/master/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    zlib1g-dev \
    libgsl-dev \
    autoconf \
    curl \
    wget

# Install fastANI
RUN wget https://github.com/ParBLiSS/FastANI/archive/refs/tags/v${FASTANI_VER}.tar.gz && \
    tar -xzvf v${FASTANI_VER}.tar.gz && \
    cd FastANI-${FASTANI_VER} && \
    ./bootstrap.sh && \
    ./configure && \
    make && \
    make install

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

FROM builder as test

RUN apt-get update && \
    apt-get install -y python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests