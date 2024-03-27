#!/bin/bash

# Create data directory
mkdir -p data
cd data

# Download test data
wget \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz

# Set database to minikraken database
database="/kraken2-database"

# Check for {hash,opts,taxo}.k2d files
for prefix in hash opts taxo; do
  if [ ! -f ${database}/${prefix}.k2d ]; then
    echo "ERROR: pre-formatted kraken2 database (${prefix}.k2d) for read classification is missing" >&2
    exit 1
  fi
done

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

# Run Kraken 2
kraken2 \
  --db "${database}" \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  --output /dev/null \
  --use-names \
  --report kraken2.tab \
  test_minigut_R1.fastq.gz \
  test_minigut_R2.fastq.gz

# Get checksum
sha256sum kraken2.tab > kraken2.tab.checksum

# Test Kraken 2 with missing database
kraken2 \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  --output /dev/null \
  --use-names \
  --report kraken_no_database.tab \
  test_minigut_R1.fastq.gz \
  test_minigut_R2.fastq.gz \
  2> missing_database.txt
