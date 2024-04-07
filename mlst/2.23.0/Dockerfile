ARG MLST_VER="2.23.0"
ARG BLASTPLUS_VER="2.13.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG MLST_VER
ARG BLASTPLUS_VER

LABEL base.image="ubuntu:focal"
LABEL description="Scan contig files against PubMLST typing schemes"
LABEL dockerfile.version="2.0.0"
LABEL license="https://github.com/tseemann/mlst/blob/master/LICENSE"
LABEL software.version="${MLST_VER}"
LABEL software="mlst"
LABEL website="https://github.com/tseemann/mlst"

LABEL maintainer="Curtis Kapsak"
LABEL maintainer.email="pjx8@cdc.gov"
LABEL maintainer2="Sarah Nadeau"
LABEL maintainer2.email="sarah.nadeau@bsse.ethz.ch"
LABEL maintainer3="Gregory Sprenger"


RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    liblist-moreutils-perl \
    ca-certificates \
    libjson-perl \
    libmoo-perl \
    libgomp1 \
    wget \
    gzip \
    file \
    pigz \
    && rm -rf /var/lib/apt/lists/*

# Install BLAST+ precompiled binaries
RUN wget -q "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/${BLASTPLUS_VER}/ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && tar -xzf "ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && mv "ncbi-blast-${BLASTPLUS_VER}+"/bin/* /usr/local/bin/ \
    && rm "ncbi-blast-${BLASTPLUS_VER}+-x64-linux.tar.gz" \
    && rm -rf "ncbi-blast-${BLASTPLUS_VER}+"

# Install any2fasta perl script
RUN wget -q https://raw.githubusercontent.com/tseemann/any2fasta/master/any2fasta \
    && chmod +x any2fasta \
    && mv any2fasta /usr/local/bin/

# Install mlst
RUN wget -q "https://github.com/tseemann/mlst/archive/v${MLST_VER}.tar.gz" \
    && tar -xzf "v${MLST_VER}.tar.gz" \
    && rm "v${MLST_VER}.tar.gz" \
    && cd "mlst-${MLST_VER}" \
    && mv bin/mlst /usr/local/bin \
    && mv -t /usr/local/ db/ perl5/ scripts/ test/

# check dependencies and list available schemes
RUN mlst --check \
    && mlst --list

WORKDIR /data

# Run Dockerfile
FROM ubuntu:focal as app
ARG MLST_VER
ARG BLASTPLUS_VER

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Test Dockerfile
FROM app as test
ARG MLST_VER

# Run test script
COPY test.sh .
RUN bash test.sh ${MLST_VER}
