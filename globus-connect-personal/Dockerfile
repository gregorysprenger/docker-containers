FROM ubuntu:noble

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        python3-full \
        python3-pip \
        tcllib \
        tk \
        wget \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN wget -q https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz \
    && tar -xzf globusconnectpersonal-latest.tgz \
    && rm globusconnectpersonal-latest.tgz \
    && mv "$(find $PWD -maxdepth 1 -mindepth 1 -type d -name 'globusconnectpersonal-*')"/* /usr/local/bin/

WORKDIR /data
