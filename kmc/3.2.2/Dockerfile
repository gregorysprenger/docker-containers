# Set global variables
ARG KMC_VER="3.2.2"
ARG ZLIB_VER="1.3"
ARG PYTHON_VER="3.9.6"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG KMC_VER
ARG ZLIB_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL description="Fast and frugal disk based k-mer counter."
LABEL dockerfile.version="3.2.2"
LABEL license.url="https://github.com/refresh-bio/KMC#license"
LABEL software.version=${KMC_VER}
LABEL software="KMC"
LABEL website="https://github.com/refresh-bio/KMC"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    libncurses5-dev \
    libreadline-dev \
    libgdbm-dev \
    libnss3-dev \
    zlib1g-dev \
    libssl-dev \
    libffi-dev \
    wget \
    curl

# Install Python 3
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz \
    && tar -zxf Python-${PYTHON_VER}.tgz \
    && rm Python-${PYTHON_VER}.tgz \
    && cd Python-${PYTHON_VER} \
    && ./configure \
    && make -j$(nproc) \
    && make install

# Install KMC
RUN wget https://github.com/refresh-bio/KMC/archive/refs/tags/v${KMC_VER}.tar.gz \
    && tar -xzf v${KMC_VER}.tar.gz \
    && rm v${KMC_VER}.tar.gz \
    && cd KMC-${KMC_VER}/3rd_party/cloudflare \
    && wget https://zlib.net/zlib-${ZLIB_VER}.tar.gz \
    && tar -xzf zlib-${ZLIB_VER}.tar.gz --strip-components=1 \
    && rm zlib-${ZLIB_VER}.tar.gz \
    && cd /KMC-${KMC_VER} \
    && make -j$(nproc) \
    && cp bin/kmc /usr/local/bin \
    && cp bin/kmc_dump /usr/local/bin \
    && cp bin/kmc_tools /usr/local/bin

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
