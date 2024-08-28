# Global variables
ARG HAPPY_VER="v0.3.15"
ARG BXPYTHON_VER="0.8.8"
ARG CYTHON_VER="0.29.37"
ARG PYSAM_VER="0.20.0"
ARG ANT_VER="1.9.7"

FROM ubuntu:jammy
ARG HAPPY_VER
ARG BXPYTHON_VER
ARG CYTHON_VER
ARG PYSAM_VER
ARG ANT_VER

LABEL base.image="ubuntu:jammy"
LABEL description="Haplotype VCF comparison tools"
LABEL dockerfile.version="${HAPPY_VER}"
LABEL license.url="https://github.com/Illumina/hap.py/blob/master/LICENSE.txt"
LABEL software.version="${HAPPY_VER}"
LABEL software="hap.py"
LABEL website="https://github.com/Illumina/hap.py"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install Ubuntu packages
## Requires python 2.7
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends -y \
    software-properties-common \
    libboost-all-dev \
    build-essential \
    ca-certificates \
    openjdk-8-jdk \
    python2-dev \
    liblzma-dev \
    libbz2-dev \
    zlib1g-dev \
    pkg-config \
    autoconf \
    cmake \
    bzip2 \
    wget \
    ant \
    git \
    && ln -s /usr/bin/python2 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Install python2.7 pip and python packages
RUN wget -q "https://bootstrap.pypa.io/pip/2.7/get-pip.py" \
    && python get-pip.py \
    && pip install --no-cache-dir \
    bx-python=="${BXPYTHON_VER}" \
    cython=="${CYTHON_VER}" \
    pysam=="${PYSAM_VER}" \
    setuptools \
    pybedtools \
    pandas \
    psutil \
    numpy \
    scipy \
    nose

# Install hap.py
WORKDIR /opt/hap.py-source
RUN wget -q "https://github.com/Illumina/hap.py/archive/refs/tags/${HAPPY_VER}.tar.gz" \
    && tar -xzf "${HAPPY_VER}.tar.gz" --strip-components 1\
    && rm "${HAPPY_VER}.tar.gz" \
    && sed -i '1i #include <limits>' src/c++/lib/tools/Roc.cpp \
    && sed -i \
        's|RESULT_ALLDTYPES\[i\], raise_on_error=False)|RESULT_ALLDTYPES\[i\], raise_on_error=False, errors="ignore")|g' \
        src/python/Haplo/happyroc.py \
    && python install.py /opt/hap.py --with-rtgtools --no-tests \
    # Set all python shebang lines to python2 \
    && find /opt/hap.py \
        -type f \
        -name "*.py" \
        -exec sed -i 's|/usr/bin/python$|/usr/bin/env python2|g' "{}" \; \
    && chmod -R 777 /opt/

WORKDIR /data
ENV PATH=$PATH:/opt/hap.py/bin
