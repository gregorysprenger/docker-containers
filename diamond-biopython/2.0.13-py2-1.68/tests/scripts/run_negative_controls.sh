#!/bin/bash

# Download test data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna -O neg_query.fna
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/proteomics/database/yeast_UPS.fasta -O neg_reference.fasta

# Create database
diamond makedb \
    --in neg_reference.fasta \
    --db neg_reference

# Run diamond
diamond blastp \
    --db neg_reference \
    --query neg_query.fna \
    --out neg_diamond.tsv \
    2> neg_diamond_stdout.txt

# Get sha256 of outputs for test data
sha256sum neg_diamond.tsv > neg_diamond.tsv.checksum