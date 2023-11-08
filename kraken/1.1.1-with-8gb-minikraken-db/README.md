# Kraken v1.1.1 with 8GB MiniKraken database

This image implements:
- [Kraken v1.1.1](https://github.com/DerrickWood/kraken)
- [MiniKraken 8GB from 2017-10-19](http://ccb.jhu.edu/software/kraken/)
- [Jellyfish v1.1.12](https://github.com/gmarcais/Jellyfish/) (dependency for Kraken)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz
wget -nv https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz
```

Run Kraken:

```
# Set database to minikraken database
database="/kraken-database"

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

# Run kraken
kraken \
  --db ${database} \
  --threads ${NUM_CPUS} \
  --fastq-input \
  --gzip-compressed \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz \
  > kraken.output
```

Run Kraken-Report:
```
kraken-report \
  --db ${database} \
  kraken.output \
  > kraken.tab 2>&1 | tr '^M' '\n' 1>&2
```