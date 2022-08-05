# Gustle

This image implements [gustle](https://github.com/supernifty/gustle) using [release version 0.2.1](https://github.com/chrisgulvik/gustle).

This docker container can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example data analysis 

Use test data from [gustle](https://github.com/supernifty/gustle/tree/master/data):

```
mkdir -p data
cd data

# Download test data
wget \
    https://raw.githubusercontent.com/supernifty/gustle/master/data/test.cgst \
    https://raw.githubusercontent.com/supernifty/gustle/master/data/test_cgst.fa \
    https://github.com/supernifty/gustle/raw/master/data/test_query.fa.gz
    
cd ../
```

Run the container to generate an index file. Output is test_query.gus

```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) gregorysprenger/gustle:v0.2.1 \
gustle index \
--cgst data/test.cgst \
--output data/test_query.gus \
data/test_query.fa.gz
```

Run the container to generate MLST. Output is written to a TSV file in the `data directory`.

```
docker run --rm -v $PWD:/data -u $(id -u):$(id -g) gregorysprenger/gustle:v0.2.1 \
gustle genotype \
--index data/test_query.gus \
data/test_cgst.fa \
> data/test_summary.tsv
```

## Output

| Filename | cgST | query1matches | query1rev | query4 | query6genome2match |
| --- | --- | --- | --- | --- | --- |
| data/test_cgst.fa | 1 (4/8) | 0 | 0 | 1 | 16 |
