#!/bin/bash

# Create data directory
mkdir -p data
cd data

# Download test data
wget \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz
  
wget \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz

# Download and extract Kraken2 database
wget https://genome-idx.s3.amazonaws.com/kraken/k2_standard_08gb_20230605.tar.gz
mkdir /kraken2-database
tar -xzvf k2_standard_08gb_20230605.tar.gz \
  -C /kraken2-database
rm k2_standard_08gb_20230605.tar.gz

# Make sure database exists
for prefix in hash opts taxo; do
  if [ ! -f /kraken2-database/${prefix}.k2d ]; then
    echo "ERROR: pre-formatted kraken2 database (${prefix}.k2d) for read classification is missing" >&2
    exit 1
  fi
done

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

# Run Kraken 2
kraken2 \
  --db /kraken2-database \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  --output /dev/null \
  --use-names \
  --report kraken2.tab \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz

# Get checksum
sha256sum kraken2.tab > kraken2.tab.checksum

# Test Kraken 2 with missing database
kraken2 \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  --output /dev/null \
  --use-names \
  --report kraken_no_database.tab \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  2> missing_database.txt

# Delete Kraken2 database to save space
rm -rf /kraken2-database
