#!/bin/bash

# Create data directory
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz

# Positive control check
skesa --gz \
  --use_paired_ends \
  --contigs_out pos_contigs.fasta \
  --fastq SRR11140744_R1.fastq.gz,SRR11140744_R2.fastq.gz

sha256sum pos_contigs.fasta >pos_contigs.fasta.checksum

# Negative control check
# --sra_run is not available on this image due to Makefile.nongs
skesa --gz \
  --use_paired_ends \
  --contigs_out neg_contigs.fasta \
  --sra_run SRR11140744 \
  2>log.txt

# Get last item in log file
tail -n 1 log.txt >neg_control.txt
