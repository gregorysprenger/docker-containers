#!/bin/bash

# Download data
wget \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/804/165/GCF_002804165.1_ASM280416v1/GCF_002804165.1_ASM280416v1_genomic.fna.gz \
  -O CP024957.fna.gz

wget \
  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/024/297/125/GCF_024297125.1_ASM2429712v1/GCF_024297125.1_ASM2429712v1_genomic.fna.gz \
  -O 2BA6PG.fna.gz

############################
#     Positive Control     #
############################
# Run fastANI and get sha256sum
fastANI \
  --ref CP024957.fna.gz \
  --query 2BA6PG.fna.gz \
  -o pos_output.txt

sha256sum pos_output.txt > pos_output.txt.checksum

##########################
#    Negative Control    #
##########################
# Create empty file
touch test.fna.gz

# Run fastANI
fastANI \
  --ref test.fna.gz \
  --query 2BA6PG.fna.gz \
  > neg_output.txt

sha256sum neg_output.txt > neg_output.txt.checksum

# Run again to get Segmentation fault error - neg_output.txt isn't created
{ sh -c 'fastANI --ref test.fna.gz --query CP024957.fna.gz -o neg_output2.txt'; } 2> neg_output_errors.txt
