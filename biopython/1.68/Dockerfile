# Set global variables
ARG BIOPYTHON_VER="1.68"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG BIOPYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1"
LABEL software="Biopython"
LABEL software.version=${BIOPYTHON_VER}
LABEL description="Biopython is a set of freely available tools for biological computation written in Python by an international team of developers."
LABEL website="https://biopython.org/"
LABEL license.url="https://github.com/biopython/biopython/blob/master/LICENSE.rst"

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    python \
    python-dev \
    gcc

# Install pip for Python 2.7 and get numpy
RUN wget https://bootstrap.pypa.io/pip/2.7/get-pip.py && \
    python get-pip.py && \
    pip install numpy

# Get Biopython 1.6.8
RUN BIOPYTHON_SHORT_VER=$(echo ${BIOPYTHON_VER} | sed 's/\.//g') && \
    wget https://github.com/biopython/biopython/archive/refs/tags/biopython-${BIOPYTHON_SHORT_VER}.tar.gz \
    -O biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    tar -zxvf biopython-${BIOPYTHON_SHORT_VER}.tar.gz && \
    mv biopython-biopython-${BIOPYTHON_SHORT_VER} biopython-${BIOPYTHON_SHORT_VER} && \
    cd biopython-${BIOPYTHON_SHORT_VER} && \
    pip install -e . && \
    python setup.py test && \
    python setup.py install 

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

FROM app as test

RUN apt-get update && apt-get install -y \
    python \
    wget

RUN python --version
