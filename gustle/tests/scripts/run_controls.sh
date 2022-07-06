#!/bin/bash


mkdir -p data
cd data

# Download test data
wget \
    https://raw.githubusercontent.com/supernifty/gustle/master/data/test.cgst \
    https://raw.githubusercontent.com/supernifty/gustle/master/data/test_cgst.fa \
    https://github.com/supernifty/gustle/raw/master/data/test_query.fa.gz

cd ../

# Run gustle with test data
gustle index --cgst data/test.cgst --output data/test_query.gus data/test_query.fa.gz
gustle genotype --index data/test_query.gus data/test_cgst.fa > data/test_summary.tsv


# Get sha256sum of outputs for testing
# test_query.gus gives different sha256 on each run, using cgst data file instead
sha256sum data/test.cgst > data/test.cgst.checksum
sha256sum data/test_summary.tsv > data/test_summary.tsv.checksum
