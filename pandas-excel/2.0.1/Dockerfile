# Set global variables
ARG PYTHON_VER="3.11.3"
ARG PANDAS_VER="2.0.1"
ARG OPENPYXL_VER="3.1.2"
ARG XLRD3_VER="1.1.0"
ARG ODFPY_VER="1.4.1"
ARG ODSWRITER_VER="0.4.0"
ARG XLWT_VER="1.3.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG PYTHON_VER
ARG PANDAS_VER
ARG OPENPYXL_VER
ARG XLRD3_VER
ARG ODFPY_VER
ARG ODSWRITER_VER
ARG XLWT_VER

LABEL base.image="ubuntu:focal"
LABEL dockerfile.version="2.0.1"
LABEL software="pandas"
LABEL software.version=${PANDAS_VER}
LABEL description="pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language."
LABEL website="https://pandas.pydata.org/"
LABEL license.url="https://github.com/pandas-dev/pandas/blob/main/LICENSE"
LABEL maintainer="Gregory Sprenger"

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    build-essential \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libgdbm-dev \
    libssl-dev \
    libbz2-dev \
    zlib1g-dev\
    libffi-dev \
    tk-dev \
    curl \
    wget

# Install Python 3
RUN wget https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz && \
    tar -zxvf Python-${PYTHON_VER}.tgz && \
    cd Python-${PYTHON_VER} && \
    ./configure && \
    make && make install

RUN pip3 install \
    pandas==${PANDAS_VER} \
    pandas[excel] \
    odswriter==${ODSWRITER_VER} \
    openpyxl==${OPENPYXL_VER} \
    odfpy==${ODFPY_VER} \
    xlrd3==${XLRD3_VER} \
    xlwt==${XLWT_VER}

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/

RUN mkdir data/
WORKDIR /data

FROM builder as test

RUN apt-get update

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests