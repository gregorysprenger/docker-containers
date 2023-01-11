#!/bin/bash

# Set WORKDIR
WORKDIR=$PWD

# # Run biopython built-in tests
# cd /biopython-*/Tests
# python run_tests.py
# cd $WORK

# Download test data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/7639b3c2f9f8f5ef153598e09bb98b7aabcaea2c/general/fasta/msa/BBA0001.tfa -O pos_query.fasta
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/proteomics/database/yeast_UPS.fasta -O pos_reference.fasta

# Create database
diamond makedb \
    --in pos_reference.fasta \
    --db pos_reference

# Run diamond
diamond blastp \
    --db pos_reference \
    --query pos_query.fasta \
    --out pos_diamond.tsv

# Get sha256 of outputs for test data
sha256sum pos_diamond.tsv > pos_diamond.tsv.checksum
