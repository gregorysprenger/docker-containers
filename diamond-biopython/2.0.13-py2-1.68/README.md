# Diamond-Biopython

This image implements:
- [Diamond v2.0.13](https://github.com/bbuchfink/diamond)
- [Python 2.7.18](https://www.python.org/downloads/release/python-2718/)
- [Biopython 1.68](https://github.com/biopython/biopython)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/7639b3c2f9f8f5ef153598e09bb98b7aabcaea2c/general/fasta/msa/BBA0001.tfa -O query.fasta
wget -nv https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/proteomics/database/yeast_UPS.fasta -O reference.fasta
```

Create database from reference data:

```
diamond makedb \
    --in reference.fasta \
    --db reference
```

Run diamond to compare query to reference:

```
diamond blastp \
    --db reference \
    --query query.fasta \
    --out diamond.tsv
```
