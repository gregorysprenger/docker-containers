FROM public.ecr.aws/docker/library/oraclelinux:8

RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm \
    && /usr/bin/crb enable

RUN dnf update \
    && dnf install -y \
        bzip2-libs \
        ca-certificates \
        coreutils \
        curl \
        gdb \
        ipmitool \
        perl \
        python3.12 \
        python3.12-pip \
        R \
        rsync \
        smartmontools \
        sos \
        systemd-libs \
        time \
        tree \
        unzip \
    && dnf clean all \
    && mkdir -m777 -p /var/log/dragen /var/run/dragen

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && rm awscliv2.zip \
    && ./aws/install
