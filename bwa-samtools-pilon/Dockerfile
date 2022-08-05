# Set global variables
ARG BWA_VER="0.7.17"
ARG SAMTOOLS_VER="1.9"
ARG PILON_VER="1.23"

FROM ubuntu:focal as builder
ARG BWA_VER
ARG SAMTOOLS_VER
ARG PILON_VER

LABEL base.image="ubuntu:focal"
LABEL software="bwa-samtools-pilon"
LABEL software.version="1.0.0"
LABEL description="Dockerfile for bwa, samtools, and pilon"

ENV DEBIAN_FRONTEND=noninteractive 

# Update and install packages
RUN apt-get update -y && apt-get install -y \
    wget \
    make \
    gcc \
    zlib1g-dev \
    bzip2 \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    perl \
    openjdk-11-jre

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# BWA 
RUN mkdir bwa && \
  mkdir /data && \
  cd bwa && \
  wget https://github.com/lh3/bwa/releases/download/v$BWA_VER/bwa-$BWA_VER.tar.bz2 && \
  tar -xjf bwa-$BWA_VER.tar.bz2 && \
  rm bwa-$BWA_VER.tar.bz2 && \
  cd bwa-$BWA_VER && \
  make

ENV PATH="${PATH}:/bwa/bwa-$BWA_VER"

# Samtools
RUN mkdir samtools && \
  cd samtools && \
  wget https://github.com/samtools/samtools/releases/download/$SAMTOOLS_VER/samtools-$SAMTOOLS_VER.tar.bz2 && \
  tar -xjf samtools-$SAMTOOLS_VER.tar.bz2 && \
  rm samtools-$SAMTOOLS_VER.tar.bz2 && \
  cd samtools-$SAMTOOLS_VER && \
  ./configure && \
  make && \
  make install

# Pilon
RUN mkdir pilon && \
  cd pilon && \
  wget https://github.com/broadinstitute/pilon/releases/download/v$PILON_VER/pilon-$PILON_VER.jar && \
  chmod +x pilon-$PILON_VER.jar && \
  echo "#!/bin/bash" >> pilon && \
  echo "exec java -jar /pilon/pilon-$PILON_VER.jar """"$""@"""" " >> pilon && \
  chmod +x pilon

ENV PATH="${PATH}:/pilon"

FROM ubuntu:focal as app
ARG BWA_VER
ARG SAMTOOLS_VER
ARG PILON_VER

COPY --from=builder /bwa/ /bwa/
COPY --from=builder /samtools/ /samtools/
COPY --from=builder /pilon/ /pilon/
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${PATH}:${JAVA_HOME}/bin"
ENV PATH="${PATH}:/bwa/bwa-$BWA_VER"
ENV PATH="${PATH}:/pilon"

RUN mkdir data/
WORKDIR /data

FROM app as test

RUN apt-get update && apt-get install -y \
    python3 \
    wget

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
