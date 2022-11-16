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
LABEL dockerfile.version="1.0.0"
LABEL software="Blast+, Python2, Biopython"
LABEL software.version="1.0.0"
LABEL description="Combination of Blast+, Python 2.7, and Biopython 1.68"

ENV DEBIAN_FRONTEND=noninteractive 

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gcc \
    build-essential \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev \
    libjson-perl \
    perl 

# Install Python 2.7
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz && \
    tar -zxvf Python-${PYTHON_VER}.tgz && \
    cd Python-${PYTHON_VER} && \
    ./configure && \
    make && make install

# Install pip for Python 2.7 and get numpy
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && \
    python get-pip.py && \
    pip install numpy==${NUMPY_VER}

# Install Biopython 1.6.8
RUN BIOPYTHON_SHORT_VER=$(echo ${BIOPYTHON_VER} | sed 's/\.//g') && \
    wget https://github.com/biopython/biopython/archive/refs/tags/biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    -O biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    tar -zxvf biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    mv biopython-biopython-${BIOPYTHON_SHORT_VER} biopython-${BIOPYTHON_VER} && \
    cd biopython-${BIOPYTHON_VER} && \
    pip install -e . && \
    python setup.py install 

# Install NCBI Blast+
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && tar xvf ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && rm ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && mv ncbi-blast-${BLASTPLUS_VER}+/bin/* /usr/local/bin/

# Run Dockerfile
FROM ubuntu:focal as app
ARG BIOPYTHON_VER

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /biopython-${BIOPYTHON_VER}/ /biopython-${BIOPYTHON_VER}/

RUN mkdir data/
WORKDIR /data

FROM app as test

RUN apt-get update && apt-get install -y wget

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests
