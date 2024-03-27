# Set global variables
ARG BWA_VER="0.7.17"
ARG SAMTOOLS_VER="1.9"
ARG PILON_VER="1.23"

FROM ubuntu:focal as builder
ARG BWA_VER
ARG SAMTOOLS_VER
ARG PILON_VER

LABEL base.image="ubuntu:focal"
LABEL description="Dockerfile for bwa, samtools, and pilon"
LABEL software.version="1.0.0"
LABEL software="bwa-samtools-pilon"
LABEL maintainer="Gregory Sprenger"

# Update and install packages
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    libcurl4-gnutls-dev \
    libncurses5-dev \
    ca-certificates \
    openjdk-11-jre \
    liblzma-dev \
    zlib1g-dev \
    libbz2-dev \
    libssl-dev \
    bzip2 \
    wget \
    make \
    perl \
    gcc \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# Install BWA
RUN wget -q https://github.com/lh3/bwa/releases/download/v${BWA_VER}/bwa-${BWA_VER}.tar.bz2 \
    && tar -xjf bwa-${BWA_VER}.tar.bz2 \
    && rm bwa-${BWA_VER}.tar.bz2 \
    && cd bwa-${BWA_VER} \
    && make \
    && mv bwa /usr/local/bin

# Install samtools
RUN wget -q https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VER}/samtools-${SAMTOOLS_VER}.tar.bz2 \
    && tar -xjf samtools-${SAMTOOLS_VER}.tar.bz2 \
    && rm samtools-${SAMTOOLS_VER}.tar.bz2 \
    && cd samtools-${SAMTOOLS_VER} \
    && ./configure \
    && make \
    && make install

# Install Pilon
RUN wget -q https://github.com/broadinstitute/pilon/releases/download/v${PILON_VER}/pilon-${PILON_VER}.jar \
    && chmod +x pilon-${PILON_VER}.jar \
    && echo "#!/bin/bash" >> pilon \
    && echo "exec java -jar /pilon/pilon-${PILON_VER}.jar """"$""@"""" " >> pilon \
    && chmod +x pilon \
    && mv pilon /usr/local/bin/ \
    && mv pilon-${PILON_VER}.jar /usr/local/bin/

FROM ubuntu:focal as app

COPY --from=builder /usr/local/ /usr/local/

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

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
