#!/bin/bash

# Download test data
wget \
  https://raw.githubusercontent.com/nf-core/test-datasets/7639b3c2f9f8f5ef153598e09bb98b7aabcaea2c/general/fasta/msa/BBA0001.tfa \
  https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/proteomics/database/yeast_UPS.fasta

# Create database
diamond makedb \
  --in yeast_UPS.fasta \
  --db pos_reference

# Run diamond
diamond blastp \
  --db pos_reference \
  --query BBA0001.tfa \
  --out pos_diamond.tsv

# Get sha256 of outputs for test data
sha256sum pos_diamond.tsv > pos_diamond.tsv.checksum
