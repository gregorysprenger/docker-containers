# Set global variables
ARG ODFPY_VER="1.4.1"
ARG ODSWRITER_VER="0.4.0"
ARG OPENPYXL_VER="3.1.2"
ARG PANDAS_VER="2.0.1"
ARG PYTHON_VER="3.11.3"
ARG XLRD3_VER="1.1.0"
ARG XLWT_VER="1.3.0"

# Build Dockerfile
FROM ubuntu:focal as builder
ARG ODFPY_VER
ARG ODSWRITER_VER
ARG OPENPYXL_VER
ARG PANDAS_VER
ARG PYTHON_VER
ARG XLRD3_VER
ARG XLWT_VER

LABEL base.image="ubuntu:focal"
LABEL description="pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language."
LABEL dockerfile.version="${PANDAS_VER}"
LABEL license.url="https://github.com/pandas-dev/pandas/blob/main/LICENSE"
LABEL software.version="${PANDAS_VER}"
LABEL software="pandas"
LABEL website="https://pandas.pydata.org/"
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
    libgdbm-dev \
    libssl-dev \
    libbz2-dev \
    libffi-dev \
    zlib1g-dev\
    tk-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3
RUN wget -q "https://www.python.org/ftp/python/${PYTHON_VER}/Python-${PYTHON_VER}.tgz" \
    && tar -xzf "Python-${PYTHON_VER}.tgz" \
    && rm "Python-${PYTHON_VER}.tgz" \
    && cd "Python-${PYTHON_VER}" \
    && ./configure \
    && make \
    && make install

# Use pip to install python dependencies
RUN pip3 install --no-cache-dir \
    pandas=="${PANDAS_VER}" \
    "pandas[excel]" \
    odswriter=="${ODSWRITER_VER}" \
    openpyxl=="${OPENPYXL_VER}" \
    odfpy=="${ODFPY_VER}" \
    xlrd3=="${XLRD3_VER}" \
    xlwt=="${XLWT_VER}"

# Run Dockerfile
FROM ubuntu:focal as app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

RUN mkdir data/
WORKDIR /data

# Run tests
FROM builder as test

RUN mkdir ../tests/
COPY tests/ ../tests/
RUN python3 -m unittest discover -v -s ../tests
