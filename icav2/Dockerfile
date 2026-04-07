ARG ICAV2_VERSION="2.44.0"

FROM ubuntu:noble
ARG ICAV2_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/*
    
RUN wget -q "https://stratus-documentation-us-east-1-public.s3.amazonaws.com/cli/${ICAV2_VERSION}/ica-linux-amd64.zip" \
    "https://stratus-documentation-us-east-1-public.s3.amazonaws.com/cli/${ICAV2_VERSION}/ica-linux-amd64.sha256" \
    && sed 's|target/||g' ica-linux-amd64.sha256 | sha256sum -c - \
    && unzip -q ica-linux-amd64.zip \
    && mv linux-amd64/icav2 /usr/local/bin/icav2 \
    && chmod +x /usr/local/bin/icav2 \
    && rm -rf ica-linux-amd64.zip ica-linux-amd64.sha256 linux-amd64
    
WORKDIR /data