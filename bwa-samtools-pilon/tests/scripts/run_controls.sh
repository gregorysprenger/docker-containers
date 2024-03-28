#!/bin/bash

# Download test data
wget \
  https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz \
  https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz

wget \
  https://github.com/nf-core/test-datasets/raw/viralrecon/genome/MN908947.3/GCA_009858895.3_ASM985889v3_genomic.200409.fna.gz \
  -O reference.fna.gz

# Create bwa index
gunzip reference.fna.gz
bwa index reference.fna

# Align PE reads
bwa mem \
  -v 2 \
  reference.fna \
  SRR11140744_R1.fastq.gz \
  SRR11140744_R2.fastq.gz \
  > test.sam

sha256sum test.sam > test.sam.checksum

# Sort and index reads
samtools sort \
  --reference reference.fna \
  -l 9 \
  -o paired.bam \
  test.sam

samtools index paired.bam

sha256sum paired.bam > paired.bam.checksum

# Get representative genome
pilon \
  --genome reference.fna \
  --frags paired.bam \
  --output "pilon"

sha256sum pilon.fasta > pilon.fasta.checksum
