# Set global variables
ARG SPADES_VER="3.13.0"
ARG PYTHON_VER="2.7.18"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SPADES_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1.0.0"
LABEL software="SPAdes"
LABEL software.version=${SPADES_VER}
LABEL description="de novo DBG genome assembler"
LABEL website="https://github.com/ablab/spades"
LABEL license="https://github.com/ablab/spades/blob/v3.15.3/assembler/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    ca-certificates \
    zlib1g-dev \
    libbz2-dev \
    cmake \
    wget \
    curl \
    pigz  

# Install Python
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz && \
    tar -zxvf Python-${PYTHON_VER}.tgz && \
    cd Python-${PYTHON_VER} && \
    ./configure && \
    make && make install

# Install SPAdes
RUN wget https://github.com/ablab/spades/archive/refs/tags/v${SPADES_VER}.tar.gz && \
    tar -xzvf v${SPADES_VER}.tar.gz && \
    cd spades-${SPADES_VER} && \
    PREFIX=/usr/local/ ./assembler/spades_compile.sh

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

# Verify SPAdes is working correctly
FROM app as test

RUN apt-get update

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests