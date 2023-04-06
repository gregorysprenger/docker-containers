ARG MLST_VER="2.23.0"
ARG BLASTPLUS_VER="2.13.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG MLST_VER
ARG BLASTPLUS_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.0.0"
LABEL software="mlst"
LABEL software.version=${MLST_VER}
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL website="https://github.com/tseemann/mlst"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"
LABEL maintainer3="Gregory Sprenger"


RUN apt-get update && apt-get install -y wget \
  libmoo-perl \
  liblist-moreutils-perl \
  libjson-perl \
  libgomp1 \
  gzip \
  file

# get BLAST+ precompiled binaries
RUN wget ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz && \
  tar -xzf ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz && \
  rm ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz

# get any2fasta perl script
RUN cd /usr/local/bin && \
  wget https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta && \
  chmod +x any2fasta

# get mlst
RUN wget https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz &&\
  tar -xzf v${MLST_VER}.tar.gz &&\
  rm v${MLST_VER}.tar.gz

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:\
  /ncbi-blast-${BLASTPLUS_VER}+/bin" \
  LC_ALL=C

# check dependencies and list available schemes
RUN mlst --check && mlst --list

WORKDIR /data

# Run Dockerfile
FROM ubuntu:focal as app
ARG MLST_VER
ARG BLASTPLUS_VER

COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/
COPY --from=builder /mlst-${MLST_VER}/ /mlst-${MLST_VER}/
COPY --from=builder /ncbi-blast-${BLASTPLUS_VER}+/ /ncbi-blast-${BLASTPLUS_VER}+/

# set PATH and perl local settings
ENV PATH="${PATH}:/mlst-${MLST_VER}/bin:\
  /ncbi-blast-${BLASTPLUS_VER}+/bin" \
  LC_ALL=C

RUN mkdir data/
WORKDIR /data

# Test Dockerfile
FROM app as test
ARG MLST_VER

# Run test script
COPY test.sh .
RUN bash test.sh ${MLST_VER}