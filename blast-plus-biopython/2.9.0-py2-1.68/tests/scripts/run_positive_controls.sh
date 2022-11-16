#!/bin/bash

# Set WORKDIR
WORKDIR=$PWD

# # Run biopython built-in tests
# cd /biopython-*/Tests
# python run_tests.py
# cd $WORK

# Download test data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna

# Download blast database
mkdir -p /db && cd /db
update_blastdb.pl 16S_ribosomal_RNA
tar -zxvf 16S_ribosomal_RNA.tar.gz
cd $WORKDIR

# Specify database location
export BLASTDB=/db

# Run tool to find closest hits to sequence
blastn \
    -task blastn \
    -db 16S_ribosomal_RNA \
    -query e_coli_k12_16s.fna \
    -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
    -out pos_blast.tsv

# Get sha256 of outputs for test data
sha256sum pos_blast.tsv > pos_blast.tsv.checksum
