FROM ubuntu:noble

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libffi-dev \
        libssl-dev \
        make \
        python3-full \
        python3-pip \
        sqlite3 \
        wget \
    && rm -rf /var/lib/apt/lists/*


RUN python3 -m venv /globus-cli-docker \
    && /globus-cli-docker/bin/pip3 install --no-cache-dir globus-cli

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
