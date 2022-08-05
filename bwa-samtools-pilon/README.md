# BWA-Samtools-Pilon

This image implements:
* [BWA v0.7.17](https://github.com/lh3/bwa)
* [Samtools v1.9](https://github.com/samtools/samtools)
* [Pilon v1.23.0](https://github.com/broadinstitute/pilon)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis
Get test data:
```
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz -O R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz -O R2.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/viralrecon/genome/MN908947.3/GCA_009858895.3_ASM985889v3_genomic.200409.fna.gz -O reference.fna.gz
gunzip reference.fna.gz
```

Index and align with bwa:
```
bwa index reference.fna

bwa mem -v 2 reference.fna R1.fastq.gz R2.fastq.gz > test.sam
```

Sort and index with samtools:
```
samtools sort --reference reference.fna -l 9 -o paired.bam test.sam

samtools index paired.bam
```

Use pilon to get representative genome:
```
pilon --genome reference.fna --frags paired.bam --output "pilon"
```

## Output
```
head -2 pilon.fasta
```

```
>MN908947.3_pilon
ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAACGAACTTTAA
```