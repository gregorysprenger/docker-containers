# Set global variables
ARG BLASTPLUS_VER="2.9.0"
ARG PYTHON_VER="3.8.15"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG BLASTPLUS_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL description="BLAST+: A suite of command-line tools to run BLAST (Basic Local Alignment Search Tool)."
LABEL dockerfile.version="1.0.0"
LABEL license.url="https://www.ncbi.nlm.nih.gov/IEB/ToolBox/CPP_DOC/lxr/source/scripts/projects/blast/LICENSE"
LABEL software.version="${BLASTPLUS_VER}"
LABEL software="BLAST+"
LABEL website="https://www.ncbi.nlm.nih.gov/books/NBK279690/"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    libncursesw5-dev \
    ca-certificates \
    build-essential \
    libreadline-dev \
    libsqlite3-dev \
    libjson-perl \
    libgdbm-dev \
    libssl-dev \
    libbz2-dev \
    libc6-dev \
    tk-dev \
    perl \
    wget \
    curl \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install BLAST+
RUN wget -q "https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && tar -xzf "ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && rm "ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && mv "ncbi-blast-${BLASTPLUS_VER}+/bin"/* /usr/local/bin/

# Install Python3
RUN wget -q "https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz" \
    && tar -xzf "Python-${PYTHON_VER}.tgz" \
    && rm "Python-${PYTHON_VER}.tgz" \
    && cd "Python-${PYTHON_VER}" \
    && ./configure \
    && make \
    && make install

RUN mkdir -p /db \
    && cd /db \
    && wget -q https://ftp.ncbi.nlm.nih.gov/blast/db/16S_ribosomal_RNA.tar.gz \
    && tar -xzf 16S_ribosomal_RNA.tar.gz

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /db/ /db/
COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir /data/
WORKDIR /data

# Run tests
FROM app as test

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
