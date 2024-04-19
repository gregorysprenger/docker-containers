FROM ubuntu:jammy
ARG AWS_VERSION="2.15.39"

LABEL base.image="ubuntu:jammy"
LABEL description="AWS CLI docker image"
LABEL dockerfile.version="1.0.0"
LABEL software="AWS CLI"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install