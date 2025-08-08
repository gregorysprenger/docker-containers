FROM ubuntu:noble

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y \
        python3-full \
        wget \
        git \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv globus-cli-docker \
    && source globus-cli-docker/bin/activate \
    && pip install globus-cli

ENV PATH="/globus-cli-docker/bin:${PATH}"
