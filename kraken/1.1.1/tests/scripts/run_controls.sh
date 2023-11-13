#!/bin/bash

# Download test data
wget \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz
wget \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz

# Download and extract MiniKraken database
wget http://ccb.jhu.edu/software/kraken/dl/minikraken_20171019_4GB.tgz
mkdir /kraken-database
tar -xzvf minikraken_20171019_4GB.tgz \
  -C /kraken-database \
  --strip-components 1
rm minikraken_20171019_4GB.tgz

# Make sure database exists
for ext in idx kdb; do
  if [ ! -f /kraken-database/database.${ext} ]; then
    echo "ERROR: Pre-formatted kraken database file `database.${ext}` for read classification is missing" >&2
    exit 1
  fi
done

for file in names nodes; do
  if [ ! -f /kraken-database/taxonomy/${file}.dmp ]; then
    echo "ERROR: Pre-formatted taxonomy information file `taxonomy/$file.dmp` is missing" >&2
    exit 1
  fi
done

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

# Run kraken
kraken \
  --db /kraken-database \
  --threads ${NUM_CPUS} \
  --fastq-input \
  --gzip-compressed \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  > kraken.output

# Run kraken-report
kraken-report \
  --db /kraken-database \
  kraken.output \
  > kraken.tab 2>&1 | tr '^M' '\n' 1>&2

# Get checksum
sha256sum kraken.tab > kraken.tab.checksum

# Test missing --fastq-input param
kraken \
  --db /kraken-database \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  > kraken_missing_fastq_input_param.output \
  2> kraken_missing_fastq_input_param.txt

# # Delete Kraken database to save space
rm -rf /kraken-database
