# SKESA 2.4.0

This image implements:
- [SKESA 2.4.0](https://github.com/ncbi/SKESA)
- [Boost 1.72.0 (dependency for SKESA)](https://www.boost.org/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz
```

Run SKESA:

```
skesa --gz \
  --use_paired_ends \
  --contigs_out pos_contigs.fasta \
  --fastq SRR11140744_R1.fastq.gz,SRR11140744_R2.fastq.gz
```

## NOTE

This image is built using `Makefile.nongs` and therefore cannot pull data from SRA.