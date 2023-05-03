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
LABEL dockerfile.version="1.0.0"
LABEL software="Biopython"
LABEL software.version=${BIOPYTHON_VER}
LABEL description="Biopython is a set of freely available tools for biological computation written in Python by an international team of developers."
LABEL website="https://biopython.org/"
LABEL license.url="https://github.com/biopython/biopython/blob/master/LICENSE.rst"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    libreadline-gplv2-dev \
    libncursesw5-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libssl-dev \
    libc6-dev \
    libbz2-dev \
    wget \
    curl \
    pigz

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

# Get Biopython 1.68
RUN BIOPYTHON_SHORT_VER=$(echo ${BIOPYTHON_VER} | sed 's/\.//g') && \
    wget https://github.com/biopython/biopython/archive/refs/tags/biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    -O biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    tar -zxvf biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    mv biopython-biopython-${BIOPYTHON_SHORT_VER} biopython-${BIOPYTHON_VER} && \
    cd biopython-${BIOPYTHON_VER} && \
    pip install -e . && \
    python setup.py test && \
    python setup.py install 

# Run Dockerfile
FROM ubuntu:focal as app
ARG BIOPYTHON_VER

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /biopython-${BIOPYTHON_VER}/ /biopython-${BIOPYTHON_VER}/

RUN mkdir data/
WORKDIR /data

FROM app as test

RUN apt-get update

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python -m unittest discover -v -s ../tests
