#!/bin/bash

###########################
#    Positive controls    #
###########################
# Check Python3
python3 -c 'test_seq = "AGTACACTGGT"; print(test_seq)' > pos_py3.txt
sha256sum pos_py3.txt > pos_py3.txt.checksum

# Download 16S rRNA database
mkdir -p /db

update_blastdb.pl 16S_ribosomal_RNA
tar -xzf 16S_ribosomal_RNA.tar.gz -c /db
rm 16S_ribosomal_RNA.tar.gz

export BLASTDB=/db

# Download data
wget https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna

# Run blastn
blastn \
  -task blastn \
  -db 16S_ribosomal_RNA \
  -query e_coli_k12_16s.fna \
  -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
  -out pos_blast.tsv

sha256sum pos_blast.tsv > pos_blast.tsv.checksum

###########################
#    Negative Controls    #
###########################
# Check Python2
python 2> neg_py2.txt
sha256sum neg_py2.txt > neg_py2.txt.checksum

# Check if BLAST works without `-db` parameter
blastn \
  -task blastn \
  -query e_coli_k12_16s.fna \
  -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
  -out neg_blast.tsv 2> neg_blast_error.txt 

sha256sum neg_blast_error.txt > neg_blast_error.txt.checksum

# Delete BLAST database to save space
rm -rf /db