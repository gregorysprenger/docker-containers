# Set global variables
ARG SKESA_VER="2.4.0"
ARG BOOST_VER="1.72.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG SKESA_VER
ARG BOOST_VER

LABEL base.image="ubuntu:jammy"
LABEL dockerfile.version="1.0.0"
LABEL software="SKESA"
LABEL software.version=${SKESA_VER}
LABEL description="Strategic Kmer Extension for Scrupulous Assemblies"
LABEL website="https://github.com/ncbi/SKESA"
LABEL lisence="https://github.com/ncbi/SKESA/blob/master/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    wget \
    curl \
    cmake \
    git \
    pigz \
    libicu-dev \
    libbz2-dev \
    python3-dev \
    autotools-dev \
    build-essential

# Install BOOST
RUN BOOST_REFORMAT_VER=$(echo ${BOOST_VER} | sed 's/\./_/g') && \
    wget https://boostorg.jfrog.io/artifactory/main/release/${BOOST_VER}/source/boost_${BOOST_REFORMAT_VER}.tar.gz && \
    tar -zxvf boost_${BOOST_REFORMAT_VER}.tar.gz && \
    mv boost_${BOOST_REFORMAT_VER} boost_${BOOST_VER} && \
    cd boost_${BOOST_VER} && \
    ./bootstrap.sh --prefix=/usr/ && \
    NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l) && \
    ./b2 -j ${NUM_CPUS} threading=multi && \
    ./b2 install -j ${NUM_CPUS} threading=multi

# Install SKESA
RUN wget https://github.com/ncbi/SKESA/archive/refs/tags/${SKESA_VER}.tar.gz && \
    tar -zxvf ${SKESA_VER}.tar.gz && \
    cd SKESA-${SKESA_VER} && \
    make -f Makefile.nongs

# Run Dockerfile
FROM ubuntu:focal as app
ARG SKESA_VER
ARG BOOST_VER

COPY --from=builder /usr/ /usr/
COPY --from=builder /SKESA-${SKESA_VER}/ /SKESA-${SKESA_VER}/

ENV PATH="${PATH}:/SKESA-${SKESA_VER}/"

RUN mkdir data/
WORKDIR /data

# Make sure skesa is working properly
FROM app as test

RUN apt-get update && apt-get install -y wget python3

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests