#!/bin/bash

# Download test data
wget https://github.com/nf-core/test-datasets/raw/6269b99f1bbd19fb0acc74e9763688bf089db814/test_data/test_minigut_R1.fastq.gz

# Database setup
if [[ ! -d database ]]; then
  mkdir -p database
  cd database

  # Download 16S rRNA database
  update_blastdb.pl 16S_ribosomal_RNA
  tar -zxf 16S_ribosomal_RNA.tar.gz
  rm 16S_ribosomal_RNA.tar.gz
  cd ..
fi

# Specify database location
export BLASTDB=$PWD/database

# Run tool to find closest hits to sequence
blastn \
  -task blastn \
  -db 16S_ribosomal_RNA \
  -query test_minigut_R1.fastq.gz \
  -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
  -out neg_blast.tsv

# Get sha256 of outputs for test data
sha256sum neg_blast.tsv > neg_blast.tsv.checksum
