#!/bin/bash

# Download test data
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz

# Create tmp output dir
mkdir -p kmc-tmp-dir

# Positive Control
kmc \
    test_minigut_R1.fastq.gz \
    pos_control \
    kmc-tmp-dir \
    1> pos_stdout.log \
    2> pos_stderr.log

# Get sha256sum of pos_stderr.log
sha256sum pos_stderr.log > pos_stderr.log.checksum

# Negative Control
kmc \
    -k257 \
    test_minigut_R1.fastq.gz \
    neg_control \
    kmc-tmp-dir \
    1> neg_stdout.log \
    2> neg_stderr.log

# Get sha256sum of neg_stderr.log
sha256sum neg_stderr.log > neg_stderr.log.checksum
