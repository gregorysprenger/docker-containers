# Set global variable
ARG VSNP_VER="3.09"
ARG PYTHON_VER="3.7.13"

# Build docker image
FROM ubuntu:focal as builder
ARG VSNP_VER
ARG PYTHON_VER

LABEL base.image="ubuntu:focal"
LABEL software="vSNP3"
LABEL software.version=${VSNP_VER}
LABEL description="Dockerfile for vSNP: validate SNPs"
LABEL website="https://github.com/USDA-VS/vsnp3"
LABEL license.url="https://github.com/USDA-VS/vsnp3/blob/main/LICENSE"

ENV DEBIAN_FRONTEND=noninteractive 

# Update and install packages
RUN apt-get update -y && apt-get install -y wget

# Install miniconda
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
ENV PATH="/root/miniconda3/bin:${PATH}"

# Install bioconda
RUN conda config --add channels defaults \
    && conda config --add channels bioconda \
    && conda config --add channels conda-forge

# Install vsnp in conda environment
RUN conda create -n vsnp vsnp3=$VSNP_VER
ENV PATH="/root/miniconda3/envs/vsnp/bin:${PATH}"

FROM ubuntu:focal as app
ARG VSNP_VER

ENV DEBIAN_FRONTEND=noninteractive 

# Copy packages from builder to production image
COPY --from=builder /root/miniconda3 /root/miniconda3
COPY --from=builder /usr/local/ /usr/local/
COPY --from=builder /usr/ /usr/

# Copy path environments from builder to production image
ENV PATH="/root/miniconda3/bin:${PATH}"
ENV PATH="/root/miniconda3/envs/vsnp/bin:${PATH}"

RUN mkdir data/
WORKDIR /data

FROM app as test

# Use git for test data
RUN apt-get update && apt-get install -y git-all

# Run tests on app output
RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
