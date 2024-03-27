# Set global variables
ARG PYTHON_VER="2.7.18"
ARG BIOPYTHON_VER="1.68"
ARG DIAMOND_VER="2.0.13"
ARG NUMPY_VER="1.16.6"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG PYTHON_VER
ARG BIOPYTHON_VER
ARG DIAMOND_VER
ARG NUMPY_VER

LABEL base.image="ubuntu:focal"
LABEL description="Combination of Diamond, Python 2.7, and Biopython 1.68"
LABEL dockerfile.version="1.0.0"
LABEL software.version="1.0.0"
LABEL software="Diamond, Python2, Biopython"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    libreadline-gplv2-dev \
    libpthread-stubs0-dev \
    libncursesw5-dev \
    build-essential \
    ca-certificates \
    libsqlite3-dev \
    libgdbm-dev \
    libssl-dev \
    libbz2-dev \
    zlib1g-dev \
    libc6-dev \
    tk-dev \
    cmake \
    wget \
    curl \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install Python 2.7
RUN wget -q https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz \
    && tar -zxf Python-${PYTHON_VER}.tgz \
    && rm Python-${PYTHON_VER}.tgz \
    && cd Python-${PYTHON_VER} \
    && ./configure \
    && make \
    && make install

# Install pip and numpy
RUN wget -q https://bootstrap.pypa.io/pip/2.7/get-pip.py \
    && python get-pip.py \
    && pip install --no-cache-dir numpy==${NUMPY_VER}

# Install Biopython 
RUN BIOPYTHON_SHORT_VER="$(echo ${BIOPYTHON_VER} | sed 's/\.//g')" \
    && wget -q https://github.com/biopython/biopython/archive/refs/tags/biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
      -O biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    && tar -zxf biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    && mv biopython-biopython-${BIOPYTHON_SHORT_VER} biopython-${BIOPYTHON_VER} \
    && cd biopython-${BIOPYTHON_VER} \
    && pip install --no-cache-dir -e . \
    && python setup.py install

# Install Diamond
RUN wget -q http://github.com/bbuchfink/diamond/archive/v${DIAMOND_VER}.tar.gz \
    && tar -xzf v${DIAMOND_VER}.tar.gz \
    && rm v${DIAMOND_VER}.tar.gz \
    && cd diamond-${DIAMOND_VER} \
    && cmake . \
    && make -j $(nproc) \
    && make install

# Run Dockerfile
FROM ubuntu:focal as app
ARG BIOPYTHON_VER

COPY --from=builder /usr/local/ /usr/local/

RUN update-ca-certificates

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    python3 \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
