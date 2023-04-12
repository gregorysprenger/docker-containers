#!/bin/bash

# Create data directory
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz

wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz

# Set database to minikraken database
database="/kraken-database"

# Make sure database exists
for ext in idx kdb; do
  if [ ! -f ${database}/database.${ext} ]; then
    echo "ERROR: pre-formatted kraken database (.${ext}) for read classification is missing" >&2
    exit 1
  fi
done

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

# Run kraken
kraken \
  --db ${database} \
  --threads ${NUM_CPUS} \
  --fastq-input \
  --gzip-compressed \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  > kraken.output

# Run kraken-report
kraken-report \
  --db ${database} \
  kraken.output \
  > kraken.tab 2>&1 | tr '^M' '\n' 1>&2

# Get checksum
sha256sum kraken.tab > kraken.tab.checksum

# Test missing --fastq-input param
kraken \
  --db ${database} \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  > kraken_missing_fastq_input_param.output \
  2> kraken_missing_fastq_input_param.txt
  