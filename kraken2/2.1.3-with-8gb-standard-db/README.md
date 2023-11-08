# Kraken v2.1.3 with Standard 8GB database

This image implements:
- [Kraken 2 v2.1.3](https://github.com/DerrickWood/kraken2)
- [Standard 8gb database](https://benlangmead.github.io/aws-indexes/k2)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get data:
```
# Create data directory
mkdir -p data
cd data

# Download test data
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz
  
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R2.fastq.gz
```

Set database, get CPUs, and run Kraken 2:
```
# Set database to minikraken database
database="/kraken2-database"

# Get number of CPUs
NUM_CPUS=$(grep "processor" /proc/cpuinfo | wc -l)

kraken2 \
  --db "${database}" \
  --threads ${NUM_CPUS} \
  --gzip-compressed \
  --output /dev/null \
  --use-names \
  --report kraken2.tab \
  test_minigut_R1.fastq.gz test_minigut_R2.fastq.gz
```