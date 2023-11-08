# NCBI BLAST+

This image implements:

- [BLAST+ 2.15.0](https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.9.0/)
- [Python 3.8.15](https://www.python.org/ftp/python/3.8.15/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis

Get test data:

```
mkdir -p /data
cd /data

# Download test data
wget \
  https://raw.githubusercontent.com/nf-core/test-datasets/44bd1eb9292b34a78c41a423805c14b63f2da56c/data/delete_me/e_coli_k12_16s.fna
```

Download 16S rRNA DB, extract, and set BLASTDB environmental variable:

```
mkdir -p /db

update_blastdb.pl 16S_ribosomal_RNA
tar -xzf 16S_ribosomal_RNA.tar.gz -c /db
rm 16S_ribosomal_RNA.tar.gz

export BLASTDB=/db
```

Run blastn on data:

```
cd /data

blastn \
  -task blastn \
  -db 16S_ribosomal_RNA \
  -query e_coli_k12_16s.fna \
  -outfmt "6 sseqid pident length mismatch gapopen gaps ssciname" \
  -out blast.tsv
```

## Output

```
head -n 2 blast.tsv
```

```
gi|444439587|ref|NR_074902.1|	99.222	1543	10	2	2	Escherichia fergusonii ATCC 35469
gi|559795236|ref|NR_104826.1|	99.080	1522	12	2	2	Shigella sonnei
```
