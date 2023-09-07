#!/bin/bash

# Download test data
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz

# Positive Control
seqtk fqchk \
  test_minigut_R1.fastq.gz \
  1> pos_stdout.log \
  2> pos_stderr.log

# Extract total bp count
grep "^ALL" pos_stdout.log | awk '{print $2}' > total_bp.txt

# Get sha256sum of total_bp.txt
sha256sum total_bp.txt > total_bp.txt.checksum

# Negative Control
seqtk mergepe \
  test_minigut_R1.fastq.gz \
  1> neg_stdout.log \
  2> neg_stderr.log

# Get sha256sum of neg_stderr.log
sha256sum neg_stderr.log > neg_stderr.log.checksum
