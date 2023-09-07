# Set global variables
ARG SEQTK_VER="1.4"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SEQTK_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1.4"
LABEL software="Seqtk"
LABEL software.version=${SEQTK_VER}
LABEL description="Toolkit for processing sequences in FASTA/Q formats."
LABEL website="https://github.com/lh3/seqtk"
LABEL license.url="https://github.com/lh3/seqtk/blob/master/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    zlib1g-dev \
    wget \
    curl

# Install Seqtk
RUN wget https://github.com/lh3/seqtk/archive/refs/tags/v${SEQTK_VER}.tar.gz && \
    tar -xzvf v${SEQTK_VER}.tar.gz && \
    rm v${SEQTK_VER}.tar.gz && \
    cd seqtk-${SEQTK_VER} && \
    make -j$(nproc) && \
    cp seqtk /usr/local/bin

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
