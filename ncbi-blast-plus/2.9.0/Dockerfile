# Set global variables
ARG BLASTPLUS_VER="2.9.0"
ARG PYTHON_VER="3.8.15"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG BLASTPLUS_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="1.0.0"
LABEL software="BLAST+"
LABEL software.version=${BLASTPLUS_VER}
LABEL description="BLAST+: A suite of command-line tools to run BLAST (Basic Local Alignment Search Tool)."
LABEL website="https://www.ncbi.nlm.nih.gov/books/NBK279690/"
LABEL license.url="https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/lxr/source/scripts/projects/blast/LICENSE"

ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    libjson-perl \
    perl \
    wget \
    gcc \
    build-essential \
    libreadline-dev \
    libncursesw5-dev \
    libssl-dev \
    libsqlite3-dev \
    tk-dev \
    libgdbm-dev \
    libc6-dev \
    libbz2-dev

# Install BLAST+
RUN wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && tar xvf ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && rm ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz \
    && mv ncbi-blast-${BLASTPLUS_VER}+/bin/* /usr/local/bin/

# Install Python3
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz && \
    tar -zxvf Python-${PYTHON_VER}.tgz && \
    cd Python-${PYTHON_VER} && \
    ./configure && \
    make && make install

RUN mkdir -p /db && cd /db && \
    update_blastdb.pl 16S_ribosomal_RNA
    
# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /db/ /db/

RUN mkdir /data/
WORKDIR /data

# Run minimum tests
FROM app as test

RUN apt-get update

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests