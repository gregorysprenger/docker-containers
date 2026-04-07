ARG AWS_VERSION="2.34.25"
ARG ICAV2_VERSION="2.44.0"
ARG RCLONE_VERSION="1.73.3"


FROM ubuntu:noble
ARG AWS_VERSION
ARG ICAV2_VERSION
ARG RCLONE_VERSION

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        golang-go \
        jq \
        unzip \
        wget \
    && rm -rf /var/lib/apt/lists/*

# Install ICAv2 CLI
RUN wget -q "https://stratus-documentation-us-east-1-public.s3.amazonaws.com/cli/${ICAV2_VERSION}/ica-linux-amd64.zip" \
    "https://stratus-documentation-us-east-1-public.s3.amazonaws.com/cli/${ICAV2_VERSION}/ica-linux-amd64.sha256" \
    && sed 's|target/||g' ica-linux-amd64.sha256 | sha256sum -c - \
    && unzip -q ica-linux-amd64.zip \
    && mv linux-amd64/icav2 /usr/local/bin/icav2 \
    && chmod +x /usr/local/bin/icav2 \
    && rm -rf ica-linux-amd64.zip ica-linux-amd64.sha256 linux-amd64

# Install AWS CLI
RUN wget -q "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-${AWS_VERSION}.zip" -O "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install \
    && rm -rf awscliv2.zip aws

# Install rclone
RUN wget -q "https://github.com/rclone/rclone/releases/download/v${RCLONE_VERSION}/rclone-v${RCLONE_VERSION}.tar.gz" \
    && tar -xzf "rclone-v${RCLONE_VERSION}.tar.gz" \
    && rm "rclone-v${RCLONE_VERSION}.tar.gz" \
    && cd "rclone-v${RCLONE_VERSION}" \
    && go build \
    && mv rclone /usr/local/bin
    
WORKDIR /data