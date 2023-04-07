# SPAdes v3.15.3

This image implements:
- [SPAdes 3.15.3](https://github.com/ablab/spades)
- [Python 2.7.18](https://www.python.org/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv \
  --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R1.fastq.gz

wget -nv \
  --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/viralrecon/illumina/sispa/SRR11140744_R2.fastq.gz
```

Run SPAdes:

```
spades.py \
  --pe1-1 SRR11140744_R1.fastq.gz \
  --pe1-2 SRR11140744_R2.fastq.gz \
  --isolate \
  --memory 2 \
  --phred-offset 33 \
  -o results
```