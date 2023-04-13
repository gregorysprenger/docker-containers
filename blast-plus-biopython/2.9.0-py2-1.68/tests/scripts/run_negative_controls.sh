#!/bin/bash

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/6269b99f1bbd19fb0acc74e9763688bf089db814/test_data/test_minigut_R1.fastq.gz

# Gunzip test data
gunzip test_minigut_R1.fastq.gz

# Download blast database
WORKDIR=$PWD
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
    -query test_minigut_R1.fastq \
    -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
    -out neg_blast.tsv

# Get sha256 of outputs for test data
sha256sum neg_blast.tsv > neg_blast.tsv.checksum
