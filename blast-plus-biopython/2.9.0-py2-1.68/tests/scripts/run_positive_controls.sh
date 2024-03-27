#!/bin/bash

# Download test data
wget https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna

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
  -query e_coli_k12_16s.fna \
  -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
  -out pos_blast.tsv

# Get sha256 of outputs for test data
sha256sum pos_blast.tsv > pos_blast.tsv.checksum
