# BLAST+ and Biopython

This image implements:
- [BLAST+ 2.9.0](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
- [Biopython 1.68](https://biopython.org/)
- [Python 2.7.18](https://www.python.org/)
- [Numpy 1.16.6](https://numpy.org/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna
```

Build BLASTn 16S database:
```
update_blastdb.pl 16S_ribosomal_RNA
tar -zxvf 16S_ribosomal_RNA.tar.gz
```

Run BLASTn on e_coli data using 16S database:
```
blastn \
    -task blastn \
    -db 16S_ribosomal_RNA \
    -query e_coli_k12_16s.fna \
    -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
    -out pos_blast.tsv
```

Further analysis of BLASTn ouptut can be analyzed via Biopython.

