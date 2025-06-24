FROM public.ecr.aws/docker/library/oraclelinux:8

RUN dnf update \
    && dnf install -y \
        curl \
        unzip \
    && dnf clean all

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && rm awscliv2.zip \
    && ./aws/install
