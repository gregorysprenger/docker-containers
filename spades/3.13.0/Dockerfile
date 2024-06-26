# Set global variables
ARG SPADES_VER="3.13.0"
ARG PYTHON_VER="2.7.18"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SPADES_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL description="de novo DBG genome assembler"
LABEL dockerfile.version="1.0.0"
LABEL license="https://github.com/ablab/spades/blob/v3.15.3/assembler/LICENSE"
LABEL software.version="${SPADES_VER}"
LABEL software="SPAdes"
LABEL website="https://github.com/ablab/spades"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    build-essential \
    ca-certificates \
    zlib1g-dev \
    libbz2-dev \
    cmake \
    wget \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install Python
RUN wget -q "https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz" \
    && tar -xzf "Python-${PYTHON_VER}.tgz" \
    && rm "Python-${PYTHON_VER}.tgz" \
    && cd "Python-${PYTHON_VER}" \
    && ./configure \
    && make \
    && make install

# Install SPAdes
RUN wget -q "https://github.com/ablab/spades/archive/refs/tags/v${SPADES_VER}.tar.gz" \
    && tar -xzf "v${SPADES_VER}.tar.gz" \
    && rm "v${SPADES_VER}.tar.gz" \
    && cd "spades-${SPADES_VER}" \
    && PREFIX=/usr/local/ ./assembler/spades_compile.sh

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests
