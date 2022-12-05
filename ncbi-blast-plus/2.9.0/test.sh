#!/bin/bash
# This script is to test that the program NCBI blast+ runs as expected

VERSION=$1

# Check version
blastx -version > version.txt
VERSION=${VERSION:="no version set"}  # ensure output doesn't match empty value if unset
if grep -q "blastx: ${VERSION}" version.txt; then
  echo "Correct version"
else
  echo "Version was unexpected:"
  blastx -version
  exit 1
fi

# Get data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna

# Download blast database
WORKDIR=$PWD
mkdir -p /db && cd /db
update_blastdb.pl 16S_ribosomal_RNA
cd $WORKDIR

# Specify database location
export BLASTDB=/db

# Run tool to find closest hits to sequence
blastn \
    -task blastn \
    -db 16S_ribosomal_RNA \
    -query e_coli_k12_16s.fna \
    -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
    -out blast.tsv

# Verify output
FILE="blast.tsv"
sha256sum $FILE > ${FILE}_sha256sum  # generate checksum
if grep -q "5c0f155a8190de9252828bd833f24308c9fdd8a3780d0732323a7844f30fcf08" ${FILE}_sha256sum ; then  # verify checksum
  echo "Correct output"
else
  echo "Output $FILE didn't match expected checksum."
  cat ${FILE}_sha256sum
  exit 1
fi