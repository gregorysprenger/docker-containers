# Set global variables
ARG PANDAS_VER="2.2.2"
ARG XLSXWRITER_VER="3.2.0"
ARG ODSWRITER_VER="0.4.0"
ARG OPENPYXL_VER="3.1.5"
ARG ODFPY_VER="1.4.1"
ARG XLRD3_VER="1.1.0"
ARG XLWT_VER="1.3.0"

# Build Dockerfile
FROM ubuntu:jammy AS builder
ARG PANDAS_VER
ARG XLSXWRITER_VER
ARG ODSWRITER_VER
ARG OPENPYXL_VER
ARG ODFPY_VER
ARG XLRD3_VER
ARG XLWT_VER

LABEL base.image="ubuntu:jammy"
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
    python3-pip \
    libssl-dev \
    libbz2-dev \
    libffi-dev \
    zlib1g-dev\
    python3 \
    tk-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Use pip to install python dependencies
RUN pip3 install --no-cache-dir \
    pandas=="${PANDAS_VER}" \
    "pandas[excel]" \
    odswriter=="${ODSWRITER_VER}" \
    xlsxwriter=="${XLSXWRITER_VER}" \
    openpyxl=="${OPENPYXL_VER}" \
    odfpy=="${ODFPY_VER}" \
    xlrd3=="${XLRD3_VER}" \
    xlwt=="${XLWT_VER}"

# Run Dockerfile
FROM ubuntu:jammy AS app

COPY --from=builder /usr/ /usr/
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs/

WORKDIR /data
