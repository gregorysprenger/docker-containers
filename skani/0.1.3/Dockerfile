# Set global variables
ARG SKANI_VER="0.1.3"
ARG RUST_VER="1.70.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SKANI_VER
ARG RUST_VER

LABEL base.image="ubuntu:focal"
LABEL description="Fast, robust ANI and aligned fraction for metagenomic genomes and contigs."
LABEL dockerfile.version="0.1.3"
LABEL license.url="https://github.com/bluenote-1577/skani/blob/main/LICENSE"
LABEL software.version=${SKANI_VER}
LABEL software="skani"
LABEL website="https://github.com/bluenote-1577/skani"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    curl \
    wget

# Install Rust
RUN wget https://static.rust-lang.org/dist/rust-${RUST_VER}-x86_64-unknown-linux-gnu.tar.gz \
    && tar -zxf rust-${RUST_VER}-x86_64-unknown-linux-gnu.tar.gz \
    && rm rust-${RUST_VER}-x86_64-unknown-linux-gnu.tar.gz \
    && mv rust-${RUST_VER}-x86_64-unknown-linux-gnu rust-${RUST_VER} \
    && cd rust-${RUST_VER} \
    && ./install.sh

# Install skani
RUN wget https://github.com/bluenote-1577/skani/archive/refs/tags/v${SKANI_VER}.tar.gz \
    && tar -zxf v${SKANI_VER}.tar.gz \
    && rm v${SKANI_VER}.tar.gz \
    && cd skani-${SKANI_VER} \
    && cargo install --path . --root /usr/local/bin/

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM builder as test

RUN apt-get update && apt-get install -y python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
