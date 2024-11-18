# Global variables
ARG NXF_VER="24.10.0"

FROM ubuntu:noble
ARG NXF_VER

LABEL base.image="ubuntu:noble"
LABEL description="Nextflow"
LABEL dockerfile.version="${NXF_VER}"
LABEL software="Nextflow"
LABEL maintainer="Gregory Sprenger"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    zip \
    curl \
    wget \
    unzip \
    default-jdk \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /data

# Install Nextflow
RUN curl -sLO "https://github.com/nextflow-io/nextflow/releases/download/v${NXF_VER}/nextflow-${NXF_VER}-dist" \
    && chmod +x "nextflow-${NXF_VER}-dist" \
    && mv "nextflow-${NXF_VER}-dist" /usr/local/bin/nextflow
