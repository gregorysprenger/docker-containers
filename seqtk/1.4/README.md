# Seqtk v1.4

This image implements:

- [Seqtk v1.4](https://github.com/lh3/seqtk)

and can be accessed at [docker hub](https://hub.docker.com/u/gregorysprenger).

## Example analysis:

```
# Download test data
wget -nv --no-check-certificate \
  https://github.com/nf-core/test-datasets/raw/mag/test_data/test_minigut_R1.fastq.gz

# Run Seqtk
seqtk fqchk \
  test_minigut_R1.fastq.gz \
  1> stdout.log \
  2> stderr.log

# Extract total bp count
grep "^ALL" stdout.log | awk '{print $2}' > total_bp.txt
```
