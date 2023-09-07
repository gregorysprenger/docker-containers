# KMC v3.2.2

This image implements:

- [KMC 3.2.2](https://github.com/refresh-bio/KMC)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

```
# Download test data
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz

# Create tmp output dir
mkdir -p kmc-tmp-dir

# Run KMC
kmc \
    test_minigut_R1.fastq.gz \
    pos_control \
    kmc-tmp-dir \
    1> pos_stdout.log \
    2> pos_stderr.log
```
