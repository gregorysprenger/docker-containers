# Set global variables
ARG PYTHON_VER="2.7.18"
ARG BIOPYTHON_VER="1.68"
ARG BLASTPLUS_VER="2.9.0"
ARG NUMPY_VER="1.16.6"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG PYTHON_VER
ARG BIOPYTHON_VER
ARG BLASTPLUS_VER
ARG NUMPY_VER

LABEL base.image="ubuntu:focal"
LABEL description="Combination of Blast+, Python, and Biopython"
LABEL dockerfile.version="1.0.0"
LABEL software.version="1.0.0"
LABEL software="Blast+, Python2, Biopython"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    build-essential \
    ca-certificates \
    libsqlite3-dev \
    libjson-perl \
    libgdbm-dev \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libc6-dev \
    tk-dev \
    wget \
    curl \
    perl \
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
    && tar -zxvf biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    && rm biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    && mv biopython-biopython-${BIOPYTHON_SHORT_VER} biopython-${BIOPYTHON_VER} \
    && cd biopython-${BIOPYTHON_VER} \
    && pip install --no-cache-dir -e . \
    && python setup.py install

# Install NCBI Blast+
RUN wget -q https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && tar xvf ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && rm ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && mv ncbi-blast-${BLASTPLUS_VER}+/bin/* /usr/local/bin/

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/

RUN apt-get install ca-certificates

RUN mkdir data/
WORKDIR /data

# Run tests
FROM app as test

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests
