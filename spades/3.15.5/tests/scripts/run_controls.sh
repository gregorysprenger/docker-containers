#!/bin/bash

# Create data directory
mkdir -p data
cd data

# Test SPAdes built in tests
spades.py --test | grep "TEST PASSED CORRECTLY" > spades_test_output.txt

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz

wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz

# Run positive control
spades.py \
  --pe1-1 SRR11140744_R1.fastq.gz \
  --pe1-2 SRR11140744_R2.fastq.gz \
  --isolate \
  --memory 2 \
  --phred-offset 33 \
  -o pos_output

# Get number of contigs
grep -c ">" pos_output/contigs.fasta > num_contigs.txt

# Get sha256 checksum for contigs
sha256sum pos_output/contigs.fasta > contigs.fasta.checksum

# Run negative control
spades.py \
  --pe1-1 SRR11140744_R1.fastq.gz \
  --pe1-2 SRR11140744_R2.fastq.gz \
  --only-error-correction \
  --isolate \
  --memory 2 \
  --phred-offset 33 \
  -o neg_output \
  1> neg_output.txt

# Get sha256 checksum for neg_spades_output.txt
sha256sum neg_output.txt > neg_output.txt.checksum
