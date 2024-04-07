#!/bin/bash

# Download data
wget \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/804/165/GCF_002804165.1_ASM280416v1/GCF_002804165.1_ASM280416v1_genomic.fna.gz \
  -O CP024957.fna.gz
  
wget \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/024/297/125/GCF_024297125.1_ASM2429712v1/GCF_024297125.1_ASM2429712v1_genomic.fna.gz \
  -O 2BA6PG.fna.gz

##########################
#    Positive Control    #
##########################
# Run SKANI
skani dist \
  CP024957.fna.gz 2BA6PG.fna.gz \
  -o pos_output.txt

sha256sum pos_output.txt > pos_output.txt.checksum

##########################
#    Negative Control    #
##########################
# Create empty file
touch test.fna.gz

# Run SKANI
skani dist \
  test.fna.gz CP024957.fna.gz \
  2> neg_output.txt

# Select error message at end of file
tail -n 1 neg_output.txt | cut -d ')' -f 2 > neg_output.txt.error

sha256sum neg_output.txt.error > neg_output.txt.error.checksum
