#!/bin/bash

# Make positive control dir and make working dir
mkdir -p pos_controls
cd pos_controls

# Download test data
wget \
  https://raw.githubusercontent.com/supernifty/gustle/master/data/test.cgst \
  https://raw.githubusercontent.com/supernifty/gustle/master/data/test_cgst.fa \
  https://github.com/supernifty/gustle/raw/master/data/test_query.fa.gz

# Run gustle index on test data
gustle index \
  --cgst test.cgst \
  --output test_query.gus \
  test_query.fa.gz

# Run gustle genotype on test data
gustle genotype \
  --index test_query.gus \
  test_cgst.fa \
  > test_summary.tsv


# Get sha256sum of outputs for test data
# test_query.gus gives different sha256 on each run, using cgst data file instead
sha256sum test.cgst > test.cgst.checksum
sha256sum test_summary.tsv > test_summary.tsv.checksum

cd ../