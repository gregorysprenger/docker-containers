# Set global variables
ARG PYTHON_VER="2.7.18"
ARG BIOPYTHON_VER="1.68"
ARG NUMPY_VER="1.16.6"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG PYTHON_VER
ARG BIOPYTHON_VER
ARG NUMPY_VER

LABEL base.image="ubuntu:focal"
LABEL description="Biopython is a set of freely available tools for biological computation written in Python by an international team of developers."
LABEL dockerfile.version="1.0.0"
LABEL license.url="https://github.com/biopython/biopython/blob/master/LICENSE.rst"
LABEL software.version=${BIOPYTHON_VER}
LABEL software="Biopython"
LABEL website="https://biopython.org/"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install dependencies
RUN apt-get update \
   && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    ca-certificates \
    build-essential \
    libsqlite3-dev \
    libgdbm-dev \
    zlib1g-dev \
    libbz2-dev \
    libssl-dev \
    libc6-dev \
    pigz \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python 2.7
RUN wget -q "https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz" \
    && tar -xzf "Python-${PYTHON_VER}.tgz" \
    && rm "Python-${PYTHON_VER}.tgz" \
    && cd "Python-${PYTHON_VER}" \
    && ./configure \
    && make \
    && make install

# Install pip and numpy
RUN wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py \
    && python get-pip.py \
    && pip install --no-cache-dir numpy=="${NUMPY_VER}"

# Install  Biopython
RUN BIOPYTHON_SHORT_VER="${BIOPYTHON_VER//\./}" \
    && wget -q "https://github.com/biopython/biopython/archive/refs/tags/biopython-${BIOPYTHON_SHORT_VER}.tar.gz" \
    && tar -xzf "biopython-${BIOPYTHON_SHORT_VER}.tar.gz" \
    && rm "biopython-${BIOPYTHON_SHORT_VER}.tar.gz" \
    && cd "biopython-biopython-${BIOPYTHON_SHORT_VER}" \
    && pip install --no-cache-dir -e . \
    && python setup.py install

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests
