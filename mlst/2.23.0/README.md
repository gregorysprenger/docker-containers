# MLST 2.23.0

This image implements:
- [MLST 2.23.0](https://github.com/tseemann/mlst/)
- [BLAST+ 2.13.0](https://www.ncbi.nlm.nih.gov/books/NBK279690/)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

Get test data:

```
mkdir -p data
cd data

# Download test data
wget -nv https://github.com/nf-core/test-datasets/raw/bactmap/genome/NCTC13799.fna
```

Run MLST:
```
mlst NCTC13799.fna > mlst-results.tsv
```

